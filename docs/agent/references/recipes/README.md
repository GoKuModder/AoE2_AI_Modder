# Reference Recipe Datasets

These datasets are the compact, implementation-oriented layer for fast RAG.
They are intended to be the low-token retrieval layer for common AoE coding workflows.

Use them before long markdown guides when the question is:

- "how do I build this system?"
- "which manager should I use?"
- "what are the steps for this AoE feature?"

## Datasets

- `scenario_recipes.json`
  Compact recipes for common scenario systems such as quests, teleports, loot, world events, and class picking.
- `parser_manager_patterns.json`
  Compact patterns for `UnitManager` and `MapManager` usage.
- `genie_recipes.json`
  Compact `.dat` / GenieWorkspace recipes for units, graphics, sounds, linking, and output workflow.
- `reference_recipes_eval.json`
  Golden queries for the recipe datasets.
- `unified_retrieval_eval.json`
  Golden map-feature and exact-lookup queries for the unified low-token retriever.

## Why These Exist

The broader guides are useful for teaching, but a fast RAG system needs smaller payloads.

These recipe datasets are designed to answer implementation questions with:

- small summaries
- exact best files to open
- short steps
- explicit pitfalls

That makes retrieval cheaper in tokens and faster to route.

For broader architecture questions, still use `../patterns/`.
For compact implementation workflows, prefer this `recipes/` folder first.

## Evaluation

- Runtime entrypoint
  `src/retrieval/aoe_unified_retriever.py`
- Eval module
  `src/eval/unified_retrieval_eval.py`
- Eval command
  `py -3 tools/eval_unified_retrieval.py`

Use the unified eval when you want to verify both retrieval quality and compactness budgets.
