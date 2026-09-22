# Frontier — 2026-09-22, hi 1121

## Cases

- [x] C1 — Slice 3f, themes 1–3 on the sprint page (`entity-sprint-migration`): closed by 304–306, still `- [ ]`; theme 3 and the Estimate line reworded from `terms` to `entity-glossary` / `## Terms` · sprint, brief · case 310
- [x] C2 — Slice 3f, theme 4 — `index.md`: one Case per §, covered by a rule page the § leaves, not covered a rule is made; the last Case removes the file and every `§N` pointer · sprint, brief · case 318
- [x] C3 — Slice 3f, theme 5 — scripts: the audit "script — what it assumes — what changes"; the `file` route and "applied by hand" out of `materialize`, `generate`, `prespec`, `lint`; the grep of `index.md` out of `rule-ask`; `rule-morph` kept compatible · sprint · case 320
- [x] C4 — Slice 3f, theme 6 — close: "Rule-class" retired in the Case schema and the glossary; `estimate-sprint-migration-rule-class-files-dissolved` read; the Slice moved to Closed · sprint · case 321
- [x] C5 — `rule-glossary` without `applies_to: [entity-glossary]`, `entity-glossary` without `rules`: the field dropped by `materialize` as `unknown` against the old schema; an `update` restores the edge; the order of a schema change and the creates that use it is a defect of the pipeline · brief · case 308
- [x] C6 — the readings of `estimate-rules-schema-checked` and `estimate-entities-schema-checked` folded into superseded creates and lost: `materialize` folds a reading into the first `create` of the slug, superseded or not; written again or the fold fixed · brief · case 309
- [x] C7 — `estimate-harness-pipeline`: a `replace` pair for "by its first two steps" — four steps of `make lint` now · brief · case 311
- [x] C8 — one Estimate with two `read` lines in one Spec (`estimate-lint-catches`, 304.8 and 305.5): `generate` ticks one; a form to refuse or a tick to add · brief · case 312
- [-] C9 — Slice 3b — `rule-work-mode`, `rule-subagent-guppi` (defer 307, the eighteenth), the sentence of `insight-workflow-code-live-before-the-page-it-reads` into `rule-work-mode` · brief · defer case 322

## Work

- [x] W1 — read `estimate-page-schemas-one-file-per-rule` (0014 line 70) by hand: `make lint`, `render --check` · brief · work
- [x] W2 — read `estimate-rules-schema-checked` (0014 line 1008) and `estimate-entities-schema-checked` (0014 line 1307): pytest and `make lint` — L52, L53 of 0014 did not reach the pages · brief · work
- [x] W3 — read `estimate-glossary-terms-defined` (0014 line 1444) by hand: the table and `make lint` · brief · work
- [x] W4 — read `estimate-documentation-completes` (0014 line 1504) by hand: the librarian's run of 0014, step 6 in the event log · brief · work
- [x] W5 — read `estimate-harness-pipeline` (0014 line 1544) by hand: `make test-harness`, then `make lint`, four steps · brief · work
- [x] W6 — read `estimate-case-protocol-loaded` (0014 line 1591) at this `/hi`, by hand · brief · work
- [x] W7 — read `estimate-sprint-migration-rule-class-files-dissolved` (1853 line 318) at the close of Slice 3f, by its `method` · brief · work
- [x] W8 — read `estimate-synthesis-keeps-actioned-by-the-mark` (1853 line 406) at the first marked lesson; no date · brief · work
- [x] W9 — read `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-merges` at the close of the sprint, by their `method` · brief · work
