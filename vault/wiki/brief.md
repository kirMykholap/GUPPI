# Brief — 2026-09-14, after session M (the cascade over the archive, the stamped hi, lint's text debt, Cases 110–121)

Written by the librarian.

## Where things stand

What the handoff of session M records under "What actually got done":

- Ratified: 110, 110.1, 111.1–111.6, 112.1–112.6, 113, 114 (supersedes 108), 115
  (supersedes 106), 115.1, 115.2. Deferred: 116 (supersedes 107), 117, 118, 119, 120, 121.
- Code, committed as `6d199d4` and `f5becdc`: `guppi/generate.py` (110: a child's status
  read in the archive; 114: `derive_insight` on every write of a lesson and in the cascade),
  `guppi/event.py` (111.1: `guppi event prompt`), `guppi/ledger.py` (111.3 and 111.6:
  `hi_moment` by stamp with the old rule as fallback), `guppi/lint.py` (112.1: the make
  target before "by hand"); tests in `test_generate.py`, `test_event.py`, `test_ledger.py`,
  `test_lint.py`, the stamped `hi` lines in `test_pretask.py` and `test_spec.py`: 318 green
  (299 before), `make style` clean. `vault/wiki/insights/schema.md` `severity` row by hand
  (110.1).
- Readings: `estimate-settings`, `estimate-hi-no-read-calls`, `estimate-hi-writes-frontier`,
  `estimate-pretask-reconciles`, `estimate-ask-finds`, `estimate-close-commits`,
  `estimate-cleanup-moves`, `estimate-materialize-walks-dates`,
  `estimate-generate-walks-dates`, `estimate-materialize-assembles`, `estimate-ledger-tail`,
  `estimate-generate-writes` (failed at 07:48, passed at 09:20), `estimate-lint-catches`
  passed; `estimate-retro-loads` failed. Not taken: `estimate-documentation-completes`,
  `estimate-event-log-records` (111.1), `estimate-git-context-current` (115), the live half
  of `estimate-ledger-write-lifts`.
- Lessons: `lesson-hi-taken-by-a-session-started-in-the-same-second`,
  `lesson-ledger-lines-lost-in-a-reply-ending-in-a-skill-call-with-the-insight-live`,
  `lesson-reader-changed-before-its-writer-closed-the-live-session`,
  `lesson-heredoc-trap-hit-a-third-time-in-work-mode`,
  `lesson-pretask-dispatch-summarized-the-plan-and-ask-guppi-judged-the-summary`.
- Not done: everything this run applies (111.2, 111.4, 111.5, 112.2–112.6, 113, 115, 115.1,
  115.2 are page edits by `generate`); the readings above; the fix of `/retro` (118); Slice
  3b (116); `guppi lint` 114 findings before this run.

`uv run guppi materialize` walked three units: `raw/2026-09-13/materialize.yaml` and
`raw/2026-09-13/0652/materialize.yaml` extended with 0 entries each, and
`raw/2026-09-14/0747/materialize.yaml` written with 66 entries from the session ledger (56
lines) and `0747/spec.md`; no date-level ledger exists on 2026-09-14. The librarian appended
7 entries at synthesis: 73 entries now, 25 decision groups, 0 unparsed lines.

`uv run guppi generate`: 22 pages for `2026-09-13` (the cascade of 114 over the clustered
lessons, attributed to the first unit walked), 0 for `2026-09-13/0652`, 86 for
`2026-09-14/0747`; exit 1, one line on stderr (entry 112.6, below). One `file` entry was
skipped as a Rule-class file applied by hand (`insights-schema`, 110.1); four
`remove_criterion` entries printed "no Estimate holds a block" (cases 108, 106, 107 twice)
and applied. `uv run guppi cleanup` moved 3 pages, stderr empty. `uv run guppi render`
printed nothing; after it `.claude/settings.json` (a `UserPromptSubmit` entry, 111.2) and
`.claude/skills/hi/SKILL.md` (no `Recorded:` line, a `Render:` line after `Pull:`, the
Frontier sentence of 115.2) differ from HEAD, `CLAUDE.md` does not. 72 entries of the yaml
are `applied`, 1 is `failed`.

| category | created | updated |
|---|---|---|
| decisions | 25 (`decision-case-110`, `110.1`, `111.1`–`111.6`, `112.1`–`112.6`, `113`, `114`, `115`, `115.1`, `115.2`, `116`–`121`) | 3 set `archived` by the supersedes cascade and moved by `cleanup` to `vault/archive/migration/2026-09-14/0747/decisions/`: `106` (by 115), `107` (by 116), `108` (by 114) |
| rules | 1 placeholder, `rule-bash-guard` (`draft`, defer 120 without a `ref`) | 20: 14 by decision (`rule-page-generation` 110 and 114, `rule-event-log` 111.1, `rule-hook-registry` 111.2, `rule-ledger-write` 111.3, 111.6 and deferred by 117, `rule-skill-hi` 111.4, 115.2 and `deferred_by` 106 cleared, `rule-lint` 112.1, `rule-render-harness` 115.1, `rule-git-context` 115, `rule-synthesis` `deferred_by` 108 cleared, `rule-work-mode` and `rule-subagent-guppi` 107 cleared then deferred by 116, `rule-retro` 118, `rule-brief` 119, `rule-pretask` 121); 6 by status cascade only (`rule-ask`, `rule-cleanup`, `rule-close`, `rule-ledger-tail`, `rule-materialize`, `rule-settings` `draft` → `built`). Also `draft` → `built`: `rule-page-generation`, `rule-pretask`, `rule-skill-hi`; `built` → `draft` on a `pending` block: `rule-event-log`, `rule-git-context`, `rule-ledger-write` |
| estimates | 0 | 18: 5 criterion blocks (`estimate-event-log-records` +111.1, `estimate-ledger-write-lifts` +111.3 +111.6, `estimate-lint-catches` +112.1, `estimate-generate-writes` +114, `estimate-git-context-current` +115); 5 Method or Context edits (`estimate-default-mode` 112.2, `estimate-settings` 112.3, `estimate-generate-walks-dates` and `estimate-materialize-walks-dates` 112.4, `estimate-cleanup-moves` 112.5); 13 readings `pending` → `passed` (`estimate-settings`, `estimate-hi-no-read-calls`, `estimate-hi-writes-frontier`, `estimate-pretask-reconciles`, `estimate-ask-finds`, `estimate-close-commits`, `estimate-cleanup-moves`, `estimate-materialize-walks-dates`, `estimate-generate-walks-dates`, `estimate-materialize-assembles`, `estimate-ledger-tail`, `estimate-generate-writes` after its `failed` of line 1, `estimate-lint-catches`); 1 `pending` → `failed` (`estimate-retro-loads`) |
| lessons | 5 (the list above); `lesson-hi-taken-…` then `root_cause` corrected by 111.5, four of the five set `clustered` by synthesis, `lesson-pretask-dispatch-…` stays `new` | 29: 22 by the cascade of 114 (`## Insight` derived, History `insight section derived`); 10 by 113 (`tags` on `lesson-agents-loaded-at-session-start`, `lesson-estimates-criterion-stale-after-contract-change`, `lesson-hooks-windows-stdin-encoding`, `lesson-tests-cli-date-pinned`; `source` on `lesson-agents-visible-in-session`; both on `lesson-agents-at-import-not-expanded`, `lesson-hooks-exitplanmode-payload`, `lesson-hooks-messagedisplay-cannot-block`, `lesson-hooks-sessionstart-cannot-block`, `lesson-hooks-stop-payload`; 4 of them also in the 22); 1 by synthesis (`lesson-ledger-hook-hi-lost-at-midnight` `new` → `clustered`) |
| insights | 1 by synthesis, `insight-ledger-hi-tied-to-its-session-by-position` (children `lesson-ledger-hook-hi-lost-at-midnight`, `lesson-hi-taken-by-a-session-started-in-the-same-second`; severity 2; `open`) | 2 by synthesis: `insight-ledger-hook-reads-only-the-final-text` (fourth child added; severity 3, one child archived), `insight-session-vault-knowledge-not-loaded` (fourth child added; severity 3 → 4); both `open`, no status change |
| entities | 0 | 0 |

The checks the handoff asks for, after `generate`:

- `insight-ledger-hook-reads-only-the-final-text` reads `severity: 3` with four children,
  `lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn` archived among
  them: the count of 110 (2 live before synthesis, 3 after) holds.
- Case 114: 22 lessons rewritten with `## Insight`, History `insight section derived`; the
  22 `## Insight` lint findings are gone. Every `clustered` lesson (26) carries the section.
- Case 113: the 9 `tags` and 6 `source` findings on lessons are gone. Case 112: the four
  `method` and two `## Context` findings are gone; the `ref` finding on
  `rule-page-generation` stays (112.6 failed, below).
- Case 111.5 applied after the create of line 2: the page's `root_cause` ends "a resume of
  this session at 07:46:53 reopened the window, and the hi of 07:47 named the folder";
  History `root_cause corrected (case 111.5)`.
- `.claude/settings.json` parses as JSON. `.claude/skills/hi/SKILL.md` has no `Recorded:`
  line, carries `Render: !`uv run guppi render --sync`` at line 13 and "at session start
  or on the `Render:` line above" at line 29.
- `sprint.md`, Slice 5: the two items of the handoff added (the `event_log.md`-only date
  folders of `raw/`; the 31 decision pages of Cases 1–28 without `## Context` and
  `## Problem`).

## What the next session does first

1. **Case 117** (`rule-ledger-write`, Deferred item 3 below): the ledger lines of a reply
   that ends in a tool call — the fourth recurrence of
   `insight-ledger-hook-reads-only-the-final-text`. The owner asked for it to be discussed
   first.
2. **Case 119** (`rule-brief`, Deferred item 1 below): an open Insight surfaces in the
   brief as a Case of the next Plan Mode. The glossary and `insights/schema.md` say "never
   a Decision target" as they stand; the Case changes them. The owner asked for it to be
   discussed first.
3. The readings due at the next `/hi`: `estimate-event-log-records` (111.1: a `<stamp> hi`
   line in `event_log.md`, a repeated `/hi` adds none), `estimate-ledger-write-lifts`
   (111.3, 111.6: the window by the stamped `hi`, the old rule as fallback while no stamped
   `hi` exists), `estimate-git-context-current` (115: the `Render:` line present in `/hi`,
   empty on a clean tree), `estimate-documentation-completes` (block 100.2, the Archive
   step, against this run: what moved and what was kept is under Flags).
4. If the `UserPromptSubmit` hook of 111.1 does not fire on a slash command, no `hi` line is
   written by anyone: 111.4 removed the `Recorded:` line from the skill, so nothing writes
   `--------` and the fallback of 111.6 has nothing to read. The way out the handoff names:
   `uv run guppi event hi --session <session id>` by hand in a terminal, then a Case on
   111.4.
5. `estimate-retro-loads` is `failed` (block 109.1): the `/retro` substitution
   `cat vault/raw/$(date +%F)/ledger.md …` exits 1 on a day with session ledgers only; the
   fix is Case 118 (Deferred item 5).
6. Plan Mode over the deferred list below.

## Deferred

1. **An open Insight as a Case of the next Plan Mode** — Case 119, `rule-brief`: the brief
   lists an open Insight beside the Deferred items, ranked by severity, its Proposal as the
   recommend; the glossary and `insights/schema.md` stop saying "never a Decision target",
   and a Decision may set `addressed_by` and `actioned`. Related Insight
   `insight-session-vault-knowledge-not-loaded`, severity 4 (and
   `insight-ledger-hook-reads-only-the-final-text`, severity 3). (postponed 1 time)
2. **A `PreToolUse Bash` hook against the heredoc trap** — Case 120, `rule-bash-guard`
   (placeholder, `draft`, no `ref`): refuses a heredoc whose body carries a backslash
   escape, or any heredoc that writes a file, and names Write and Edit instead; the third
   recurrence of the trap. Related Insight `insight-session-vault-knowledge-not-loaded`,
   severity 4. (postponed 1 time)
3. **The ledger lines of a reply that ends in a tool call** — Case 117,
   `rule-ledger-write`: reach the ledger by a hook that sees them before the call, or by a
   gate that refuses the call while they are unwritten. Related Insight
   `insight-ledger-hook-reads-only-the-final-text`, severity 3. (postponed 1 time)
4. **Slice 3b: Work Mode** — Case 116 (supersedes 107), `rule-work-mode` and
   `rule-subagent-guppi` (placeholders, `draft`, two of the three lint orphans): the Spec
   as tasks with code, the ticked boxes, what a subagent may do, and the fork that comes
   back as a Case. Related Insight `insight-harness-agent-visibility`, severity 2.
   (postponed 8 times)
5. **The `/retro` ledger substitution on a day without a date-level ledger** — Case 118,
   `rule-retro`: exits 0 — `|| true`, or `cat` over the files a glob finds — so the skill
   loads on a day with session ledgers only. No related Insight. (postponed 1 time)
6. **The pre-task dispatch carries the `then` blocks** — Case 121, `rule-pretask`: the
   dispatch to `ask-guppi` carries the `then` blocks of every ratified Case (`replace`
   old/new, `set`, `sections`) or the plan file's path, not a summary. No related Insight;
   `lesson-pretask-dispatch-summarized-the-plan-and-ask-guppi-judged-the-summary` is `new`.
   (postponed 1 time)

Of the previous brief's three items, all three left it by a ratified Case: 106 (a render
inside `/hi`) by 115, 108 (the `## Insight` section) by 114, 107 (Slice 3b) by 116 — which
defers the same two pages again, item 4 above.

## Flags

- **Entry 112.6 is `failed`**: `generate: rule-page-generation: replace: 'History and log
  lines end with · [[decision-case-N]] when a ' is absent or not unique`. The `old` text
  occurs in the page only inside the History line of case 52.4 (line 95); the body sentence
  of line 44 already reads `· [[decision-case-N]]` in backticks. The entry stays as it is;
  no repair. The `ref` lint finding on `rule-page-generation` (the literal
  `decision-case-N`) stays with it, and the decision pages `decision-case-112.1`–`112.6`
  carry the same literal in their shared text: 7 `ref` findings, 1 before this run.
- **No entry is marked `incomplete`; `unparsed` is empty.** 6 defers carry `exists: true`
  (116 twice, 117, 118, 119, 121: the targets were live pages, `deferred_by` set), 120
  `exists: false` (the placeholder `rule-bash-guard` written).
- **Three entries marked `near`, by this run's index check, none merged.**
  `lesson-hi-taken-by-a-session-started-in-the-same-second` near
  `lesson-ledger-hook-hi-lost-at-midnight` (the same binding of the `hi` to its session by
  the session-start lines around it; a different failure of it — clustered, below).
  `lesson-ledger-lines-lost-in-a-reply-ending-in-a-skill-call-with-the-insight-live` near
  `lesson-ledger-hook-misses-a-reply-ending-in-a-tool-call` (the same loss; the new lesson
  records the recurrence with the lesson and the Insight live).
  `lesson-heredoc-trap-hit-a-third-time-in-work-mode` near
  `lesson-heredoc-trap-hit-twice-with-its-lesson-live` (the same trap; the new lesson
  records the third occurrence with the Insight live). A lesson is one occurrence; the
  shared cause is the Insight's, so none was turned into an update.
- **Synthesis: one Insight made, two extended.**
  `insight-ledger-hi-tied-to-its-session-by-position` over
  `lesson-ledger-hook-hi-lost-at-midnight` (session H, midnight put the session-start in
  another day's file) and `lesson-hi-taken-by-a-session-started-in-the-same-second`
  (session M, a stranger's start inside the window): the `hi` line carries no session id
  and `hi_recorded` binds it by position; its Proposal points at Case 111, already coded,
  and the two readings at the next `/hi`.
  `lesson-ledger-lines-lost-in-a-reply-ending-in-a-skill-call-with-the-insight-live` joined
  `insight-ledger-hook-reads-only-the-final-text` (severity 3): its root cause names the
  Insight. The handoff also named it a candidate for
  `insight-session-vault-knowledge-not-loaded` (the lesson was live and did not reach the
  agent); a lesson carries one `insight` field, so it went to the Insight its cause names,
  and the second reading is recorded here.
  `lesson-heredoc-trap-hit-a-third-time-in-work-mode` joined
  `insight-session-vault-knowledge-not-loaded` (severity 3 → 4).
  `lesson-reader-changed-before-its-writer-closed-the-live-session` stays `new`: compared
  with `lesson-pretask-runs-before-the-check-it-adds` (a check not re-run after the code
  that changes it) — a different cause (a reader live in the working tree before its
  writer). `lesson-pretask-dispatch-summarized-…` stays `new`, no candidate.
- **The History line of `rule-page-generation` for case 114 reads `updated: the`**: the
  `change` of the 114 update entry is the single word `the` as materialized from the Spec.
  The `replace` of 114 applied; only the History line and `log.md` carry the fragment.
- **`estimate-retro-loads` is `failed`** (block 109.1, the substitution exits 1 without a
  date-level ledger; Case 118). `estimate-generate-writes` was `failed` at line 1 (block
  104.3, the archived child counted live) and `passed` at line 46 (blocks 101.1, 104.1,
  104.2, 104.3 against the test of case 110, 105.3, 114 against the test of case 114); the
  page holds the later reading.
- **7 Estimates are `pending`**: `estimate-documentation-completes`,
  `estimate-event-log-records`, `estimate-git-context-current`,
  `estimate-handoff-dispatches`, `estimate-ledger-write-lifts`,
  `estimate-plan-mode-verified`, `estimate-spec-capture-appends`. Three Rule pages went
  `built` → `draft` on their new block: `rule-event-log`, `rule-git-context`,
  `rule-ledger-write`.
- **The handoff's counts differ from the yaml.** The handoff says the ledger holds 40
  lines, 1 `failed` and 12 `passed` readings, 4 lessons; `materialize` read 56 lines: 2
  `failed` (lines 1 and 50) and 13 `passed` readings, 5 lessons, and its "What actually got
  done" lists the five lessons and both `failed` readings.
- **Stale defers:** `rule-work-mode` and `rule-subagent-guppi` have stood as placeholders
  since Case 29 (now 116), without `kind`, `estimates` or `tags`; `rule-bash-guard` joins
  them as a placeholder of 120. They are the three lint orphans and 12 `schema` findings.
- **No MOC candidate.** `entities-index.md` is empty; the vault holds no Entity page.
  Eleven Rule pages are `draft`.
- **Two forms of ledger coexist on 2026-09-13** (`raw/2026-09-13/ledger.md`, 49 lines, and
  `raw/2026-09-13/0652/ledger.md`, 4 lines); 2026-09-14 has the session form only. Both
  units of 2026-09-13 are applied to the last entry; the Archive step of this run is below.
- **Archive (the first inside a librarian's run).** `uv run guppi archive` moved
  `raw/2026-09-13` → `archive/migration/2026-09-13/raw` and `raw/2026-09-13/0652` →
  `archive/migration/2026-09-13/0652/raw`, beside the `decisions/` folder already under
  `2026-09-13/0652/`; kept `raw/2026-09-14/0747`, the session of the run, which is never
  moved. Exit 0, stderr empty. `raw/` now holds the session folder `2026-09-14/0747/` and
  the `event_log.md` of six dates (09-09…09-14), which the archive never moves.
- **Contradiction the handoff names:** Case 119's purpose (an Insight as a Decision target)
  contradicts the glossary row `Insight` ("never a Decision target") and
  `insights/schema.md` as they stand; the next Plan Mode changes them.
- **The handoff's instructions were all within the frame**; none was refused.
- **Lint.** `make lint` exits 1 at its third step. `guppi render --check` exits 0 and
  `guppi index --check` exits 0. `guppi lint`: 84 findings, exit 1 — 74 `schema` (31
  missing `## Context`, 31 `## Problem`, on the decision pages of Cases 1–28; 3 `kind`, 3
  `estimates`, 3 `tags`, 3 `## Estimates` on the three placeholders), 7 `ref` (the literal
  `decision-case-N` in `rule-page-generation` and `decision-case-112.1`–`112.6`), 3
  `orphan`. 116 before this run: −22 `## Insight` (114), −9 `tags` and −6 `source` (113),
  −4 `method` and −2 `## Context` (112), +4 `schema` and +1 `orphan` (`rule-bash-guard`),
  +6 `ref` (the decision pages of 112). The handoff expected near 70; the placeholder of
  120 and the six decision pages of 112 make the difference.

## Readings at the close

- `make test` → 318 passed.
- `make lint` → exit 1 at `guppi lint`; `guppi render --check` → exit 0; `guppi index
  --check` → exit 0; `guppi lint` → 84 findings, exit 1.
- Live pages, 309: rules 40 (29 `built`, 11 `draft`), entities 0, estimates 41 (33
  `passed`, 7 `pending`, 1 `failed`), lessons 44 (18 `new`, 26 `clustered`), insights 10
  (all `open`), decisions 174 (all `current`).
- `vault/archive/migration/` holds 57 pages: 21 under `2026-09-11/estimates/`, 1 under
  `2026-09-12/1156/lessons/`, 32 under `2026-09-13/0652/decisions/`, 3 under
  `2026-09-14/0747/decisions/`; and the raw of the dates 09-09…09-13 under `<date>/raw/`
  after the Archive step of this run. `cleanup` moved 3 in this run.
- `raw/2026-09-14/0747/materialize.yaml`: 73 entries (66 from the ledger and the Spec, 7
  appended at synthesis), 25 decision groups, 0 unparsed lines, 0 `incomplete` marks, 1
  `failed`, 3 `near`, 7 `librarian: synthesis`.
