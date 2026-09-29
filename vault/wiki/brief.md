# Brief — 2026-09-29, after the librarian's run on session 1753

## Where things stand

- Session 1753 ratified 520, 521.1, 521.2, 521.3, 521.4, 522, 523, 524.1, 524.2, 524.3, 525. The code of 521.1, 521.2 and 522 is in commit dd08a1b (`guppi/materialize.py`, `guppi/ratified.py`, `guppi/generate.py` and their tests); the session folder is in 3520653; make test 923 passed, 2 skipped; make style clean (handoff).
- Not done, from the handoff: the read line of `estimate-glossary-terms-defined` under Case 520; eight values cut at ` #` in archived Specs of 2026-09-12 to 2026-09-21; the `Stop` line of `estimate-context-size-warns-past-the-limit` not read.
- `vault/raw/2026-09-29/1753/materialize.yaml`: 29 entries from 29 ledger lines, plus 2 of the synthesis; all 31 `applied`, none `failed`, none `incomplete`; the defer of `rule-documentation` marked `exists`. The yamls of 0137, 1134 and 1432 took 0 entries.
- Created: decisions 11 (520, 521.1–521.4, 522, 523, 524.1–524.3, 525); estimates 1 (`estimate-materialize-marks-a-comment`); lessons 2 (`lesson-case-build-rebuild-quotes-the-relayed-words`, `lesson-glossary-one-where-for-a-term-many-schemas-define`).
- Updated: entities 1 (`entity-glossary`); rules 8 by entries (`rule-spec-write`, `rule-materialize`, `rule-estimates-schema`, `rule-case-protocol` by three Cases, `rule-page-generation`, `rule-skill-grill-me`, `rule-case-build`, `rule-documentation` by a defer), and 3 more by the cascade `draft` → `built` (`rule-brief`, `rule-decisions-schema`, `rule-glossary`); estimates 15 (9 readings, 6 by decisions); insights 1; lessons 1.
- Superseded: `decision-case-517` by 525, `decision-case-518` by 523, `decision-case-519` by 521.3; `cleanup` moved the three pages to the archive. `deferred_by` of `rule-documentation` is now `[[decision-case-525]]`; `rule-estimates-schema` and `rule-case-protocol` carry no `deferred_by`.
- Synthesis: `lesson-case-build-rebuild-quotes-the-relayed-words` is clustered under `insight-case-form-chat-form-read-by-no-script` (status `open`, now seven children). `lesson-glossary-one-where-for-a-term-many-schemas-define` has no pair and stays `new`.
- Rendered: `.claude/agents/case-guppi.md`, `.claude/skills/grill-me/SKILL.md`, `vault/wiki/backlog.md`, `vault/wiki/glossary.md`.

## Readings due

- `estimate-case-protocol-defers-in-one-reply` (failed) — `rule-case-protocol` stands `draft`; read by hand in a later session after the render: the first defer that closes the last Cases line, read in the chat against the Criterion (spec.md). Last result: the defer of C2 in session 1134 had the short form, but the question after the Frontier asked about the W readings, not `/pre-spec`.
- `estimate-documentation-completes` (failed) — `rule-documentation` stands `draft`; read by `make test-documentation` and the live reading by hand (method). Last result: run ff62585 read beyond its list: tail of log.md, the old brief.md, git diffs, a grep of sprint.md, a count in the 0137 Spec.
- `estimate-glossary-terms-defined` (failed) — `entity-glossary` stands `draft`; read by hand on the table after the librarian's run, plus `make lint` (method; its spec.md line names no place). Last result: five rows named a `where` page that does not define the term (Vault, `deferred_by`, `origin`, Entity / Rule (status), Hook). This run: `guppi glossary` exit 0, no stderr; the `## Terms` table holds 58 lines, the header included; the rows Vault, Hook, `deferred_by`, `origin`, Entity (status) and Rule (status) stand in `glossary.md` with their new text; `make lint` prints no line on `entity-glossary`.
- `estimate-retro-report-holds-each-fact-once` (failed) — `rule-retro` stands `draft`; read by hand at the first /retro after the render (method). Last result: readings L4, W12 and W15 named in two parts of the report; the commit named as after the approval.
- `estimate-work-mode-takes-the-work-readings` (failed) — `rule-work-mode` stands `draft`; read by hand at the first /work after the render (method). Last result: W1 and W6 skipped though their moment had come.
- `estimate-agent-writing-followed` — `rule-agent-writing` stands `draft`; by hand in a later session (method).
- `estimate-ask-finds` — `rule-ask` stands `draft`; by hand on three dispatches of ask-guppi in a later session (method).
- `estimate-carry-over-writes` — `rule-carry-over` stands `draft`; `guppi render --check`, then by hand the first /carry after the fork of ExitPlanMode (method).
- `estimate-case-build-writes-a-plain-round` — `rule-case-build` stands `draft`; in a later session after the render: one first round that quotes a page and one later round of `case-guppi`, read in the chat against the Criterion (spec.md).
- `estimate-case-build-writes-the-case` — `rule-case-build` stands `draft`; by hand, live dispatches in a session after the render (method).
- `estimate-case-check-sends-back-a-faulty-case` — `rule-case-check` stands `draft`; `pytest tests/test_casecheck.py -k subagent`, then by hand (method).
- `estimate-case-check-shows-only-the-checked-case` — `rule-case-check` stands `draft`; `pytest tests/test_casecheck.py -k stop`, then by hand (method).
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` stands `draft`; by hand on the first session where a lesson and the Case that closes its cause stand together (method).
- `estimate-case-protocol-shows-the-built-case` — `rule-case-protocol` stands `draft`; in a later session after the render: one round of `case-guppi` that quotes a page, read in the chat against the answer and the Criterion (spec.md).
- `estimate-compact-recall-reloads` — `rule-compact-recall` stands `draft`; `pytest tests/test_recall.py`, then by hand at the first compaction (method).
- `estimate-context-size-warns-past-the-limit` — `rule-context-size` stands `draft`; `pytest tests/test_context.py -k limit`, then by hand past 400 000 tokens (method); the handoff says the `Stop` line was not read.
- `estimate-end-of-work-order` — `rule-end-of-work` stands `draft`; `make test-end-of-work`, then by hand at the close of a later session (method).
- `estimate-event-log-records` — `rule-event-log` stands `draft`; pytest in `tests/test_event.py` and `tests/test_gate.py`, then by hand (method).
- `estimate-generate-renames` — `rule-page-generation` stands `draft`; pytest, then by hand at the librarian's run on a real rename (method). This run: no entry of the 1753 yaml carries `rename`; `guppi generate` printed 45 page(s) for 1753 and 0 for 0137, 1134 and 1432, exit 0, no stderr.
- `estimate-generate-rewords` — `rule-page-generation` stands `draft`; pytest, then the librarian's run that applies the first reword (method). This run: no entry of the 1753 yaml carries `reword`; `guppi generate` exit 0, no stderr.
- `estimate-generate-ticks-the-spec` — `rule-page-generation` stands `draft`; pytest with a Spec beside the yaml, then one reading of the session's spec.md after the librarian's run (method). This run: `generate` changed 23 lines of `raw/2026-09-29/1753/spec.md`, each a `- [ ]` to `- [x]`; 8 `- [ ] read` lines stand there; it ticked 3 read lines in `1134/spec.md` and 4 in `1432/spec.md`.
- `estimate-generate-writes` — `rule-page-generation` stands `draft`; pytest, then the live reading by hand (method).
- `estimate-git-context-current` — `rule-git-context` stands `draft`; by hand at the /hi of the next session (method).
- `estimate-governed-files-hook-refuses` — `rule-governed-files-hook` stands `draft`; `pytest tests/test_guard.py`, then one refused Edit by hand (method).
- `estimate-handoff-dispatches` — `rule-handoff` stands `draft`; by hand at the /handoff of a later session (method).
- `estimate-handoff-holds-each-fact-once` — `rule-handoff` stands `draft`; by hand at the first /handoff after the render (method).
- `estimate-materialize-marks-a-comment` — `rule-materialize` stands `draft`; `uv run pytest tests/test_materialize.py -k comment`, at a later session (spec.md).
- `estimate-permissions` — `rule-permissions` stands `draft`; the allow list and `tests/test_render.py`, the live probe by the person's word (method).
- `estimate-plan-mode-verified` — `rule-plan-mode` stands `draft`; `make test-plan-mode`, one live reading by hand (method).
- `estimate-retro-commit-gates` — `rule-retro-commit` stands `draft`; pytest in `tests/test_gate.py`, the live reading by hand (method).
- `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — `rule-retro` stands `draft`; by hand at the first /retro whose work.md names a check under Expected red (method).
- `estimate-session-phases-in-order` — `rule-session` stands `draft`; by hand at the close of a session (method).
- `estimate-session-start-context` — `rule-session-start` stands `draft`; `make test-session-start`, then by hand (method).
- `estimate-skill-grill-me-asks-in-rounds` — `rule-skill-grill-me` stands `draft`; in a later session after the render: `uv run guppi render --check`, then one round that quotes a page read in the chat against the Criterion (spec.md).
- `estimate-skill-wait-what-re-pitches` — `rule-skill-wait-what` stands `draft`; `guppi render --check`, then one run of the skill by hand (method).
- `estimate-spec-write-reaches-the-approved-spec` — `rule-spec-write` stands `draft`; `pytest tests/test_ratified.py -k approved_spec`, then the first Case ratified in Work Mode (method).
- `estimate-spec-write-writes-a-defer` — `rule-spec-write` stands `draft`; `uv run pytest tests/test_ratified.py -k defer`, then by hand the first defer the person asks for after the change, at a later session (spec.md).
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` stands `draft`; by hand on the tree at the close of the sprint (method).
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` stands `draft`; `make lint`, exit 0 or only unread lines on its Estimates (method).
- `estimate-sprint-migration-merges` — `entity-sprint-migration` stands `draft`; `make test` on the last commit of migration, then git log of main (method).
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `rule-work-mode` stands `draft`; `guppi render --check`, then by hand at the first /work (method).
- No pending Estimate's `method` names the archive step of the librarian's run.

## Flags

- No entry marked `incomplete`, `failed` or `near`; `unparsed: []`.
- Failed Estimates: `estimate-case-protocol-defers-in-one-reply`, `estimate-documentation-completes`, `estimate-glossary-terms-defined`, `estimate-retro-report-holds-each-fact-once`, `estimate-work-mode-takes-the-work-readings`.
- The read line of `estimate-glossary-terms-defined` at `raw/2026-09-29/1753/spec.md` line 72 stays unticked: its reading L4 stands before the first decision line of Case 520 (handoff).
- Contradiction (handoff): the context of Case 521, and the text it wrote into `rule-spec-write`, `rule-materialize` and `rule-case-protocol`, say YAML reads a `#` after a tab as a comment; the handoff says PyYAML refuses such a block.
- Contradiction (handoff): `insight-materialize-estimate-update-lifts-the-criterion-whole` describes behaviour gone since case 378.4.
- Handoff: eight values cut at ` #` stand in archived Specs of 2026-09-12 to 2026-09-21; `materialize` reads no archive.
- MOC candidates: none raised. `generate` moved no item to the Backlog and dropped no milestone in this run (no such line printed).
- Stale defers, from `make lint`: `rule-subagent-guppi` 31 times since case 29; `rule-case-build-checks-its-sub-cases` since case 480; `rule-complaint-becomes-a-lesson` since case 504; `rule-morph` since case 239; `rule-orchestration` since case 424; `rule-prespec-script-skips-code-spans` since case 481 (1 time each).
- `make lint`, exit 2, 82 findings: 41 `unread` (36 pending, 5 failed Estimates); 33 `schema` (31 Decision pages of Cases 1–28 missing `## Problem`; `rule-spec-box` missing the fields `kind` and `estimates`); 1 `fence` on `decision-case-13`; 1 `orphan` on `rule-spec-box`; 6 `deferred`. `render --check`, `sprint --check`, `backlog --check` and `glossary --check` print nothing.

## Next session

Cases:
- `estimate-case-protocol-defers-in-one-reply` failed (Estimate page).
- `estimate-documentation-completes` failed (Estimate page).
- `estimate-glossary-terms-defined` failed; its read line in the 1753 Spec stays open (ledger L4, handoff).
- `estimate-retro-report-holds-each-fact-once` failed (ledger L29).
- `estimate-work-mode-takes-the-work-readings` failed (ledger L27).
- The tab before `#`: PyYAML refuses the block, while Case 521 and three rule pages say it cuts (handoff).
- `insight-materialize-estimate-update-lifts-the-criterion-whole` describes behaviour gone since case 378.4 (handoff).
- `rule-spec-box`: `schema` missing `kind` and `estimates`, and `orphan` (make lint).

Work:
- The 36 pending readings of Readings due, by slug. The unticked boxes of the Specs are all `read` lines of these Estimates or of the failed ones above: 8 in `1753/spec.md`, 6 in `0137/spec.md`, 1 in `1134/spec.md`, 3 in `1432/spec.md`.
- Ledger lines not applied: none (29 lines, 29 entries, all applied).
- Dirty tree: none after the librarian's commit.

## Readings at the close

- `make test`: 923 passed, 2 skipped.
- `make lint`: exit 2, 82 findings, as in Flags.
- Pages: decisions 801, entities 4, estimates 159, insights 26, lessons 68, rules 73.
