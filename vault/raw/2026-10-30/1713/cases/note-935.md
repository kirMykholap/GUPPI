# Note — Case 935 (lift carries `drop`)

## Questions
- Round 1, Q1 **Who guards the Criterion against a drop** — recommended (a) this Case adds a sub-case guarding the Criterion. Answer: (a).
- Settled in Case 931's round (person chose (b)): this Case adds `drop` to the Criterion list of `estimate-materialize-assembles` and to the key list of `rule-materialize`.

## Read
- case-schema.md, ratification.md, case-example.md (whole)
- vault/raw/2026-10-30/1713/cases/case-931.md (whole, second pass too: only context changed, agrees with 935)
- rule-materialize.md, estimate-materialize-assembles.md, estimate-materialize-changes-a-named-part-alone.md
- materialize.py: docstring 77-156, ITEM_KEYS 906-912, _lift_item 1013-1085, names_a_part/touches_criterion/lift_criterion 1102-1163, caller 1520
- prespec.py check_criterion_pairs 1631-1647
- tests: test_materialize.py 240-267, 2502-2523

## Open forks
- none

## To do
- Case file written; casecheck notes answered in context. Answer with summary.
