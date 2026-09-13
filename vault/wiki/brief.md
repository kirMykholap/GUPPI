# Brief — 2026-09-13, after session L (Slice 3c: the archive of raw/, the ledger of a session, Cases 100–109)

Written by the librarian.

## Where things stand

What the handoff of session L records under "What actually got done":

- Ratified and coded: Cases 100 (the archive of an applied unit, `guppi archive`), 101
  (`guppi tail`, the placeholder fill, the `/hi` tail), 102 (one root `vault/archive/`,
  `cleanup` under the session of the run), 103 (the ledger of a session: hook,
  materialize, generate, pretask, lint, the map and five schemas), 104 (the three
  cascades), 105 (the slug against the archive: `ask-guppi`, `exists` by Case, `find`
  into the archive), 109 (rule-retro, rule-claude-md, insights schema). Deferred: 106,
  107, 108.
- Code: `guppi/archive.py`, `guppi/tail.py` new; `ledger.py`, `materialize.py`,
  `generate.py`, `pretask.py`, `lint.py`, `cleanup.py`, `cli.py` changed; tests
  `test_archive.py`, `test_tail.py` new, six others extended: 299 green (267 before),
  `make style` clean.
- Files: the old `vault/archive/` (August, 49 folders) and `vault/raw/notes/` removed;
  `vault/archived/migration/` moved to `vault/archive/migration/`; the four dates
  09-09…09-12 archived live by `guppi archive` under `vault/archive/migration/<date>/raw/`
  with the session folders of 09-12 beside as `<HHMM>/raw/`. `guppi lint` 133 findings
  before and after, `render --check` 0, `index --check` 0.
- By hand: `index.md` §1 and §4, glossary (six rows), `schema.md` of entities, rules,
  estimates, lessons, decisions, insights, `sprint.md` (Slice 3c rewritten, Done-when 1,
  Slice 5).
- Readings taken in the session: `estimate-case-protocol-loaded`,
  `estimate-render-sync-reports`, `estimate-default-mode`, `estimate-hook-registry-rendered`,
  `estimate-permissions`, `estimate-render-harness-reproduces`, `estimate-claude-md-rendered`
  (the date-level ledger); `estimate-raw-archive`, `estimate-lint-catches`,
  `estimate-ledger-write-lifts` (the session ledger). Lessons: the transcript, the
  heredoc trap.
- Commits: `44e4e37`, `c08c878`, `57d68e2`, `5c4ea2a`.
- Not done: 21 tasks of the Spec, all readings — 12 against this librarian run, 6 against
  the next session start, plus the two render checks (`rule-cleanup` sentence, `CLAUDE.md`
  path) that this run's render answers.

`uv run guppi materialize` walked two units of one date: `raw/2026-09-13/materialize.yaml`
with 79 entries (the date-level ledger, 49 lines, and `0652/spec.md`) and
`raw/2026-09-13/0652/materialize.yaml` with 4 entries (the session ledger, 4 lines, the
same Spec). The four earlier dates sit in `vault/archive/migration/<date>/raw/` and were
not walked. The librarian appended 2 entries at synthesis to each yaml: 81 and 6 entries
now, 32 decision groups, 0 unparsed lines.

`uv run guppi generate`: 107 pages for `2026-09-13`, 8 for `2026-09-13/0652`; exit 0,
stderr empty. Nine `file` entries were skipped as Rule-class files applied by hand
(`index` twice, `glossary` four times, `entities-schema`, `rules-schema`,
`estimates-schema`, `lessons-schema`, `decisions-schema`, `insights-schema`); nine
`remove_criterion` entries printed "no Estimate holds a block" (cases 95, 100.5 twice, 97,
94, 98, 93 twice, 96) and applied. The two deletes outside the vault, `raw-notes` (100.6)
and `old-archive` (102.1), printed "outside the vault, nothing to archive" and applied.
`uv run guppi cleanup` moved 32 pages, stderr empty. `uv run guppi render` wrote six
files, stderr empty. Every entry of both yamls is `applied`; none is `failed`.

| category | created | updated |
|---|---|---|
| decisions | 32 (`decision-case-100.1`–`100.6`, `101.1`–`101.5`, `102.1`, `102.2`, `102.4`, `103.1`–`103.6`, `104.1`–`104.3`, `105.1`–`105.3`, `106`, `107`, `108`, `109.1`–`109.3`) | 32 set `archived` by the cascade of 104.1 and moved by `cleanup`: the 24 `superseded` of earlier sessions (`15.2`, `22`, `23.1`, `24.2`, `29`, `30`, `31`, `38.1`, `45`, `50`, `51`, `63`, `64`, `65`, `67`, `68`, `69`, `78`–`84`), the two superseded inside this Spec (`100.3`, `100.5`) and the six superseded by this session's Cases (`93`, `94`, `95`, `96`, `97`, `98`) |
| rules | 1 (`rule-raw-archive`, `built`) and 1 filled over its placeholder (`rule-ledger-tail`, History `created over placeholder`, `kind: Leaf`, `estimates: [estimate-ledger-tail]`, no `deferred_by`) | 20: 14 by decision (`rule-documentation`, `rule-lint`, `rule-cleanup`, `rule-page-generation`, `rule-skill-hi`, `rule-ledger-write`, `rule-materialize`, `rule-pretask`, `rule-ask`, `rule-retro`, `rule-claude-md`, and `deferred_by` on `rule-synthesis`, `rule-work-mode`, `rule-subagent-guppi`), 6 by status cascade only (`rule-case-protocol`, `rule-default-mode`, `rule-hook-registry`, `rule-permissions`, `rule-render-harness` `draft` → `built`; `rule-ask`, `rule-cleanup`, `rule-materialize`, `rule-page-generation`, `rule-pretask`, `rule-skill-hi` `built` → `draft` on a `pending` block) |
| estimates | 2 (`estimate-raw-archive` `passed` by the session ledger, `estimate-ledger-tail` `pending`) | 20: 13 criterion blocks (`estimate-documentation-completes` +100.2, `estimate-lint-catches` +100.3 then −100.3 +103.5, `estimate-generate-writes` +101.1, 104.1, 104.2, 104.3, 105.3, `estimate-hi-no-read-calls` +101.3, `estimate-hi-writes-frontier` +101.4, `estimate-cleanup-moves` +102.2, `estimate-ledger-write-lifts` +103.1, `estimate-materialize-walks-dates` +103.2, `estimate-generate-walks-dates` +103.3, `estimate-pretask-reconciles` +103.4, `estimate-ask-finds` +105.1, `estimate-materialize-assembles` +105.2, `estimate-retro-loads` +109.1); 7 readings `pending` → `passed` (`estimate-case-protocol-loaded`, `estimate-render-sync-reports`, `estimate-default-mode`, `estimate-hook-registry-rendered`, `estimate-permissions`, `estimate-render-harness-reproduces`, `estimate-claude-md-rendered`); `estimate-lint-catches` and `estimate-ledger-write-lifts` `pending` → `passed` by the session ledger after their new block |
| lessons | 2 (`lesson-transcript-omits-text-emitted-before-tool-calls`, `lesson-heredoc-trap-hit-twice-with-its-lesson-live`), both set `clustered` by synthesis | 0 others |
| insights | 0 | 2 by synthesis: `insight-ledger-hook-reads-only-the-final-text` (child added, severity 2 → 3), `insight-session-vault-knowledge-not-loaded` (child added, severity 2 → 3); both `open` |
| entities | 0 | 0 |

The checks the handoff asks for, after `generate`:

- `rule-ledger-tail` carries `kind: Leaf`, `estimates: [estimate-ledger-tail]`,
  `parent: rule-skill-hi`, `origin: raw/2026-09-13/ledger.md#case-101.2`, no `deferred_by`;
  its History ends `defer by decision-case-95 superseded`, `created over placeholder`,
  `estimate estimate-ledger-tail added`. `rule-skill-hi.children` gained it as the fourth.
- `estimate-generate-writes` holds the five blocks 101.1, 104.1, 104.2, 104.3, 105.3;
  `estimate-lint-catches` lost 100.3 and holds 103.5.
- `cleanup` wrote under `vault/archive/migration/2026-09-13/0652/decisions/`: 32 pages,
  not the 26 the handoff counted — the six defers and supersedes of this session (93–98)
  were archived by the same cascade.
- The render wrote `.claude/agents/librarian-guppi.md` (the archive step between brief
  and close, `vault/archive/` in the ban), `.claude/agents/ask-guppi.md` (105.1),
  `.claude/skills/hi/SKILL.md` (the `Tail:` line after `rule-github-issues`, the Frontier
  sentence of 101.4), `.claude/skills/retro/SKILL.md` (109.1), `CLAUDE.md` (the Migration
  paragraph names `raw/<date>/<hi HHMM>/ledger.md`, 109.2), and one file the handoff did
  not name: `.claude/skills/pre-task/SKILL.md` (the window sentence of 103.4).

## What the next session does first

1. `/hi` carries a `Tail:` line for the first time (`uv run guppi tail`): the readings at
   the next session start — `estimate-settings`, `estimate-hi-no-read-calls`,
   `estimate-hi-writes-frontier`, `estimate-pretask-reconciles` (live), `estimate-ask-finds`
   (dispatch `ask-guppi` with the archived slug `estimate-agents-at-import-not-expanded`),
   `estimate-retro-loads`.
2. The readings against this librarian run: `estimate-documentation-completes`,
   `estimate-close-commits`, `estimate-generate-writes`, `estimate-cleanup-moves`,
   `estimate-materialize-walks-dates`, `estimate-generate-walks-dates`,
   `estimate-materialize-assembles`, `estimate-ledger-tail` (live: `guppi tail` after this
   run's commit shows the readings written after it and nothing else).
3. The first `guppi archive` inside a librarian's run happens at the next session's close,
   moving `2026-09-13` (date level) and `2026-09-13/0652` if both are applied and covered.
4. Plan Mode over the deferred list below.

## Deferred

1. **A render inside `/hi`, after the pull** — Case 106, `rule-skill-hi`: what arrives
   from outside the session reaches its files in the same session. Related Insight
   `insight-workflow-contract-change-leaves-its-derived-text-stale`, severity 3.
   (postponed 2 times)
2. **Slice 3b: Work Mode** — Case 107, `rule-work-mode` and `rule-subagent-guppi`
   (placeholders, `draft`, the two lint orphans): the Spec as tasks with code, the ticked
   boxes, what a subagent may do, and the fork that comes back as a Case. Related Insight
   `insight-harness-agent-visibility`, severity 2. (postponed 7 times)
3. **The `## Insight` section of a clustered lesson** — Case 108, `rule-synthesis`: a
   synthesis entry carries the `## Insight` section of the lesson it clusters, or the
   lessons schema stops requiring it; 22 lessons carry the gap. No related Insight.
   (postponed 2 times)

Of the previous brief's six items, three left it by a ratified Case: 95 (Slice 3c,
`rule-ledger-tail`) by 100.1, 97 (an Insight whose children are archived) by 104.3, 94
(the archive in `ask-guppi`) by 105.1. The other three were postponed again: 98 by 106, 93
by 107, 96 by 108.

## Flags

- **Entries marked `incomplete` in this walk: 2**, both `incomplete: [category]` — the
  deletes outside the vault, `raw-notes` (100.6) and `old-archive` (102.1). `generate`
  applied each with the stdout line "outside the vault, nothing to archive". No entry of
  either yaml is `failed`; `unparsed` is empty in both.
- **One entry marked `near`, by this run's index check.** `rule-raw-archive` ("Keeps raw/
  to the sessions not yet turned into pages, by moving an applied session whole into the
  archive") near `rule-cleanup` ("Prevents an archived page from staying among the live
  ones, or the indexes from lagging behind the vault"): both move something into
  `vault/archive/` at the librarian's close; one moves the raw of a session, the other a
  page. Not merged. `rule-ledger-tail` was not marked: its index line was the placeholder
  of Case 95, filled by this create (101.1).
- **Synthesis: no Insight made, two extended.**
  `lesson-transcript-omits-text-emitted-before-tool-calls` joined
  `insight-ledger-hook-reads-only-the-final-text` (children now
  `lesson-ledger-hook-misses-a-reply-ending-in-a-tool-call`,
  `lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn` (archived),
  the new lesson; severity 3): the lesson answers the question the Insight's Proposal
  asks — the intermediate text is not in the transcript, so the writer sees the last text
  only. `lesson-heredoc-trap-hit-twice-with-its-lesson-live` joined
  `insight-session-vault-knowledge-not-loaded` (severity 3): the same trap as
  `lesson-vault-lesson-absent-at-the-moment-it-applies`, a third time, with its lesson
  live. Neither Insight was `actioned`; no status change.
- **`insight-ledger-hook-reads-only-the-final-text` keeps an archived child in
  `children`** — `lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn`,
  withdrawn by case 70, in `vault/archive/migration/2026-09-12/1156/lessons/`. The page
  says `severity: 3` with three children, one of them archived. The cascade of 104.3
  counts a child as live when its status is not `archived`, and reads statuses from
  `wiki/lessons/` only (`generate.py`, the cascade over insights): a child whose page is
  in the archive has no status there and is counted. Two children are live; the previous
  brief flagged the same count at 2 for the same reason.
- **`estimate-cleanup-moves` holds two wordings.** Its prose Criterion, from before case
  72, names `vault/archived/`; its `### case 102.2` block names `vault/archive/`. The
  handoff says the block is the criterion that holds now and nothing is to be repaired.
- **The render changed one file the handoff did not list**, `.claude/skills/pre-task/SKILL.md`,
  one sentence: the window is the session's ledger plus the date-level ledgers from the
  `hi` date on (103.4).
- **No Estimate is `failed`.** 17 are `pending`: `estimate-ask-finds`,
  `estimate-cleanup-moves`, `estimate-close-commits`, `estimate-documentation-completes`,
  `estimate-generate-walks-dates`, `estimate-generate-writes`,
  `estimate-handoff-dispatches`, `estimate-hi-no-read-calls`,
  `estimate-hi-writes-frontier`, `estimate-ledger-tail`, `estimate-materialize-assembles`,
  `estimate-materialize-walks-dates`, `estimate-plan-mode-verified`,
  `estimate-pretask-reconciles`, `estimate-retro-loads`, `estimate-settings`,
  `estimate-spec-capture-appends`. Six Rule pages went `built` → `draft` on their new
  block: `rule-ask`, `rule-cleanup`, `rule-materialize`, `rule-page-generation`,
  `rule-pretask`, `rule-skill-hi`.
- **22 `clustered` lessons have no `## Insight` section**, two of them from this run. 22 of
  the 109 `schema` findings; Case 108 is its defer.
- **Four `method` findings, unchanged from the previous run:** `estimate-default-mode`
  names no `tests/` file and does not say by hand; `estimate-settings`, a MOC's Estimate,
  names no `make <target>`; `estimate-documentation-completes` and
  `estimate-harness-pipeline` say "by hand" while another Estimate names a test file.
- **Stale defers:** `rule-work-mode` and `rule-subagent-guppi` have stood as placeholders
  since Case 29 (now 107), without `kind`, `estimates` or `tags`. They are the two lint
  orphans. `rule-ledger-tail` left this list: filled by 101.2.
- **No MOC candidate.** `entities-index.md` is empty; the vault holds no Entity page.
  Sixteen Rule pages are `draft`.
- **Two forms of ledger coexist on 2026-09-13**: `raw/2026-09-13/ledger.md` (49 lines,
  Cases 100–109 and the readings to 22:18) and `raw/2026-09-13/0652/ledger.md` (4 lines,
  from 22:36). Both units are applied to the last entry; the next `guppi archive` decides
  whether they move.
- **The handoff's instructions were all within the frame**; none was refused. The frame of
  this run has no archive step and `guppi archive` was not run, as the handoff says.
- **Lint.** `make lint` exits 1 at its third step. `guppi render --check` exits 0 and
  `guppi index --check` exits 0. `guppi lint`: 116 findings, exit 1 — 109 `schema` (33
  missing `## Context`, 31 `## Problem`, 22 `## Insight`, 11 `tags`, 6 `source`, 2 `kind`,
  2 `estimates`, 2 `## Estimates`), 4 `method`, 2 `orphan`, 1 `ref`
  (`rule-page-generation` names `decision-case-N` in its body, a literal). 133 before this
  run: the 32 archived decisions took 14 findings with them (`## Context`, `## Problem`),
  the fill of `rule-ledger-tail` took 5 (`kind`, `estimates`, `tags`, `## Estimates`,
  `orphan`), and the two new clustered lessons added 2 (`## Insight`).

## Readings at the close

- `make test` → 299 passed.
- `make lint` → exit 1 at `guppi lint`; `guppi render --check` → exit 0; `guppi index
  --check` → exit 0; `guppi lint` → 116 findings, exit 1.
- Live pages, 280: rules 39 (23 `built`, 16 `draft`), entities 0, estimates 41 (24
  `passed`, 17 `pending`, 0 `failed`), lessons 39 (17 `new`, 22 `clustered`), insights 9
  (all `open`), decisions 152 (all `current`).
- `vault/archive/migration/` holds 54 pages: 21 under `2026-09-11/estimates/`, 1 under
  `2026-09-12/1156/lessons/`, 32 under `2026-09-13/0652/decisions/`; and the raw of the
  four dates 09-09…09-12 under `<date>/raw/`. `cleanup` moved 32 in this run.
- `raw/2026-09-13/materialize.yaml`: 81 entries (79 from the ledger and the Spec, 2
  appended at synthesis), 32 decision groups, 0 unparsed lines, 2 `incomplete` marks, 1
  `near`. `raw/2026-09-13/0652/materialize.yaml`: 6 entries (4 from the ledger, 2 appended
  at synthesis), 0 unparsed lines.
