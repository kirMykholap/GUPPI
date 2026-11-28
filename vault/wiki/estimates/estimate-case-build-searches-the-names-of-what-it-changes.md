---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi, on the note of the hook of rule-case-check that lists the files that name what its Case changes, reads each listed file whose purpose line or path speaks of that change by Read or by a Grep whose path is it, or names it in context, enters each file the change makes false in the Case, and gives each file outside vault/wiki/ that a task changes a task line of its own with its path in the first code span, a line that opens with a command such as a render line kept in its own form
method: "by hand, after the /pre-spec of the session that sets this method: the agent transcript of each case-guppi of that session under ~/.claude/projects/ that got the note of the hook of rule-case-check, for each listed file whose purpose line or path speaks of what its Case changes whether the agent read it by Read or by a Grep whose path is it, or named it in context; and its case file, whether each task line that changes a file outside vault/wiki/ holds its path in its first code span and changes no other such file, a line that opens with a code span holding a command, such as a render line, left out; the count and the transcripts in the estimate line"
checked: 2026-11-25
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [session, workflow, harness, case-build]
core: true
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, gets from the `SubagentStop` hook of `rule-case-check` the note that lists the files that name a page or a file its Case changes, and answers again.

Then:
For each listed file whose purpose line or path speaks of what its Case changes, it reads that file by a `Read` call of it, or by a `Grep` call whose `path` is it, whole or in parts as `rule-case-build` sets for its kind of text, or the `context` of the Case names the file and says why it stands.
**＋** Each file that the change makes false enters the Case, or the `context` of the Case names it and says why it stands.
**＋** In its case file, a file of the repository outside `vault/wiki/` that a task changes has a task line of its own that opens with the path in a code span.
**－** A listed file whose purpose line and path speak of something else needs no read and no line in `context`.
**－** A task line that opens with a code span holding a command, such as `uv run --project .guppi guppi render` with the rendered file in its second span, keeps the form `vault/wiki/case-schema.md` sets for it.

## Result

2026-11-25, passed in the repository of GUPPI.

## History

- 2026-11-28 shipped with GUPPI
