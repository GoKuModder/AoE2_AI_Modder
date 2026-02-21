#!/usr/bin/env python3
import sys
from pathlib import Path

# Add project root to sys.path so we can import 'src'
root_dir = Path(__file__).parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

from src.builds.ai_scripting_knowledge_build import build_ai_scripting_knowledge


if __name__ == "__main__":
    sys.exit(build_ai_scripting_knowledge())
