# Brief — 2026-09-09, after Slice 1 session B

**Hand-written by the session that ran Slice 1's second part. No librarian exists yet.**
The next brief is written the same way until Slice 3 delivers the librarian.

## Where things stand

Branch `migration`, seven commits above `main`. Slice 0 is closed. Slice 1 is **open, two
sessions of three done**: its spec is the second document in `raw/2026-09-09/spec.md`
(cases 9–13), its sixteen decision lines and three lesson lines are in
`raw/2026-09-09/ledger.md`, all written by hand.

**Built:** `uv run guppi ledger`, registered on `Stop`. It lifts the bare `- decision[`,
`- estimate[` and `- lesson[` lines of a finished reply into `raw/<date>/ledger.md`,
refuses with exit 2 and a reason when the event log has no `hi` after this session's last
`session-start`, and never writes a line twice. `guppi event` now reads its stdin as UTF-8
bytes. The probe is gone. `make test`: 28 green.

**Measured this session** (five Estimate pages now `passed`, filled by hand):
`estimate-hi-no-read-calls`, `estimate-internal-context-loaded`,
`estimate-git-context-current`, `estimate-github-issues-listed`,
`estimate-event-log-records`. The probe readings are the three `lesson[...]` lines in the
ledger: `Stop` carries `last_assistant_message` and `stop_hook_active`; `ExitPlanMode`
carries the plan in `tool_response.plan`, not in `tool_input`; a hook's stdin on Windows is
cp1252 with `surrogateescape`, which is why the first probe files were empty.

**Not measured:** `estimate-ledger-write-lifts` (live part), `estimate-session-start-context`,
`estimate-case-protocol-loaded`. All three are session C's.

## What the next session does — Slice 1, session C

**The owner restarts Claude Code twice.**

**First start, without `/hi`.** Ask the agent to put one bare line in its reply, exactly:
`- decision[case 0][defer][probe]`. The `Stop` hook must refuse: the reply the owner sees
names the cause (`ledger: 1 line(s) not written — no /hi recorded for session …`) and
`raw/<date>/ledger.md` stays untouched. That is the first reading of
`estimate-session-start-context`. Nothing else happens in that session.

**Second start, with `/hi`.** Then, in order (spec.md, "Сессия C"):

1. The agent writes the `- estimate[<slug>][passed|failed] <result>` lines for all eight
   Estimates, bare, in one reply — the five already measured repeat their page's
   `## Result` in short; `estimate-session-start-context` takes the two readings of these
   two starts; `estimate-case-protocol-loaded` is read off the agent's first reply of this
   session (does it state the fence/bare rule and one-Case-at-a-time without a read call);
   `estimate-ledger-write-lifts` is the fact that these very lines reach the ledger by the
   hook. Check the ledger's tail after the reply: the lines are there, once.
2. Fill the three remaining Estimate pages by hand (`status`, `## Result`, `History`),
   `log.md` too.
3. Retro: what is done and not done; a `- lesson[error][…]` bare line if anything burned.
   Rewrite this brief for Slice 2. Extend `raw/2026-09-09/handoff.md` with a session C
   section. Commit `docs(vault): Slice 1 closes, the brief points at Slice 2`.

**Open Case, not ratified, decide first in session C:** Case 14 (raised in session B).
`SessionStart` also fires on `compact` and `resume`, so by the letter of
`rule-ledger-write` a mid-session compaction closes the `hi` window and every later line
is refused. Recommendation: only another session's `session-start` closes the window.
The code follows the letter until the owner decides; the change is one condition in
`hi_recorded` in `guppi/ledger.py`, one sentence on the rule page, one test.

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
- C9 by hook (`PostToolUse ExitPlanMode` → copy `tool_response.plan` into
  `raw/<date>/spec.md`): Slice 2, `rule-branch-commit`. The payload is now known.
- The fate of `vault/parked/`, `vault/archive/`, `docs/superpowers/`, `docs/HANDOFF.md` and
  the 2026-08 documents under `docs/`. Slice 5.

## Known false, and left so on purpose

- `rule-case-protocol` has `parent: rule-plan-mode`; that page arrives with Slice 2.
- Until Slice 2's renderer the skill file and the four rule pages are two copies of one
  text, kept identical by hand. They are identical again: the `Probe:` line is gone.
- `docs/migration/rule-*.md` carry `origin: TBD`, `sprint: TBD`, `created: TBD`. They are
  drafts, not pages; the drafts stay until Slice 5.
- The `hi` line in `event_log.md` has no session id: `CLAUDE_SESSION_ID` does not reach a
  `!` substitution (measured session B: `unset`). The two-sessions limit of
  `rule-event-log` stands.

## Readings at the close of session B

- `find vault/wiki -type f | wc -l` → 35.
- `make style` → clean; `make test` → 28 passed.
- `git check-ignore vault/raw/2026-09-09/event_log.md` → ignored.
- `guppi event tool` through a pipe: exit 0, 0.10 s.
