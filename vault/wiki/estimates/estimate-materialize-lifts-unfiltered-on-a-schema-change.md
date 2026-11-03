---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: A create of a category whose schema rule the same unit creates or updates is lifted with every key into fields and no unknown; a unit without that entry is lifted by the schema on disk
method: uv run --project .guppi pytest .guppi/tests/test_materialize.py::test_a_create_of_a_category_whose_schema_rule_the_unit_changes_is_lifted_whole .guppi/tests/test_materialize.py::test_a_schema_line_after_the_create_still_lifts_it_whole .guppi/tests/test_materialize.py::test_without_a_schema_line_the_lift_filters_as_before — a unit with update rule-rules-schema and create rule-x carrying a key the disk schema lacks, the key in fields and no unknown, with the schema line before and after the create; the same create without the schema entry, unknown as before
checked: 2026-09-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, librarian]
core: true
---

## Criterion

When:
`materialize` walks a unit whose ledger holds a decision line, a `create` or an `update`, with the slug `rule-<category>-schema`.

Then:
A `create` of that category in the same unit is lifted whole: every key goes into `fields`, and no key is `unknown`, wherever the schema entry stands in the Spec, before or after.
**＋** The pages the librarian writes carry the field before `render` lands the schema on disk.
**－** In a unit without such an entry, and for the other categories of the same unit, a `create` is lifted by `vault/wiki/<category>/schema.yaml` on disk: a key outside the schema is `unknown` and does not reach `fields`.

## Result

2026-09-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
