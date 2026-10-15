---
type: estimate
kind: QA
status: pending
target: "[[rule-guppi-package]]"
purpose: Whether /guppi:install stops and writes nothing when uv is missing, and builds the Python environment .guppi/.venv/ by uv sync after the copy, before it sends the person to /hi
method: "by hand, after the librarian's run of the session whose Work Mode builds this change: a local copy that uv run --project .guppi guppi ship --allow-draft writes into an empty folder, the plugin guppi installed from it; in an empty project on a machine whose search path holds no uv, /guppi:install typed and its output and the files of the project read; in an empty project on a machine with uv, /guppi:install typed, .guppi/.venv/ read and Claude Code reopened there, read against the Criterion"
deferred_by: ["[[decision-case-831]]", "[[decision-case-832]]"]
origin: raw/2026-10-15/0553/ledger.md#case-819.4
sprint: plugin
created: 2026-10-15
tags: [plugin, harness]
---

## Criterion

When:
The person installs the plugin `guppi` from the catalogue of the branch `prod` and types `/guppi:install` in an empty project open in Claude Code, as `rule-plugin-install` sets it.

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
