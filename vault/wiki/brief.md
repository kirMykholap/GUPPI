# Brief — 2026-09-28, the librarian's run over session 2229 of 2026-09-28

## Where things stand

- Session 2229 ratified 486, 487.1–487.4, 488.1–488.6, 489.1–489.8, 490.1–490.8, 491.1–491.5, 492.1–492.4, 493.1–493.6, 494.1–494.6, 495 and 496 (handoff).
- Commits b67fc6c (code) and d7ad72f (the session folder). Code: `fence_breaks` in `guppi/materialize.py`, `check_pairs` in `guppi/prespec.py`, the class `fence` in `guppi/lint.py`, 15 tests added. The session's `make test` gave 891 passed, 2 skipped; `make style` clean (handoff).
- Not done in the session (handoff): the `fence` findings on `rule-retro` and `rule-synthesis`, waiting for this run; the `fence` finding on `decision-case-13`, left with the old Decision pages 1–28; the 109 Baseline findings; lessons L52 and L53; the stale `guppi/__pycache__/__init__.cpython-314.pyc`; the readings of Readings due and the unticked `read` lines of the Specs of sessions 2000, 1318 and 0000.
- The walk named `raw/2026-09-28/0000/`, `1318/` and `2000/` (each extended with 0 entries; `generate` 0 pages each) and `raw/2026-09-28/2229/` (written with 53 entries from the 53 lines of its ledger).
- Yaml of 2229: 53 entries from the ledger: 2 `create` (Estimates, 487.1, 487.2), 46 `update` (3 rules, 37 Estimates, 6 on `entity-sprint-migration`), 2 `defer` (495, 496, both `exists`), 2 `lesson`. The synthesis added 2 `update` entries. All 55 `applied`. No `failed`, `near` or `merged`. 1 `incomplete` (L52). `unparsed: []`.
- Pages (`generate`: 119 pages written or changed, `log.md` included; `cleanup`: 0 pages moved):
  - decisions: 50 created (486, 487.1–487.4, 488.1–488.6, 489.1–489.8, 490.1–490.8, 491.1–491.5, 492.1–492.4, 493.1–493.6, 494.1–494.6, 495, 496).
  - rules: 3 updated by Cases: `rule-retro` (486), `rule-prespec` (487.1), `rule-synthesis` (487.3). 2 defers: `rule-case-build` (495), `rule-skill-wait-what` (496). Cascade built → draft on 19: `rule-atomicity`, `rule-claude-md`, `rule-compact-recall`, `rule-decisions-schema`, `rule-entities-schema`, `rule-estimates-schema`, `rule-glossary`, `rule-lessons-schema`, `rule-lint`, `rule-materialize`, `rule-one-judgment-one-implementation`, `rule-page-schemas`, `rule-plan-mode`, `rule-prespec-hook`, `rule-render-harness`, `rule-retro-commit`, `rule-rules-schema`, `rule-sprint`, `rule-vault-layout`.
  - estimates: 2 created, `pending`: `estimate-prespec-catches-a-broken-fence`, `estimate-lint-catches-a-broken-fence`. 37 updated by Cases (36 by 488–494, 1 by 487.4), all `pending`; 33 of them went passed → pending, 4 were `pending` before.
  - entities: `entity-sprint-migration` updated by 488.6, 489.8, 490.8, 491.5, 492.4, 493.6 and 494.6. Cascade built → draft: `entity-glossary`, `entity-guppi`.
  - lessons: 2 created: `lesson-prespec-judged-a-pair-by-its-anchor-alone` (`new`), `lesson-generate-replaced-a-ratified-criterion-on-a-field-update` (`clustered`).
  - insights: 1 updated by the synthesis: `insight-materialize-estimate-update-lifts-the-criterion-whole`, a third child, `actioned` → `open`, severity 1.
- Governed files `render` wrote: `.claude/skills/retro/SKILL.md` (`rule-retro`), `.claude/skills/pre-spec/SKILL.md` (`rule-prespec`), `.claude/agents/librarian-guppi.md` (`rule-synthesis`). `guppi sprint` rewrote `vault/wiki/sprint.md`: two items of the Rule-class milestone went from ticked `passed` to unticked `pending`, and Slice 3g holds one note, "the old shape recut". `guppi backlog` rewrote `vault/wiki/backlog.md`: 18 → 21 items (`rule-case-build`, `rule-skill-wait-what`, the reopened Insight). `guppi glossary` left `vault/wiki/glossary.md` unchanged.
- `generate` ticked 53 lines of `raw/2026-09-28/2229/spec.md`.

## Readings due

73 Estimates stand `pending` or `failed` after `generate`: 2 `failed`, 71 `pending`. Every rule or entity they read stands `draft`.

- `estimate-case-build-writes-a-plain-round` — `failed` — `rule-case-build` draft — by hand, one round of case-guppi read in the chat against the four parts of the Criterion (method). Result: Case 482 Q2 and Q4 give no before, Case 483 Q3 and Q4 give only "After:".
- `estimate-skill-wait-what-re-pitches` — `failed` — `rule-skill-wait-what` draft — `uv run guppi render --check`; by hand, one run of the skill read in the chat (method). Result: the re-pitch of round 2 Q1 on Case 485 showed a made-up example and did not ask the case-guppi of the Case for a real line.
- `estimate-prespec-catches-a-broken-fence` — `rule-prespec` draft — `raw/2026-09-28/2229/spec.md` line 115.
- `estimate-lint-catches-a-broken-fence` — `rule-lint` draft — `raw/2026-09-28/2229/spec.md` line 155.
- `estimate-materialize-judges-a-fence` — `rule-materialize` draft — `raw/2026-09-28/2229/spec.md` line 222.
- `estimate-glossary-renders-the-terms` — `rule-glossary` draft — `raw/2026-09-28/2229/spec.md` line 268.
- `estimate-glossary-checks-the-file` — `rule-glossary` draft — `raw/2026-09-28/2229/spec.md` line 300.
- `estimate-glossary-ticks-the-spec` — `rule-glossary` draft — `raw/2026-09-28/2229/spec.md` line 335.
- `estimate-glossary-terms-defined` — `entity-glossary` draft — `raw/2026-09-28/2229/spec.md` line 364.
- `estimate-guppi-tests-green` — `entity-guppi` draft — `raw/2026-09-28/2229/spec.md` line 392.
- `estimate-generate-writes` — `rule-page-generation` draft — `raw/2026-09-28/2229/spec.md` line 476.
- `estimate-generate-walks-dates` — `rule-page-generation` draft — `raw/2026-09-28/2229/spec.md` line 511.
- `estimate-generate-renames` — `rule-page-generation` draft — `raw/2026-09-28/2229/spec.md` line 546.
- `estimate-generate-rewords` — `rule-page-generation` draft — `raw/2026-09-28/2229/spec.md` line 579.
- `estimate-generate-writes-rules-from-applies-to` — `rule-page-generation` draft — `raw/2026-09-28/2229/spec.md` line 610.
- `estimate-materialize-lifts-unfiltered-on-a-schema-change` — `rule-materialize` draft — `raw/2026-09-28/2229/spec.md` line 641.
- `estimate-materialize-refolds-a-reading-on-a-supersede` — `rule-materialize` draft — `raw/2026-09-28/2229/spec.md` line 671.
- `estimate-page-schemas-one-file-per-rule` — `rule-page-schemas` draft — `raw/2026-09-28/2229/spec.md` line 743.
- `estimate-rules-schema-checked` — `rule-rules-schema` draft — `raw/2026-09-28/2229/spec.md` line 776.
- `estimate-entities-schema-checked` — `rule-entities-schema` draft — `raw/2026-09-28/2229/spec.md` line 809.
- `estimate-estimates-schema-checked` — `rule-estimates-schema` draft — `raw/2026-09-28/2229/spec.md` line 841.
- `estimate-decisions-schema-checked` — `rule-decisions-schema` draft — `raw/2026-09-28/2229/spec.md` line 874.
- `estimate-lessons-schema-checked` — `rule-lessons-schema` draft — `raw/2026-09-28/2229/spec.md` line 906.
- `estimate-vault-layout-holds` — `rule-vault-layout` draft — `raw/2026-09-28/2229/spec.md` line 939.
- `estimate-sprint-ticks-the-spec` — `rule-sprint` draft — `raw/2026-09-28/2229/spec.md` line 1010.
- `estimate-sprint-checks-the-file` — `rule-sprint` draft — `raw/2026-09-28/2229/spec.md` line 1042.
- `estimate-sprint-drops-an-emptied-milestone` — `rule-sprint` draft — `raw/2026-09-28/2229/spec.md` line 1075.
- `estimate-render-harness-ticks-the-spec` — `rule-render-harness` draft — `raw/2026-09-28/2229/spec.md` line 1107.
- `estimate-atomicity-rendered` — `rule-atomicity` draft — `raw/2026-09-28/2229/spec.md` line 1178.
- `estimate-claude-md-rendered` — `rule-claude-md` draft — `raw/2026-09-28/2229/spec.md` line 1212.
- `estimate-one-judgment-one-implementation-followed` — `rule-one-judgment-one-implementation` draft — `raw/2026-09-28/2229/spec.md` line 1245.
- `estimate-compact-recall-reloads` — `rule-compact-recall` draft — `raw/2026-09-28/2229/spec.md` line 1319.
- `estimate-plan-mode-verified` — `rule-plan-mode` draft — `raw/2026-09-28/2229/spec.md` line 1351.
- `estimate-retro-commit-gates` — `rule-retro-commit` draft — `raw/2026-09-28/2229/spec.md` line 1387.
- `estimate-session-phases-in-order` — `rule-session` draft — `raw/2026-09-28/2229/spec.md` line 1417.
- `estimate-prespec-hook-gates` — `rule-prespec-hook` draft — `raw/2026-09-28/2229/spec.md` line 1451.
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` draft — `raw/2026-09-28/2229/spec.md` line 1519.
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` draft — `raw/2026-09-28/2229/spec.md` line 1553.
- `estimate-sprint-migration-merges` — `entity-sprint-migration` draft — `raw/2026-09-28/2229/spec.md` line 1583.
- `estimate-sprint-migration-rule-class-files-dissolved` — `entity-sprint-migration` draft — `raw/2026-09-28/2229/spec.md` line 1616.
- `estimate-sprint-migration-index-dissolved` — `entity-sprint-migration` draft — `raw/2026-09-28/2229/spec.md` line 1648.
- `estimate-close-commits` — `rule-close` draft — `archive/migration/2026-09-28/2000/raw/spec.md` line 58.
- `estimate-retro-report-holds-each-fact-once` — `rule-retro` draft — `archive/migration/2026-09-28/2000/raw/spec.md` line 129.
- `estimate-prespec-catches-a-command-line-off-form` — `rule-prespec` draft — `archive/migration/2026-09-28/2000/raw/spec.md` line 184.
- `estimate-prespec-catches-a-superseded-case` — `rule-prespec` draft — `archive/migration/2026-09-28/2000/raw/spec.md` line 215.
- `estimate-prespec-catches-a-method-without-a-form` — `rule-prespec` draft — `archive/migration/2026-09-28/2000/raw/spec.md` line 247.
- `estimate-prespec-catches-an-unwrapped-render` — `rule-prespec` draft — `archive/migration/2026-09-28/2000/raw/spec.md` line 280.
- `estimate-prespec-catches-bare-wikilinks` — `rule-prespec` draft — `archive/migration/2026-09-28/2000/raw/spec.md` line 312.
- `estimate-prespec-simulates-the-pairs` — `rule-prespec` draft — `archive/migration/2026-09-28/2000/raw/spec.md` line 342.
- `estimate-session-start-context` — `rule-session-start` draft — `archive/migration/2026-09-28/2000/raw/spec.md` line 413.
- `estimate-hi-no-read-calls` — `rule-skill-hi` draft — `archive/migration/2026-09-28/2000/raw/spec.md` line 446.
- `estimate-git-context-current` — `rule-git-context` draft — `archive/migration/2026-09-28/2000/raw/spec.md` line 478.
- `estimate-github-issues-listed` — `rule-github-issues` draft — `archive/migration/2026-09-28/2000/raw/spec.md` line 507.
- `estimate-ledger-tail` — `rule-ledger-tail` draft — `archive/migration/2026-09-28/2000/raw/spec.md` line 545.
- `estimate-agent-writing-followed` — `rule-agent-writing` draft — `archive/migration/2026-09-28/1318/raw/spec.md` line 497.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `rule-work-mode` draft — `archive/migration/2026-09-28/1318/raw/spec.md` line 743.
- `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — `rule-retro` draft — `archive/migration/2026-09-28/1318/raw/spec.md` line 788 and `archive/migration/2026-09-28/0000/raw/spec.md` line 303.
- `estimate-retro-red-in-the-baseline-is-not-charged` — `rule-retro` draft — `archive/migration/2026-09-28/1318/raw/spec.md` line 838.
- `estimate-permissions` — `rule-permissions` draft — `archive/migration/2026-09-28/1318/raw/spec.md` line 886.
- `estimate-case-check-notes-a-then-line-shared-by-siblings` — `rule-case-check` draft — `archive/migration/2026-09-28/0000/raw/spec.md` line 181.
- `estimate-documentation-completes` — `rule-documentation` draft — `archive/migration/2026-09-28/0000/raw/spec.md` line 468.
- `estimate-synthesis-clusters` — `rule-synthesis` draft — `archive/migration/2026-09-28/0000/raw/spec.md` line 504. The yaml of 2229 holds two lesson entries.
- `estimate-carry-over-writes` — `rule-carry-over` draft — `uv run guppi render --check`; by hand, the first /carry after the fork of ExitPlanMode (method).
- `estimate-case-build-writes-the-case` — `rule-case-build` draft — by hand, live dispatches in a session after the render (method).
- `estimate-case-check-sends-back-a-faulty-case` — `rule-case-check` draft — `uv run pytest tests/test_casecheck.py -k subagent`, then by hand the first answer the hook sends back (method).
- `estimate-case-check-shows-only-the-checked-case` — `rule-case-check` draft — `uv run pytest tests/test_casecheck.py -k stop`, then by hand the first reply the hook refuses (method).
- `estimate-case-protocol-defers-in-one-reply` — `rule-case-protocol` draft — by hand, the first defer the person asks for after the render (method).
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` draft — by hand, the ledger and the preview of the first session where a lesson and the Case that closes its cause stand together (method).
- `estimate-context-size-warns-past-the-limit` — `rule-context-size` draft — `uv run pytest tests/test_context.py -k limit`; by hand at the first prompt past 400 000 tokens (method).
- `estimate-event-log-records` — `rule-event-log` draft — pytest in `tests/test_event.py` and `tests/test_gate.py`; by hand, one /hi outside plan mode and one in it (method).
- `estimate-generate-writes-the-decision-page` — `rule-page-generation` draft — `pytest tests/test_generate.py`; the live reading in the librarian's run (method).
- `estimate-handoff-holds-each-fact-once` — `rule-handoff` draft — by hand at the first /handoff after the render (method).
- `estimate-spec-write-reaches-the-approved-spec` — `rule-spec-write` draft — `uv run pytest tests/test_ratified.py -k approved_spec`; by hand, the first Case ratified in Work Mode after the change (method).

## Flags

- `incomplete`: `lesson-prespec-judged-a-pair-by-its-anchor-alone` (L52) lacks `addressed_by`. Its line carries `{addressed_by:case 487}`; the unit holds decision lines for 487.1–487.4 and none for 487, so `materialize` found no decision line of that Case. The page is written with status `new` and no `addressed_by`.
- `failed`, `near`, `merged`, `unparsed`: none in the yaml of 2229. The yaml of 0000 still carries `incomplete` on three entries and the yaml of 1318 `near: rule-morph` on one; no script changed them in this run.
- Index check: the two `create` entries are Estimates; no index line compared.
- Synthesis: the two lessons compared with 58 index lines of `lessons/` and 26 of `insights/`.
  - `lesson-generate-replaced-a-ratified-criterion-on-a-field-update` has the pattern of `insight-materialize-estimate-update-lifts-the-criterion-whole`. It is `clustered` under it. The Insight gets the lesson as its third child and goes `actioned` → `open`: the lesson entry carries no `addressed_by`. The Insight's `addressed_by` stays `decision-case-296`.
  - `lesson-prespec-judged-a-pair-by-its-anchor-alone`: no shared root cause found. It stays `new`.
- Failed Estimates: 2, listed first under Readings due.
- Handoff instruction on Case 487: 487.1–487.4 all `applied`, 487.4 (L51) included.
- Handoff instruction on lint `fence`: after the run the class holds one finding, `decisions/decision-case-13` (`## When`, a fence open at the end of the section). No `fence` finding on `rule-retro` or `rule-synthesis`.
- Handoff instruction on 494.6: `vault/wiki/sprint.md` shows Slice 3g with one note, "the old shape recut".
- Handoff instruction on `purpose`: `estimate-generate-writes`, `estimate-generate-walks-dates`, `estimate-plan-mode-verified`, `estimate-retro-commit-gates` and `estimate-prespec-hook-gates` each carry a `purpose` line.
- Handoff instruction on the Estimates of 488–494: no entry `failed`. The yaml holds 36 Estimate updates for 488–494; the handoff says 38 Estimates. `estimate-generate-writes` holds 12 `＋` lines.
- Handoff: the History `change` lines of 488.6–493.6 on `entity-sprint-migration` end with "the note on every other Estimate stands"; 494.6 removed that note. The person chose to keep the lines.
- Handoff: on 489 the person kept `estimate-generate-writes` as one page, with no split and no backlog item, against the recommendation.
- Handoff: `decision-case-13` is not fixed in this session; it stays with the old Decision pages 1–28.
- Handoff: the trial run of `materialize`, `generate` and `render` was dropped; nothing records it.
- Handoff: the harness filter "settings-json" fired twice on answers of `case-guppi`, on a `given` line naming `.claude/settings.json`.
- `sprint.md`: the items "No Rule-class file at the close of Slice 3f" and "index.md is gone" went from ticked `passed` to unticked `pending`: 494.4 and 494.5 set their Estimates `pending`.
- Contradictions: none found in this run.
- MOC candidates: none named by lint.
- Stale defers, from lint: `rule-subagent-guppi` 31 times since case 29; `rule-morph` once since case 239; `rule-orchestration` once since case 424; `rule-case-build-checks-its-sub-cases` once since case 480; `rule-prespec-script-skips-code-spans` once since case 481.
- Backlog moves by `generate`: none printed. Milestones dropped: none printed.
- `materialize`, `generate`, `cleanup`, `render`, `sprint`, `backlog`, `glossary`: no stderr lines.
- `archive` (run after the brief): exit 0. It moved `raw/2026-09-28/0000`, `1318` and `2000` to `archive/migration/2026-09-28/<id>/raw`; it kept `raw/2026-09-28/2229`, the session of the run. The Spec and ledger paths above name the moved units at their new place. No stderr lines.
- `make lint`, after the render: exit 2, 145 findings (109 at the last brief).
  - `schema: missing section ## Context` and `## Problem` on 31 Decision pages (cases 1–28). That is 62 findings.
  - `rules/rule-spec-box`: `schema: missing field kind`, `missing field estimates`, and `orphan`.
  - `decisions/decision-case-13: fence`.
  - 5 `deferred` findings, the stale defers above.
  - `unread: pending` on 71 Estimates and `unread: failed` on 2. These are the 73 Estimates of Readings due.
  - `estimates: unmigrated: 12 pages in the shape before case 193`.

## Next session

Cases:
- `estimate-case-build-writes-a-plain-round` `failed` (L25 of `archive/migration/2026-09-28/2000/raw/ledger.md`): rounds of case-guppi whose options give no before and after; put off by 495.
- `estimate-skill-wait-what-re-pitches` `failed` (L26 of `archive/migration/2026-09-28/2000/raw/ledger.md`): the re-pitch showed a made-up example; put off by 496.
- L52 of `raw/2026-09-28/2229/ledger.md` names `{addressed_by:case 487}`, a Case whose decision lines are 487.1–487.4 only; the mark did not reach the lesson (found in this run).

Work:
- The 71 `pending` readings of Readings due, by slug.
- The unticked boxes of the Specs, all `read` lines: `raw/2026-09-28/2229/spec.md` (39), `archive/migration/2026-09-28/2000/raw/spec.md` (13), `archive/migration/2026-09-28/1318/raw/spec.md` (5), `archive/migration/2026-09-28/0000/raw/spec.md` (4).
- The stale `guppi/__pycache__/__init__.cpython-314.pyc` (handoff).
- Ledger lines this run did not apply: none; the 53 lines of `raw/2026-09-28/2229/ledger.md` each have an entry.

## Readings at the close

- `make test`: 891 passed, 2 skipped.
- `make lint`: exit 2, 145 findings.
- Pages: decisions 746, estimates 156, rules 72, lessons 60, insights 26, entities 4.
