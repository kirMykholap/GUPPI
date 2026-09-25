# Brief — 2026-09-25, the librarian's run over session 1228

## Where things stand

- Session 1228 ratified Case 419 (419.1–419.4), Case 420 (420.1, 420.2) and Case 421 (421.1–421.4), and deferred 422, 423 and 424. Frontier: C3 and C4 were closed by 419; C5, C6 and C11 by sub-cases of 419; C8 by 421; C12 by 420; C1 and C2 stay for the sprint; C7, C9 and C10 were deferred.
- Work Mode, commit 9aae9f8: `guppi/casecheck.py` (the `SubagentStop` check and the `Stop` comparison), `guppi/pageread.py` (the two `Read` hooks), `guppi/pages.py` (`section_starts`, `history_line`, `HISTORY`, shared with `generate` and `lint`), `guppi/ratified.py` (`case_section`, shared with casecheck; the write of a defer-only Case), `guppi/prespec.py` (`kept`), `guppi/cli.py`; tests `test_casecheck.py`, `test_pageread.py`, and new tests in `test_ratified.py` and `test_prespec.py`. The session's `make test` gave 663 passed, 2 skipped; `make style` was clean.
- Readings of the session: passed — `estimate-case-protocol-acknowledging-reply`, `estimate-case-protocol-ledger-line-form`, `estimate-hook-registry-rendered`, `estimate-prespec-reconciles`, `estimate-one-judgment-one-implementation-followed`; failed — `estimate-context-size-warns-past-the-limit`. The line of `estimate-frame-check-finds-a-contradiction` (ledger line 40) was not applied, by the handoff's instruction.
- Not done in the session: every `read` line of the Spec (the pages exist only after `generate`, and `case-guppi` and the new hooks load only in the next session); `git rm .claude/agents/frame-guppi.md`; Frontier Work lines W1, W3, W4, W8, W11–W14, W16–W23.
- The walk named `raw/2026-09-25/0051/` (0 new entries) and `raw/2026-09-25/1228/`.
- Yaml of 1228: 53 entries. 45 come from the 45 lines of the ledger: 24 `update`, 6 `create`, 3 `defer`, 5 `lesson`, 7 `estimate` readings. 8 were added by the librarian's synthesis: 1 `create` of an Insight, 2 `update` of Insights, 5 `update` of lessons. 52 are `applied`; line 40 is `failed`. 13 Decisions applied.
- Yaml of 0051: `{supersedes:case 416}` of 419.2 marked lines 6–10 and the decision of 416 `superseded_by: 419.2`. These entries had been applied on 2026-09-25 by the earlier run.
- Pages, from the tree after cleanup against commit 9aae9f8:
  - decisions: 13 written (419.1–419.4, 420.1, 420.2, 421.1–421.4, 422, 423, 424). 403 and 416 moved to the archive. 391.1, 391.2, 396.1 and 396.2 changed.
  - estimates: 4 created — `estimate-case-check-sends-back-a-faulty-case`, `estimate-case-check-shows-only-the-checked-case`, `estimate-page-read-cuts-the-history`, `estimate-spec-write-writes-a-defer`. 2 renamed — `estimate-case-protocol-checks-its-frame` to `estimate-case-protocol-shows-the-built-case`, `estimate-frame-check-finds-a-contradiction` to `estimate-case-build-writes-the-case`. 12 more updated.
  - rules: 3 created — `rule-case-check`, `rule-page-read`, and `rule-orchestration` (the placeholder of defer 424). 12 updated: `rule-ask`, `rule-case-protocol`, `rule-context-size`, `rule-frame-check`, `rule-harness`, `rule-hook-registry`, `rule-one-judgment-one-implementation`, `rule-plan-mode`, `rule-prespec`, `rule-skill-hi`, `rule-spec-reconcile`, `rule-spec-write`.
  - lessons: 5 created. `lesson-case-form-given-written-before-tasks` and the three lessons of `insight-case-form-chat-form-read-by-no-script` went to the archive by the cascade. 3 lessons are now `clustered`, 1 of them updated from an older page.
  - insights: 1 created, `insight-retro-reading-taken-on-a-criterion-the-session-replaces`, `open`, severity 2. 2 updated: `insight-case-form-chat-form-read-by-no-script` is `actioned` by `decision-case-419.3`; `insight-workflow-case-schema-silent-on-what-the-scripts-accept` is `open` again, with 2 new children.
  - entities: none.
- Governed files differ from commit 9aae9f8: `vault/wiki/case-schema.md`, `.claude/agents/ask-guppi.md`, `.claude/agents/case-guppi.md` (new), `.claude/skills/hi/SKILL.md`, `.claude/skills/pre-spec/SKILL.md`, `.claude/settings.json`. `guppi sprint` and `guppi glossary` changed nothing.

## Readings due

2 Estimates stand `failed` and 24 stand `pending`:

- `estimate-context-size-warns-past-the-limit` — `failed` — `rule-context-size` draft — `uv run pytest tests/test_context.py -k limit`, then by hand at the first prompt past 400 000 tokens (method). Result: the pytest gave 3 passed; at 456 635 tokens the hook printed the order to recommend /retro then /handoff, and the agent called /retro at once without opening its reply with the recommendation.
- `estimate-case-protocol-case-form` — `failed` — `rule-case-protocol` draft — by hand, the Cases of a session at its close (method). Result: Case 414 showed a count of items in its `context` and Case 415 a bookkeeping `－` line in `then`; both were found by ask-guppi at pre-spec and fixed.
- `estimate-case-protocol-shows-the-built-case` — `rule-case-protocol` draft — `raw/2026-09-25/1228/spec.md` line 82 (the read line of the old slug `estimate-case-protocol-checks-its-frame`).
- `estimate-case-build-writes-the-case` — `rule-frame-check` draft — `raw/2026-09-25/1228/spec.md` line 155 (the read line of the old slug `estimate-frame-check-finds-a-contradiction`).
- `estimate-case-check-sends-back-a-faulty-case` — `rule-case-check` draft — `raw/2026-09-25/1228/spec.md` line 240.
- `estimate-case-check-shows-only-the-checked-case` — `rule-case-check` draft — `raw/2026-09-25/1228/spec.md` line 299.
- `estimate-page-read-cuts-the-history` — `rule-page-read` draft — `raw/2026-09-25/1228/spec.md` line 382.
- `estimate-harness-pipeline` — `rule-harness` draft — `raw/2026-09-25/1228/spec.md` line 417.
- `estimate-spec-write-copies-the-ratified-case` — `rule-spec-write` draft — `raw/2026-09-25/1228/spec.md` line 511.
- `estimate-spec-write-checks-the-written-case` — `rule-spec-write` draft — `raw/2026-09-25/1228/spec.md` line 512 and `raw/2026-09-25/0051/spec.md` line 79.
- `estimate-spec-write-writes-a-defer` — `rule-spec-write` draft — `raw/2026-09-25/1228/spec.md` line 513.
- `estimate-case-protocol-defers-in-one-reply` — `rule-case-protocol` draft — `raw/2026-09-25/1228/spec.md` line 553.
- `estimate-prespec-checks-the-frontier` — `rule-prespec` draft — `raw/2026-09-25/1228/spec.md` line 595.
- `estimate-hi-writes-frontier` — `rule-skill-hi` draft — `raw/2026-09-25/1228/spec.md` line 649.
- `estimate-agent-writing-followed` — `rule-agent-writing` draft — by hand, the section in `CLAUDE.md` and one reply of the agent against it (method).
- `estimate-carry-over-writes` — `rule-carry-over` draft — pytest over the skill's render, plus one live reading of a carried-over session (method).
- `estimate-documentation-completes` — `rule-documentation` draft — `make test-documentation`, then the live reading by hand (method).
- `estimate-language-followed` — `rule-language` draft — by hand, the section in `CLAUDE.md`, the session's commit, Spec and chat against it (method).
- `estimate-retro-report-holds-each-fact-once` — `rule-retro` draft — by hand, the first `/retro` after the render (method).
- `estimate-session-phases-in-order` — `rule-session` draft — by hand at the close of a session, the day's records in order (method).
- `estimate-sprint-renders-the-backlog` — `rule-sprint` draft — `pytest tests/test_sprint.py`, plus one reading of the rendered `sprint.md` after the librarian's run (method).
- `estimate-synthesis-keeps-actioned-by-the-mark` — `rule-synthesis` draft — by hand, the yaml and the brief after the first marked lesson is clustered under an actioned Insight (method).
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` draft — by hand, the tree at the close of the sprint (method).
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` draft — `make lint` exit 0, or only unread lines on the Estimates of the sprint (method).
- `estimate-sprint-migration-merges` — `entity-sprint-migration` draft — `make test` on the last commit of migration, then `git log` of main after the merge (method).
- `estimate-sprint-migration-rule-class-files-dissolved` — `entity-sprint-migration` draft — by hand, the listed `ls`, `grep`, `render --check` and `glossary --check` (method).

## Deferred

1. `insight-workflow-case-schema-silent-on-what-the-scripts-accept` — severity 2, `open` again. Pattern: the Case schema does not say how the scripts read the text a Case writes, so the agent writes a form the scripts do not handle and only the pre-spec check finds it. Proposal: the Case schema of `rule-case-protocol` states, beside each form a Case writes, the limit the scripts put on it. Briefs: 1.
2. `insight-retro-reading-taken-on-a-criterion-the-session-replaces` — severity 2. Pattern: the Retro writes the readings a list asks for without holding each slug against the Cases of the same session, so an Estimate whose Criterion a Case of that Spec replaces gets a reading. Proposal: a check at the Retro or at the ledger write holds each `estimate[...]` line against the `then` blocks of the session's Spec and refuses such a reading. Briefs: 1.
3. `rule-context-size` — deferred by Cases 404, 409, 418 and 422: the limit of 400 000 tokens in `guppi/context.py` and the text of the `UserPromptSubmit` hook past it, judged once a session reaches it. Severity: none. Briefs: 4.
4. `rule-spec-reconcile` — deferred by Case 423: a guard that refuses the agent's edits of the plan while a Cases line of the Frontier is open; when and how the prose of a Case is translated (the question of case 410). Severity: none. Briefs: 3 (2 of them under Case 416).
5. `rule-orchestration` — deferred by Case 424: the orchestration of the main agent as a rule of its own loaded by `/hi`, and `case-schema.md` read by `case-guppi` alone. Severity: none. Briefs: 1.

`{supersedes:case 416}` and `{supersedes:case 403}` of 419.2 retired the previous brief's items `rule-frame-check`, `rule-case-protocol`, `rule-spec-write` and `rule-ask`. `insight-case-form-chat-form-read-by-no-script` is `actioned` by `decision-case-419.3`, so it is not listed. The open Insight `insight-workflow-code-live-before-the-page-it-reads` is named by the sprint page, so it is not listed here.

## Flags

- `failed`: `raw/2026-09-25/1228/materialize.yaml` line 40, `estimate-frame-check-finds-a-contradiction` — `generate: estimate-frame-check-finds-a-contradiction: no estimate page to fill`. Line 7 (Case 419.2) renamed the page to `estimate-case-build-writes-the-case`. The handoff asked that this line not be applied. While the entry carries `failed`, the yaml of 1228 is not applied whole: `render` ticks none of its render boxes and `archive` keeps the unit.
- The rename of `rule-frame-check` to `rule-case-build` is not on disk. The handoff says Case 419.2 holds two `update` items of `rule-frame-check`, the sections then the `rename`, in one ledger line. The yaml holds one entry for it (line 6), with the sections and no `rename`. `raw/2026-09-25/1228/spec.md` line 151 (`update rule-frame-check`) stays unticked. `rule-frame-check` governs `.claude/agents/case-guppi.md` with the markers `<!-- rule-frame-check -->`. `rule-case-protocol`, `rule-skill-hi`, `vault/wiki/case-schema.md` and `.claude/skills/hi/SKILL.md` name `rule-case-build` in a code span, and no page has that slug. Lint does not report it.
- `near`: `rule-case-check` (line 8) is near `rule-spec-write`. One checks a Case before it is shown, the other checks it as written into the Spec.
- `incomplete`, `unparsed`: none in the yamls of 0051 and 1228.
- Failed Estimates: `estimate-context-size-warns-past-the-limit` and `estimate-case-protocol-case-form`. Their results are under Readings due.
- Synthesis: `insight-retro-reading-taken-on-a-criterion-the-session-replaces` was created `open` with children `lesson-retro-reading-of-a-replaced-criterion` and `lesson-retro-reading-of-a-criterion-this-spec-replaces`, both now `clustered`. `lesson-prespec-read-line-of-a-renamed-estimate` and `lesson-prespec-wikilink-to-a-decision-page-not-yet-written` were clustered under `insight-workflow-case-schema-silent-on-what-the-scripts-accept`, which went from `actioned` to `open`. `lesson-case-form-given-written-before-tasks` carries `addressed_by: decision-case-419.3` and was clustered under `insight-case-form-chat-form-read-by-no-script`. Line 11 (Case 419.3) set that Insight `actioned` with `addressed_by: decision-case-419.3`, and its four lessons went to the archive by the cascade. `lesson-hooks-pretooluse-updatedinput-limits-a-read` has no pair and stays `new`.
- The marks of this run were already on the yaml of 1228 when the run started: `applied` at 15:42:11 on 52 entries and 13 decisions, `failed` on line 40, and the librarian's `near` and `synthesis` marks. The pages and governed files were already in the tree, and this run's `generate` wrote 0 pages. `brief.md` had not been rewritten, and no librarian commit existed.
- `.claude/agents/frame-guppi.md` is still in the tree. No page governs it now. The handoff leaves its `git rm` to the next session.
- The handoff records that `claude-code-guide`, answering from the docs, said `SubagentStop` cannot block and has no `stop_hook_active`. The live payloads of the 0051 probe show both. The code follows the probe.
- MOC candidates: none.
- Stale defers, from lint: `rule-subagent-guppi` and `rule-work-mode` have been deferred 31 times since case 29. `rule-morph` has been deferred once since case 239, and `rule-orchestration` once since case 424.
- Backlog moves by `generate`: none printed. Milestones dropped: none printed.
- `generate` stderr: the line of line 40 above. `cleanup`, `render`, `sprint`, `glossary`: no stderr lines.
- `make lint`, after the render: exit 2, 96 findings.
  - `decisions/decision-case-N: schema: missing section ## Context` and `## Problem` on 31 pages. That is 62 findings.
  - `rules/rule-spec-box: schema: missing field kind`, `missing field estimates`, and `orphan: no other live page names it in its frontmatter`.
  - `rules/rule-morph: deferred: 1 time since case 239`; `rules/rule-orchestration: deferred: 1 time since case 424`; `rules/rule-subagent-guppi: deferred: 31 times since case 29`; `rules/rule-work-mode: deferred: 31 times since case 29`.
  - `unread: pending` on 24 Estimates and `unread: failed` on 2. These are the 26 Estimates of Readings due.
  - `estimates: unmigrated: 20 pages in the shape before case 193`.

## Next session

Cases:
- The rename of `rule-frame-check` to `rule-case-build` from Case 419.2 was not applied. Four texts name `rule-case-build`, a page that does not exist (Flags; handoff; `raw/2026-09-25/1228/spec.md` line 151).
- `raw/2026-09-25/1228/materialize.yaml` line 40 carries `failed` by the handoff's instruction. The unit cannot be applied whole: its render boxes stay unticked and `archive` keeps it (Flags).
- Failed Estimate `estimate-context-size-warns-past-the-limit`: past 400 000 tokens, the agent did not open its reply with the recommendation (`raw/2026-09-25/1228/ledger.md#L45`).
- Failed Estimate `estimate-case-protocol-case-form`: Case 414 showed a count of items and Case 415 a bookkeeping `－` line at the showing (`raw/2026-09-25/0051/ledger.md#L19`).

Work:
- `estimate-case-protocol-shows-the-built-case`
- `estimate-case-build-writes-the-case`
- `estimate-case-check-sends-back-a-faulty-case`
- `estimate-case-check-shows-only-the-checked-case`
- `estimate-page-read-cuts-the-history`
- `estimate-harness-pipeline`
- `estimate-spec-write-copies-the-ratified-case`
- `estimate-spec-write-checks-the-written-case`
- `estimate-spec-write-writes-a-defer`
- `estimate-case-protocol-defers-in-one-reply`
- `estimate-prespec-checks-the-frontier`
- `estimate-hi-writes-frontier`
- `estimate-agent-writing-followed`
- `estimate-carry-over-writes`
- `estimate-documentation-completes`
- `estimate-language-followed`
- `estimate-retro-report-holds-each-fact-once`
- `estimate-session-phases-in-order`
- `estimate-sprint-renders-the-backlog`
- `estimate-synthesis-keeps-actioned-by-the-mark`
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-merges`
- `estimate-sprint-migration-rule-class-files-dissolved`
- `git rm .claude/agents/frame-guppi.md` (`raw/2026-09-25/1228/spec.md` line 154).
- Unticked render boxes of `raw/2026-09-25/1228/spec.md`, lines 79–81, 153, 239, 298, 381, 552, 594, 647 and 648. The files differ from 9aae9f8, but `render` does not tick them while line 40 is `failed`.
- Ledger line not applied: `raw/2026-09-25/1228/ledger.md` line 40, by the handoff's instruction. The other 44 of its 45 lines were applied.
- Frontier Work lines W1, W3, W4, W8, W11–W14, W16–W23 (handoff).

## Readings at the close

- `make test`: 663 passed, 2 skipped.
- `make lint`: exit 2, 96 findings (listed under Flags).
- Pages in `vault/wiki/`: decisions 589, estimates 133, rules 66, lessons 56, insights 23, entities 4.
