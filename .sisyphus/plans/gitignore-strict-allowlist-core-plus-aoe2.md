# Gitignore Strict Allowlist (Core + AoE2)

## TL;DR

> **Quick Summary**: Replace root `.gitignore` with strict allowlist semantics so only core development and selected AoE2 folders are visible for tracking, while generated/build/cache paths stay ignored.
>
> **Deliverables**:
> - Updated root `.gitignore` using ignore-all + explicit unignore rules
> - Verified allowlist behavior with `git check-ignore` matrix
> - Explicit decision on whether to de-track already tracked out-of-scope files
>
> **Estimated Effort**: Quick
> **Parallel Execution**: YES - 2 waves + final verification
> **Critical Path**: T1 -> T2 -> T4 -> T6

---

## Context

### Original Request
Update `.gitignore` to keep only important project folders.

### Interview Summary
**Key Discussions**:
- User selected **strict allowlist mode**.
- User selected scope **Core + AoE2 content**.

**Research Findings**:
- Existing `.gitignore` mixes pattern ignores and broad extension ignores.
- Broad ignores (for example `*.xs`, `*.per`, `*.jsonl`) can conflict with allowlisted AoE2/docs content.

### Metis Review
**Identified Gaps (addressed in this plan)**:
- Clarified that `.gitignore` controls future tracking visibility, not existing tracked entries by itself.
- Added explicit acceptance checks for allowed/ignored paths with `git check-ignore`.
- Added explicit scope lock to avoid accidental history/index cleanup unless requested.

---

## Work Objectives

### Core Objective
Produce a robust strict-allowlist `.gitignore` for this repository that keeps only agreed core + AoE2 paths trackable and keeps generated/noise paths ignored.

### Concrete Deliverables
- Root `.gitignore` rewritten in strict allowlist form.
- Verification evidence showing target paths are allowed and non-target paths are ignored.
- Optional follow-up command plan for de-tracking existing files (not executed unless explicitly requested).

### Definition of Done
- [ ] `.gitignore` uses ignore-all with explicit unignore rules for the selected folders/files.
- [ ] `git check-ignore -v` confirms allow/deny behavior for the verification matrix.
- [ ] `git status --short` shows expected noise reduction behavior for new/untracked files.

### Must Have
- Strict allowlist semantics at repo root.
- Include these folder groups:
  - Core: `src/`, `tests/`, `tools/`, `docs/`
  - AoE2 content: `AI_Scripting/`, `XS_Scripting/`, `Verify_XS/`, `AoE2_AI_Scripting_Guide/`, `XS_Training/`
- Keep runtime/build/system noise ignored (`.venv/`, `build/`, `dist/`, `*.egg-info/`, caches, `.sisyphus/`).

### Must NOT Have (Guardrails)
- No edits outside root `.gitignore`.
- No destructive index/history operations during this task (`git rm --cached`, rewrite history) unless separately requested.
- No CI/workflow changes.

---

## Verification Strategy (MANDATORY)

> **ZERO HUMAN INTERVENTION** — verification is command/tool driven.

### Test Decision
- **Infrastructure exists**: N/A (configuration task)
- **Automated tests**: None
- **Agent-Executed QA**: Yes (git behavior checks)

### QA Policy
Every task includes command-executable checks and concrete expected outcomes.
Evidence files should be saved under `.sisyphus/evidence/gitignore-allowlist/`.

| Deliverable Type | Verification Tool | Method |
|------------------|-------------------|--------|
| Ignore rules | Bash (`git check-ignore`) | Probe allow/deny behavior by path |
| Repo status | Bash (`git status --short`) | Confirm noise reduction and expected visibility |
| Syntax/logic | Read + grep | Validate rule ordering and conflict overrides |

---

## Execution Strategy

### Parallel Execution Waves

```text
Wave 1 (foundation, parallel):
  T1 - Enumerate allowlist + denylist matrix
  T2 - Draft strict allowlist .gitignore structure
  T3 - Resolve conflict patterns (extensions/jsonl/docs nesting)

Wave 2 (after Wave 1):
  T4 - Apply root .gitignore update
  T5 - Run git check-ignore verification matrix

Wave FINAL:
  T6 - Scope fidelity + risk check and optional de-track guidance
```

### Dependency Matrix

| Task | Depends On | Blocks | Wave |
|------|------------|--------|------|
| T1 | - | T2,T3,T5 | 1 |
| T2 | T1 | T4 | 1 |
| T3 | T1 | T4 | 1 |
| T4 | T2,T3 | T5,T6 | 2 |
| T5 | T1,T4 | T6 | 2 |
| T6 | T4,T5 | - | FINAL |

---

## TODOs

- [ ] 1. Enumerate include/exclude matrix for strict allowlist

  **What to do**:
  - Confirm selected include roots and required root files.
  - Build explicit denylist for generated/system/noise paths.

  **Must NOT do**:
  - Do not edit files.

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: `superpowers/brainstorming`

  **Parallelization**:
  - **Can Run In Parallel**: YES (with T2/T3 drafting prep)
  - **Blocks**: T2,T3,T5
  - **Blocked By**: None

  **References**:
  - `.gitignore` - current rules and conflicts
  - `src/builds/ai_scripting_knowledge_build.py` - confirms `AoE2_AI_Scripting_Guide/` relevance
  - `src/builds/xs_knowledge_build.py` - confirms `XS_Training/` relevance

  **Acceptance Criteria**:
  - [ ] Include matrix and deny matrix explicitly listed in task notes.

  **QA Scenarios**:
  ```text
  Scenario: Include matrix complete
    Tool: Read
    Steps:
      1. Read relevant build/runtime files.
      2. Confirm required content roots are represented in include matrix.
      3. Assert matrix contains both core and AoE2 selected folders.
    Expected Result: matrix reflects selected scope exactly.
    Evidence: .sisyphus/evidence/gitignore-allowlist/task-1-matrix.txt

  Scenario: Negative - accidental scope expansion blocked
    Tool: Read
    Steps:
      1. Review matrix for non-requested roots.
      2. Assert no extra root folders are added without rationale.
    Expected Result: no unexplained scope additions.
    Evidence: .sisyphus/evidence/gitignore-allowlist/task-1-negative.txt
  ```

- [ ] 2. Draft strict allowlist rule structure for root `.gitignore`

  **What to do**:
  - Use robust ordering: ignore-all, directory traversal unignore, explicit root-file unignores, explicit folder unignores, explicit re-ignores for generated artifacts.
  - Ensure parent path unignore chain is valid for nested paths.

  **Must NOT do**:
  - Do not apply changes yet.

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: `superpowers/systematic-debugging`

  **Parallelization**:
  - **Can Run In Parallel**: YES (with T3)
  - **Blocks**: T4
  - **Blocked By**: T1

  **References**:
  - `.gitignore` - existing baseline

  **Acceptance Criteria**:
  - [ ] Draft contains complete ordering and no ambiguous wildcard conflicts.

  **QA Scenarios**:
  ```text
  Scenario: Rule order soundness
    Tool: Read
    Steps:
      1. Inspect draft order top-to-bottom.
      2. Verify unignore rules occur after ignore-all rule.
      3. Verify directory parents are unignored before child patterns.
    Expected Result: ordering supports intended behavior.
    Evidence: .sisyphus/evidence/gitignore-allowlist/task-2-order.txt

  Scenario: Negative - broad extension conflict detected
    Tool: Read
    Steps:
      1. Search draft for `*.xs`, `*.per`, `*.jsonl`.
      2. Confirm either removed or explicitly overridden for allowlisted paths.
    Expected Result: no unresolved conflicts remain.
    Evidence: .sisyphus/evidence/gitignore-allowlist/task-2-negative.txt
  ```

- [ ] 3. Resolve conflict patterns and docs/jsonl handling

  **What to do**:
  - Resolve conflicts between strict allowlist and prior extension-wide ignore behavior.
  - Ensure `docs/` allowlist behavior is explicit.

  **Must NOT do**:
  - No file edits outside `.gitignore`.

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: `superpowers/systematic-debugging`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Blocks**: T4
  - **Blocked By**: T1

  **References**:
  - `.gitignore`
  - `docs/` tree

  **Acceptance Criteria**:
  - [ ] Conflict treatment documented and reflected in final rules.

  **QA Scenarios**:
  ```text
  Scenario: Docs dataset compatibility
    Tool: Read
    Steps:
      1. Inspect docs-related patterns.
      2. Confirm allowlisted docs paths are not shadow-ignored.
    Expected Result: docs allowlist behaves as intended.
    Evidence: .sisyphus/evidence/gitignore-allowlist/task-3-docs.txt

  Scenario: Negative - forbidden generated folders stay ignored
    Tool: Read
    Steps:
      1. Verify explicit ignores for `.venv/`, `build/`, `dist/`, `.sisyphus/`.
      2. Confirm no later unignore rule re-exposes them.
    Expected Result: generated/system folders remain ignored.
    Evidence: .sisyphus/evidence/gitignore-allowlist/task-3-negative.txt
  ```

- [ ] 4. Apply root `.gitignore` strict allowlist update

  **What to do**:
  - Update root `.gitignore` with finalized strict allowlist rules.

  **Must NOT do**:
  - Do not modify any other file.

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: `superpowers/verification-before-completion`

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Blocks**: T5,T6
  - **Blocked By**: T2,T3

  **References**:
  - `.gitignore`

  **Acceptance Criteria**:
  - [ ] Only `.gitignore` changed.
  - [ ] File contains strict allowlist structure and selected include roots.

  **QA Scenarios**:
  ```text
  Scenario: Single-file change integrity
    Tool: Bash (git)
    Steps:
      1. Run `git status --short`.
      2. Assert only `.gitignore` is modified by this task scope.
    Expected Result: no unrelated file modifications.
    Evidence: .sisyphus/evidence/gitignore-allowlist/task-4-status.txt

  Scenario: Negative - accidental secondary edits
    Tool: Bash (git)
    Steps:
      1. Run `git diff --name-only`.
      2. Assert no path outside `.gitignore` appears.
    Expected Result: zero out-of-scope edits.
    Evidence: .sisyphus/evidence/gitignore-allowlist/task-4-negative.txt
  ```

- [ ] 5. Verify ignore behavior with command matrix

  **What to do**:
  - Run `git check-ignore -v` probes for allowed and ignored examples.

  **Must NOT do**:
  - Do not alter index/tracked state.

  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: `superpowers/verification-before-completion`

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Blocks**: T6
  - **Blocked By**: T1,T4

  **References**:
  - `.gitignore`

  **Acceptance Criteria**:
  - [ ] Allowed probes are not ignored.
  - [ ] Ignored probes map to expected rules.

  **QA Scenarios**:
  ```text
  Scenario: Allowed path probes pass
    Tool: Bash (git)
    Steps:
      1. Run probes on `src/`, `tests/`, `tools/`, `docs/`, `AI_Scripting/`, `XS_Scripting/`, `Verify_XS/`, `AoE2_AI_Scripting_Guide/`, `XS_Training/` sample files.
      2. Assert each returns non-ignored status.
    Expected Result: all selected scope paths are trackable.
    Evidence: .sisyphus/evidence/gitignore-allowlist/task-5-allowed.txt

  Scenario: Ignored path probes fail correctly
    Tool: Bash (git)
    Steps:
      1. Run probes on `.venv/`, `build/`, `dist/`, `.sisyphus/`, `*.egg-info/` samples.
      2. Assert each returns ignore rule match.
    Expected Result: noise/system paths remain ignored.
    Evidence: .sisyphus/evidence/gitignore-allowlist/task-5-ignored.txt
  ```

- [ ] 6. Final scope fidelity + optional de-track guidance

  **What to do**:
  - Confirm implementation exactly matches user-selected scope.
  - Provide optional follow-up command set for de-tracking already tracked out-of-scope files (not executed).

  **Must NOT do**:
  - Do not execute `git rm --cached` unless explicitly requested.

  **Recommended Agent Profile**:
  - **Category**: `unspecified-low`
  - **Skills**: `superpowers/verification-before-completion`

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Blocks**: -
  - **Blocked By**: T4,T5

  **References**:
  - `.gitignore`

  **Acceptance Criteria**:
  - [ ] Scope report calls out what is in and out.
  - [ ] Optional de-track guidance is explicit and marked as not-run.

  **QA Scenarios**:
  ```text
  Scenario: Scope fidelity check
    Tool: Read + Bash (git)
    Steps:
      1. Compare final rules against selected include scope.
      2. Verify no extra root folders are allowlisted.
    Expected Result: exact scope match.
    Evidence: .sisyphus/evidence/gitignore-allowlist/task-6-scope.txt

  Scenario: Negative - unintended destructive action
    Tool: Bash (git)
    Steps:
      1. Review executed command history for `git rm --cached`.
      2. Assert not executed in this task.
    Expected Result: no destructive index changes performed.
    Evidence: .sisyphus/evidence/gitignore-allowlist/task-6-negative.txt
  ```

---

## Success Criteria

### Verification Commands
```bash
git check-ignore -v src/retrieval/xs_script_retriever.py
git check-ignore -v AI_Scripting/training/Promisory/merge.per
git check-ignore -v XS_Scripting/xs_arrays_full_project_demo.xs
git check-ignore -v AoE2_AI_Scripting_Guide/06_LLM_COMMAND_ALLOWLIST.md
git check-ignore -v XS_Training/fetch_pages.py
git check-ignore -v .sisyphus/plans/ai-xs-separation-xs-rag-publish.md
git check-ignore -v build/
git check-ignore -v dist/
git status --short
```

### Final Checklist
- [ ] Strict allowlist behavior implemented in root `.gitignore`.
- [ ] Core + AoE2 selected paths are trackable.
- [ ] Generated/system/noise paths remain ignored.
- [ ] No unapproved destructive tracking cleanup executed.
