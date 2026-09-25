# Brief — 2026-09-25, the librarian's run over session 1654

## Where things stand

- Session 1654 ratified Cases 425, 426, 427, 428 (428.1–428.4), 429, 430, 431 and 432. Frontier: C3–C9, C12 and C13 were closed by Cases; C1 and C2 stay for the sprint; C10 and C11 are deferred and kept.
- Code, commit 6ffb2c9: `guppi/prespec.py` (426, 429, 432), `guppi/materialize.py` (429, 427), `guppi/ledger.py` (the refusal of 428.1), `guppi/context.py` (430); tests in `test_prespec.py`, `test_materialize.py`, `test_casecheck.py`, `test_ledger.py`, `test_context.py`. The session's `make test` gave 680 passed, 2 skipped; `make style` was clean.
- Migrations of the session: the yaml of 1228 line 40 (427); two read lines of `raw/2026-09-25/1228/spec.md` rewritten to the new slugs (432); `git rm .claude/agents/frame-guppi.md` (W25).
- Readings of the session: failed — `estimate-case-protocol-shows-the-built-case`; passed — `estimate-case-check-shows-only-the-checked-case`, `estimate-page-read-cuts-the-history`, `estimate-harness-pipeline`, `estimate-spec-write-copies-the-ratified-case`, `estimate-spec-write-checks-the-written-case`, `estimate-prespec-checks-the-frontier`, `estimate-hi-writes-frontier`.
- Not done in the session: the `read` lines of the Estimates this session changed (a later session, case 428.1); Work readings W2, W3, W9, W10, W13–W24 and W28 (handoff).
- The walk named `raw/2026-09-25/0051/` (0 new entries), `raw/2026-09-25/1228/` (0 new entries) and `raw/2026-09-25/1654/`.
- Yaml of 1654: 32 entries from the 32 lines of the ledger: 22 `update`, 1 `create`, 1 `lesson`, 8 `estimate` readings. All 32 are `applied`. The librarian added no entries. 11 Decisions applied.
- `{supersedes:case 404}`, `409`, `418` and `422` of Case 430 (ledger line 16, read as a list of four) marked one entry and one decision in each yaml of 0051 and 1228 `superseded_by: 430`.
- Pages, from the tree after cleanup against commit 6ffb2c9:
  - decisions: 11 written (425, 426, 427, 428.1–428.4, 429, 430, 431, 432). 404, 409, 418 and 422 moved to the archive. 391.1, 391.2 and 419.2 changed.
  - estimates: 1 created, `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session`. 18 updated.
  - rules: `rule-frame-check` renamed to `rule-case-build` (425). 10 updated: `rule-case-protocol`, `rule-context-size`, `rule-harness`, `rule-ledger-write`, `rule-materialize`, `rule-page-read`, `rule-plan-mode`, `rule-prespec`, `rule-retro`, `rule-skill-hi`.
  - lessons: 1 created, `lesson-case-show-sub-case-ratification-retyped`, `new`. 4 moved to the archive by the cascade: `lesson-retro-reading-of-a-replaced-criterion`, `lesson-retro-reading-of-a-criterion-this-spec-replaces`, `lesson-prespec-read-line-of-a-renamed-estimate`, `lesson-prespec-wikilink-to-a-decision-page-not-yet-written`.
  - insights: 2 updated. `insight-retro-reading-taken-on-a-criterion-the-session-replaces` is `actioned` by `decision-case-428.1`. `insight-workflow-case-schema-silent-on-what-the-scripts-accept` is `actioned` by `decision-case-432`.
  - entities: 1 updated, `entity-glossary`.
- Governed files differ from commit 6ffb2c9: `.claude/skills/pre-spec/SKILL.md`, `.claude/skills/retro/SKILL.md`, `vault/wiki/case-schema.md`, `vault/wiki/glossary.md`. `guppi sprint` changed nothing.

## Readings due

1 Estimate stands `failed` and 25 stand `pending`:

- `estimate-case-protocol-shows-the-built-case` — `failed` — `rule-case-protocol` draft — by hand, the Cases of a session at its close, their context against the Agent calls of the event log (method). Result: the first showing of sub-case 428.3 carried the ledger line of 428.2 under its ratification, retyped by the agent; the `Stop` comparison of casecheck refused it, and 428.3 was shown again unchanged.
- `estimate-prespec-matches-lines-and-items` — `rule-prespec` draft — `raw/2026-09-25/1654/spec.md` line 99.
- `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` — `rule-ledger-write` draft — `raw/2026-09-25/1654/spec.md` line 240.
- `estimate-ledger-write-lifts` — `rule-ledger-write` draft — `raw/2026-09-25/1654/spec.md` line 274.
- `estimate-retro-loads` — `rule-retro` draft — `raw/2026-09-25/1654/spec.md` line 313.
- `estimate-retro-report-holds-each-fact-once` — `rule-retro` draft — `raw/2026-09-25/1654/spec.md` line 354.
- `estimate-materialize-marks-superseded` — `rule-materialize` draft — `raw/2026-09-25/1654/spec.md` line 439, in the next session (case 428.1).
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` draft — `raw/2026-09-25/1654/spec.md` line 440, in the next session (case 428.1).
- `estimate-context-size-warns-past-the-limit` — `rule-context-size` draft — `raw/2026-09-25/1654/spec.md` line 492.
- `estimate-case-protocol-case-form` — `rule-case-protocol` draft — `raw/2026-09-25/1654/spec.md` line 535.
- `estimate-prespec-requires-a-task-line` — `rule-prespec` draft — `raw/2026-09-25/1654/spec.md` line 596.
- `estimate-case-build-writes-the-case` — `rule-case-build` draft — `raw/2026-09-25/1228/spec.md` line 155.
- `estimate-case-check-sends-back-a-faulty-case` — `rule-case-check` draft — `raw/2026-09-25/1228/spec.md` line 240.
- `estimate-spec-write-writes-a-defer` — `rule-spec-write` draft — `raw/2026-09-25/1228/spec.md` line 513.
- `estimate-case-protocol-defers-in-one-reply` — `rule-case-protocol` draft — `raw/2026-09-25/1228/spec.md` line 553.
- `estimate-agent-writing-followed` — `rule-agent-writing` draft — by hand, the section in `CLAUDE.md` and one reply of the agent against it (method).
- `estimate-carry-over-writes` — `rule-carry-over` draft — pytest over the skill's render, plus one live reading of a carried-over session (method).
- `estimate-documentation-completes` — `rule-documentation` draft — `make test-documentation`, then the live reading by hand (method).
- `estimate-language-followed` — `rule-language` draft — by hand, the section in `CLAUDE.md`, the session's commit, Spec and chat against it (method).
- `estimate-session-phases-in-order` — `rule-session` draft — by hand at the close of a session, the day's records in order (method).
- `estimate-sprint-renders-the-backlog` — `rule-sprint` draft — `pytest tests/test_sprint.py`, plus one reading of the rendered `sprint.md` after the librarian's run (method).
- `estimate-synthesis-keeps-actioned-by-the-mark` — `rule-synthesis` draft — by hand, the yaml and the brief after the first marked lesson is clustered under an actioned Insight (method).
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` draft — by hand, the tree at the close of the sprint (method).
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` draft — `make lint` exit 0, or only unread lines on the Estimates of the sprint (method).
- `estimate-sprint-migration-merges` — `entity-sprint-migration` draft — `make test` on the last commit of migration, then `git log` of main after the merge (method).
- `estimate-sprint-migration-rule-class-files-dissolved` — `entity-sprint-migration` draft — by hand, the listed `ls`, `grep`, `render --check` and `glossary --check` (method).

## Deferred

1. `rule-spec-reconcile` — deferred by Case 423: a guard that refuses the agent's edits of the plan while a Cases line of the Frontier is open; when and how the prose of a Case is translated (the question of case 410). Severity: none. Briefs: 4.
2. `rule-orchestration` — deferred by Case 424: the orchestration of the main agent as a rule of its own loaded by `/hi`, and `case-schema.md` read by `case-guppi` alone. Severity: none. Briefs: 2.

The yaml of 1654 holds no `defer` entry. `{supersedes:case 404}`, `409`, `418` and `422` of Case 430 retired the previous brief's item `rule-context-size`. `insight-workflow-case-schema-silent-on-what-the-scripts-accept` (`decision-case-432`) and `insight-retro-reading-taken-on-a-criterion-the-session-replaces` (`decision-case-428.1`) are `actioned`, so they are not listed. The one open Insight, `insight-workflow-code-live-before-the-page-it-reads`, is named by the sprint page, so it is not listed here.

## Flags

- `incomplete`, `failed`, `unparsed`: none in the yamls of 0051, 1228 and 1654.
- `near`, from earlier runs: `raw/2026-09-25/0051/materialize.yaml` line 17, `lesson-hooks-subagentstop-exit-2-sends-the-subagent-back` near `lesson-hooks-windows-stdin-encoding`; `raw/2026-09-25/1228/materialize.yaml` line 8, `rule-case-check` near `rule-spec-write`. This run added no `near`.
- Failed Estimate: `estimate-case-protocol-shows-the-built-case`. The result is under Readings due.
- Synthesis: `lesson-case-show-sub-case-ratification-retyped` has no pair and stays `new`. The actioned updates of lines 8 (428.1) and 21 (432) sent the four lessons of their Insights to the archive by the cascade.
- The by-hand check of Case 425 (`raw/2026-09-25/1654/spec.md` line 46): a Grep of `rule-frame-check` over `vault/wiki/` finds it in History lines (`rule-case-build`, `rule-plan-mode`, `estimate-case-build-writes-the-case`), `brief.md` and `log.md`, and also in the body of `decisions/decision-case-426.md` line 14, where the Context of Case 426 names the lost `update` of `rule-frame-check`.
- The by-hand check of Case 427 (`raw/2026-09-25/1654/spec.md` line 149): `generate` printed no line for `estimate-frame-check-finds-a-contradiction`; `render` ticked the render lines of `raw/2026-09-25/1228/spec.md`, and no unticked render line is left there.
- `raw/2026-09-25/1228/spec.md` line 151, `- [ ] update rule-frame-check`, stays unticked. The page was renamed to `rule-case-build` by Case 425 in this run.
- Contradiction: the Trigger of `lesson-case-show-sub-case-ratification-retyped` (ledger line 12) names "the SubagentStop comparison of casecheck". The handoff and the result of `estimate-case-protocol-shows-the-built-case` name the comparison on `Stop`. The handoff says the line stands as written.
- Handoff note, point 12 of pre-spec: a `read` line of an Estimate this session changes is ticked by a later reading only while its unit lies in `raw/`. The debt is carried by the Estimate's `pending` and by lint's `unread`. The same holds for the two read lines of 1228 that Case 432 rewrote.
- MOC candidates: none.
- Stale defers, from lint: `rule-subagent-guppi` and `rule-work-mode` have been deferred 31 times since case 29. `rule-morph` has been deferred once since case 239, and `rule-orchestration` once since case 424.
- Backlog moves by `generate`: none printed. Milestones dropped: none printed.
- `generate`, `cleanup`, `render`, `sprint`, `glossary`: no stderr lines.
- `make lint`, after the render: exit 2, 96 findings.
  - `decisions/decision-case-N: schema: missing section ## Context` and `## Problem` on 31 pages. That is 62 findings.
  - `rules/rule-spec-box: schema: missing field kind`, `missing field estimates`, and `orphan: no other live page names it in its frontmatter`.
  - `rules/rule-morph: deferred: 1 time since case 239`; `rules/rule-orchestration: deferred: 1 time since case 424`; `rules/rule-subagent-guppi: deferred: 31 times since case 29`; `rules/rule-work-mode: deferred: 31 times since case 29`.
  - `unread: pending` on 25 Estimates and `unread: failed` on 1. These are the 26 Estimates of Readings due.
  - `estimates: unmigrated: 20 pages in the shape before case 193`.

## Next session

Cases:
- Failed Estimate `estimate-case-protocol-shows-the-built-case`: the first showing of 428.3 carried the ledger line of 428.2, retyped by the agent (`raw/2026-09-25/1654/ledger.md#L25`).
- Contradiction: the Trigger of `lesson-case-show-sub-case-ratification-retyped` names the `SubagentStop` comparison, and the handoff names the `Stop` comparison (Flags; handoff).
- `raw/2026-09-25/1228/spec.md` line 151 (`update rule-frame-check`) is unticked, and the page now has the slug `rule-case-build` (Flags).
- The by-hand check of Case 425 expects `rule-frame-check` only in History lines, `brief.md` and `log.md`, and `decision-case-426` line 14 also holds it (Flags; `raw/2026-09-25/1654/spec.md` line 46).

Work:
- `estimate-prespec-matches-lines-and-items`
- `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session`
- `estimate-ledger-write-lifts`
- `estimate-retro-loads`
- `estimate-retro-report-holds-each-fact-once`
- `estimate-materialize-marks-superseded`
- `estimate-case-protocol-ledger-line-form`
- `estimate-context-size-warns-past-the-limit`
- `estimate-case-protocol-case-form`
- `estimate-prespec-requires-a-task-line`
- `estimate-case-build-writes-the-case`
- `estimate-case-check-sends-back-a-faulty-case`
- `estimate-spec-write-writes-a-defer`
- `estimate-case-protocol-defers-in-one-reply`
- `estimate-agent-writing-followed`
- `estimate-carry-over-writes`
- `estimate-documentation-completes`
- `estimate-language-followed`
- `estimate-session-phases-in-order`
- `estimate-sprint-renders-the-backlog`
- `estimate-synthesis-keeps-actioned-by-the-mark`
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-merges`
- `estimate-sprint-migration-rule-class-files-dissolved`
- Unticked by-hand box of `raw/2026-09-25/1654/spec.md` line 149 (the check of Case 427; its result is under Flags).
- Frontier Work lines W2, W3, W9, W10, W13–W24 and W28 (handoff).
- Ledger lines not applied: none. All 32 lines of `raw/2026-09-25/1654/ledger.md` have an entry, and all are `applied`.

## Readings at the close

- `make test`: 680 passed, 2 skipped.
- `make lint`: exit 2, 96 findings (listed under Flags).
- Pages in `vault/wiki/`: decisions 596, estimates 134, rules 66, lessons 53, insights 23, entities 4.
