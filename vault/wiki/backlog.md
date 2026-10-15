# Backlog

19 items

## Conserved Specs

## Deferred

- `entity-guppi` — GUPPI — a Claude Code harness governed by ratified decisions, and the vault it keeps; its parts the sprint and the glossary, and in the repository of GUPPI also that repository on GitHub · put off in 1 session
- `entity-sprint-plugin` — GUPPI ships as a Claude Code plugin: a clean version built by CI on a branch of its own, on GitHub with a README and ready for pull requests from others, and the close of a sprint works with no fix by hand · put off in 1 session
- `rule-documentation` — Prevents a ratified decision from ending the session without becoming a vault page · put off in 0 sessions
- `rule-guppi-package` — Prevents a project with GUPPI from depending on files at its root that it does not own, or on a command that runs only in the repository of GUPPI · put off in 0 sessions
- `rule-lint` — Prevents a page that breaks the schema, points nowhere, or claims a status its Estimates do not support from sitting in the vault unnoticed · put off in 0 sessions
- `rule-page-generation` — Prevents a ratified decision from ending the session without a page, or a page from carrying a field nobody ratified · put off in 1 session
- `rule-rules-schema` — Prevents a Rule page from carrying a field or section outside the shape lint checks, or lacking one it needs · put off in 1 session
- `estimate-clean-branch-installs-as-a-plugin` — Whether the clean version holds the manifest of the plugin guppi and the catalogue guppi-marketplace, passes claude plugin validate, which CI runs before prod is written, and installs as a plugin with no error · put off in 1 session
- `estimate-guppi-package-is-ready-after-the-install` — Whether /guppi:install stops and writes nothing when uv is missing, and builds the Python environment .guppi/.venv/ by uv sync after the copy, before it sends the person to /hi · put off in 0 sessions
- `estimate-guppi-package-runs-from-its-own-folder` — Whether the code, the settings, the lock and the tests of GUPPI stand under .guppi/, every hook, skill, agent, Makefile line and page runs them through uv run --project .guppi, the modules and the guards take that form, and the clean version holds no pyproject.toml at its root · put off in 1 session
- `estimate-guppi-tests-green` — uv run --project .guppi guppi test is green on the branch — the whole suite of the harness · put off in 1 session
- `estimate-harness-pipeline` · put off in 1 session
- `estimate-page-schemas-one-file-per-rule` — Each vault/wiki/<category>/schema.yaml is written by guppi render from exactly one rule page, no schema.md remains, lint reads every file and a hand edit is refused · put off in 1 session
- `estimate-plugin-install-writes-guppi-into-an-empty-project` — Whether guppi ship puts the skill install into the clean version, and whether /guppi:install copies every file of the plugin but its own into a project that holds none of them, and writes nothing into one that holds one · put off in 1 session
- `insight-case-build-claims-what-code-does-without-reading-it` — case-guppi states what a function or a script of the code does, and builds a Case or a recommendation on that claim, without reading the function that decides it, so the claim proves false after the person has signed it and the Case is built again · severity 2 · put off in 0 sessions
- `insight-case-build-rests-on-an-unchecked-fact-of-a-tool` — case-guppi builds a Case on a fact of how an outside tool behaves — what GitHub accepts, which config file pytest reads from the root — that neither the round nor /pre-spec checked, so the fact proves false in Work Mode after the person ratified the Case · severity 2 · put off in 0 sessions
- `insight-workflow-code-live-before-the-page-it-reads` — A Case changes a reader in code and the text it reads in a page or a governed file; the code of the working tree runs at once, the page lands at the librarian's run and the file at the render, so the reader refuses or goes red in between, by construction. · severity 4 · put off in 14 sessions
- The category set as data: the person sets the categories of a project, the development set entity, rule, estimate by default, and the harness holds them as data, so a changed set rewrites no rule; taken out of rule-morph (case 802); the categories discussion of session 1119, vault/archive/migration/2026-09-17/1119/raw/categories-discussion.md · put off in 0 sessions
- `rule-work-mode` — Prevents implementation starting before the plan, branch and baseline exist · put off in 31 sessions
