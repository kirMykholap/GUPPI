# Brief — 2026-09-18, after session 2054 of 2026-09-18 (the Spec conserved by `/carry`: sprint ticks its Spec lines, applied whole counts a superseded entry, three tickers named; Slice 3b deferred)

Written by the skill `carry` from `raw/2026-09-18/2054/spec.md`, its `ledger.md` and
`frontier.md`, and the previous brief (after session 1957). No librarian ran: no
`materialize`, `generate`, `cleanup`, `render` or `sprint`; no page of `wiki/` changed.

## Where things stand

- The Spec `vault/raw/2026-09-18/2054/spec.md` is conserved: approved 22:50:13, none of
  its work done. `raw/2026-09-18/2054/carry.md` marks the folder; the session that
  finishes the Spec deletes it. This is the first live `/carry`, the reading of
  `estimate-carry-over-writes` (Flags).
- Its Cases, ratified in session 2054 (11 decision lines in `raw/2026-09-18/2054/ledger.md`):
  - 250.1 — `update` `estimate-render-harness-ticks-the-spec`: a yaml is applied whole when
    every entry carries `applied` or `superseded_by` and none `failed`, as `guppi archive`
    counts it; the Criterion written whole under `sections`, `pending`. Code:
    `applied_whole` in `guppi/render.py`, a test in `tests/test_render.py`.
  - 250.2 — `update` `rule-sprint` (one sentence of Purpose), `create`
    `estimate-sprint-ticks-the-spec` (QA, `ref` `rule-sprint`, tags `harness`, `sprint`):
    `guppi sprint`, once it wrote `sprint.md` and exits 0, ticks every unticked task line
    that opens with a code span holding `guppi sprint` in the `spec.md` of every unit under
    `raw/` whose yaml is applied whole; `--check` and exit 1 tick nothing. Code: one shared
    helper for `render` and `sprint`, tests in `tests/test_sprint.py`.
  - 253.1 — `update` `rule-case-protocol` (Render `replace`), `estimate-case-protocol-loaded`
    (one line of the Criterion, written whole under `sections`, `pending`), and by hand
    `vault/wiki/case-schema.md` and `vault/wiki/index.md` §1: `generate`, `render` and
    `sprint` tick the page, render and sprint lines (cases 226, 250).
  - 253.2 — `update` `rule-retro` (Render `replace`), `estimate-retro-loads` (Criterion
    replaced by the Case's `given`/`when`/`then`, `pending`): a `guppi sprint` line waits
    for the librarian at Retro, not debt.
  - 252 — `defer` `rule-work-mode`, `rule-subagent-guppi` (Slice 3b, `## Deferred` of the
    Spec, a `purpose` per target).
- Not done on the Spec: every task line — the code of 250.1 and 250.2 and their tests; the
  two hand edits of 253.1; every page `update` and the one `create`; the render and sprint
  lines; the four `read` lines (`estimate-render-harness-ticks-the-spec`,
  `estimate-sprint-ticks-the-spec`, `estimate-case-protocol-loaded`, `estimate-retro-loads`).
  Work Mode on the Spec is the next session's first item; then Slice 3b (252).
- Frontier of 2054: 5 items — F2 by case 250, F5 (a pre-task finding) by case 253, F3 and
  F4 as `work`, F1 (Slice 3b) deferred by 252. Case 251 (`rule-skill-hi`: a failed pull or
  an unavailable `gh` whose rule the sprint page names is not a Frontier item) was proposed
  and not ratified: the person waits for Slice 5, the item stays on every Frontier until then.
- Code: none. Tests and `make style` as at the previous commit (`d40a030`): 425 green,
  style clean; `make style` run by `carry` before its commit.
- The previous brief's "Where things stand" (session 1957, the librarian's run of
  `d40a030`) stands as it was: 16 pages written from 1957, 3 archived, the sprint page's
  Slice 3b and Slice 5 items rewritten, `rule-render-harness` and `rule-sprint` `built`.

## Deferred

None. Every candidate is named by the sprint page (case 229.4) or is closed:

- The `defer` of this Spec, case 252: `rule-work-mode` and `rule-subagent-guppi` — the two
  items of Slice 3b, the current milestone; defers 183, 206, 218, 231, 242, 248 and now
  252. `deferred_by` on their pages does not carry 252 until the librarian applies the
  2054 ledger.
- Left out as before, the sprint page names them:
  `insight-workflow-code-live-before-the-page-it-reads` (`open`, severity 2, defer 238
  without a `purpose`; in the text of the `rule-work-mode` item of Slice 3b);
  `rule-git-context` and `rule-github-issues` (defers 220, 243; in the text of the
  `estimate-sprint-migration-merges` item of Slice 5); `rule-spec-box` (defers 207, 219,
  232; Slice 5); `rule-morph` (defer 239; Slice 5).
- Retired earlier: `insight-hi-skill-substitution-checked-by-a-model-call` — `actioned` by
  246, rejected; a third lesson with the same cause reopens it.

## Flags

- The vault does not know session 2054: its 11 decision lines are in
  `raw/2026-09-18/2054/ledger.md` with no `materialize.yaml`; `carry.md` tells
  `materialize` to pass the unit by until the work of the Spec is done and the file
  deleted. No Decision page of 250.1, 250.2, 252, 253.1 or 253.2 exists; `deferred_by` of
  `rule-work-mode` and `rule-subagent-guppi` ends at `decision-case-248`.
- `estimate-carry-over-writes` (`rule-carry-over`, `draft`, `pending`): its live reading is
  this `/carry`. The estimate line is written in the reply after the commit of `carry`, so
  it lands in `raw/2026-09-18/2054/ledger.md` after that commit: the tree is dirty by that
  one file at the end of the session, and the next session's commit takes it. `carry.md`
  keeps the unit out of `materialize` until then; the reading enters the yaml with the
  rest of 2054.
- The Spec's `- [ ] read` lines name where each reading happens:
  `estimate-render-harness-ticks-the-spec` and `estimate-sprint-ticks-the-spec` after the
  librarian's run that follows Work Mode (the 1957 Spec's three `uv run guppi sprint` lines
  37, 103, 137 and this Spec's own sprint line are the place); `estimate-case-protocol-loaded`
  at the first turn of the session after the render; `estimate-retro-loads` at the first
  live `/retro` after the render. None of the four is readable before the Spec's work.
- The flags of the previous brief stand, none resolved by this session: `materialize` on
  `raw/2026-09-18/1252/materialize.yaml` ("line 8 changed since the yaml was written");
  the defer of 238 without a `purpose`; the three `uv run guppi sprint` lines of the 1957
  Spec unticked (their ticker is case 250.2, not yet built); `estimate-hi-no-read-calls` in
  the shape before case 193 by choice; `rule-spec-box` placeholder findings; stale defers
  of `rule-work-mode` and `rule-subagent-guppi` (now 19 since case 29); the 73 lint
  findings of the last run, 62 of them `decisions/decision-case-<1–28>` (Slice 5).
- F3 of 2054: the failed `git pull` and the unavailable `gh` are raised by the text of
  `rule-skill-hi` at every `/hi`; the person chose to leave the rule as it is until Slice 5
  (Case 251 not ratified). The item closes as `work` each session until then; the place of
  its reading stays `estimate-sprint-migration-leftovers-gone` (case 249).
- Handoff flags, each a Case or a task of the next session:
  1. Work Mode on `raw/2026-09-18/2054/spec.md` — Cases 250.1, 250.2, 253.1, 253.2 — then
     delete `carry.md`, `/retro`, `/handoff`, the librarian.
  2. Slice 3b — `rule-work-mode`, `rule-subagent-guppi` (defer 252), with the sentence of
     `insight-workflow-code-live-before-the-page-it-reads` written into `rule-work-mode`.
