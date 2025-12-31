import re

try:
    from bs4 import BeautifulSoup  # type: ignore
except ImportError:
    BeautifulSoup = None


def require_bs4() -> None:
    if BeautifulSoup is None:
        raise RuntimeError(
            "Missing dependency 'beautifulsoup4'. Install it (PyCharm Interpreter Packages)."
        )


def clean_ws(s: str) -> str:
    s = s.replace("¶", "")
    return re.sub(r"\s+", " ", s).strip()
