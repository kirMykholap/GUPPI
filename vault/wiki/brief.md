# Brief — 2026-09-12, after session K (settings.json as a MOC, the render in the librarian's phase, Cases 85–99)

Written by the librarian.

## Where things stand

What the handoff of session K records under "What actually got done":

- One commit, `0ed3afb`: the code of the Spec, the two Rule-class files by hand, the
  `source` backfill on five lesson pages, and the render of the six governed files that
  `render --sync` wrote at session start (the first item of the previous brief).
- Ratified: 85.1–85.5, 86, 87, 88.1, 88.2, 89.1–89.4, 90.1–90.3, 91, 92, 99. Deferred:
  93–98.
- Code in four files: `render.py` (the bare splice into a comment-less file, the JSON gate
  before the write), `materialize.py` (`source` from the braces, the named Estimate),
  `pretask.py` (the fifth form finding), `guard.py` (the event line on a refusal).
- Readings passed and written in the session: `estimate-governed-files-hook-refuses`
  (`failed` → `passed`), `estimate-materialize-assembles`, `estimate-pretask-reconciles`.
- Not done: 19 of the Spec's 40 tasks. Eight readings wait on this run, two on the next
  session start; the rest are the pages this run writes.
- `make test` 267 green, `make style` clean. `guppi lint` was not run after the commit.
- Four `estimate_slug` lines were added to the Spec after the owner approved it (cases
  85.1, 88.1, 89.4, 87); the lesson is `lesson-pretask-runs-before-the-check-it-adds`.

`uv run guppi materialize` walked four dates: `raw/2026-09-09` extended with 0 entries
(74), `raw/2026-09-10` with 0 (157), `raw/2026-09-11` with 0 (84), `raw/2026-09-12` with
70. It read the three Specs of the date, `0454/spec.md`, `1156/spec.md` and
`1610/spec.md`. The librarian appended 3 entries at synthesis; the yaml of 2026-09-12 now
holds 244 entries, 74 decision groups and 30 unparsed lines.

`uv run guppi generate`: 0 pages for 2026-09-09, 2026-09-10 and 2026-09-11; 72 for
2026-09-12; exit 0, stderr empty. Two entries of category `file` were skipped as
Rule-class files applied by hand; 12 `remove_criterion` entries printed "no Estimate holds
a block" and applied. `uv run guppi cleanup` moved 0 pages, stderr empty. Every entry of
every yaml is `applied`; none is `failed`.

| category | created | updated |
|---|---|---|
| decisions | 25 (`decision-case-85.1`–`85.5`, `86`, `87`, `88.1`, `88.2`, `89.1`–`89.4`, `90.1`–`90.3`, `91`, `92`, `93`–`99`) | 7 set `superseded`: `decision-case-78`–`84` |
| rules | 3 (`rule-settings` MOC, `rule-default-mode`, `rule-permissions`) | 17: 10 by decision (`rule-case-protocol`, `rule-claude-md`, `rule-close`, `rule-documentation`, `rule-governed-files-hook`, `rule-harness`, `rule-hook-registry`, `rule-materialize`, `rule-pretask`, `rule-render-harness`), 6 by `deferred_by` (`rule-ask`, `rule-ledger-tail`, `rule-skill-hi`, `rule-subagent-guppi`, `rule-synthesis`, `rule-work-mode`), `rule-page-generation` `draft` → `built` by cascade |
| estimates | 3 (`estimate-settings`, `estimate-default-mode`, `estimate-permissions`, all `pending`) | 12: `estimate-case-protocol-loaded`, `estimate-claude-md-rendered`, `estimate-close-commits`, `estimate-documentation-completes`, `estimate-generate-writes`, `estimate-governed-files-hook-refuses`, `estimate-hook-registry-rendered`, `estimate-materialize-assembles`, `estimate-pretask-reconciles`, `estimate-render-harness-reproduces`, `estimate-render-sync-reports`, `estimate-synthesis-clusters` |
| lessons | 3 (`lesson-handoff-instructs-a-repair-the-librarian-rule-forbids`, `lesson-pretask-runs-before-the-check-it-adds`, `lesson-vault-lesson-absent-at-the-moment-it-applies`) | 2 set `clustered` by synthesis (`lesson-vault-lesson-absent-at-the-moment-it-applies`, `lesson-readings-after-librarian-invisible-to-next-hi`) |
| insights | 1 by synthesis (`insight-session-vault-knowledge-not-loaded`, severity 2, `open`) | 1: `insight-ledger-hook-reads-only-the-final-text`, severity recounted 1 → 2 |
| entities | 0 | 0 |

The three checks the handoff asks for, after `generate`:

- `rule-settings.children` is `[rule-default-mode, rule-permissions, rule-hook-registry]`,
  no duplicate.
- `rule-harness.children` is `[rule-render-harness, rule-settings, rule-lint, rule-index,
  rule-governed-files-hook, rule-claude-md]`; `rule-hook-registry` is gone from it and its
  `parent` is `rule-settings`.
- The pages updated twice kept every criterion block:
  `estimate-render-harness-reproduces` holds `### case 85.1`, `88.1`, `89.4`;
  `estimate-materialize-assembles` holds `73.5`, `76`, `87`, `90.1`;
  `estimate-documentation-completes` holds `73.8`, `89.1`, `90.3`. No `replace` pair was
  reported absent or not unique; `generate` wrote nothing to stderr, so the Case 99
  replaces on `estimate-hook-registry-rendered`, `rule-pretask`, `rule-materialize` and
  `rule-harness` all applied, the `rule-pretask` pair included.

Readings recorded in this walk: `estimate-render-sync-reports`, `estimate-generate-writes`,
`estimate-synthesis-clusters`, `estimate-governed-files-hook-refuses`,
`estimate-materialize-assembles` and `estimate-pretask-reconciles` `passed`;
`estimate-documentation-completes` `failed` (the librarian's run of session J, one clause:
three yaml entries edited by hand).

`uv run guppi render` was not run, and the commit holds `vault/` only, as the handoff
instructs. Cases 89.1 and 89.2 take effect at the next session.

## What the next session does first

1. `/hi` runs `render --sync`: three governed files differ from their Rule pages —
   `.claude/settings.json` (new, from `rule-settings` and its three children),
   `.claude/agents/librarian-guppi.md` (89.1, 90.3) and `.claude/skills/pre-task/SKILL.md`
   (90.2). `make lint` stops at that step until they are written and committed.
2. Take the readings the handoff names against this run: `estimate-settings`,
   `estimate-permissions`, `estimate-default-mode`, `estimate-hook-registry-rendered`,
   `estimate-documentation-completes`, `estimate-close-commits`,
   `estimate-render-harness-reproduces`, `estimate-claude-md-rendered`; and at session
   start `estimate-case-protocol-loaded` and `estimate-render-sync-reports`.
3. Plan Mode over the deferred list below.

## Deferred

1. **A render inside `/hi`, after the pull** — Case 98, `rule-skill-hi`: what arrives from
   outside the session reaches its files in the same session. Related Insight
   `insight-workflow-contract-change-leaves-its-derived-text-stale`, severity 3.
   (postponed 1 time)
2. **Slice 3b: Work Mode** — Case 93, `rule-work-mode` and `rule-subagent-guppi`
   (placeholders, `draft`, two of the three lint orphans): the Spec as tasks with code,
   the ticked boxes, what a subagent may do, and the fork that comes back as a Case.
   Related Insight `insight-harness-agent-visibility`, severity 2. (postponed 6 times)
3. **Slice 3c: the lifecycle of `raw/`** — Case 95, `rule-ledger-tail`: an applied date
   archived by run stamp, the fresh ledger the tail prints at `/hi`, `decided_by` and
   `origin` under lint. Related Insight `insight-session-vault-knowledge-not-loaded`,
   severity 2. (postponed 5 times)
4. **What becomes of an Insight when its children are archived** — Case 97,
   `rule-synthesis`: the count, the status, and who decides. Related Insight
   `insight-ledger-hook-reads-only-the-final-text`, severity 1. (postponed 1 time)
5. **The archive in `ask-guppi`** — Case 94, `rule-ask`: the archive is part of the vault
   the agent answers from, and a named slug is checked against it; `vault/archived/` holds
   22 pages. No related Insight. (postponed 6 times)
6. **The `## Insight` section of a clustered lesson** — Case 96, `rule-synthesis`: the
   synthesis update sets the `insight` field and nothing writes the section
   `lessons/schema.md` requires; 20 lessons carry the gap. The `purpose` of this defer
   reads "A synthesis entry carries the" in the yaml and on `decision-case-96` — see
   Flags. No related Insight. (postponed 1 time)

Every item of the previous brief's list left it: Case 93 supersedes 78, 94 supersedes 80,
95 supersedes 79; Cases 85.1, 88.1 and 89.4 retired 84 (the live clauses of the two render
readings), 86 and 92 retired 81 (the field names of the `then` item), 87 retired 82
(`source` dropped at the parser), 91 retired 83 (a guard refusal with no event line).

## Flags

- **Entries marked `incomplete` in this walk: 2**, both of category `file` with
  `incomplete: [then]` — `case-schema` and `index`, the Rule-class file items applied by
  hand in Work Mode. No entry of this walk is marked `failed`.
- **The entries of the two earlier runs on this date keep their marks**, three of them
  `incomplete: [source]` and one `incomplete: [estimate]`; nothing in the yaml was
  repaired, as the handoff asks.
- **One entry marked `near`, by this run's index check.** `rule-default-mode` ("Keeps a
  session from writing anything before a Case is ratified") near `rule-case-protocol`
  ("Prevents a decision from being acted on before it is ratified, or ratified without its
  content in view"): the same aim, a different file and a different enforcement — one is
  the `defaultMode` key of `settings.json`, the other the protocol text of `CLAUDE.md`.
  Not merged. `rule-settings` and `rule-permissions` were compared with every line of
  `rules-index.md` and marked neither same nor near.
- **The `purpose` of the defer of Case 96 is cut short.** The yaml entry and
  `decision-case-96` both carry `purpose: A synthesis entry carries the`. The handoff
  names the subject: the missing `## Insight` section on a clustered lesson. Left as it
  is.
- **`estimate-documentation-completes` is `pending` after a `failed` reading.** The
  reading (line 168) failed on one clause — three yaml entries edited by hand in the
  librarian's run of session J — and the derived updates of Cases 89.1 and 90.3 later in
  the same walk set the Estimate `pending`. The failed result stands in its Result
  section. The fact is `lesson-handoff-instructs-a-repair-the-librarian-rule-forbids`,
  `new`.
- **No Estimate is `failed`.** 14 are `pending`: `estimate-case-protocol-loaded`,
  `estimate-claude-md-rendered`, `estimate-close-commits`, `estimate-default-mode`,
  `estimate-documentation-completes`, `estimate-handoff-dispatches`,
  `estimate-hook-registry-rendered`, `estimate-permissions`, `estimate-plan-mode-verified`,
  `estimate-render-harness-reproduces`, `estimate-render-sync-reports`,
  `estimate-retro-loads`, `estimate-settings`, `estimate-spec-capture-appends`.
- **`insight-ledger-hook-reads-only-the-final-text` was recounted from severity 1 to 2**
  while one of its two children,
  `lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn`, sits in
  `vault/archived/migration/2026-09-12/lessons/`. `insights/schema.md` defines `severity`
  as the count of children whose status is not `archived`. This is the subject of the
  deferred Case 97.
- **Synthesis: one Insight made, none extended.**
  `insight-session-vault-knowledge-not-loaded` (severity 2, `open`) over
  `lesson-readings-after-librarian-invisible-to-next-hi` (session F, `new` until now) and
  `lesson-vault-lesson-absent-at-the-moment-it-applies` (session K): in both a fact was in
  the record and absent from the session that needed it. Its `Proposal` is a suggestion,
  not a decision.
- **Two new lessons stay `new` without a pair:**
  `lesson-handoff-instructs-a-repair-the-librarian-rule-forbids` (compared with
  `lesson-librarian-reads-beyond-the-four-inputs`, which is about the frame contradicting
  itself, and with `insight-librarian-frame-omits-required-reads`) and
  `lesson-pretask-runs-before-the-check-it-adds` (compared with
  `lesson-pretask-nested-estimate-exempt-from-the-line-check`, a coverage gap in the
  check, and with `insight-workflow-contract-change-leaves-its-derived-text-stale`).
- **20 `clustered` lessons have no `## Insight` section**, three of them from this run.
  20 of the 125 `schema` findings; Case 96 is its defer.
- **Four `method` findings, three of them new.** `estimate-default-mode` names no `tests/`
  file and does not say by hand; `estimate-settings`, a MOC's Estimate, names no `make
  <target>`; `estimate-documentation-completes` and `estimate-harness-pipeline` say "by
  hand" while another Estimate names a test file. The previous run had one `method`
  finding.
- **Stale defers:** `rule-work-mode` and `rule-subagent-guppi` have stood as placeholders
  since Case 29 (now 93) and `rule-ledger-tail` since Case 45 (now 95), without `kind`,
  `estimates` or `tags`. They are the three lint orphans.
- **No MOC candidate.** `entities-index.md` is empty; the vault holds no Entity page.
  Sixteen Rule pages are `draft`.
- **30 lines under `unparsed`**, all of session I, unchanged by this walk.
- **`new_tags` holds one entry, `tests`**, already in `tags.md`. The handoff declares no
  new tag; the tags used by this run's creates — `harness`, `render`, `session`,
  `workflow` — are all registered.
- **Lint.** `make lint` exits 1 at its first step with three lines:
  `.claude/agents/librarian-guppi.md`, `.claude/skills/pre-task/SKILL.md` and
  `.claude/settings.json` each "differs from its Rule page" — the render the next session
  runs first. `guppi index --check` exits 0. `guppi lint` run separately: 133 findings,
  exit 1 — 125 `schema` (40 missing `## Context`, 38 `## Problem`, 20 `## Insight`, 12
  `tags`, 6 `source`, 3 `kind`, 3 `estimates`, 3 `## Estimates`), 4 `method`, 3 `orphan`,
  1 `ref` (`rule-page-generation` names `decision-case-N` in its body, a literal). 133
  before this run as well.

## Readings at the close

- `make test` → 267 passed.
- `make lint` → exit 1 at `render --check`, three files; `guppi lint` → 133 findings, exit
  1; `guppi index --check` → exit 0.
- Live pages, 275: rules 38 (22 `built`, 16 `draft`), entities 0, estimates 39 (25
  `passed`, 14 `pending`, 0 `failed`), lessons 37 (17 `new`, 20 `clustered`), insights 9
  (all `open`), decisions 152 (128 `current`, 24 `superseded`).
- `vault/archived/` holds 22 pages: 21 under `migration/2026-09-11/estimates/` and
  `lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn` under
  `migration/2026-09-12/lessons/`. `cleanup` moved none in this run.
- `raw/2026-09-12/materialize.yaml`: 244 entries (241 from the three Specs and the ledger,
  3 appended at synthesis), 74 decision groups, 30 unparsed lines, 2 `incomplete` marks in
  this walk, 1 `new_tags` entry. `raw/2026-09-11`: 84 entries. `raw/2026-09-10`: 157
  entries. `raw/2026-09-09`: 74 entries.
