# Brief — 2026-09-09, after Slice 1 session A

**Hand-written by the session that ran Slice 1's first part. No librarian exists yet.**
The next brief is written the same way until Slice 3 delivers the librarian.

## Where things stand

Branch `migration`, four commits above `main`. Slice 0 is closed. Slice 1 is **open, one
session of three done**: its spec is the second document in `raw/2026-09-09/spec.md`
(cases 9–13), its sixteen decision lines are in `raw/2026-09-09/ledger.md`, written by
hand at ratification.

**`vault/wiki/` holds its first sixteen pages**: eight Rules (`rule-session-start`,
`rule-skill-hi`, `rule-internal-context`, `rule-git-context`, `rule-github-issues`,
`rule-event-log`, `rule-ledger-write`, `rule-case-protocol`) and their eight Estimates, all
`draft` / `pending`.

**Built:** `guppi/` with `uv run guppi event` (the event log) and `uv run guppi probe`
(throwaway); `.claude/settings.json` registers `SessionStart` and `PostToolUse` on
`guppi event`, `Stop` and `PostToolUse ExitPlanMode` on `guppi probe`; the `/hi` skill;
the Case protocol section in `CLAUDE.md`; `make test` (pytest, 14 green).

**Not built:** `guppi ledger`, the `Stop` hook. It waits on the probe below. Until it is
registered, ledger lines are still written by hand, in the same format.

**Already measured, this session:** a `PostToolUse` hook added to `settings.json` fires on
the next tool call without a restart, and `guppi event` receives the real `session_id`
(`event_log.md` carries `1cee6ce3 tool Write: …` lines). `uv run guppi` needs the project
installed — `uv sync` after a fresh clone, and a `[build-system]` block in
`pyproject.toml` (uv's own backend, build-time only).

## What the next session does — Slice 1, session B

**The owner, before opening Claude Code:** nothing. Then, in the new session:

1. Type `/hi`. It records itself in the event log and prints a `Probe:` line with
   `CLAUDE_SESSION_ID` or `unset`.
2. Make one tool call of any kind, enter Plan Mode, exit it with a trivial plan, and let
   the agent reply. `raw/2026-09-09/probe-Stop-1.json` and `probe-PostToolUse-1.json`
   appear (gitignored).

**The agent, in that session** (spec.md, "Сессия B"):

- Read the probe files. Record the readings as two `- lesson[knowledge][…]` lines — by
  hand into the ledger, the hook does not exist yet: `lesson-hooks-stop-payload`
  (which field carries the reply; whether `stop_hook_active` is present; whether a
  `Stop` registration needed a restart) and `lesson-hooks-exitplanmode-payload` (does
  `tool_input` carry the plan text, C9).
- Take the readings of `estimate-hi-no-read-calls`, `estimate-internal-context-loaded`,
  `estimate-git-context-current`, `estimate-github-issues-listed` from this very start,
  and of `estimate-event-log-records` (`git check-ignore`, timing through a pipe).
- Write `guppi/ledger.py` and `tests/test_ledger.py` to the contract of case 10, on the
  branch the probe confirmed. Remove `guppi/probe.py`, the probe files, the `Probe:` line
  from the skill and the `ExitPlanMode` registration; register `Stop` →
  `uv run guppi ledger`. If `CLAUDE_SESSION_ID` was `unset`, the skill text stays as it
  is and the two-sessions limit in `rule-event-log` stands.
- Fill the measured Estimates' pages (`status`, `## Result`, `History`) by hand.
- `make style`, `make test`, commit. Rewrite this brief for session C: one start without
  `/hi` (the hook must refuse a bare decision line and say why), one with `/hi` (the hook
  must write the `estimate[...]` lines itself — item 5 of the definition of done).

## Deferred, carried here so it surfaces

- `/grill-me` is kept without a page. Decide at Slice 3 (retro) or Slice 5.
- Rendering `.claude/settings.json` from a Rule page (`rule-hook-registry`, `render: full`).
  Decide in Slice 2; until then the three hook registrations are hand-written.
- `origin` points at the product repository (`c:/PROJECTS/job hunt ai`) and `migration`
  has no upstream; `git pull --ff-only` in `/hi` fails visibly and harmlessly. Owner's
  decision 11.1: leave until Slice 5.
- `gh` is not logged in and there is no GitHub remote; `gh issue list` in `/hi` prints its
  own message. Owner's decision 11.2: leave until a remote exists.
- Estimate pages are updated by hand (`status`, `## Result`) until Slice 3's generator.
- The fate of `vault/parked/`, `vault/archive/`, `docs/superpowers/`, `docs/HANDOFF.md` and the
  2026-08 documents under `docs/`. Slice 5.

## Known false, and left so on purpose

- `rule-case-protocol` has `parent: rule-plan-mode`; that page arrives with Slice 2.
- `rule-ledger-write` lists `guppi/ledger.py` in `implementation_ref`; the file arrives
  with session B.
- `.claude/skills/hi/SKILL.md` carries a `Probe:` line that is not in `rule-skill-hi`'s
  `## Render`; it leaves with the probe. Until Slice 2's renderer the skill file and the
  four rule pages are two copies of one text, kept identical by hand.
- `docs/migration/rule-*.md` carry `origin: TBD`, `sprint: TBD`, `created: TBD`. They are
  drafts, not pages; `rule-session-start` now has a real page and the draft stays until
  Slice 5.

## Readings at the close of session A

- `find vault/wiki -type f | wc -l` → 35.
- `make style` → clean; `make test` → 14 passed.
- `git check-ignore vault/raw/2026-09-09/event_log.md` → ignored.
