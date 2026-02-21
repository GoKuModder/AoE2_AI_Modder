# 05 - LLM-Safe Workflow (No-Error Focus)

Use this workflow whenever an LLM generates `.per` logic.

Companion files:

- `06_LLM_COMMAND_ALLOWLIST.md` (strict command filter)
- `07_RETRIEVAL_INDEX.md` (fast lookup map)

## Step 1 - Declare command compatibility

For each command used, tag one of:

- AoC
- UP
- DE

Reject mixed-version code unless each command is supported in your runtime target.

Also enforce allowlist: commands not listed in `06_LLM_COMMAND_ALLOWLIST.md` are rejected.

## Step 2 - Build from templates only

Start from templates in `templates/` and modify goals/constants only.

Do not generate fresh syntax from scratch unless required.

## Step 3 - Enforce single-purpose rules

One rule should do one job:

- input routing (taunts/signals)
- combat decisions
- movement/scouting

## Step 4 - Add hard gates

Every high-impact action requires a gate:

- `attack-now` -> army count + timer
- taunt branch -> quest/dialogue state
- movement retask -> scout-active state

## Step 5 - Debug visibility

Include temporary debug actions during testing:

- `chat-local-to-self`
- `log` / `log-trace`

Remove noisy debug lines for production builds.

## Step 6 - Regression checks

Before accepting generated script:

1. No build/train/research commands present.
2. No duplicate fire loops (same action every tick).
3. All goals/constants referenced are initialized.
4. Every taunt branch is acknowledged and exits state.
5. Movement rules do not reuse stale search contexts.
