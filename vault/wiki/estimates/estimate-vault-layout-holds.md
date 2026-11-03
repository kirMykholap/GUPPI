---
type: estimate
kind: QA
status: passed
target: "[[rule-vault-layout]]"
purpose: lint finds a page under the wrong category folder, a page whose slug is not its filename, and a .md at the root of wiki/ that no live rule page names; the live vault has none
method: uv run --project .guppi pytest .guppi/tests/test_lint.py -k layout, then uv run --project .guppi guppi check — no layout finding on the live vault
checked: 2026-09-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow]
core: true
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

2026-09-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
