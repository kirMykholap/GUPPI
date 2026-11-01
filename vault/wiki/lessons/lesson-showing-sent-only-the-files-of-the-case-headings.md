---
type: lesson
kind: error
root_cause: the main agent sent the file of each top-level Case it named in a heading, 992 and 991, and not each path the summary marks Built, while the check asks a SendUserFile call for every case file the summary names as built
status: new
origin: raw/2026-11-01/2038/ledger.md#L23
sprint: plugin
created: 2026-11-01
tags: [session, workflow]
---

## Trigger

at the showing of Cases 992 and 991 after /pre-spec, the casecheck Stop hook refused the reply: case 990 had no SendUserFile call on vault/raw/2026-11-01/2038/cases/case-990.md; the summary of case-guppi had marked both case-992.md and case-990.md Built

## Root cause

the main agent sent the file of each top-level Case it named in a heading, 992 and 991, and not each path the summary marks Built, while the check asks a SendUserFile call for every case file the summary names as built

## History

- 2026-11-01 created · raw/2026-11-01/2038/ledger.md#L23
