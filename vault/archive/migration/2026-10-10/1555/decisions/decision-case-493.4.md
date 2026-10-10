---
type: decision
case: "493.4"
status: archived
update: ["[[estimate-session-phases-in-order]]"]
origin: raw/2026-09-28/2229/ledger.md#case-493.4
sprint: migration
created: 2026-09-28
tags: [session, workflow]
---

## Context

Each Estimate page holds one promise, its Criterion. A Criterion should hold only `When:`, the trigger and the input it acts on, and `Then:`, what must hold after. Older Estimates also open with `Given:`, a set of lines that describe the code and the cases as they stood on the day the promise was written. This group holds the Estimates of the hooks and gates of a session: the recall after a compaction, the two checkpoints of Plan Mode, the gate of `/retro` and `/handoff`, the order of the five phases, and the hook that holds Plan Mode open until `/pre-spec` has run. The group has five pages and not six, because the first round left `estimate-end-of-work-order` to the old-layout item C2. Their `Given:` holds facts from the Claude Code docs, a lesson, the case numbers of old fixes, and one line on the bounds of an edit: "The `--check` pass of `rule-prespec` does not change here". Three of the pages have no `purpose`.
The person decided in the first round on this item. The item goes in seven Cases by area, one group per Case. History and the lines on the bounds of an edit leave the Criterion. A lost ratified text is restored, and a page with no `purpose` gets one in the same change. This group is the sixth, after cases 488 to 492. None of these pages lost its Criterion to a tool fault like case 211.3. Their History shows only Criteria that cases 40, 136.2, 169.1, 180, 213.2, 261, 265.2, 265.3, 287 and 316 wrote on purpose, so nothing is restored and no commit needs to be read. `estimate-plan-mode-verified`, `estimate-retro-commit-gates` and `estimate-prespec-hook-gates` get a `purpose` from their own Criterion. Each Criterion is replaced whole and goes back to `pending`. Its reading waits for a later session (case 428.1). The note of Slice 3g stays as it is until the last group.
What each new Criterion keeps and drops. The check of the answer notes every old line as not carried, because each new line is a whole statement and not the old wording. The content of the old lines is carried, except for the lines named here. Each `Given:` goes out, and a `Given:` line that states lasting behaviour moves into `When:` or `Then:`. In 493.1 the facts of the Claude Code docs, the lesson that a `SessionStart` hook cannot block and the example "the glossary by C4.1" go out as history. The line on the 10,000 characters stays: no code caps the output, but a reading can check it. In 493.2 the line on the children of `rule-plan-mode` goes out, and the vault query before a `create` without a `ref` moves into `When:`. "The plan is still written" now names the hook of `rule-spec-capture`, the writer of `spec.md` at approval. In 493.3 the line "live, the first `/handoff` from Retro on a dirty tree is refused and passes after the commit" is a way of reading, and the `method` already names the live reading. "`guppi event prompt` does not change and does not fail" goes out as a bound of an edit. The old line "without `hi` — nothing to check, exit 0" is a line the code does not honour: `guppi/gate.py` checks the tree of a `/handoff` with or without a `hi`. It is dropped, and the true part stays, that without a `hi` the checks of `/retro` do not run. The check of the Spec against the ledger still names `/retro` only, as before. The code runs it on all three commands, and this Case does not widen the promise. In 493.4 the line that a Rule MOC promises its order goes out, because that is the schema's rule and not this promise. In 493.5 the `－` line on the `--check` pass goes out as a bound of an edit, and "as before" becomes a plain statement.
Each kept line was read against `guppi/recall.py`, `guppi/gate.py`, the hook part of `guppi/prespec.py` and the `children` of `rule-session`, and none is contradicted. Some finding lines and headers hold a `/` inside a path. They stand in plain quotation marks, as the old text had them, or name the folder in words, because a code span with a `/` reads as a path that `given` must name. No behaviour changes, so no code, test, Render or hook changes, and no reader keeps an old form. `estimate-plan-mode-names-its-estimates` and the other Estimates of these rules speak of other steps and are not touched. The Case creates no page, so no vault query was run. Not done: the last group, the five done-conditions of the sprint, and `estimate-end-of-work-order` with item C2.

## Problem

The five Estimates of the session hooks and gates still open with a `Given:` of docs, lessons and old case numbers. Three of them have no `purpose`, and one line promises a pass on a `/handoff` without a `hi` that the gate does not give. So their readings check a frame that goes stale, and one line is false.

## Given

`estimate-session-phases-in-order` — the promise, its Criterion replaced whole
**＋** `rule-session` — the MOC it promises for, its children in order
**＋** `vault/raw/<date>/event_log.md` — the day's event log with the `hi` line
**＋** `vault/raw/<date>/<hi HHMM>/` — the session's folder: `frontier.md`, `spec.md`, `handoff.md` or `carry.md`
**＋** `/carry` — the skill that conserves a session after Plan Mode

## History

- 2026-09-29 created · raw/2026-09-28/2229/ledger.md#case-493.4
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
