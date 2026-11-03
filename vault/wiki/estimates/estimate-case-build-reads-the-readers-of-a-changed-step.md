---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether no step, skill or place of code that reads the output of a step a Case changes, or does the same step, and that the change makes false, gets past the approved Spec unnamed by both case-guppi and /pre-spec and comes to light in the Work Mode or Retro of that session or of the session after it
method: "by hand, after the Retro of the session that follows a session whose approved Spec holds a Case of case-guppi that changes what a step writes, copies or shows or adds a path on which a step does so: the Work Mode and Retro of both sessions, read in their ledgers and in the transcripts of their main agents under ~/.claude/projects/, for a step, a skill or a place of code that reads the output of the changed step or does the same step, that the change makes false and that no Case and no context of the approved Spec named, such as a Case built again in Work Mode, a task added by hand, a red test or check or an error lesson for it, the count and the transcripts in the estimate line"
checked: 2026-11-02
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness, case-build]
core: true
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

2026-11-02, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
