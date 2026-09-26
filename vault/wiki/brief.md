# Brief — 2026-09-26, the librarian's run over session 1745

## Where things stand

- Session 1745 ratified Cases 439, 440 (440.1–440.3) and 441 (441.1–441.10), and deferred `rule-ledger-write` by Case 442. Commit e82477f; the `/hi` fix is commit 54509ed, made before `/hi` and outside a Case, ratified after the fact by Case 439 (handoff).
- Code, commit e82477f: `guppi/materialize.py`, `guppi/prespec.py`, `guppi/casecheck.py`, `guppi/ratified.py`, `guppi/spec.py`; tests in `test_materialize.py`, `test_prespec.py`, `test_gate.py`, `test_casecheck.py`, `test_ratified.py`. The session's `make test` gave 707 passed, 2 skipped; `make style` was clean (handoff).
- Readings of the session: 7 passed, 4 failed (handoff, ledger lines 27–37).
- Not done in the session: the readings of the 12 Estimates the session changes or creates; the readings the handoff names not readable yet; Frontier Work lines W1–W3, W9, W10, W12, W13, W16, W19–W28 and W31 (handoff). Frontier C1 and C2 stay for the sprint; C7–C9 are deferred and kept (handoff).
- The walk named `raw/2026-09-26/1337/` (0 new entries; `materialize` added the mark `superseded_by: 441.4` to its defer of `rule-prespec`, line 18) and `raw/2026-09-26/1745/`.
- Yaml of 1745: 38 entries from the 38 lines of the ledger: 22 `update`, 2 `create`, 1 `defer` (`exists`), 11 `estimate`, 2 `lesson`. The librarian added 2 entries (synthesis): 1 `update` of an Insight, 1 `update` of a lesson. All 40 are `applied`. 15 Decisions applied.
- Pages (`generate`: 50 pages written or changed; `cleanup`: 2 pages moved):
  - decisions: 15 created (439, 440.1–440.3, 441.1–441.10, 442). `decision-case-438` became `superseded` by 441.4, then `archived`; `cleanup` moved it to the archive.
  - estimates: 2 created, `pending`: `estimate-spec-write-reaches-the-approved-spec` (441.6), `estimate-spec-write-removes-a-superseded-case` (441.7). 10 updated by Cases, all `pending`: `estimate-materialize-lifts-a-create-by-the-schema` (440.1), `estimate-materialize-assembles` (440.2), `estimate-case-build-writes-the-case` (441.1), `estimate-case-protocol-shows-the-built-case` (441.2), `estimate-case-check-shows-only-the-checked-case` (441.3), `estimate-prespec-reconciles` (441.4), `estimate-prespec-checks-the-ratified-copy` (441.5), `estimate-spec-write-copies-the-ratified-case` (441.8), `estimate-spec-write-checks-the-written-case` (441.9), `estimate-spec-capture-appends` (441.10). 11 updated by readings: 7 `passed`, 4 `failed`.
  - rules: 8 updated: `rule-skill-hi` (439), `rule-case-protocol` (440.3, 441.2, 441.6, 441.7), `rule-case-build` (441.1), `rule-case-check` (441.3), `rule-prespec` (441.4; its `deferred_by` 438 removed), `rule-spec-write` (441.6, 441.7, 441.8), `rule-spec-capture` (441.6). 1 deferred: `rule-ledger-write` (`deferred_by` 442). Cascade: `rule-ledger-write` draft → built; `rule-spec-capture` built → draft.
  - lessons: 2 created: `lesson-case-build-a-criterion-replaced-whole-drops-a-line` (`new`); `lesson-hi-substitution-gets-no-verdict-from-the-server-side-classifier` (`clustered`, then `archived` by the cascade under an `actioned` Insight; `cleanup` moved it to the archive).
  - insights: 1 updated: `insight-hi-skill-substitution-checked-by-a-model-call` (child added, `addressed_by` 246 → 439, `actioned` kept).
  - entities: none changed.
- Governed files `render` rewrote: `vault/wiki/case-schema.md`, `.claude/agents/case-guppi.md`, `.claude/skills/pre-spec/SKILL.md`. `guppi sprint` and `guppi glossary` changed nothing.

## Readings due

30 Estimates stand `pending` or `failed` after `generate`: 4 `failed`, 26 `pending`.

- `estimate-case-protocol-case-form` — `failed` — `rule-case-protocol` draft — by hand, the Cases of a session at its close (method). Result: the context of Case 439 and of Case 441 shown again holds bullet lists, not prose, and the given of 441.4 holds the state "deferred by case 438".
- `estimate-case-protocol-defers-in-one-reply` — `failed` — `rule-case-protocol` draft — by hand, the first defer the person asks for after the render (method). Result: Case 442 was shown in the short form, but the agent then edited the plan file to translate its heading, context and problem, and text followed the Frontier in the reply.
- `estimate-agent-writing-followed` — `failed` — `rule-agent-writing` draft — by hand, the section in `CLAUDE.md` and one reply against it (method). Result: the Work Mode report says 10 Estimates wait where the ledger names 12, and the retro reply announces "three more" and lists two.
- `estimate-language-followed` — `failed` — `rule-language` draft — by hand, the section in `CLAUDE.md`, the session's commit, Spec and chat (method). Result: Case 441 was shown in the chat with its name, context, problem and recommend in English, and the agent's Russian text transliterates hook, commit, skill, insight and Case.
- `estimate-materialize-lifts-a-create-by-the-schema` — `rule-materialize` draft — `raw/2026-09-26/1745/spec.md` line 96.
- `estimate-materialize-assembles` — `rule-materialize` draft — `raw/2026-09-26/1745/spec.md` line 132.
- `estimate-case-build-writes-the-case` — `rule-case-build` draft — `raw/2026-09-26/1745/spec.md` line 240.
- `estimate-case-protocol-shows-the-built-case` — `rule-case-protocol` draft — `raw/2026-09-26/1745/spec.md` line 287; `raw/2026-09-26/1337/spec.md` line 163.
- `estimate-case-check-shows-only-the-checked-case` — `rule-case-check` draft — `raw/2026-09-26/1745/spec.md` line 335.
- `estimate-prespec-reconciles` — `rule-prespec` draft — `raw/2026-09-26/1745/spec.md` line 381.
- `estimate-prespec-checks-the-ratified-copy` — `rule-prespec` draft — `raw/2026-09-26/1745/spec.md` line 413.
- `estimate-spec-write-reaches-the-approved-spec` — `rule-spec-write` draft — `raw/2026-09-26/1745/spec.md` line 479.
- `estimate-spec-write-removes-a-superseded-case` — `rule-spec-write` draft — `raw/2026-09-26/1745/spec.md` line 537.
- `estimate-spec-write-copies-the-ratified-case` — `rule-spec-write` draft — `raw/2026-09-26/1745/spec.md` line 590; `raw/2026-09-26/1337/spec.md` lines 232 and 436.
- `estimate-spec-write-checks-the-written-case` — `rule-spec-write` draft — `raw/2026-09-26/1745/spec.md` line 626.
- `estimate-spec-capture-appends` — `rule-spec-capture` draft — `raw/2026-09-26/1745/spec.md` line 659.
- `estimate-case-check-sends-back-a-faulty-case` — `rule-case-check` draft — `raw/2026-09-26/1337/spec.md` lines 107 and 368.
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

1. `insight-case-show-built-case-retyped-by-hand` — severity 2 — The main agent writes the Case that case-guppi built out again by hand instead of copying the answer, so a showing can differ from the answer in any line, and only the comparison on Stop stands between the retyped Case and the person. Proposal: let the showing of a built Case not pass through the agent's retyping, or let the comparison on Stop also refuse a second showing that differs. Briefs: 2.
2. `rule-spec-reconcile` — deferred by Case 423: a guard that refuses the agent's edits of the plan while a Cases line of the Frontier is open; when and how the prose of a Case is translated. Severity: none. Briefs: 6.
3. `rule-orchestration` — deferred by Case 424: the orchestration of the main agent as a rule of its own loaded by `/hi`, and `case-schema.md` read by `case-guppi` alone. Severity: none. Briefs: 4.
4. `rule-ledger-write` — deferred by Case 442: a lesson line whose cause a Case of the same session closed carries `addressed_by`, or the decision line carries `addresses`; nothing catches a missing mark. Severity: none. Briefs: 1.

The item `rule-prespec` (deferred by Case 438) is retired: 441.4 carries `{supersedes:case 438}`. The open Insight `insight-workflow-code-live-before-the-page-it-reads` is named by the sprint page, so it is not listed here.

## Flags

- `incomplete`, `failed`, `unparsed`: none in the yamls of 1337 and 1745.
- `near`, this run: none. From the earlier run: `raw/2026-09-26/1337/materialize.yaml` line 19, `lesson-hooks-subagentstop-fires-before-and-after-the-handback` near `lesson-hooks-subagentstop-exit-2-sends-the-subagent-back`; line 20, `lesson-case-show-ref-of-a-ratification-line-retyped` near `lesson-case-show-sub-case-ratification-retyped`.
- Synthesis: `lesson-hi-substitution-gets-no-verdict-from-the-server-side-classifier` clustered into `insight-hi-skill-substitution-checked-by-a-model-call`, which stood `actioned` by Case 246. The lesson entry carries `addressed_by: decision-case-439`; 439 is later than 246, so the update sets `addressed_by: decision-case-439` and keeps `actioned`. The cascade archived the lesson. `lesson-case-build-a-criterion-replaced-whole-drops-a-line` has no pair and stays `new`.
- Contradiction: the Pattern and Proposal of `insight-hi-skill-substitution-checked-by-a-model-call` name a lapsed login as the cause and `/login` as the cure; the Root cause of `lesson-hi-substitution-gets-no-verdict-from-the-server-side-classifier` and Case 439 say the server-side classifier of client 2.1.282 gives no verdict for a typed substitution, and `/login` did not help (handoff). The Pattern and Proposal stand unchanged.
- Failed Estimates: 4, listed first under Readings due.
- The order the handoff asks: every `replace` pair of `rule-case-protocol` (440.3, 441.2, 441.6, 441.7) and of `rule-spec-write` (441.6, 441.7, 441.8) applied in one run; `generate` printed no line on stderr. `render` rewrote `vault/wiki/case-schema.md`, `.claude/agents/case-guppi.md` and `.claude/skills/pre-spec/SKILL.md`.
- Handoff note: the `/hi` fix (commit 54509ed) was committed before `/hi` and outside a Case, with the owner's consent; Case 439 ratified it after the fact.
- Handoff note: case-guppi found no item with the four keys of the shape before case 189 under `raw/` (Case 440); the agent did not check it.
- Handoff note: Case 441 was ratified, then rebuilt to 441.1–441.10 after pre-spec found ten issues, and ratified again; 441.1–441.6 stand once in the ledger (21:59:07), 441.7–441.10 at 22:27:05.
- Handoff note: pre-spec found three facts in `context` that the vault does not bear out (439: where `ITEM_KEYS` lives, "generate does not rewrite Insights"; 441: "translated, ticks kept"); the agent fixed them as prose in the plan.
- Handoff note: the test names differ from those the Spec task lines give (`raw/2026-09-26/1745/spec.md` lines 92 and 130); the content matches the Cases.
- Handoff note: the by-hand boxes of `raw/2026-09-26/1337/spec.md` line 43 and `archive/migration/2026-09-25/1654/raw/spec.md` line 149 were ticked; both checks held.
- Handoff note: context passed 400 000 tokens during Retro.
- MOC candidates: none named by lint.
- Stale defers, from lint: `rule-subagent-guppi` and `rule-work-mode` have been deferred 31 times since case 29; `rule-morph` once since case 239; `rule-orchestration` once since case 424.
- Backlog moves by `generate`: none printed. Milestones dropped: none printed.
- `archive` (run after the brief): no stdout or stderr line, nothing moved. Both units are dated 2026-09-26, the day of the run, and `archive` looks only at units dated before it; `raw/2026-09-26/1745/` is also the session of the run.
- `generate`, `cleanup`, `render`, `sprint`, `glossary`: no stderr lines. `cleanup` moved 2 pages: `decision-case-438` and `lesson-hi-substitution-gets-no-verdict-from-the-server-side-classifier`, to `archive/migration/2026-09-26/1745/`.
- `make lint`, after the render: exit 2, 100 findings.
  - `decisions/decision-case-N: schema: missing section ## Context` and `## Problem` on 31 pages. That is 62 findings.
  - `rules/rule-spec-box: schema: missing field kind`, `missing field estimates`, and `orphan: no other live page names it in its frontmatter`.
  - `rules/rule-morph: deferred: 1 time since case 239`; `rules/rule-orchestration: deferred: 1 time since case 424`; `rules/rule-subagent-guppi: deferred: 31 times since case 29`; `rules/rule-work-mode: deferred: 31 times since case 29`.
  - `unread: pending` on 26 Estimates and `unread: failed` on 4. These are the 30 Estimates of Readings due.
  - `estimates: unmigrated: 19 pages in the shape before case 193`.

## Next session

Cases:
- `estimate-case-protocol-case-form` failed: bullet lists in `context`, a state in `given` (reading of session 1745).
- `estimate-case-protocol-defers-in-one-reply` failed: the plan edited after a short-form defer (reading of session 1745).
- `estimate-agent-writing-followed` failed: counts in replies that differ from the ledger and from their own lists (reading of session 1745).
- `estimate-language-followed` failed: a Case shown in English in the chat, English terms transliterated (reading of session 1745).
- The Pattern and Proposal of `insight-hi-skill-substitution-checked-by-a-model-call` are contradicted by `lesson-hi-substitution-gets-no-verdict-from-the-server-side-classifier` and Case 439 (handoff, Notes from memory; Flags).

Work:
- `estimate-materialize-lifts-a-create-by-the-schema`
- `estimate-materialize-assembles`
- `estimate-case-build-writes-the-case`
- `estimate-case-protocol-shows-the-built-case`
- `estimate-case-check-shows-only-the-checked-case`
- `estimate-prespec-reconciles`
- `estimate-prespec-checks-the-ratified-copy`
- `estimate-spec-write-reaches-the-approved-spec`
- `estimate-spec-write-removes-a-superseded-case`
- `estimate-spec-write-copies-the-ratified-case`
- `estimate-spec-write-checks-the-written-case`
- `estimate-spec-capture-appends`
- `estimate-case-check-sends-back-a-faulty-case`
- `estimate-case-protocol-ledger-line-form`
- `estimate-context-size-warns-past-the-limit` (the handoff says it is readable from the transcript of session 1745, 400 025 tokens and later)
- `estimate-retro-loads`
- `estimate-retro-report-holds-each-fact-once`
- `estimate-carry-over-writes`
- `estimate-documentation-completes`
- `estimate-session-phases-in-order`
- `estimate-sprint-renders-the-backlog`
- `estimate-synthesis-keeps-actioned-by-the-mark` (this run clustered a marked lesson under an actioned Insight; see Flags, Synthesis)
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-merges`
- `estimate-sprint-migration-rule-class-files-dissolved`
- The unticked boxes of the Specs are the `read` lines of the readings above: `raw/2026-09-26/1745/spec.md` lines 96, 132, 240, 287, 335, 381, 413, 479, 537, 590, 626, 659; `raw/2026-09-26/1337/spec.md` lines 107, 163, 232, 368, 436.
- A check of Case 440: no item under `raw/` carries the four keys of the shape before case 189 (handoff: case-guppi found none, the agent did not check).
- Frontier Work lines W1–W3, W9, W10, W12, W13, W16, W19–W28 and W31 (handoff).
- Ledger lines not applied: none. All 38 lines of `raw/2026-09-26/1745/ledger.md` have an entry, and all are `applied`.

## Readings at the close

- `make test`: 707 passed, 2 skipped.
- `make lint`: exit 2, 100 findings (listed under Flags).
- Pages in `vault/wiki/`: decisions 619, estimates 136, rules 66, lessons 57, insights 24, entities 4.
