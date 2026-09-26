# Brief — 2026-09-26, the librarian's run over session 1337

## Where things stand

- Session 1337 ratified Cases 433, 434 (three times; the last version stands), 435, 436.1, 436.2, 436.3, 436.4 (twice) and 437, and deferred `rule-prespec` by Case 438. Frontier: C3–C6 and C9–C11 were closed by Cases or work; C1 and C2 stay for the sprint; C7 and C8 are deferred and kept; C12 is deferred by Case 438 (handoff).
- Code, commit 95e9619: `guppi/materialize.py` (`ITEM_KEYS`, `accepted_keys`, `item_keys`), `guppi/generate.py`, `guppi/ratified.py`, `guppi/prespec.py`, `guppi/casecheck.py`, `guppi/ledger.py`; tests in `test_casecheck.py`, `test_ratified.py`, `test_prespec.py`, `test_materialize.py`. The session's `make test` gave 694 passed, 2 skipped; `make style` was clean (handoff).
- W28 is done: the `SubagentStop` payload of Claude Code 2.1.282 carries `agent_transcript_path`; the probe in `guppi/casecheck.py` was removed (handoff).
- Not done in the session: the readings of the Estimates the session changed (a later session); Frontier Work lines W1–W27; the manual part of 434, whether an exit 2 with `stop_hook_active: true` reaches the subagent (handoff).
- The walk named `raw/2026-09-25/0051/`, `raw/2026-09-25/1228/` and `raw/2026-09-25/1654/` (0 new entries each) and `raw/2026-09-26/1337/`. After the brief, `guppi archive` moved the three units of 2026-09-25 to `archive/migration/2026-09-25/<unit>/raw`; the paths below name them there. `raw/2026-09-26/1337/` stays, the session of the run.
- Yaml of 1337: 20 entries from the 20 lines of the ledger: 16 `update`, 1 `defer`, 3 `lesson`. The librarian added 3 entries (synthesis): 1 `create` of an Insight, 2 `update` of lessons. All 23 are `applied`. 9 Decisions applied.
- Pages, from the tree after cleanup against commit 95e9619 (`generate`: 23 pages written or changed):
  - decisions: 9 written (433, 434, 435, 436.1–436.4, 437, 438).
  - estimates: 5 updated, all set `pending`: `estimate-case-check-sends-back-a-faulty-case` (434, then 436.4), `estimate-case-protocol-shows-the-built-case` (435), `estimate-spec-write-copies-the-ratified-case` (436.1, then 437), `estimate-prespec-checks-the-form-of-an-item` (436.2), `estimate-spec-write-writes-a-defer` (436.3).
  - rules: 4 updated: `rule-case-check` (434, 436.4), `rule-case-protocol` (435, 437), `rule-spec-write` (436.1, 436.3, 437), `rule-prespec` (436.2; `deferred_by` 438).
  - lessons: 3 created: `lesson-hooks-subagentstop-reads-the-last-text-not-the-handback` (`new`), `lesson-hooks-subagentstop-fires-before-and-after-the-handback` (`new`), `lesson-case-show-ref-of-a-ratification-line-retyped` (`clustered`). 1 updated: `lesson-case-show-sub-case-ratification-retyped` (`## Trigger` by 433; `clustered`).
  - insights: 1 created, `insight-case-show-built-case-retyped-by-hand`, `open`, severity 2.
  - entities: none changed.
- Governed files differ from commit 95e9619: `.claude/skills/pre-spec/SKILL.md`, `vault/wiki/case-schema.md`. `guppi sprint` and `guppi glossary` changed nothing.

## Readings due

28 Estimates stand `pending`; none stands `failed`. The handoff puts the readings of the five Estimates this session changed in a later session.

- `estimate-case-check-sends-back-a-faulty-case` — `rule-case-check` draft — `raw/2026-09-26/1337/spec.md` lines 107 and 368; `archive/migration/2026-09-25/1228/raw/spec.md` line 240.
- `estimate-case-protocol-shows-the-built-case` — `rule-case-protocol` draft — `raw/2026-09-26/1337/spec.md` line 163. It stood `failed`; Case 435 replaced its Criterion and set it `pending`.
- `estimate-spec-write-copies-the-ratified-case` — `rule-spec-write` draft — `raw/2026-09-26/1337/spec.md` lines 232 and 436.
- `estimate-prespec-checks-the-form-of-an-item` — `rule-prespec` draft — `raw/2026-09-26/1337/spec.md` line 277.
- `estimate-spec-write-writes-a-defer` — `rule-spec-write` draft — `raw/2026-09-26/1337/spec.md` line 320; `archive/migration/2026-09-25/1228/raw/spec.md` line 513.
- `estimate-prespec-matches-lines-and-items` — `rule-prespec` draft — `archive/migration/2026-09-25/1654/raw/spec.md` line 99.
- `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` — `rule-ledger-write` draft — `archive/migration/2026-09-25/1654/raw/spec.md` line 240.
- `estimate-ledger-write-lifts` — `rule-ledger-write` draft — `archive/migration/2026-09-25/1654/raw/spec.md` line 274.
- `estimate-retro-loads` — `rule-retro` draft — `archive/migration/2026-09-25/1654/raw/spec.md` line 313.
- `estimate-retro-report-holds-each-fact-once` — `rule-retro` draft — `archive/migration/2026-09-25/1654/raw/spec.md` line 354.
- `estimate-materialize-marks-superseded` — `rule-materialize` draft — `archive/migration/2026-09-25/1654/raw/spec.md` line 439.
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` draft — `archive/migration/2026-09-25/1654/raw/spec.md` line 440.
- `estimate-context-size-warns-past-the-limit` — `rule-context-size` draft — `archive/migration/2026-09-25/1654/raw/spec.md` line 492.
- `estimate-case-protocol-case-form` — `rule-case-protocol` draft — `archive/migration/2026-09-25/1654/raw/spec.md` line 535.
- `estimate-prespec-requires-a-task-line` — `rule-prespec` draft — `archive/migration/2026-09-25/1654/raw/spec.md` line 596.
- `estimate-case-build-writes-the-case` — `rule-case-build` draft — `archive/migration/2026-09-25/1228/raw/spec.md` line 155.
- `estimate-case-protocol-defers-in-one-reply` — `rule-case-protocol` draft — `archive/migration/2026-09-25/1228/raw/spec.md` line 553.
- `estimate-agent-writing-followed` — `rule-agent-writing` draft — by hand, the section in `CLAUDE.md` and one reply of the agent against it (method).
- `estimate-carry-over-writes` — `rule-carry-over` draft — pytest over the skill's render, plus one live reading of a carried-over session (method).
- `estimate-documentation-completes` — `rule-documentation` draft — `make test-documentation`, then the live reading by hand (method).
- `estimate-language-followed` — `rule-language` draft — by hand, the section in `CLAUDE.md`, the session's commit, Spec and chat against it (method).
- `estimate-session-phases-in-order` — `rule-session` draft — by hand at the close of a session, the day's records in order (method).
- `estimate-sprint-renders-the-backlog` — `rule-sprint` draft — `pytest tests/test_sprint.py`, plus one reading of the rendered `sprint.md` after the librarian's run (method).
- `estimate-synthesis-keeps-actioned-by-the-mark` — `rule-synthesis` draft — by hand, the yaml and the brief after the librarian's run on the first marked lesson clustered under an actioned Insight (method).
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` draft — by hand, the tree at the close of the sprint (method).
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` draft — `make lint` exit 0, or only unread lines on the Estimates of the sprint (method).
- `estimate-sprint-migration-merges` — `entity-sprint-migration` draft — `make test` on the last commit of migration, then `git log` of main after the merge (method).
- `estimate-sprint-migration-rule-class-files-dissolved` — `entity-sprint-migration` draft — by hand, the listed `ls`, `grep`, `render --check` and `glossary --check` (method).

## Deferred

1. `insight-case-show-built-case-retyped-by-hand` — severity 2 — The main agent writes the Case that case-guppi built out again by hand instead of copying the answer, so a showing can differ from the answer in any line, and only the comparison on Stop stands between the retyped Case and the person. Proposal: let the showing of a built Case not pass through the agent's retyping, or let the comparison on Stop also refuse a second showing that differs. Briefs: 1.
2. `rule-spec-reconcile` — deferred by Case 423: a guard that refuses the agent's edits of the plan while a Cases line of the Frontier is open; when and how the prose of a Case is translated. Severity: none. Briefs: 5.
3. `rule-orchestration` — deferred by Case 424: the orchestration of the main agent as a rule of its own loaded by `/hi`, and `case-schema.md` read by `case-guppi` alone. Severity: none. Briefs: 3.
4. `rule-prespec` — deferred by Case 438: after case 437, a pre-spec finding in the body of a Case goes to its case-guppi and a new ratification, prose is fixed in the plan as a DIFF, and the translation of name, context and problem is the last step. Severity: none. Briefs: 1.

No `supersedes` in the yaml of 1337, so no item of the previous list is retired. The defers of Case 416 (yaml of 0051) are `superseded_by: 419.2`, and the defer of `rule-context-size` is retired by 430. The open Insight `insight-workflow-code-live-before-the-page-it-reads` is named by the sprint page, so it is not listed here.

## Flags

- `incomplete`, `failed`, `unparsed`: none in the yamls of 0051, 1228, 1654 and 1337.
- `near`, this run: `raw/2026-09-26/1337/materialize.yaml` line 19, `lesson-hooks-subagentstop-fires-before-and-after-the-handback` near `lesson-hooks-subagentstop-exit-2-sends-the-subagent-back`; line 20, `lesson-case-show-ref-of-a-ratification-line-retyped` near `lesson-case-show-sub-case-ratification-retyped`.
- `near`, from earlier runs: `archive/migration/2026-09-25/0051/raw/materialize.yaml` line 17, `lesson-hooks-subagentstop-exit-2-sends-the-subagent-back` near `lesson-hooks-windows-stdin-encoding`; `archive/migration/2026-09-25/1228/raw/materialize.yaml` line 8, `rule-case-check` near `rule-spec-write`.
- Synthesis: `insight-case-show-built-case-retyped-by-hand` created from `lesson-case-show-sub-case-ratification-retyped` and `lesson-case-show-ref-of-a-ratification-line-retyped`; both lessons `clustered`. No lesson of the pair carries `addressed_by`, so the Insight is `open`. `lesson-hooks-subagentstop-reads-the-last-text-not-the-handback` (entry `addressed_by: decision-case-434`) and `lesson-hooks-subagentstop-fires-before-and-after-the-handback` have no pair and stay `new`.
- Failed Estimates: none after `generate`.
- The by-hand check of Case 433 (`raw/2026-09-26/1337/spec.md` line 43): after `generate` the `## Trigger` of `lesson-case-show-sub-case-ratification-retyped` reads "the comparison of casecheck on Stop refused the reply", and the page holds `SubagentStop` 0 times. The box stays unticked. The contradiction of the previous brief is closed by Case 433.
- The order the handoff asks: in the yaml, 434 (line 4) stands before 436.4 (line 17), and 436.1 (line 8) before 437 (line 14). After `generate`, `estimate-case-check-sends-back-a-faulty-case` holds the line of 436.4 on the categories whose schema rule the session changes, and `estimate-spec-write-copies-the-ratified-case` holds the "stored answer of Case N" of 437. Every `replace` pair of `rule-case-check`, `rule-spec-write` and `rule-case-protocol` applied; `generate` printed no line.
- Handoff note: `/hi` did not run as a skill; its `!` command lines failed the permission check of Claude Code 2.1.282 in VS Code, and the agent ran the four commands by hand.
- Handoff note: Cases 434 and 436.4, re-ratified in Work Mode, reached only the plan file; their sections of `raw/2026-09-26/1337/spec.md` were replaced by hand from the plan, with the person's consent.
- Handoff note: a consequence of 436.2 that no Case ratified on its own — the old key `contract` on an `update` item is now a pre-spec finding, where case 194.1 let it pass; the test `test_the_keys_of_the_old_shape_are_not_read` was changed to that. On a `create` the old keys still pass.
- Handoff note: `archive/migration/2026-09-25/1228/raw/spec.md` line 151 and `archive/migration/2026-09-25/1654/raw/spec.md` line 46 were ticked by hand as work (C5 and C6 of the Frontier).
- Handoff note: context passed 400 000 tokens in Work Mode.
- MOC candidates: none.
- Stale defers, from lint: `rule-subagent-guppi` and `rule-work-mode` have been deferred 31 times since case 29. `rule-morph` has been deferred once since case 239, and `rule-orchestration` once since case 424.
- Backlog moves by `generate`: none printed. Milestones dropped: none printed.
- `generate`, `cleanup`, `render`, `sprint`, `glossary`, `archive`: no stderr lines. `cleanup` moved 0 pages.
- `archive` moved `raw/2026-09-25/0051`, `raw/2026-09-25/1228` and `raw/2026-09-25/1654` to `archive/migration/2026-09-25/<unit>/raw`, the specs of 1228 and 1654 with 14 unticked `read` lines (4 in 1228, 10 in 1654) and 1 unticked by-hand box (1654 line 149) among them. The debt of those read lines is carried by the Estimates' `pending` and lint's `unread`.
- `make lint`, after the render: exit 2, 98 findings.
  - `decisions/decision-case-N: schema: missing section ## Context` and `## Problem` on 31 pages. That is 62 findings.
  - `rules/rule-spec-box: schema: missing field kind`, `missing field estimates`, and `orphan: no other live page names it in its frontmatter`.
  - `rules/rule-morph: deferred: 1 time since case 239`; `rules/rule-orchestration: deferred: 1 time since case 424`; `rules/rule-subagent-guppi: deferred: 31 times since case 29`; `rules/rule-work-mode: deferred: 31 times since case 29`.
  - `unread: pending` on 28 Estimates. These are the 28 Estimates of Readings due.
  - `estimates: unmigrated: 20 pages in the shape before case 193`.

## Next session

Cases:
- A Case re-ratified in Work Mode does not reach `spec.md`; the handoff names a possible fix, the Spec hook writing into `spec.md` once it stands (handoff, question 1).
- The agent can forget the mark `{addressed_by:case N}` or `{addresses:…}` on a lesson line; `lesson-hooks-subagentstop-fires-before-and-after-the-handback` (ledger L19) carries none, though Case 434 closes its cause (handoff, question 2).
- `/hi` did not run as a skill: its `!` command lines failed the permission check of Claude Code 2.1.282 in VS Code (handoff, Notes from memory).
- The key `contract` on an `update` item became a pre-spec finding by 436.2 with no Case of its own (handoff, Notes from memory).

Work:
- `estimate-case-check-sends-back-a-faulty-case`, with the manual part of 434: whether an exit 2 with `stop_hook_active: true` reaches the subagent (handoff)
- `estimate-case-protocol-shows-the-built-case`
- `estimate-spec-write-copies-the-ratified-case`
- `estimate-prespec-checks-the-form-of-an-item`
- `estimate-spec-write-writes-a-defer`
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
- Unticked by-hand box of `raw/2026-09-26/1337/spec.md` line 43 (the check of Case 433; its result is under Flags).
- Unticked by-hand box of `archive/migration/2026-09-25/1654/raw/spec.md` line 149 (the check of Case 427; its result stood under the Flags of the previous brief).
- Frontier Work lines W1–W27 (handoff).
- Ledger lines not applied: none. All 20 lines of `raw/2026-09-26/1337/ledger.md` have an entry, and all are `applied`.

## Readings at the close

- `make test`: 694 passed, 2 skipped.
- `make lint`: exit 2, 98 findings (listed under Flags).
- Pages in `vault/wiki/`: decisions 605, estimates 134, rules 66, lessons 56, insights 24, entities 4.
