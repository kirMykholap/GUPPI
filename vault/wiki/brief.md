# Brief — 2026-09-09

**Hand-written by the session that ran Slice 0. No librarian exists yet, so no ingest produced
this.** The next brief is written the same way until Slice 3 delivers the librarian.

## Where things stand

The repository is on branch `migration`, three commits above `main` (`047a612`, tagged
`vault-v1` at the split from the product). Slice 0 of the migration plan is closed: the layout
of `vault/wiki/index.md` §1 exists, the model's documents live in the vault, the old harness is
gone, and the sprint `migration` is open in `sprint.md`.

**`vault/wiki/` holds no page.** Six categories, each with `schema.yaml` and `schema.md`, four
registers, three top-level documents. The first pages arrive with Slice 1.

**The old vault is parked, not retired**, under `vault/parked/2026-09-09/` (entities 44, rules
35, lessons 31, proposals 52, and the eight old registers) and `vault/parked/2026-09-07/`
(decisions 218, concepts 147, and four product pages). `vault/archive/` is the old archive,
untouched. Slice 4 converts entities, rules and lessons by group; proposals stay parked
(decision D2).

**The decisions of 2026-09-09** are the nine lines of `vault/raw/2026-09-09/ledger.md`, with
their content in `spec.md` beside it (the approved plan, D1–D8 and C1–C14). Their Decision pages
do not exist yet: the generator that writes them is Slice 3's.

## What the next session does — Slice 1

Open Plan Mode and plan Slice 1 from `docs/migration/rule-session-start.md` and the roadmap in
`raw/2026-09-09/spec.md`:

1. The Python package `guppi/` with a CLI (`uv run guppi …`) and the pytest suite beside it.
2. `guppi event` — the event log, `raw/<date>/event_log.md`, gitignored.
3. `guppi ledger` — the `Stop` hook that lifts `- decision[...]`, `- estimate[...]` and
   `- lesson[...]` lines out of the finished reply into `raw/<date>/ledger.md`, refusing with a
   reason when no `/hi` was recorded. **Probe the `Stop` payload first** (does it carry the last
   assistant message, or only `transcript_path`?) with a throwaway hook, as the old vault's
   lesson on probe hooks teaches; do not trust the documentation on this.
4. The `/hi` skill, recording its own invocation through a `!` substitution, loading
   `sprint.md`, `brief.md`, git state and open issues.
5. The Rule pages that describe all of the above — `rule-session-start` and its children — written
   by hand into `vault/wiki/rules/`, each with its Estimate. They are re-rendered by Slice 2's
   renderer; until then the skill file and the rule page are two copies, for one session.
6. `CLAUDE.md` gains the Case protocol section (`rule-case-protocol`), by hand, same caveat.

## Deferred, carried here so it surfaces

- `/grill-me` is kept without a page. Decide at Slice 3 (retro) or Slice 5.
- Rendering `.claude/settings.json` from a Rule page (`rule-hook-registry`, `render: full`).
  Decide in Slice 2, when the renderer exists.
- `PostToolUse ExitPlanMode`: does its payload carry the plan text? Needed for the hook that
  copies the approved plan into `raw/<date>/spec.md` (C9). Check in Slice 2.
- The fate of `vault/parked/`, `vault/archive/`, `docs/superpowers/`, `docs/HANDOFF.md` and the
  2026-08 documents under `docs/`. Slice 5.

## Known false, and left so on purpose

- `docs/migration/rule-*.md` carry `origin: TBD`, `sprint: TBD`, `created: TBD`. They are
  drafts, not pages; each gets real values when it becomes a page in `vault/wiki/rules/`.
- The old harness's own lessons (31, parked) describe hooks that no longer exist. They are
  still the record of what burned; Slice 4 decides which survive as Lessons of the new model.

## Readings at the close of Slice 0

- `find vault/wiki -type f | wc -l` → 19.
- `ls .claude` → `settings.json`, `skills/` (holding `grill-me` only).
- `make style` → clean, over no Python.
