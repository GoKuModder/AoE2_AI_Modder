# Agent Docs

This folder contains the agent-facing layer of the repository. It is separated from the raw/generated datasets so an agent can first learn how to use the repo and only then open the right data source.

## Subfolders

- `navigation/`
  Global onboarding, routing rules, cross-domain workflows, and the repo-wide knowledge map.
- `domains/`
  One guide per core domain plus focused sub-guides for areas that need deeper retrieval, such as parser conditions and effects inside `scenario triggers`.
- `scenario_builder/`
  Task-oriented docs for building scenarios from idea documents, including trigger lookup, parser-manager usage, XS project-file generation, and Genie workflow implementation.
- `routing/`
  Machine-readable maps that help route queries to the right domain or dataset.
- `references/`
  Curated external project references plus normalized architecture-pattern and compact recipe datasets.
- `examples/`
  Curated example scripts intended to stay readable and publishable.

## Recommended Use

1. Start with `AGENT_START_HERE.md`.
2. Open `navigation/KNOWLEDGE_MAP.md`.
3. Open `scenario_builder/WHERE_TO_FIND_THINGS.md` if the task is implementation-heavy or scenario-building oriented.
4. Open the right domain guide in `domains/`.
5. Use `routing/` and `references/` when the task needs structured routing or project-scale examples.
