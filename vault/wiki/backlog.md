# Backlog

17 items

## Conserved Specs

## Deferred

- `entity-guppi` — GUPPI — a Claude Code harness governed by ratified decisions, and the vault it keeps; its parts the sprint and the glossary, and in the repository of GUPPI also that repository on GitHub · put off in 1 session
- `rule-documentation` — Prevents a ratified decision from ending the session without becoming a vault page · put off in 0 sessions
- `rule-guppi-package` — Prevents a project with GUPPI from depending on files at its root that it does not own, or on a command that runs only in the repository of GUPPI · put off in 0 sessions
- `rule-lint` — Prevents a page that breaks the schema, points nowhere, or claims a status its Estimates do not support from sitting in the vault unnoticed · put off in 0 sessions
- `rule-page-generation` — Prevents a ratified decision from ending the session without a page, or a page from carrying a field nobody ratified · put off in 1 session
- `estimate-git-context-offers-git-init` — Whether /hi in a folder that is no git repository asks to run git init -b main, runs it on the person's yes and ends, ends on a no, and opens no sprint and writes no Frontier either way · put off in 0 sessions
- `estimate-guppi-package-is-ready-after-the-install` — Whether /guppi:install runs uv --version before it writes anything and, where it passes, asks nothing about uv and builds the Python environment .guppi/.venv/ by uv sync after the copy before it sends the person to /hi · put off in 0 sessions
- `estimate-page-schemas-one-file-per-rule` — Each vault/wiki/<category>/schema.yaml is written by guppi render from exactly one rule page, no schema.md remains, lint reads every file and a hand edit is refused · put off in 1 session
- `estimate-plugin-install-offers-to-install-uv` — Whether /guppi:install, where uv is missing, asks to install uv by its standalone installer, stops with nothing written on a no, and on a yes goes on once uv --version passes or sends the person to a new terminal · put off in 0 sessions
- `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails` — Whether /guppi:install, when uv sync fails after the copy, shows its output, deletes every file and folder it wrote into the project, and sends the person to /guppi:install again, not to /hi · put off in 0 sessions
- `insight-case-build-claims-what-code-does-without-reading-it` — case-guppi states what a function or a script of the code does, and builds a Case or a recommendation on that claim, without reading the function that decides it, so the claim proves false after the person has signed it and the Case is built again · severity 3 · put off in 0 sessions
- `insight-case-build-opens-a-new-case-where-one-was-named` — case-guppi opens a new top-level Case under a new number where the main agent named an existing Case to change, so the named Case stays as it was and the Cases that name it are built again · severity 2 · put off in 0 sessions
- `insight-case-build-rests-on-an-unchecked-fact-of-a-tool` — case-guppi builds a Case on a fact of how an outside tool behaves — what GitHub accepts, which config file pytest reads from the root — that neither the round nor /pre-spec checked, so the fact proves false in Work Mode after the person ratified the Case · severity 2 · put off in 0 sessions
- `insight-subagents-read-a-sibling-mid-flight` — agents that work at once read files that another agent of the same run is still writing, so what one agent reads or measures is the other agent's half-done state, not its result · severity 2 · put off in 0 sessions
- `insight-workflow-code-live-before-the-page-it-reads` — A Case changes a reader in code and the text it reads in a page or a governed file; the code of the working tree runs at once, the page lands at the librarian's run and the file at the render, so the reader refuses or goes red in between, by construction. · severity 4 · put off in 14 sessions
- The category set as data: the person sets the categories of a project, the development set entity, rule, estimate by default, and the harness holds them as data, so a changed set rewrites no rule; taken out of rule-morph (case 802); the categories discussion of session 1119, vault/archive/migration/2026-09-17/1119/raw/categories-discussion.md · put off in 0 sessions
- `rule-work-mode` — Prevents implementation starting before the plan, branch and baseline exist · put off in 31 sessions
