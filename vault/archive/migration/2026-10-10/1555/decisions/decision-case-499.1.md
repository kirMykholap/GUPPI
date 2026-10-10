---
type: decision
case: "499.1"
status: archived
update: ["[[estimate-end-of-work-order]]"]
origin: raw/2026-09-29/0137/ledger.md#case-499.1
sprint: migration
created: 2026-09-29
tags: [session, workflow]
---

## Context

Each Estimate page holds one promise, its Criterion. A Criterion should hold only `When:`, the trigger and the input it acts on, and `Then:`, what must hold after. The page carries its promise as a `purpose` field and its way of checking as a `method` field. The older Estimates lack both fields. They carry `## Context` and `## Method`, and stack `Given:` or `### case N` blocks, and `make lint` counts them as `unmigrated`. This group holds the two Estimates of the end of a session: `estimate-end-of-work-order`, which still opens with a `Given:` about the Spec hook, the cascade and the methods of other Estimates, and `estimate-handoff-dispatches`, which has a head paragraph and block 73.7. The two parts of the second page disagree. The head says the librarian is dispatched "with the date". Block 73.7 says it is dispatched with the path of `handoff.md`. The skill `/handoff` sends only `Materialize <date>.`, but the librarian's frame takes as its first input "the `handoff.md` your dispatch names". The History of `rule-handoff` records that case 73.7 meant the path, "the librarian is dispatched with its path". The Render never got the path, so the librarian has had to find the file on its own.
The person decided in the first round on this item. The twelve old pages go in three Cases by area: case 498 took rendering and settings, this Case takes the end of a session, and case 500 takes the librarian's and the vault's tools and replaces the Slice note. Each page gets one Criterion, no page is split, and each live half of a reading stays. In the second round the person chose to keep the path in the promise and to change the skill to match. So 499.2 changes the Render of `rule-handoff` to send `Materialize <date> from <path of handoff.md>.` and recuts `estimate-handoff-dispatches` to that behaviour. Neither page has `purpose` or `method`, so each `update` sets both, and setting `method` drops `## Context` and `## Method` (case 211). Each Criterion is replaced whole and goes back to `pending`, and its reading waits for a later session (case 428.1). `rule-end-of-work` goes from `built` to `draft` until the reading. `rule-handoff` is `draft` already. Neither page lost its Criterion to a tool fault like case 211.3. Their History shows only Criteria that cases 38, 38.3, 73.7, 190.2 and 196.2 wrote on purpose, so nothing is restored.
What each new Criterion keeps and drops. The check of the answer notes every old line as not carried, because each new line is a whole statement and not the old wording. The content of the old lines is carried, except for the lines named here. In 499.1 the `Given:` goes out whole. Its lines describe the Spec hook, the cascade of case 190.2, the methods of three Estimates and the order of the entries of 190.x, and all of these are history. The line on `rule-carry-over` as a child is already in `Then:`. "`make test-end-of-work` is green" moves into `method`. The `－` line "The order of the three steps of the ordinary way does not change" goes out as a bound of an edit, because the order itself stands in the line before it. In 499.2 "with the date" gives way to the path the person chose. "The first turn's context holds git status --porcelain" is kept as the skill's own check.
The check also notes that 499.2 shares words with 499.1 on `/handoff` on a dirty tree and on the commit after the handoff. This is expected. 499.1 promises the order of the ordinary end of a session, read across its folder, the event log and `git log`: the gate of `guppi/gate.py` refuses a dirty tree, and no other commit stands between the handoff and the librarian's. 499.2 promises what the skill does when it is called: it stops on a dirty tree, writes the note, dispatches with the path, and commits nothing itself. Both old pages held these lines, as cases 38 and 38.3 signed them. `estimate-session-phases-in-order` (case 493.4) promises that the marks of all five phases rise in time, a reading across the whole session. 499.1 promises the gate and the two ends inside End of Work, so it is not touched.
The frame. The kept lines were read against the Render of `rule-handoff`, the Purpose and `children` of `rule-end-of-work`, `guppi/gate.py`, the `Makefile` and the frame of the librarian, `.claude/agents/librarian-guppi.md`. With the new Render, the librarian's "the `handoff.md` your dispatch names" becomes true. No test and no script reads the dispatch line. The new skill text lands at the render of the librarian's run. So the `/handoff` of this session still sends the date alone, and its librarian finds the folder as it has so far. Nothing refuses in between and nothing is lost, so no old form is kept. `estimate-handoff-holds-each-fact-once` promises the content of the three sections, not the dispatch, and is left alone. The pair of 499.2 hits the one sentence of the Render that names the dispatch. The History line of 499.3 does not say the Slice note stands, because case 500.6 replaces that note in the same librarian's run. The Case creates no page, so no vault query was run. Not done: case 500 and the note of Slice 3g, and the removal of the old-layout checks.

## Problem

The two Estimates of the end of a session still have the layout from before case 193, and lint counts them as `unmigrated`. One of them promises two different dispatch texts, and the skill it reads sends neither the path it promised nor the file the librarian expects.

## Given

`estimate-end-of-work-order` — the promise, its Criterion replaced whole
**＋** `rule-end-of-work` — the MOC it promises for, its `children` and the two ends in its Purpose
**＋** `rule-carry-over` — the second end, `/carry` straight after Plan Mode
**＋** `rule-handoff` — the child that `rule-carry-over` follows
**＋** `guppi/gate.py` — the gate that refuses `/handoff` on a dirty tree
**＋** `vault/raw/<date>/<hi HHMM>/` — the session's folder, with `handoff.md`
**＋** `vault/raw/<date>/event_log.md` — the day's event log
**＋** `Makefile` — the target `test-end-of-work`

## History

- 2026-09-29 created · raw/2026-09-29/0137/ledger.md#case-499.1
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
