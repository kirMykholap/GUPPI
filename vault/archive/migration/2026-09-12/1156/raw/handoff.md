# Handoff — 2026-09-12, session J: the Estimate derived from the Case; one Spec per session

## Notes from memory

- Case 70 (delete a lesson under an `open` Insight): the owner accepted with the caveat
  in its `given` — the schema has no state for a lesson found wrong; the Insight
  `insight-ledger-hook-reads-only-the-final-text` is yours to judge, its Proposal was
  already the behaviour of case 55.2.
- Case 71.1 was ratified in the old form, before 72; the owner's question "shouldn't
  this be mechanical?" became Case 72. 72 settles: one Leaf, one Estimate; Criterion =
  `when` + `then` block by Case; Context = `problem` once at birth; the agent writes
  `method` on a create and `contract: same|changed` on an update, nothing else; a second
  Estimate on one target only by case 53.2 with a named slug. The owner chose "append a
  block per Case" over "replace the whole criterion".
- Case 72's own `then` items carry explicit `update`s of five Estimates and no
  `contract`, so the scheme applies from Case 73 on; the new `pretask --check` prints five
  "update <rule> has no contract" findings for 72 — the transition, not a defect.
- Case 73: the session folder is named by the `hi` time (`0454`, `1156`); the owner
  chose it over a session letter.
- The field names `estimate_kind` and `estimate_slug` in the `then` item were the
  agent's resolution of a fork (72.1 says `kind`, `slug`); deferred as Case 81.
- The owner asked why pre-task findings appeared after approval; answered: the second
  run was the new code of 72.5 on the same Spec. He wants nothing done about the
  ExitPlanMode hook gating on the `pretask` line rather than on the check's result.
- Cases 78, 79, 80 defer 3b, 3c and the ask-guppi archive again (postponed 5, 4, 5
  times).

## Direct instructions to the librarian

1. Your inputs moved (case 73): this file is `raw/2026-09-12/1156/handoff.md`; the Spec
   of this session is `raw/2026-09-12/1156/spec.md`; session I's Spec, frontier and
   handoff are in `raw/2026-09-12/0454/`. `guppi materialize` (73.5) reads both Specs of
   the date; the yaml of 2026-09-12 exists with 85 applied entries and is extended.
   Session I's librarian report is in the brief; do not redo it.
2. Before `generate`, three entry edits, each one judgment:
   a. The derived update of Case 73.10 (`rule-claude-md`, `contract: changed`) has
      `slug: null`, `incomplete: [estimate]`: the page had `estimates: []` when
      materialize ran, and its Estimate `estimate-claude-md-rendered` is created by
      71.1 earlier in the same yaml. Set `slug: estimate-claude-md-rendered` on that
      entry.
   b. The derived update of Case 73.3 (`rule-skill-hi`) takes the first slug of the
      page's `estimates`, which is `estimate-hi-no-read-calls`; the Estimate that
      checks the Frontier file is `estimate-hi-writes-frontier` (case 59.2). Set the
      entry's `slug` to `estimate-hi-writes-frontier`.
   c. The knowledge lesson `lesson-hooks-blocked-pretooluse-leaves-no-posttooluse-event`
      is marked `incomplete: [source]` though its line carries `{source:...}`
      (`lesson-materialize-lesson-line-source-dropped`, deferred as Case 82). Set
      `fields.source` on its entry from the line. The page of session I's
      `lesson-subagents-parallel-on-one-tree-red-mid-flight` lacks `source` for the same
      reason; its entry is applied — name it in the brief, do not edit the page.
3. Expected in the yaml: 21 derived entries (73.2–73.10, 74, 75.1, 75.2, 76 append
   `### case N` blocks to their Estimates and set them `pending`; 77 is `contract: same`
   and derives nothing); 8 `remove_criterion` entries for the `supersedes` lines — they
   supersede defers (63, 64, 65, 67, 68, 69), no Estimate holds a block, generate
   prints "no Estimate holds a block" and applies; 12 `file` entries `incomplete: [then]`
   (Rule-class files applied by hand in Work Mode, as in session I); 30 `unparsed` lines
   of session I (the wrong-form lines, the trace; the brief said 33 — the file holds
   30).
4. Case 70 deletes `lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn`;
   `insight-ledger-hook-reads-only-the-final-text` keeps it in `children`, lint recounts
   severity to 1. Judge the Insight at synthesis: its second member is gone, its
   Proposal was already the code.
5. New lessons to compare at synthesis:
   `lesson-ledger-preview-in-ratification-taken-for-the-record` (against the children
   of `insight-ledger-line-written-unchecked`);
   `lesson-pretask-nested-estimate-exempt-from-the-line-check` (same Insight, or
   `insight-workflow-contract-change-leaves-its-derived-text-stale`);
   `lesson-estimates-live-clause-stale-at-first-render` (a recurrence of
   `lesson-estimates-criterion-stale-after-contract-change` — the Insight
   `insight-workflow-contract-change-leaves-its-derived-text-stale`);
   `lesson-materialize-lesson-line-source-dropped`;
   `lesson-hooks-blocked-pretooluse-leaves-no-posttooluse-event` (knowledge).
6. Duplicates to check: 71.1 creates `estimate-governed-files-hook-refuses` and
   `estimate-claude-md-rendered` as standalone creates with `ref`; no derived create
   competes with them. The derived slug rule would have named them
   `estimate-governed-files-hook` and `estimate-claude-md`; the ratified names stand.
7. Do not run `guppi render`: the six governed files (`CLAUDE.md`, four skills, your own
   agent file) change at the next session's first render; `make lint` will stop at
   `render --check` after your run — expected, say so in the brief.
8. `sprint.md`: do not touch.
9. Readings the next session takes against your report: `estimate-generate-writes`
   (the live half), `estimate-documentation-completes`, `estimate-synthesis-clusters`;
   at its start: `estimate-case-protocol-loaded`, `estimate-render-sync-reports`.
10. For the brief's Deferred list: Cases 78 (3b), 79 (3c), 80 (ask archive), 81 (field
    names), 82 (lesson source), 83 (guard refusal in the event log), 84 (the live
    clauses of the two render readings). Two notes for the next Plan Mode that are not
    defers: `index.md` §4 still says `ref` is omitted on `update`/`delete` while every
    line carries it; `case-schema.md` had two `raw/<date>/spec.md` mentions changed to
    the session folder by the Work Mode agent beyond the literal `change` lines of 73.

## What actually got done

- Commits: `e43c9e4` the render of six harness files (brief, next 1); `16b7f58` Cases
  72–76 — materialize (72.3, 73.5, 76), generate (72.4), pretask/spec/ledger (72.5,
  73.2, 73.4, 74, 75.2; `session_dir` lives in `guppi/ledger.py`, not `event.py`, an
  import cycle), lint (72.6), the ledger test of 70, seven Rule-class files (72.1,
  72.2, 73.1, 75.1), the one-off of 73.1; `90bdd36` the Retro.
- `make test` 258 green, `make style` clean, `guppi lint` 129 findings as before,
  `render --check` exit 0 before your run.
- Ratified: 70, 71.1, 72.1–72.6, 73.1–73.10, 74, 75.1, 75.2, 76, 77. Deferred: 78–84.
- Readings passed: `estimate-hi-writes-frontier`, `estimate-materialize-assembles`,
  `estimate-pretask-reconciles`, `estimate-lint-catches`. Failed on a clause, not on
  the code: `estimate-governed-files-hook-refuses`, `estimate-claude-md-rendered`,
  `estimate-render-harness-reproduces` (Cases 83, 84).
- Not done: the render of the governed files by 72.1, 73.x, 74, 75 (next session
  start); the five readings of item 9; the Spec's 15 unticked tasks are all of that
  kind.
- The next session does first: `uv run guppi render`, commit; the readings; Plan Mode
  over the deferred list.
