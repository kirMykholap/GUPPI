---
type: decision
case: "776"
status: current
update: ["[[rule-materialize]]", "[[estimate-materialize-marks-superseded]]"]
origin: raw/2026-10-12/1449/ledger.md#case-776
sprint: plugin
created: 2026-10-12
tags: [harness, workflow, ledger, librarian]
---

## Problem

The entry-level `superseded_by` of a yaml holds one Case. When two Cases retire the same Case, the yaml names only the last one on every entry. So an entry of `rule-skill-sprint-open` names a Case other than the one that set its page anew.

## Recommend

- **What should the entry's mark hold when two Cases retire the same Case?**
  - Recommended: (a) a list of every retiring Case, in ledger order; an older yaml with one value read as a list of one; a one-off migration that retires a reading writes a list of one; the tests that compare the field to one value compare it to a list.
  - Answer: agreed, (a).
- **Should the archived yaml of the earlier session be corrected?**
  - Recommended: (a) leave it as it stands; its Decision record of the earlier Case already names both sub-cases.
  - Answer: agreed, (a).
- **How is the change checked?**
  - Recommended: (a) replace the Criterion of `estimate-materialize-marks-superseded` whole and set its method anew to the `tests/test_materialize.py` tests of the mark, including a new test where two lines retire one Case, read at the Retro of this session.
  - Answer: agreed, (a).

## History

- 2026-10-12 created · raw/2026-10-12/1449/ledger.md#case-776
