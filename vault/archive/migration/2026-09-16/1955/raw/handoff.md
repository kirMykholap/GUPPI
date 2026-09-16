# Handoff — 2026-09-16, Slice 3d closed: case 191 taken up (generate, lint, pre-task by the Estimate model)

## Notes from memory

- The person asked twice for the plain meaning under the Case form: once on what a recut is
  and whether every Estimate goes through it (no: at first touch, 42 pages of the old shape
  remain, counted by lint from now on), once on what Case 204 decides (a written
  `sections: Criterion` wins over the Case's text, on an update as on a create). Both
  answers stand in the chat only; the Cases carry the decisions.
- `{supersedes:case 191}` sits on the `rule-pretask` line of 203.2, the last of the three
  targets, on purpose: one supersedes clears `deferred_by` on all three.
- Case 207 (`rule-spec-box`) was a long conversation, not a Case: parallel Work Mode
  sessions in git worktrees over conserved Specs, the librarian once after the merge. The
  person found it complex; the placeholder's `purpose` holds the whole argument. After 3b.
- The reading of `estimate-case-protocol-loaded` says "the rules were followed, not
  recited": the Criterion asks the agent to state two rules at the first turn, and the
  first turn wrote the frontier instead. Read as passed on behaviour; the person may dispute.
- `estimate-permissions` read `passed` while its Criterion says "eight entries" and lists
  nine. The set holds; the count is the Criterion's own error. An `update` next Plan Mode.
- The four `has no contract` lines `pretask --check` printed on this plan came from the old
  `check_form`; after 203.1 the same plan checks clean (exit 0).

## Direct instructions to the librarian

- Unit `raw/2026-09-16/1955`: 26 decision lines (Cases 201.1–208.3), 14 estimate lines,
  1 lesson line. `materialize --show` over it was run in Work Mode: 26 entries lifted,
  no `incomplete`. Expect the four defer entries of 205–207 to be `exists` for the three
  live targets and a placeholder for `rule-spec-box` (tags `session, workflow, git,
  harness` — all registered).
- `generate` is the new code: an Estimate `update` entry carries `sections.Criterion` and
  `set: {status: pending}` — the whole replacement; the four creates write `purpose`,
  `method`, `tags` as fields, no `## Context`, no `## Method`; the reading lines write
  `checked`. The Decision pages of this session carry no `## Given` and no `## Criterion`
  list. `decision-case-191` becomes `superseded` and archived; `rule-page-generation`,
  `rule-lint`, `rule-pretask` lose `deferred_by`.
- The `replace` texts: 203.2 two in the Render of `rule-pretask`, 208.3 a third in the
  same Render (a later entry of the same unit — applied after 203.2's, the old text stands
  after the first two), 204 one in the Purpose of `rule-materialize`, 208.2 one in the
  Render of `rule-case-protocol`. Every old text was checked verbatim and once by
  `ask-guppi` at pre-task. A `replace` failure on any of them is a flag, not a fix.
- After `generate`: `uv run guppi render` — `CLAUDE.md` (208.2), `.claude/skills/pre-task/SKILL.md`
  (203.2, 208.3); `render --check` exit 0 at the close.
- Index check: the four new Estimates need no index; `rule-spec-box` against the rules
  Grep — `rule-carry-over` is near by design (the box opens a carried Spec), not a
  duplicate. Synthesis: one lesson,
  `lesson-materialize-item-ref-lifted-as-a-page-field` (`error`), against the lesson and
  insight lines; I expect no shared root cause.
- Readings due after this run, for the brief: `estimate-materialize-marks-superseded`
  (this run marks 191's three defer entries `superseded_by: 203.2` — they are applied, so
  `generate` skips nothing new; the Decision page of 191 is set superseded by the record's
  `supersedes`), `estimate-end-of-work-order` (retro → handoff → this run),
  `estimate-brief-written` (the brief you write), `estimate-carry-over-writes` (a live
  `/carry`, not this session). Six recut Estimates go `pending` in this run and were read
  `passed` in the same ledger, later lines: the reading lands after the update, so they
  end `passed`.
- `make lint` at the close: expect ~77 → the 62 of Cases 1–28, 2 `deferred`, `unread` on
  the pages still `pending` (4–5), 1 `method` (`estimate-plan-mode-names-its-estimates`),
  1 `unmigrated` (42 — the six recuts do not set `method` and keep `## Context`/`## Method`,
  see the flags). The body `[[slug]]` finding on `estimate-generate-writes` leaves.
- Flags for the brief, each a Case of the next Plan Mode:
  1. The 13 Estimate pages born of cases 188 and 189 carry a stray `ref` field beside
     `target` (the lesson above); the code is fixed, the pages need a one-off migration.
  2. A recut `update` sets `pending` and the Criterion but not `method`, and drops neither
     `## Context` nor `## Method`: the six pages recut today stay in `unmigrated`. The rule
     of a recut should carry `set: {method: …}` and the two sections dropped by hand.
  3. `estimate-plan-mode-names-its-estimates: method: says by hand while
     estimate-spec-capture-offers-the-fork names a test file` — the MOC clause of 112.1 now
     reads the `method` field; the Estimate is a reading of Plan Mode, not a pipeline over
     the children. Either its `method` names `make test-plan-mode` or the clause changes.
  4. `estimate-permissions`: the Criterion counts eight entries and lists nine.
  5. `sprint.md`: Slice 3d closes with this session — case 191 built; 3b (case 206) next,
     after this session's pages are in place; a line for the recut remainder counted by
     lint (`unmigrated`). Change the Slice 3d clause accordingly.

## What actually got done

- Cases 201–204 and 208 ratified and built in code: `guppi/generate.py` (fields
  `purpose`/`method`/`checked` in order, `checked` from the Result's date, the old
  `criterion_block`/`remove_criterion` paths refused, the Decision page without Given and
  the Criterion list, the docstring by the five promises), `guppi/lint.py` (`unread`, the
  `method` field with the classes test / `pytest` / `make` / reading, `unmigrated` as one
  line), `guppi/pretask.py` (`check_form` by the model), `guppi/materialize.py` (`ref` on
  an Estimate item is the entry's). Tests 397 → 396 (the old-shape tests replaced), all
  green; `make style` clean; `render --check` 0.
- Rule-class by hand: `decisions/schema.md` and `.yaml` (Given and Criterion the shape
  before 201.2), `index.md` §7 and §12, `case-schema.md` two sentences, `estimates/schema.md`
  and `.yaml` (201.1 and 202 instead of 191). `## How it works` dropped by hand on
  `rule-page-generation` and `rule-lint`.
- Cases 205, 206, 207 deferred under `## Deferred` of the Spec.
- 14 readings taken and in the ledger; one lesson.
- Commit `8fd804e` on `migration`.
- Not done: the vault pages of 201–208 (this run), the three renders (this run), the four
  readings named above, the five flags.
