# Brief — 2026-09-25, the librarian's run over session 0051

## Where things stand

- Session 0051 closed Plan Mode with Cases 414 (414.1, 414.2), 415 and 417 ratified, and deferred 416 and 418. Frontier C3, C7, C10 and C11 were closed by Cases; C6 and W24 were closed as work; C4, C5, C8, C12, C13 and C14 were deferred by 416 and C9 by 418; C1 and C2 stay for the sprint.
- Work Mode, commit 5c945b4: `guppi/prespec.py` (`judge`, the checks shared by `check` and `written_findings`; `check_ratified` excepts a parent whose sub-cases in the copy are all superseded), `guppi/ratified.py` (`stop` runs `written_findings` on each Case it wrote), `tests/test_ratified.py` and `tests/test_prespec.py`. The session's `make test` gave 633 passed, 2 skipped, and `make style` was clean.
- Not done in the session: the reading of `estimate-spec-write-checks-the-written-case` (its method has a live part), the reading of `estimate-case-protocol-acknowledging-reply` (by hand), and the Work list of the previous brief.
- The run walked `raw/2026-09-24/2214/` (0 new entries, 0 pages written) and `raw/2026-09-25/0051/`.
- Yaml of 0051: 24 entries. 20 come from the 20 lines of the ledger: 6 `update`, 1 `create`, 6 `defer`, 5 `lesson`, 2 `estimate` readings. 4 were added by the librarian's synthesis: 1 `create` of an Insight and 3 `update` of lessons. All 24 were applied.
- Yaml of 2214: the `{supersedes}` lines of 0051 marked 8 entries `superseded_by`: line 15 by 416, lines 19–24 by 414.1, line 25 by 415. These entries had already been applied on 2026-09-24.
- Pages, from the tree after cleanup:
  - decisions: 6 written (414.1, 414.2, 415, 416, 417, 418). 408, 412 and 413 became `superseded`, and cleanup moved them to the archive.
  - estimates: 1 created, `estimate-spec-write-checks-the-written-case`. 3 updated: `estimate-case-protocol-acknowledging-reply`, `estimate-case-protocol-case-form` and `estimate-prespec-checks-the-ratified-copy`.
  - rules: 7 updated. Cases changed `rule-spec-write`, `rule-case-protocol` and `rule-prespec`. Defers changed `rule-frame-check`, `rule-case-protocol`, `rule-spec-write`, `rule-spec-reconcile`, `rule-ask` and `rule-context-size`.
  - lessons: 5 created. 2 updated to `clustered`.
  - insights: 1 created, `insight-case-form-chat-form-read-by-no-script`, `open`, severity 3.
  - entities: none.
- Governed files written by render: `vault/wiki/case-schema.md` (Case 414.2) and `.claude/skills/pre-spec/SKILL.md` (Case 417). `guppi sprint` and `guppi glossary` changed nothing.

## Readings due

1 Estimate stands `failed` and 23 stand `pending`:

- `estimate-case-protocol-case-form` — `failed` — `rule-case-protocol` draft — by hand, the Cases of a session at its close (method). Result: on 2026-09-25, Case 414 showed a count of items in its `context` and Case 415 showed a bookkeeping `－` line in `then`. ask-guppi found both at pre-spec, and both were fixed. Cases 416–418 hold the form.
- `estimate-spec-write-checks-the-written-case` — `rule-spec-write` draft — `uv run pytest tests/test_ratified.py -k checks_the_written`, then by hand at the first ratification after the change (`raw/2026-09-25/0051/spec.md`).
- `estimate-case-protocol-acknowledging-reply` — `rule-case-protocol` draft — by hand, the first acknowledging reply that a `Stop` hook refuses (`raw/2026-09-25/0051/spec.md`).
- `estimate-case-protocol-checks-its-frame` — `rule-case-protocol` draft — by hand, the Cases of a session at its close, their context against the Agent calls of the event log (method).
- `estimate-case-protocol-defers-in-one-reply` — `rule-case-protocol` draft — by hand, the first defer the person asks for after the render (method).
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` draft — by hand, the ledger and the preview of the first session where a lesson and the Case that closes its cause stand together (method).
- `estimate-frame-check-finds-a-contradiction` — `rule-frame-check` draft — by hand, two live dispatches (method).
- `estimate-context-size-warns-past-the-limit` — `rule-context-size` draft — `uv run pytest tests/test_context.py -k limit`, then by hand at the first prompt past 400 000 tokens (method).
- `estimate-harness-pipeline` — `rule-harness` draft — `make test-harness`, then the live reading of `make lint` by hand (method).
- `estimate-hook-registry-rendered` — `rule-hook-registry` draft — the JSON case of `tests/test_render.py`, then `uv run guppi render --check` after the render (method).
- `estimate-prespec-reconciles` — `rule-prespec` draft — by hand, the first `/pre-spec` after the render (method).
- `estimate-agent-writing-followed` — `rule-agent-writing` draft — by hand, the section in `CLAUDE.md` and one reply of the agent against it (method).
- `estimate-carry-over-writes` — `rule-carry-over` draft — pytest over the skill's render, plus one live reading of a carried-over session (method).
- `estimate-documentation-completes` — `rule-documentation` draft — `make test-documentation`, then the live reading by hand (method).
- `estimate-language-followed` — `rule-language` draft — by hand, the section in `CLAUDE.md`, the session's commit, Spec and chat against it (method).
- `estimate-one-judgment-one-implementation-followed` — `rule-one-judgment-one-implementation` draft — `render --check` exit 0, then by hand the diff of the next Work Mode session (method).
- `estimate-retro-report-holds-each-fact-once` — `rule-retro` draft — by hand, the first `/retro` after the render (method).
- `estimate-session-phases-in-order` — `rule-session` draft — by hand at the close of a session, the day's records in order (method).
- `estimate-sprint-renders-the-backlog` — `rule-sprint` draft — `pytest tests/test_sprint.py`, plus one reading of the rendered `sprint.md` after the librarian's run (method).
- `estimate-synthesis-keeps-actioned-by-the-mark` — `rule-synthesis` draft — by hand, the yaml and the brief after the first marked lesson is clustered under an actioned Insight (method).
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` draft — by hand, the tree at the close of the sprint (method).
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` draft — `make lint` exit 0, or only unread lines on the Estimates of the sprint (method).
- `estimate-sprint-migration-merges` — `entity-sprint-migration` draft — `make test` on the last commit of migration, then `git log` of main after the merge (method).
- `estimate-sprint-migration-rule-class-files-dissolved` — `entity-sprint-migration` draft — by hand, the listed `ls`, `grep`, `render --check` and `glossary --check` (method).

## Deferred

1. `insight-case-form-chat-form-read-by-no-script` — severity 3. Pattern: no script reads the form rules of a Case as shown in the chat (section order, what `ratification` holds, a count in a story section), so they hold only as far as the agent reads its own Case, and the person or ask-guppi at pre-spec finds the fault later. Proposal: have a check read the chat form of a Case before the person does, for example the `SubagentStop` check that the scheme deferred by Case 416 proposes. Briefs: 1.
2. `rule-frame-check` — deferred by Cases 403 and 416. Under 403: whether `frame-guppi` pays for its tokens and time. Under 416: `frame-guppi` becomes `case-guppi`, which builds the Case, runs on Opus with effort medium and is asked again by `SendMessage`; the question of Case 408 is part of 416. Severity: none. Briefs: 3.
3. `rule-context-size` — deferred by Cases 404, 409 and 418: the limit of 400 000 tokens and the text of the `UserPromptSubmit` hook past it. This is judged once a session reaches the limit. Severity: none. Briefs: 3.
4. `rule-spec-write` — deferred by Case 416: the Case checked on `SubagentStop` and shown by a hook from the answer of `case-guppi`; `ratified` writes the Case the person saw, and writes the defers too. Severity: none. Briefs: 2.
5. `rule-spec-reconcile` — deferred by Case 416: the plan written by hooks alone, with a guard while a Frontier Case line is open; when the prose of a Case is translated (the question of Case 410). Severity: none. Briefs: 2.
6. `rule-case-protocol` — deferred by Case 416: `case-schema.md` read by `case-guppi` only; the orchestration of the main agent becomes a rule of its own, loaded by `/hi`. Severity: none. Briefs: 1.
7. `rule-ask` — deferred by Case 416: `ask-guppi` answers at pre-spec only; the vault query before a `create` moves to `case-guppi`. Severity: none. Briefs: 1.

`{supersedes:case 412}` of 414.1 and `{supersedes:case 413}` of 415 retired the previous brief's item `rule-prespec`. `{supersedes:case 408}` of 416 retired 408 in the `rule-frame-check` item. The open Insight `insight-workflow-code-live-before-the-page-it-reads` is named by the sprint page, so it is not listed here.

## Flags

- `near`: `lesson-hooks-subagentstop-exit-2-sends-the-subagent-back` (`raw/2026-09-25/0051/ledger.md#L17`) is near `lesson-hooks-windows-stdin-encoding`. Both say that a Python hook on Windows must read stdin as UTF-8.
- `incomplete`, `failed`, `unparsed`: none in the yamls of 2214 and 0051.
- Failed Estimate: `estimate-case-protocol-case-form`. Its reading is under Readings due.
- Synthesis: `insight-case-form-chat-form-read-by-no-script` was created `open`, with children `lesson-case-form-the-spec-free-sections-written-last`, `lesson-case-form-ratification-used-for-the-agents-caveats` and `lesson-case-form-a-count-in-the-sentence-that-opens-a-list`. All three are now `clustered`.
- Case 414.1 updated `rule-spec-write` and Case 414.2 updated `rule-case-protocol`. Case 416 of the same Spec defers both pages. The handoff names this as known and chosen: 414 is the step now, and 416 is the scheme after it.
- MOC candidates: none.
- Stale defers, from lint: `rule-subagent-guppi` and `rule-work-mode` have been deferred 31 times since case 29. `rule-morph` has been deferred once since case 239.
- Contradictions: none found in this run.
- Backlog moves by `generate`: none printed. Milestones dropped: none printed.
- `generate`, `cleanup`, `render`, `sprint`, `glossary`: no stderr lines.
- `make lint`, after the render: exit 2, 93 findings.
  - `decisions/decision-case-N: schema: missing section ## Context` and `## Problem` on 31 pages. That is 62 findings.
  - `rules/rule-spec-box: schema: missing field kind`, `missing field estimates`, and `orphan: no other live page names it in its frontmatter`.
  - `rules/rule-morph: deferred: 1 time since case 239`; `rules/rule-subagent-guppi: deferred: 31 times since case 29`; `rules/rule-work-mode: deferred: 31 times since case 29`.
  - `unread: pending` on 23 Estimates and `unread: failed` on `estimate-case-protocol-case-form`. These are the 24 Estimates of Readings due.
  - `estimates: unmigrated: 20 pages in the shape before case 193`.

## Next session

Cases:
- The scheme of Case 416 is to be decided with the results of live probe W24. The handoff records these results. A `SubagentStop` exit 2 sends the subagent back. A `SubagentStop` `systemMessage` is shown nowhere. A `Stop` `systemMessage` shows in VS Code with each line prefixed and no markdown, and the person judged that unusable for showing a Case. So the showing stays the main agent's copy, which a hook compares with the checked answer (handoff).
- Failed Estimate `estimate-case-protocol-case-form`: Case 414 showed a count of items and Case 415 a bookkeeping `－` line at the showing (`raw/2026-09-25/0051/ledger.md#L19`).

Work:
- `estimate-spec-write-checks-the-written-case`
- `estimate-case-protocol-acknowledging-reply`
- `estimate-case-protocol-checks-its-frame`
- `estimate-case-protocol-defers-in-one-reply`
- `estimate-case-protocol-ledger-line-form`
- `estimate-frame-check-finds-a-contradiction`
- `estimate-context-size-warns-past-the-limit`
- `estimate-harness-pipeline`
- `estimate-hook-registry-rendered`
- `estimate-prespec-reconciles`
- `estimate-agent-writing-followed`
- `estimate-carry-over-writes`
- `estimate-documentation-completes`
- `estimate-language-followed`
- `estimate-one-judgment-one-implementation-followed`
- `estimate-retro-report-holds-each-fact-once`
- `estimate-session-phases-in-order`
- `estimate-sprint-renders-the-backlog`
- `estimate-synthesis-keeps-actioned-by-the-mark`
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-merges`
- `estimate-sprint-migration-rule-class-files-dissolved`
- Ledger lines not applied: `raw/2026-09-24/2214/ledger.md` lines 3–14, 17 and 18. They are superseded by 412 and 413. All 20 lines of `raw/2026-09-25/0051/ledger.md` were applied.

## Readings at the close

- `make test`: 633 passed, 2 skipped.
- `make lint`: exit 2, 93 findings (listed under Flags).
- Pages in `vault/wiki/`: decisions 578, estimates 129, rules 63, lessons 55, insights 22, entities 4.
