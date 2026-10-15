---
type: estimate
kind: QA
status: passed
target: "[[rule-guppi-config]]"
purpose: Whether the render puts the names of the languages set in the Render of rule-guppi-config in place of the placeholders of every Render, and stops with nothing written on a placeholder, key or code it cannot resolve
method: "uv run --project .guppi pytest .guppi/tests/test_config.py and uv run --project .guppi pytest .guppi/tests/test_render.py -k placeholder; by hand, the first render after the librarian's run: CLAUDE.md names English and Russian where rule-language holds the placeholders, and guppi.toml holds documentation_lang and chat_lang"
checked: 2026-09-28
origin: raw/2026-09-28/1318/ledger.md#case-476.1
sprint: migration
created: 2026-09-28
tags: [harness, render]
---

## Criterion

When:
`guppi render` builds the governed files from the `## Render` of the render pages.

Then:
Each `{{documentation_lang}}` and `{{chat_lang}}` in the `## Render` of a render page becomes, in the file it governs, the name of the language whose code the `## Render` of `rule-guppi-config` sets for that key, by the table of `.guppi/guppi/config.py`.
**＋** The page keeps the placeholder, so the next render after a changed code writes the new name.
**＋** `guppi.toml` is written from the `## Render` of `rule-guppi-config`, like any file rendered in full.
**＋** A placeholder whose name is not a key, a key missing from `rule-guppi-config`, or a code the table does not hold stops the run: nothing is written, the page and the placeholder or key go to stderr, `guppi render` exits 1, and `guppi render --sync` exits 0 with the same line.
**＋** `guppi render --check` compares each governed file with the filled text.
**－** A run in which no `## Render` holds a placeholder reads no `rule-guppi-config` and needs none.
**－** The render reads the codes from the `## Render` of `rule-guppi-config`, never from `guppi.toml`, which is its own output.

## Result

2026-09-28, uv run pytest tests/test_config.py (9 passed) and uv run pytest tests/test_render.py -k placeholder (8 passed); by hand, session 2000: CLAUDE.md `## Language` names English and Russian, guppi.toml holds documentation_lang = "en" and chat_lang = "ru", uv run guppi render --check exit 0

## History

- 2026-09-28 created · [[decision-case-476.1]]
- 2026-09-28 status: pending → passed · raw/2026-09-28/2000/ledger.md#L18
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
