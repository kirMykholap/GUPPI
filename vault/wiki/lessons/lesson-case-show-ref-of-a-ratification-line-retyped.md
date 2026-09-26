---
type: lesson
kind: error
root_cause: the main agent retyped the Case from the subagent's report instead of copying the stored answer, and changed a ref it took for a slip; a showing retyped by hand can differ in any line, and only the comparison on Stop, which lets the re-fire through, stands between it and the person
status: clustered
insight: "[[insight-case-show-built-case-retyped-by-hand]]"
origin: raw/2026-09-26/1337/ledger.md#L20
sprint: migration
created: 2026-09-26
tags: [session, harness]
---

## Trigger

the first showing of Case 436.4 again in Work Mode carried `{ref:rule-case-check}` on its second ratification line where the answer of case-guppi held `{ref:estimate-case-check-sends-back-a-faulty-case}`; the Stop comparison of casecheck refused it with "case 436.4: differs from the answer of case-guppi", and the answer was shown again from the store

## Root cause

the main agent retyped the Case from the subagent's report instead of copying the stored answer, and changed a ref it took for a slip; a showing retyped by hand can differ in any line, and only the comparison on Stop, which lets the re-fire through, stands between it and the person

## History

- 2026-09-26 created · raw/2026-09-26/1337/ledger.md#L20
- 2026-09-26 updated: clustered into insight-case-show-built-case-retyped-by-hand · raw/2026-09-26/1337/ledger.md#L20
