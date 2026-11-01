---
type: decision
case: "994"
status: current
update: ["[[rule-close]]", "[[rule-documentation]]", "[[estimate-close-reports-the-run]]"]
origin: raw/2026-11-01/2227/ledger.md#case-994
sprint: plugin
created: 2026-11-01
tags: [harness, workflow, git, librarian, session, render]
---

## Problem

The frame of the librarian asks for its report twice, as its last text and in its handback, while the hook copies only the last output and a run outside auto mode has no handback. A run that follows only one of the two steps departs from the frame, and nothing checks that the report is the last output.

## Recommend

- **How the close tells the librarian to give its report back**
  - Recommended: (a) the handback where the tool exists, else plain text: the report given once, as the last output, nothing after it.
  - Answer: agreed, (a).
- **Whether the stop at the first step says the same**
  - Recommended: (a) the same wording as the close, in step 1 of `rule-documentation`.
  - Answer: agreed, (a).
- **How the change is checked**
  - Recommended: (a) the Criterion of `estimate-close-reports-the-run` replaced with one more line, its purpose and method set anew, and a new reading after the next librarian run.
  - Answer: agreed, (a).

## History

- 2026-11-02 created · raw/2026-11-01/2227/ledger.md#case-994
