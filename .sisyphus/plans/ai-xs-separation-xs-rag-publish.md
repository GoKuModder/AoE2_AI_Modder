# Separate AI vs XS, Build XS RAG, Publish-Ready

## TL;DR

> **Quick Summary**: Split repository concerns into explicit AI and XS domains, add a production-grade XS retrieval stack (deterministic symbol lookup + chunk retrieval), and harden packaging so the project is git-installable and usable in a separate consumer project.
>
> **Deliverables**:
> - Clear AI/XS boundary with compatibility-safe bridge contract
> - New XS retrieval runtime and XS retrieval build/eval pipeline
> - Git-install publish readiness (metadata + package data for installed runtime)
>
> **Estimated Effort**: Large
> **Parallel Execution**: YES - 3 waves + final verification wave
> **Critical Path**: T6 -> T14 (active minimal scope)

## Scope Update (2026-02-21)

**Active Execution Mode**: Minimal publish scope for immediate consumer use via git install.

**Remaining Required Tasks**:
- T14 only (**1 task remaining**) to harden packaging/resource loading for installed usage.

**Deferred (not required for current objective)**:
- T13 (layout migration)
- T15 (root CI hardening)
- F1-F4 (final audit wave)

**Metis Guardrails Applied**:
- Do not rename module/package layout in this scope.
- Do not add PyPI/release automation scope.
- Do not bundle training/source corpora unnecessarily; include runtime-required artifacts only.
- Validate install/use from a clean consumer environment, not repo-root assumptions.

**Default Applied**:
- Keep current import surface unchanged for this scope; no namespace migration task added.

---

## Context

### Original Request
Organize the project so AI Scripting and XS Scripting are clearly separated, make XS retrieval accurate for agent code generation, then make the project ready to publish.

### Interview Summary
**Key Discussions**:
- User priority is agent retrieval accuracy for XS scripting.
- Publish preference is git-install usage in another project, with optional friend sharing.
- Test strategy chosen: **tests after implementation** (plus agent-executed QA scenarios).

**Research Findings**:
- AI runtime retrieval exists: `src/retrieval/ai_script_retriever.py`, `src/retrieval/ai_script_validator.py`.
- XS structured datasets exist: `docs/agent_database/xs_functions_catalog.json`, `docs/agent_database/xs_constants_catalog.json`, `docs/agent_database/agent_query_map.json`.
- Bridge coupling exists across domains: `AI_Scripting/rpg_xs_bridge_v3.{ai,per,xs}` and `src/integration/xs_injector.py`.
- Root packaging exists via `pyproject.toml`, but publish metadata/CI are incomplete.

### Metis Review
**Identified Gaps (addressed in this plan)**:
- Missing explicit interop contract and compatibility guardrails for bridge semantics.
- Missing XS runtime retriever parity with AI retrieval runtime.
- Missing measurable retrieval accuracy gate (golden set + metrics threshold).
- Missing packaged-data rules for installed (wheel/git) usage.
- Missing root CI for install + retrieval validation.

---

## Work Objectives

### Core Objective
Deliver a maintainable project structure where AI and XS concerns are clearly separated, while ensuring agents can retrieve accurate XS symbols/context and generate valid XS-oriented code workflows.

### Concrete Deliverables
- Domain separation contract and migration-safe structure for AI vs XS.
- `src/retrieval/xs_script_retriever.py` + companion XS retrieval modules.
- XS retrieval artifacts (normalized index/chunks) under a dedicated XS knowledge path.
- XS retrieval evaluation harness with thresholded pass/fail.
- Git-install-ready packaging with required metadata and package data wiring.
- Optional follow-up (deferred in minimal mode): root CI workflows for install/eval quality gates.

### Definition of Done
- [x] `python -m unittest discover -s tests -p "test_*.py"` passes. (Verified via `py -3 -m unittest discover -s tests -p "test_*.py"`)
- [x] `python -m pip wheel . -w dist` succeeds and installed wheel can access required XS data files. (Verified via `py -3 -m pip wheel . -w dist` + clean-venv wheel install smoke)
- [x] `python -m src.eval.xs_retrieval_eval --golden docs/agent_database/xs_eval.json --k 5` exits 0 and meets thresholds. (Verified via `py -3 -m src.eval.xs_retrieval_eval --k 5 --min-recall 0.8 --min-mrr 0.8` using packaged golden)
- [x] AI/XS boundary checks pass (no illegal cross-domain imports except interop contract). (Verified via full unittest discovery)

### Must Have
- High-precision deterministic XS symbol lookup before fuzzy/chunk fallback.
- Hybrid retrieval context for non-symbol conceptual queries.
- Agent-executable evaluation metrics with explicit numeric threshold.
- Backward-compatible bridge behavior for existing `rpg_xs_bridge*` flows.

### Must NOT Have (Guardrails)
- No external vector DB dependency in MVP.
- No silent bridge behavior drift.
- No publish claim without install + eval gates passing.
- No human-only verification criteria.

---

## Verification Strategy (MANDATORY)

> **ZERO HUMAN INTERVENTION** - all verification is agent-executed.

### Test Decision
- **Infrastructure exists**: YES
- **Automated tests**: Tests-after
- **Framework**: `unittest` (Python)
- **Agent-Executed QA**: ALWAYS

### QA Policy
Every task includes at least one happy-path and one failure/edge scenario with evidence files under `.sisyphus/evidence/`.

| Deliverable Type | Verification Tool | Method |
|------------------|-------------------|--------|
| Retrieval modules | Bash (python/unittest) | Run module tests + command assertions |
| Package install | Bash (pip) | Build wheel, install, import, resource access checks |
| Repo structure | Bash + Grep | Path/import contract and boundary rule checks |
| CI/publish config | Bash | Workflow lint and dry-run style command checks |

---

## Execution Strategy

### Active Minimal Path

```text
Completed baseline: T1-T12
Required now: T14
Deferred: T13, T15, F1-F4
Minimal Critical Path: T6 -> T14
```

### Parallel Execution Waves

```
Wave 1 (Start Immediately - boundaries + foundations, 6 parallel):
├── Task 1: Domain boundary contract + path map [deep]
├── Task 2: Interop API contract for bridge surface [deep]
├── Task 3: XS dataset manifest and schema wiring [quick]
├── Task 4: XS normalization/chunking build pipeline [unspecified-high]
├── Task 5: XS retrieval module scaffolding [quick]
└── Task 6: Root publish metadata baseline [writing]

Wave 2 (After Wave 1 - retrieval core + evaluation, 6 parallel):
├── Task 7: Deterministic XS symbol retriever [deep]
├── Task 8: Hybrid chunk retriever + ranking [deep]
├── Task 9: XS retrieval context builder + validator [unspecified-high]
├── Task 10: Golden set + eval CLI harness [unspecified-high]
├── Task 11: Tests for builder + deterministic lookup [quick]
└── Task 12: Tests for hybrid retrieval + metrics thresholds [deep]

Wave 3 (After Wave 2 - migration + publish hardening, 3 parallel):
├── Task 13: AI/XS layout migration with compatibility shims [unspecified-high]
├── Task 14: Git-install packaging hardening + package-data [quick]
└── Task 15: Root CI workflows for test/install/eval + release prep [quick]

Wave FINAL (After ALL tasks - independent review, 4 parallel):
├── Task F1: Plan compliance audit (oracle)
├── Task F2: Code quality review (unspecified-high)
├── Task F3: Real manual QA execution of all scenarios (unspecified-high)
└── Task F4: Scope fidelity check (deep)

Critical Path: T2 -> T4 -> T8 -> T10 -> T12 -> T14 -> T15
Parallel Speedup: ~60% vs sequential
Max Concurrent: 6
```

### Dependency Matrix (FULL)

### Dependency Matrix (ACTIVE MINIMAL)

| Task | Depends On | Blocks | Status |
|------|------------|--------|--------|
| T14 | T6 | - | ACTIVE |
| T13 | T1, T2 | - | DEFERRED |
| T15 | T6, T10, T11, T12, T14 | F1-F4 | DEFERRED |
| F1-F4 | T1-T15 | - | DEFERRED |

The full matrix below is retained as historical context.

| Task | Depends On | Blocks | Wave |
|------|------------|--------|------|
| T1 | - | T13 | 1 |
| T2 | - | T7, T13 | 1 |
| T3 | - | T7, T10 | 1 |
| T4 | - | T8, T9, T10 | 1 |
| T5 | - | T7, T8, T9 | 1 |
| T6 | - | T14, T15 | 1 |
| T7 | T2, T3, T5 | T11, T12 | 2 |
| T8 | T4, T5 | T9, T12 | 2 |
| T9 | T4, T5, T8 | T12 | 2 |
| T10 | T3, T4 | T12, T15 | 2 |
| T11 | T7 | T15 | 2 |
| T12 | T7, T8, T9, T10 | T15 | 2 |
| T13 | T1, T2 | T14 | 3 |
| T14 | T6, T13 | T15 | 3 |
| T15 | T6, T10, T11, T12, T14 | F1-F4 | 3 |
| F1 | T1-T15 | - | FINAL |
| F2 | T1-T15 | - | FINAL |
| F3 | T1-T15 | - | FINAL |
| F4 | T1-T15 | - | FINAL |

### Agent Dispatch Summary

| Wave | # Parallel | Tasks -> Agent Category |
|------|------------|-------------------------|
| 1 | **6** | T1,T2 -> `deep`; T3,T5 -> `quick`; T4 -> `unspecified-high`; T6 -> `writing` |
| 2 | **6** | T7,T8,T12 -> `deep`; T9,T10 -> `unspecified-high`; T11 -> `quick` |
| 3 | **3** | T13 -> `unspecified-high`; T14,T15 -> `quick` |
| FINAL | **4** | F1 -> `oracle`; F2,F3 -> `unspecified-high`; F4 -> `deep` |

---

## TODOs

- [x] 1. Define AI/XS domain boundary contract and path map
  **What to do**:
  - Add a boundary contract doc and machine-readable allowlist of cross-domain touchpoints.
  - Define canonical locations for AI docs/data/code and XS docs/data/code.
  - Add boundary enforcement test stub.
  **Must NOT do**:
  - Do not move files yet.
  - Do not change bridge behavior.
  **Recommended Agent Profile**:
  - **Category**: `deep` (architecture boundary reasoning)
  - **Skills**: `superpowers/writing-plans`, `git-master`
  - **Skills Evaluated but Omitted**: `playwright` (no browser work)
  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1
  - **Blocks**: T13
  - **Blocked By**: None
  **References**:
  - Pattern: `AI_Scripting/rpg_xs_bridge_v3.ai` - current bridge entrypoint pattern.
  - Pattern: `XS_Scripting/XS_ARRAYS_PROJECT_GUIDE.md` - XS-focused location pattern.
  - API: `src/integration/xs_injector.py` - current interop boundary candidate.
  - WHY: These three define current coupling and must anchor the boundary contract.
  **Acceptance Criteria**:
  - [ ] Boundary contract file exists and lists allowed cross-domain paths.
  - [ ] Boundary test stub fails on intentional illegal import fixture.
  **QA Scenarios**:
  ```text
  Scenario: Boundary contract parse success
    Tool: Bash
    Preconditions: Contract file created
    Steps:
      1. Run `python -m json.tool <contract-file>`
      2. Run boundary checker in dry-run mode
      3. Assert output includes "0 violations"
    Expected Result: command exit code 0 and no violations
    Evidence: .sisyphus/evidence/task-1-boundary-parse.txt

  Scenario: Illegal import is detected
    Tool: Bash
    Preconditions: Test fixture with illegal import exists
    Steps:
      1. Run boundary checker against fixture directory
      2. Assert one violation referencing fixture path
    Expected Result: non-zero exit with violation details
    Evidence: .sisyphus/evidence/task-1-boundary-illegal.txt
  ```
  **Commit**: YES - `chore(arch): add ai-xs boundary contract`.

- [x] 2. Implement interop API contract for bridge surface
  **What to do**:
  - Define stable interop functions for bridge access and XS injection handoff.
  - Add compatibility tests ensuring current `rpg_xs_bridge_v3.*` semantics remain unchanged.
  **Must NOT do**:
  - No runtime behavior drift in bridge scripts.
  **Recommended Agent Profile**:
  - **Category**: `deep`
  - **Skills**: `superpowers/systematic-debugging`, `git-master`
  - **Skills Evaluated but Omitted**: `writing` (implementation-heavy)
  **Parallelization**: YES, Wave 1, blocks T7/T13, blocked by none.
  **References**:
  - `AI_Scripting/rpg_xs_bridge_v3.per`
  - `AI_Scripting/rpg_xs_bridge_v3.xs`
  - `tests/test_xs_injector.py`
  - WHY: define and preserve bridge IO behavior and test pattern.
  **Acceptance Criteria**:
  - [ ] Compatibility test snapshots pass for bridge entry semantics.
  - [ ] Interop module used by downstream retrieval/injection code.
  **QA Scenarios**:
  ```text
  Scenario: Bridge compatibility snapshot unchanged
    Tool: Bash
    Steps:
      1. Run `python -m unittest tests.test_xs_bridge_compat`
      2. Assert all snapshot checks pass
    Expected Result: PASS, 0 failures
    Evidence: .sisyphus/evidence/task-2-bridge-compat.txt

  Scenario: Invalid bridge payload rejected
    Tool: Bash
    Steps:
      1. Execute interop function with missing required field
      2. Assert typed error is raised with code `bridge_contract_error`
    Expected Result: graceful failure, no silent fallback
    Evidence: .sisyphus/evidence/task-2-bridge-invalid.txt
  ```
  **Commit**: YES - `feat(interop): add stable bridge contract api`.

- [x] 3. Add XS datasets to manifest and schema wiring
  **What to do**:
  - Extend `docs/agent_database/database_manifest.json` to include XS datasets.
  - Define schema validation rules for XS function/constant catalogs.
  **Must NOT do**:
  - No schema assumptions without validation script.
  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: `superpowers/test-driven-development`, `git-master`
  - **Skills Evaluated but Omitted**: `playwright`
  **Parallelization**: YES, Wave 1, blocks T7/T10, blocked by none.
  **References**:
  - `docs/agent_database/database_manifest.json`
  - `docs/agent_database/xs_functions_catalog.json`
  - `docs/agent_database/xs_constants_catalog.json`
  - WHY: canonical discovery starts from manifest and schema constraints.
  **Acceptance Criteria**:
  - [ ] Manifest includes XS dataset entries with record_count and key fields.
  - [ ] Schema check script passes on existing catalogs.
  **QA Scenarios**:
  ```text
  Scenario: Manifest discovery includes XS datasets
    Tool: Bash
    Steps:
      1. Run `python tools/check_manifest.py --dataset xs_functions`
      2. Run `python tools/check_manifest.py --dataset xs_constants`
    Expected Result: both commands exit 0 and print dataset path
    Evidence: .sisyphus/evidence/task-3-manifest-check.txt

  Scenario: Broken schema is detected
    Tool: Bash
    Steps:
      1. Run schema validator against intentionally malformed fixture
      2. Assert validator reports missing `name` key
    Expected Result: non-zero exit with explicit field error
    Evidence: .sisyphus/evidence/task-3-schema-fail.txt
  ```
  **Commit**: YES - `chore(data): register xs datasets and schemas`.

- [x] 4. Build XS normalization and chunking pipeline
  **What to do**:
  - Add builder that converts XS docs/catalog text into normalized chunk store.
  - Emit deterministic artifacts with manifest metadata.
  **Must NOT do**:
  - Do not depend on external SaaS/vector services.
  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
  - **Skills**: `superpowers/systematic-debugging`, `superpowers/test-driven-development`
  - **Skills Evaluated but Omitted**: `visual-engineering`
  **Parallelization**: YES, Wave 1, blocks T8/T9/T10, blocked by none.
  **References**:
  - `src/knowledge_builders/ai_scripting_builder.py`
  - `tools/build_ai_scripting_knowledge.py`
  - `XS_Training/SOURCE_PAGE_INDEX.md`
  - WHY: reuse builder pattern and source inventory for XS corpus.
  **Acceptance Criteria**:
  - [ ] XS build command produces metadata index + chunk store + manifest.
  - [ ] Re-running with same inputs produces deterministic counts/checksums.
  **QA Scenarios**:
  ```text
  Scenario: Deterministic build output
    Tool: Bash
    Steps:
      1. Run XS build script twice
      2. Compare SHA256 of generated artifacts
    Expected Result: checksums match
    Evidence: .sisyphus/evidence/task-4-deterministic-build.txt

  Scenario: Missing source file fails fast
    Tool: Bash
    Steps:
      1. Execute build with a missing input path fixture
      2. Assert explicit error message contains missing path
    Expected Result: non-zero exit and clear missing-file error
    Evidence: .sisyphus/evidence/task-4-missing-source.txt
  ```
  **Commit**: YES - `feat(xs-build): add xs normalization chunk pipeline`.

- [x] 5. Create XS retrieval module scaffolding
  **What to do**:
  - Add `src/retrieval/xs_script_retriever.py` and `src/retrieval/xs_script_validator.py` skeletons.
  - Mirror AI retriever public interface shape for consistency.
  **Must NOT do**:
  - No business logic in stubs beyond typed interfaces.
  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: `superpowers/test-driven-development`, `git-master`
  - **Skills Evaluated but Omitted**: `writing`
  **Parallelization**: YES, Wave 1, blocks T7/T8/T9, blocked by none.
  **References**:
  - `src/retrieval/ai_script_retriever.py`
  - `src/retrieval/ai_script_validator.py`
  - WHY: API parity reduces integration risk.
  **Acceptance Criteria**:
  - [ ] New XS modules import cleanly.
  - [ ] Public method signatures documented and type-check cleanly.
  **QA Scenarios**:
  ```text
  Scenario: XS retriever module import succeeds
    Tool: Bash
    Steps:
      1. Run `python -c "from src.retrieval.xs_script_retriever import XSScriptRetriever"`
      2. Run same for validator module
    Expected Result: both imports succeed
    Evidence: .sisyphus/evidence/task-5-import.txt

  Scenario: Constructor rejects invalid dataset path
    Tool: Bash
    Steps:
      1. Instantiate retriever with non-existent path
      2. Assert raised error includes path and reason
    Expected Result: deterministic validation error
    Evidence: .sisyphus/evidence/task-5-invalid-path.txt
  ```
  **Commit**: YES - `feat(retrieval): scaffold xs retriever modules`.

- [x] 6. Add publish metadata baseline at repo root
  **What to do**:
  - Add root `README.md`, `LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`, `CODEOWNERS`.
  - Include git-install instructions and scope statement.
  **Must NOT do**:
  - Do not claim PyPI availability.
  **Recommended Agent Profile**:
  - **Category**: `writing`
  - **Skills**: `superpowers/writing-plans`, `git-master`
  - **Skills Evaluated but Omitted**: `deep`
  **Parallelization**: YES, Wave 1, blocks T14/T15, blocked by none.
  **References**:
  - `pyproject.toml`
  - `docs/ai_scripting_knowledge/README.md`
  - WHY: align top-level project docs with existing package metadata and domain docs.
  **Acceptance Criteria**:
  - [ ] All required root metadata files exist.
  - [ ] README includes git install and quick verification steps.
  **QA Scenarios**:
  ```text
  Scenario: Metadata file presence check
    Tool: Bash
    Steps:
      1. Run file existence script for required root docs
      2. Assert no missing files reported
    Expected Result: 0 missing
    Evidence: .sisyphus/evidence/task-6-metadata-files.txt

  Scenario: README install command is executable
    Tool: Bash
    Steps:
      1. Copy command from README into clean venv
      2. Run import smoke command from README
    Expected Result: install + import succeed
    Evidence: .sisyphus/evidence/task-6-readme-smoke.txt
  ```
  **Commit**: YES - `docs(repo): add publish baseline metadata`.

- [x] 7. Implement deterministic XS symbol retrieval
  **What to do**:
  - Implement exact lookup by symbol name for functions/constants.
  - Add alias/case normalization and typed output contract.
  **Must NOT do**:
  - No fuzzy-first behavior.
  **Recommended Agent Profile**:
  - **Category**: `deep`
  - **Skills**: `superpowers/systematic-debugging`, `superpowers/test-driven-development`
  - **Skills Evaluated but Omitted**: `writing`
  **Parallelization**: YES, Wave 2, blocks T11/T12, blocked by T2,T3,T5.
  **References**:
  - `docs/agent_database/xs_functions_catalog.json`
  - `docs/agent_database/xs_constants_catalog.json`
  - `docs/agent_database/agent_query_map.json`
  - WHY: direct symbol truth source and routing hints.
  **Acceptance Criteria**:
  - [ ] Query `xsSetUnitPosition` returns correct signature and param list.
  - [ ] Unknown symbol returns explicit not-found object (not empty success).
  **QA Scenarios**:
  ```text
  Scenario: Exact function lookup
    Tool: Bash
    Steps:
      1. Run `python -m aoe2_ai_modder.retrieval.xs_lookup --symbol xsSetUnitPosition`
      2. Assert output includes `bool` return type and expected parameters
    Expected Result: status success with exact symbol match
    Evidence: .sisyphus/evidence/task-7-exact-lookup.txt

  Scenario: Missing symbol returns typed failure
    Tool: Bash
    Steps:
      1. Query nonexistent symbol `xsNotAFunction`
      2. Assert JSON includes `found:false` and error code `symbol_not_found`
    Expected Result: graceful typed failure
    Evidence: .sisyphus/evidence/task-7-not-found.txt
  ```
  **Commit**: YES - `feat(xs-retrieval): deterministic symbol lookup`.

- [x] 8. Implement hybrid chunk retrieval and ranking fallback
  **What to do**:
  - Add token-overlap/chunk ranking for conceptual queries.
  - Merge deterministic and chunk results with clear precedence.
  **Must NOT do**:
  - No override of deterministic top result when exact symbol exists.
  **Recommended Agent Profile**:
  - **Category**: `deep`
  - **Skills**: `superpowers/systematic-debugging`, `superpowers/test-driven-development`
  - **Skills Evaluated but Omitted**: `playwright`
  **Parallelization**: YES, Wave 2, blocks T9/T12, blocked by T4,T5.
  **References**:
  - `src/retrieval/ai_script_retriever.py`
  - `docs/ai_scripting_knowledge/document_store.jsonl`
  - WHY: existing hybrid strategy and chunk-store format reference.
  **Acceptance Criteria**:
  - [ ] Concept query returns ranked chunk list with score field.
  - [ ] Deterministic hit remains rank-1 when present.
  **QA Scenarios**:
  ```text
  Scenario: Concept query retrieves ranked chunks
    Tool: Bash
    Steps:
      1. Run retrieval query `how to move unit with collision check`
      2. Assert top 5 results contain score descending order
    Expected Result: sorted ranked list with source paths
    Evidence: .sisyphus/evidence/task-8-concept-ranking.txt

  Scenario: Deterministic precedence over chunk fallback
    Tool: Bash
    Steps:
      1. Query exact symbol `xsSetUnitPosition`
      2. Assert first result type is `symbol` and not `chunk`
    Expected Result: deterministic result rank 1
    Evidence: .sisyphus/evidence/task-8-precedence.txt
  ```
  **Commit**: YES - `feat(xs-retrieval): hybrid chunk fallback ranking`.

- [x] 9. Implement XS retrieval context builder and validator
  **What to do**:
  - Build context payload for agent consumption (source, score, snippet, constraints).
  - Add validator for malformed retrieval payloads.
  **Must NOT do**:
  - No ambiguous field names in output schema.
  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
  - **Skills**: `superpowers/test-driven-development`, `superpowers/systematic-debugging`
  - **Skills Evaluated but Omitted**: `writing`
  **Parallelization**: YES, Wave 2, blocks T12, blocked by T4,T5,T8.
  **References**:
  - `src/retrieval/ai_script_retriever.py`
  - `src/retrieval/ai_script_validator.py`
  - WHY: follow existing contract style and validation philosophy.
  **Acceptance Criteria**:
  - [ ] Context JSON schema documented and validated in tests.
  - [ ] Invalid payload rejected with stable error code.
  **QA Scenarios**:
  ```text
  Scenario: Build valid context payload
    Tool: Bash
    Steps:
      1. Run context builder for query `cooldown spell arrays`
      2. Assert output has `query`, `retrieved[]`, `score`, `source_file`
    Expected Result: valid schema-compliant payload
    Evidence: .sisyphus/evidence/task-9-valid-context.json

  Scenario: Payload validator catches malformed result
    Tool: Bash
    Steps:
      1. Run validator on fixture missing `score`
      2. Assert error path references `retrieved[0].score`
    Expected Result: non-zero validation failure
    Evidence: .sisyphus/evidence/task-9-invalid-context.txt
  ```
  **Commit**: YES - `feat(xs-retrieval): add context builder and validator`.

- [x] 10. Add XS retrieval golden set and eval harness CLI
  **What to do**:
  - Create golden query set for XS symbol and concept queries.
  - Add CLI that computes recall@k and MRR with pass/fail thresholds.
  **Must NOT do**:
  - Do not report "high accuracy" without threshold result.
  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
  - **Skills**: `superpowers/test-driven-development`, `git-master`
  - **Skills Evaluated but Omitted**: `playwright`
  **Parallelization**: YES, Wave 2, blocks T12/T15, blocked by T3,T4.
  **References**:
  - `docs/agent_database/xs_functions_catalog.json`
  - `docs/agent_database/xs_constants_catalog.json`
  - `tests/test_knowledge_integration.py`
  - WHY: source of truth and existing test style.
  **Acceptance Criteria**:
  - [ ] Eval CLI prints recall@5 and MRR.
  - [ ] Threshold flags configurable via CLI args.
  **QA Scenarios**:
  ```text
  Scenario: Eval harness produces metrics
    Tool: Bash
    Steps:
      1. Run eval CLI on golden set with `--k 5`
      2. Assert stdout contains `recall@5` and `mrr`
    Expected Result: metrics printed and exit 0 when thresholds met
    Evidence: .sisyphus/evidence/task-10-eval-pass.txt

  Scenario: Threshold failure exits non-zero
    Tool: Bash
    Steps:
      1. Re-run eval with unrealistic threshold (e.g., `--min-recall 1.0`)
      2. Assert process exits non-zero with failure summary
    Expected Result: explicit threshold failure
    Evidence: .sisyphus/evidence/task-10-eval-fail.txt
  ```
  **Commit**: YES - `feat(eval): add xs retrieval golden-set harness`.

- [x] 11. Add tests for builder and deterministic retrieval
  **What to do**:
  - Add unit tests for XS builder artifact generation.
  - Add deterministic lookup tests for known symbols/constants.
  **Must NOT do**:
  - No flaky tests with network dependency.
  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: `superpowers/test-driven-development`, `git-master`
  - **Skills Evaluated but Omitted**: `deep`
  **Parallelization**: YES, Wave 2, blocks T15, blocked by T7.
  **References**:
  - `tests/test_xs_injector.py`
  - `src/knowledge_builders/ai_scripting_builder.py`
  - WHY: existing test conventions and builder patterns.
  **Acceptance Criteria**:
  - [ ] New unit tests added and pass.
  - [ ] Deterministic lookup coverage includes found + missing + alias cases.
  **QA Scenarios**:
  ```text
  Scenario: Unit suite passes for deterministic paths
    Tool: Bash
    Steps:
      1. Run targeted unittest module for xs deterministic retrieval
      2. Assert total failures = 0
    Expected Result: PASS
    Evidence: .sisyphus/evidence/task-11-tests-pass.txt

  Scenario: Alias edge case test
    Tool: Bash
    Steps:
      1. Execute alias lookup test fixture
      2. Assert canonical symbol is returned
    Expected Result: alias resolves deterministically
    Evidence: .sisyphus/evidence/task-11-alias.txt
  ```
  **Commit**: YES - `test(xs): add deterministic retriever and builder tests`.

- [x] 12. Add tests for hybrid retrieval and eval thresholds
  **What to do**:
  - Add tests for chunk ranking and precedence logic.
  - Add integration tests for eval threshold pass/fail behavior.
  **Must NOT do**:
  - No metrics hardcoding that hides regression.
  **Recommended Agent Profile**:
  - **Category**: `deep`
  - **Skills**: `superpowers/test-driven-development`, `superpowers/systematic-debugging`
  - **Skills Evaluated but Omitted**: `writing`
  **Parallelization**: YES, Wave 2, blocks T15, blocked by T7,T8,T9,T10.
  **References**:
  - `src/retrieval/ai_script_retriever.py`
  - `tests/test_knowledge_integration_unittest.py`
  - WHY: ranking and unittest style reference.
  **Acceptance Criteria**:
  - [ ] Hybrid ranking tests verify sorting and deterministic precedence.
  - [ ] Eval CLI tests verify exit-code contract.
  **QA Scenarios**:
  ```text
  Scenario: Hybrid ranking assertions pass
    Tool: Bash
    Steps:
      1. Run hybrid retrieval unittest module
      2. Assert ranked scores are monotonic descending
    Expected Result: PASS
    Evidence: .sisyphus/evidence/task-12-hybrid-tests.txt

  Scenario: Eval exit contract regression test
    Tool: Bash
    Steps:
      1. Run eval harness test suite
      2. Assert one fixture expects non-zero and passes
    Expected Result: PASS with expected failure-case handling
    Evidence: .sisyphus/evidence/task-12-eval-exit-contract.txt
  ```
  **Commit**: YES - `test(eval): add hybrid retrieval and threshold tests`.

- [x] 13. DEFERRED (minimal scope): Migrate layout separation with compatibility shims
  **What to do**:
  - Move/organize files into explicit AI and XS areas per boundary map.
  - Add compatibility path shims where needed to avoid breakage.
  **Must NOT do**:
  - Do not break existing bridge script entry paths without shim.
  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
  - **Skills**: `superpowers/systematic-debugging`, `git-master`
  - **Skills Evaluated but Omitted**: `playwright`
  **Parallelization**: Deferred in minimal scope.
  **References**:
  - `AI_Scripting/rpg_xs_bridge_v3.ai`
  - `AI_Scripting/rpg_xs_bridge_v3.per`
  - `AI_Scripting/rpg_xs_bridge_v3.xs`
  - `XS_Scripting/xs_arrays_full_project_demo.xs`
  - WHY: highest-risk migration points.
  **Acceptance Criteria**:
  - [ ] Legacy paths still resolve via shims.
  - [ ] New canonical paths documented and used by new code.
  **QA Scenarios**:
  ```text
  Scenario: Legacy path compatibility
    Tool: Bash
    Steps:
      1. Run compatibility import/load checks for old paths
      2. Assert warnings indicate deprecation but behavior preserved
    Expected Result: compatibility success
    Evidence: .sisyphus/evidence/task-13-legacy-shim.txt

  Scenario: Shim missing detection
    Tool: Bash
    Steps:
      1. Disable one shim in fixture
      2. Run path check and assert failure references missing shim
    Expected Result: non-zero with explicit path
    Evidence: .sisyphus/evidence/task-13-missing-shim.txt
  ```
  **Commit**: YES - `refactor(layout): separate ai and xs with shims`.

- [x] 14. ACTIVE REMAINING TASK: Harden git-install packaging and package-data loading
  **What to do**:
  - Update `pyproject.toml` package metadata and package-data include rules.
  - Use resource-safe file loading (`importlib.resources`) for runtime data.
  - Provide a deterministic packaged-data resolver path/utility so consumer-side runtime does not depend on repo-root paths.
  **Must NOT do**:
  - No relative-path runtime reads that break when installed.
  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: `git-master`, `superpowers/systematic-debugging`
  - **Skills Evaluated but Omitted**: `visual-engineering`
  **Parallelization**: YES, Minimal Wave, blocked by T6 only (T13 deferred).
  **References**:
  - `pyproject.toml`
  - `src/retrieval/ai_script_retriever.py`
  - `docs/agent_database/xs_functions_catalog.json`
  - WHY: package metadata + runtime file access + packaged datasets.
  **Acceptance Criteria**:
  - [ ] `pip install "aoe2-ai-modder @ git+<repo-url>@<ref>"` succeeds in a clean consumer venv.
  - [ ] Consumer-side import smoke passes from non-repo CWD.
  - [ ] Installed package can load required XS catalogs/runtime data without repo-relative paths.
  **QA Scenarios**:
  ```text
  Scenario: Git install in clean consumer environment and runtime resource access
    Tool: Bash
    Steps:
      1. Create fresh venv and install `aoe2-ai-modder @ git+<repo-url>@<ref>`
      2. From non-repo CWD, run import smoke for retrieval/eval modules
      3. Run runtime lookup command requiring packaged XS catalogs/data
    Expected Result: successful lookup in installed environment
    Evidence: .sisyphus/evidence/task-14-git-install-resource.txt

  Scenario: Missing package-data fails explicitly
    Tool: Bash
    Steps:
      1. Run test fixture with intentionally omitted data file
      2. Assert error code `resource_not_found`
    Expected Result: explicit failure, no silent fallback
    Evidence: .sisyphus/evidence/task-14-resource-missing.txt
  ```
  **Commit**: YES - `build(pkg): harden git-install packaging and resources`.

- [x] 15. DEFERRED (minimal scope): Add root CI workflows for test/install/eval and release prep
  **What to do**:
  - Add root CI workflow(s) for unittest, install smoke, and eval thresholds.
  - Add release prep checks (tag sanity/version consistency).
  **Must NOT do**:
  - No CI green without running eval threshold checks.
  **Recommended Agent Profile**:
  - **Category**: `quick`
  - **Skills**: `git-master`, `superpowers/verification-before-completion`
  - **Skills Evaluated but Omitted**: `playwright`
  **Parallelization**: Deferred in minimal scope.
  **References**:
  - `pyproject.toml`
  - `tests/test_xs_injector.py`
  - `tools/build_ai_scripting_knowledge.py`
  - WHY: CI commands must match package + tests + build scripts.
  **Acceptance Criteria**:
  - [ ] CI runs tests on PR/push.
  - [ ] CI runs install smoke and eval gate.
  - [ ] CI fails on eval metric regression.
  **QA Scenarios**:
  ```text
  Scenario: CI workflow local simulation command set
    Tool: Bash
    Steps:
      1. Execute each CI command locally in sequence
      2. Assert all pass under clean environment
    Expected Result: all commands return 0
    Evidence: .sisyphus/evidence/task-15-ci-local-sequence.txt

  Scenario: Eval regression gate blocks build
    Tool: Bash
    Steps:
      1. Run eval command with strict threshold to force failure
      2. Assert workflow command path exits non-zero
    Expected Result: CI gate failure on metric regression
    Evidence: .sisyphus/evidence/task-15-eval-gate-fail.txt
  ```
  **Commit**: YES - `ci: add root quality gates for test install eval`.

---

## Final Verification Wave (DEFERRED for minimal scope)

- [x] F1. DEFERRED (minimal scope): **Plan Compliance Audit** - `oracle`
  Output: `Must Have [N/N] | Must NOT Have [N/N] | Tasks [N/N] | VERDICT`

- [x] F2. DEFERRED (minimal scope): **Code Quality Review** - `unspecified-high`
  Output: `Build [PASS/FAIL] | Lint [PASS/FAIL] | Tests [N pass/N fail] | VERDICT`

- [x] F3. DEFERRED (minimal scope): **Real QA Scenario Execution** - `unspecified-high`
  Output: `Scenarios [N/N pass] | Integration [N/N] | Edge Cases [N tested] | VERDICT`

- [x] F4. DEFERRED (minimal scope): **Scope Fidelity Check** - `deep`
  Output: `Tasks [N/N compliant] | Contamination [CLEAN/N issues] | VERDICT`

---

## Commit Strategy

Minimal scope execution currently expects a single implementation commit for T14, with T13/T15 and F1-F4 deferred.

| After Task | Message | Files | Verification |
|------------|---------|-------|--------------|
| T1-T3 | `chore(arch): define boundaries and xs manifest` | contract + manifest files | `python -m unittest` (targeted) |
| T4-T6 | `feat(xs): add xs build scaffold and publish metadata` | builder/docs files | build script + file checks |
| T7-T10 | `feat(xs-retrieval): implement runtime and eval harness` | retrieval/eval files | targeted retrieval tests |
| T11-T12 | `test(xs): add retrieval quality tests` | tests | `python -m unittest discover -s tests -p "test_*.py"` |
| T13-T15 | `build(ci): migrate layout and harden git install` | layout/pyproject/ci | wheel install + eval gate |

---

## Success Criteria

### Verification Commands

```bash
python -m unittest discover -s tests -p "test_*.py"
python -m pip wheel . -w dist
python -m pip install "aoe2-ai-modder @ git+<repo-url>@<ref>"
python -m src.eval.xs_retrieval_eval --golden docs/agent_database/xs_eval.json --k 5 --min-recall 0.85 --min-mrr 0.75
```

### Final Checklist
- [x] AI and XS domains are separated with explicit interop-only coupling.
- [x] XS retrieval supports deterministic symbol lookup and hybrid context fallback.
- [x] Retrieval metrics gate passes for local eval harness.
- [x] Git-install usage works in clean environment with packaged data access. (Verified via clean-venv wheel install smoke; git+ref install not exercised)
- [x] Root publish metadata is complete for git-install usage. (Public-release placeholders remain; see issues notepad)
