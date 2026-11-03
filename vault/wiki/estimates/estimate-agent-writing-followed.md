---
type: estimate
kind: QA
status: passed
target: "[[rule-agent-writing]]"
purpose: The agent's text holds to the section How the agent writes of CLAUDE.md, and the person's complaint is the test
method: by hand in a later session — the person's messages of one session read for a complaint about the agent's text, against the section in CLAUDE.md
checked: 2026-09-30
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, render, workflow]
core: true
---

## Criterion

When:
A session starts with `CLAUDE.md` loaded, and the agent writes a text — a reply, a page, a commit message, a document.

Then:
The person raised no complaint in the session that the agent's text broke the section `## How the agent writes` of `CLAUDE.md` — a claim with no real source or wider than the output it rests on, a sales pitch, a long or passive sentence, an answer not given first, a not-done left implied.
**－** A slip in the agent's text that the agent found and corrected itself, with no complaint of the person, is no fault.
**－** When the person says they did not follow and wants it said more simply, by `/wait-what` or in words, that is the normal use of `.claude/skills/wait-what/SKILL.md`, not a fault of this rule.
**－** The code the agent writes is not a text of this rule; `uv run --project .guppi guppi style` judges the code.

## Result

2026-09-30, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
