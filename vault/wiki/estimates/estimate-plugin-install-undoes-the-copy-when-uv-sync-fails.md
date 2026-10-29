---
type: estimate
kind: QA
status: passed
target: "[[rule-plugin-install]]"
purpose: Whether /guppi:install, when uv sync fails after the copy, shows its output, deletes every file and folder it wrote into the project, and sends the person to /guppi:install again, not to /hi
method: "by hand, after the librarian's run of the session that sets this Criterion, with a tag prod-x.y.z in the history of HEAD: the clean version written into a local folder by uv run --project .guppi guppi ship --allow-draft, that folder added as a catalogue by /plugin marketplace add and guppi installed from it by /plugin install guppi@guppi-marketplace; in an empty project with Claude Code started from a terminal with UV_OFFLINE=1 and UV_CACHE_DIR set to an empty folder, where uv --version passes, /guppi:install typed; its reply and the files and folders of the project before and after read against the Criterion"
checked: 2026-10-29
origin: raw/2026-10-16/0342/ledger.md#case-853
sprint: plugin
created: 2026-10-16
tags: [plugin, harness]
---

## Criterion

When:
The person types `/guppi:install` of `plugin/skills/install/SKILL.md` in an empty project open in Claude Code, where `uv --version` passes, and `uv sync --project .guppi` fails after the copy, such as with no network and an empty cache of `uv`.

Then:
The agent shows the output of `uv sync --project .guppi`.
**＋** It deletes each file it copied into the project and each folder it made there, `.guppi/` with `.guppi/.venv/` included, so that the project holds only what it held before `/guppi:install`.
**＋** It says that the install did not finish and that the project stands as before, and that the person types `/guppi:install` again once the cause that the output shows is fixed, and stops.
**－** It does not tell the person to run `uv sync`, to reopen Claude Code or to type `/hi`.
**－** It deletes no file or folder that stood in the project before `/guppi:install`, and nothing in the folder of the plugin.

## Result

2026-10-29, Work Mode of session 0327, install C, transcript 56092f88 of C:/tmp/guppi-0327-c, UV_OFFLINE=1 and an empty UV_CACHE_DIR: 467 files copied, uv sync --project .guppi EXIT=1 "Failed to download ruff==0.16.1 … Network connectivity is disabled"; the reply showed that output, removed .claude .github .guppi vault .gitattributes CLAUDE.md, ls -A of the folder prints nothing, said that GUPPI did not install and the folder is empty as before, and to type /guppi:install again once uv has network access, and sent the person to no /hi; the catalogue folder keeps its 470 files and no .venv

## History

- 2026-10-16 created · [[decision-case-853]]
- 2026-10-16 deferred · [[decision-case-862]]
- 2026-10-29 defer by decision-case-862 superseded · [[decision-case-900.5]]
- 2026-10-29 updated: the defer retired, the reading taken at the install stop of Work Mode · [[decision-case-900.5]]
- 2026-10-29 status: pending → passed · raw/2026-10-29/0327/ledger.md#L36
