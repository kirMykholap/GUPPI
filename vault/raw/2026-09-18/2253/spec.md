<!-- approved 23:05:30 · session 757fff5b -->

# Spec — 2026-09-18, session 2253

## Work Mode on the conserved Spec of session 2054

The Spec `vault/raw/2026-09-18/2054/spec.md` was ratified and approved in session 2054 and
conserved by `/carry` (`carry.md` marks the folder). This session does its work; no Case
of it is ratified again. Its `tasks` blocks are the executable plan; Work Mode ticks the
boxes in `vault/raw/2026-09-18/2054/spec.md`, not here.

Order of work, test first, each test red then green:

1. Case 250.1 — `guppi/render.py`: `applied_whole` counts an entry with `superseded_by`
   as done, an entry with `failed` or with neither mark as not; `tests/test_render.py`:
   a yaml with a superseded entry is ticked, one with an unmarked entry is not.
2. Case 250.2 — one shared helper that ticks the unticked task lines opening with a code
   span holding a given command, in the `spec.md` of every unit under `raw/` whose yaml is
   applied whole and that carries no `carry.md`; `render` calls it with `guppi render`,
   `sprint` with `guppi sprint` after the plain write exits 0; `tests/test_sprint.py`:
   the tick, `--check`, a later code span, an unapplied unit, a carried-over unit.
3. Case 253.1 — by hand: the sentence of the Spec paragraph in `vault/wiki/case-schema.md`
   and the `spec.md` line of §1 in `vault/wiki/index.md` — `generate`, `render` and
   `sprint` tick the page, render and sprint lines (cases 226, 250).
4. `make style`, `make test` green.
5. Delete `vault/raw/2026-09-18/2054/carry.md`; the commit of this session takes the
   modified `vault/raw/2026-09-18/2054/ledger.md` (the estimate line of
   `estimate-carry-over-writes`, written after the commit of `carry`).
6. `/retro`, `/handoff`, the librarian: `materialize` on 2054 and 2253, `generate`,
   `render`, `sprint`, `cleanup`, brief, commit.

Readings of the 2054 Spec: `estimate-render-harness-ticks-the-spec` and
`estimate-sprint-ticks-the-spec` after the librarian's run; `estimate-case-protocol-loaded`
at the first turn of the next session; `estimate-retro-loads` at the first live `/retro`
after the render.

```tasks
- [x] the tasks of `vault/raw/2026-09-18/2054/spec.md`, Cases 250.1, 250.2, 253.1, 253.2, ticked there
- [x] delete `vault/raw/2026-09-18/2054/carry.md`
- [x] commit `vault/raw/2026-09-18/2054/ledger.md` with this session
```

## Deferred

## Case 254 — `rule-work-mode`, `rule-subagent-guppi`: Slice 3b to the next session

> **context:**
> `rule-work-mode` and `rule-subagent-guppi` are the two items of Slice 3b, the current milestone, both placeholders in `draft`; the draft of Work Mode stands in `docs/migration/rule-work-mode.md`. Deferred by 183, 206, 218, 231, 242, 248 and 252; `deferred_by` on their pages ends at 248 until the librarian applies the ledger of 2054. Since case 245 the item of `rule-work-mode` on the sprint page also names `insight-workflow-code-live-before-the-page-it-reads`, whose sentence enters the rule; the defer of 238 on that Insight, without a `purpose`, closes with the Slice. This session takes F4 and F1 — Work Mode on the conserved Spec of 2054, then `/retro`, `/handoff`, the librarian.

> **problem:**
> Slice 3b is a whole session's work: the body of two rules, their Estimates, the code of Work Mode. This session goes to the work of the 2054 Spec; Slice 3b stays the first item of the next session.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: Slice 3b, the first item of the next session — the body of Work Mode with the sentence of the Insight on a check that reads a page the same Spec changes
  - slug: rule-subagent-guppi
    type: rule
    purpose: Slice 3b, with rule-work-mode — what a subagent may do in Work Mode, and the fork that comes back as a Case
```
