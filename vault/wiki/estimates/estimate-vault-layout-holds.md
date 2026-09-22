---
type: estimate
kind: QA
status: passed
target: "[[rule-vault-layout]]"
purpose: lint finds a page under the wrong category folder, a page whose slug is not its filename, and a .md at the root of wiki/ that no live rule page names; the live vault has none
method: uv run pytest tests/test_lint.py -k layout, then make lint — no layout finding on the live vault
origin: raw/2026-09-22/1121/ledger.md#case-315
sprint: migration
created: 2026-09-22
tags: [harness, workflow]
---

## Criterion

Given:
`read_vault` reads the `*.md` of a category folder but `schema.yaml`; a file at the root of `wiki/` it does not read (`guppi/pages.py`).
**＋** Every file of `wiki/` is a page, the Render of a page under `governs`, or a record a script keeps by a named rule: `sprint.md` and `glossary.md` under `rule-sprint` and `rule-glossary`, `case-schema.md` under `rule-case-protocol`, `brief.md` by the frame of `rule-brief`, `log.md` from `generate` and `cleanup`, `tags.md` the registry of ratified tags.
**＋** `tests/test_lint.py` fixes the behaviour on a temp vault.

When:
`guppi lint` reads the vault.

Then:
A page whose `type` does not match its folder is a `layout` finding.
**＋** A page whose `slug` is not its filename without the extension is a `layout` finding.
**＋** A `.md` at the root of `wiki/` whose name no live rule page carries — in `governs` or in its text — is a `layout` finding.
**－** A category folder without a `schema.yaml` is the finding it is today, not this one.

## Result

2026-09-22, uv run pytest tests/test_lint.py: 62 passed; make lint on the live vault — no layout finding, 81 findings as before

## History

- 2026-09-22 created · [[decision-case-315]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L92
