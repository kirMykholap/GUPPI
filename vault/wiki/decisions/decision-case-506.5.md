---
type: decision
case: "506.5"
status: current
update: ["[[estimate-generate-fails-alone]]", "[[rule-case-protocol]]"]
origin: raw/2026-09-29/1134/ledger.md#case-506.5
sprint: migration
created: 2026-09-29
tags: [harness, workflow, ledger, tests, session]
---

## Context

Until case 193, an Estimate page kept its check method in a `## Method` section and the Case's problem in a `## Context` section, and its Criterion could hold `### case N` blocks. Since then `method` is a one-line field and the Criterion is one text. Old pages were converted one at a time, so the scripts learned both shapes. `guppi lint` counts the old pages in one line, `estimates: unmigrated: <N> pages in the shape before case 193`. It reads `## Method` when a page has no `method` field, and it checks that each `### case N` block names a real Decision page. `guppi generate` refuses a Criterion rewrite on a page with no `method` field, and it deletes `## Context` and `## Method` when an update sets `method`. The schema keeps `purpose` and `method` optional "until their recut", and it describes the two old sections. The last librarian's run counted 0 `unmigrated` pages. No live Estimate has a `## Context`, a `## Method`, a `### case N` block or a `Given:` line. All 157 live Estimates have a `method` field, and 12 have no `purpose`. So the transition code handles nothing now. There is one gap: `check_method` of `guppi/lint.py` gives no finding when a page has no method. Once the count leaves, a new Estimate without `method` would pass unnoticed.
The person decided in one round. The code leaves `guppi/lint.py` and `guppi/generate.py`. `guppi/materialize.py` keeps its handling of the `context` and `criterion` keys, because those rules deal with how a Case item is written (cases 189, 194.1), not with the shape of a page. `method` becomes a required field and `purpose` stays optional. The schema also loses the sentence that older pages keep their `Given:`. `estimate-sprint-migration-lint-clean` is left as it stands. Its words "`unmigrated` included — the counter at zero" stay true once the old shape is gone, and it is already `pending` for its reading at the close of the sprint. For the same reason the Slice 5 line of `entity-sprint-migration` that names the counter stands.
What `case-guppi` found in the frame. The case-schema sentence "`set.method` when the page has no `method` field, since the recut brings the page to the shape of case 193 and `generate` refuses one without it (case 211)" would become false. So 506.5 changes it in `rule-case-protocol`, and `vault/wiki/case-schema.md` is rendered again. Five Estimates have a Criterion that speaks of the removed code. Each is replaced whole in its own sub-case: `estimate-estimates-schema-checked`, `estimate-lint-checks-the-method`, `estimate-lint-finds-a-broken-link`, `estimate-generate-fails-alone` and `estimate-generate-writes`. `estimate-lint-counts-the-unmigrated` is deleted, and the cascade takes it out of the `estimates` of `rule-lint`, as in case 445.4. The check of the answer notes the changed or dropped Criterion lines of 506.1 and 506.3 to 506.6 as not carried. They are changed on purpose: each names the old shape, the count, the `## Method` fallback, the `### case N` link, the recut refusal or the `set.method` drop. Every other line is kept word for word. The check also notes that a `then` line of 506.2 and one of 506.3 share words with 506.1. This is expected. 506.1 promises the `schema` finding for a missing `method`. 506.2 promises that no other line reports it. 506.3 promises that `lint` reads no `## Method` section, while 506.1 says the schema text no longer names that section. They are separate promises with separate tests. Pre-spec found that the first rewrite of the description paragraph in 506.1 said `checked` is written "at the first reading". The `checked` field of the same Render says it is "written by `generate` on every reading (case 201.1)". The new clause now uses those words and that source. `estimate-estimates-schema-checked` and `estimate-generate-writes` are already `pending` and are Frontier items W22 and W29. After this Case their readings wait for a later session (case 428.1). The sentence of `rule-decisions-schema` on the `## Criterion` of old Decision pages describes Decision pages, which keep that section, so it stands. No reader here refuses anything. `guppi lint` only goes red, and all live Estimates already have `method`, so no old form is kept. The near backlog item `insight-materialize-estimate-update-lifts-the-criterion-whole` deals with how `materialize` lifts a Criterion into an update. This Case does not touch that, so the item stands. The Case creates no page, so no vault query was run. Not done: the `materialize` key rules of older Case formats, and a `purpose` on the 12 pages without one.

## Problem

The old Estimate shape is gone from the vault, but the scripts, the schema, the case schema and the sprint page still describe and handle it. The count that stood in for a required `method` field is the only guard against an Estimate with no method, so it cannot simply be removed.

## Given

`guppi/generate.py` — the refusal `a recut without method` in `update`, and the docstring
**＋** `tests/test_generate.py` — the tests of a failing entry
**＋** `estimate-generate-fails-alone` — the promise, its Criterion replaced whole
**＋** `rule-case-protocol` — its Render names the refusal
**＋** `vault/wiki/case-schema.md` — the file rendered from it
**＋** `materialize.yaml` — the entries `generate` applies
**＋** `vault/wiki/log.md` — the log appended after each entry

## History

- 2026-09-29 created · raw/2026-09-29/1134/ledger.md#case-506.5
