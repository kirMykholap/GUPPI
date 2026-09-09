# Brief — 2026-09-09, after Slice 1 session C

**Hand-written by the session that closed Slice 1. No librarian exists yet.** The next
brief is written the same way until Slice 3 delivers the librarian.

## Where things stand

Branch `migration`, eight commits above `main`. Slices 0 and 1 are **closed**. Slice 1's
spec is the second document in `raw/2026-09-09/spec.md` (cases 9–13); its ledger lines are
in `raw/2026-09-09/ledger.md`: the sixteen decision lines and three lesson lines of sessions
A and B by hand, everything from session C on by the hook.

**Built:** `uv run guppi event` (`SessionStart`, `PostToolUse`) and `uv run guppi ledger`
(`Stop`). The ledger hook lifts the `- decision[`, `- estimate[` and `- lesson[` lines of a
```` ```LEDGER ```` block in the finished reply into `raw/<date>/ledger.md`, each prefixed
with the time of writing (`- HH:MM:SS decision[...]`); lines anywhere else are previews. It
refuses with exit 2 and a reason when no `hi` follows a `session-start` of this session;
`compact` and `resume` of the same session keep the window open. A line already present,
with or without a time, is not written twice. `make test`: 32 green.

**Measured:** all eight Estimate pages of Slice 1 are `passed`, filled by hand.
`estimate-ledger-write-lifts` has two live readings, one under each contract.

**Decided in session C** (cases 14–17, all `update`): the `hi` window survives
`compact`/`resume` (14); a record is a LEDGER block, not a bare line (15.1); a Case renders
as `## Case N — name` plus one blockquote per section, sub-cases as `###` (17, replacing
15.2); each ledger line carries the time (15.3); the two Estimate criteria that quoted the
bare-line contract were rewritten (16.1, 16.2).

## What the next session does — Slice 2

Slice 2 per `sprint.md`: renderer, lint, indexes, `/ask`, pre-task. Its own Plan Mode and
its own approval; the approved plan is copied to `raw/<date>/spec.md`. Candidates for the
Frontier, in the order the plan suggests:

1. **Harness renderer** (`migration-plan.md`, Phase 1): reads every Rule page with
   `enforcement: render`, writes `## Render` into the file named by `governs` — `full`
   replaces, `partial` splices between `<!-- slug -->` markers. Today four rule pages and
   `.claude/skills/hi/SKILL.md`, and `rule-case-protocol` and `CLAUDE.md`, are two copies
   of one text kept identical by hand. Includes the deferred `rule-hook-registry`
   (`render: full` → `.claude/settings.json`).
2. **`rule-plan-mode`** MOC: `rule-case-protocol` already names it as parent.
3. **C9 by hook**: `PostToolUse ExitPlanMode` copies `tool_response.plan` into
   `raw/<date>/spec.md` (`rule-branch-commit`). The payload is known (lesson line of
   session B).
4. **Lint, indexes, `/ask`, pre-task**: the 35 pages of `vault/wiki/` were written by hand
   against `schema.md`; lint will be their first check.

Free readings at the start: the agent's first reply is a reading of
`estimate-case-protocol-loaded` under its new criterion (states the LEDGER-block rule and
one-Case-at-a-time, no read call). A fresh reading 1 of `estimate-session-start-context`
under the LEDGER form costs one start without `/hi`; optional, the refusal path did not
change.

## Deferred, carried here so it surfaces

- `/grill-me` is kept without a page. Decide at Slice 3 (retro) or Slice 5.
- Rendering `.claude/settings.json` from a Rule page (`rule-hook-registry`, `render: full`).
  Slice 2; until then the three hook registrations are hand-written.
- `origin` points at the product repository (`c:/PROJECTS/job hunt ai`) and `migration`
  has no upstream; `git pull --ff-only` in `/hi` fails visibly and harmlessly. Owner's
  decision 11.1: leave until Slice 5.
- `gh` is not logged in and there is no GitHub remote; `gh issue list` in `/hi` prints its
  own message. Owner's decision 11.2: leave until a remote exists.
- Estimate pages are updated by hand (`status`, `## Result`, `History`) until Slice 3's
  generator; `log.md` likewise.
- C9 by hook: Slice 2, item 3 above.
- The fate of `vault/parked/`, `vault/archive/`, `docs/superpowers/`, `docs/HANDOFF.md` and
  the 2026-08 documents under `docs/`. Slice 5.

## Known false, and left so on purpose

- `rule-case-protocol` has `parent: rule-plan-mode`; that page arrives with Slice 2.
- Until Slice 2's renderer the skill file and the four rule pages, and the render block of
  `rule-case-protocol` and `CLAUDE.md`, are two copies of one text kept identical by hand.
  Checked identical by `diff` at the close of session C.
- `docs/migration/rule-*.md` carry `origin: TBD`, `sprint: TBD`, `created: TBD`. They are
  drafts, not pages; the drafts stay until Slice 5.
- `docs/migration/migration-plan.md`, Phase 1 item 4, says hand-written and hook-written
  ledger lines must be indistinguishable. Case 15.3 made them distinguishable by design:
  the hook's lines carry a time. The plan is a draft and is corrected at Slice 5.
- The `hi` line in `event_log.md` has no session id: `CLAUDE_SESSION_ID` does not reach a
  `!` substitution (measured session B: `unset`). The two-sessions limit of
  `rule-event-log` stands.
- The one lesson line of session C is written by the hook after the closing commit, so it
  sits in `ledger.md` uncommitted until the next commit.

## Readings at the close of session C

- `find vault/wiki -type f | wc -l` → 35.
- `make style` → clean; `make test` → 32 passed.
- Ledger tail: cases 15.1–15.3, 14, 16.1, 16.2, 17 written by the hook with times, once each.
