---
type: decision
case: "869"
status: current
create: ["[[estimate-case-build-reads-the-code-it-states]]"]
update: ["[[rule-case-build]]", "[[insight-case-build-claims-what-code-does-without-reading-it]]"]
supersedes: ["[[decision-case-835]]"]
origin: raw/2026-10-16/2104/ledger.md#case-869
sprint: plugin
created: 2026-10-16
tags: [session, workflow, harness, case-build, ci]
---

## Problem

`case-guppi` can state what a function or a script of the repository does without reading the function that decides it. A Case the person signed then rests on a false claim and is built again.

## Recommend

- **What happens to this pattern**
  - Recommended: (a) fix it: add a duty to `rule-case-build`, set the Insight `actioned` and retire its defer.
  - Answer: agreed, (a).
- **How wide the duty to read the code is**
  - Recommended: (a) every claim about code in a round, `context`, `then` or a page text, the whole deciding function read, the file and the function named in `context`.
  - Answer: agreed, (a).
- **How the fix is checked**
  - Recommended: (a) a new Estimate `estimate-case-build-reads-the-code-it-states` on `rule-case-build`.
  - Answer: agreed, (a).
- **Change**
  - Asked: by findings of `/pre-spec`: the `context` overstated what the Render lacks, it did not name `estimate-case-build-offers-a-page-for-code-no-page-covers`, and the `method` of the new Estimate counted findings at the `/pre-spec` of this session, whose Cases were built under the old Render.
  - Taken: the `context` names the sentences of cases 752, 754 and 803 that already read code for set tasks, and says why the Criterion of `estimate-case-build-offers-a-page-for-code-no-page-covers` does not clash with the new sentence. The count of findings in the `method` waits for the first `/pre-spec` of a session whose Cases were built under the new Render.

## History

- 2026-10-17 created · raw/2026-10-16/2104/ledger.md#case-869
