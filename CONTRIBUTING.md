# Contributing

Thanks for helping improve `aoe2-ai-modder`.

## Development setup

```bash
py -3 -m pip install -e .
```

## Run tests

```bash
py -3 -m unittest discover -s tests -p "test_*.py"
```

## Build datasets

```bash
py -3 tools/build_ai_scripting_knowledge.py
```

## What to include in a PR

- A clear description of the change and why it is needed.
- Tests for behavior changes.
- Keep generated artifacts out of commits unless the PR is specifically about the generated outputs.
