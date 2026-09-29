# Brief

## Where things stand

Session 1134 of 2026-09-29, sprint `migration`. Ratified: 506, 508, 509 (507 superseded by 508.2 in the same session). Commits 35bb520 (code of 506) and ab14bec (the session folder); `guppi/lint.py`, `guppi/generate.py`, `tests/test_lint.py`, `tests/test_generate.py`, `tests/test_schemas.py` changed; readings L23–L66 and L71–L74 taken. Slice 3g is closed: `vault/wiki/sprint.md` now opens its milestones at Slice 4 (case 506.7).

Not done, from the handoff: the failed readings of `estimate-case-build-writes-a-plain-round` and `estimate-documentation-completes`; the `method` of `estimate-materialize-lifts-unfiltered-on-a-schema-change` selects no test with `-k schema_change`; three readings not taken (`estimate-glossary-terms-defined`, `estimate-glossary-ticks-the-spec`, `estimate-sprint-migration-index-dissolved`); the readings whose moment comes after Retro; lessons L69 and L70.

The run over `vault/raw/2026-09-29/1134/materialize.yaml`: 74 entries from 74 ledger lines, plus 2 of the synthesis; 72 applied, 1 failed, 2 superseded, 1 `exists` (the defer of `rule-retro`, applied). The 0137 yaml was extended with 0 entries.

- Created: estimates 3 (`estimate-hi-takes-its-readings`, `estimate-work-mode-takes-the-work-readings`, `estimate-brief-carries-the-run-facts`), lessons 2 (`lesson-case-build-signs-one-criterion-twice-in-a-session`, `lesson-retro-report-copies-the-fence-of-its-template`), decisions 12 (506.1–506.7, 508.1–508.4, 509).
- Updated by entry: rules 8 and 1 defer (`rule-retro`), estimates 7 updates and 48 readings, entities 1 (`entity-sprint-migration`), insights 1, lessons 1. Files changed on disk: rules 29, estimates 55, entities 2, insights 1.
- Deleted: estimates 1 (`estimate-lint-counts-the-unmigrated`, case 506.2); `guppi cleanup` moved 2 pages.
- Synthesis: `lesson-case-build-signs-one-criterion-twice-in-a-session` joined `insight-case-build-promise-lines-compared-by-no-check`, which went from `actioned` to `open`; its `addressed_by` `decision-case-472.3` stands. `lesson-retro-report-copies-the-fence-of-its-template` stays `new`.

## Readings due

Failed first:

- `estimate-case-build-writes-a-plain-round` — `rule-case-build` — failed: the first round on C1 names "case 193" in its Context, and the round on C4 names "Cases 506 and 507" in the Now line of Q3, outside the ➡️ lines. Read by hand, in a session after the render: one round of case-guppi read in the chat against the four parts of the Criterion.
- `estimate-case-protocol-defers-in-one-reply` — `rule-case-protocol` — failed: after the Frontier, with no Cases line open, the question asked whether to take the W readings, not whether to run /pre-spec. Read by hand, the first defer the person asks for after the render.
- `estimate-documentation-completes` — `rule-documentation` — failed: the run of ff62585 read beyond its list (tail of log.md, head of the old brief.md, git diff of sprint.md and backlog.md, a grep of sprint.md, a count of [x] in the 0137 Spec). Read by `make test-documentation`; the live reading by hand.

Pending:

- `estimate-agent-writing-followed` — `rule-agent-writing` — by hand in a later session, the person's messages of one session against the section in CLAUDE.md.
- `estimate-ask-finds` — `rule-ask` — by hand in a later session: three dispatches of ask-guppi read against the event log.
- `estimate-brief-carries-the-run-facts` — `rule-brief` — by hand at the /hi of the session after the first librarian run whose frame holds this Render.
- `estimate-carry-over-writes` — `rule-carry-over` — `uv run guppi render --check`; by hand, the first /carry after the fork of ExitPlanMode.
- `estimate-case-build-writes-the-case` — `rule-case-build` — by hand: live dispatches in a session after the render.
- `estimate-case-check-sends-back-a-faulty-case` — `rule-case-check` — `uv run pytest tests/test_casecheck.py -k subagent`, then by hand the first answer the hook sends back.
- `estimate-case-check-shows-only-the-checked-case` — `rule-case-check` — `uv run pytest tests/test_casecheck.py -k stop`, then by hand the first reply the hook refuses.
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` — by hand: the first session where a lesson and the Case that closes its cause stand together.
- `estimate-close-commits` — `rule-close` — by hand after the next librarian run: git log, git status, the report in the transcript.
- `estimate-compact-recall-reloads` — `rule-compact-recall` — `pytest tests/test_recall.py`; live, the first compaction of a working session.
- `estimate-context-size-warns-past-the-limit` — `rule-context-size` — `uv run pytest tests/test_context.py -k limit`; live at the first prompt past 400 000 tokens.
- `estimate-end-of-work-order` — `rule-end-of-work` — `make test-end-of-work`, plus by hand at the close of a later session.
- `estimate-estimates-schema-checked` — `rule-estimates-schema` — `pytest tests/test_schemas.py -k estimates`; live, `make lint` with no schema finding on wiki/estimates/.
- `estimate-event-log-records` — `rule-event-log` — pytest in tests/test_event.py and tests/test_gate.py; by hand, one /hi outside plan mode and one in it.
- `estimate-generate-fails-alone` — `rule-page-generation` — `pytest tests/test_generate.py`, the tests of the failed, skipped and marked entries.
- `estimate-generate-renames` — `rule-page-generation` — pytest in tests/test_generate.py; live, the librarian's run on a real rename.
- `estimate-generate-rewords` — `rule-page-generation` — pytest in tests/test_generate.py; live, the librarian's run that applies the first reword.
- `estimate-generate-writes` — `rule-page-generation` — pytest in tests/test_generate.py; the live reading once by hand.
- `estimate-git-context-current` — `rule-git-context` — by hand at the /hi of the next session on the current remote, and its event_log.md at its close.
- `estimate-glossary-terms-defined` — `entity-glossary` — one reading of the table by hand after the librarian's run, plus `make lint`.
- `estimate-glossary-ticks-the-spec` — `rule-glossary` — `pytest tests/test_glossary.py`, plus one reading of the session's spec.md after the librarian's run.
- `estimate-governed-files-hook-refuses` — `rule-governed-files-hook` — `pytest tests/test_guard.py`, plus by hand one Edit of a governed file refused.
- `estimate-handoff-dispatches` — `rule-handoff` — by hand at the /handoff of a later session.
- `estimate-handoff-holds-each-fact-once` — `rule-handoff` — by hand at the first /handoff after the render.
- `estimate-hi-takes-its-readings` — `rule-skill-hi` — by hand at the first /hi after the render.
- `estimate-hi-writes-frontier` — `rule-skill-hi` — by hand at the first /hi of the next session; unit: the frontier findings of `guppi prespec --check`.
- `estimate-index-check-merges` — `rule-index-check` — by hand on the report of a later librarian's run, against its materialize.yaml.
- `estimate-lint-checks-the-method` — `rule-lint` — `uv run pytest tests/test_lint.py`.
- `estimate-lint-finds-a-broken-link` — `rule-lint` — `uv run pytest tests/test_lint.py`.
- `estimate-permissions` — `rule-permissions` — the allow list of .claude/settings.json and tests/test_render.py; live, the person's word on the prompt at a Write of work.md.
- `estimate-plan-mode-verified` — `rule-plan-mode` — `make test-plan-mode`; one live reading by hand.
- `estimate-prespec-catches-a-superseded-case` — `rule-prespec` — `pytest tests/test_prespec.py`; live, the first /pre-spec whose window holds a supersedes of a Case of that session.
- `estimate-raw-archive` — `rule-raw-archive` — `pytest tests/test_archive.py`, plus by hand on the archive step of a later librarian's run.
- `estimate-retro-commit-gates` — `rule-retro-commit` — pytest in tests/test_gate.py; the live reading once by hand.
- `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — `rule-retro` — by hand at the first /retro after the render whose work.md names a check under Expected red.
- `estimate-retro-red-in-the-baseline-is-not-charged` — `rule-retro` — by hand at the first /retro after the render whose Baseline holds a failing test or a lint finding.
- `estimate-retro-report-holds-each-fact-once` — `rule-retro` — by hand at the first /retro after the render.
- `estimate-session-phases-in-order` — `rule-session` — by hand at the close of a session.
- `estimate-session-start-context` — `rule-session-start` — `make test-session-start`; by hand, one session opened without /hi.
- `estimate-skill-wait-what-re-pitches` — `rule-skill-wait-what` — `uv run guppi render --check`; by hand, one run of the skill in a session after the render.
- `estimate-spec-write-reaches-the-approved-spec` — `rule-spec-write` — `uv run pytest tests/test_ratified.py -k approved_spec`; by hand, the first Case ratified in Work Mode.
- `estimate-sprint-migration-index-dissolved` — `entity-sprint-migration` — `test -e vault/wiki/index.md` false; rg for §N and index.md, every hit read by hand.
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` — one reading of the tree by hand at the close of the sprint.
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` — `make lint` exit 0, or only unread lines on the sprint's Estimates.
- `estimate-sprint-migration-merges` — `entity-sprint-migration` — `make test` on the last commit of migration, then git log of main after the merge.
- `estimate-synthesis-clusters` — `rule-synthesis` — by hand, the yaml and the report after a live librarian run whose yaml holds at least two lesson entries.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `rule-work-mode` — `uv run guppi render --check`; by hand, the first /work at the fork and the first /work the person types.
- `estimate-work-mode-takes-the-work-readings` — `rule-work-mode` — by hand at the first /work after the render.

## Flags

- failed: L67 `decision[case 508.2][update][rule-skill-hi]{supersedes:case 507}` — `generate: rule-skill-hi: replace: 'In the chat the Cases are the agenda of Plan Mode, one line ' is absent or not unique`. The ledger holds the lines of 508.2 twice: L15–L16 without `{supersedes:case 507}`, L67–L68 with it. L15 applied the two pairs, so L67 found its anchor gone. L16 and L68 (the update of `estimate-hi-writes-frontier`) both applied, the same `set` and Criterion twice. The entries of 507 (L11, L12) carry `superseded_by: 508.2` and were not applied. The entry stays as it is.
- incomplete: L12 (case 507, `estimate-hi-writes-frontier`) lacks `criterion`; superseded, not applied.
- near: none. unparsed: none.
- Failed Estimates: `estimate-case-build-writes-a-plain-round`, `estimate-case-protocol-defers-in-one-reply`, `estimate-documentation-completes`.
- Synthesis: `insight-case-build-promise-lines-compared-by-no-check` reopened (`actioned` to `open`) by its new child `lesson-case-build-signs-one-criterion-twice-in-a-session`; `addressed_by` `decision-case-472.3` stands.
- MOC candidates: none printed. Contradictions: none found.
- Stale defers, from lint: `rule-subagent-guppi` deferred 31 times since case 29; `rule-case-build-checks-its-sub-cases`, `rule-complaint-becomes-a-lesson`, `rule-morph`, `rule-orchestration`, `rule-prespec-script-skips-code-spans` deferred 1 time each.
- Backlog moves by `generate`: none printed; milestones dropped: none printed.
- `make lint`: exit 2, 123 finding lines. `render --check`, `sprint --check`, `backlog --check` and `glossary --check` passed. Findings: 64 `schema: missing` (`rule-spec-box` fields `kind` and `estimates`; `## Context` and `## Problem` on 31 Decision pages of cases 1–28); 1 `fence` (`decision-case-13`, `## When`); 1 `orphan` (`rule-spec-box`); 6 `deferred`; 51 `unread` (3 failed, 48 pending).

## Next session

Cases:
- `estimate-case-build-writes-a-plain-round` failed — the rounds of case-guppi name Case numbers outside the ➡️ lines (reading L39, handoff).
- `estimate-documentation-completes` failed — the librarian of ff62585 read beyond its list (reading L52, handoff).
- `estimate-case-protocol-defers-in-one-reply` failed — the question after the Frontier asked about the W readings, not /pre-spec (reading L71).
- The `method` of `estimate-materialize-lifts-unfiltered-on-a-schema-change` selects no test with `-k schema_change` (handoff, reading L28).
- Case 508.2 stands twice in the 1134 ledger, the first time without `{supersedes:case 507}`: L67 failed and L68 applied a second time (generate, this run).

Work:
- `estimate-agent-writing-followed`
- `estimate-ask-finds`
- `estimate-brief-carries-the-run-facts`
- `estimate-carry-over-writes`
- `estimate-case-build-writes-the-case`
- `estimate-case-check-sends-back-a-faulty-case`
- `estimate-case-check-shows-only-the-checked-case`
- `estimate-case-protocol-ledger-line-form`
- `estimate-close-commits`
- `estimate-compact-recall-reloads`
- `estimate-context-size-warns-past-the-limit`
- `estimate-end-of-work-order`
- `estimate-estimates-schema-checked`
- `estimate-event-log-records`
- `estimate-generate-fails-alone`
- `estimate-generate-renames`
- `estimate-generate-rewords`
- `estimate-generate-writes`
- `estimate-git-context-current`
- `estimate-glossary-terms-defined`
- `estimate-glossary-ticks-the-spec`
- `estimate-governed-files-hook-refuses`
- `estimate-handoff-dispatches`
- `estimate-handoff-holds-each-fact-once`
- `estimate-hi-takes-its-readings`
- `estimate-hi-writes-frontier`
- `estimate-index-check-merges`
- `estimate-lint-checks-the-method`
- `estimate-lint-finds-a-broken-link`
- `estimate-permissions`
- `estimate-plan-mode-verified`
- `estimate-prespec-catches-a-superseded-case`
- `estimate-raw-archive`
- `estimate-retro-commit-gates`
- `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`
- `estimate-retro-red-in-the-baseline-is-not-charged`
- `estimate-retro-report-holds-each-fact-once`
- `estimate-session-phases-in-order`
- `estimate-session-start-context`
- `estimate-skill-wait-what-re-pitches`
- `estimate-spec-write-reaches-the-approved-spec`
- `estimate-sprint-migration-index-dissolved`
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-merges`
- `estimate-synthesis-clusters`
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
- `estimate-work-mode-takes-the-work-readings`

## Readings at the close

- `make test`: 900 passed, 2 skipped.
- `make lint`: exit 2, 123 finding lines (see Flags).
- Pages in vault/wiki: rules 73, estimates 159, entities 4, decisions 781, lessons 62, insights 26.
