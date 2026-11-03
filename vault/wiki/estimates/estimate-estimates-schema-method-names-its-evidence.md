---
type: estimate
kind: QA
status: passed
target: "[[rule-estimates-schema]]"
purpose: Whether each reading by hand of a method that a Spec creates or sets pending names the file, command or transcript where its evidence is saved, reads a text of a chat in its transcript, and names an event by its kind
method: "by hand, at Retro: the method of each Estimate that a Case of the session's spec.md creates or sets pending, read against the Criterion, each fault counted in the estimate line"
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [schema, workflow]
core: true
---

## Criterion

When:
At the Retro of a session, the `method` of each Estimate that a Case of its Spec `raw/<date>/<hi HHMM>/spec.md` creates or sets `pending` is read.

Then:
Each reading by hand in such a method names the place where its evidence is saved: a file of the repository, the output of a command, or the transcript of a session under `~/.claude/projects/`.
**＋** A reading whose evidence is a reply, a text shown to the person or the output of an agent reads it in the transcript of the session where it stood.
**＋** A reading that waits for an event names the kind of the event, and the word "first" stands only for an event that has never happened.
**－** No reading by hand names a text of a chat as its evidence with no file, command or transcript to read it in.
**－** A reading that is the person's answer is no fault: the estimate line keeps that answer.

## Result

2026-10-31, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
