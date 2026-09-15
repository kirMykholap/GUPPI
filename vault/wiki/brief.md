# Brief — 2026-09-15, after session R (the derived sections dropped, the librarian's Insight through generate, the gate on a typed command, Cases 164–172)

Written by the librarian, by the frame it was dispatched with (the frame before 168; the
reading of 168 is the brief of the next run).

## Where things stand

What the handoff of session R records under "What actually got done":

- Ratified: 164 (`rule-page-generation`, supersedes 124.2; superseded by 166.2 before it
  applies), 165.2 (defer, taken up by 166.1), 166.1 (eight schema files by hand), 166.2
  (`generate` writes no derived section; migration; supersedes 164), 166.3 (the cascade of
  114 removed; supersedes 114), 166.4 (`rule-cleanup`), 167 (`rule-case-protocol`,
  supersedes 157), 168 (`rule-brief`, `insight-librarian-frame-omits-required-reads`
  actioned), 169.1 (`rule-retro-commit`; `rule-event-log`, `rule-ledger-write` text), 169.2
  (`rule-hook-registry`), 169.3 (`rule-retro`, supersedes 150), 170 (defer Slice 3b,
  supersedes 162), 171 (`rule-page-generation`, contract same, supersedes 124.2), 172
  (`rule-page-generation`, supersedes 148.1).
- Readings: `estimate-index-check-merges` (147.3) and `estimate-synthesis-clusters` (147.4)
  `passed` against the brief of Q's run; `estimate-case-protocol-loaded` blocks 159 and 157
  `passed` on Case 164 and its acknowledging reply. 160's second box ticked in
  `1110/spec.md`.
- Code, commit `f78747c` on `migration`: `guppi/generate.py` (SECTION_ORDER without the
  seven sections; `create` writes none; `rebuild_list`, `derive_insight`,
  `derive_addressed_by`, `links`, `paths_list` removed; `save` writes as is; the cascade
  step of 114 removed; a `create` in `insights` passes when the entry carries `librarian`),
  `guppi/cleanup.py` (`unlink` edits the field only), `guppi/gate.py` (`skill_of` reads
  `prompt` of a `UserPromptSubmit` payload for `/pre-task`, `/retro`, `/handoff`; `typed()`;
  the refusal text for the person), `tests/test_generate.py` (+2), `tests/test_cleanup.py`,
  `tests/test_gate.py` (+5), `tests/test_lint.py`. 377 green, `make style` clean, `guppi
  render --check` exit 0, `guppi lint` 72.
- By hand: `vault/wiki/{rules,entities,lessons,insights}/schema.yaml` and `schema.md`
  (166.1). The migration: 80 pages under `wiki/` and `archive/` lost their derived
  sections.
- Lesson: `lesson-supersedes-in-the-same-session-skips-the-earlier-cases-entries` (`error`,
  L30).
- Not done: the live halves of every reading — 166.2, 166.3, 166.4, 172 (the pages after
  this run, the backlinks in Obsidian — the owner's half), 167 (the first acknowledging
  reply of the next session), 168 (the brief of the next run), 169.1–169.3 (the first
  typed `/retro` of the next session, after the render of `settings.json`); the head
  Criterion texts of `estimate-generate-writes` and `estimate-cleanup-moves` and the second
  refusal text of `rule-ledger-write` (F17); Slice 3b (170).

`uv run guppi materialize` walked two units, exit 0: `raw/2026-09-15/1110/materialize.yaml`
extended with 0 entries; `raw/2026-09-15/1448/materialize.yaml` written with 49 entries
from the session ledger (30 lines) and `1448/spec.md`: 0 `create` of a page, 24 `update`
(13 rules, 10 estimates derived from `contract: changed`, 1 insight), 8 `file`, 3 `defer`,
9 `remove_criterion`, 4 `estimate`, 1 `lesson`; 0 unparsed lines, 0 `incomplete`. The
entries of 164 (`replace`, criterion block) got `superseded_by: '166.2'`, the defer of
165.2 `superseded_by: '166.1'`; the `remove_criterion` of 164 carries no mark, see Flags.

The librarian at the index check: the one lesson compared against the Grep
`^(root_cause|deferred_by):` over `wiki/lessons/`, 29 lines (27 lessons, 2 `schema.md`), 0
`deferred_by`; nothing merged, no `near`. No entity, rule or insight `create` in the yaml
of this session; the Greps of `rules/` and `entities/` were not run. The `create` of
`insight-retro-typed-command-is-never-a-tool-call` in `1110` was checked in Q's run and
was not checked again.

At synthesis: the one `root_cause` against the same 29 lesson lines and the Grep
`^(pattern|deferred_by):` over `wiki/insights/`, 11 lines (10 Insights, 1 `schema.md`), 0
`deferred_by`. Nothing appended. `insight-workflow-contract-change-leaves-its-derived-text-stale`
(a change leaves the text derived from it stale) and `insight-ledger-line-written-unchecked`
(a line nothing reads back until materialize) settled on the index line: the lesson's
mechanism is a `supersedes` that skips every entry of the earlier Case, caught at
pre-task — not the same cause. No page opened. The lesson stays `new`.

`uv run guppi generate`: exit 0; 1 page for `1110` (the retried Insight), 45 for `1448`.
Lines: 8 `file` entries of 166.1 "a Rule-class file, applied by hand"; `remove_criterion`
of 165.2, 164, 162 and 124.2 "no Estimate holds a block". `uv run guppi cleanup`: 9 pages
moved, stderr empty. `uv run guppi render`: stdout and stderr empty; three governed files
differ from HEAD — `CLAUDE.md` (167), `.claude/settings.json` (169.2),
`.claude/agents/librarian-guppi.md` (168); `guppi render --check` exit 0.

| category | created | updated |
|---|---|---|
| decisions | 14 (`decision-case-164`, `165.2`, `166.1`…`172`) | 8 set `archived` by the supersedes cascade and moved by `cleanup` to `vault/archive/migration/2026-09-15/1448/decisions/`: `164` (by 166.2), `165.2` (by 166.1), `114` (by 166.3), `124.2` (by 171), `148.1` (by 172), `150` (by 169.3), `157` (by 167), `162` (by 170) |
| rules | 0 | 11 by decision: `rule-page-generation` (166.2, 166.3, 171, 172 — five `replace` in one paragraph, all applied; the sentence of 171 stands once), `rule-cleanup` (166.4), `rule-case-protocol` (167), `rule-brief` (168), `rule-retro-commit`, `rule-event-log`, `rule-ledger-write` (169.1), `rule-hook-registry` (169.2), `rule-retro` (169.3), `rule-work-mode` and `rule-subagent-guppi` (`deferred_by` `decision-case-162` → `decision-case-170`); `deferred_by` of 165.2 on `rule-page-generation` never written (superseded). By cascade: `rule-index-check`, `rule-synthesis` `draft` → `built` (147.3, 147.4 `passed`); `rule-brief`, `rule-cleanup`, `rule-hook-registry`, `rule-page-generation`, `rule-retro-commit` `built` → `draft` (a `pending` block); `rule-case-protocol`, `rule-retro` stay `draft` |
| estimates | 0 | 9 criterion blocks appended on 7 pages: `estimate-generate-writes` +166.2 +166.3 +172, `estimate-cleanup-moves` +166.4, `estimate-case-protocol-loaded` +167, `estimate-brief-written` +168, `estimate-retro-commit-gates` +169.1, `estimate-hook-registry-rendered` +169.2, `estimate-retro-loads` +169.3 — all seven `pending`; 5 blocks removed: 114, 124.2, 148.1 (`estimate-generate-writes`), 157 (`estimate-case-protocol-loaded`), 150 (`estimate-retro-loads`); 4 `remove_criterion` found no block (165.2, 164, 162 — defers or never applied; 124.2 by 171, removed already, see Flags); 4 readings written, all `passed`: `estimate-index-check-merges` (147.3), `estimate-synthesis-clusters` (147.4), `estimate-case-protocol-loaded` ×2 (159, 157 — before 167 set it `pending`) |
| lessons | 1 (`lesson-supersedes-in-the-same-session-skips-the-earlier-cases-entries`, `error`, tags `workflow`, `ledger`) | 1 set `archived` by the cascade of the actioned Insight and moved to `vault/archive/migration/2026-09-15/1448/lessons/`: `lesson-brief-next-section-has-no-source` |
| insights | 1: `insight-retro-typed-command-is-never-a-tool-call` — the `failed` entry of `1110` retried and applied, `open`, `severity` 2, two children, `## Pattern` and `## Proposal`, no `## Children`; its `failed` mark dropped | 1 by decision: `insight-librarian-frame-omits-required-reads` `open` → `actioned`, `addressed_by: decision-case-168` |
| entities | 0 | 0 |

The checks the handoff asks for, after the run:

- `rule-page-generation`: 164 did not apply; the sentence "A `create` in `insights/` from a
  ledger line is refused…" stands once, marked `case 171, the text of 164; supersedes
  124.2`; the three `replace` of 166.2 and the one of 166.3 applied, 172's too.
- `estimate-generate-writes`: blocks 166.2, 166.3, 172 present, `pending`; blocks 114,
  124.2, 148.1 absent; no block 164. The eight decisions named are archived.
- The retried Insight: page written, `severity` 2; `guppi lint` raises no `ref` on the two
  retro lessons.
- No live page of `rules/`, `entities/`, `lessons/` or `insights/` carries a `## Estimates`,
  `## Children`, `## Parent`, `## Implementation`, `## Code`, `## Insight` or `## Addressed
  by` heading (Grep over the four folders, 0 hits). `log.md` has no `insight section
  derived` line of today.
- `.claude/settings.json` rendered with `uv run guppi gate` as the second `UserPromptSubmit`
  command; `guppi render --check` exit 0. The typed `/retro` of session R before the render
  is not a failure of 169.
- `sprint.md` unchanged: the handoff says "no change".
- Lint 72 → 70, as the handoff expected.

## What the next session does first

From the handoff's "Not done" list and the state after this run:

1. The readings `pending`, one per block, on the rules that stand `draft`:
   `estimate-case-protocol-loaded` (167: the first acknowledging reply — the `LEDGER`
   block first, the question last), `estimate-brief-written` (168: the brief of the next
   run, "Readings due" as its second section), `estimate-retro-commit-gates` (169.1),
   `estimate-hook-registry-rendered` (169.2) and `estimate-retro-loads` (169.3): the first
   typed `/retro` of the session, now that `settings.json` carries the gate;
   `estimate-generate-writes` (166.2, 166.3, 172) and `estimate-cleanup-moves` (166.4): the
   pages of this run are written without derived sections, no `insight section derived`
   line, the backlinks in Obsidian are the owner's half.
2. Plan Mode over the Deferred list and the Flags: the open Insight
   `insight-retro-typed-command-is-never-a-tool-call` (its Proposal is largely what 169.1–169.3
   ratified; the Case that takes it up ends in `actioned`, a rejection, or a `defer`); F17
   (the head Criterion texts, the second refusal text); Slice 3b (170).

## Deferred

1. **`insight-retro-typed-command-is-never-a-tool-call`** — `open`, severity 2, created in
   this run from the retried entry of Q. Pattern: a slash command typed by the person is
   expanded by the client into the prompt and is never a Skill tool call, so a hook on the
   Skill tool sees only the agent's own calls; a cure aimed at the skill's settings changes
   the agent's path and leaves the typed one as it was. Proposal: treat the two paths as
   two — the agent's call gated on the Skill tool, the person's typed command on
   `UserPromptSubmit`; a `then` on a slash command names which path it covers, and its
   reading takes both. In Plan Mode a Case whose `recommend` starts from that Proposal,
   ending in an `update` of the Insight (`status: actioned`, `addressed_by`), a rejection
   written the same way, or a `defer` with the Insight as its target. (stood in 1 brief)
2. **Slice 3b: Work Mode** — Case 170 (supersedes 162), `rule-work-mode` and
   `rule-subagent-guppi` (placeholders, `draft`, `deferred_by: [[decision-case-170]]`, the
   two lint orphans): the Spec as tasks with code, the ticked boxes in `spec.md`, the
   readings taken in Work Mode, what a subagent may do and the fork that comes back as a
   Case; the Plan Mode of a session of its own, before Slice 4. Related Insight
   `insight-harness-agent-visibility`, `actioned`, severity 0. (postponed 13 times)

Of the previous brief's two items, item 1 (`insight-librarian-frame-omits-required-reads`)
was actioned by 168 (`addressed_by: decision-case-168`) and is no longer `open`; item 2
(Slice 3b, 162) was retired by 170's `supersedes` and deferred again by 170, item 2 above.
The defer of 165.2 (`rule-page-generation`) was retired by 166.1's `supersedes` in the same
session. Item 1 above is the one `open` Insight, ranked first by severity.

## Flags

- **0 `failed`, 0 `incomplete`, 0 `unparsed`, 0 `near`, 0 `merged`** in `1448`. The one
  `failed` of `1110` (the Insight create) applied in this run and lost its mark.
- **3 entries marked `exists`**: the defer of 165.2 on `rule-page-generation` (superseded,
  not applied) and the two defers of 170 on the live placeholders; `deferred_by` set, no
  placeholder written. Expected.
- **The `remove_criterion` of 164 applied although 164 is superseded.** `materialize` wrote
  `superseded_by: '166.2'` on the `replace` and the criterion-block entries of line 3 and
  not on its third entry, `remove_criterion` of 124.2; `generate` applied it
  (`log.md`: "criterion: case 124.2 removed · [[decision-case-164]]"), and 171's own
  removal of 124.2 then found no block. The page is as the handoff expected — block 124.2
  gone — but the History credits a superseded decision. Not repaired.
- **No Estimate `failed`.** `estimate-retro-loads` went from `failed` (150) to `pending`
  when 169.3 appended its block and 150's block was removed. 7 Estimates `pending`, 9
  rules `draft` (the five set `draft` by this run's blocks, `rule-case-protocol`,
  `rule-retro`, the two placeholders).
- **Contradictions, pre-existing, from the handoff (F17)**: the head Criterion of
  `estimate-generate-writes` and `estimate-cleanup-moves` still names `## Children` and
  `## Estimates` — no `### case` block, so no `supersedes` reaches it; `rule-ledger-write`
  after 169.1 names one refusal text where the gate now has two. Both are the pattern of
  `insight-workflow-contract-change-leaves-its-derived-text-stale` (`actioned`).
- **Stale defers:** `rule-work-mode` and `rule-subagent-guppi` have stood as placeholders
  since Case 29 (now 170), without `kind`, `estimates` or `tags`; 6 `schema` findings and 2
  orphans.
- **No MOC candidate.** The vault holds no Entity page.
- **The handoff's instructions were all within the frame**; none was refused. Its
  expectations held.
- **The librarian read outside its inputs twice**, both named in the report: a Grep of
  `status:` over eight pages of `wiki/decisions/` to confirm the cascade the handoff asked
  about (the archive folder listing would have answered), and a Grep of the unticked
  `- [ ] read` lines of `1448/spec.md`; the brief uses neither, its readings list comes
  from the handoff and the Estimate statuses.
- **Archive (run after the brief): 0 units moved**, stdout and stderr empty, exit 0.
  `raw/2026-09-15/1110` is applied but dated today, kept; `raw/2026-09-15/1448` is the
  session of the run, never moved.
- **Lint.** `make lint` exits 1 at its second step (`guppi lint`); `guppi render --check`
  exit 0. `guppi lint`: 70 findings, exit 1 — 68 `schema` (31 missing `## Context`, 31
  `## Problem`, on the decision pages of Cases 1–28; `kind`, `estimates`, `tags` on the two
  placeholders), 2 `orphan` (the two placeholders). 72 before this run: −2 `ref` (the
  retro lessons, their Insight now on disk). The two `## Estimates` findings of the
  placeholders went with 166.1 in session R.

## Readings at the close

- `make test` → 377 passed.
- `make lint` → exit 1 at `guppi lint`; `guppi render --check` → exit 0; `guppi lint` → 70
  findings, exit 1.
- Live pages, 358: rules 40 (31 `built`, 9 `draft`: `rule-brief`, `rule-case-protocol`,
  `rule-cleanup`, `rule-hook-registry`, `rule-page-generation`, `rule-retro-commit`,
  `rule-retro`, `rule-work-mode`, `rule-subagent-guppi`), entities 0, estimates 42 (35
  `passed`, 7 `pending`: `estimate-brief-written`, `estimate-case-protocol-loaded`,
  `estimate-cleanup-moves`, `estimate-generate-writes`, `estimate-hook-registry-rendered`,
  `estimate-retro-commit-gates`, `estimate-retro-loads`; 0 `failed`), lessons 27 (25 `new`,
  2 `clustered`), insights 11 (10 `actioned`, 1 `open`), decisions 238 (all `current`).
- `vault/archive/migration/` holds 109 pages: the 100 of the previous brief and 9 under
  `2026-09-15/1448/` (8 decisions, 1 lesson); and the raw of the dates 09-09…09-14 under
  `<date>/[HHMM/]raw/`. `cleanup` moved 9 in this run.
- `raw/2026-09-15/1448/materialize.yaml`: 49 entries, 46 `applied`, 3 `superseded_by`, 0
  `failed`, 0 unparsed lines, 0 `incomplete`, 0 `near`, 3 `exists`, 0 `merged`.
  `raw/2026-09-15/1110/materialize.yaml`: 42 entries, all `applied`.
