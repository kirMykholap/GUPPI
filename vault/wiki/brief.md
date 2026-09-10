# Brief — 2026-09-10, after Slice 3 session E

**Hand-written by the session that built Slice 3, for the last time.** The librarian
exists since this slice and writes the next brief; its first run is what the next session
does first.

## Where things stand

Branch `migration`, eleven commits above `main`. Slices 0–2 are closed. Slice 3 is
**built, not closed**: every script, page and skill exists, `make test` is 126 green, but
the librarian has never run and `/retro` and `/handoff` were never invoked. Its Spec is
`raw/2026-09-10/spec.md` (Cases 29–41, copied by the hook); its ledger lines were all
written by the hook; its pages were all written by `guppi generate`, none by hand.

**Built in Slice 3:** `uv run guppi materialize` (ledger + Spec → `raw/<date>/
materialize.yaml`, extends an existing yaml), `guppi generate` (pages, backlinks, History,
`log.md`, `tags.md`, one Decision page per Case, lesson-born Estimates, the `built`
cascade), `guppi cleanup` (archived pages → `vault/archived/<sprint>/<date>/<category>/`,
restores, rebuilds the indexes), `guppi gate` (`PreToolUse Skill`, refuses `/handoff` on a
dirty tree), the agent `.claude/agents/librarian-guppi.md`, the skills `/retro` and
`/handoff`, MOCs `rule-documentation`, `rule-harness`, `rule-end-of-work`, `make
test-documentation`, `make test-harness`, `make test-end-of-work`. The Case has seven
sections (Case 34), the `then` block lives in the Spec, a `create` line carries `{tags}`.

**Measured:** `materialize-assembles`, `generate-writes`, `cleanup-moves`,
`render-harness-reproduces`, `harness-pipeline`, `pretask-reconciles`,
`pretask-hook-gates`, `spec-capture-appends` are `passed`. The gate refused `/handoff` on
the dirty tree at the end of session E (`retro-commit-gates`, live part).

## What the next session does first

1. **Run the librarian.** `/retro` (the person), commit, then `/handoff` from Retro: it
   dispatches `librarian-guppi` with `Materialize 2026-09-11.` The 2026-09-10 yaml is
   fully applied; the librarian's own run materializes the next session's ledger. Read
   `documentation-completes`, `index-check-merges`, `synthesis-clusters`,
   `brief-written`, `close-commits`, `retro-loads`, `handoff-dispatches`,
   `end-of-work-order`; each is one `estimate[...]` line, written by the main agent from
   the librarian's report.
2. **Synthesis has material:** `lesson-agents-loaded-at-session-start` (D) says a rendered
   agent is usable only from the next session; `lesson-agents-visible-in-session` (E) says
   the opposite was observed. Same area, contradicting claims: the librarian's first
   judgment.
3. Then Slice 3b or Slice 4 per `sprint.md`; the owner chooses.

## Deferred, carried here so it surfaces

- **Slice 3b: Work Mode** — `rule-work-mode`, `rule-subagent-guppi` (placeholders,
  `draft`, red at lint until then), `to-executable-plan`, the four hooks. Case 29.
- **Archive in `ask-guppi`:** a named slug checked against `vault/archived/`. Case 31
  discussion; decide when the archive holds something.
- `/grill-me` is kept without a page. Slice 3b or 5. (postponed 3 times)
- `origin` points at the product repository and `migration` has no upstream; `git pull` in
  `/hi` fails visibly. Owner's decision 11.1: leave until Slice 5. (postponed 3 times)
- `gh` is not logged in and there is no GitHub remote. Owner's decision 11.2. (postponed 3 times)
- The fate of `vault/parked/`, `vault/archive/` (the old one, 505 files, beside the new
  `vault/archived/`), `docs/superpowers/`, `docs/HANDOFF.md`, `docs/migration/rule-*.md`
  and the 2026-08 documents under `docs/`. Slice 5. (postponed 2 times)

## Flags — what `make lint` prints today, 159 lines, all known

- **Decision pages of Cases 1–30 have no `## Context`, `## Now`, `## Problem`** (and
  Cases 1–8, 28, 30 no `## Then`): their Specs predate the seven-block form, so
  `materialize` put the whole Case text under `Then` or found none. Debt of the
  backfill, not of the model; a Case to accept it as is or to archive them.
- **Nine lessons and their nine Estimates carry no `tags`;** five `knowledge` lessons
  carry no `source`. A lesson line carried no tags before Case 34; the sources sit in
  the Trigger text. One `update` Case with `set` fixes all eighteen.
- **`[delete][old-harness]` of case 6** names no page and no category; `generate` reports
  it on every run. Decide: a `file` route to `docs/harness-map-2026-09-07.md`, or leave.
- **Two placeholders** (`rule-work-mode`, `rule-subagent-guppi`): no `kind`, `estimates`,
  `tags`; orphans. Slice 3b fills them.
- `estimate-render-harness-reproduces` kept its D Result: the 36.2 reading is in the
  ledger only, since a page already `passed` with a Result is skipped by design.
- `docs/migration/rule-documentation.md` and `rule-end-of-work.md` are superseded by
  pages; `rule-work-mode.md`, `rule-subagent-guppi.md`, `rule-plan-mode.md`,
  `rule-session-start.md` stay as drafts until Slice 5.
- `raw/2026-09-09/ledger.md` has mixed line endings; git normalizes on commit.

## Readings at the close of session E

- `find vault/wiki -type f | wc -l` → 160 (58 before the slice).
- `make style` → clean; `make test` → 126 passed.
- `make lint` → 159 findings, the flags above; `render --check`, `index --check` → exit 0.
- `raw/2026-09-10/materialize.yaml`: 77 entries, 21 decisions, none failed, none unparsed.
  `raw/2026-09-09/materialize.yaml`: 74 entries, 34 decisions, one failed (`old-harness`).
