# Problems

Append-only. Capture recurring problems, root causes, and mitigations.

- No unresolved XS build pipeline problems after implementation; deterministic checksums matched across two consecutive runs on identical input.
- Initial eval tests assumed top-rank hits would come from synthetic `xs-command:*` entries, but symbol-precedence retrieval produced `xs-symbol:*` first. Mitigation: match expected tokens by substring instead of exact title/source equality.
- Potential compatibility drift risk: earlier retrieval context rows used `source_file`; Task 9 mitigates this by pinning the new schema (`source`) in unit tests and validating every context payload before return.
- No new implementation blockers in Task 12 beyond pre-existing Python LSP unavailability; coverage hardening was completed with deterministic local fixtures and unittest.
