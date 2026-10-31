# Note — Case 965 (Work Mode, replaces 956.1)

## Questions
- none asked; no round.

## Read for the frame
- vault/wiki/case-schema.md, vault/wiki/ratification.md, vault/wiki/case-example.md
- vault/raw/2026-10-31/0431/cases/case-956.md (whole); spec.md lines 55-94
- .guppi/guppi/ratified.py: code_value, fenced_value, sub_point_key, put, read_tasks
- .guppi/guppi/materialize.py: create_fields, _lift_item, lift_line, accepted_keys, ITEM_KEYS
- .guppi/guppi/generate.py: scalar, frontmatter, create, update (895-926), apply
- .guppi/guppi/prespec.py: core_as_left (1615-1625), check_form
- rule-rules-schema (core: [true]); ledger of 0431 (no error lessons)

## Finding
- put() YAML-parses only values opening with [ or {, and `set`; every other create
  sub-point (span or fence) is a string. No create form lifts core as a bool.
- Fix used: drop core from the create; an update of rule-librarian-report-copy with
  set {core: true} (YAML-parsed by put); generate applies entries in ledger order.

## Open forks
- none

## To do
- write case-965.md; answer with summary. Do not read Case 964.
