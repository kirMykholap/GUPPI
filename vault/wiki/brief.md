# Brief — 2026-09-16, after session 2225 of 2026-09-15 (the gate's third refusal, the Estimate model deferred as Slice 3d, Cases 180–185)

Written by the librarian, by the frame after 168; block 168 of `estimate-brief-written` is
`passed` since this session's ledger.

## Where things stand

What the handoff of session 2225 records under "What actually got done":

- Ratified: 180 (`rule-retro-commit`, `contract: changed`), 181 (`rule-case-protocol`,
  `contract: same`, supersedes 179), 182 (defer ×5, Slice 3d, supersedes 178), 183 (defer
  ×2, Slice 3b after 3d, supersedes 176), 184 (`rule-ledger-write`, `contract: changed`),
  185 (defer `rule-case-protocol`).
- Readings `passed`: `estimate-retro-commit-gates` block 169.1,
  `estimate-materialize-assembles` block 175, `estimate-brief-written` block 168,
  `estimate-ledger-write-lifts` block 184.
- Lesson: `lesson-pretask-check-session-fallback-stops-at-midnight` (`error`).
- Code, commit `572df74` on `migration`: `guppi/gate.py` (`nothing_to_review`, the refusal
  in `run` for `retro` before the check of 122, the docstring), `tests/test_gate.py` (+6
  tests, two fixtures given a reading line). 385 green, `make style` clean.
- `raw/2026-09-15/2225/spec.md`: the two code boxes of 180 ticked; open — the `update`
  boxes of 180, 181, 184 and the `render --check` of 181 (the librarian's), the reading of
  block 180 (live, next session), the reading of block 184 (taken).
- Not done: the live reading of 180 — impossible in a session that already has ledger
  lines; next session types `/retro` first thing after `/hi` and sees the refusal. Slice
  3d and 3b: their own Plan Modes. The owner's question on `ask-guppi` and defers: next
  Plan Mode — why `ask-guppi` at pre-task reads a `defer` in depth when the Case moves to
  another session; a candidate `update` of `rule-pretask`.
- The session ran from 22:25 past midnight into 2026-09-16; the folder is
  `raw/2026-09-15/2225/`, the ledger lines after 01:00 belong to it.

`uv run guppi materialize` walked four units, exit 0: `raw/2026-09-15/1110`, `1448` and
`1809` extended with 0 entries; `raw/2026-09-15/2225/materialize.yaml` written with 21
entries from the session ledger (16 lines) and `2225/spec.md`: 0 `create` of a page, 5
`update` (3 rules, 2 estimates derived from `contract: changed`), 8 `defer`, 3
`remove_criterion` (derived from the three `supersedes`), 4 `estimate`, 1 `lesson`; 0
unparsed lines, 0 `incomplete`. `1809/materialize.yaml` gained 5 `superseded_by` marks
(the three entries of 176 by 183, 178 by 182, 179 by 181), each keeping its `applied`.

The librarian at the index check: the handoff's checks first — the four `old` strings of
the `replace` of 180, 181 (two) and 184, each found once in its page after whitespace
collapse. The one lesson compared against the Grep `^(root_cause|deferred_by):` over
`wiki/lessons/`, 28 lines (26 lessons, 2 `schema.md`), 0 `deferred_by`; no live lesson
line speaks of the session stamp or the `--------` mark (the lessons of 136.1 are archived
children of an Insight, not in the Grep); nothing merged, no `near`. No entity, rule or
insight `create` in the yaml; the Greps of `rules/` and `entities/` were not run.

At synthesis: the one `root_cause` against the same 28 lesson lines and the Grep
`^(pattern|deferred_by):` over `wiki/insights/`, 12 lines (11 Insights, 1 `schema.md`), 0
`deferred_by`. One page opened, `insight-ledger-hi-tied-to-its-session-by-position`
(`actioned` by 136.4, severity 0): its pattern — a session found from the event log by the
position of the `session-start` lines, not by an id, so a start outside the window breaks
the binding — is the cause of the lesson too (`pretask.resolve_session` falls back to the
last `session-start` of today's log when no id is given, and yesterday's start is outside
it); its first child is the hook's own midnight failure. Clustered: two entries appended
with `librarian: synthesis` — the Insight `update` (`status: open`, four children) and the
lesson `update` (`status: clustered`).

`uv run guppi generate`: exit 0; 0 pages for `1110`, `1448` and `1809`, 26 for `2225`;
stderr empty. Stdout: three "remove_criterion: case N: no Estimate holds a block" lines,
for 179, 178 and 176 — the derived removals of 181, 182 and 183; the three were defers and
had no block. `uv run guppi cleanup`: 3 pages moved, stderr empty. `uv run guppi render`:
stdout and stderr empty; `CLAUDE.md` and `.claude/` equal to HEAD; `guppi render --check`
exit 0.

| category | created | updated |
|---|---|---|
| decisions | 6 (`decision-case-180`…`185`) | 3 set `archived` by the supersedes cascade and moved by `cleanup` to `vault/archive/migration/2026-09-16/2225/decisions/`: `176` (by 183), `178` (by 182), `179` (by 181) |
| rules | 0 | 10 by decision: `rule-retro-commit` (180, `replace` applied, stays `draft`), `rule-case-protocol` (181, two `replace` applied; `deferred_by` `decision-case-179` → `decision-case-185`), `rule-ledger-write` (184, `replace` applied, stays `built`), `rule-plan-mode` (`deferred_by` `decision-case-178` → `decision-case-182`), `rule-page-generation`, `rule-materialize`, `rule-lint`, `rule-pretask` (`deferred_by: decision-case-182`), `rule-work-mode` and `rule-subagent-guppi` (`deferred_by` `decision-case-176` → `decision-case-183`). By cascade: `rule-materialize` and `rule-brief` `draft` → `built` (their blocks `passed`) |
| estimates | 0 | 4: `estimate-retro-commit-gates` (`passed` on 169.1, then +180 `pending`; ends `pending`), `estimate-ledger-write-lifts` (+184, then `passed` on 184; ends `passed`), `estimate-materialize-assembles` (`passed` on 175), `estimate-brief-written` (`passed` on 168) |
| lessons | 1 (`lesson-pretask-check-session-fallback-stops-at-midnight`, `error`, tags `harness`, `session`; `clustered` by synthesis) | 0 |
| insights | 0 | 1: `insight-ledger-hi-tied-to-its-session-by-position` `actioned` → `open` by synthesis, fourth child added, severity 0 → 1 |
| entities | 0 | 0 |

The checks the handoff asks for, after the run:

- `rule-case-protocol`: `deferred_by: ["[[decision-case-185]]"]` only; `decision-case-179`
  archived. Both `old` strings of 181 applied; the second spanned a line wrap.
- `rule-retro-commit`: the `replace` of 180 applied once; `estimate-retro-commit-gates`
  holds blocks 169.1 and 180, `status: pending`; the rule stays `draft`.
- `rule-ledger-write`: the `replace` of 184 applied once; `estimate-ledger-write-lifts`
  holds block 184 and ends `passed`; the rule `built`.
- Readings: `estimate-materialize-assembles` `passed`, `rule-materialize` `built`;
  `estimate-brief-written` `passed`, `rule-brief` `built`.
- 182, 183, 185: `deferred_by` set on the eight rule pages, no placeholder written;
  `decision-case-178` and `decision-case-176` archived; `rule-work-mode` and
  `rule-subagent-guppi` keep their placeholder state.
- `sprint.md`: Slice 3d added before 3b in the Slices list, one sentence naming Case 182
  and its sixteen points on `rule-plan-mode`, "3d before 3b, Slice 4 after both". Nothing
  else changed there.
- Lint 70, unchanged, as the handoff expected.

## Readings due

After `generate`, 1 Estimate `pending`, 0 `failed`:

- `estimate-retro-commit-gates`, block 180, `rule-retro-commit` `draft`. Read from the
  unticked line of `2225/spec.md`: `tests/test_gate.py` green; live — a typed `/retro` as
  the first prompt of the next session after `/hi`, the refusal seen.

## Deferred

1. **`insight-ledger-hi-tied-to-its-session-by-position`** — `open`, severity 1. Pattern:
   the event log ties a hi line to its session by the session-start lines around it, not
   by an id; any start that is missing from the window or added to it sends the hi to the
   wrong session and the ledger writer refuses. Proposal (from the page, written before
   136.4): the stamped `hi` of 111 and the window read by stamp let the binding by position
   be retired; the fallback keeps the lessons live while it stands. The new child: the
   pre-task check's `resolve_session` still falls back to today's log by position when
   `--session` is absent, and stops at midnight, unlike the hook's window (the lesson of
   session 2225). (stood in 1 brief)
2. **`rule-work-mode`** — Case 183 (supersedes 176), Slice 3b: the Spec as tasks with
   code, the ticked boxes in `spec.md`, the test of each Estimate written first and turned
   green; the Plan Mode of a session of its own, after Slice 3d and before Slice 4.
   Placeholder, `draft`, a lint orphan. Related Insight `insight-harness-agent-visibility`,
   `actioned`, severity 0. (stood in 15 briefs)
3. **`rule-subagent-guppi`** — Case 183, Slice 3b: what a subagent may do in Work Mode,
   and the fork that comes back to the main agent as a Case; with `rule-work-mode`.
   Placeholder, `draft`, a lint orphan. Related Insight `insight-harness-agent-visibility`,
   `actioned`, severity 0. (stood in 15 briefs)
4. **`rule-plan-mode`** — Case 182 (supersedes 178), Slice 3d, the Estimate model agreed
   in session 2225: the sixteen points of the purpose of `decision-case-182` — one promise,
   one check, one last result per Estimate; the Criterion replaced whole; no `### case N`
   blocks, no `contract`, no `method` on `create`; lint `unread` on every `pending`; the
   Rule-class files of 3d: `estimates/schema.md`, `rules/schema.md`, `decisions/schema.md`,
   `case-schema.md`, `index.md` §6–§7, `glossary.md`. The question of 178 disappears with
   the blocks. Related Insight `insight-workflow-contract-change-leaves-its-derived-text-stale`,
   `actioned`, severity 0. (stood in 2 briefs)
5. **`rule-case-protocol`** — Case 185, Slice 3d: the Render rewritten by points 6, 7 and 9
   of the model of 182 — `given` the conditions of the behaviour, `given` + `when` + `then`
   the Estimate's Criterion, no `### case N` blocks, no `method` on `create` and no
   `contract` on `update`, `tasks` without `contract` lines. No related Insight. (stood in
   2 briefs)
6. **`rule-page-generation`** — Case 182, Slice 3d: `generate` without Criterion blocks and
   `remove_criterion`; the Criterion replaced whole; the fields `purpose`, `method`,
   `checked`. No related Insight. (stood in 1 brief)
7. **`rule-materialize`** — Case 182, Slice 3d: `materialize` without `contract`, derived
   blocks, `method`/`estimate_kind`/`estimate_slug` on `create`; an `update` of an Estimate
   is a replaced Criterion. No related Insight. (stood in 1 brief)

Nine candidates for the cap of seven: the two cut are the last two targets of 182 in the
yaml, `rule-lint` (the finding `unread` on every `pending`/`failed` Estimate; the Estimate
schema without Context and the Method section) and `rule-pretask` (pre-task checks the
Estimates of the rule named in `context` and asks `ask-guppi` whether an unnamed one
speaks of the same thing), both `deferred_by: decision-case-182`, both stood in 1 brief.
Of the previous brief's three items: item 1 (Slice 3b, 176) retired by 183's `supersedes`
and deferred again by 183, items 2 and 3 above; item 2 (`rule-plan-mode`, 178) retired by
182's `supersedes` and deferred again by 182, item 4 above; item 3 (`rule-case-protocol`,
179) retired by 181's `supersedes`, the page deferred again by 185, item 5 above.

## Flags

- **0 `failed`, 0 `incomplete`, 0 `unparsed`, 0 `near`, 0 `merged`** in `2225`; 2 entries
  `librarian: synthesis`, both `applied`.
- **8 entries marked `exists`**: the defers of 182 (five), 183 (two) and 185 on live rule
  pages; `deferred_by` set, no placeholder written. Expected.
- **`generate` stdout**: "remove_criterion: case 179 / 178 / 176: no Estimate holds a
  block" — the derived removals of 181, 182, 183; the superseded Cases were defers.
  Nothing removed, nothing to remove.
- **No Estimate `failed`.** 1 `pending` (Readings due). 3 rules `draft`:
  `rule-retro-commit`, `rule-work-mode`, `rule-subagent-guppi`.
- **An Insight reopened by synthesis**: `insight-ledger-hi-tied-to-its-session-by-position`
  `actioned` (136.4) → `open`; its three earlier children stay archived, the new one is
  live, severity 1. The handoff expected a `near` on a lesson and no merge; no live lesson
  line matched, and the pair was found in `insights/`, not `lessons/`.
- **The lesson's `near` from the handoff not set**: the handoff named "the lessons on the
  session stamp and `CLAUDE_SESSION_ID`" as the comparison; none is live, so no `near`
  could name one.
- **Deferred list cut**: nine candidates, seven kept; `rule-lint` and `rule-pretask` of
  182 named above, not in the list.
- **The owner's open question** (from the handoff, for the next Plan Mode): why
  `ask-guppi` at pre-task reads a `defer` in depth when the Case moves to another
  session — a candidate `update` of `rule-pretask`, itself a target of 182.
- **`spec.md` boxes**: the handoff says the reading of block 184 is taken and asks that
  its box be ticked; the librarian does not write `spec.md` — not done, named in the
  report. The librarian's `update` boxes of 180, 181, 184 and the `render --check` box of
  181 stay open, as in the previous sessions; `render --check` itself exited 0.
- **Contradictions:** none new. The three `remove_criterion` entries of this run are the
  same shape as 176's of the previous run — a `supersedes` of a defer derives a removal
  that finds no block; stdout, not stderr.
- **Stale defers:** `rule-work-mode` and `rule-subagent-guppi` have stood as placeholders
  since Case 29 (now 183), without `kind`, `estimates` or `tags`; 6 `schema` findings and
  2 orphans.
- **No MOC candidate.** The vault holds no Entity page.
- **The handoff's instructions were within the frame** except the tick of a `spec.md` box,
  named above. Its expectations held.
- **Reads outside the yaml, handoff and index lines**, named in the report: the Insight
  opened at synthesis; the four `old` strings checked over the three rule pages at the
  handoff's request; a Grep of `- [ ]` lines over `2225/spec.md` (`rule-brief` names it as
  the source of "where it is read"); Greps of `status:`, `deferred_by:` and the block
  headings over the pages the handoff's checks name; a Grep of `severity:` over
  `wiki/insights/` for the ranking; and of `status:` over every category for the counts.
- **Archive (run after the brief): 3 units moved**, stderr empty, exit 0; `1110`, `1448`
  and `1809` of 2026-09-15 — the first archive of units dated the day before the run.
- **Lint.** `make lint` exits 1 at `guppi lint`; `guppi render --check` exit 0. `guppi
  lint`: 70 findings, exit 1 — 68 `schema` (31 missing `## Context`, 31 `## Problem`, on
  the decision pages of Cases 1–28; `kind`, `estimates`, `tags` on the two placeholders),
  2 `orphan` (the two placeholders). 70 before this run.

## Readings at the close

- `make test` → 385 passed.
- `make lint` → exit 1 at `guppi lint`; `guppi render --check` → exit 0; `guppi lint` → 70
  findings, exit 1.
- Live pages, 366: rules 40 (37 `built`, 3 `draft`), entities 0, estimates 42 (41
  `passed`, 1 `pending`: `estimate-retro-commit-gates`; 0 `failed`), lessons 27 (26 `new`,
  1 `clustered`), insights 11 (10 `actioned`, 1 `open`), decisions 246 (all `current`).
- `vault/archive/migration/` holds 116 pages: the 113 of the previous brief and 3 under
  `2026-09-16/2225/decisions/` (`176`, `178`, `179`); and the raw of the dates
  09-09…09-14 under `<date>/[HHMM/]raw/`. `cleanup` moved 3 in this run.
- `uv run guppi archive`, after the brief: 3 units moved, stderr empty, exit 0 —
  `raw/2026-09-15/1110`, `1448` and `1809` (applied, dated before the run) to
  `vault/archive/migration/2026-09-15/<HHMM>/raw/`; `raw/2026-09-15/2225` is the session
  of the run, kept. `raw/2026-09-15/` now holds `2225/` and `event_log.md`.
- `raw/2026-09-15/2225/materialize.yaml`: 23 entries (21 written, 2 by synthesis), all
  `applied`, 0 `failed`, 0 unparsed lines, 0 `incomplete`, 0 `near`, 8 `exists`, 0
  `merged`. In the archive: `1809/raw/materialize.yaml` 20 entries, all `applied`, 5
  `superseded_by` (176 ×3, 178, 179); `1448/raw/materialize.yaml` 49 entries, 46
  `applied`, 6 `superseded_by`; `1110/raw/materialize.yaml` 42 entries, all `applied`, 4
  `superseded_by`.
