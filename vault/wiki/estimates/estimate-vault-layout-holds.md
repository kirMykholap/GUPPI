---
type: estimate
kind: QA
status: pending
target: "[[rule-vault-layout]]"
purpose: lint finds a page under the wrong category folder, a page whose slug is not its filename, and a .md at the root of wiki/ that no live rule page names; the live vault has none
method: uv run pytest tests/test_lint.py -k layout, then make lint — no layout finding on the live vault
origin: raw/2026-09-22/1121/ledger.md#case-315
sprint: migration
created: 2026-09-22
tags: [harness, workflow]
---

## Criterion

When:
`guppi lint` reads the pages of the category folders of `vault/wiki/` and the `.md` files at its root.

Then:
A page whose `type` does not match its folder is a `layout` finding.
**＋** A page whose `slug` is not its filename without the extension is a `layout` finding.
**＋** A `.md` at the root of `vault/wiki/` whose name no live rule page carries — in `governs` or in its text — is a `layout` finding.
**＋** `read_vault` passes by the schema file of a category folder, so it is never judged as a page.
**－** A category folder that lacks its schema file gives no `layout` finding.

## Result

2026-09-22, uv run pytest tests/test_lint.py: 62 passed; make lint on the live vault — no layout finding, 81 findings as before

## History

- 2026-09-22 created · [[decision-case-315]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L92
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given out, the schema file not read as a page stated (case 490.7) · [[decision-case-490.7]]
