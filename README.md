# aoe2-ai-modder

AoE2:DE AI scripting and trigger knowledge tooling.

This repo focuses on building local knowledge datasets and providing small utilities that help LLM agents write safer `.per` AI scripts.

Status: git install only. Not published to PyPI.

## Quick start

Requirements: Python 3.10+

```bash
git clone <REPO_URL>
cd <REPO_DIR>
py -3 -m pip install -e .
```

Or install directly from git:

```bash
py -3 -m pip install "aoe2-ai-modder @ git+https://github.com/<ORG>/<REPO>.git"
```

Build the AI scripting knowledge dataset (writes to `docs/ai_scripting_knowledge/`):

```bash
py -3 tools/build_ai_scripting_knowledge.py
```

Run tests:

```bash
py -3 -m unittest discover -s tests -p "test_*.py"
```

## Usage

Retrieval:

```python
from pathlib import Path

from src.retrieval.ai_script_retriever import AIScriptKnowledgeRetriever

retriever = AIScriptKnowledgeRetriever(Path("docs/ai_scripting_knowledge"))
hits = retriever.search("taunt-detected")
for h in hits[:3]:
    print(h.score, h.title, h.source_file)
```

Validation:

```python
import json
from pathlib import Path

from src.retrieval.ai_script_validator import validate_ai_script

metadata = json.loads(
    (Path("docs/ai_scripting_knowledge") / "metadata_index.json").read_text(encoding="utf-8")
)

script_text = "(defrule (goal 1) => (acknowledge-taunt))"
result = validate_ai_script(script_text, metadata)
print(result["ok"], result["blocked_commands"], result["unknown_commands"], result["warnings"])
```

## Related docs

- `AoE2_AI_Scripting_Guide/` - LLM-safe guide source.
- `docs/ai_scripting_knowledge/README.md` - dataset artifacts and build command.

## Support

For now, use GitHub Issues for bug reports and feature requests.

Security issues: see `SECURITY.md`.
