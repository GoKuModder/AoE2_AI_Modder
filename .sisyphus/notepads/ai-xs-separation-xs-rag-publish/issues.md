# Issues

Append-only. Track blockers, failures, and unexpected constraints.

- `lsp_diagnostics` could not run for Python files because `basedpyright-langserver` is not installed in this environment.
- `python` and `python3` executables are unavailable in shell; verification had to use `py -3` launcher.

- Root publish metadata files include placeholders that must be replaced before a public release (`<REPO_URL>`, `<ORG>/<REPO>`, `<SECURITY_CONTACT_EMAIL>`, `@your-github-handle`, `<COPYRIGHT_HOLDER>`).

- `lsp_diagnostics` cannot report on `.md` files because no markdown LSP server is configured in this environment.
- `pytest` is not installed (`py -3 -m pytest` fails with `No module named pytest`), so build determinism tests were implemented and verified with `unittest`.
- During Task 2 verification, `lsp_diagnostics` remained unavailable for new Python files for the same `basedpyright-langserver` missing dependency; syntax verification used `py -3 -m py_compile` as a fallback signal only.
- Initial validator logic joined manifest path with entry path relative to manifest's parent directory, but existing manifest entries use project-root-relative paths. Fixed by resolving paths directly from project root (current working directory).
- Task 10 verification still cannot run `lsp_diagnostics` on Python files because `basedpyright-langserver` is not installed; verification used `py -3 -m py_compile` as a syntax fallback.
- Task 8 verification still cannot satisfy Python `lsp_diagnostics` cleanliness checks in this environment because `basedpyright-langserver` is not installed; test verification continued via `py -3 -m unittest tests.test_xs_retrieval`.
- Task 7 verification still cannot use `lsp_diagnostics` for Python because `basedpyright-langserver` remains unavailable in the environment.
- Installing `basedpyright` via `py -3 -m pip install basedpyright` still did not expose a callable `basedpyright-langserver` binary to this shell, so `lsp_diagnostics` remains unavailable.
- Task 9 still cannot provide Python `lsp_diagnostics` cleanliness evidence because `basedpyright-langserver` is unavailable in this environment; verification used `py -3 -m unittest` and `py -3 -m py_compile`.
- Task 12 still cannot run Python `lsp_diagnostics` on changed tests because `basedpyright-langserver` is unavailable; verification used `py -3 -m unittest tests.test_xs_retrieval tests.test_xs_retrieval_eval` and `py -3 -m py_compile`.
- Task 14 still cannot provide Python `lsp_diagnostics` evidence in this environment; relied on unittest + wheel build + fresh-venv install smoke.
- Task 14 still cannot run Python `lsp_diagnostics` due to `basedpyright-langserver` unavailability; verification used `py -3 -m unittest` and `py -3 -m py_compile` instead.
- Task 14 (packaging verification) completed successfully without any issues - all existing functionality was already in place.
