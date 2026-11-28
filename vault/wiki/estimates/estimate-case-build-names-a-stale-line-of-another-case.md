---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi, on a note that lists the Case file of another Case of the session, reads it, and names each line there that its change makes false with the change it needs on a line Other Case of its summary, or fixes its own Case where it is the one that is wrong
method: "by hand, after the first build in a session on the new Render of rule-case-build in which the note of the hook of rule-case-check lists the Case file of another Case of the session: the agent transcript of that case-guppi under ~/.claude/projects/, its case file and its summary read against the Criterion, the transcript in the estimate line"
checked: 2026-11-27
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [session, workflow, harness, case-build]
core: true
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, gets from the `SubagentStop` hook of `rule-case-check` a note that lists a file `raw/<date>/<hi HHMM>/cases/case-<M>.md` of another Case of the session, and answers again.

Then:
It reads that Case file whole by `Read`, as it reads each Case file of the session that a note names, and judges each line there that rests on what its own Case changes.
**＋** Where its change makes such a line false and the other Case should change, its `context` names that Case, the line and the change it needs, and the item of its Case in the summary carries a line `**Other Case:**` that names that Case and the change.
**＋** Where its own Case is the one that is wrong, it fixes its own Case instead.
**－** It reads no listed file of a Case that its prompt or a message names as built at the same time; its `context` names that Case and says why the file is not read.
**－** A line that its change leaves true needs no line `**Other Case:**`.

## Result

2026-11-27, passed in the repository of GUPPI.

## History

- 2026-11-28 shipped with GUPPI
