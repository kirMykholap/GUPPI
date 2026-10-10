---
type: decision
case: "498.3"
status: archived
update: ["[[estimate-settings]]"]
origin: raw/2026-09-29/0137/ledger.md#case-498.3
sprint: migration
created: 2026-09-29
tags: [harness, render]
---

## Context

Each Estimate page holds one promise, its Criterion. A Criterion should hold only `When:`, the trigger and the input it acts on, and `Then:`, what must hold after. The page carries its promise as a `purpose` field and its way of checking as a `method` field. Twelve older Estimates still have the layout from before this model. They have no `purpose` and no `method` field. They have a `## Context` and a `## Method` section. Most of them also stack one `### case N` block under the Criterion for each Case that changed them. `make lint` counts these twelve as `unmigrated`. Here is where it goes wrong: `estimate-render-harness-reproduces` holds a unit-and-live paragraph and four blocks. One of those blocks, 139.1, is a probe that ran once in session O, to see whether an agent file written mid-session can be called. A new reading cannot tell which lines are the promise and which record an act that happened once.
The person decided in the first round on this item. The twelve go in three Cases by area, all in this session: this Case takes rendering and settings, case 499 takes the end of a session, and case 500 takes the librarian's and the vault's tools. Each page gets one Criterion, and no page is split. The live half of each reading stays. The last Case replaces the Slice note with a note on removing the old-layout checks, so Slice 3g stays open until a later session removes them after lint counts zero (case 202). A Criterion that records a one-time act gets a Criterion of the repeating behaviour (case 485). This group holds five pages: `estimate-render-harness-reproduces`, `estimate-render-sync-reports`, `estimate-settings`, `estimate-default-mode` and `estimate-governed-files-hook-refuses`. None of them has `purpose` or `method`, so each `update` sets both from the page's own Criterion and `## Method`. Setting `method` also drops `## Context` and `## Method` (case 211). Each Criterion is replaced whole and goes back to `pending`, and its reading waits for a later session (case 428.1). Their rules `rule-settings`, `rule-default-mode` and `rule-governed-files-hook` go from `built` to `draft` until the reading. `rule-render-harness` is `draft` already. None of the five lost its Criterion to a tool fault like case 211.3. Their History shows only Criteria that cases 18.1, 36.2, 59.7, 66, 71.1, 85.1, 85.2, 85.4, 88.1, 89.3, 89.4, 91 and 139.1 wrote on purpose, so nothing is restored.
What each new Criterion keeps and drops. The check of the answer notes every old line as not carried, because each new line is a whole statement and not the old wording. The content of the old lines is carried, except for the lines named here. "Unit, against a temp vault" and "Live:" name ways of reading, and they move into `method`. In 498.1, block 139.1 goes out as a one-time probe. Two more lines go out: the `－` line of 88.1 on how to read the clause, and the second half of the `－` line of 85.1, which follows from the first. The unit paragraph, 85.1, 88.1 and 89.4 become one list. The clause of 89.4 that `--sync` exits 0 on a JSON error also goes out of 498.1, because its `when` covers only the plain run and `--check`, and 498.2 promises the exit 0 of the sync on any render error. In 498.3 the line "Its Estimate reads the rendered file" becomes the lines it names. The page fields of `rule-settings` shrink to what the render does with them, and "that order is the order of the keys in the file" is kept. In 498.4, "the page" is named as `rule-default-mode` and its Purpose. In 498.5 the unit paragraph and block 91 join. The live probe on the file of `/hi` moves into `method`.
The check of the answer also notes that the error line of 498.2 shares words with the line of 498.1 on a child without `enforcement: render`. This is expected. 498.1 promises that the plain render exits 1 and writes nothing on that fault. 498.2 promises that the sync at session start swallows any render error with exit 0, because a `SessionStart` hook cannot block. They are two promises, read by two different runs.
The frame. Each kept line was read against `guppi/render.py`, `guppi/guard.py`, `tests/test_render.py`, `tests/test_guard.py`, the `Makefile` and the live `.claude/settings.json`, and none is contradicted. One sentence of the docstring of `guppi/render.py` calls "When Claude Code reads an agent file" "the reading of case 139.1 on `estimate-render-harness-reproduces`". After the recut the page no longer holds that reading, and the next reading overwrites its Result. So 498.1 has one task that writes the finding into the docstring in place of the pointer. That task changes no behaviour and no test. `estimate-render-harness-ticks-the-spec` promises the tick, not the render, and is left alone. `rule-settings` is a MOC, so its `method` names `make test-harness`. The render also fills the language placeholders, but no Estimate of this group promises that, and this Case adds no promise. The History line of 498.6 does not say the Slice note stands, because case 500.6 replaces that note in the same librarian's run. No behaviour changes, so no Render and no hook changes, and no reader keeps an old form. The Case creates no page, so no vault query was run. Not done: cases 499 and 500, the note of Slice 3g, and the removal of the old-layout checks.

## Problem

The five Estimates of rendering and settings still have the layout from before case 193. They have no `purpose` or `method` field, they carry `## Context` and `## Method`, and four of them stack `### case N` blocks, one of them a probe that ran once. Lint counts them as `unmigrated`, and a reading of them cannot tell the promise from the record of past acts.

## Given

`estimate-settings` — the promise, its Criterion replaced whole
**＋** `rule-settings` — the MOC it promises for, the `full` owner of the file
**＋** `rule-default-mode` — its first child
**＋** `rule-permissions` — its second child
**＋** `rule-hook-registry` — its third child
**＋** `.claude/settings.json` — the file rendered
**＋** `vault/raw/<date>/event_log.md` — the day's event log with the `session-start` line
**＋** `Makefile` — the target `test-harness`

## History

- 2026-09-29 created · raw/2026-09-29/0137/ledger.md#case-498.3
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
