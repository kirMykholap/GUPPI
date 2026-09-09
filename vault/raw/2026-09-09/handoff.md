# Handoff — 2026-09-09, Slice 0

## Notes from memory

- The owner read the whole map of the old harness and the whole `docs/migration/` set in the
  same session and chose every recommended option. None of the eight decisions was contested;
  the one he asked about first was the volume of ratifications, which D1 answers.
- The old hooks kept firing their advice during this session (pre-task, one-writer, feedback
  block). Ignored on the owner's permission, and they are gone after this slice.
- `docs/migration/` was untracked when it arrived. It is committed in its original form first,
  then moved and edited, so the drafts survive in history exactly as written.
- `CLAUDE.md` at the root already had the product paragraph removed in the working tree
  before this session started; that edit was the owner's and is folded into the rewrite.

## Direct instructions to the librarian

There is no librarian yet. When one exists (Slice 3), the first thing it should materialize is
this folder: the nine ledger lines above map onto `spec.md`, and the Decision pages for cases
1–8 do not exist yet.

## What actually got done

- Branch `migration` from `main` at `047a612`.
- `job_hunt_ai_vault/` → `vault/`; old live wiki folders and registers → `vault/parked/2026-09-09/`;
  the earlier parking → `vault/parked/2026-09-07/`; `harness-map.md` → `docs/harness-map-2026-09-07.md`.
- `vault/wiki/` holds `index.md`, `glossary.md`, `case-schema.md`, four registers and six
  `schema.yaml` + `schema.md` pairs. No page.
- Corrections C1–C14 applied to `index.md`, `glossary.md`, `rule-session-start.md` and
  `README.md`.
- Old harness removed: `.claude/hooks`, `.claude/agents`, `.claude/templates`, `scripts/`,
  `.superpowers/`, six skills. `/grill-me` kept. `settings.json` holds only the default mode.
- `CLAUDE.md` rewritten as a bootstrap with `@import` of the glossary and the Case schema.
- Where the code landed: the three commits above `047a612` on `migration`.

---

# Handoff — 2026-09-09, Slice 1, session A

## Notes from memory

- Five Cases (9–13), each ratified as recommended on the first pass; the owner's only
  choices were the two sub-questions of Case 11 (`origin`, `gh`), both answered "leave it".
- The `PostToolUse` registration fired mid-session, on the very next tool call, and the
  first firing failed with `Failed to spawn: guppi — program not found`: the entry point
  needs `uv sync` and a build backend. That is why `pyproject.toml` grew a
  `[build-system]` block; it is uv's own backend, fetched once at build time.
- ruff here enforces `DTZ` (timezone-aware datetimes); `datetime.now().astimezone()` is
  the shape that passes.
- The `Stop` probe was registered during this session's last turn; whether it fires at
  that turn's end without a restart is itself a reading — look for
  `probe-Stop-1.json` before assuming a restart was needed.

## Direct instructions to the librarian

Still no librarian. When one exists: the sixteen pages of this slice were written by hand
against `rules/schema.md` and `estimates/schema.md`; check them against lint first, they
predate it.

## What actually got done

- Commit `feat(harness): guppi event, the probe, /hi and the Slice 1 pages` — everything
  of session A but this brief and this note.
- `guppi/event.py`, `guppi/probe.py`, `guppi/cli.py`, `tests/test_event.py` (14 tests).
- `.claude/settings.json`: four registrations. `.claude/skills/hi/SKILL.md`.
- `vault/wiki/rules/` ×8, `vault/wiki/estimates/` ×8, `tags.md` ×7 tags, `log.md` ×6 lines.
- `CLAUDE.md`: Case protocol section, Migration mode updated.
- Not done: `guppi/ledger.py` (waits on the probe), every Estimate reading.

---

# Handoff — 2026-09-09, Slice 1, session B

## Notes from memory

- The first two `probe-Stop-*.json` were 0 bytes, which looked like "no payload". It was
  the write failing after the file was created: a hook's stdin on Windows is cp1252 with
  `surrogateescape`, and the reply is Cyrillic. Reproduced with a one-line pipe before
  fixing. The event log had carried the same defect as mojibake since session A.
- `Stop` fired at the end of the very turn that registered it, in session A: no restart.
- `ExitPlanMode` was exercised on purpose with a real, short plan, so the reading came from
  an ordinary approval; `tool_input` is empty, the plan is in `tool_response.plan`.
- Case 14 (a same-session `session-start compact`/`resume` after `hi` closes the window)
  was raised and is not ratified. The code follows the letter of the rule page.
- The five Estimate pages were filled from this session's own start; that start is the
  measurement, which is why they could not have been taken in session A.

## Direct instructions to the librarian

Still no librarian. The three `lesson[...]` lines of this session have no pages; when the
generator exists they are the first Lessons to materialize. `estimate-event-log-records`'s
Result names `lesson-hooks-windows-stdin-encoding` before that page exists.

## What actually got done

- Commit `feat(harness): guppi ledger on Stop, the probe leaves` — the code, the pages, the
  hand-written lesson lines.
- `guppi/ledger.py`, `tests/test_ledger.py` (13); `read_text` in `guppi/event.py` and a
  test; UTF-8 streams in `guppi/cli.py`. `guppi/probe.py` removed.
- `.claude/settings.json`: `Stop` → `uv run guppi ledger`; `ExitPlanMode` registration gone.
  `.claude/skills/hi/SKILL.md`: `Probe:` line gone. `.gitignore`: probe line gone.
- Five Estimate pages `passed`; `log.md` one line.
- Not done: the live reading of the hook and the three remaining Estimates (session C);
  Case 14.

---

# Handoff — 2026-09-09, Slice 1, session C

## Notes from memory

- The owner's first move after the readings was three format changes (cases 15.1–15.3),
  raised together and ratified together as sub-cases; then he reopened the Case rendering
  (15.2) after seeing it in use, chose the blockquote variant from three rendered in chat,
  and 17 supersedes 15.2. Expect the rendering to be judged on how it reads, not on the
  rule's text.
- The contract change of 15.1 was applied inside the acknowledging reply, before the
  LEDGER block: the `Stop` hook runs the code as it is at the end of the turn, so the lines
  of that very reply landed in the new format. Useful when a hook's own contract changes.
- Filling the three Estimate Results by hand is what exposed the stale criteria (16.1,
  16.2): a rule's `decision update` has no step that lists the Estimates quoting the old
  wording. The lesson line below records it; lint or the generator should own that check.
- The first attempt to write `ledger.py` through a quoted bash heredoc failed on quoting;
  the Write tool was used instead. Not a lesson, a tool choice.
- Case 14 was ratified as recommended: only another session's `session-start` closes the
  `hi` window.

## Direct instructions to the librarian

Still no librarian. The lesson line of session C
(`lesson-estimates-criterion-stale-after-contract-change`) has no page. Case 17
supersedes 15.2: when Decision pages are generated, `decision-update-rule-case-protocol`
for 15.2 is `superseded`, not `current`. Everything from 15.1 on in `ledger.md` carries a
time; the lines before it do not, and that is the hand/hook boundary.

## What actually got done

- Commit `docs(vault): Slice 1 closes, the brief points at Slice 2` — everything of
  session C. The code changes ride in the same commit: `guppi/ledger.py` (LEDGER block,
  time prefix, `hi` window across `compact`/`resume`), `tests/test_ledger.py` (16 tests,
  32 in the suite).
- Pages: `rule-ledger-write` (three updates), `rule-case-protocol` (three updates, render
  block mirrored in `CLAUDE.md`), `estimate-ledger-write-lifts` (criterion, passed),
  `estimate-session-start-context` (passed, criterion), `estimate-case-protocol-loaded`
  (passed, criterion). `log.md` five lines. `CLAUDE.md` Migration-mode paragraph.
- Ledger: eight `estimate[...]` lines (first reply, pre-15.1 format), then cases 15.1,
  15.1, 15.2, 15.3, 14, 16.1, 16.2, 17 and one more `estimate[...]`, all by the hook.
- Not done: nothing of Slice 1's plan. The lesson line lands after the commit.
