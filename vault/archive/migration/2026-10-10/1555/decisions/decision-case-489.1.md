---
type: decision
case: "489.1"
status: archived
update: ["[[estimate-generate-writes]]"]
origin: raw/2026-09-28/2229/ledger.md#case-489.1
sprint: migration
created: 2026-09-28
tags: [harness, workflow, ledger]
---

## Context

Each Estimate page holds one promise, its Criterion. A Criterion should hold only `When:`, the trigger and the input it acts on, and `Then:`, what must hold after. Older Estimates also open with `Given:`, a set of lines that describe the code and the cases as they stood on the day the promise was written. This group holds the five Estimates of `rule-page-generation` and the two of `rule-materialize` that still have `Given:`. Two of them lost their promise by a fault of the tools. Case 211.1 wrote a new Criterion for `estimate-generate-writes`: the text of case 201.1 plus one line on `set.method`. Case 211.3 then set a `method` field on both `estimate-generate-writes` and `estimate-generate-walks-dates`. The scripts of that day replaced the whole Criterion of each page with the `when` and `then` of 211.3, which was a one-time job on five named pages. So the 211.1 text never stood on the page, and the 201.5 text of `estimate-generate-walks-dates` was lost. No decision chose this. Since case 378.4, an `update` that names only a field leaves the Criterion alone.
The person decided in three rounds. The item goes in seven Cases by area, one group per Case. The pages that record a one-time act get a real promise, and a page with no `purpose` gets one in the same change. This group is the second, after case 488. For the two lost promises the person chose to restore the ratified text, checked against the code of today. The main agent read the text of 211.1 in the archived Spec of session 2238 and the text of 201.5 at the librarian's commit of session 1955. The person also chose to keep `estimate-generate-writes` as one page, although its `Then:` holds 11 `＋` lines, with no split and no backlog item. Each Criterion is replaced whole and goes back to `pending`. Its reading waits for a later session (case 428.1). The note of Slice 3g stays as it is until the last group.
What each new Criterion keeps and drops. The check of the answer notes every old line as not carried, because each new line is a whole statement and not the old wording. On 489.1 and 489.2 it compares with the 211.3 text on the page, which this Case replaces on purpose. The content of the old lines is carried, except for the lines named here. Each `Given:` goes out. A `Given:` line that states behaviour of the step moves into `When:` or `Then:`. 489.1 restores the 211.1 text word for word. It drops only "The Decision page, the failure of an entry and the cascade are three other Estimates", because that is a pointer to other pages. Every other line was read against the docstring and the code of `guppi/generate.py`, and none is contradicted. The drop of `## Context` and `## Method` on `set.method` still runs in `update`. 489.2 restores the 201.5 text word for word. `run` and `generate_date` hold each line. 489.3 moves the `rename` key and the category prefix into `When:` and `Then:`. It drops "`guppi sprint` redraws `sprint.md`", because that is another script, and it drops the collision of a `create`, which 489.1 promises ("any other existing page is a collision"). 489.4 moves the owner and the whole-word boundary into `Then:`. The owner's text now also counts the field `purpose`, as `reword_pairs` compares it. It drops "the Rule-class files", which no longer exist, and the line that a slug goes through `rename`, which is advice and no behaviour of the step. 489.5 keeps its lines and names the `guppi lint` finding in place of "(305.5)". 489.6 turns "as before" into the lift by the `schema.yaml` on disk that the old `Given:` stated. 489.7 keeps its `Then:` word for word and moves the fold of a reading into `When:`.
The check of the answer also notes that a `then` line of 489.4 shares words with 489.3. This is expected. Both steps walk the live pages and replace a whole word outside History and Result. 489.3 moves a page and follows its slug into links and ref fields, and 489.4 replaces a word that is not a slug, and the owner page must carry the new word. They are two promises, each with its own test.
The frame. No behaviour changes, so no code, test, Render or hook changes, and no reader keeps an old form. `rule-page-generation` carries `deferred_by` for case 469. No open Frontier line of this session names it, and this Case changes only its Estimates, so the backlog item stands. The other Estimates of `rule-page-generation` (`-cascades`, `-fails-alone`, `-ticks-the-spec`, `-writes-the-decision-page`, `-writes-the-given`) and of `rule-materialize` are already in the new layout and speak of other steps, so they are not touched. 489.1 names `estimate-generate-fails-alone` as the promise of an entry that fails, and does not change it. The sentence of `rule-estimates-schema` on `Given:` "until the one pass of its migration" stays true. The Case creates no page, so no vault query was run. Not done: the other five groups (24 pages), and the split of `estimate-generate-writes`, which the person declined.

## Problem

The seven Estimates of `generate` and `materialize` still open with `Given:`. Two of them promise a one-time job in place of the promise the person ratified, which the tools overwrote. So their readings check stale text, or nothing that can happen again.

## Given

`estimate-generate-writes` — the promise, its Criterion restored and replaced whole
**＋** `rule-page-generation` — the rule it promises for
**＋** `guppi/generate.py` — `Vault` and its steps per kind of entry
**＋** `vault/wiki/` — the live pages written
**＋** `vault/archive/` — where an entry finds a page not under `vault/wiki/`
**＋** `raw/` — the session folders inside the archive, which the search passes by
**＋** `estimate-generate-fails-alone` — the promise of an entry that fails, named and not changed
**＋** `tests/test_generate.py` — the tests the reading runs

## History

- 2026-09-29 created · raw/2026-09-28/2229/ledger.md#case-489.1
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
