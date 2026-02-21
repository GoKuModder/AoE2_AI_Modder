#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ast
import fnmatch
import json
import sys
from pathlib import Path
from typing import Any


def load_contract(contract_path: Path) -> dict[str, Any]:
    return json.loads(contract_path.read_text(encoding="utf-8"))


def _to_posix(path: Path) -> str:
    return path.as_posix()


def _matches_any(value: str, patterns: list[str]) -> bool:
    for pattern in patterns:
        if fnmatch.fnmatch(value, pattern):
            return True
        if "/**/" in pattern:
            shallow_pattern = pattern.replace("/**/", "/")
            if fnmatch.fnmatch(value, shallow_pattern):
                return True
    return False


def classify_file_domain(rel_path: Path, contract: dict[str, Any]) -> str | None:
    rel = _to_posix(rel_path)
    domains = contract.get("domains", {})
    for domain_name, config in domains.items():
        patterns = config.get("path_patterns", [])
        if _matches_any(rel, patterns):
            return domain_name
    return None


def classify_module_domain(module_name: str, contract: dict[str, Any]) -> str | None:
    if not module_name:
        return None
    domains = contract.get("domains", {})
    for domain_name, config in domains.items():
        for prefix in config.get("module_prefixes", []):
            if module_name == prefix or module_name.startswith(prefix + "."):
                return domain_name
    return None


def module_name_from_relpath(rel_path: Path) -> str:
    parts = list(rel_path.with_suffix("").parts)
    if parts and parts[-1] == "__init__":
        parts = parts[:-1]
    return ".".join(parts)


def _resolve_import_from(current_module: str, node: ast.ImportFrom) -> str:
    if node.level == 0:
        return node.module or ""
    current_parts = current_module.split(".") if current_module else []
    if node.level <= len(current_parts):
        base_parts = current_parts[:-node.level]
    else:
        base_parts = []
    if node.module:
        base_parts = [*base_parts, node.module]
    return ".".join(base_parts)


def extract_imports(current_module: str, tree: ast.AST) -> list[tuple[int, str]]:
    imports: list[tuple[int, str]] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append((node.lineno, alias.name))
            continue
        if not isinstance(node, ast.ImportFrom):
            continue
        base_module = _resolve_import_from(current_module, node)
        if base_module:
            imports.append((node.lineno, base_module))
        for alias in node.names:
            if alias.name == "*":
                continue
            if base_module:
                imports.append((node.lineno, f"{base_module}.{alias.name}"))
            else:
                imports.append((node.lineno, alias.name))
    deduped: list[tuple[int, str]] = []
    seen: set[tuple[int, str]] = set()
    for item in imports:
        if item in seen:
            continue
        seen.add(item)
        deduped.append(item)
    return deduped


def collect_python_files(root: Path, scan_paths: list[str]) -> list[Path]:
    files: set[Path] = set()
    for raw in scan_paths:
        target = (root / raw).resolve()
        if not target.exists():
            continue
        if target.is_file() and target.suffix == ".py":
            files.add(target)
            continue
        for file_path in target.rglob("*.py"):
            if file_path.is_file():
                files.add(file_path.resolve())
    return sorted(files, key=lambda p: _to_posix(p.relative_to(root)))


def _allowlisted(module_name: str, current_module: str, contract: dict[str, Any]) -> bool:
    allowlist = contract.get("interop_allowlist", {})
    patterns = allowlist.get("module_patterns", [])
    if not patterns:
        return False
    return _matches_any(module_name, patterns) or _matches_any(current_module, patterns)


def check_boundaries(
    *,
    root: Path,
    contract_path: Path,
    scan_paths: list[str],
) -> list[dict[str, Any]]:
    contract = load_contract(contract_path)
    files = collect_python_files(root, scan_paths)
    rules = contract.get("rules", [])
    violations: list[dict[str, Any]] = []

    for file_path in files:
        rel_path = file_path.relative_to(root)
        source_domain = classify_file_domain(rel_path, contract)
        if source_domain not in {"ai", "xs"}:
            continue
        source_module = module_name_from_relpath(rel_path)
        tree = ast.parse(file_path.read_text(encoding="utf-8"), filename=_to_posix(rel_path))
        for line_no, imported_module in extract_imports(source_module, tree):
            imported_domain = classify_module_domain(imported_module, contract)
            if imported_domain is None:
                continue
            for rule in rules:
                if rule.get("from_domain") != source_domain:
                    continue
                if rule.get("to_domain") != imported_domain:
                    continue
                if _allowlisted(imported_module, source_module, contract):
                    continue
                violations.append(
                    {
                        "path": _to_posix(rel_path),
                        "line": line_no,
                        "import": imported_module,
                        "rule": rule.get("name", "boundary_violation"),
                    }
                )

    violations.sort(key=lambda v: (v["path"], v["line"], v["import"], v["rule"]))
    return violations


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check AI/XS boundary import violations")
    default_root = Path(__file__).resolve().parents[1]
    parser.add_argument("--root", default=str(default_root), help="Project root directory")
    parser.add_argument(
        "--contract",
        default="docs/architecture/ai_xs_boundary.json",
        help="Boundary contract JSON path (relative to root unless absolute)",
    )
    parser.add_argument(
        "--paths",
        nargs="*",
        default=["src", "tools", "tests"],
        help="Directories/files to scan for Python imports",
    )
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    contract_path = Path(args.contract)
    if not contract_path.is_absolute():
        contract_path = (root / contract_path).resolve()

    violations = check_boundaries(root=root, contract_path=contract_path, scan_paths=args.paths)
    for violation in violations:
        print(
            f"{violation['path']}:{violation['line']} "
            f"import={violation['import']} rule={violation['rule']}"
        )
    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main())
