from __future__ import annotations

import importlib.resources as resources
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from src.retrieval.xs_script_validator import validate_xs_retrieval_context


# Package identifier for bundled XS data
_XS_DATA_PACKAGE = "src.data.xs"

TOKEN_RE = re.compile(r"[a-z0-9-]+")
SYMBOL_NORMALIZE_RE = re.compile(r"[^a-z0-9]")


def _get_default_dataset_path() -> Path | None:
    """Get the default dataset path from packaged resources.

    Returns the path to the xs_knowledge directory in the package,
    or None if the resources are not available.
    """
    try:
        # Try to access the packaged xs_knowledge directory
        # This will raise FileNotFoundError if package data is missing
        ref = resources.files(_XS_DATA_PACKAGE).joinpath("xs_knowledge")
        # Verify the directory exists by trying to access a known file
        ref.joinpath("metadata_index.json").read_text()
        # Return a path-like object that can be used for resource access
        return Path(str(ref))
    except (ModuleNotFoundError, FileNotFoundError, TypeError):
        return None


def _load_resource_text(package: str, resource: str) -> str:
    """Load text resource from package using importlib.resources.

    Args:
        package: The package to load from (e.g., 'src.data.xs')
        resource: The resource path relative to the package

    Returns:
        The text content of the resource

    Raises:
        FileNotFoundError: If the resource is not found
    """
    return resources.files(package).joinpath(resource).read_text(encoding="utf-8")


@dataclass
class XSRetrievalResult:
    source_file: str
    title: str
    score: float
    text: str


class XSScriptKnowledgeRetriever:
    """Hybrid retrieval utility for local XS scripting knowledge.

    This intentionally stays lightweight:
    - deterministic command lookup from metadata index
    - token-overlap relevance over chunked document store
    - simple context builder for LLM prompt injection

    Semantic embeddings can be added later without changing callers.

    API parity with AIScriptKnowledgeRetriever for consistent retrieval interface.

    Args:
        dataset_dir: Optional path to dataset directory. If not provided,
                     uses packaged defaults from src.data.xs.xs_knowledge.
    """

    def __init__(self, dataset_dir: Path | None = None):
        # Determine the dataset directory to use
        self._custom_dataset_dir = dataset_dir
        self._use_packaged = dataset_dir is None

        if dataset_dir is not None:
            self.dataset_dir = dataset_dir
            # Load from custom path
            self.metadata = self._load_json(self.dataset_dir / "metadata_index.json")
            self.chunks = self._load_jsonl(self.dataset_dir / "document_store.jsonl")
        else:
            # Load from packaged resources
            # Set dataset_dir to None to indicate packaged resources are being used
            # (but we keep the attribute for backwards compatibility)
            self.dataset_dir = None
            try:
                self.metadata = self._load_json_from_package("xs_knowledge/metadata_index.json")
                self.chunks = self._load_jsonl_from_package("xs_knowledge/document_store.jsonl")
            except FileNotFoundError as e:
                raise ValueError(
                    f"Packaged XS knowledge data not available: {e}. "
                    "Either provide dataset_dir or ensure package data is installed."
                ) from e

        self._commands_by_name = {
            row["command"]: row for row in self.metadata.get("commands", [])
        }

        # Load catalog data - always from package, then optionally merge custom
        # First try to load from package (bundled catalogs)
        try:
            function_rows = self._load_catalog_from_package("xs_functions_catalog.json")
            constant_rows = self._load_catalog_from_package("xs_constants_catalog.json")
        except FileNotFoundError:
            # Package data not available - start empty
            function_rows = []
            constant_rows = []

        # If custom dataset_dir provided, also load from there (for custom scenarios)
        if dataset_dir is not None:
            custom_function_rows = self._load_catalog_json(
                dataset_dir.parent / "agent_database" / "xs_functions_catalog.json"
            )
            custom_constant_rows = self._load_catalog_json(
                dataset_dir.parent / "agent_database" / "xs_constants_catalog.json"
            )
            # Merge custom catalogs (custom takes precedence for duplicates)
            existing_funcs = {self._normalize_symbol_key(row.get("name", "")) for row in function_rows}
            for row in custom_function_rows:
                key = self._normalize_symbol_key(row.get("name", ""))
                if key and key not in existing_funcs:
                    function_rows.append(row)
                    existing_funcs.add(key)

            existing_consts = {self._normalize_symbol_key(row.get("name", "")) for row in constant_rows}
            for row in custom_constant_rows:
                key = self._normalize_symbol_key(row.get("name", ""))
                if key and key not in existing_consts:
                    constant_rows.append(row)
                    existing_consts.add(key)

        self._functions_by_key = {
            self._normalize_symbol_key(str(row.get("name", ""))): row
            for row in function_rows
            if row.get("name")
        }
        self._constants_by_key = {
            self._normalize_symbol_key(str(row.get("name", ""))): row
            for row in constant_rows
            if row.get("name")
        }

    @staticmethod
    def _load_json(path: Path) -> dict[str, Any]:
        return json.loads(path.read_text(encoding="utf-8"))

    @staticmethod
    def _load_json_from_package(resource_path: str) -> dict[str, Any]:
        """Load JSON from packaged resources.

        Args:
            resource_path: Path to the resource relative to _XS_DATA_PACKAGE

        Returns:
            Parsed JSON as dict
        """
        text = _load_resource_text(_XS_DATA_PACKAGE, resource_path)
        return json.loads(text)

    @staticmethod
    def _load_jsonl(path: Path) -> list[dict[str, Any]]:
        rows = []
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            rows.append(json.loads(line))
        return rows

    @staticmethod
    def _load_jsonl_from_package(resource_path: str) -> list[dict[str, Any]]:
        """Load JSONL from packaged resources.

        Args:
            resource_path: Path to the resource relative to _XS_DATA_PACKAGE

        Returns:
            List of parsed JSON objects
        """
        text = _load_resource_text(_XS_DATA_PACKAGE, resource_path)
        rows = []
        for line in text.splitlines():
            if not line.strip():
                continue
            rows.append(json.loads(line))
        return rows

    @staticmethod
    def _load_catalog_json(path: Path) -> list[dict[str, Any]]:
        if not path.exists():
            return []
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, list):
            return [row for row in data if isinstance(row, dict)]
        return []

    @staticmethod
    def _load_catalog_from_package(resource_name: str) -> list[dict[str, Any]]:
        """Load catalog JSON from packaged resources.

        Args:
            resource_name: Name of the resource file (e.g., 'xs_functions_catalog.json')

        Returns:
            List of catalog entries as dicts
        """
        try:
            text = _load_resource_text(_XS_DATA_PACKAGE, f"agent_database/{resource_name}")
            data = json.loads(text)
            if isinstance(data, list):
                return [row for row in data if isinstance(row, dict)]
            return []
        except (ModuleNotFoundError, FileNotFoundError) as e:
            raise FileNotFoundError(
                f"Packaged catalog resource '{resource_name}' not found: {e}"
            ) from e

    @staticmethod
    def _normalize_symbol_key(value: str) -> str:
        return SYMBOL_NORMALIZE_RE.sub("", value.strip().lower())

    @staticmethod
    def _optional_default(param_type: str) -> str:
        defaults = {
            "bool": "False",
            "int": "0",
            "float": "0.0",
            "string": '""',
            "vector": "cInvalidVector",
        }
        return defaults.get(param_type, "None")

    def _build_function_signature(self, row: dict[str, Any]) -> str:
        params = []
        for param in row.get("params", []):
            param_type = str(param.get("type", "any"))
            param_name = str(param.get("name", "arg"))
            if param.get("required", True):
                params.append(f"{param_type} {param_name}")
            else:
                params.append(
                    f"{param_type} {param_name}={self._optional_default(param_type)}"
                )
        return_type = str(row.get("return_type", "void"))
        name = str(row.get("name", ""))
        return f"{return_type} {name}({', '.join(params)})"

    def _build_constant_signature(self, row: dict[str, Any]) -> str:
        const_type = str(row.get("type", "any"))
        name = str(row.get("name", ""))
        value = row.get("value", "")
        return f"{const_type} {name} = {value}"

    def lookup_symbol(self, symbol_name: str) -> dict[str, Any]:
        """Deterministic exact symbol lookup for XS functions/constants."""
        normalized_query = self._normalize_symbol_key(symbol_name)

        found_function = self._functions_by_key.get(normalized_query)
        if found_function is not None:
            return {
                "query": symbol_name,
                "normalized_query": normalized_query,
                "found": True,
                "error_code": "OK",
                "symbol_type": "function",
                "name": str(found_function.get("name", "")),
                "signature": self._build_function_signature(found_function),
                "details": found_function,
            }

        found_constant = self._constants_by_key.get(normalized_query)
        if found_constant is not None:
            return {
                "query": symbol_name,
                "normalized_query": normalized_query,
                "found": True,
                "error_code": "OK",
                "symbol_type": "constant",
                "name": str(found_constant.get("name", "")),
                "signature": self._build_constant_signature(found_constant),
                "details": found_constant,
            }

        return {
            "query": symbol_name,
            "normalized_query": normalized_query,
            "found": False,
            "error_code": "XS_SYMBOL_NOT_FOUND",
            "symbol_type": "",
            "name": "",
            "signature": "",
            "details": {},
        }

    def lookup_command(self, command: str) -> dict[str, Any] | None:
        """Lookup a specific XS command by name."""
        return self._commands_by_name.get(command)

    @staticmethod
    def _result_priority(result: XSRetrievalResult) -> int:
        if result.title.startswith("xs-symbol:"):
            return 2
        if result.title.startswith("xs-command:"):
            return 1
        return 0

    def _find_symbol_hit(
        self, query: str, normalized_tokens_in_order: list[str]
    ) -> dict[str, Any] | None:
        direct_hit = self.lookup_symbol(query)
        if direct_hit.get("found"):
            return direct_hit

        for token in normalized_tokens_in_order:
            hit = self.lookup_symbol(token)
            if hit.get("found"):
                return hit
        return None

    def search(self, query: str, *, limit: int = 8) -> list[XSRetrievalResult]:
        """Route query and return ranked chunks.

        Routing strategy:
        - if query contains exact command token, prioritize command-linked snippets
        - else, do token-overlap retrieval over markdown/per chunks
        """
        token_sequence = list(dict.fromkeys(TOKEN_RE.findall(query.lower())))
        tokens = set(token_sequence)

        # 1) Deterministic exact symbol path.
        symbol_hit = self._find_symbol_hit(query, token_sequence)
        ranked: list[XSRetrievalResult] = []

        if symbol_hit is not None:
            details = symbol_hit.get("details")
            description = ""
            if isinstance(details, dict):
                description = str(details.get("desc", "") or details.get("description", ""))
            ranked.append(
                XSRetrievalResult(
                    source_file=f"agent_database/xs_{symbol_hit.get('symbol_type', 'unknown')}s_catalog.json",
                    title=f"xs-symbol:{symbol_hit.get('name', '')}",
                    score=1.0,
                    text=(f"{symbol_hit.get('signature', '')}\n{description}").strip(),
                )
            )

        # 2) Structured command hit path.
        command_hits = [c for c in token_sequence if c in self._commands_by_name]

        if command_hits:
            for cmd in command_hits:
                row = self._commands_by_name[cmd]
                examples = row.get("examples", [])
                for ex in examples:
                    ranked.append(
                        XSRetrievalResult(
                            source_file=ex.get("template", row.get("source_file", "")),
                            title=f"xs-command:{cmd}",
                            score=1.0,
                            text=ex.get("snippet", "") or row.get("description", ""),
                        )
                    )

        # 3) Token-overlap retrieval against chunk store.
        for chunk in self.chunks:
            text = chunk.get("text", "")
            if not text:
                continue
            chunk_tokens = set(TOKEN_RE.findall(text.lower()))
            if not chunk_tokens:
                continue
            overlap = tokens & chunk_tokens
            if not overlap:
                continue
            score = len(overlap) / max(1, len(tokens))
            ranked.append(
                XSRetrievalResult(
                    source_file=chunk.get("source_file", ""),
                    title=chunk.get("title", "section"),
                    score=score,
                    text=text,
                )
            )

        ranked.sort(
            key=lambda r: (
                -self._result_priority(r),
                -r.score,
                r.source_file,
                r.title,
                r.text[:120],
            )
        )

        # Deduplicate by (source,title,text-prefix) to keep context compact.
        seen = set()
        deduped: list[XSRetrievalResult] = []
        for item in ranked:
            key = (item.source_file, item.title, item.text[:120])
            if key in seen:
                continue
            seen.add(key)
            deduped.append(item)
            if len(deduped) >= limit:
                break

        return deduped

    def build_context(self, query: str, *, limit: int = 8) -> dict[str, Any]:
        results = self.search(query, limit=limit)
        commands = sorted(
            {
                token
                for token in TOKEN_RE.findall(query.lower())
                if token in self._commands_by_name
            }
        )

        payload = {
            "query": query,
            "commands_detected": commands,
            "retrieved": [
                {
                    "source": r.source_file,
                    "title": r.title,
                    "score": round(r.score, 4),
                    "text": r.text,
                }
                for r in results
            ],
        }

        validation = validate_xs_retrieval_context(payload)
        if not validation["ok"]:
            raise ValueError(
                f"{validation['error_code']} at {validation['error_path']}: {validation['message']}"
            )

        return payload
