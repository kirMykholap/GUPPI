---
type: decision
case: "924"
status: current
create: ["[[estimate-case-build-reads-the-readers-of-a-changed-step]]"]
update: ["[[rule-case-build]]", "[[insight-case-build-changes-a-step-without-reading-its-readers]]"]
origin: raw/2026-10-30/0304/ledger.md#case-924
sprint: plugin
created: 2026-10-30
tags: [session, workflow, harness, case-build, prespec]
---

## Problem

`case-guppi` changes what a step writes, copies or shows from the one step in front of it, and does not read the steps and skills that read that output or do the same step, or the new path its own Case adds, so the Case holds for one step only and /pre-spec finds the rest after the person has ratified it.

## Recommend

- **Where the fix goes**
  - Recommended: (a) a new sentence in the paragraph of the Render on the checks before the summary, a new Estimate `estimate-case-build-reads-the-readers-of-a-changed-step`, and the Insight set actioned by this Case.
  - Answer: agreed, (a).
- **What the reading covers**
  - Recommended: (a) the steps of the harness texts: the rules in `vault/wiki/rules/` and the files under `.claude/`, the steps after it in the same text and the new path the Case adds.
  - Answer: agreed, (a).
- **Change**
  - Asked: the person agreed to the /pre-spec finding that the second part of the `method` read the /pre-spec of this session, whose Cases were built on the old Render, and so waited for no event that could show the behaviour.
  - Taken: that part now waits for the /pre-spec of the first session whose `case-guppi` runs on the Render this Case sets; the first part, the Render in the Spec read at the Retro, stays.

## History

- 2026-10-30 created · raw/2026-10-30/0304/ledger.md#case-924
