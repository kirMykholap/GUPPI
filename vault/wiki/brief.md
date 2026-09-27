# Brief — 2026-09-27, the librarian's run over session 2300 of 2026-09-26

## Where things stand

- Session 2300 ratified Cases 443 (443.1–443.3), 444 (444.1–444.3), 445 (445.1–445.4, 445.6, 445.7) and 446, and deferred Cases 447 (`rule-work-mode`) and 448 (`insight-hi-skill-substitution-checked-by-a-model-call`). 445.7 supersedes 445.5. Frontier C1 and C2 stay for the sprint; C8, C10 and C11 are deferred and kept (handoff).
- Code, commit b2825a0: `guppi/materialize.py`, `guppi/ratified.py`, `guppi/prespec.py`, `guppi/casecheck.py`, `guppi/ledger.py`, `guppi/event.py`, `guppi/cli.py`; tests in `test_materialize.py`, `test_ratified.py`, `test_prespec.py`, `test_event.py`. The session's `make test` gave 734 passed, 2 skipped; `make style` was clean (handoff).
- Readings of the session: 2, both `failed`: `estimate-case-protocol-case-form` (W30) and `estimate-agent-writing-followed` (W31) (handoff, ledger lines 35–36).
- Not done in the session: the `read` lines of the 11 Estimates the session creates or updates; Frontier Work lines W1–W29; W32 `estimate-language-followed`, whose Criterion Case 446 replaced (handoff).
- The walk named `raw/2026-09-26/1337/` and `raw/2026-09-26/1745/` (0 new entries each, 0 pages written) and `raw/2026-09-26/2300/`.
- Yaml of 2300: 36 entries from the 36 lines of the ledger: 23 `update`, 5 `create`, 1 `delete`, 2 `defer` (both `exists`), 3 `lesson`, 2 `estimate`. The librarian added 5 entries (synthesis): 1 `create` of an Insight, 1 `update` of an Insight, 3 `update` of lessons. 39 of 41 are `applied`; lines 23 and 24 (445.5) carry `superseded_by: 445.7` and were not applied.
- Pages (`generate`: 67 pages written or changed; `cleanup`: 3 pages moved):
  - decisions: 16 created (443.1–443.3, 444.1–444.3, 445.1–445.7, 446, 447, 448). `decision-case-423` became `superseded` by 445.1 and `decision-case-445.5` by 445.7; both `archived` and moved by `cleanup`.
  - rules: 1 created: `rule-skill-grill-me` (443.1, child of `rule-plan-mode`). 10 updated: `rule-case-build` (443.2), `rule-case-protocol` (443.3, 444.3, 445.2), `rule-spec-write` (444.2, 445.2), `rule-spec-reconcile` (445.1; its defer by 423 superseded), `rule-hook-registry` (445.1), `rule-case-check` (445.2), `rule-prespec` (445.4), `rule-event-log` (445.6), `rule-language` (446), `rule-skill-hi` (445.7). 1 deferred: `rule-work-mode` (447). Cascade: `rule-event-log` and `rule-spec-reconcile` built → draft.
  - estimates: 3 created, `pending`: `estimate-skill-grill-me-asks-in-rounds` (443.1), `estimate-materialize-judges-a-fence` (444.1), `estimate-language-spec-prose-in-english` (445.4). 1 renamed and updated: `estimate-spec-reconcile-shows-a-changed-case` → `estimate-spec-reconcile-refuses-an-edit-of-the-plan` (445.1). 7 updated by Cases, all `pending`: `estimate-case-build-writes-the-case` (443.2), `estimate-case-protocol-shows-the-built-case` (443.3), `estimate-spec-write-copies-the-ratified-case` (444.2), `estimate-spec-write-checks-the-written-case` (445.2), `estimate-spec-write-removes-a-superseded-case` (445.3), `estimate-event-log-records` (445.6), `estimate-language-followed` (446). 2 updated by readings, both `failed`. 1 deleted: `estimate-prespec-checks-the-ratified-copy` (445.4), moved by `cleanup`. `estimate-skill-hi-opens-only-in-plan-mode` was not created (445.5 superseded).
  - lessons: 3 created: `lesson-case-build-a-list-in-context` (`clustered`), `lesson-case-build-one-promise-signed-in-two-sub-cases` (`clustered`), `lesson-ledger-a-dropped-item-needs-a-superseding-sub-case` (`new`). 1 updated: `lesson-case-build-a-criterion-replaced-whole-drops-a-line` (`clustered`).
  - insights: 1 created: `insight-case-build-promise-lines-compared-by-no-check` (`open`). 2 updated: `insight-case-form-chat-form-read-by-no-script` (child added, `actioned` → `open`); `insight-hi-skill-substitution-checked-by-a-model-call` (deferred by 448).
  - entities: 1 updated: `entity-sprint-migration` (443.1).
  - git status also shows 14 decision pages of earlier Cases changed by `generate` with no line in `log.md`: 387.3, 396.1, 396.2, 437, 441.1–441.10; see Flags.
- Governed files `render` rewrote: `.claude/settings.json` (`rule-hook-registry`: `guppi ratified --guard` on PreToolUse of Edit, Write and MultiEdit; `guppi ratified --edit` gone from PostToolUse), `.claude/skills/grill-me/SKILL.md`, `.claude/agents/case-guppi.md`, `.claude/skills/pre-spec/SKILL.md`, `CLAUDE.md`, `vault/wiki/case-schema.md`. `guppi sprint` rewrote `vault/wiki/sprint.md`; `guppi glossary` changed nothing.

## Readings due

34 Estimates stand `pending` or `failed` after `generate`: 3 `failed`, 31 `pending`.

- `estimate-case-protocol-case-form` — `failed` — `rule-case-protocol` draft — by hand, the Cases of a session at its close (method). Result: the context of Case 446 carries a count of items and case numbers it is not about (378.5, 428.1), and the problem of Case 445 cites case 410, which the Case is not about.
- `estimate-agent-writing-followed` — `failed` — `rule-agent-writing` draft — by hand, the section in `CLAUDE.md` and one reply against it (method). Result: a reply said the ledger gained amended lines of 445.6 where the tail shows L31 alone new, and one reply gave W32 a closer the Frontier gives only to sprint items.
- `estimate-case-protocol-defers-in-one-reply` — `failed` — `rule-case-protocol` draft — by hand, the first defer the person asks for after the render (method). Result: Case 442 was shown in the short form, but the agent then edited the plan file to translate its heading, context and problem, and text followed the Frontier in the reply.
- `estimate-skill-grill-me-asks-in-rounds` — `rule-skill-grill-me` draft — `raw/2026-09-26/2300/spec.md` line 99.
- `estimate-case-build-writes-the-case` — `rule-case-build` draft — `raw/2026-09-26/2300/spec.md` line 161; `archive/migration/2026-09-26/1745/raw/spec.md` line 240.
- `estimate-case-protocol-shows-the-built-case` — `rule-case-protocol` draft — `raw/2026-09-26/2300/spec.md` line 209; `archive/migration/2026-09-26/1745/raw/spec.md` line 287; `archive/migration/2026-09-26/1337/raw/spec.md` line 163.
- `estimate-materialize-judges-a-fence` — `rule-materialize` draft — `raw/2026-09-26/2300/spec.md` line 269.
- `estimate-spec-write-copies-the-ratified-case` — `rule-spec-write` draft — `raw/2026-09-26/2300/spec.md` line 328; `archive/migration/2026-09-26/1745/raw/spec.md` line 590; `archive/migration/2026-09-26/1337/raw/spec.md` lines 232 and 436.
- `estimate-spec-reconcile-refuses-an-edit-of-the-plan` — `rule-spec-reconcile` draft — `raw/2026-09-26/2300/spec.md` line 436.
- `estimate-spec-write-checks-the-written-case` — `rule-spec-write` draft — `raw/2026-09-26/2300/spec.md` line 507; `archive/migration/2026-09-26/1745/raw/spec.md` line 626.
- `estimate-spec-write-removes-a-superseded-case` — `rule-spec-write` draft — `raw/2026-09-26/2300/spec.md` line 541; `archive/migration/2026-09-26/1745/raw/spec.md` line 537.
- `estimate-language-spec-prose-in-english` — `rule-language` draft — `raw/2026-09-26/2300/spec.md` line 596.
- `estimate-event-log-records` — `rule-event-log` draft — `raw/2026-09-26/2300/spec.md` line 651.
- `estimate-language-followed` — `rule-language` draft — `raw/2026-09-26/2300/spec.md` line 732, by hand in a later session.
- `estimate-materialize-lifts-a-create-by-the-schema` — `rule-materialize` draft — `archive/migration/2026-09-26/1745/raw/spec.md` line 96.
- `estimate-materialize-assembles` — `rule-materialize` draft — `archive/migration/2026-09-26/1745/raw/spec.md` line 132.
- `estimate-case-check-shows-only-the-checked-case` — `rule-case-check` draft — `archive/migration/2026-09-26/1745/raw/spec.md` line 335.
- `estimate-prespec-reconciles` — `rule-prespec` draft — `archive/migration/2026-09-26/1745/raw/spec.md` line 381.
- `estimate-spec-write-reaches-the-approved-spec` — `rule-spec-write` draft — `archive/migration/2026-09-26/1745/raw/spec.md` line 479.
- `estimate-spec-capture-appends` — `rule-spec-capture` draft — `archive/migration/2026-09-26/1745/raw/spec.md` line 659.
- `estimate-case-check-sends-back-a-faulty-case` — `rule-case-check` draft — `archive/migration/2026-09-26/1337/raw/spec.md` lines 107 and 368.
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` draft — by hand, the ledger and preview of the first session where a lesson and the Case that closes its cause stand together, and of the first Case that takes up a decision with more than one Case in its `deferred_by` (method).
- `estimate-context-size-warns-past-the-limit` — `rule-context-size` draft — `uv run pytest tests/test_context.py -k limit`; by hand at the first prompt past 400 000 tokens (method).
- `estimate-retro-loads` — `rule-retro` draft — by hand at the first `/retro` (method).
- `estimate-retro-report-holds-each-fact-once` — `rule-retro` draft — by hand at the first `/retro` after the render (method).
- `estimate-carry-over-writes` — `rule-carry-over` draft — pytest over the skill's render, plus one live reading of a carried-over session (method).
- `estimate-documentation-completes` — `rule-documentation` draft — `make test-documentation`, then the live reading by hand (method).
- `estimate-session-phases-in-order` — `rule-session` draft — by hand at the close of a session, the day's records in order (method).
- `estimate-sprint-renders-the-backlog` — `rule-sprint` draft — `pytest tests/test_sprint.py`, plus one reading of the rendered `sprint.md` after the librarian's run (method).
- `estimate-synthesis-keeps-actioned-by-the-mark` — `rule-synthesis` draft — by hand, the yaml and the brief after the librarian's run on the first marked lesson clustered under an actioned Insight (method).
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` draft — by hand, the tree at the close of the sprint (method).
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` draft — `make lint` exit 0, or only unread lines on the Estimates of the sprint (method).
- `estimate-sprint-migration-merges` — `entity-sprint-migration` draft — `make test` on the last commit of migration, then `git log` of main after the merge (method).
- `estimate-sprint-migration-rule-class-files-dissolved` — `entity-sprint-migration` draft — by hand, the listed `ls`, `grep`, `render --check` and `glossary --check` (method).

## Deferred

1. `insight-case-show-built-case-retyped-by-hand` — severity 2 — The main agent writes the Case that case-guppi built out again by hand instead of copying the answer, so a showing can differ from the answer in any line, and only the comparison on Stop stands between the retyped Case and the person. Proposal: let the showing of a built Case not pass through the agent's retyping, or let the comparison on Stop also refuse a second showing that differs. Briefs: 3.
2. `insight-case-build-promise-lines-compared-by-no-check` — severity 2 — case-guppi writes the promise lines of a Case against the lines beside them (the Criterion it replaces, the then of a sibling sub-case) and no check of its answer compares them, so a dropped or doubled promise is found only by ask-guppi at pre-spec. Proposal: let a check of the answer of case-guppi compare the old lines of a Criterion replaced whole with the new ones, and the then lines of sibling sub-cases with each other, before the Case is shown. Briefs: 1.
3. `insight-case-form-chat-form-read-by-no-script` — severity 1 — A rule of the form of a Case as shown in the chat is read by no script, so it holds only as far as the agent's own reading at the showing, and the fault is found later. Proposal: let a check read the chat form of a Case before the person does, over the order of the sections, the content of `ratification` and a count in a story section. Reopened this run (it stood `actioned` by Case 419.3). Briefs: 1.
4. `insight-hi-skill-substitution-checked-by-a-model-call` — deferred by Case 448: its Pattern and Proposal name a lapsed login and `/login`, while the newest lesson and Case 439 name the server-side classifier of client 2.1.282. Severity 0. Briefs: 1.
5. `rule-orchestration` — deferred by Case 424: the orchestration of the main agent as a rule of its own loaded by `/hi`, and `case-schema.md` read by `case-guppi` alone. Severity: none. Briefs: 5.
6. `rule-ledger-write` — deferred by Case 442: a lesson line whose cause a Case of the same session closed carries `addressed_by`, or the decision line carries `addresses`; nothing catches a missing mark. Severity: none. Briefs: 2.

The item `rule-spec-reconcile` (deferred by Case 423) is retired: 445.1 carries `{supersedes:case 423}`. `rule-work-mode` (deferred by Case 447) and the open Insight `insight-workflow-code-live-before-the-page-it-reads` are named in the Backlog of the sprint page, so they are not listed here.

## Flags

- `incomplete`: `raw/2026-09-26/2300/materialize.yaml` line 23, `estimate-skill-hi-opens-only-in-plan-mode`, lacks `criterion`; the entry carries `superseded_by: 445.7` and was not applied, so no page was written.
- `failed`, `unparsed`, `merged`: none in the yamls of 1337, 1745 and 2300.
- `near`, this run: line 33, `lesson-case-build-one-promise-signed-in-two-sub-cases` near `lesson-case-build-a-criterion-replaced-whole-drops-a-line` (the handoff named it); line 34, `lesson-ledger-a-dropped-item-needs-a-superseding-sub-case` near `lesson-supersedes-in-the-same-session-skips-the-earlier-cases-entries`.
- Synthesis: `lesson-case-build-a-list-in-context` clustered into `insight-case-form-chat-form-read-by-no-script`, which stood `actioned` by Case 419.3; the lesson entry carries no `addressed_by`, so the update sets `status: open`. `lesson-case-build-one-promise-signed-in-two-sub-cases` and `lesson-case-build-a-criterion-replaced-whole-drops-a-line` (session 1745) clustered into the new `insight-case-build-promise-lines-compared-by-no-check`. `lesson-ledger-a-dropped-item-needs-a-superseding-sub-case` has no pair and stays `new`.
- Handoff: the handoff pairs `lesson-case-build-a-list-in-context` with the failed reading of `estimate-case-protocol-case-form`; an Estimate is no lesson, so the pair is not a synthesis. Both stand: the lesson under the reopened Insight, the Estimate `failed`.
- Failed Estimates: 3, listed first under Readings due.
- Contradiction, from lint: `estimates/estimate-claude-md-rendered: method: says by hand while estimate-language-spec-prose-in-english names a test file`.
- Contradiction, standing: the Pattern and Proposal of `insight-hi-skill-substitution-checked-by-a-model-call` against Case 439; Case 448 deferred it.
- Defect, handoff: `materialize.case_text` and `ratified.quoted_sections` are two copies of one section reader, against "one judgment, one implementation"; both judge fences by the same functions.
- Defect: `archive/migration/2026-09-26/1745/raw/spec.md` line 413 is an unticked `read` box of `estimate-prespec-checks-the-ratified-copy`, which Case 445.4 deleted and `cleanup` moved to the archive.
- Defect, this run: before `render`, the PostToolUse hook `uv run guppi ratified --edit` failed on the librarian's own Write ("unrecognized arguments: --edit"), as the handoff foretold; `render` removed it from `.claude/settings.json`.
- `generate` changed 14 pages under `wiki/decisions/` of earlier Cases (git status: 387.3, 396.1, 396.2, 437, 441.1–441.10) with no line in `log.md`; the librarian does not read decision pages, so what changed is not known here.
- The order the handoff asks: `rule-hook-registry` rendered in this run; the `replace` pairs of `rule-case-protocol` (443.3, 444.3, 445.2) and of `rule-spec-write` (444.2, 445.2) applied in one run of `generate`, which printed no stderr line; the rename, the delete and the create of 445.1 and 445.4 applied; 445.5 not applied, `estimate-skill-hi-opens-only-in-plan-mode` not created.
- Handoff note: C14 (the ticks out of the Spec into a work file) was deferred by Case 447 to `rule-work-mode`; the round's seven questions were not answered and the proposal stands in the chat only.
- Handoff note: the first 445.5 created `estimate-skill-hi-opens-only-in-plan-mode`; the person moved the promise of the `/hi` refusal into 445.6 alone, and 445.7 supersedes 445.5 (ledger L31 over L23–L24).
- Handoff note: the rounds of Case 443 were run by prompt in this session, before its render; Cases 445 and 447 each went through two or three rounds.
- Handoff note: context passed 400 000 tokens during the re-ratification; Work Mode was delegated to one subagent.
- MOC candidates: none named by lint.
- Stale defers, from lint: `rule-work-mode` deferred 32 times since case 29; `rule-subagent-guppi` 31 times since case 29; `rule-morph` once since case 239; `rule-orchestration` once since case 424.
- Backlog moves by `generate`: none printed. Milestones dropped: none printed.
- `generate`, `cleanup`, `render`, `sprint`, `glossary`: no stderr lines. `cleanup` moved 3 pages to `archive/migration/2026-09-27/2300/`: `decision-case-423`, `decision-case-445.5`, `estimate-prespec-checks-the-ratified-copy`.
- `archive` (run after the brief): no stderr line. It moved `raw/2026-09-26/1337` and `raw/2026-09-26/1745` to `archive/migration/2026-09-26/<HHMM>/raw`; the line numbers of their Specs above point there. It kept `raw/2026-09-26/2300/`, the session of the run.
- `make lint`, after the render: exit 2, 105 findings.
  - `decisions/decision-case-N: schema: missing section ## Context` and `## Problem` on 31 pages. That is 62 findings.
  - `rules/rule-spec-box: schema: missing field kind`, `missing field estimates`, and `orphan: no other live page names it in its frontmatter`.
  - `rules/rule-morph: deferred: 1 time since case 239`; `rules/rule-orchestration: deferred: 1 time since case 424`; `rules/rule-subagent-guppi: deferred: 31 times since case 29`; `rules/rule-work-mode: deferred: 32 times since case 29`.
  - `estimates/estimate-claude-md-rendered: method: says by hand while estimate-language-spec-prose-in-english names a test file`.
  - `unread: pending` on 31 Estimates and `unread: failed` on 3. These are the 34 Estimates of Readings due.
  - `estimates: unmigrated: 19 pages in the shape before case 193`.

## Next session

Cases:
- `estimate-case-protocol-case-form` failed: a count and unrelated case numbers in `context`, an unrelated case in `problem` (reading of session 2300).
- `estimate-agent-writing-followed` failed: a reply that misstated the ledger tail, a closer given to the wrong item (reading of session 2300).
- `estimate-case-protocol-defers-in-one-reply` failed: the plan edited after a short-form defer (reading of session 1745).
- Contradiction from lint: the method of `estimate-claude-md-rendered` says by hand while `estimate-language-spec-prose-in-english` names a test file.
- Defect from the handoff: `materialize.case_text` and `ratified.quoted_sections` are two copies of one section reader.
- Defect found in this run: `archive/migration/2026-09-26/1745/raw/spec.md` line 413 holds an unticked `read` box of the deleted `estimate-prespec-checks-the-ratified-copy`.

Work:
- `estimate-skill-grill-me-asks-in-rounds`
- `estimate-case-build-writes-the-case`
- `estimate-case-protocol-shows-the-built-case`
- `estimate-materialize-judges-a-fence`
- `estimate-spec-write-copies-the-ratified-case`
- `estimate-spec-reconcile-refuses-an-edit-of-the-plan`
- `estimate-spec-write-checks-the-written-case`
- `estimate-spec-write-removes-a-superseded-case`
- `estimate-language-spec-prose-in-english`
- `estimate-event-log-records`
- `estimate-language-followed` (W32)
- `estimate-materialize-lifts-a-create-by-the-schema`
- `estimate-materialize-assembles`
- `estimate-case-check-shows-only-the-checked-case`
- `estimate-prespec-reconciles`
- `estimate-spec-write-reaches-the-approved-spec`
- `estimate-spec-capture-appends`
- `estimate-case-check-sends-back-a-faulty-case`
- `estimate-case-protocol-ledger-line-form`
- `estimate-context-size-warns-past-the-limit`
- `estimate-retro-loads`
- `estimate-retro-report-holds-each-fact-once`
- `estimate-carry-over-writes`
- `estimate-documentation-completes`
- `estimate-session-phases-in-order`
- `estimate-sprint-renders-the-backlog`
- `estimate-synthesis-keeps-actioned-by-the-mark`
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-merges`
- `estimate-sprint-migration-rule-class-files-dissolved`
- The unticked boxes of the Specs are the `read` lines of the readings above: `raw/2026-09-26/2300/spec.md` lines 99, 161, 209, 269, 328, 436, 507, 541, 596, 651, 732; `archive/migration/2026-09-26/1745/raw/spec.md` lines 96, 132, 240, 287, 335, 381, 479, 537, 590, 626, 659; `archive/migration/2026-09-26/1337/raw/spec.md` lines 107, 163, 232, 368, 436.
- Frontier Work lines W1–W29 (handoff: the brief's readings, the `read` boxes of 1745 and 1337, the check of Case 440, the Work lines of 1745).
- Ledger lines not applied: L23 and L24 of `raw/2026-09-26/2300/ledger.md` (445.5), superseded by 445.7. All 36 lines have an entry.

## Readings at the close

- `make test`: 734 passed, 2 skipped.
- `make lint`: exit 2, 105 findings (listed under Flags).
- Pages in `vault/wiki/`: decisions 633, estimates 138, rules 67, lessons 60, insights 25, entities 4.
