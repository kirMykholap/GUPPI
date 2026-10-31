---
type: decision
case: "956"
status: current
children: ["[[decision-case-956.2]]", "[[decision-case-956.3]]", "[[decision-case-956.4]]", "[[decision-case-956.5]]"]
origin: raw/2026-10-31/0431/ledger.md#case-956
sprint: plugin
created: 2026-10-31
tags: [hooks, harness, librarian, render, workflow, git, session]
---

## Problem

Claude Code refuses the librarian's `Write` of `report.md`, so no run can leave its report in the session folder, and `estimate-close-reports-the-run` cannot pass.

## Recommend

- **How the report reaches the disk**
  - Recommended: no recommendation, since what triggers the refusal of Claude Code is not checked and options (a) to (d) rest on it; (e) rests on nothing unchecked but undoes the aim of case 944.
  - Answer: (a), a script writes the file; the person added that what blocks the librarian should be understood, and pictured the librarian returning its report as text, a hook copying it, and the main agent sending the file instead of retyping the report.
- **A check for a missing report**
  - Recommended: (a) no new check.
  - Answer: (a).
- **What copies the text into the file**
  - Recommended: (c) a hook copies the returned report, and the main agent shows and commits it.
  - Answer: (c).
- **What `/handoff` shows the person**
  - Recommended: (a) the text of the file, and the returned text with one line that the file is missing when no file stands.
  - Answer: (a).
- **Finding out what triggers the refusal**
  - Recommended: (a) a probe by hand in Work Mode, its result kept as a `knowledge` lesson.
  - Answer: (a).
- **What happens to the report of this session's own run**
  - Recommended: (b) a one-off task commits it in this session.
  - Answer: (b).
- **Change**
  - Asked: Case 960 of this session sets that a reading by hand names where its evidence is saved, and asked that the methods of `estimate-handoff-dispatches` and `estimate-spec-box-runs-a-conserved-spec` read the dispatch line and the text shown to the person in the transcript of the session under `~/.claude/projects/`, the estimate line naming that transcript.
  - Taken: both methods now read the dispatch line and the text shown in the transcript of the session and name it in the estimate line; the method of `estimate-handoff-dispatches` names its event by its kind, with no "first". The method of 956.1, a command, already names where its evidence is saved and stands.
- **Change**
  - Asked: the findings of `ask-guppi` at `/pre-spec` on Case 956.
  - Taken: the new Rule gets `core` as a boolean and its `ref` to `rule-documentation`; the commit of `report.md` is allowed in the − line of 956.3 and 956.4; the method of `estimate-close-reports-the-run` also reads the librarian's last output in its agent transcript; the new Render of `rule-close` tells the librarian to write no text after its handback; Case 956.5 replaces the Criterion of `estimate-close-commits`, whose wording the commit of `report.md` made false; `context` names `estimate-end-of-work-order` and why it stands.

## History

- 2026-10-31 created · raw/2026-10-31/0431/ledger.md#case-956
- 2026-10-31 child decision-case-956.1 archived · cleanup
