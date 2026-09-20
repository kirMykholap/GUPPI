# Handoff — 2026-09-18, session 2253: Work Mode on the conserved Spec of 2054

## Notes from memory

- The session took F4 and F1 of its Frontier — the dirty `ledger.md` of 2054 and Work Mode on the Spec of 2054 — and deferred the rest. Case 254 defers Slice 3b (`rule-work-mode`, `rule-subagent-guppi`) again, the eighth postponement after 183, 206, 218, 231, 242, 248, 252; the `purpose` says "the first item of the next session". The person chose this without hesitation.
- F3 (`git pull` without an upstream, `gh` not logged in) closed as `work`, not as a new defer: the defer of 243 stands and the sprint page names both rules in the Slice 5 item (249). The person agreed; no new decision line.
- The `ExitPlanMode` result did not show the line of the `guppi spec` hook — the second time this is seen (the reading of `estimate-carry-over-writes` in 2054 noted the fork line was not visible either). The Spec was in `raw/2026-09-18/2253/spec.md` when checked by hand. No lesson written: the cause is not known.
- The four `read` lines of the 2054 Spec could not be taken in this session: `estimate-render-harness-ticks-the-spec` and `estimate-sprint-ticks-the-spec` need the librarian's `render` and `sprint` to run over an applied yaml; `estimate-case-protocol-loaded` is read at the first turn of the next session; `estimate-retro-loads` at the first live `/retro` after the render. This session's `/retro` ran before the render and is not that reading.
- One lesson, `lesson-pretask-session-flag-took-the-folder-for-the-stamp` (`error`): the same cause as `lesson-pretask-session-flag-takes-the-id-not-the-hi-line` of 1252 — the skill text of `/pre-task` still says "the stamp from the `hi:` line". Two lessons with one root cause: an Insight is due, and its action is an `update` of `rule-pretask`'s Render naming the eight-character session id.

## Direct instructions to the librarian

- Two units to materialize: `raw/2026-09-18/2054` (11 decision lines — 250.1, 250.2, 252, 253.1, 253.2 — and the reading of `estimate-carry-over-writes`; `carry.md` is deleted, the Spec's work is done) and `raw/2026-09-18/2253` (case 254, two `defer` lines, and one lesson). The Spec of 2054 is `raw/2026-09-18/2054/spec.md`; the Spec of 2253 holds only the Deferred Case 254 and a pointer at the 2054 Spec.
- Case 253.1 has two `file` items (`vault/wiki/case-schema.md`, `vault/wiki/index.md`) already applied by hand in Work Mode; `materialize` should carry them as done, not apply them again.
- The lesson of 2253 shares its root cause with `lesson-pretask-session-flag-takes-the-id-not-the-hi-line` (1252): the second lesson — make the Insight (`insight-pretask-session-flag-…`), severity by the two live lessons.
- After `generate`, `render` and `sprint`: `render` ticks the two `uv run guppi render` lines of the 2054 Spec (253.1, 253.2) and `sprint` ticks its one `uv run guppi sprint` line (250.2) and the three of the 1957 Spec — the first live use of the tick of 250.2, and the place of the reading of `estimate-sprint-ticks-the-spec` and `estimate-render-harness-ticks-the-spec` (the 1957 yaml has the superseded entry of 247). Report whether the lines were ticked; the readings are the main agent's to write in the next session from the report.
- The known flag stands: `materialize` on `raw/2026-09-18/1252/materialize.yaml` ("line 8 changed since the yaml was written").

## What actually got done

- Code, commit `390f412` on `migration`: `guppi/render.py` — `applied_whole` counts `superseded_by` (250.1), `tick_render_lines` became `tick_command_lines(project_dir, command)` with `command_line(command)` building the regex; `guppi/sprint.py` imports it and calls it with `guppi sprint` after the plain write exits 0 (250.2). Tests: one in `tests/test_render.py`, three in `tests/test_sprint.py`; 429 green, style clean; `render --check` and `sprint --check` exit 0.
- By hand (253.1): the sentence in `vault/wiki/case-schema.md` and the `spec.md` line of §1 in `vault/wiki/index.md`.
- The 2054 Spec: six task lines ticked (code, tests, the two hand edits); `carry.md` deleted; the 2054 ledger with the reading of `estimate-carry-over-writes` committed. The 2253 Spec: its three task lines ticked.
- Not done: the page `update`/`create` lines, the render and sprint lines (the librarian); the four readings (next session); Slice 3b (defer 254); F3 (Slice 5).
