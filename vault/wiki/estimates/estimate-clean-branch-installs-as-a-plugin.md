---
type: estimate
kind: QA
status: failed
target: "[[rule-clean-branch]]"
purpose: Whether the clean version holds the manifest of the plugin guppi and the catalogue guppi-marketplace, passes claude plugin validate, which CI runs before prod is written, and installs as a plugin with no error
method: "uv run --project .guppi pytest .guppi/tests/test_ship.py; by hand, after the Work Mode of this change: uv run --project .guppi guppi ship --allow-draft into an empty local folder, claude plugin validate run on that folder, the two files of its .claude-plugin/ and the step of .github/workflows/prod.yml that runs claude plugin validate, and in an empty project an add of that folder as a catalogue and an install of guppi from it, read against the Criterion"
checked: 2026-10-15
deferred_by: ["[[decision-case-831]]"]
origin: raw/2026-10-15/0553/ledger.md#case-816.1
sprint: plugin
created: 2026-10-15
tags: [ci, plugin]
---

## Criterion

When:
`uv run --project .guppi guppi ship <folder>`, or `uv run --project .guppi guppi ship --allow-draft <folder>` into a local folder, builds the clean version, as `rule-clean-branch` sets it, and `claude plugin validate` runs on that folder.
**＋** In an empty project, someone adds that folder to Claude Code as a catalogue and installs the plugin `guppi` from it.

Then:
`uv run --project .guppi guppi ship <folder>` writes `.claude-plugin/plugin.json` into the clean version, copied from `plugin/plugin.json`, with the `name` `guppi`, a description, the author `kirMykholap` and the repository of the project on GitHub.
**＋** It writes `.claude-plugin/marketplace.json`, copied from `plugin/marketplace.json`, with the `name` `guppi-marketplace`, the owner `kirMykholap` and one entry, the plugin `guppi`, whose source is the root of the branch.
**＋** `claude plugin validate` passes on that folder.
**＋** Before a run of `.github/workflows/prod.yml` commits, it runs `claude plugin validate` on the clean folder.
**＋** The catalogue adds to Claude Code, and the plugin `guppi` installs from it, with no error.
**－** A run whose `claude plugin validate` fails fails and writes nothing to `prod`.
**－** The clean version holds no folder `plugin/`, and this repository holds no folder `.claude-plugin/`.
**－** Which skills the installed plugin `guppi` loads is no part of this promise.

## Result

2026-10-15, Retro, not read: uv run --project .guppi pytest .guppi/tests/test_ship.py passed (50), but the by-hand part needs uv run --project .guppi guppi ship --allow-draft, which exits 1 with no tag prod-x.y.z in the history; the tag is the stop task of Case 816.2, not placed; the install in an empty project was not run

## History

- 2026-10-15 created · [[decision-case-816.1]]
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 status: pending → failed · raw/2026-10-15/1739/ledger.md#L12
- 2026-10-15 deferred · [[decision-case-831]]
