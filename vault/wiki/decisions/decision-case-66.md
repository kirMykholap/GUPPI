---
type: decision
case: "66"
status: current
update: ["[[rule-case-protocol]]", "[[rule-plan-mode]]", "[[rule-prespec-hook]]", index, "[[rule-harness]]", "[[estimate-retro-loads]]", "[[estimate-spec-capture-appends]]", "[[estimate-render-harness-reproduces]]"]
origin: raw/2026-09-12/ledger.md#case-66
sprint: migration
created: 2026-09-12
tags: [session, workflow, ledger, hooks, harness, render]
---

## Context

`/pre-task` sent the list of this Plan Mode's decisions to `ask-guppi` once. It returned
findings against `rules/schema.md`, `estimates/schema.md`, `index.md` §10 and the
criteria of five Estimates that quote wording the Cases change (the lesson
`lesson-estimates-criterion-stale-after-contract-change` names the pattern). Each is
settled here, as case 57 did, by a line under this Case; the `then` blocks of the Cases
concerned were corrected in place where no new line was needed.

## Problem

Six findings hold: (1) 59.8 lists `rule-case-protocol` in two MOCs' `children` while
`parent` is one slug; (2) 59.8 gave the MOC another page's Estimates, and an Estimate has
one `target`; (3) 59.7 set `enforcement: hook` on a `check` rule that `make lint` and
`estimate-harness-pipeline` rest on; (4) 59.1 set `implementation_ref` on a `render`
rule, which the schema forbids; (5) `index.md` §10 still says "not the code" against
case 58; (6) `rule-harness` says its four children run together in `make lint` and 59.6,
59.8 add two that do not; and the criteria of `estimate-retro-loads`,
`estimate-spec-capture-appends` (`## Retro`) and `estimate-render-harness-reproduces`
("no change to `CLAUDE.md`") quote wording 59.5 and 59.8 change. Four findings do not
hold: `rule-prespec-hook` gates on the `pretask` line and the check is content, not a
duplicate; `estimate-brief-written`'s clause on `sprint.md` binds the librarian, and 59.5
has the agent edit it in Work Mode; 59.3 and 62 replace different sentences of the Render;
the Render of `rule-claude-md` carries the whole present text of `CLAUDE.md` in its block.

## Given

`rules/schema.md`: `parent` is one slug; `implementation_ref` and `## Implementation` for
`hook` and `check` only; a MOC's `estimates` are cross-cutting. `estimates/schema.md`:
one `target`.
**＋** `rule-plan-mode` `children: [rule-case-protocol, rule-ask, rule-prespec-hook,
rule-prespec, rule-spec-capture]`; `rule-case-protocol` `parent: rule-plan-mode`.
**＋** `rule-prespec-hook` (`hook`, `guppi/pretask.py`, `.claude/settings.json`) gates
`ExitPlanMode` on the `pretask` line.
**＋** `rule-harness` Purpose: "Four rules belong to no phase of the session: the renderer,
the hook registry, lint and the indexes. They run together in `make lint`…";
`estimate-harness-pipeline` reads `make lint`'s three commands in order — unchanged.
**＋** `index.md` §10: "Not `ledger.md`, not `spec.md`, not `plan.md`, not
`wiki/decisions/`, not the archive, not the code".
**＋** `estimate-retro-loads` (pending): "a short defer with its Case under ## Retro in
spec.md"; `estimate-spec-capture-appends` (pending): "A `## Retro` section appended by
the agent stays intact"; `estimate-render-harness-reproduces` (passed): "no change to
`CLAUDE.md`".

## When

The librarian generates the pages of this session; the next session renders and reads.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-66
