#!/usr/bin/env python3
import sys
from pathlib import Path

root_dir = Path(__file__).parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

from src.eval.unified_retrieval_eval import main


if __name__ == "__main__":
    golden = root_dir / "docs" / "agent" / "references" / "recipes" / "design_brief_eval.json"
    raise SystemExit(main(["--golden", str(golden)]))
