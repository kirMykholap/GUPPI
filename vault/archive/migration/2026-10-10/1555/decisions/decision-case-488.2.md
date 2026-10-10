---
type: decision
case: "488.2"
status: archived
update: ["[[estimate-glossary-checks-the-file]]"]
origin: raw/2026-09-28/2229/ledger.md#case-488.2
sprint: migration
created: 2026-09-28
tags: [harness, workflow, librarian, session]
---

## Context

Each Estimate page holds one promise, its Criterion. A Criterion should hold only `When:`, which is the trigger and the input it acts on, and `Then:`, which is what must hold after. The older Estimates also open with `Given:`, a set of lines that describe the code, the tests or the history as they stood on the day the promise was written. The five Estimates of this group were all written by one parent Case (306), and four of them carry the same `Given:` text, copied from that parent. It speaks of `rule-sprint`, of MOCs and Leaves, and of superseded Cases, and none of it bears on the promise. Two of the five also promise the wrong thing. `estimate-guppi-tests-green` has the `purpose` "make test is green on the branch", but its `Then:` describes the one-time build of `entity-guppi`. `estimate-glossary-terms-defined` describes the one-time build of the glossary table, "a table of 49 rows", and the row splits of that day.
The person decided in one round. Slice 3g's item on the `Given:` pages goes in seven Cases by area, one group per Case, and this session takes one group now. This Case takes the first group, the glossary and `entity-guppi`, with one sub-case per Estimate. A Criterion that records a one-time act gets a new Criterion that states the repeating behaviour its name, its `purpose` and the code give today (case 485). The done-conditions of the sprint are recut like the rest in their own group. `estimate-end-of-work-order` goes to the old-layout item. A page with no `purpose` gets one in the same change. All five pages of this group already have `purpose` and `method`, so no field is set but `status`. Each Criterion is replaced whole and goes back to `pending`. Its reading waits for a later session (case 428.1). The note of Slice 3g stays as it is until the last group (cases 484.7, 485.6).
What each new Criterion keeps and drops. The check of the answer notes every old line as not carried, because each new line is a whole statement and not the old wording. The content of the old lines is carried, except for the lines named here. Each `Given:` goes out whole. The input moves into `When:`. In 488.1 that is the `## Terms` table and step 6 of the librarian's frame. In 488.3 it is the units under `vault/raw/` with a `materialize.yaml`. 488.1 drops "`index.md` is not read", because the file no longer exists. It keeps the refusals of the old text and adds three that `guppi/glossary.py` and `tests/test_glossary.py` already hold: a `where` that is no `[[slug]]`, no `## Terms` section, and no single live `entity-glossary`. 488.2 drops "after `sprint --check`". The `Makefile` runs `backlog --check` between the two now, and the order is not the promise. It adds that a missing file differs, because `run` compares it as `None`. The finding line of 488.2 names the file outside its code span, because a span with a `/` reads as a path that `given` must name. 488.3 keeps the form of the line in `vault/wiki/case-schema.md` ("a glossary line `- [ ] `uv run guppi glossary``") and the two `－` lines of the old text, and it names the unit that is not applied whole, as `tick_command_lines` of `guppi/render.py` reads it. 488.4 drops the build of the table, its 49 rows and the two rows that split. It also drops the line on how a term enters or leaves, which the Purpose of `entity-glossary` keeps. It keeps the purpose, a live page in each `where` that defines its term and no term twice, and the terms the Purpose names as not rows. 488.5 drops the whole build of `entity-guppi`: its kind, its `children`, `code_ref`, the `parent` of `entity-sprint`, the `applies_to` of `rule-harness`, and the phase MOCs without `applies_to`. The line that the cascade writes `rules` is promised by `estimate-generate-writes-rules-from-applies-to`. 488.5 keeps the one line of its purpose, `make test` with no failed test.
The check of the answer also notes that the `then` lines of 488.4 share words with 488.1. This is expected. 488.1 promises that the script refuses a table with a dead `where` or a term twice and writes nothing. 488.4 promises the state of the table itself, read at each librarian's run, including the judgment by hand that the page defines the term. No script makes that judgment.
The frame. No behaviour changes, so no code, test, Render or hook changes, and no reader keeps an old form. Each kept line was read against `guppi/glossary.py`, `tick_command_lines` and `applied_whole` of `guppi/render.py`, the `Makefile`, step 6 of `.claude/agents/librarian-guppi.md` and the table of `entity-glossary`. None of them is contradicted. The sentence of `rule-estimates-schema` that an older page carries its `Given:` "until the one pass of its migration" stays true while other groups remain. The Purpose of `rule-glossary` says `make lint` runs the check "after `sprint --check`". That is still true, since it runs later in the same target. `rule-glossary`, `entity-glossary` and `entity-guppi` have no other Estimates, so none is left alone. `estimate-sprint-ticks-the-spec` and `estimate-render-harness-ticks-the-spec` use the same tick helper and belong to the group of the tickers. 488.6 gives `entity-sprint-migration` an `update` with only `change`, because pre-spec asks for one under a Case that closes a `sprint` line. The Case creates no page, so no vault query was run. Not done: the other six groups (31 pages), and `estimate-end-of-work-order` with the old-layout item C2.

## Problem

The five Estimates of the glossary and `entity-guppi` still open with a `Given:` copied from another Case. Two of them promise a build that happened once and not the behaviour their name and `purpose` state. So a reading of them checks a state of the code that goes stale, or checks nothing that can happen again.

## Given

`estimate-glossary-checks-the-file` — the promise, its Criterion replaced whole
**＋** `rule-glossary` — the rule it promises for
**＋** `entity-glossary` — the page the file is rendered from
**＋** `guppi/glossary.py` — `run` with `--check`, which renders in memory and compares
**＋** `vault/wiki/glossary.md` — the file compared
**＋** `Makefile` — the target `lint`, which runs the check
**＋** `tests/test_glossary.py` — the tests the reading runs

## History

- 2026-09-29 created · raw/2026-09-28/2229/ledger.md#case-488.2
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
