"""Fetch and save XS documentation pages as Markdown.

Targets:
- https://ugc.aoe2.rocks/general/xs/ (crawl within /general/xs/)
- https://github.com/Divy1211/AoE2DE_UGC_Guide (clone + copy markdown sources)

Outputs (under XS_Training/):
- ugc.aoe2.rocks/.../*.md  (one file per crawled page)
- github.com/Divy1211/AoE2DE_UGC_Guide/.../*.md (one file per markdown source)
- manifest.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urljoin, urlparse, urlunparse


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _norm_url(url: str) -> str:
    """Normalize URL for crawl de-duplication.

    - drops fragment
    - drops query
    - ensures https scheme
    """

    p = urlparse(url)
    scheme = "https"
    path = p.path or "/"
    # normalize trailing slash for directory-like paths
    if not os.path.splitext(path)[1] and not path.endswith("/"):
        path = path + "/"
    return urlunparse((scheme, p.netloc, path, "", "", ""))


def _safe_relpath_from_url(url: str) -> Path:
    """Turn a URL into a relative output path.

    Example:
      https://ugc.aoe2.rocks/general/xs/beginner/ ->
      ugc.aoe2.rocks/general/xs/beginner/index.md
    """

    p = urlparse(url)
    parts = [p.netloc] + [seg for seg in p.path.split("/") if seg]
    # Always write as a directory with index.md to avoid filename collisions.
    out_dir = Path(*parts)
    return out_dir / "index.md"


def _sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()


def _write_text_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8", errors="replace")
    tmp.replace(path)


def _try_import_deps() -> tuple[Any, tuple[Any, Any]]:
    try:
        import requests  # type: ignore
    except Exception as e:  # pragma: no cover
        raise RuntimeError(
            "Missing dependency 'requests'. Install with: python -m pip install requests"
        ) from e

    try:
        from bs4 import BeautifulSoup  # type: ignore
    except Exception as e:  # pragma: no cover
        raise RuntimeError(
            "Missing dependency 'beautifulsoup4'. Install with: python -m pip install beautifulsoup4"
        ) from e

    try:
        from markdownify import markdownify as html_to_md  # type: ignore
    except Exception as e:  # pragma: no cover
        raise RuntimeError(
            "Missing dependency 'markdownify'. Install with: python -m pip install markdownify"
        ) from e

    return requests, (BeautifulSoup, html_to_md)


@dataclass(frozen=True)
class SavedPage:
    source_url: str
    output_path: str
    sha256: str
    fetched_at: str


def crawl_ugc_xs(out_root: Path, *, delay_s: float = 0.1, max_pages: int | None = None) -> list[SavedPage]:
    """Crawl within https://ugc.aoe2.rocks/general/xs/ and save each page to .md."""

    requests, (BeautifulSoup, html_to_md) = _try_import_deps()

    seed = "https://ugc.aoe2.rocks/general/xs/"
    allowed_host = "ugc.aoe2.rocks"
    allowed_prefix = "/general/xs/"

    queue: list[str] = [_norm_url(seed)]
    seen: set[str] = set()
    saved: list[SavedPage] = []

    session = requests.Session()
    session.headers.update({"User-Agent": "AoE2_AI_Modder XS_Training fetcher"})

    while queue:
        if max_pages is not None and len(saved) >= max_pages:
            break

        url = queue.pop(0)
        if url in seen:
            continue
        seen.add(url)

        p = urlparse(url)
        if p.netloc != allowed_host:
            continue
        if not p.path.startswith(allowed_prefix):
            continue

        resp = session.get(url, timeout=30)
        if resp.status_code != 200:
            continue
        ctype = resp.headers.get("content-type", "")
        if "text/html" not in ctype:
            continue

        html = resp.text
        soup = BeautifulSoup(html, "html.parser")

        # Crawl links.
        for a in soup.select("a[href]"):
            href = a.get("href")
            if not href:
                continue
            abs_url = _norm_url(urljoin(url, href))
            ap = urlparse(abs_url)
            if ap.netloc == allowed_host and ap.path.startswith(allowed_prefix):
                if abs_url not in seen:
                    queue.append(abs_url)

        # Convert HTML to Markdown.
        body_md = html_to_md(html, heading_style="ATX")
        body_md = body_md.strip() + "\n"

        fetched_at = _utc_now_iso()
        header = (
            f"---\nsource_url: {url}\nfetched_at: {fetched_at}\n---\n\n"
        )
        md = header + body_md

        rel = _safe_relpath_from_url(url)
        out_path = out_root / rel
        _write_text_atomic(out_path, md)

        saved.append(
            SavedPage(
                source_url=url,
                output_path=str(out_path.relative_to(out_root)).replace("\\", "/"),
                sha256=_sha256_text(md),
                fetched_at=fetched_at,
            )
        )

        time.sleep(delay_s)

    return saved


def _run_git(args: list[str], *, cwd: Path) -> None:
    proc = subprocess.run(
        ["git"] + args,
        cwd=str(cwd),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if proc.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed:\n{proc.stdout}")


def copy_github_markdown(out_root: Path, *, repo_url: str) -> list[SavedPage]:
    """Clone repo and copy its markdown files into out_root."""

    parsed = urlparse(repo_url)
    if parsed.netloc.lower() != "github.com":
        raise ValueError("repo_url must be a github.com URL")

    # Normalize repo path: /owner/name
    repo_path = parsed.path.strip("/")
    if repo_path.endswith(".git"):
        repo_path = repo_path[:-4]
    parts = repo_path.split("/")
    if len(parts) < 2:
        raise ValueError("repo_url must include owner/repo")
    owner, name = parts[0], parts[1]

    tmp_root = out_root / "_sources"
    clone_dir = tmp_root / f"{owner}__{name}"
    tmp_root.mkdir(parents=True, exist_ok=True)

    if not clone_dir.exists():
        _run_git(["clone", "--depth", "1", repo_url, str(clone_dir)], cwd=tmp_root)
    else:
        # Best-effort update.
        _run_git(["fetch", "--depth", "1", "origin"], cwd=clone_dir)
        _run_git(["reset", "--hard", "origin/HEAD"], cwd=clone_dir)

    # Find markdown files.
    md_exts = {".md", ".markdown"}
    saved: list[SavedPage] = []
    fetched_at = _utc_now_iso()

    for path in clone_dir.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in md_exts:
            continue
        # Skip the cloned repo's .git files (in case rglob hits them).
        if ".git" in path.parts:
            continue

        rel_in_repo = path.relative_to(clone_dir)
        out_path = out_root / "github.com" / owner / name / rel_in_repo
        out_path.parent.mkdir(parents=True, exist_ok=True)
        text = path.read_text(encoding="utf-8", errors="replace")
        _write_text_atomic(out_path, text)
        saved.append(
            SavedPage(
                source_url=f"{repo_url}/blob/HEAD/{rel_in_repo.as_posix()}",
                output_path=str(out_path.relative_to(out_root)).replace("\\", "/"),
                sha256=_sha256_text(text),
                fetched_at=fetched_at,
            )
        )

    # Don't delete clone_dir; it serves as a local cache.
    return saved


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--out-root",
        default=str(Path(__file__).resolve().parent),
        help="Output root directory (default: XS_Training/)",
    )
    ap.add_argument("--ugc-delay-s", type=float, default=0.1)
    ap.add_argument("--ugc-max-pages", type=int, default=0)
    ap.add_argument(
        "--github-repo",
        default="https://github.com/Divy1211/AoE2DE_UGC_Guide",
    )
    ns = ap.parse_args(argv)

    out_root = Path(ns.out_root).resolve()
    out_root.mkdir(parents=True, exist_ok=True)

    ugc_max = None if ns.ugc_max_pages <= 0 else ns.ugc_max_pages

    manifest = {
        "generated_at": _utc_now_iso(),
        "ugc": {
            "seed": "https://ugc.aoe2.rocks/general/xs/",
            "scope": "host=ugc.aoe2.rocks path_prefix=/general/xs/",
            "saved": [],
        },
        "github": {
            "repo": ns.github_repo,
            "saved": [],
        },
    }

    ugc_saved = crawl_ugc_xs(out_root, delay_s=ns.ugc_delay_s, max_pages=ugc_max)
    manifest["ugc"]["saved"] = [sp.__dict__ for sp in ugc_saved]

    gh_saved = copy_github_markdown(out_root, repo_url=ns.github_repo)
    manifest["github"]["saved"] = [sp.__dict__ for sp in gh_saved]

    _write_text_atomic(out_root / "manifest.json", json.dumps(manifest, indent=2, sort_keys=True) + "\n")

    # Human-readable full index.
    lines: list[str] = []
    lines.append("# XS Training Source Index")
    lines.append("")
    lines.append(f"Generated at: {manifest['generated_at']}")
    lines.append("")
    lines.append("## UGC website pages")
    lines.append(f"- Seed: {manifest['ugc']['seed']}")
    lines.append(f"- Scope: {manifest['ugc']['scope']}")
    lines.append(f"- Count: {len(ugc_saved)}")
    lines.append("")
    for sp in sorted(ugc_saved, key=lambda x: x.output_path):
        lines.append(f"- `{sp.output_path}` <- {sp.source_url}")

    lines.append("")
    lines.append("## GitHub Markdown files")
    lines.append(f"- Repository: {manifest['github']['repo']}")
    lines.append(f"- Count: {len(gh_saved)}")
    lines.append("")
    for sp in sorted(gh_saved, key=lambda x: x.output_path):
        lines.append(f"- `{sp.output_path}` <- {sp.source_url}")

    lines.append("")
    lines.append("## Notes")
    lines.append("- `manifest.json` contains full metadata and SHA-256 per saved file.")
    lines.append("- `_sources/` is a local cache clone for reproducible re-fetches.")
    lines.append("")
    _write_text_atomic(out_root / "SOURCE_PAGE_INDEX.md", "\n".join(lines))

    print(f"UGC pages saved: {len(ugc_saved)}")
    print(f"GitHub markdown files saved: {len(gh_saved)}")
    print(f"Manifest: {out_root / 'manifest.json'}")
    print(f"Index: {out_root / 'SOURCE_PAGE_INDEX.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
