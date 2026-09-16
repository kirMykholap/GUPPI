---
type: decision
case: "190.5"
status: current
create: ["[[estimate-spec-capture-offers-the-fork]]"]
update: ["[[rule-spec-capture]]"]
origin: raw/2026-09-16/1034/ledger.md#case-190.5
sprint: migration
created: 2026-09-16
tags: [session, workflow, harness, hooks]
---

## Context

A session closes one way today: `rule-end-of-work`, a MOC over `rule-retro`,
`rule-retro-commit` and `rule-handoff`, promises three steps in order, and `/handoff`
dispatches the librarian straight after the commit. The librarian writes the vault pages
from the Spec. But a Spec can be ready while the work on it is not: this session is one.
`guppi materialize` walks every unit under `raw/` without distinction, so the next
session's librarian will apply the Spec whether the work was done or not. The vault was
asked: no live page covers a close without the librarian, the three slugs are free, and
the word "parked" is already taken twice in this repository.

## Problem

A Spec without its work is more dangerous than no Spec. Applied blind, it makes the vault
claim that `materialize` behaves by the new model while the code is untouched; and
`rule-case-protocol` is a `render` page, so `guppi render` would splice a new Render into
`CLAUDE.md` — the harness would change without the code written for it. Meanwhile there is
nothing to stop before the librarian, and the next session would not learn of the
unfinished work: the brief is written by the librarian, and the `/hi` rule tells the agent
to ignore the decision lines of the tail.

## Given

`guppi spec` writes the Spec into the session folder on `ExitPlanMode`; only after it is
there is anything to carry.
**＋** `guppi materialize` without `--date` walks every unit under `raw/`; no skip exists.
**＋** `rule-raw-archive` already keeps a unit in `raw/` until its yaml is applied, so the
mark is not a second notion of "done".
**＋** `brief.md` is imported into the context of `/hi` by `rule-internal-context`, so the
brief itself carries the news to the next session; neither `guppi tail` nor the Frontier
rule needs to change.
**＋** the brief lives in `wiki/` and cannot mark a unit: `materialize` needs a mark in the
session folder.
**＋** `rule-brief` is a Leaf, `enforcement: render`, `governs:
.claude/agents/librarian-guppi.md`, Estimate `estimate-brief-written`.
**＋** `governs` is one file per rule; not one of the 41 carries a list.
**＋** `rule-end-of-work` is a MOC, Estimate `estimate-end-of-work-order`, promising three
steps in order.
**＋** `rule-spec-capture` is a Leaf, `enforcement: hook`, code `guppi/spec.py` and
`.claude/settings.json`, one Estimate `estimate-spec-capture-appends`.
**＋** a `PostToolUse` hook cannot block — the tool has run; it adds to the context.
**＋** `rule-carry-over`, `estimate-carry-over-writes`,
`estimate-materialize-skips-a-carried-over-unit` and
`estimate-spec-capture-offers-the-fork` are free; the words "carry-over" and
"carried-over" appear nowhere in the vault or the archive.
**－** "parked" is not used: `vault/parked/` and the glossary's "rejected, parked" hold the
word already.

## History

- 2026-09-16 created · raw/2026-09-16/1034/ledger.md#case-190.5
