---
type: decision
case: "60"
status: archived
update: ["[[rule-materialize]]", "[[estimate-materialize-assembles]]", "[[rule-case-protocol]]", case-schema]
origin: raw/2026-09-12/ledger.md#case-60
sprint: migration
created: 2026-09-12
tags: [harness, workflow, ledger, session]
---

## Context

Sub-cases share what their parent states once. `materialize` inherits `context`,
`problem` and `recommend` from the parent Case but not `given`; ten decision groups of
sessions H (52.1–52.4, 53.1–53.4, 55.1, 55.2) carry `incomplete: given`, and their ten
Decision pages have no `## Given` section, though the parent's `given` sits in the Spec.
The Retro of session H named it; the brief carries it as observation (b).

## Problem

The rule says a sub-case has "its own `given`, `when`, `then` and `ratification`", and
practice puts a shared `given` on the parent when it is the same for every child. Either
the rule bends or the Spec does; and the ten pages need their Given either way.

## Given

`guppi/materialize.py` (`assemble`): "a sub-case shares context, problem and recommend
with its parent" — `given` is not in that tuple; `decision_record` marks `incomplete` for
a missing `given` or `when` when a kind other than `defer` is among the lines.
**＋** `rule-materialize` (Leaf, `draft`) says one decision entry per Case with
`case_text`; `estimate-materialize-assembles` (`passed` by the line of 2026-09-11) reads
"marked incomplete for a missing given or when only when a kind other than defer is among
its lines".
**＋** `rule-case-protocol` Render: "A sub-case is `### Case N.M — name` under its parent,
with its own `given`, `when`, `then` and `ratification`; the sections the children share
live on the parent." `case-schema.md` says the same under Splitting.
**＋** No Decision page exists for a parent Case without lines of its own (`decision-case-52`
does not exist); the parent's `given` is only in `raw/<date>/spec.md`.
**＋** The ten pages: `decision-case-52.1` … `52.4` (Spec of 2026-09-10), `53.1` … `53.4`,
`55.1`, `55.2` (Spec of 2026-09-11); each has `## Context`, `## Problem`, `## When`, no
`## Given`.
**＋** The yaml is extended, never rewritten: the ten groups are `applied`; `generate`
skips an existing decision page.
**－** `when` is never inherited: it is the trigger of the sub-case's own criterion.
**－** The Spec of this session puts `given` on every sub-case of 59; nothing there to
inherit.

## When

`guppi materialize` assembles a sub-case's decision entry; the one-off runs once.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-60
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
