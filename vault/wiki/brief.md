# Brief — 2026-09-12, after session J (the Estimate derived from the Case, Cases 70–84)

Written by the librarian.

## Where things stand

What the handoff of session J records under "What actually got done":

- Commits: `e43c9e4` the render of six harness files (the first item of the previous
  brief); `16b7f58` Cases 72–76 — `materialize` (72.3, 73.5, 76), `generate` (72.4),
  `pretask`/`spec`/`ledger` (72.5, 73.2, 73.4, 74, 75.2; `session_dir` lives in
  `guppi/ledger.py`, not `event.py`, an import cycle), `lint` (72.6), the ledger test of
  70, seven Rule-class files (72.1, 72.2, 73.1, 75.1), the one-off of 73.1; `90bdd36` the
  Retro.
- `make test` 258 green, `make style` clean, `guppi lint` 129 findings, `render --check`
  exit 0 before this run.
- Ratified: 70, 71.1, 72.1–72.6, 73.1–73.10, 74, 75.1, 75.2, 76, 77. Deferred: 78–84.
- Readings passed: `estimate-hi-writes-frontier`, `estimate-materialize-assembles`,
  `estimate-pretask-reconciles`, `estimate-lint-catches`. Failed on a clause, not on the
  code: `estimate-governed-files-hook-refuses`, `estimate-claude-md-rendered`,
  `estimate-render-harness-reproduces` (Cases 83, 84).
- Not done: the render of the governed files by 72.1, 73.x, 74, 75 (next session start);
  five readings; the Spec's 15 unticked tasks are all of that kind.
- Per-session files moved under `raw/<date>/<hi HHMM>/` (Case 73): session I is `0454`,
  session J is `1156`. `sprint.md` was not touched, as the handoff instructs.

`guppi materialize` walked four dates: `raw/2026-09-09` extended with 0 entries (74),
`raw/2026-09-10` with 0 (157), `raw/2026-09-11` with 0 (84), `raw/2026-09-12` with 80 (163
entries). It read both Specs of the date, `0454/spec.md` and `1156/spec.md`. The librarian
appended 8 entries at synthesis; the yaml of 2026-09-12 now holds 171 entries, 49 decision
groups and 30 unparsed lines (all of session I).

`guppi generate`: 0 pages for 2026-09-09, 2026-09-10 and 2026-09-11; 76 for 2026-09-12;
exit 0, stderr empty. 11 entries of category `file` were skipped as Rule-class files
applied by hand; 8 `remove_criterion` entries printed "no Estimate holds a block" and
applied. `guppi cleanup` moved 1 page, stderr empty. Every entry of every yaml is
`applied`; none is `failed`.

| category | created | updated |
|---|---|---|
| decisions | 30 (`decision-case-70`, `71.1`, `72.1`–`72.6`, `73.1`–`73.10`, `74`, `75.1`, `75.2`, `76`–`84`) | 6 set `superseded`: `decision-case-63`, `64`, `65`, `67`, `68`, `69` |
| rules | 0 | 17: `rule-ask`, `rule-case-protocol`, `rule-claude-md`, `rule-documentation`, `rule-governed-files-hook`, `rule-handoff`, `rule-ledger-tail`, `rule-lint`, `rule-materialize`, `rule-page-generation`, `rule-pretask`, `rule-render-harness`, `rule-retro`, `rule-skill-hi`, `rule-spec-capture`, `rule-subagent-guppi`, `rule-work-mode` |
| estimates | 2 (`estimate-governed-files-hook-refuses` `failed`, `estimate-claude-md-rendered`, both of Case 71.1) | 11: `estimate-case-protocol-loaded`, `estimate-documentation-completes`, `estimate-generate-writes`, `estimate-handoff-dispatches`, `estimate-hi-writes-frontier`, `estimate-lint-catches`, `estimate-materialize-assembles`, `estimate-pretask-reconciles`, `estimate-render-harness-reproduces`, `estimate-retro-loads`, `estimate-spec-capture-appends` |
| lessons | 5 (`lesson-ledger-preview-in-ratification-taken-for-the-record`, `lesson-pretask-nested-estimate-exempt-from-the-line-check`, `lesson-estimates-live-clause-stale-at-first-render`, `lesson-hooks-blocked-pretooluse-leaves-no-posttooluse-event`, `lesson-materialize-lesson-line-source-dropped`) | 5 set `clustered` by synthesis (four of the new five, plus `lesson-materialize-standalone-estimate-keeps-criterion-as-a-field`); 1 archived by Case 70 |
| insights | 1 by synthesis (`insight-materialize-lift-loses-a-schema-field`, severity 2, `open`) | 3: `insight-ledger-line-written-unchecked` (severity 4), `insight-workflow-contract-change-leaves-its-derived-text-stale` (severity 3), `insight-ledger-hook-reads-only-the-final-text` (severity recounted to 1) |
| entities | 0 | 0 |

The 21 derived entries of Cases 73.2–73.10, 74, 75.1, 75.2 and 76 appended a `### case N`
block to the Criterion of their Estimate and set it `pending` (Case 72). Case 77 carried
`contract: same` and derived nothing. `deferred_by` was set on `rule-work-mode` and
`rule-subagent-guppi` (78), `rule-ledger-tail` (79), `rule-ask` (80), `rule-case-protocol`
(81), `rule-materialize` (82), `rule-governed-files-hook` (83), `rule-claude-md` and
`rule-render-harness` (84).

Readings recorded in this walk: `estimate-hi-writes-frontier`,
`estimate-materialize-assembles`, `estimate-pretask-reconciles` and `estimate-lint-catches`
`passed`; `estimate-render-harness-reproduces` and `estimate-governed-files-hook-refuses`
`failed`. `estimate-claude-md-rendered` took a `failed` result at birth and was set
`pending` by the derived update of Case 73.10 in the same run.

## What the next session does first

1. `uv run guppi render` once, by hand, then commit. Six governed files differ from their
   Rule pages after this run: `CLAUDE.md`, `.claude/agents/librarian-guppi.md` and the
   four skills (`hi`, `pre-task`, `retro`, `handoff`). `make lint` stops at that step
   until then; the handoff foretold it.
2. Take the readings the handoff names: at the start, `estimate-case-protocol-loaded` and
   `estimate-render-sync-reports`; against this report, `estimate-generate-writes` (the
   live half), `estimate-documentation-completes` and `estimate-synthesis-clusters`.
3. Plan Mode over the deferred list below.

## Deferred

1. **The live clauses of the two render readings** — Case 84, `rule-claude-md` and
   `rule-render-harness`: the live clause of `estimate-claude-md-rendered` and of
   `estimate-render-harness-reproduces` names a diff of marker lines only; the first
   render moved six files and 37 lines of text, and both readings failed on the clause.
   Related Insight `insight-workflow-contract-change-leaves-its-derived-text-stale`,
   severity 3. (postponed 1 time)
2. **Slice 3b: Work Mode** — Case 78, `rule-work-mode` and `rule-subagent-guppi`
   (placeholders, `draft`, two of the three lint orphans). The draft in `docs/migration/`
   has to be reconciled with 59.3 (no separate `plan.md`; the `tasks` blocks of the Spec)
   and with the fork clause. Related Insight `insight-harness-agent-visibility`, severity
   2. (postponed 5 times)
3. **`source` dropped between the ledger line and the page** — Case 82,
   `rule-materialize`: `parse_line` reads the braces of a lesson line into options and
   returns `tags` only, so every knowledge lesson is marked `incomplete: [source]` and its
   page is written without the field. Related Insight
   `insight-materialize-lift-loses-a-schema-field`, severity 2. (postponed 1 time)
4. **Archive in `ask-guppi`** — Case 80, `update` of `rule-ask` with its Estimate: a named
   slug checked against `vault/archived/`, which holds 22 pages. No related Insight.
   (postponed 5 times)
5. **Slice 3c: the raw lifecycle** — Case 79, `rule-ledger-tail`: `decided_by` and
   `origin` as a ledger pointer, `raw/<date>/` of an applied date archived by run stamp,
   the fresh ledger as the tail `/hi` prints, lint on both fields. No related Insight.
   (postponed 4 times)
6. **The field names of the `then` item** — Case 81, `rule-case-protocol`: Case 72.1 says
   `kind` and `slug` inside the `estimate` item, the Work Mode agent wrote `estimate_kind`
   and `estimate_slug`, and the code and the Render now disagree with the ratified text.
   No related Insight. (postponed 1 time)
7. **A guard refusal leaves no line in the event log** — Case 83,
   `rule-governed-files-hook`: `PostToolUse` does not fire for a tool a `PreToolUse` hook
   blocked, so a refusal is visible only on stderr unless the hook writes its own line.
   The fact is `lesson-hooks-blocked-pretooluse-leaves-no-posttooluse-event`, `new`, no
   Insight. (postponed 1 time)

Three items of the previous brief left this list: Case 75.1 supersedes 67 (the ledger
grammar in `case-schema.md` and `rule-case-protocol`), Case 74 supersedes 68 (the wording
of `rule-pretask` on a Case whose lines are all `defer`), Case 76 supersedes 69
(`materialize --show`). Cases 63, 64 and 65 are superseded by their re-defers 79, 78 and
80.

## Flags

- **Entries marked `incomplete` in this walk: 13.** Eleven of category `file` carry
  `incomplete: [then]` — the Rule-class file items of Cases 72.1 (`case-schema`, `index`,
  `glossary`), 72.2 (`estimates-schema`, `estimates-schema-yaml`, `decisions-schema`,
  `decisions-schema-yaml`), 73.1 (`index`, `glossary`) and 75.1 (`case-schema`, `index`),
  applied by hand in Work Mode. The handoff expected twelve; the yaml holds eleven. One
  entry carries `incomplete: [estimate]` and one `incomplete: [source]`; both were
  repaired by hand as the handoff instructs (item 2) and the mark was left standing.
- **The three entry edits of the handoff were made**, each one judgment: the derived
  update of Case 73.10 got `slug: estimate-claude-md-rendered` (it had `slug: null`
  because the page's `estimates` was empty when materialize ran); the derived update of
  Case 73.3 got `slug: estimate-hi-writes-frontier` in place of the page's first Estimate
  `estimate-hi-no-read-calls`; the knowledge lesson
  `lesson-hooks-blocked-pretooluse-leaves-no-posttooluse-event` got `fields.source` from
  the braces of its own ledger line.
- **A page written without `source`, not repaired:**
  `lesson-subagents-parallel-on-one-tree-red-mid-flight` (session I, `kind: knowledge`,
  its line carries a source). Its entry is applied; the handoff says not to edit the page.
  It is one of lint's 11 `source` findings.
- **Two failed Estimates:** `estimate-governed-files-hook-refuses` (`failed`, its live
  clause is Case 83) and `estimate-render-harness-reproduces` (`failed`, Case 84). Nine
  Estimates are `pending`: `estimate-case-protocol-loaded`, `estimate-claude-md-rendered`,
  `estimate-documentation-completes`, `estimate-generate-writes`,
  `estimate-handoff-dispatches`, `estimate-plan-mode-verified`,
  `estimate-render-sync-reports`, `estimate-retro-loads`, `estimate-spec-capture-appends`.
- **`estimate-claude-md-rendered` is `pending` after a `failed` reading.** Its create and
  the reading were folded into one entry (result `failed`), and the derived update of Case
  73.10 later in the same yaml set it `pending`. The failed result stands in its Result
  section.
- **Entries marked `near`, 4 added by this run.**
  `lesson-ledger-preview-in-ratification-taken-for-the-record` and
  `lesson-pretask-nested-estimate-exempt-from-the-line-check` near
  `lesson-spec-then-items-unchecked-against-ledger-lines`: all three are a Spec item and a
  ledger line that do not meet, but one is a line never written, one is a check that
  exempts a nested Estimate, and one is an item that was never in the block; not merged,
  all three now under one Insight. `lesson-estimates-live-clause-stale-at-first-render`
  near `lesson-estimates-criterion-stale-after-contract-change`: one is a criterion left
  quoting a dropped wording, the other a live clause written against a tree that changed
  the same session; not merged, clustered together.
  `lesson-materialize-lesson-line-source-dropped` near
  `lesson-materialize-standalone-estimate-keeps-criterion-as-a-field`: one drops a field
  at the parser, the other puts a section in the frontmatter; not merged, clustered
  together.
- **Synthesis: one Insight made, two extended, one judged.** New:
  `insight-materialize-lift-loses-a-schema-field` (severity 2) over
  `lesson-materialize-standalone-estimate-keeps-criterion-as-a-field` and
  `lesson-materialize-lesson-line-source-dropped`. Extended:
  `insight-ledger-line-written-unchecked` to four children (severity 4) and
  `insight-workflow-contract-change-leaves-its-derived-text-stale` to three (severity 3).
  Five lessons moved to `clustered`. Each `Proposal` is a suggestion, not a decision.
- **`insight-ledger-hook-reads-only-the-final-text` stands on one live child.** Case 70
  archived `lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn`, the
  second of its two members, and `generate` recounted severity to 1; the archived slug
  stays in `children`. Its Proposal was already the behaviour of Case 55.2, and the new
  `lesson-ledger-preview-in-ratification-taken-for-the-record` states the hook dropped
  nothing. The librarian did not put the new lesson under it and did not change its
  Pattern or its status: what becomes of an Insight whose evidence is withdrawn is a
  decision, not a librarian's judgment.
- **One new lesson stays `new` without a pair:**
  `lesson-hooks-blocked-pretooluse-leaves-no-posttooluse-event` (`knowledge`; compared
  with `lesson-hooks-sessionstart-cannot-block` and
  `lesson-hooks-messagedisplay-cannot-block`, which are about what an event may do, not
  about which event fires).
- **18 `clustered` lessons have no `## Insight` section**, five of them from this run. The
  synthesis update sets the `insight` field in the frontmatter; nothing writes the section
  `lessons/schema.md` requires. 18 of the 128 `schema` findings.
- **Two facts for the next Plan Mode, from the handoff, that are not defers:** `index.md`
  §4 still says `ref` is omitted on `update` and `delete` while every line now carries it;
  `case-schema.md` had two `raw/<date>/spec.md` mentions changed to the session folder by
  the Work Mode agent beyond the literal `change` lines of Case 73.
- **The contradiction the previous brief raised is gone.** The sentence of
  `rule-claude-md` that kept `rule-case-protocol` under `rule-plan-mode` "for the renderer
  only" is no longer in the page.
- **30 lines under `unparsed`**, all of session I, as the handoff says; the earlier count
  of 33 stands corrected in the yaml itself.
- **Stale defers:** `rule-work-mode` and `rule-subagent-guppi` have stood as placeholders
  since Case 29 (now 78) and `rule-ledger-tail` since Case 45 (now 79), without `kind`,
  `estimates` or `tags`. They are the three lint orphans.
- **No MOC candidate.** `entities-index.md` is empty; the vault holds no Entity page.
  Thirteen Rule pages are `draft`.
- **Lint.** `make lint` exits 1 at its first step with six lines: `CLAUDE.md`,
  `.claude/agents/librarian-guppi.md`, `.claude/skills/handoff/SKILL.md`,
  `.claude/skills/pre-task/SKILL.md`, `.claude/skills/retro/SKILL.md` and
  `.claude/skills/hi/SKILL.md` each "differs from its Rule page" — the render the next
  session runs first. `guppi index --check` exits 0. `guppi lint` run separately: 133
  findings, exit 1 — 128 `schema` (40 missing `## Context`, 38 `## Problem`, 18
  `## Insight`, 12 `tags`, 11 `source`, 3 `kind`, 3 `estimates`, 3 `## Estimates`), 3
  `orphan`, 1 `ref` (`rule-page-generation` names `decision-case-N` in its body, a
  literal), 1 `method`. 129 before this run.

## Readings at the close

- `make test` → 258 passed.
- `make lint` → exit 1 at `render --check`, six files; `guppi lint` → 133 findings, exit 1.
- Live pages, 240: rules 35 (22 `built`, 13 `draft`), entities 0, estimates 36 (25
  `passed`, 9 `pending`, 2 `failed`), lessons 34 (16 `new`, 18 `clustered`), insights 8
  (all `open`), decisions 127 (110 `current`, 17 `superseded`).
- `vault/archived/` holds 22 pages: 21 under `migration/2026-09-11/estimates/` and
  `lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn` under
  `migration/2026-09-12/lessons/`, moved by `guppi cleanup` in this run.
- `raw/2026-09-12/materialize.yaml`: 171 entries (163 from the two Specs and the ledger, 8
  appended at synthesis), 49 decision groups, 30 unparsed lines, 13 `incomplete` marks in
  this walk, no `new_tags`. `raw/2026-09-11`: 84 entries. `raw/2026-09-10`: 157 entries.
  `raw/2026-09-09`: 74 entries.
