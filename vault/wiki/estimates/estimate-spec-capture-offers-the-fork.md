---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-capture]]"
origin: raw/2026-09-16/1034/ledger.md#case-190.5
sprint: migration
created: 2026-09-16
tags: [session, workflow, harness]
purpose: The hook prints the fork between Work Mode and /carry after the Spec is written
method: pytest in the tests of guppi/spec.py, the tests of the printed fork
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
`guppi spec` has run on `PostToolUse` of `ExitPlanMode` and written the Spec.

Then:
It prints the fork into the context: Work Mode — or `/carry`.
**＋** the line names the session folder and the Spec file.
**－** it blocks nothing: the agent asks, the person chooses.
**－** the writing of the Spec does not change: that is the promise of
`estimate-spec-capture-appends`, and it stands as it is.

## Result

2026-09-16, `pytest tests/test_spec.py`: 14 green, three of the fork — after the Spec is written the hook prints one line naming vault/raw/<date>/<HHMM>/spec.md and <folder>/carry.md, Work Mode and /carry, and that nothing starts until the person answers; the line is printed again when the plan was already there, and never without a Spec; the live print in the client is read at the next ExitPlanMode, this session's ran the old code

## History

- 2026-09-16 created · [[decision-case-190.5]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1651/ledger.md#L36
- 2026-09-17 ref removed · one-off migration · raw/2026-09-16/2238/spec.md#case-210
