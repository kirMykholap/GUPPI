---
type: decision
case: "490.1"
status: current
update: ["[[estimate-page-schemas-one-file-per-rule]]"]
origin: raw/2026-09-28/2229/ledger.md#case-490.1
sprint: migration
created: 2026-09-28
tags: [harness, render, schema]
---

## Context

Each Estimate page holds one promise, its Criterion. A Criterion should hold only `When:`, the trigger and the input it acts on, and `Then:`, what must hold after. Older Estimates also open with `Given:`, a set of lines that describe the code and the cases as they stood on the day the promise was written. This group holds seven such pages: the Estimate of `rule-page-schemas`, the five Estimates of the category schemas under it (rules, entities, estimates, decisions, lessons), and the Estimate of `rule-vault-layout`. The five category pages share one `Given:`, which describes how `render` writes a file, the hook on a hand edit, and the keys lint reads. Each of them also keeps two lines from the day in September when the old `schema.md` files became `schema.yaml` files. One says the prose of "the former `schema.md`" stands in the file "verbatim". The other says `schema.md` "does not exist".
The person decided in the first round on this item. The item goes in seven Cases by area, one group per Case. A one-time act leaves the Criterion and the lasting behaviour stays. A lost ratified text is restored, and a page with no `purpose` gets one. This group is the third, after cases 488 and 489. None of these pages lost its Criterion to a tool fault like case 211.3. Their History shows only Cases that changed the text on purpose (350, 358, 362.1, 372), so nothing is restored and no commit needs to be read. All seven pages already have `purpose` and `method`, so no field is set but `status`. Each Criterion is replaced whole and goes back to `pending`. Its reading waits for a later session (case 428.1). The note of Slice 3g stays as it is until the last group.
What each new Criterion keeps and drops. The check of the answer notes every old line as not carried, because each new line is a whole statement and not the old wording. The content of the old lines is carried, except for the lines named here. Each `Given:` goes out. The line on the keys lint reads names `properties.single`, and none of the five category schemas of this group carries that key. That line promises behaviour of `guppi/lint.py`, which belongs to the Estimates of `rule-lint`. From the prose line of each category page, "the former `schema.md`" and "verbatim" go out, because they tell where the text came from. The paragraphs the `description` holds stay, and so does the rule that `fields` and `sections` describe each name of the lists, which lint checks as the class `schema-description`. The Decision schema keeps its line on the History of a Decision (case 358), since the file still says so. The line "`schema.md` does not exist" leaves the five category pages. `estimate-page-schemas-one-file-per-rule` keeps it for every category, and a second copy would sign one promise twice. Two old lines say lint reads `computed: [rules]` and `ordered_children: true`. `guppi/lint.py` reads neither key, so the new line says the file holds them and lint does not read them. This is a line the code does not honour, corrected here and not dropped. 490.1 states a missing `schema.yaml` as the `schema` finding `schema.yaml is missing`, which `guppi/lint.py` gives. The old `Given:` said only "a missing file is a finding". "The six" files and "no seventh" become a statement with no count, so they cannot go stale. 490.7 moves into `Then:` the fact that `read_vault` does not read `schema.yaml` as a page. It drops the list of the files that may stand at the root of `wiki/`, because the check reads the rule pages for their names and keeps no list. Its old `－` line, "the finding it is today, not this one", becomes "no `layout` finding": 490.1 promises which finding a missing file gives, and 490.7 promises only that it is not a `layout` one.
The check of the answer also notes that the `then` lines of 490.2 to 490.6 share most of their words. This is expected. The five category schemas are read in the same way, and the old pages were written in one form. Each sub-case names its own file, its own lists and its own `pytest -k` run, so a fault in one schema fails one promise alone. It also notes that 490.7 shares words with 490.1. 490.1 is about the schema files themselves, and 490.7 is about how lint reads the pages next to them.
The frame. Each kept line was read against the live `schema.yaml` of its category, `check_descriptions`, `check_layout` and the missing-file finding of `guppi/lint.py`. None is contradicted. No behaviour changes, so no code, test, Render or hook changes, and no reader keeps an old form. The sentence of `rule-estimates-schema` on `Given:` "until the one pass of its migration" stays true, and so does the rest of its Render, which this Case does not touch. `estimate-insights-schema-checked` has no `Given:` and is not touched. The Case creates no page, so no vault query was run. Not done: the other four groups (17 pages).

## Problem

The seven Estimates of the page schemas and the layout of the vault still open with a `Given:` that describes the code of their day. Some of their lines record where a text came from, or state what lint reads when it does not read it. So their readings check history and stale claims next to the lasting promise.

## Given

`estimate-page-schemas-one-file-per-rule` — the promise, its Criterion replaced whole
**＋** `rule-page-schemas` — the MOC it promises for; its children render the files
**＋** `vault/wiki/<category>/schema.yaml` — the schema file of a category
**＋** `guppi/render.py` — writes each file and `render --check`
**＋** `guppi/lint.py` — reads each file; the classes `schema`, `path` and `schema-description`
**＋** `rule-governed-files-hook` — the hook that refuses a hand edit
**＋** `tests/test_render.py` — the test of two `full` pages on one file

## History

- 2026-09-29 created · raw/2026-09-28/2229/ledger.md#case-490.1
