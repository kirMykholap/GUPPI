---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
origin: raw/2026-09-16/1034/ledger.md#case-190.3
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger]
ref: rule-materialize
purpose: A unit holding carry.md is skipped, with one line on stdout
method: pytest in tests/test_materialize.py, the tests of the skip
---

## Criterion

Given:
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

When:
`guppi materialize` reaches a unit whose folder holds `carry.md`.

Then:
The unit is skipped and one line naming it is printed on stdout; no yaml is written or
extended for it.
**－** the unit is marked neither applied nor failed: `rule-raw-archive` decides that as
before.

## Result

2026-09-16, `pytest tests/test_materialize.py`: 51 green, four tests of the skip — a unit whose folder holds carry.md is passed by with one line on stdout naming it, its yaml neither written nor extended, a foreign supersedes not written into it, the content of the mark not read, --show passes it by too, and a unit without the mark is read as before

## History

- 2026-09-16 created · [[decision-case-190.3]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1651/ledger.md#L34
