---
type: estimate
kind: QA
status: pending
target: "[[rule-guppi-package]]"
purpose: Whether /guppi:install stops and writes nothing when uv is missing, and builds the Python environment .guppi/.venv/ by uv sync after the copy, before it sends the person to /hi
method: "by hand, after a tag prod-x.y.z stands in the history of HEAD: the agent writes the clean version into a local folder by uv run --project .guppi guppi ship --allow-draft; then, at a stop of Work Mode, the person adds that folder as a catalogue, installs the plugin guppi from it and, in an empty project on the machine with uv, types /guppi:install, reopens Claude Code there and types /hi; in an empty project with Claude Code started from a terminal whose PATH holds no folder of uv, types /guppi:install; in an empty project with Claude Code started from a terminal with UV_OFFLINE=1 and UV_CACHE_DIR set to an empty folder, types /guppi:install; the person's answer on the output of each install, the files of each project and .guppi/.venv/ of the project with uv, read against the Criterion; the copy and the project with uv may be those of the reading of estimate-plugin-install-writes-guppi-into-an-empty-project at the same commit"
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
**－** When `uv --version` fails, it says that GUPPI needs the tool `uv`, and that the person installs it and types `/guppi:install` again, writes nothing and stops.
**－** When `uv sync --project .guppi` fails, it shows its output and stops, and does not tell the person to type `/hi`.

## History

- 2026-10-15 created · [[decision-case-819.4]]
- 2026-10-15 deferred · [[decision-case-831]]
- 2026-10-15 deferred · [[decision-case-832]]
- 2026-10-16 defer by decision-case-831 superseded · [[decision-case-846]]
- 2026-10-16 defer by decision-case-832 superseded · [[decision-case-846]]
- 2026-10-16 updated: the Criterion replaced whole — the install comes from a local copy that guppi ship --allow-draft writes, not from the branch prod; the method makes uv missing by the PATH of a terminal, makes uv sync fail offline and reads the person's answer · [[decision-case-846]]
