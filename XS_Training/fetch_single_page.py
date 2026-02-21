"""Fetch a single web page and save it as Markdown.

Usage:
  py XS_Training\fetch_single_page.py --url <URL> --out <output.md>
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as html_to_md


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def fetch_as_markdown(url: str) -> str:
    session = requests.Session()
    session.headers.update({"User-Agent": "AoE2_AI_Modder XS_Training fetcher"})
    response = session.get(url, timeout=40)
    response.raise_for_status()

    text = response.text
    ctype = response.headers.get("content-type", "").lower()

    if "text/plain" in ctype or "action=raw" in url:
        md = text.strip()
    else:
        soup = BeautifulSoup(text, "html.parser")

        # Prefer the content body when available, fallback to full page.
        content = soup.find(id="mw-content-text")
        source_html = str(content) if content is not None else text
        md = html_to_md(source_html, heading_style="ATX").strip()

    header = (
        "---\n"
        f"source_url: {url}\n"
        f"fetched_at: {utc_now_iso()}\n"
        "---\n\n"
    )
    return header + md + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(fetch_as_markdown(args.url), encoding="utf-8")
    print(str(out_path.resolve()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
