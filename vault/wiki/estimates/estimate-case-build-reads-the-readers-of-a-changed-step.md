---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether no step, skill or place of code that reads the output of a step a Case changes, or does the same step, and that the change makes false, gets past the approved Spec unnamed by both case-guppi and /pre-spec and comes to light in the Work Mode or Retro of that session or of the session after it
method: "by hand, after the Retro of the session that follows a session whose approved Spec holds a Case of case-guppi that changes what a step writes, copies or shows or adds a path on which a step does so: the Work Mode and Retro of both sessions, read in their ledgers and in the transcripts of their main agents under ~/.claude/projects/, for a step, a skill or a place of code that reads the output of the changed step or does the same step, that the change makes false and that no Case and no context of the approved Spec named, such as a Case built again in Work Mode, a task added by hand, a red test or check or an error lesson for it, the count and the transcripts in the estimate line"
checked: 2026-11-02
origin: raw/2026-10-30/0304/ledger.md#case-924
sprint: plugin
created: 2026-10-30
tags: [session, workflow, harness, case-build]
---

## Criterion

When:
The person approves the Spec of a session whose Cases `case-guppi` built, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, and checked by `/pre-spec`, and a Case of that Spec changes what a step of a skill, an agent, a hook or a function of `.guppi/guppi/` writes, copies or shows, or adds a path on which a step does so.

Then:
Each step, skill or place of code that reads that output or does the same step, and that the change makes false, stands in a Case of the approved Spec, or the `context` of a Case names it and says why it stands.
**＋** A reader that a finding of `/pre-spec` named and that a Case built again took in counts as found.
**＋** No such reader comes to light in the Work Mode or the Retro of that session or of the session after it, by a Case built again, a task added by hand, a red test or check, or an `error` lesson.
**－** A text in a History line, in `log.md` or in `brief.md` is not such a reader.

## Result

2026-11-02, Work Mode of session 1337, the Work Mode and Retro of sessions 0039 and 0254 in their ledgers, spec.md, work.md and handoff.md and in the main transcripts f240d478 (ExitPlanMode at record 794, /work 816, /retro 977) and 68effdf4 (ExitPlanMode 630, /work 651, /retro 716) under ~/.claude/projects/c--PROJECTS-GUPPI/: 0 readers of a changed step that no Case and no context of the approved Spec of 0039 named came to light; no case-guppi called after approval in either session, no task added by hand, no red test (1891 passed in both), the only tool errors bashguard refusals of heredocs; the two path lines of guppi check on rule-link-graph-at-session-start in 0039 stand in Case 999.1, which deletes that page, as an expected red

## History

- 2026-10-30 created · [[decision-case-924]]
- 2026-10-30 status: pending → failed · raw/2026-10-30/2005/ledger.md#L54
- 2026-10-31 updated: pending again after the failed reading of session 2005, the Criterion written back unchanged; the method waits for the /pre-spec of the first session on the Render with the sentence on a new member of a list · [[decision-case-948.2]]
- 2026-10-31 updated: the method reads the findings of any such /pre-spec in the agent transcript of ask-guppi, the Criterion written back unchanged · [[decision-case-960.3]]
- 2026-10-31 status: pending → failed · raw/2026-10-31/0431/ledger.md#L43
- 2026-10-31 updated: pending again after the failed reading of session 0431, the Criterion written back unchanged; the method waits for the /pre-spec of the first session on the Render that follows a step to the one who carries it out · [[decision-case-966]]
- 2026-11-01 status: pending → failed · raw/2026-11-01/0141/ledger.md#L18
- 2026-11-01 updated: the Criterion replaced whole — the readers of a changed step include the places of the harness code; pending again after the failed reading of session 0141 · [[decision-case-985]]
- 2026-11-02 status: pending → failed · raw/2026-11-01/2227/ledger.md#L19
- 2026-11-02 updated: the Criterion replaced whole — a missed reader of a changed step counts only when it gets past the approved Spec and comes to light in that session or the session after it; pending again after the failed reading of session 2227 · [[decision-case-998]]
- 2026-11-02 status: pending → passed · raw/2026-11-02/1337/ledger.md#L16
