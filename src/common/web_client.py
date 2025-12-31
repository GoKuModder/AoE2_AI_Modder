import requests
from pathlib import Path

def http_get(url: str, cache_path: Path) -> str:
    """
    Fetches a URL, caching the result at the specified path.
    """
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    if cache_path.exists():
        return cache_path.read_text(encoding="utf-8", errors="ignore")

    if requests is None:
        raise RuntimeError(
            "Missing dependency 'requests'. Install it (PyCharm Interpreter Packages) or adapt to urllib."
        )

    resp = requests.get(url, timeout=30, headers={"User-Agent": "ChainBoundTriggerKnowledge/1.0"})
    resp.raise_for_status()
    cache_path.write_text(resp.text, encoding="utf-8")
    return resp.text
