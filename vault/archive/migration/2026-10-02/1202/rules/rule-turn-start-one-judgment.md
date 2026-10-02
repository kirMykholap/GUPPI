---
type: rule
purpose: Prevents the start of the person's turn in a transcript from being judged by two predicates that can answer differently - turn_of_reply in guppi/casecheck.py, after the last user record not isMeta that holds more than tool results, and the stretch of guppi/ledger.py, after the last user record whose origin.kind is human; whether they are one judgment under rule-one-judgment-one-implementation
status: archived
origin: raw/2026-10-01/1725/ledger.md#case-586
sprint: migration
created: 2026-10-01
---

## Purpose

Prevents the start of the person's turn in a transcript from being judged by two predicates that can answer differently - turn_of_reply in guppi/casecheck.py, after the last user record not isMeta that holds more than tool results, and the stretch of guppi/ledger.py, after the last user record whose origin.kind is human; whether they are one judgment under rule-one-judgment-one-implementation

## History

- 2026-10-01 deferred, placeholder · [[decision-case-586]]
- 2026-10-02 defer by decision-case-586 superseded · [[decision-case-590.1]]
- 2026-10-02 deleted · [[decision-case-592]]
- 2026-10-02 archived · cleanup
