#!/usr/bin/env python3
import sys
from pathlib import Path

# Add project root to sys.path so we can import 'src'
# Logic: this file is tools/build_trigger_knowledge.py -> parent is tools/ -> parent is root
root_dir = Path(__file__).parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

from src.builds.trigger_knowledge_build import build_trigger_knowledge

if __name__ == "__main__":
    sys.exit(build_trigger_knowledge())
