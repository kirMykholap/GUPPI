# Brief — 2026-09-12, after session I (the artifacts of Plan Mode, Cases 58–69)

Written by the librarian.

## Where things stand

What the handoff of session I records under "What actually got done":

- Commits, in order: `f2b2d83` the render of four files, the ledger tail of session H, the
  Spec and the Frontier; `8404072` Cases 59.4 and 60 (`generate`, `lint`, the decisions
  schema, 78 pages migrated, `## Given` on ten pages); `7c745f3` Cases 59.8, 60, 61
  (`materialize`); `0ff3af5` Cases 59.6, 59.7 (`guppi guard`, `render --sync`, BOM in
  `read_payload`); `2b7dd42` Cases 59.1–59.3, 59.6 (`guppi pretask --check`); `70588a8`
  the Rule-class files by hand, `sprint.md`, the Spec ticked, the ledger; `a35f851` the
  Retro.
- `make test` 211 green, `make style` clean, `guppi pretask --check` on the Spec prints
  nothing. Readings taken and passed: `estimate-spec-capture-appends`,
  `estimate-documentation-completes` (Slice 3 closes), `estimate-lint-catches`,
  `estimate-materialize-assembles`, `estimate-retro-loads`.
- Not done, named for the next session: one manual `uv run guppi render` at its start; the
  live readings of `estimate-pretask-reconciles`, `estimate-hi-writes-frontier`,
  `estimate-generate-writes` (the live half), `estimate-governed-files-hook-refuses`,
  `estimate-render-sync-reports`, `estimate-claude-md-rendered` and
  `estimate-render-harness-reproduces`.
- `sprint.md` was changed in Work Mode under Cases 58 and 59.5: Slice 3 closed, the four
  Slice-5 items moved there. The librarian did not touch it, as the handoff instructs.
- The agent's memory directory is empty (Case 62). `vault/Untitled.canvas`, an empty file
  Obsidian left, was deleted so the handoff gate passed.

`guppi materialize` walked four dates: `raw/2026-09-09` extended with 0 entries (74),
`raw/2026-09-10` with 0 (157), `raw/2026-09-11` with 5 (84 entries, 9 decision groups),
`raw/2026-09-12` written with 76 entries and 19 decision groups. 30 lines of 2026-09-12
stand under `unparsed`. The librarian appended 9 entries at synthesis; the yaml of
2026-09-12 now holds 85.

`guppi generate`: 0 pages for 2026-09-09, 0 for 2026-09-10, 8 for 2026-09-11, 64 for
2026-09-12; exit 0, stderr empty. It registered the tag `tests` in `tags.md`. 13 entries
of category `file` were skipped as Rule-class files applied by hand. `guppi cleanup`
moved 0 pages, stderr empty.

| category | created | updated |
|---|---|---|
| decisions | 19 (`decision-case-58`, `59.1`–`59.8`, `60`–`69`) | 2 (`decision-case-29`, `decision-case-45`, superseded by 64 and 63) |
| rules | 2 (`rule-claude-md`, `rule-governed-files-hook`, both `draft`, both `estimates: []`) | 19: `rule-ask`, `rule-brief`, `rule-case-protocol`, `rule-documentation`, `rule-harness`, `rule-hook-registry`, `rule-ledger-tail`, `rule-lint`, `rule-materialize`, `rule-page-generation`, `rule-plan-mode`, `rule-pretask`, `rule-pretask-hook`, `rule-render-harness`, `rule-retro`, `rule-skill-hi`, `rule-spec-capture`, `rule-subagent-guppi`, `rule-work-mode` |
| estimates | 2 (`estimate-hi-writes-frontier`, `estimate-render-sync-reports`, both `pending`) | 8: `estimate-documentation-completes`, `estimate-generate-writes`, `estimate-lint-catches`, `estimate-materialize-assembles`, `estimate-pretask-reconciles`, `estimate-render-harness-reproduces`, `estimate-retro-loads`, `estimate-spec-capture-appends` |
| lessons | 7 (6 of 2026-09-12: `lesson-plan-mode-exited-per-frontier-item`, `lesson-bash-tool-heredoc-escapes-interpreted`, `lesson-render-governed-file-updated-as-rule-class-file`, `lesson-ledger-decision-line-written-without-the-case-word`, `lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn`, `lesson-subagents-parallel-on-one-tree-red-mid-flight`; 1 of 2026-09-11: `lesson-lint-decision-target-archived-counts-as-missing`) | 6 by synthesis, all set `clustered`: `lesson-ledger-hook-misses-a-reply-ending-in-a-tool-call`, `lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn`, `lesson-estimates-criterion-stale-after-contract-change`, `lesson-render-governed-file-updated-as-rule-class-file`, `lesson-spec-then-items-unchecked-against-ledger-lines`, `lesson-ledger-decision-line-written-without-the-case-word` |
| insights | 3 by synthesis (`insight-ledger-hook-reads-only-the-final-text`, `insight-workflow-contract-change-leaves-its-derived-text-stale`, `insight-ledger-line-written-unchecked`; severity 2, `open`) | 0 |
| entities | 0 | 0 |

The four readings of the 2026-09-11 walk, written after the previous librarian's commit:
`estimate-documentation-completes` `failed` (one read outside the four inputs and the four
reasons, not named in the report), `estimate-synthesis-clusters` `passed`,
`estimate-generate-writes` `passed`, `estimate-materialize-assembles` `passed`. Of the
five readings of 2026-09-12, `estimate-documentation-completes` was set back to `pending`
by Case 58 in the same walk, after its `passed` result was written; `estimate-lint-catches`
and `estimate-materialize-assembles` likewise by 59.4 and 61. `estimate-retro-loads` and
`estimate-spec-capture-appends` stand `passed`, then updated by Case 66.

`deferred_by` was set on `rule-ledger-tail` (63), `rule-work-mode` and
`rule-subagent-guppi` (64), `rule-ask` (65), `rule-case-protocol` (67), `rule-pretask`
(68), `rule-materialize` (69). No page was archived.

## What the next session does first

1. `uv run guppi render` once, by hand, then commit: `CLAUDE.md`,
   `.claude/settings.json`, `.claude/agents/librarian-guppi.md` and the three skills
   differ from their Rule pages. `make lint` stops at that step until then.
2. Take the readings the handoff names: `estimate-claude-md-rendered` and
   `estimate-render-harness-reproduces` at that render, `estimate-render-sync-reports` the
   session after, `estimate-hi-writes-frontier` at `/hi`, `estimate-pretask-reconciles` at
   `/pre-task`, `estimate-governed-files-hook-refuses` on one refused Edit,
   `estimate-generate-writes` (the live half) against this run,
   `estimate-documentation-completes` and `estimate-synthesis-clusters` against this
   report.
3. Two Estimates ratified in the Cases of session I have no page and no yaml entry:
   `estimate-claude-md-rendered` (Case 66, nested under `rule-claude-md`) and
   `estimate-governed-files-hook-refuses` (Case 59.6). Both Rule pages are `draft` with
   `estimates: []`, so neither can become `built`.
4. Read `guppi/ledger.py` against the transcript of session I, as the owner asks: the two
   ledger-hook lessons share one root cause and are now clustered under
   `insight-ledger-hook-reads-only-the-final-text` — the writer sees the last text of a
   turn, not the turn. Session F's lesson is the case where no `Stop` fires at all (the
   turn ends in a tool call); session I's is the case where `Stop` fires and the block sits
   in an intermediate text message of the turn. The question to settle in
   `transcript_texts` and its main-agent filter: is that message absent from what the
   function collects, or collected and dropped. If present, collect every assistant text
   message of the `hi` window; if absent, the writer needs a second event beside `Stop`.
5. Plan Mode over the deferred list below.

## Deferred

1. **Slice 3b: Work Mode** — Case 64, `rule-work-mode` and `rule-subagent-guppi`
   (placeholders, `draft`, lint orphans). The draft in `docs/migration/` has to be
   reconciled with 59.3 (no separate `plan.md`; the `tasks` blocks of the Spec) and with
   the fork clause (a fork becomes a short-form Case under `## Deferred`, worked next
   session). Related Insight `insight-harness-agent-visibility`, severity 2. (postponed 4
   times)
2. **The ledger grammar** — Case 67, `update` of `case-schema.md` and
   `rule-case-protocol`: the table "What a Case produces" shows
   `decision[case_id][kind][slug]`, read literally by the agent; it should show
   `decision[case N][kind][slug]{ref:…}{tags:…}`. Related Insight
   `insight-ledger-line-written-unchecked`, severity 2. (postponed 1 time)
3. **Archive in `ask-guppi`** — Case 65, `update` of `rule-ask` with its Estimate: a named
   slug checked against `vault/archived/`, which holds 21 pages. Case 31 discussion. No
   related Insight. (postponed 4 times)
4. **Slice 3c: the raw lifecycle** — Case 63, `rule-ledger-tail`: `decided_by` and
   `origin` as a ledger pointer, `raw/<date>/` of an applied date archived by run stamp,
   the fresh ledger as the tail `/hi` prints, lint on both fields. The tail of session H
   reached session I through the agent's memory file, which Case 62 deletes. No related
   Insight. (postponed 3 times)
5. **The wording of `rule-pretask`** — Case 68: 59.3 says the check reports "a Case that
   has decision lines and no `tasks` block"; the code exempts a Case whose lines are all
   `defer` (commit `2b7dd42`), the ratified wording does not. An `update` of the Render
   and of the criterion of `estimate-pretask-reconciles`. No related Insight. (postponed 1
   time)
6. **A show-only mode of `materialize`** — Case 69: `--check` or `--show` prints the
   entries, the unparsed lines and the incomplete marks and writes nothing, so the agent
   and pre-task can look before the librarian runs. An `update` of `rule-materialize` with
   its Estimate. No related Insight. (postponed 1 time)

The four Slice-5 items of the previous brief (`/grill-me` without a page, `origin` and
`git pull` on `migration`, `gh` not logged in, the fate of `vault/parked/`,
`vault/archive/`, `docs/superpowers/` and the 2026-08 documents) left this list for
`sprint.md` under Cases 58 and 59.5. Cases 29 and 45 left it: Case 64 supersedes 29, Case
63 supersedes 45.

## Flags

- **Entries marked `incomplete`, 2026-09-12: 15.** Two lessons lack `source`:
  `lesson-bash-tool-heredoc-escapes-interpreted`, `lesson-subagents-parallel-on-one-tree-red-mid-flight`
  (both `kind: knowledge`, where `source` is required; two of lint's 11 `source` findings
  are theirs). Thirteen entries
  of category `file` carry `incomplete: [then]` — `index` (4), `case-schema` (5),
  `glossary` (2), `decisions-schema` and `decisions-schema-yaml` — the Rule-class file
  items of Cases 59.2, 59.3, 59.4, 59.5, 59.8, 60, 62 and 66, whose `then` blocks were
  applied by hand in Work Mode. No decision group is `incomplete`.
- **Entries marked `incomplete` in the earlier yamls stand unchanged:** ten in
  2026-09-10, all 74 entries and all 34 decision groups of 2026-09-09 (the backfill debt).
  The 2026-09-11 walk added none.
- **No entry is marked `failed`; every entry of every yaml is applied.**
- **No Estimate page carries `failed`.** `estimate-documentation-completes` took the
  `failed` result of the 2026-09-11 reading and was set `pending` by Case 58 in this run.
  Seven Estimates are `pending`: `estimate-documentation-completes`,
  `estimate-generate-writes`, `estimate-hi-writes-frontier`, `estimate-plan-mode-verified`,
  `estimate-pretask-reconciles`, `estimate-render-harness-reproduces`,
  `estimate-render-sync-reports`.
- **Two ratified Estimates have no entry and no page.** Case 66 gives `rule-claude-md` a
  nested `estimate-claude-md-rendered`; Case 59.6 names
  `estimate-governed-files-hook-refuses` in its `then`. Neither is in the yaml, neither
  page exists, and both Rule pages carry `estimates: []`. This is the class of
  `lesson-spec-then-items-unchecked-against-ledger-lines`.
- **Contradiction.** The "How it works" section of `rule-claude-md` says "`rule-case-protocol`
  keeps its parent `rule-plan-mode`; it is listed here for the renderer only". Case 66,
  ratified after 59.8, moved `rule-case-protocol` under `rule-claude-md` and out of
  `rule-plan-mode`'s children, and the frontmatter of both pages now says so. The sentence
  is stale.
- **30 lines under `unparsed`, not 33.** The handoff, Case 67 and
  `lesson-ledger-decision-line-written-without-the-case-word` all say 33 malformed decision
  lines; `raw/2026-09-12/materialize.yaml` holds 30, lines 3–11 and 13–33 of the ledger.
  Three of the 33 are not in the file.
- **Entries marked `near`, 2 added by this run.** `rule-governed-files-hook` near
  `rule-render-harness`: the new page blocks a hand edit of a governed file with a
  `PreToolUse` hook, `rule-render-harness` keeps page and file one text with
  `render --check`; different `when`, not merged.
  `lesson-bash-tool-heredoc-escapes-interpreted` near `lesson-hooks-windows-stdin-encoding`:
  both are the Windows text layer between the harness and python, and the cp1252 console is
  named in both, but one is the shell interpreting backslash escapes before python reads
  the script and the other is a cp1252 stdin wrapper with `surrogateescape`; two fixes, not
  clustered.
- **Three Insights were made at synthesis, all severity 2, `open`.**
  `insight-ledger-hook-reads-only-the-final-text` over
  `lesson-ledger-hook-misses-a-reply-ending-in-a-tool-call` and
  `lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn` (the previous
  librarian compared the first with `lesson-ledger-hook-hi-lost-at-midnight` and did not
  cluster; the new lesson, not that one, shares its cause).
  `insight-workflow-contract-change-leaves-its-derived-text-stale` over
  `lesson-estimates-criterion-stale-after-contract-change` and
  `lesson-render-governed-file-updated-as-rule-class-file`.
  `insight-ledger-line-written-unchecked` over
  `lesson-spec-then-items-unchecked-against-ledger-lines` and
  `lesson-ledger-decision-line-written-without-the-case-word`. Six lessons moved to
  `clustered`. Each `Proposal` is a suggestion, not a decision.
- **Three new lessons stay `new` without a pair.**
  `lesson-plan-mode-exited-per-frontier-item` (compared with
  `lesson-frame-read-clauses-omit-candidate-check-and-brief` and
  `insight-librarian-frame-omits-required-reads`: the shape is a rule silent on a case, the
  pattern of that Insight is the librarian's read clauses only);
  `lesson-subagents-parallel-on-one-tree-red-mid-flight` (`knowledge`; the owner takes it
  with Slice 3b); `lesson-lint-decision-target-archived-counts-as-missing` (compared with
  `insight-harness-yaml-entry-shape-assumed`: an inconsistent known set between two lint
  checks, not an assumed entry shape).
- **14 `clustered` lessons have no `## Insight` section**, six of them new. The synthesis
  update sets the `insight` field in the frontmatter; nothing writes the section
  `lessons/schema.md` requires. 14 of the 124 `schema` findings.
- **The 25 lint findings of class `decision` are gone.** They were the subject of
  `lesson-lint-decision-target-archived-counts-as-missing`, created in this run from the
  2026-09-11 ledger: `check_decision` resolved a `target_slug` against live pages only.
  `guppi lint` reports no `decision` finding now; whether Case 59.4 fixed the lookup or
  dropped the check is not recorded in any input.
- **Stale defers:** `rule-work-mode` and `rule-subagent-guppi` have stood as placeholders
  since Case 29 (now 64) without `kind`, `estimates` or `tags`; `rule-ledger-tail` since
  Case 45 (now 63). They are the three lint orphans.
- **No MOC candidate.** `entities-index.md` is empty; the vault holds no Entity page.
  Eleven Rule pages are `draft`, two of them created in this run.
- **Lint.** `make lint` exits 1 at its first step with six lines: `CLAUDE.md`,
  `.claude/agents/librarian-guppi.md`, `.claude/settings.json`,
  `.claude/skills/pre-task/SKILL.md`, `.claude/skills/retro/SKILL.md`,
  `.claude/skills/hi/SKILL.md` each "differs from its Rule page". `guppi lint` run
  separately: 129 findings, exit 1 — 124 `schema` (40 missing `## Context`, 38 missing
  `## Problem`, mostly the 2026-09-09 decision backfill; 14 `## Insight`; 12 `tags`; 11
  `source`; 3 `kind`; 3 `estimates`; 3 `## Estimates`), 3 `orphan`, 1 `ref`
  (`rule-page-generation` names `decision-case-N` in its body, a literal), 1 `method`. 146
  before this run. No finding of class `decision` remains: the 25 the previous brief
  reported, and the two `ref` findings on `decision-case-59.4` and `decision-case-60` the
  handoff foretold, are gone — `guppi lint` was changed by Case 59.4 in this session, and
  this run created those two decision pages.

## Readings at the close

- `make test` → 211 passed.
- `make lint` → exit 1 at `render --check`, six files; `guppi lint` → 129 findings, exit 1.
- Live pages, 203: rules 35 (24 `built`, 11 `draft`), entities 0, estimates 34 (27
  `passed`, 7 `pending`, 0 `failed`), lessons 30 (16 `new`, 14 `clustered`), insights 7
  (all `open`), decisions 97 (86 `current`, 11 `superseded`).
- `vault/archived/` holds 21 pages, all under `migration/2026-09-11/estimates/`; `guppi
  cleanup` moved none in this run.
- `raw/2026-09-12/materialize.yaml`: 85 entries (76 from the ledger, 9 appended at
  synthesis), 19 decision groups, 30 unparsed lines, one `new_tags` entry (`tests`,
  registered). `raw/2026-09-11/materialize.yaml`: 84 entries, 9 decision groups, all
  applied. `raw/2026-09-10`: 157 entries. `raw/2026-09-09`: 74 entries.
