# Brief — 2026-09-18, after session 2253 of 2026-09-18 (Work Mode on the conserved Spec of 2054: sprint ticks its Spec lines, applied whole counts a superseded entry, three tickers named; Slice 3b deferred; one Insight on `--session` of pre-task)

Written by the librarian from `raw/2026-09-18/2253/handoff.md`, the yamls of
`raw/2026-09-18/2054` and `raw/2026-09-18/2253`, and the Greps of the indexes.

## Where things stand

- Code, commit `390f412` on `migration`: `guppi/render.py` — `applied_whole` counts
  `superseded_by` (250.1); `tick_render_lines` became `tick_command_lines(project_dir,
  command)` with `command_line(command)`; `guppi/sprint.py` calls it with `guppi sprint`
  after the plain write exits 0 (250.2). Tests: one in `tests/test_render.py`, three in
  `tests/test_sprint.py`. By hand (253.1): one sentence in `vault/wiki/case-schema.md`, the
  `spec.md` line of §1 in `vault/wiki/index.md`. The 2054 Spec: six task lines ticked in
  Work Mode, `carry.md` deleted, the 2054 ledger committed with the reading of
  `estimate-carry-over-writes`. The 2253 Spec: its three task lines ticked.
- Not done in the session: the page lines, the render and sprint lines (this run, below);
  the four readings (next session); Slice 3b (defer 254); F3 (Slice 5).
- Two units materialized. `raw/2026-09-18/2054`: 12 entries — 5 Decision pages created
  (250.1, 250.2, 252, 253.1, 253.2); rules: 3 updated (`rule-sprint`, `rule-case-protocol`,
  `rule-retro`), 2 deferred (`rule-work-mode`, `rule-subagent-guppi`); estimates: 1 created
  (`estimate-sprint-ticks-the-spec`), 3 updated to `pending` (`estimate-render-harness-ticks-the-spec`,
  `estimate-case-protocol-loaded`, `estimate-retro-loads`), 1 reading applied
  (`estimate-carry-over-writes`, `passed`); 2 Rule-class files (`case-schema`, `index`)
  marked applied by hand by `generate`. 17 pages written or changed.
  `raw/2026-09-18/2253`: 3 entries plus 3 of the synthesis — 1 Decision page (254), 2 defers
  (`rule-work-mode`, `rule-subagent-guppi`), 1 lesson created
  (`lesson-pretask-session-flag-took-the-folder-for-the-stamp`), 1 Insight created
  (`insight-pretask-session-flag-takes-the-id-not-the-hi-line`, severity 2), 2 lessons set
  `clustered`. 6 pages written or changed. Cleanup moved 0 pages.
- Statuses computed by `generate`: `rule-carry-over` `draft` → `built` (its one Estimate
  passed); `rule-render-harness`, `rule-sprint`, `rule-case-protocol`, `rule-retro`
  `built` → `draft` (one Estimate of each `pending`). `deferred_by` of `rule-work-mode` and
  `rule-subagent-guppi` now ends at `decision-case-254`.
- Rendered: `CLAUDE.md` (the Case protocol names three tickers) and
  `.claude/skills/retro/SKILL.md` (a `guppi sprint` line waits for the librarian).
  `vault/wiki/sprint.md` rewritten by `guppi sprint`: Slice 3b current, both items `draft`
  with defers to 254.
- Ticks by the scripts this run: `render` ticked lines 162 and 193 of the 2054 Spec (the
  two `uv run guppi render` lines); `sprint` ticked line 94 of the 2054 Spec and lines 37,
  103 and 137 of the 1957 Spec (the unit whose yaml holds the superseded entry of 247, no
  `applied` on it). The 2054 Spec now has four unticked lines, all `read`.
- Tests: 429 green (`make test`), style clean at `390f412`.

## Readings due

- `estimate-sprint-ticks-the-spec` — `rule-sprint` stands `draft` — read at line 95 of
  `raw/2026-09-18/2054/spec.md`: `pytest tests/test_sprint.py`, plus one reading of the 2054
  and 1957 Specs after the librarian's run. The facts of this run: 2054 line 94 and 1957
  lines 37, 103, 137 ticked by `guppi sprint`; nothing else of those Specs changed by it.
- `estimate-render-harness-ticks-the-spec` — `rule-render-harness` stands `draft` — read at
  line 53 of the 2054 Spec. The facts of this run: `guppi render` ticked 2054 lines 162 and
  193; the 1957 unit counts applied whole with its superseded entry (its sprint lines were
  ticked by the same `applied_whole`); the four `read` lines stayed unticked.
- `estimate-case-protocol-loaded` — `rule-case-protocol` stands `draft` — line 163 of the
  2054 Spec: the first turn of the next session, without a read call, `CLAUDE.md` as
  rendered by this run.
- `estimate-retro-loads` — `rule-retro` stands `draft` — line 194 of the 2054 Spec: the
  first live `/retro` after this render.
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` — by its `method`:
  `make lint` exit 0, or only unread lines on the sprint page's own Estimates, at the close
  of the sprint.
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` — by its `method`:
  one reading of the tree by hand at the close of the sprint.
- `estimate-sprint-migration-merges` — `entity-sprint-migration` — by its `method`:
  `make test` on the last commit of `migration`, then `git log` of `main` after the merge.

## Deferred

1. `insight-pretask-session-flag-takes-the-id-not-the-hi-line` — severity 2, `open`, first
   brief. Pattern: the `/pre-task` skill says "the stamp from the `hi:` line", but
   `--session` of `guppi pretask` takes the eight-character session id alone, one of the
   three tokens of that line; a wrong token answers "no hi recorded" with exit 0 and the
   value cut to eight characters, so the run looks clean and nothing was checked. Proposal:
   an `update` of the Render of `rule-pretask` that names the eight-character session id —
   the second token of the `hi:` line — as the value of `--session`, and one line on reading
   the output's first line, not the exit code. In Plan Mode a Case whose `recommend` starts
   from this; it ends in an `update` of the Insight (`status: actioned`, `addressed_by`), a
   rejection written the same way, or a `defer` with the Insight as its target.

Left out, the sprint page names them (case 229.4): `rule-work-mode` and
`rule-subagent-guppi` (defers 252, 254 this walk; 183, 206, 218, 231, 242, 248 before —
Slice 3b, the current milestone); `insight-workflow-code-live-before-the-page-it-reads`
(`open`, severity 2, defer 238; in the text of the `rule-work-mode` item);
`rule-git-context`, `rule-github-issues` (defers 220, 243; Slice 5, the
`estimate-sprint-migration-merges` item); `rule-spec-box` (defers 207, 219, 232; Slice 5);
`rule-morph` (defer 239; Slice 5). The previous brief's list was empty.

## Flags

- Handoff flags, each a Case of the next Plan Mode: Slice 3b — `rule-work-mode`,
  `rule-subagent-guppi` (defer 254, "the first item of the next session"), with the
  sentence of `insight-workflow-code-live-before-the-page-it-reads` written into
  `rule-work-mode`; the Insight above.
- The `ExitPlanMode` result did not show the line of the `guppi spec` hook, the second
  time (the reading of `estimate-carry-over-writes` in 2054 saw the fork line missing too);
  the Spec was in `raw/2026-09-18/2253/spec.md` when checked by hand. No lesson: the cause
  is not known.
- F3 of every Frontier since 243: the failed `git pull` and the unavailable `gh` in `/hi`
  close as `work` until Slice 5 (Case 251 not ratified; the defer of 243 stands).
- The handoff asked `materialize` to carry the two `file` items of 253.1 as done:
  `generate` marks a `category: file` entry "applied by hand" itself; no edit of the yaml.
- Standing: `materialize` on `raw/2026-09-18/1252/materialize.yaml` — "line 8 changed
  since the yaml was written; entry left alone"; the defer of 238 on
  `insight-workflow-code-live-before-the-page-it-reads` without a `purpose`;
  `estimate-hi-no-read-calls` in the shape before case 193 by choice;
  `rule-spec-box` placeholder findings (`kind`, `estimates`, orphan).
- Stale defers by lint: `rule-work-mode` and `rule-subagent-guppi` 20 times since case 29;
  `rule-morph` 1 time since case 239.
- Four rules back to `draft` from `built` by their pending Estimates (above); they return
  to `built` when the readings pass.
- No entry marked `incomplete`, `failed`, `near` or `unparsed` in either yaml; no failed
  Estimate; no MOC candidate.
- Lint, 76 findings: 2 `rules/rule-spec-box` schema (`kind`, `estimates`) and 1 orphan;
  62 `decisions/decision-case-<1–28>` missing `## Context` and `## Problem` (Slice 5);
  3 deferred (`rule-morph` 1, `rule-subagent-guppi` 20, `rule-work-mode` 20); 7 unread
  pending (the Readings due); `estimates: unmigrated: 29 pages in the shape before case 193`.

## Readings at the close

- `make test`: 429 passed.
- `make lint`: 76 findings, exit 1 (the list above).
- Pages: entities 2, rules 44, estimates 67, lessons 34, insights 14, decisions 349.
