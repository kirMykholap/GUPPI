---
type: estimate
kind: QA
status: passed
target: "[[rule-guppi-config]]"
purpose: Whether the render puts the value of the key main_branch of the Render of rule-guppi-config in place of each {{main_branch}}, the code reads it from guppi.toml with main where it is missing, and both judge the value by one function
method: "uv run --project .guppi pytest .guppi/tests/test_config.py -k main_branch and uv run --project .guppi pytest .guppi/tests/test_render.py -k main_branch; by hand, after the librarian's run of the session that sets this method: guppi.toml read for main_branch = \"main\" and the output of uv run --project .guppi guppi render --check, recorded in the estimate line"
checked: 2026-11-26
origin: raw/2026-11-26/1515/ledger.md#case-1070.1
sprint: plugin
created: 2026-11-26
tags: [harness, render, git]
---

## Criterion

When:
`guppi render` builds the governed files from the `## Render` of the render pages, or a script of `.guppi/guppi/` asks `main_branch` of `.guppi/guppi/config.py` for the name of the main branch of the project.

Then:
Each `{{main_branch}}` in the `## Render` of a render page becomes, in the file it governs, the value of the key `main_branch` that the `## Render` of `rule-guppi-config` sets, as it stands.
**＋** The page keeps the placeholder, so the next render after a changed name writes the new name.
**＋** `main_branch` of `.guppi/guppi/config.py` gives the value of the key `main_branch` of `guppi.toml` at the root of the project, and `main` where the file is missing, does not parse or holds no such key.
**＋** The render and `main_branch` judge the value by one function of `.guppi/guppi/config.py`: a value that is not a string, is empty or holds a space is an error that names its source and the key.
**＋** A `{{main_branch}}` while the `## Render` of `rule-guppi-config` holds no key `main_branch`, or a value that function refuses, stops the run: nothing is written, the page and the key go to stderr, `guppi render` exits 1, and `guppi render --sync` exits 0 with the same line.
**＋** The `## Render` of `rule-guppi-config` holds `main_branch = "main"`, and `guppi.toml` holds it after the render.
**－** A run in which no `## Render` holds a placeholder reads no `rule-guppi-config` and needs none.
**－** The render reads the name from the `## Render` of `rule-guppi-config`, never from `guppi.toml`, which is its own output.

## Result

2026-11-26, /hi of session 2333, uv run --project .guppi pytest .guppi/tests/test_config.py .guppi/tests/test_render.py -k main_branch: 13 passed, 54 deselected; guppi.toml line 6 holds main_branch = "main"; uv run --project .guppi guppi render --check: exit 0, no line

## History

- 2026-11-26 created · [[decision-case-1070.1]]
- 2026-11-27 status: pending → passed · raw/2026-11-26/2333/ledger.md#L1
