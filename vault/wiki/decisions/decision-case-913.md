---
type: decision
case: "913"
status: current
update: ["[[rule-close]]", "[[estimate-close-reports-the-run]]"]
origin: raw/2026-10-29/2341/ledger.md#case-913
sprint: plugin
created: 2026-10-29
tags: [harness, workflow, git, librarian]
---

## Problem

The report of the librarian follows a list in `rule-close` that the other steps of its own frame contradict. That list ends with "Nothing else" and a twenty-line limit, while those steps send more parts to the report. The report then adds parts that no step asks for, such as test results and a list of files. The Estimate that checks the report checks neither those parts nor their absence.

## Recommend

- **What the reading of the report stands on**
  - Recommended: (a) a new reading from the report as shown, written by the main agent; no Case for it.
  - Answer: agreed, (a); the person then said they had looked at another report.
- **The created count in the brief**
  - Recommended: (a) an error lesson line by the main agent; this Case changes nothing for it.
  - Answer: agreed, (a).
- **What the report may hold beyond the list of `rule-close`**
  - Recommended: (a) Case 913 rewrites the list: the counts, the marks, the archived pages, the flags, the lint total and each read and refusal another step sends to the report; no test results and no list of files.
  - Answer: agreed, (a).
- **The commit command that failed once**
  - Recommended: (a) a new Frontier item on `estimate-close-commits`; Case 913 does not cover it.
  - Answer: agreed, (a).
- **How the new list is checked**
  - Recommended: (a) replace the Criterion and the purpose of `estimate-close-reports-the-run`; it goes back to `pending`.
  - Answer: agreed, (a).
- **The twenty-line limit**
  - Recommended: (a) keep twenty lines.
  - Answer: (b) drop the limit; the person sees no point in it.
- **How the list names the other parts**
  - Recommended: (a) one pointer to the other steps of the frame.
  - Answer: agreed, (a).
- **The name of the Estimate, now that the limit is gone**
  - Recommended: (a) rename it to `estimate-close-reports-the-run`.
  - Answer: (a).
- **Change**
  - Asked: the person agreed with the fix of a pre-spec finding: name `estimate-spec-box-runs-a-conserved-spec`, and say that the exit code of the tests that `/box` shows is a line of its own beside the report, not a part of the report.
  - Taken: `given` names that Estimate, `then` gains a `－` line on the exit code, the `method` leaves that line out of the report, and `context` says why that Criterion stands.
- **Change**
  - Asked: the person agreed with the fix of a pre-spec finding: name the Estimates that set the parts other steps send to the report, and add the Greps of the index check to the list of those parts.
  - Taken: `context` names `estimate-index-check-merges`, `estimate-synthesis-clusters` and `estimate-documentation-completes` as covered by the pointer of the new list and says why each stands, and its list of parts adds each Grep of the index check with its number of lines.

## History

- 2026-10-30 created · raw/2026-10-29/2341/ledger.md#case-913
