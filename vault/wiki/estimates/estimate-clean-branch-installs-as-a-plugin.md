---
type: estimate
kind: QA
status: passed
target: "[[rule-clean-branch]]"
purpose: Whether the clean version holds the manifest of the plugin guppi and the catalogue guppi-marketplace, passes claude plugin validate, which CI runs before prod is written, and installs as a plugin with no error
method: "uv run --project .guppi pytest .guppi/tests/test_ship.py; by hand, after a tag prod-x.y.z stands in the history of HEAD: uv run --project .guppi guppi ship --allow-draft into an empty local folder, claude plugin validate run on that folder, the two files of its .claude-plugin/ and the step of .github/workflows/prod.yml that runs claude plugin validate read against the Criterion, then the person's answer after the person adds that folder as a catalogue by /plugin marketplace add <folder> and installs guppi by /plugin install guppi@guppi-marketplace in an empty project open in Claude Code"
checked: 2026-10-16
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

2026-10-16, /hi of session 0342, the person's answer: in every test folder of session 0104 the catalogue `scratchpad/ship-plugin` added and the plugin `guppi` installed from it with no error

## History

- 2026-10-15 created · [[decision-case-816.1]]
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 status: pending → failed · raw/2026-10-15/1739/ledger.md#L12
- 2026-10-15 deferred · [[decision-case-831]]
- 2026-10-16 defer by decision-case-831 superseded · [[decision-case-842]]
- 2026-10-16 updated: read again once a tag prod-x.y.z stands; the Criterion stands, the method waits for the tag and names the person's install · [[decision-case-842]]
- 2026-10-16 status: pending → passed · raw/2026-10-16/0342/ledger.md#L3
