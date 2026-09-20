---
type: decision
case: "59.6"
status: current
create: ["[[rule-governed-files-hook]]"]
update: ["[[rule-hook-registry]]", "[[rule-case-protocol]]", "[[rule-prespec]]", "[[estimate-prespec-reconciles]]"]
origin: raw/2026-09-12/ledger.md#case-59.6
sprint: migration
created: 2026-09-12
tags: [hooks, harness, render, session, workflow, ledger]
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

`rule-harness` (MOC, `built`, children `rule-render-harness`, `rule-hook-registry`,
`rule-lint`, `rule-index`) holds the harness tools; `rule-render-harness` (`check`,
`guppi/render.py`) keeps a Rule page and its file one text, and its live criterion says
"no change to `CLAUDE.md`" after a render.
**＋** Sixteen Rule pages carry `governs`: `.claude/skills/hi/SKILL.md` (four pages),
`.claude/agents/librarian-guppi.md` (six), `.claude/agents/ask-guppi.md`,
`.claude/skills/pre-task/SKILL.md`, `.claude/skills/retro/SKILL.md`,
`.claude/skills/handoff/SKILL.md`, `.claude/settings.json` (`rule-hook-registry`),
`CLAUDE.md` (`rule-case-protocol`).
**＋** `rule-hook-registry` (`render`, governs `.claude/settings.json`) lists the hooks:
`PreToolUse` has `ExitPlanMode` → `guppi pretask` and `Skill` → `guppi gate`; a new hook
is an `update` of its Render (case 18.2).
**＋** `guppi/pretask.py` reads the payload with `read_payload` and exits 2 to block;
`tool_input` of `Edit` carries `file_path` and `old_string`, of `Write` `file_path` and
`content` (the Slice 1 probes).
**＋** Case 56 wrote the Retro sentence into `CLAUDE.md` by hand; `render --check` names
the file; `lesson-render-governed-file-updated-as-rule-class-file` records it.
**＋** The slug `rule-governed-files-hook` names no page; `guppi guard` names no command.
**－** A path no Rule page governs is not touched: `vault/`, `guppi/`, `tests/`, the plan
file, `docs/`.
**－** The librarian, `ask-guppi` and any subagent are not gated: they inherit no project
hook, and the librarian's own hook logs only.

## When

The agent calls `Edit`, `Write` or `MultiEdit` on a path some Rule page governs; `/pre-task`
runs; a session starts with `CLAUDE.md`.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-59.6
