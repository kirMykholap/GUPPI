---
type: decision
case: "492.4"
status: current
update: ["[[entity-sprint-migration]]"]
origin: raw/2026-09-28/2229/ledger.md#case-492.4
sprint: migration
created: 2026-09-28
tags: [sprint, workflow]
---

## Context

Each Estimate page holds one promise, its Criterion. A Criterion should hold only `When:`, the trigger and the input it acts on, and `Then:`, what must hold after. Older Estimates also open with `Given:`, a set of lines that describe the code and the cases as they stood on the day the promise was written. This group holds three such pages. Each promises a text that the agent reads when it acts: `CLAUDE.md` from `rule-claude-md`, the atomicity rule in `vault/wiki/case-schema.md`, and the one-judgment rule inside `CLAUDE.md`. Their `Given:` repeats how a Render is written and how the hook refuses a hand edit, and it also keeps history. For example, `estimate-claude-md-rendered` still lists each item of the old "Migration mode" section and the Rule it became, and `estimate-one-judgment-one-implementation-followed` names the three functions that case 351 lifted into one module.
The person decided in the first round on this item. The item goes in seven Cases by area, one group per Case. History and the lines on the bounds of an edit leave the Criterion. A lost ratified text is restored, and a page with no `purpose` gets one. This group is the fifth, after cases 488 to 491. None of these pages lost its Criterion to a tool fault like case 211.3. Their History shows only Criteria that cases 73.10, 88.2, 272.1, 273.3, 288.3, 317, 360 and 374 changed on purpose, so nothing is restored and no commit needs to be read. All three pages already have `purpose` and `method`, so no field is set but `status`. Each Criterion is replaced whole and goes back to `pending`. Its reading waits for a later session (case 428.1). The note of Slice 3g stays as it is until the last group.
What each new Criterion keeps and drops. The check of the answer notes every old line as not carried, because each new line is a whole statement and not the old wording. The content of the old lines is carried, except for the lines named here. Each `Given:` goes out. A `Given:` line that states lasting behaviour moves into `When:` or `Then:`: where a `partial` Render lands, that the governed-files hook refuses a hand edit, and that every session and subagent loads `CLAUDE.md`. In 492.2 the list of the "Migration mode" items and the Rules they became goes out as history, and so does the line that the glossary and the schema arrive with `/hi`, which `estimate-internal-context-loaded` promises. The first `then` line of 492.2 quotes the paragraph of `CLAUDE.md` in plain quotation marks, in place of the old summary in code spans. The quote keeps every word of the paragraph but drops the code spans around the vault folder, the glossary path and the skill that opens a session. A span with a `/` reads as a path that `given` must name, and the paragraph is text of the file, not a frame of the Case. So the check notes that line as not carried, while its content is the same. In 492.3 the functions that case 351 lifted go out as history. In 492.1 the `Given:` line on the refusal of `pre-spec` described the form before case 472.3, "two Estimate items and no written `sections: Criterion`". The `－` line keeps only that the refusal stays with `rule-prespec`, as the Purpose of `rule-atomicity` says today, so the stale form is not signed again.
The check also notes that 492.1, 492.2 and 492.3 share a line on `render --check` and the governed-files hook. This is expected. Each promise guards a rendered text by the same two means, but each names its own file or its own markers, and a drift in one fails one reading alone.
The frame. Each kept line was read against `CLAUDE.md`, the Render of `rule-claude-md` and its `children`, the Render of `rule-atomicity` and its marker line in `rule-case-protocol` (a MOC with the one child `rule-atomicity`), and the Render of `rule-one-judgment-one-implementation`. None is contradicted. The Render of `rule-atomicity` has since gained a last sentence on two behaviours and two angles. The new Criterion names the parts it named before and does not sign that sentence. The file equals the Render in any case, and `render --check` holds the rest. No behaviour changes, so no code, test, Render or hook changes, and no reader keeps an old form. `rule-claude-md`, `rule-atomicity` and `rule-one-judgment-one-implementation` have no other Estimates. The Case creates no page, so no vault query was run. Not done: the other two groups (10 pages).

## Problem

The three Estimates of the text every context loads still open with a `Given:` that repeats the render and keeps history, and one of them states an old form of the refusal of `pre-spec`. So their promises carry lines that go stale beside the text they guard.

## Given

`entity-sprint-migration` — the sprint page; its Slice 3g holds the note on every other Estimate
**＋** `vault/wiki/sprint.md` — the render of the sprint page
**＋** `/hi` — builds the Frontier from `vault/wiki/sprint.md`
**＋** `rule-claude-md` — a rule whose Estimate this Case recuts
**＋** `rule-atomicity` — a rule whose Estimate this Case recuts
**＋** `rule-one-judgment-one-implementation` — a rule whose Estimate this Case recuts

## History

- 2026-09-29 created · raw/2026-09-28/2229/ledger.md#case-492.4
