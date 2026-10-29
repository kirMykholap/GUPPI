---
type: lesson
kind: error
root_cause: case-guppi judged the readers of the `Branch:` line by the path in a repository alone and did not follow the new path its own Case adds, so the claim held for the old path only
status: clustered
insight: "[[insight-case-build-changes-a-step-without-reading-its-readers]]"
origin: raw/2026-10-16/0342/ledger.md#L21
sprint: plugin
created: 2026-10-16
tags: [case-build, prespec]
---

## Trigger

the context of Case 851 claimed that step 4 of rule-skill-sprint-open, step 1 of rule-skill-merge-main and their Estimates stand, and ask-guppi at /pre-spec found that on the yes path `Branch:` still read `none: …`, which step 4 would take for the branch of a closed sprint

## Root cause

case-guppi judged the readers of the `Branch:` line by the path in a repository alone and did not follow the new path its own Case adds, so the claim held for the old path only

## History

- 2026-10-16 created · raw/2026-10-16/0342/ledger.md#L21
- 2026-10-29 updated: clustered under insight-case-build-changes-a-step-without-reading-its-readers (synthesis) · raw/2026-10-29/1930/ledger.md#L26
