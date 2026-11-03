---
type: estimate
kind: QA
status: passed
target: "[[rule-internal-context]]"
purpose: The text of sprint.md, backlog.md, brief.md, orchestration.md, where-to-stop.md, ratification.md and glossary.md is present in the first turn's context after /hi, without a read call, and case-schema.md is not
method: by hand, the text of .claude/skills/hi/SKILL.md as rendered, or, at the Retro of the session that changes it, the new Render of rule-internal-context in the Spec, read against the Criterion, recorded in the estimate line
checked: 2026-10-06
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, harness]
core: true
---

## Criterion

When:
The person invokes `/hi`, with `.claude/skills/hi/SKILL.md` rendered from `rule-internal-context`.

Then:
The text of `vault/wiki/sprint.md`, `vault/wiki/backlog.md`, `vault/wiki/brief.md`, `vault/wiki/orchestration.md`, `vault/wiki/where-to-stop.md`, `vault/wiki/ratification.md` and `vault/wiki/glossary.md` is in the context of the first turn, in that order, without a read call.
**＋** `vault/wiki/case-schema.md` is not in it.
**＋** The glossary and the backlog reach a session through this block alone. After a compaction, the paths of these files are in the list of `guppi recall`.
**－** A subagent, such as `librarian-guppi`, `ask-guppi` or one of Work Mode, carries none of these texts. Its prompt names what it needs.

## Result

2026-10-06, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
