---
type: estimate
kind: QA
status: passed
target: "[[rule-retro]]"
purpose: Whether Retro and the handoff leave out the sub-cases of a Case that a supersedes tag names
method: "by hand at a /retro whose session ledger holds a {supersedes:case N} on a Case N whose sub-cases have decision lines: the debt Retro sorts and the Cases that handoff.md lists"
checked: 2026-10-05
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
The skill of `rule-retro` sorts the boxes of a session whose ledger holds a decision line carrying `{supersedes:case N}`, Case N having sub-cases with decision lines, and the skill of `rule-handoff` then writes `handoff.md`.

Then:
Retro counts no line of Case N or of any of its sub-cases as debt.
**＋** The `## What actually got done` section of `handoff.md` lists neither Case N nor any of its sub-cases among the Cases ratified.
**－** A tag that names Case N.M leaves out N.M and its own sub-cases only; the parent and its other sub-cases are counted.

## Result

2026-10-05, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
