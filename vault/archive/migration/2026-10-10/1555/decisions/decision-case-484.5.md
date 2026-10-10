---
type: decision
case: "484.5"
status: archived
update: ["[[estimate-prespec-catches-bare-wikilinks]]"]
origin: raw/2026-09-28/2000/ledger.md#case-484.5
sprint: migration
created: 2026-09-28
tags: [session, workflow, harness, tests]
---

## Context

Each Estimate page holds one promise of a rule, its Criterion. Since case 378.2 a Criterion has only `When:`, the trigger and the input it acts on, and `Then:`, what must hold after. The frame of a Case stays in the Case and on its Decision page. Older Estimates still open with `Given:`: lines that describe the code, the tests or the history as they stood when the promise was written. Those lines go stale when the code moves on. For example, `estimate-prespec-simulates-the-pairs` says in `Given:` that pre-spec "has no check of an anchor at all", and that check is now the promise itself. Some of these pages also have `－` lines on what one edit left alone, such as "Nothing else in pre-spec changes". Those lines state no behaviour. A search on 2026-09-28 found `Given:` in the Criterion of 43 Estimate pages, spread over about 25 target rules.
The person decided in one round. This Case takes one group, the six Estimates of `rule-prespec` that hold `Given:`, with one sub-case for each Estimate (case 395, and the eleven of case 396 onward). The one note of Slice 3g stays as it is until the last group. Each Criterion is replaced whole and goes back to `pending`. Its reading is a pytest run and waits for a later session (case 428.1). A `－` line on the bounds of an edit goes out with its group, and a `－` line that states real behaviour of the check stays. No lint count of the `Given:` pages is added.
What each new Criterion keeps and drops. The check of the answer noted each old line that the new Criterion does not carry word for word. The `Then:` lines are now carried word for word, except for the changes below, each made on purpose.
The `Given:` lines go out: the state of the code ("has no check of an anchor at all", "`check_form` already reads"), what `materialize` and `generate` do, the cases each check stands on, the lines on `tests/test_prespec.py` (the file is in `given` and in `method`), "the conditions of the parent", and the line that `rule-prespec` renders the skill.
The exit code of the command ("exit 1 on any") goes out of 484.1 and 484.5. `estimate-prespec-checks-the-plan` promises it for every finding ("Each finding is one line on stdout; exit 1 on any finding, 0 on none"), so a second copy would sign one promise twice.
A `Given:` line that states behaviour of this check moves into `Then:`. These are the form the tickers match (484.1), and the rule that a `create` reads `enforcement` from the item and an `update` from the page (484.4). `enforcement_of` in `guppi/prespec.py` reads no `render_mode`, so that word goes out.
The input moves into `When:`: the `tasks` block (484.1), the record lines of the window and a line with `{supersedes:case N}` (484.2), the items of the `then` blocks (484.3, 484.4), and the pairs and the live pages (484.6). The `When:` of 484.5 is kept word for word.
Two finding texts are split. The old ones hold a code span with a `/`: the markers `<!-- /slug -->` in 484.4, and "a tests/ file" in 484.3. `frame_name` of `guppi/prespec.py` reads any span with a `/` as a path that `given` must name. So the new lines name the markers, and the list of method forms, outside the span of the finding. The finding line of 484.1 splits the same way: the old text nests code spans inside one another, and each span now stands alone.
These `－` lines go out as bounds of an edit: "Nothing else in pre-spec changes" (on two pages), "`lint` does not change" and "The behaviour of lint does not change". The line in `estimate-prespec-catches-a-superseded-case` on a Frontier line closed by a superseded Case, "a finding as today", also goes out. That behaviour is promised by `estimate-prespec-checks-the-frontier`: "A line closed `case N` is a finding when the plan has no heading of Case N".
The frame. Each `then` line rests on `guppi/prespec.py`, and was read against it:
- 484.1: the finding text and `OFF_FORM_LINE` in `check_tasks`.
- 484.2: `check_lines`, which matches the plan heading by the exact Case id, so a superseded sub-case is found by its own heading alone.
- 484.3: `check_form`, `NO_FORM`, and `names_a_form` imported from `guppi/lint.py`.
- 484.4: `check_markers`, which matches the markers of the item's own slug, and `enforcement_of`, which reads `enforcement` from the item on a `create` and from the page on an `update`.
- 484.5: `check_bare_links` and `plan_prose`.
- 484.6: `check_pairs`.
- One exception: the form the tickers match in 484.1 rests on `vault/wiki/case-schema.md`, "the command in the first code span is what the ticker matches (case 235)".
The Render of `rule-prespec` describes each of these findings in its own words, not in the text of the finding line. It does not say that the markers are those of the item's own slug, or where `enforcement` is read from; those stand in the code only. No behaviour changes, so no code, test, Render or hook changes, and no reader keeps an old form. The sentence of `rule-estimates-schema` "a page written before carries its `Given:` until the one pass of its migration" stays true while other groups remain. The other Estimates of `rule-prespec` speak of other findings and are not touched. `estimate-prespec-hook-gates` targets `rule-prespec-hook` and belongs to another group. Pre-spec asks for an `update` of the sprint page under a Case that closes a `sprint` line, so 484.7 gives `entity-sprint-migration` an `update` with only `change`, and its note stands. The Case creates no page, so no vault query was run. Not done: the other 37 pages with `Given:`, the bounds lines on pages outside this group, and the pages with `### case N` blocks (the sibling item C2).

## Problem

The Criteria of six Estimates of `rule-prespec` still open with `Given:`, and some carry `－` lines on the bounds of an old edit. So their promises describe a state of the code that goes stale, and they do not read as the trigger and the result alone.

## Given

`estimate-prespec-catches-bare-wikilinks` — the promise, its Criterion replaced whole
**＋** `rule-prespec` — the rule it promises for; its Render describes the finding
**＋** `.claude/skills/pre-spec/SKILL.md` — the skill `/pre-spec`, rendered from `rule-prespec`, which runs the check
**＋** `guppi/prespec.py` — `check_bare_links` and `plan_prose`, which judge the links
**＋** `vault/wiki/` — the live pages, the archived pages and the hub files a link may name
**＋** `tests/test_prespec.py` — the tests the reading runs

## History

- 2026-09-28 created · raw/2026-09-28/2000/ledger.md#case-484.5
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
