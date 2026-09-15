# Brief — 2026-09-15, after session Q (the readings due, the three deferred items, the shape of the Case, Cases 155–163)

Written by the librarian.

## Where things stand

What the handoff of session Q records under "What actually got done":

- Ratified: 155 (`rule-ask`, `rule-pretask`, supersedes 154), 156 (`rule-lint`, supersedes
  146), 157 (`rule-case-protocol`), 158 (`rule-materialize`), 159 (`rule-case-protocol`,
  `case-schema`), 160 (`decision-case-140`,
  `lesson-obsidian-property-links-need-wikilink-form`), 161 (`rule-materialize`), 163
  (`index`, `glossary`, `case-schema`). Deferred: 162 (`rule-work-mode`,
  `rule-subagent-guppi`, supersedes 152).
- Code, commit `891fd56` on `migration`: `guppi/lint.py` (`check_orphans` excludes
  `insights`, docstring), `guppi/materialize.py` (docstring on readable entries; `find_item`
  matches a Rule-class item by `file`), `tests/test_lint.py` (+1),
  `tests/test_materialize.py` (+1): 370 green, `make style` clean, `guppi render --check`
  exit 0, `guppi lint` 74 findings.
- By hand: `vault/wiki/case-schema.md` ("Eight, in this order.", the `tasks` row, `then` as
  behaviour only, Operands "and also / but not", the story rules paragraph under Language,
  `tasks` on a sub-case, the `ratification` row), `vault/wiki/index.md` §2 (eight
  sections), `vault/wiki/glossary.md` (the Case row).
- Readings: `estimate-lint-catches` (149.3, 156), `estimate-cleanup-moves` (147.6),
  `estimate-harness-pipeline` (153), `estimate-ask-finds` (147.2),
  `estimate-documentation-completes` (147.5), `estimate-case-protocol-loaded` (144.1),
  `estimate-materialize-assembles` (158, 161) — all `passed`; `estimate-retro-loads` (150)
  `failed`. `estimate-brief-written` (124.1) not re-read.
- Lessons: `lesson-brief-next-section-has-no-source`,
  `lesson-materialize-file-item-matched-by-slug-only`,
  `lesson-retro-typed-still-bypasses-the-skill-tool-after-150`,
  `lesson-wiki-page-edited-by-hand-in-obsidian` — all `error`, no `source`.
- Not done: the readings of 157 and 159 (the next session, after the render), 147.3 and
  147.4 (from this brief), 160 (`lint` without `ref`, the next `/hi`), 122 and the use
  clause of 144.1 (at the event); the cure of 150 and the `parent` mismatch of `rule-lint`
  (Cases of the next Plan Mode); Slice 3b (162).

`uv run guppi materialize` walked five units, exit 0: `raw/2026-09-14/0747`, `1029`, `1229`
and `1633` extended with 0 entries; `raw/2026-09-15/1110/materialize.yaml` written with 37
entries from the session ledger (28 lines) and `1110/spec.md`: 0 `create`, 17 `update` (9
rules, 5 estimates derived from `contract: changed`, 1 decision, 1 lesson, 4 `file`), 2
`defer`, 4 `remove_criterion`, 9 `estimate`, 4 `lesson`; 0 unparsed lines, 0
`incomplete`. In `1633` the entries of 146, 152 (×2) and 154 got `superseded_by: '156'` /
`'162'` / `'155'`.

The librarian at the index check: the four lessons compared against the Grep
`^(root_cause|deferred_by):` over `wiki/lessons/`, 27 lines (25 lessons, 2 `schema.md`),
0 `deferred_by`; nothing merged; 1 `near`:
`lesson-retro-typed-still-bypasses-the-skill-tool-after-150` near
`lesson-retro-typed-by-the-person-bypasses-the-skill-tool-and-the-gate` (the same path, a
corrected cause, a second event — not the same page). No entity, rule or insight `create`
in the yaml; the Greps of `rules/` and `entities/` were not run.

At synthesis: the four `root_cause` lines against the same 27 lesson lines and the Grep
`^(pattern|deferred_by):` over `wiki/insights/`, 11 lines (10 Insights, 1 `schema.md`), 0
`deferred_by`. Five entries appended, `librarian: synthesis`:

- a `create` of `insight-retro-typed-command-is-never-a-tool-call` over
  `lesson-retro-typed-by-the-person-bypasses-the-skill-tool-and-the-gate` and
  `lesson-retro-typed-still-bypasses-the-skill-tool-after-150` (one cause: a typed slash
  command is expanded into the prompt and is never a Skill tool call; the earlier lesson's
  cause names `disable-model-invocation`, 150 removed it, the typed path did not change) —
  **refused by `generate`**, see Flags; and the two lesson `update`s to `clustered`, which
  applied;
- an `update` of `insight-librarian-frame-omits-required-reads` (`actioned` →
  `open`, child `lesson-brief-next-section-has-no-source` added) and the lesson's `update`
  to `clustered`: the frame's list of sources is shorter than the brief needs, as its list
  of reads was shorter than the judgments — the same mechanism; the page was opened for the
  judgment.
- `lesson-materialize-file-item-matched-by-slug-only` against
  `insight-materialize-lift-loses-a-schema-field` (`actioned`): the page opened; not
  clustered. The Insight's mechanism is a field lost from a page and named by lint on the
  page; the lesson is an item not found at all, marked `incomplete: [then]` in the yaml,
  no page and no lint finding. Same area, not the same cause; the lesson stays `new`.
- `lesson-wiki-page-edited-by-hand-in-obsidian`: no lesson or Insight with the cause;
  stays `new`.

`uv run guppi generate`: 0 pages for the four units of 09-14; 38 for `1110`; exit 1, one
stderr line (the Insight create). Stdout: 4 `file` entries "a Rule-class file, applied by
hand" (159 `case-schema`; 163 `index`, `glossary`, `case-schema`); the `remove_criterion`
of 154, 146 and 152 (×2) "no Estimate holds a block" (defers, no block). Entry 112.6 of
`0747` skipped without a line. `uv run guppi cleanup`: 3 pages moved, stderr empty.
`uv run guppi render`: stdout and stderr empty; two governed files differ from HEAD —
`CLAUDE.md` (157, 159), `.claude/agents/ask-guppi.md` (155); `guppi render --check` exit 0.

| category | created | updated |
|---|---|---|
| decisions | 9 (`decision-case-155`…`163`) | 1 by decision (`decision-case-140`, 160, `replace` in its Context); 3 set `archived` by the supersedes cascade and moved by `cleanup` to `vault/archive/migration/2026-09-15/1110/decisions/`: `146` (by 156), `152` (by 162), `154` (by 155) |
| rules | 0 | 9 by decision: `rule-ask` (155), `rule-pretask` (155), `rule-lint` (156), `rule-case-protocol` (157 then 159, two `replace` on different paragraphs), `rule-materialize` (158 then 161, two `replace` on different sentences), `rule-work-mode` and `rule-subagent-guppi` (`deferred_by` `decision-case-152` → `decision-case-162`); `deferred_by` cleared on `rule-lint` (146) and `rule-ask` (154); 3 `draft` → `built` by cascade (`rule-cleanup`, `rule-documentation`, `rule-harness`); `rule-case-protocol` stays `draft` (157, 159 `pending`), `rule-retro` `draft` (`estimate-retro-loads` `failed`) |
| estimates | 0 | 5 criterion blocks appended: `estimate-lint-catches` +156, `estimate-case-protocol-loaded` +157 +159, `estimate-materialize-assembles` +158 +161; 4 `remove_criterion` found no block (154, 146, 152 ×2); 9 readings written: 8 `passed` (`estimate-lint-catches` ×2, `estimate-cleanup-moves`, `estimate-harness-pipeline`, `estimate-ask-finds`, `estimate-documentation-completes`, `estimate-case-protocol-loaded` on 144.1 before 157 and 159 set it `pending`, `estimate-materialize-assembles` after 158 and 161), 1 `failed` (`estimate-retro-loads`, 150) |
| lessons | 4 (`error`, no `source`, listed above) | 1 by decision (`lesson-obsidian-property-links-need-wikilink-form`, 160: `set: root_cause`, `replace` in the body); 3 set `clustered` by synthesis: the two retro lessons (their `insight` names a page that was not written) and `lesson-brief-next-section-has-no-source` |
| insights | 0 (1 refused) | 1 reopened by synthesis: `insight-librarian-frame-omits-required-reads` `actioned` → `open`, `severity` 1, three children |
| entities | 0 | 0 |

The checks the handoff asks for, after the run:

- Case 159's `file` item for `case-schema.md` with no `slug` and the three `file` items of
  163 were found by `find_item`: no `incomplete: [then]` on any of the four — the live half
  of the reading of 161 (`estimate-materialize-assembles`, `passed` on line 25).
- `rule-case-protocol`: 157 then 159 applied in ledger order, both `replace` applied, no
  failure; `estimate-case-protocol-loaded` carries blocks `157` and `159`, `pending`.
  `rule-materialize`: 158 then 161, both `replace` applied; `estimate-materialize-assembles`
  carries `158` and `161`, `passed`; block 142.1 keeps its wording, as the handoff says.
- `rule-lint`: 156 applied, `deferred_by` cleared, `decision-case-146` superseded and
  archived; `rule-ask`: 155 applied, `deferred_by` cleared, `decision-case-154` superseded
  and archived; `rule-work-mode` and `rule-subagent-guppi`: `deferred_by:
  ["[[decision-case-162]]"]`, `decision-case-152` superseded and archived.
- Case 160: `decision-case-140` and `lesson-obsidian-property-links-need-wikilink-form`
  updated; `guppi lint` raises no `ref` on either.
- The two renders listed above; `guppi render --check` exit 0.
- Entry 112.6 of `0747`: `failed`, `superseded_by: '130.1'`, skipped without a line.
- `sprint.md` unchanged: the handoff says "no change".

## What the next session does first

From the handoff's "Not done" list and the state after this run:

1. The readings `pending`: `estimate-case-protocol-loaded` (157: the first acknowledging
   reply after the render; 159: the first Case shown in the chat),
   `estimate-index-check-merges` (147.3: this brief names the Grep and 27 lines, 1 `near`,
   0 merged), `estimate-synthesis-clusters` (147.4: this brief names the two Greps, 27 and
   11 lines, one Insight reopened, one create refused). `rule-case-protocol`,
   `rule-index-check`, `rule-synthesis` stand `draft` until then.
2. `estimate-retro-loads` (150) is `failed`, `rule-retro` `draft`: the cure of 150 is a
   Case of the next Plan Mode.
3. 160: `guppi lint` after this run raises no `ref` on `decision-case-140` or
   `lesson-obsidian-property-links-need-wikilink-form` — the line is not written here. 122
   and the use clause of 144.1 at the event.
4. Plan Mode over the Deferred list and the Flags: the refused Insight create (the two
   retro lessons carry a dangling `insight`), the `parent` mismatch of `rule-lint`, Slice
   3b.

## Deferred

1. **`insight-librarian-frame-omits-required-reads`** — `open`, severity 1, reopened from
   `actioned` (143). Pattern: the frame of the librarian names the reads it allows one by
   one, and the list is shorter than the judgments the librarian must make; the agent then
   breaks a clause or judges on an index line alone. New child
   `lesson-brief-next-section-has-no-source`: "What the next session does first" is the one
   section of `rule-brief` with no source named. Proposal: derive the read clauses from the
   judgments, one clause per judgment naming the page and the field; change every rule that
   names a read in one pass. In Plan Mode a Case whose `recommend` starts from that
   Proposal, ending in an `update` of the Insight (`status: actioned`, `addressed_by`), a
   rejection written the same way, or a `defer` with the Insight as its target. (stood in 1
   brief since reopening)
2. **Slice 3b: Work Mode** — Case 162 (supersedes 152), `rule-work-mode` and
   `rule-subagent-guppi` (placeholders, `draft`, `deferred_by: [[decision-case-162]]`, the
   two lint orphans): the Spec as tasks with code, the ticked boxes, what a subagent may do,
   and the fork that comes back as a Case; the Plan Mode of a session of its own. Related
   Insight `insight-harness-agent-visibility`, `actioned`, severity 0. (postponed 12 times)

Of the previous brief's three items, item 2 (`rule-ask`, 154) was retired by 155's
`supersedes` and ratified there; item 3 (`rule-lint`, 146) by 156's `supersedes`, ratified
there; item 1 (Slice 3b, 152) was retired by 162's `supersedes` and deferred again by 162,
item 2 above. Item 1 above is the one `open` Insight, ranked first by severity.

## Flags

- **1 `failed`: the `create` of `insight-retro-typed-command-is-never-a-tool-call`**,
  `librarian: synthesis`. `generate` refused it: "an Insight is made and retired by the
  librarian, never created or deleted by a decision (case 124.2)". `generate.create`
  refuses every `create` in `insights` and does not read the `librarian` mark, so the
  synthesis path of `rule-synthesis` (a `create` in `insights` on the second lesson) and
  the guard of 124.2 contradict each other; the last synthesis create that applied
  (`insight-ledger-hi-tied-to-its-session-by-position`, `0747`) ran before 124.2 was
  committed. The entry stays as it is, not repaired. The two lesson `update`s of the same
  cluster applied before the refusal was known: both retro lessons are `clustered` with
  `insight: "[[insight-retro-typed-command-is-never-a-tool-call]]"`, which no page carries —
  2 new `ref` findings. A Case of the next Plan Mode: either `generate` exempts an entry
  marked `librarian`, or the Insight is created another way; the yaml holds the
  `pattern`, `children`, `tags`, `Pattern` and `Proposal` the page would carry.
- **1 `near`**: `lesson-retro-typed-still-bypasses-the-skill-tool-after-150` near
  `lesson-retro-typed-by-the-person-bypasses-the-skill-tool-and-the-gate`.
- **2 entries marked `exists`**: the defers of 162 on the two live placeholders; the pages
  get `deferred_by`, no placeholder is written. Expected.
- **0 `incomplete`, 0 `unparsed`** in `1110`. The four `file` entries were found by `file`
  (161). Entry 112.6 of `0747` stays `failed` with `superseded_by: '130.1'`; the 13
  `incomplete: [then]` of `1633` and the 3 `incomplete: [source]` of `1229` stay as they
  were, those units are applied and archived at the close.
- **1 Estimate `failed`: `estimate-retro-loads`** (150) — the typed `/retro` bypasses the
  Skill tool and the gate; the agent's own call passes. `rule-retro` `draft`.
- **The reopened Insight**: `insight-librarian-frame-omits-required-reads` returned to
  `open` on the librarian's judgment that a missing source for a section of the brief is
  the same gap as a missing read clause. The judgment is the librarian's; the Case that
  takes the Insight up can reject the clustering.
- **Contradiction, pre-existing, not acted on**: `rule-lint` frontmatter `parent:
  "[[rule-harness]]"` while its `## Parent` section names `rule-documentation`; lint does
  not catch it (handoff). A Case of the next Plan Mode, or a lint check.
- **Stale defers:** `rule-work-mode` and `rule-subagent-guppi` have stood as placeholders
  since Case 29 (now 162), without `kind`, `estimates` or `tags`; 8 `schema` findings and 2
  orphans.
- **No MOC candidate.** The vault holds no Entity page.
- **The handoff's instructions were all within the frame**; none was refused. Its
  expectations held except the lint total: 74 → 72 was expected after 160; the two `ref`
  findings of 160 are gone and two new `ref` findings came from the refused Insight, so the
  total stays 74.
- **Archive (run after the brief): 4 units moved.** `raw/2026-09-14/0747`, `1029`, `1229`,
  `1633` — applied and dated before today. `raw/2026-09-15/1110` is the session of the run,
  never moved. See the report for the archive's stderr.
- **Lint.** `make lint` exits 1 at its second step (`guppi lint`); `guppi render --check`
  exit 0. `guppi lint`: 74 findings, exit 1 — 70 `schema` (31 missing `## Context`, 31
  `## Problem`, on the decision pages of Cases 1–28; `kind`, `estimates`, `tags`,
  `## Estimates` on the two placeholders), 2 `ref` (the two retro lessons, `insight` names
  `insight-retro-typed-command-is-never-a-tool-call`, "which no live or archived page
  carries"), 2 `orphan` (the two placeholders). 84 before this run: −10 `orphan` (the
  Insights, 156), −2 `ref` (160), +2 `ref` (the refused Insight).

## Readings at the close

- `make test` → 370 passed.
- `make lint` → exit 1 at `guppi lint`; `guppi render --check` → exit 0; `guppi lint` → 74
  findings, exit 1.
- Live pages, 351: rules 40 (34 `built`, 6 `draft`: `rule-case-protocol`,
  `rule-index-check`, `rule-retro`, `rule-synthesis`, `rule-work-mode`,
  `rule-subagent-guppi`), entities 0, estimates 42 (38 `passed`, 3 `pending`:
  `estimate-case-protocol-loaded`, `estimate-index-check-merges`,
  `estimate-synthesis-clusters`; 1 `failed`: `estimate-retro-loads`), lessons 27 (24
  `new`, 3 `clustered`), insights 10 (9 `actioned`, 1 `open`), decisions 232 (all
  `current`).
- `vault/archive/migration/` holds 100 pages: the 97 of the previous brief and 3 under
  `2026-09-15/1110/decisions/` (`146`, `152`, `154`); and the raw of the dates 09-09…09-13
  under `<date>/[HHMM/]raw/`, with the four units of 09-14 added by the archive of this
  run. `cleanup` moved 3 in this run.
- `raw/2026-09-15/1110/materialize.yaml`: 42 entries (37 lifted, 5 `librarian: synthesis`),
  41 `applied`, 1 `failed`, 0 unparsed lines, 0 `incomplete`, 1 `near`, 2 `exists`, 0
  `merged`.
