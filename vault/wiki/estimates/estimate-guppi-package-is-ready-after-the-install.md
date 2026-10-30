---
type: estimate
kind: QA
status: passed
target: "[[rule-guppi-package]]"
purpose: Whether /guppi:install runs uv --version before it writes anything and, where it passes, asks nothing about uv, copies every file but .claude/settings.json, builds the Python environment .guppi/.venv/ by uv sync, and copies .claude/settings.json only then, before it sends the person to /hi
method: "by hand, at Retro of the session that sets this Criterion, with a tag prod-x.y.z in the history of HEAD: in the repository of GUPPI, the agent writes the clean version into a local folder by uv run --project .guppi guppi ship --allow-draft in Work Mode; then, at a stop of Work Mode, the person adds that folder as a catalogue, installs the plugin guppi from it and, in an empty project on the machine with uv, types /guppi:install, reopens Claude Code there and types /hi; the person's answer on the output of the install, the order of its steps, the files of the project and its .guppi/.venv/, read against the Criterion; the copy and the project may be those of the reading of estimate-plugin-install-runs-no-hook-before-uv-sync"
checked: 2026-10-30
origin: raw/2026-10-15/0553/ledger.md#case-819.4
sprint: plugin
created: 2026-10-15
tags: [plugin, harness]
---

## Criterion

When:
In the repository of GUPPI, the agent writes the clean version into a local folder by `uv run --project .guppi guppi ship --allow-draft <folder>`; the person adds that folder as a catalogue by `/plugin marketplace add <folder>`, installs the plugin by `/plugin install guppi@guppi-marketplace` and types `/guppi:install` in an empty project open in Claude Code, as `rule-plugin-install` sets it.

Then:
Before it writes anything, `/guppi:install` runs `uv --version`.
**＋** It copies each file of the install but `.claude/settings.json`, and then runs `uv sync --project .guppi` in the project, which builds the Python environment `.guppi/.venv/`.
**＋** Once `uv sync` passes, it copies `.claude/settings.json`, and then tells the person to reopen Claude Code and type `/hi`.
**＋** The hooks of the project find that environment built at the first `/hi`.
**－** Where `uv --version` passes, it asks nothing about `uv`.

## Result

2026-10-30, Retro of session 2005: the person's answer at the stop of Work Mode, "по a1 - проблем не заметил"; transcript 589efbd9 of p1-empty: uv --version first (uv 0.11.32), nothing asked about uv, 467 files copied without .claude/settings.json, uv sync --project .guppi exit 0 "Creating virtual environment at: .guppi\.venv", then .claude/settings.json copied, then the message to reopen Claude Code and type /hi; at the first /hi (transcript 73386ca9) the hooks ran and /sprint-open opened

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
- 2026-10-29 defer by decision-case-862 superseded · [[decision-case-900.3]]
- 2026-10-29 updated: the defer retired, the reading taken at the install stop of Work Mode; the method states that it runs where the command ship stands and names no Estimate the clean version leaves out · [[decision-case-900.3]]
- 2026-10-29 status: pending → passed · raw/2026-10-29/0327/ledger.md#L34
- 2026-10-29 updated: the Criterion replaced whole — the install copies every file but .claude/settings.json before uv sync, and that file after uv sync passes · [[decision-case-912.2]]
- 2026-10-30 updated: the Criterion replaced whole and the method set — both state that the install starts in the repository of GUPPI · [[decision-case-918.4]]
- 2026-10-30 updated: the Criterion replaced whole — the agent writes the clean copy; the reading at Retro of the session that sets it · [[decision-case-943.3]]
- 2026-10-30 status: pending → passed · raw/2026-10-30/2005/ledger.md#L50
