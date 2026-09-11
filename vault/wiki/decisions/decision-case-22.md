---
type: decision
case: "22"
status: superseded
kind: [create, create]
target_slug: [rule-index, estimate-index-lists]
superseded_by: [decision-case-27]
origin: raw/2026-09-09/ledger.md#case-22
sprint: migration
created: 2026-09-09
tags: [harness, workflow]
---

## When

```
create:
  slug: rule-index
  type: rule
  kind: Leaf
  purpose: Prevents a pre-task check from reading every page of a category to learn what already exists
  enforcement: check
  implementation_ref: [guppi/index.py, tests/test_index.py, Makefile]
  parent: rule-documentation
  tags: [harness, workflow]
  estimate:
    slug: estimate-index-lists
    kind: QA
    criterion: against a temp vault — each category file holds exactly one line per live page in slug order with the field its schema names; an estimate line carries its whole criterion on one line; an archived page and a decision have no line; an empty category yields an empty file; --check exits 1 naming a stale file and 0 when all match, writing nothing. Against the live vault — five files appear, rules-index.md has one line per page of rules/, --check exits 0 right after
    method: pytest in tests/test_index.py; the live reading once by hand
update:
  slug: index
  file: vault/wiki/index.md
  change: the index file is `wiki/<category>-index.md` — §1 layout, §10 (librarian reads), §11; decisions still have none
```

`uv run guppi index` пишет `vault/wiki/<category>-index.md` для entities, rules,
estimates, lessons, insights: строка `slug: text`, по slug, файл есть и пустым. Текст —
`purpose` (entities, rules), `root_cause` (lessons), `pattern` (insights), `## Criterion`
в одну строку (estimates). Архив и decisions без строк. `--check` — сравнение, exit 1,
не пишет. Файлы коммитятся.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-22
- 2026-09-09 superseded by decision-case-27 · raw/2026-09-09/ledger.md#case-27
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
