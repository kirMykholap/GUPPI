# Brief — 2026-09-15, after session S (the Insight actioned, the stale heads caught up, the supersedes marks every entry, Cases 173–179)

Written by the librarian, by the frame after 168; this brief is the reading of block 168
of `estimate-brief-written`.

## Where things stand

What the handoff of session S records under "What actually got done":

- Ratified: 173 (`insight-retro-typed-command-is-never-a-tool-call` `actioned`;
  `case-schema.md` by hand), 174 (`estimate-generate-writes`, `estimate-cleanup-moves`
  head texts; `rule-ledger-write` both advices, `contract: same`), 175 (`rule-materialize`,
  `contract: changed`, `estimate_slug: estimate-materialize-assembles`), 176 (defer Slice
  3b, supersedes 170), 177 (`rule-materialize`, `contract: same`, supersedes 130.2), 178
  (defer `rule-plan-mode`), 179 (defer `rule-case-protocol`).
- Readings `passed`: `estimate-case-protocol-loaded` (167), `estimate-cleanup-moves`
  (166.4), `estimate-generate-writes` (166.2, 166.3, 172 — one line),
  `estimate-hook-registry-rendered` (169.2), `estimate-retro-loads` (169.3).
- Lesson: `lesson-plan-mode-contract-change-skips-the-estimates-blocks` (`error`).
- Code, commit `e88a357` on `migration`: `guppi/materialize.py` (`mark_superseded` by case
  number), `tests/test_materialize.py` (+2). 379 green, `make style` clean.
- By hand: `vault/wiki/case-schema.md`, one sentence (173).
- `raw/2026-09-15/1448/spec.md`: five reading boxes ticked. `raw/2026-09-15/1809/spec.md`:
  the agent's boxes ticked; the librarian's `update` boxes of 173, 174, 175, 177 and the
  readings 169.1, 175, 168 open.
- Not done: the reading of 175 (this run's report, read next session); 169.1 `pending` on
  purpose; 168 (this brief); Slice 3b (176); F6–F8 of the frontier are Slice 5 tasks in
  `sprint.md`.

`uv run guppi materialize` walked three units, exit 0: `raw/2026-09-15/1110` and `1448`
extended with 0 entries; `raw/2026-09-15/1809/materialize.yaml` written with 20 entries
from the session ledger (17 lines) and `1809/spec.md`: 0 `create` of a page, 8 `update`
(3 rules, 4 estimates — one derived from `contract: changed` — 1 insight), 1 `file`, 4
`defer`, 2 `remove_criterion`, 4 `estimate`, 1 `lesson`; 0 unparsed lines, 0
`incomplete`. The three entries of 170 in `1448/materialize.yaml` (line 26 `defer`
`rule-work-mode`, line 26 `remove_criterion` of 162, line 27 `defer` `rule-subagent-guppi`)
carry `superseded_by: '176'`; each also keeps its `applied: 17:58:17` of R's run.

The librarian at the index check: the one lesson compared against the Grep
`^(root_cause|deferred_by):` over `wiki/lessons/`, 29 lines (27 lessons, 2 `schema.md`), 0
`deferred_by`; nothing merged; `near:
lesson-supersedes-in-the-same-session-skips-the-earlier-cases-entries` added (the same
events, 164 and 171; a different cause — the supersedes semantics, not the unread
Estimate). No entity, rule or insight `create` in the yaml; the Greps of `rules/` and
`entities/` were not run.

At synthesis: the one `root_cause` against the same 29 lesson lines and the Grep
`^(pattern|deferred_by):` over `wiki/insights/`, 12 lines (11 Insights, 1 `schema.md`), 0
`deferred_by`. Two pages opened, neither clustered:
`insight-workflow-contract-change-leaves-its-derived-text-stale` (`actioned`, severity 0)
— its mechanism is the dependent of a change going unnamed, cured by the derived blocks of
72.1 and 88.2; the block of 175 did land on the right Estimate, and the lesson's mechanism
is the existing blocks of that Estimate going unread at Case time.
`insight-session-vault-knowledge-not-loaded` (`actioned`, severity 0) — a fact missing
from the session's loading channel, not a read missing from a step of Plan Mode.
`insight-ledger-line-written-unchecked` settled on the index line. Nothing appended; the
lesson stays `new`.

`uv run guppi generate`: exit 0; 0 pages for `1110` and `1448`, 29 for `1809`; stderr
empty. Stdout: "case-schema: a Rule-class file, applied by hand" (173) and
"remove_criterion: case 170: no Estimate holds a block" (the derived removal of 176; 170
was a defer and had no block). No line for the three superseded entries of 170. `uv run
guppi cleanup`: 4 pages moved, stderr empty. `uv run guppi render`: stdout and stderr
empty; `CLAUDE.md` and `.claude/` equal to HEAD; `guppi render --check` exit 0.

| category | created | updated |
|---|---|---|
| decisions | 7 (`decision-case-173`…`179`) | 2 set `archived` by the supersedes cascade and moved by `cleanup` to `vault/archive/migration/2026-09-15/1809/decisions/`: `130.2` (by 177), `170` (by 176) |
| rules | 0 | 6 by decision: `rule-ledger-write` (174), `rule-materialize` (175 and 177, both `replace` applied; `built` → `draft` on the pending block), `rule-work-mode` and `rule-subagent-guppi` (`deferred_by` `decision-case-170` → `decision-case-176`), `rule-plan-mode` (`deferred_by: decision-case-178`), `rule-case-protocol` (`deferred_by: decision-case-179`). By cascade: `rule-case-protocol`, `rule-cleanup`, `rule-hook-registry`, `rule-page-generation`, `rule-retro` `draft` → `built` (their blocks `passed`) |
| estimates | 0 | 6: `estimate-materialize-assembles` (+175 `pending`, −130.2; `passed` → `pending`), `estimate-generate-writes` (174 one `replace` on the head; `passed` on 166.2, 166.3, 172), `estimate-cleanup-moves` (174 two `replace` on the head; `passed` on 166.4), `estimate-case-protocol-loaded` (`passed` on 167), `estimate-hook-registry-rendered` (`passed` on 169.2), `estimate-retro-loads` (`passed` on 169.3) |
| lessons | 1 (`lesson-plan-mode-contract-change-skips-the-estimates-blocks`, `error`, tags `workflow`, `harness`, `near` set) | 2 set `archived` by the cascade of the actioned Insight and moved to `vault/archive/migration/2026-09-15/1809/lessons/`: `lesson-retro-typed-by-the-person-bypasses-the-skill-tool-and-the-gate`, `lesson-retro-typed-still-bypasses-the-skill-tool-after-150` |
| insights | 0 | 1: `insight-retro-typed-command-is-never-a-tool-call` `open` → `actioned`, `addressed_by: decision-case-173` |
| entities | 0 | 0 |

The checks the handoff asks for, after the run:

- `estimate-materialize-assembles`: block 130.2 gone (History: "case 130.2 removed ·
  decision-case-177"), block 175 present, `status: pending`, no block 177.
- `rule-materialize`: the `replace` of 175 in the line about a later `supersedes` ("every
  entry carrying its `case`") and the one of 177 in the description of the yaml ("marks
  every entry carrying `case: N`") both applied. `decision-case-130.2` archived.
- 174: `estimate-generate-writes` and `estimate-cleanup-moves` end `passed` with the
  corrected head (the three `old` texts replaced once each); `rule-ledger-write` carries
  both advices.
- 173: the Insight `actioned`, `addressed_by` set; its two lessons archived under
  `2026-09-15/1809/lessons/`.
- 176, 178, 179: `deferred_by` set on the four rule pages; no placeholder written.
- `sprint.md` unchanged: the handoff says "no change".
- Lint 70, unchanged, as the handoff expected.

## Readings due

After `generate`, 3 Estimates `pending`, 0 `failed`:

- `estimate-materialize-assembles`, block 175, `rule-materialize` `draft`. Read from the
  unticked line of `1809/spec.md`: the tests green; live — the first `supersedes` of a Case
  whose own line carried a `supersedes`: every entry of it marked in the yaml, `generate`
  prints no line for them. This run's report: the three entries of 170 in
  `1448/materialize.yaml` (two `defer`, one `remove_criterion` of 162) carry
  `superseded_by: '176'`; `generate` printed no line for them; its one line naming 170,
  "remove_criterion: case 170: no Estimate holds a block", is the derived entry of 176.
- `estimate-retro-commit-gates`, block 169.1, `rule-retro-commit` `draft`. Read from the
  unticked line of `1809/spec.md`: the next session types `/retro` before the plan is
  written, to see what the gate says — the live refusal of a typed `/retro` on a Spec item
  without its line.
- `estimate-brief-written`, block 168, `rule-brief` `draft`. No unticked line in
  `1809/spec.md`; from the page's `Method`: one reading by hand after the first librarian
  run, recorded in the estimate line — this brief, "Readings due" as its second section.

## Deferred

1. **Slice 3b: Work Mode** — Case 176 (supersedes 170), `rule-work-mode` and
   `rule-subagent-guppi` (placeholders, `draft`, `deferred_by: [[decision-case-176]]`, the
   two lint orphans): the Spec as tasks with code, the ticked boxes in `spec.md`, the
   readings taken in Work Mode; the Plan Mode of a session of its own, before Slice 4.
   Related Insight `insight-harness-agent-visibility`, `actioned`, severity 0. (stood in 14
   briefs)
2. **`rule-plan-mode`** — Case 178: decide who reads the blocks of an Estimate's Criterion
   and names the block a contract change supersedes — the Case at its forming (`given`
   carries the blocks, `pretask --check` before the ratification question) or the
   librarian at `generate`; today only pre-task catches the contradiction, after the
   signature (cases 171, 177). Related Insight
   `insight-workflow-contract-change-leaves-its-derived-text-stale`, `actioned`, severity
   0; the lesson of this session is its record. (stood in 1 brief)
3. **`rule-case-protocol`** — Case 179: one `replace` in How it works, "The six Case
   sections" → eight, the count of case 163; found by `ask-guppi` at the pre-task of
   session S. No related Insight. (stood in 1 brief)

Of the previous brief's two items, item 1 (`insight-retro-typed-command-is-never-a-tool-call`)
was actioned by 173 and is no longer `open`; item 2 (Slice 3b, 170) was retired by 176's
`supersedes` and deferred again by 176, item 1 above. No Insight is `open`.

## Flags

- **0 `failed`, 0 `incomplete`, 0 `unparsed`, 1 `near`, 0 `merged`** in `1809`: the
  `near` on the lesson, named above.
- **4 entries marked `exists`**: the defers of 176 (two), 178 and 179 on live rule pages;
  `deferred_by` set, no placeholder written. Expected.
- **No Estimate `failed`.** 3 `pending` (Readings due). 5 rules `draft`: `rule-brief`,
  `rule-materialize`, `rule-retro-commit`, `rule-work-mode`, `rule-subagent-guppi`.
- **The three entries of 170 carry both `applied` (R's run) and `superseded_by: '176'`.**
  `generate` skipped them; nothing was undone. Expected by 175's block ("the block a
  superseded Case meant to remove stands until a live Case removes it").
- **History of `estimate-generate-writes`** still credits `decision-case-164` (superseded)
  with the removal of block 124.2; left as it is on purpose, by the handoff. Not repaired.
- **Contradictions:** none new. F17 (the head texts of the two Estimates, the second refusal
  text of `rule-ledger-write`) closed by 174.
- **Stale defers:** `rule-work-mode` and `rule-subagent-guppi` have stood as placeholders
  since Case 29 (now 176), without `kind`, `estimates` or `tags`; 6 `schema` findings and 2
  orphans.
- **No MOC candidate.** The vault holds no Entity page.
- **The handoff's instructions were all within the frame**; none was refused. Its
  expectations held.
- **Reads outside the yaml, handoff and index lines**, named in the report: the two
  Insights opened at synthesis; `estimate-brief-written` (`Method` and block 168, where
  168 is read); a Grep of `- [ ] read` lines over `1809/spec.md` (rule-brief names it as
  the source of "where it is read"); Greps of `status:`, `deferred_by:` and the block
  headings over the pages the handoff's checks name, and of `status:` over every category
  for the counts.
- **Archive (run after the brief): 0 units moved**, stdout and stderr empty, exit 0.
  `raw/2026-09-15/1110` and `1448` are applied but dated today, kept; `raw/2026-09-15/1809`
  is the session of the run, never moved.
- **Lint.** `make lint` exits 1 at `guppi lint`; `guppi render --check` exit 0. `guppi
  lint`: 70 findings, exit 1 — 68 `schema` (31 missing `## Context`, 31 `## Problem`, on
  the decision pages of Cases 1–28; `kind`, `estimates`, `tags` on the two placeholders),
  2 `orphan` (the two placeholders). 70 before this run.

## Readings at the close

- `make test` → 379 passed.
- `make lint` → exit 1 at `guppi lint`; `guppi render --check` → exit 0; `guppi lint` → 70
  findings, exit 1.
- Live pages, 362: rules 40 (35 `built`, 5 `draft`), entities 0, estimates 42 (39
  `passed`, 3 `pending`: `estimate-brief-written`, `estimate-materialize-assembles`,
  `estimate-retro-commit-gates`; 0 `failed`), lessons 26 (26 `new`), insights 11 (11
  `actioned`, 0 `open`), decisions 243 (all `current`).
- `vault/archive/migration/` holds 113 pages: the 109 of the previous brief and 4 under
  `2026-09-15/1809/` (2 decisions, 2 lessons); and the raw of the dates 09-09…09-14 under
  `<date>/[HHMM/]raw/`. `cleanup` moved 4 in this run.
- `raw/2026-09-15/1809/materialize.yaml`: 20 entries, all `applied`, 0 `failed`, 0
  unparsed lines, 0 `incomplete`, 1 `near`, 4 `exists`, 0 `merged`.
  `raw/2026-09-15/1448/materialize.yaml`: 49 entries, 46 `applied`, 6 `superseded_by`
  (164 ×2, 165.2, 170 ×3). `raw/2026-09-15/1110/materialize.yaml`: 42 entries, all
  `applied`.
