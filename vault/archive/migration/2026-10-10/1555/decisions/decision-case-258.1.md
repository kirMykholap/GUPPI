---
type: decision
case: "258.1"
status: archived
create: ["[[estimate-generate-renames]]"]
update: ["[[rule-page-generation]]", index, case-schema, decisions-schema, glossary]
origin: raw/2026-09-20/0527/ledger.md#case-258.1
sprint: migration
created: 2026-09-20
tags: [harness, workflow, tests, ledger]
---

## Context

A decision is a `create`, `update`, `delete` or `defer`; the id of a page is its filename; `origin` is never rewritten. An `update` in a `then` block carries `set`, `sections`, `replace`, `change`; `guppi materialize` copies these keys from the item into the yaml, `guppi generate` (`rule-page-generation`, `guppi/generate.py`) applies them to the page found by its slug and writes a History line; a `create` on a taken slug it refuses with an error, never renaming. The links to a page live in the `[[slug]]` of bodies and in the `REF_FIELDS` — `parent`, `children`, `estimates`, `target`, `deferred_by`, `addressed_by`; lint checks them against live and archived pages; `log.md`, `brief.md` and `raw/` are not pages. `rule-page-generation` carries six Estimates, none about moving a file: the Case creates a seventh, `estimate-generate-renames`, the slug free. `rule-materialize` carries nine; `estimate-materialize-assembles` — the assembly of the yaml from ledger and Spec — keeps its Criterion: the key is added in code, the reading is pytest. The Rule-class files that describe `update`: `index.md` §3 and §5, `case-schema.md`, `decisions/schema.md`, `glossary.md`.

## Problem

A page cannot be renamed today except as a `create` of a new one and a `delete` of the old — losing History on the live page, signing Criteria twice, and leaving two pages for one thing. One decision has to change a slug so that the page stays the same page and every link to it in the vault names the new slug.

## History

- 2026-09-20 created · raw/2026-09-20/0527/ledger.md#case-258.1
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
