---
type: estimate
kind: QA
status: pending
target: "[[rule-guppi-package]]"
purpose: Whether /guppi:install runs uv --version before it writes anything and, where it passes, asks nothing about uv and builds the Python environment .guppi/.venv/ by uv sync after the copy before it sends the person to /hi
method: "by hand, after a tag prod-x.y.z stands in the history of HEAD: the agent writes the clean version into a local folder by uv run --project .guppi guppi ship --allow-draft; then, at a stop of Work Mode, the person adds that folder as a catalogue, installs the plugin guppi from it and, in an empty project on the machine with uv, types /guppi:install, reopens Claude Code there and types /hi; the person's answer on the output of the install, the files of the project and its .guppi/.venv/, read against the Criterion; the copy and the project may be those of the reading of estimate-plugin-install-writes-guppi-into-an-empty-project at the same commit"
checked: 2026-10-16
deferred_by: ["[[decision-case-862]]"]
origin: raw/2026-10-15/0553/ledger.md#case-819.4
sprint: plugin
created: 2026-10-15
tags: [plugin, harness]
---

## Criterion

When:
The person writes the clean version into a local folder by `uv run --project .guppi guppi ship --allow-draft <folder>`, adds that folder as a catalogue by `/plugin marketplace add <folder>`, installs the plugin by `/plugin install guppi@guppi-marketplace` and types `/guppi:install` in an empty project open in Claude Code, as `rule-plugin-install` sets it.

Then:
Before it writes anything, `/guppi:install` runs `uv --version`.
**＋** After it copies the files, it runs `uv sync --project .guppi` in the project, which builds the Python environment `.guppi/.venv/` before it tells the person to reopen Claude Code and type `/hi`.
**＋** The hooks of the project find that environment built at the first `/hi`.
**－** Where `uv --version` passes, it asks nothing about `uv`.

## Result

2026-10-16, /hi of session 0342, the person's answer on the three installs of session 0104: `C:\PROJECTS\test` passes; `C:\PROJECTS\test-no-uv` almost — the install said `uv` is missing and wrote nothing, but the person wants the agent to offer to install `uv`; `C:\PROJECTS\test-uv-offline` fails — `uv sync` failed and the install stopped but told the person to type `/hi` after a fix, which must change

## History

- 2026-10-15 created · [[decision-case-819.4]]
- 2026-10-15 deferred · [[decision-case-831]]
- 2026-10-15 deferred · [[decision-case-832]]
- 2026-10-16 defer by decision-case-831 superseded · [[decision-case-846]]
- 2026-10-16 defer by decision-case-832 superseded · [[decision-case-846]]
- 2026-10-16 updated: the Criterion replaced whole — the install comes from a local copy that guppi ship --allow-draft writes, not from the branch prod; the method makes uv missing by the PATH of a terminal, makes uv sync fail offline and reads the person's answer · [[decision-case-846]]
- 2026-10-16 status: pending → failed · raw/2026-10-16/0342/ledger.md#L4
- 2026-10-16 updated: the Criterion replaced whole — the missing uv is left to estimate-plugin-install-offers-to-install-uv and the failed uv sync to the Estimate of case 853, and the method drops the project with no uv and the offline project · [[decision-case-852.2]]
- 2026-10-16 deferred · [[decision-case-862]]
