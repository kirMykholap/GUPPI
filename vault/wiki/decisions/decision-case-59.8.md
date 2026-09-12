---
type: decision
case: "59.8"
status: current
create: [rule-claude-md]
update: [case-schema, glossary]
origin: raw/2026-09-12/ledger.md#case-59.8
sprint: migration
created: 2026-09-12
tags: [harness, render]
---

## Context

Plan Mode leaves four things behind: the Frontier it opened with, the ledger lines the
Stop hook wrote at each ratification, the Spec the human approved, and the Decision pages
the librarian generates from both. In sessions G and H the four drifted: three decision
lines had no item under their Case in the Spec (`lesson-spec-then-items-unchecked-against-
ledger-lines`); the Frontier lived in the agent's memory and a plan was closed on one item
of it (`lesson-plan-mode-exited-per-frontier-item`); a Decision page shows its targets as
two lists aligned by position, unreadable; the items left over at the end of a session are
carried by the brief's counter, not by a decision.

## Problem

Each drift has a mechanical check or a form that removes it, and none is written. The
sub-cases below fix one each; they share this context and are ratified apart. In Work
Mode a fork is not a return to Plan Mode: the subagent stops, the fork is written as a
Case in the short form, shown at Retro, appended to the Spec with a `defer`, and the plan
stays unfinished until the next session (the owner, 2026-09-12; a clause of
`rule-work-mode`, Slice 3b).

## Given

`CLAUDE.md` is hand-written except the Case protocol section, which `rule-case-protocol`
(`partial`, parent `rule-plan-mode`) splices between its markers; `guppi render --check`
names it (the finding of this session).
**＋** `case-schema.md` lists `CLAUDE.md` among the Rule-class files changed by a `file`
item; the glossary row "`CLAUDE.md`, `index.md`" calls it the system prompt; `index.md`
§1's Rule-class table does not list it.
**＋** `guppi/materialize.py` maps the slug `claude-md` to `CLAUDE.md` in `RULE_CLASS`;
`decision-case-56` and `decision-case-52` name `claude-md` in their lists.
**＋** The renderer: a full page's text becomes the whole file; a lone marker line is
replaced by the child's text, markers kept; a partial whose file a full page owns must be
in that page's `children`, else an error (`guppi/render.py`).
**＋** `rule-case-protocol` keeps `parent: rule-plan-mode` and stays in that MOC's
`children`; it is listed in the `children` of `rule-claude-md` too, for the renderer.
Lint does not compare `parent` with `children`.
**＋** The slug `rule-claude-md` names no page.
**－** The text of `CLAUDE.md` is not changed by this Case; the Case moves it. The
"Migration mode" section is carried as it is (the owner, 2026-09-12).
**－** The `@` imports are text to the renderer and to Claude Code alike.

## When

`guppi render` runs; a Case names `CLAUDE.md`.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-59.8
