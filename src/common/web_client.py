import urllib.request
import urllib.error
from pathlib import Path

def http_get(url: str, cache_path: Path) -> str:
    """
    Fetches a URL, caching the result at the specified path.
    Uses generic urllib to avoid external dependencies like requests.
    """
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    if cache_path.exists():
        return cache_path.read_text(encoding="utf-8", errors="ignore")

    headers = {"User-Agent": "ChainBoundTriggerKnowledge/1.0"}
    req = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            content = response.read().decode("utf-8")
            cache_path.write_text(content, encoding="utf-8")
            return content
    except urllib.error.URLError as e:
        raise RuntimeError(f"Failed to fetch {url}: {e}") from e
