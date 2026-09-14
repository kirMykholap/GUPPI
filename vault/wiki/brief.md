# Brief — 2026-09-14, after session N (the gate on an unwritten ledger line, the hi line in context, bashguard, an Insight as a Case, Cases 122–132)

Written by the librarian.

## Where things stand

What the handoff of session N records under "What actually got done":

- Ratified: 123, 122 (supersedes 117), 124.1 (supersedes 119), 124.2, 124.3, 125, 126
  (supersedes 118), 127 (supersedes 120), 128 (supersedes 121), 129 (defer, supersedes 116),
  130.1 (supersedes 112.6), 130.2, 131, 132. Deferred: 129 only.
- Code, commit `a5dc64e` on `migration`: `guppi/gate.py` (122), `guppi/event.py` (125),
  `guppi/bashguard.py` new + `guppi/cli.py` (127), `guppi/generate.py` (124.2),
  `guppi/materialize.py` (130.2); tests `test_gate.py` (14), `test_event.py` (+5),
  `test_bashguard.py` new (15), `test_generate.py` (+2), `test_materialize.py` (+2): 352
  green (318 before), `make style` clean, `guppi render --check` exit 0 before this run's
  render.
- By hand, same commit: `vault/wiki/case-schema.md` Language (123); `glossary.md` Insight
  and `deferred_by` rows, `index.md` §8, `insights/schema.md` three edits +
  `insights/schema.yaml` `deferred_by` (124.3; the yaml row unsigned, under Flags);
  `rules/rule-page-generation.md` History lines of 2026-09-11 and of case 114 (130.1, 131);
  `decisions/decision-case-112.1`–`112.6` the literal in backticks (130.1). `guppi lint`
  84 → 77 findings before this run.
- Readings, all in `raw/2026-09-14/1029/ledger.md`: passed — `estimate-git-context-current`
  (115), `estimate-documentation-completes` (100.2), `estimate-ledger-write-lifts` (111.3,
  111.6 at 10:57; 122 at 11:51), `estimate-event-log-records` (111.1 at 11:23; 125 test half
  at 11:51), `estimate-pretask-reconciles` (128), `estimate-generate-writes` (124.2),
  `estimate-bash-guard` (127, test), `estimate-materialize-assembles` (130.2),
  `estimate-spec-capture-appends` (73.2), `estimate-plan-mode-verified`; failed —
  `estimate-retro-loads` (109.1, second time).
- Lessons: `lesson-heredoc-trap-hit-a-fourth-time-in-the-session-that-ratified-its-hook`
  (error), `lesson-pretask-line-unstamped-and-bound-by-position` (knowledge).
- Not done: the five renders and the readings listed above (the renders came with this run;
  the readings are due at the next session); Slice 3b (129); the live refusal of `bashguard`
  (the hook is registered by this run's render); the yaml row of `insights/schema.yaml`
  unsigned.

`uv run guppi materialize` walked two units: `raw/2026-09-14/0747/materialize.yaml`
extended with 0 entries — the entry of 112.6 marked `superseded_by: '130.1'` and the defers
116, 117, 118, 119, 121 marked `superseded_by` (129, 122, 126, 124.1, 128) — and
`raw/2026-09-14/1029/materialize.yaml` written with 57 entries from the session ledger (41
lines) and `1029/spec.md`. The librarian appended 4 entries at synthesis: 60 entries now
(34 `update`, 2 `create`, 2 `defer`, 12 `estimate`, 2 `lesson`, 8 `remove_criterion`; 16
derived), 14 decision groups, 0 unparsed lines.

`uv run guppi generate`: 0 pages for `2026-09-14/0747`, 58 for `2026-09-14/1029`; exit 1,
one line on stderr (entry 112.6 of `0747`, below). Four `file` entries were skipped as
Rule-class files applied by hand (`case-schema` 123, `glossary`, `index`, `insights-schema`
124.3); eight `remove_criterion` entries printed "no Estimate holds a block" (117, 119, 118,
120, 116 twice, 121, 112.6 — defers and a failed update, none had a block) and applied.
Every entry of `1029` is `applied`. `uv run guppi cleanup` moved 7 pages, stderr empty.
`uv run guppi render` printed nothing; after it six governed files differ from HEAD:
`CLAUDE.md` (123 Language, 122 sentence), `.claude/settings.json` (127 `Bash` matcher;
parses as JSON), `.claude/skills/hi/SKILL.md` (125), `.claude/skills/retro/SKILL.md` (126,
`Ledger: !`uv run guppi tail``), `.claude/skills/pre-task/SKILL.md` (128), and
`.claude/agents/librarian-guppi.md` (124.1, the Deferred item of the brief frame — not in
the handoff's list of five).

| category | created | updated |
|---|---|---|
| decisions | 14 (`decision-case-122`, `123`, `124.1`, `124.2`, `124.3`, `125`, `126`, `127`, `128`, `129`, `130.1`, `130.2`, `131`, `132`) | 7 set `archived` by the supersedes cascade and moved by `cleanup` to `vault/archive/migration/2026-09-14/1029/decisions/`: `112.6` (by 130.1), `116` (by 129), `117` (by 122), `118` (by 126), `119` (by 124.1), `120` (by 127), `121` (by 128) |
| rules | 1, `rule-bash-guard` created over its placeholder (127; `Leaf`, `hook`, `built`, `deferred_by` 120 cleared) | 20: 17 by decision (`rule-claude-md` 123, `rule-ledger-write` 122 and `deferred_by` 117 cleared, `rule-case-protocol` 122, `rule-brief` 124.1 and 132 and 119 cleared, `rule-page-generation` 124.2, 130.1, 131, `rule-event-log` 125 and 132, `rule-skill-hi` 125, `rule-retro` 126 and 132 and 118 cleared, `rule-hook-registry` 127, `rule-pretask` 128 and 121 cleared, `rule-work-mode` and `rule-subagent-guppi` 116 cleared then deferred by 129, `rule-materialize` 130.2, `rule-retro-commit`, `rule-harness`, `rule-ledger-tail` 132); 4 by status cascade only (`rule-documentation`, `rule-git-context`, `rule-plan-mode`, `rule-spec-capture` `draft` → `built`). Also `draft` → `built`: `rule-event-log`, `rule-ledger-write`; `built` → `draft` on a `pending` block: `rule-brief` |
| estimates | 1, `estimate-bash-guard` (derived from 127, the `passed` reading of line 35 folded in) | 11: 7 criterion blocks (`estimate-ledger-write-lifts` +122, `estimate-brief-written` +124.1, `estimate-generate-writes` +124.2, `estimate-event-log-records` +125, `estimate-retro-loads` +126, `estimate-pretask-reconciles` +128, `estimate-materialize-assembles` +130.2); 10 readings `pending` → `passed` (`estimate-git-context-current`, `estimate-documentation-completes`, `estimate-ledger-write-lifts`, `estimate-event-log-records`, `estimate-pretask-reconciles`, `estimate-generate-writes`, `estimate-materialize-assembles`, `estimate-spec-capture-appends`, `estimate-plan-mode-verified`; `estimate-event-log-records` and `estimate-ledger-write-lifts` twice); 1 `pending` → `failed` (`estimate-retro-loads`) |
| lessons | 2 (the list above), both set `clustered` by synthesis | 0 beyond the two created |
| insights | 0 | 2 by synthesis: `insight-session-vault-knowledge-not-loaded` (fifth child added; severity 4 → 5), `insight-ledger-hi-tied-to-its-session-by-position` (third child added; severity 2 → 3); both `open`, no status change |
| entities | 0 | 0 |

The checks the handoff asks for, after `generate`:

- Entry 112.6 of `0747`: `generate` retried it once more and failed it again, one stderr
  line; the entry keeps `failed` and `superseded_by: '130.1'`; no repair.
- `rule-bash-guard`: frontmatter `kind: Leaf`, `enforcement: hook`, `implementation_ref`
  `guppi/bashguard.py`, `tests/test_bashguard.py`, `.claude/settings.json`, `estimates:
  [estimate-bash-guard]`, `status: built`, no `deferred_by`; History `created over
  placeholder`. `rules-index.md` shows its purpose without a `deferred_by`.
- `rule-page-generation`: the three updates applied in ledger order (124.2, 130.1, 131);
  `estimate-generate-writes` holds the `### case 124.2` block and reads `passed` (line 33).
- `rule-brief`, `rule-event-log`, `rule-retro`: each carries the `contract: changed` block
  and the `contract: same` edit of 132.
- `.claude/settings.json` parses as JSON; a `PreToolUse` entry with `"matcher": "Bash"` at
  line 29. `.claude/skills/retro/SKILL.md` line 12 reads `Ledger: !`uv run guppi tail``.
- `sprint.md` unchanged: the handoff gives no instruction on it.

## What the next session does first

1. **Slice 3b: Work Mode** — Case 129 (supersedes 116), `rule-work-mode` and
   `rule-subagent-guppi`; the owner set it apart as the next session's whole agenda
   (Deferred item 6 below).
2. The readings due: `estimate-claude-md-rendered` (the `CLAUDE.md` of this run: the
   Language section of 123 and the sentence of 122); `estimate-brief-written` (124.1,
   against this brief: the `open` Insights stand in Deferred by severity, with a count);
   `estimate-event-log-records`, the live half of 125 (at the next `/hi`: the `hi:` line in
   context and the folder named without a read call); `estimate-retro-loads` (126, at the
   next `/retro`: the skill loads, `Ledger:` carries the folder's lines);
   `estimate-handoff-dispatches` (pending since its creation; the `/handoff` of session N
   dispatched this run); `estimate-bash-guard` live (the first refusal of a heredoc — the
   hook is registered since this run's render).
3. The unsigned line of `vault/wiki/insights/schema.yaml` (`deferred_by` in `optional`,
   commit `a5dc64e`, no `then` block): ratify or revert.
4. Plan Mode over the deferred list below.

## Deferred

1. **`insight-session-vault-knowledge-not-loaded`**, severity 5, `open`, five children
   (`lesson-readings-after-librarian-invisible-to-next-hi`,
   `lesson-vault-lesson-absent-at-the-moment-it-applies`,
   `lesson-heredoc-trap-hit-twice-with-its-lesson-live`,
   `lesson-heredoc-trap-hit-a-third-time-in-work-mode`,
   `lesson-heredoc-trap-hit-a-fourth-time-in-the-session-that-ratified-its-hook`). Pattern: a
   fact the vault holds does not reach the session that needs it; only `brief.md`,
   `CLAUDE.md`, the skills and the agent frames are loaded, and everything else waits for a
   read the agent must first think to make. Proposal: a second channel beside the brief —
   the unmaterialized ledger tail at `/hi` (`rule-ledger-tail`, live) and a way for a Rule
   page to name the lessons that bear on it, so the pages loaded with a phase carry the
   traps of that phase; whether in the prompt or in a hook is a Case. `rule-bash-guard`
   (127) now stands as a hook against the heredoc trap, the fourth child's cause. (stood in
   1 brief)
2. **`insight-ledger-line-written-unchecked`**, severity 4, `open`, four children
   (`lesson-spec-then-items-unchecked-against-ledger-lines`,
   `lesson-ledger-decision-line-written-without-the-case-word`,
   `lesson-ledger-preview-in-ratification-taken-for-the-record`,
   `lesson-pretask-nested-estimate-exempt-from-the-line-check`). Pattern: a ledger line is
   written verbatim and nothing reads it back until `materialize`, so a line that does not
   parse or does not match the Spec costs a session. Proposal: `guppi pretask --check`
   already reads the day's ledger for the `then`-item comparison (59.1); the same pass can
   put every line through `materialize.parse_line` and report the ones that do not parse;
   the table of `case-schema.md` should show `decision[case N]`, not `decision[case_id]`
   (Case 67 defers that half). (stood in 1 brief)
3. **`insight-ledger-hi-tied-to-its-session-by-position`**, severity 3, `open`, three
   children (`lesson-ledger-hook-hi-lost-at-midnight`,
   `lesson-hi-taken-by-a-session-started-in-the-same-second`,
   `lesson-pretask-line-unstamped-and-bound-by-position`). Pattern: the event log ties a
   `hi` line to its session by the session-start lines around it, not by an id; any start
   missing from the window or added to it sends the `hi` to the wrong session and the ledger
   writer refuses. Proposal: Case 111 already writes a stamped `hi` from the
   `UserPromptSubmit` hook and reads the window by the stamp with the old rule as fallback;
   the readings of `estimate-event-log-records` and `estimate-ledger-write-lifts` (passed in
   session N, 111.1 at 11:23 and 111.3/111.6 at 10:57) decide whether the binding by
   position can be retired. The third child names the `pretask` line (and the handoff the
   `retro` line) as the same class: written through `!` substitutions with an empty
   `CLAUDE_SESSION_ID`, bound by position. (stood in 1 brief)
4. **`insight-ledger-hook-reads-only-the-final-text`**, severity 3, `open`, four children
   (`lesson-ledger-hook-misses-a-reply-ending-in-a-tool-call`,
   `lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn` archived,
   `lesson-transcript-omits-text-emitted-before-tool-calls`,
   `lesson-ledger-lines-lost-in-a-reply-ending-in-a-skill-call-with-the-insight-live`).
   Pattern: the ledger writer sees the last text of a turn, not the turn; a `LEDGER` block
   anywhere else in the turn is never written. Proposal: settle whether an intermediate
   assistant text is in the transcript at all; if present, collect every assistant text of
   the `hi` window, if absent the writer needs a second event beside `Stop`; either way count
   blocks seen against lines written, shown at `/hi`. Case 122 (`guppi gate`, applied this
   run) refuses a skill call while a `then` item has no ledger line. (stood in 1 brief)
5. **`insight-workflow-contract-change-leaves-its-derived-text-stale`**, severity 3,
   `open`, three children (`lesson-estimates-criterion-stale-after-contract-change`,
   `lesson-render-governed-file-updated-as-rule-class-file`,
   `lesson-estimates-live-clause-stale-at-first-render`). Pattern: a ratified change lands
   on one text and leaves the text derived from it behind, because no step of the pipeline
   names the dependents of a change. Proposal: resolve the dependents of a change in one
   pass at pre-task — for each changed slug the Estimates whose criterion quotes it, for
   each `file` path the Rule whose `governs` names it; a change without its pair is a
   finding. Cases 59.6 and 59.8 cover the path half; the Estimate-criterion half is done by
   grep in the acknowledging reply. (stood in 1 brief)
6. **Slice 3b: Work Mode** — Case 129 (supersedes 116), `rule-work-mode` and
   `rule-subagent-guppi` (placeholders, `draft`, the two lint orphans): the Spec as tasks
   with code, the ticked boxes, what a subagent may do, and the fork that comes back as a
   Case. Related Insight `insight-harness-agent-visibility`, severity 2. (postponed 9
   times)
7. **`insight-harness-agent-visibility`**, severity 2, `open`, two children
   (`lesson-agents-loaded-at-session-start`, `lesson-agents-visible-in-session`). Pattern:
   the moment Claude Code reads an agent definition is not established; two sessions
   rendered an agent and got opposite results, and no measurement separates them.
   Proposal: one reading that separates the two — render a throwaway agent mid-session,
   dispatch it at once, record the result and the session state; write it as an Estimate
   on the Rule that renders agents; until then plan as if a rendered agent were unusable in
   the session that creates it. (stood in 1 brief)

Of the previous brief's six items, all six left it by a ratified Case: 119 by 124.1, 120 by
127, 117 by 122, 116 by 129 (which defers the same two pages again, item 6 above), 118 by
126, 121 by 128. Four `open` Insights of severity 2 fall outside the cap of seven, each in
its first brief, ordered by slug behind item 7: `insight-harness-yaml-entry-shape-assumed`,
`insight-librarian-frame-omits-required-reads`, `insight-materialize-lift-loses-a-schema-field`,
`insight-tests-clock-not-pinned`. Ties of severity and count are ordered by slug.

## Flags

- **Entry 112.6 of `raw/2026-09-14/0747/materialize.yaml` is `failed` a second time**:
  `generate: rule-page-generation: replace: 'History and log lines end with ·
  [[decision-case-N]] when a ' is absent or not unique`. `materialize` marked it
  `superseded_by: '130.1'` (130.2); `generate` skips `applied` only and retried it; the
  `old` text is gone from the page since 130.1's hand edit. The entry stays as it is; no
  repair. The `superseded_by` mark is what lets `archive` move `0747` (below).
- **No entry is marked `incomplete`; `unparsed` is empty; no `near`.** 2 defers carry
  `exists: true` (129 on `rule-work-mode` and `rule-subagent-guppi`, live placeholders;
  `deferred_by` set to `decision-case-129`).
- **Index check: `rule-bash-guard` (127) was the one non-estimate create**; its index line
  was its own placeholder (`deferred_by: decision-case-120`, which 127 supersedes), and no
  other rules line names the same or a near thing; `generate` wrote it over the placeholder.
  No page opened for the index check.
- **Synthesis: two lessons clustered, no Insight made.**
  `lesson-heredoc-trap-hit-a-fourth-time-in-the-session-that-ratified-its-hook` joined
  `insight-session-vault-knowledge-not-loaded` (severity 4 → 5): its root cause names the
  Insight and repeats the cause of the third-time lesson, its child. The handoff also named
  it near `lesson-heredoc-trap-hit-a-third-time-in-work-mode`; a lesson is one occurrence
  and the shared cause is the Insight's, so no `near` mark and no merge.
  `lesson-pretask-line-unstamped-and-bound-by-position` (knowledge) joined
  `insight-ledger-hi-tied-to-its-session-by-position` (severity 2 → 3): the `pretask` line
  carries no session id and is bound by position among the log's lines, the Insight's
  pattern with another line in the `hi` line's place. The two Insight pages were opened for
  `children`, `status` and `severity`, which no input carries.
- **The Deferred list follows the rendered 124.1**, as the handoff instructs: every `open`
  Insight stands in it with its severity, pattern, Proposal and count. The frame this run
  was dispatched with still carries the Deferred item of before 124.1 (the render of
  `rule-brief` into `.claude/agents/librarian-guppi.md` came with this run); the reading of
  `estimate-brief-written` is against this brief. Ten Insight pages were opened for
  `status` and `severity`; the Proposal section of `insight-ledger-line-written-unchecked`,
  `insight-ledger-hook-reads-only-the-final-text`,
  `insight-workflow-contract-change-leaves-its-derived-text-stale` and
  `insight-harness-agent-visibility` was read for their lines above.
- **A hand edit nobody signed:** `vault/wiki/insights/schema.yaml` gained `deferred_by` in
  `optional` (with a two-line comment) in commit `a5dc64e`, outside every `then` block,
  because lint requires `schema.md` and `schema.yaml` to agree once 124.3 added the row to
  `schema.md`. The next Plan Mode ratifies or reverts it.
- **The `then` of 124.2 said a `create` or `delete` of an Insight "is a `generate` error,
  as today"; "as today" was false** — `generate` accepted them before session N. The error
  exists now (`LIBRARIAN_ONLY` in `generate.py`). The Estimate block quotes the sentence as
  ratified.
- **A known limit of the gate (122), not a Case yet:** `plan_path` reads the plan file's
  path from the event log's `tool Write:`/`tool Edit:` lines, which `event.py` cuts at 80
  characters (`DETAIL_LIMIT`); a longer plan path is not found and the gate passes silently.
  Session N's paths were 54 characters.
- **The `retro` line of the event log (11:55:48) is unstamped**, `--------` like the
  `pretask` line (11:26:29); the lesson names the `pretask` line, the handoff says the
  `retro` line is the same class. No lesson or defer names the `retro` line.
- **`estimate-retro-loads` is `failed`** (block 109.1, the second `failed` reading, 11:55:
  `/retro` failed to load on the old substitution). The `### case 126` block was appended
  after the reading; the page holds the reading of line 41. The retro skill is rendered
  with `guppi tail` since this run; the reading of 126 is at the next `/retro`. `rule-retro`
  stays `draft`.
- **2 Estimates are `pending`**: `estimate-brief-written` (124.1, `rule-brief` `built` →
  `draft`), `estimate-handoff-dispatches` (`rule-handoff` `draft`). Readings the handoff
  names as due at the next session on pages that read `passed` today, since the test half
  passed: `estimate-event-log-records` (the live half of 125), `estimate-bash-guard` (the
  live refusal), `estimate-claude-md-rendered` (`passed`, no block of 122 or 123).
- **The render wrote six files, the handoff named five**: `.claude/agents/librarian-guppi.md`
  changed with `rule-brief` (124.1). `guppi render --check` exit 0 after the render.
- **The handoff's count of the ledger differs from the file**: "90-odd lines" against 41
  lines read by `materialize` (12 readings, 2 lessons, 27 decision lines). `materialize`
  reported 57 entries; the yaml holds 60 after the 4 synthesis entries (the `passed` line
  35 of `estimate-bash-guard` was folded into its create).
- **Eight `remove_criterion` entries printed "no Estimate holds a block"** (117, 119, 118,
  120, 116 twice, 121, 112.6): the superseded Cases were defers or a failed update and had
  written no block; the entries applied.
- **Stale defers:** `rule-work-mode` and `rule-subagent-guppi` have stood as placeholders
  since Case 29 (now 129), without `kind`, `estimates` or `tags`; the two lint orphans and
  8 `schema` findings. `rule-bash-guard` left that list this run.
- **No MOC candidate.** `entities-index.md` is empty; the vault holds no Entity page. Five
  Rule pages are `draft`: `rule-brief`, `rule-handoff`, `rule-retro`, `rule-subagent-guppi`,
  `rule-work-mode`.
- **Archive.** See the line at the end of this section, written after the step ran.
- **The handoff's instructions were all within the frame**; none was refused. Its
  instruction not to read `raw/2026-09-14/0747/spec.md` or any decision page matches the
  frame.
- **Lint.** `make lint` exits 1 at its third step. `guppi render --check` exits 0 and
  `guppi index --check` exits 0. `guppi lint`: 74 findings, exit 1 — 70 `schema` (31
  missing `## Context`, 31 `## Problem`, on the decision pages of Cases 1–28; `kind`,
  `estimates`, `tags`, `## Estimates` on the two placeholders), 2 `ref` (the literal
  `decision-case-N` in the body of `decision-case-130.1` and `decision-case-130.2`, the
  shared text of Case 130 — the same literal 130.1 put in backticks on the pages of 112),
  2 `orphan`. 77 before this run: −4 `schema` and −1 `orphan` (`rule-bash-guard` filled),
  −2 `ref` (the pages of 112 by hand; `decision-case-112.6` archived), +2 `ref` (130.1,
  130.2).
- **Archive (run after the brief): nothing moved.** `uv run guppi archive` exit 0, stdout
  and stderr empty. `raw/2026-09-14/0747` was kept — not by its marks (every entry is
  `applied` or `superseded_by`, so `kept_reason` is None) but by the date guard of
  `guppi/archive.py` (`run`, `if unit.split("/")[0] >= today or unit == running:
  continue`): a unit dated today is skipped without a line. The handoff expected `0747` to
  move on the `superseded_by` mark, and the live half of the `### case 130.2` block of
  `estimate-materialize-assembles` says "112.6 marked, `0747` moved": the mark is there,
  the move is not; the page reads `passed` from the reading of line 36. `raw/2026-09-14/1029`
  is the session of the run, never moved. `0747` moves at the first run on a later date.

## Readings at the close

- `make test` → 352 passed.
- `make lint` → exit 1 at `guppi lint`; `guppi render --check` → exit 0; `guppi index
  --check` → exit 0; `guppi lint` → 74 findings, exit 1.
- Live pages, 319: rules 40 (35 `built`, 5 `draft`), entities 0, estimates 42 (39
  `passed`, 2 `pending`, 1 `failed`), lessons 46 (18 `new`, 28 `clustered`), insights 10
  (all `open`), decisions 181 (all `current`).
- `vault/archive/migration/` holds 64 pages: 21 under `2026-09-11/estimates/`, 1 under
  `2026-09-12/1156/lessons/`, 32 under `2026-09-13/0652/decisions/`, 3 under
  `2026-09-14/0747/decisions/`, 7 under `2026-09-14/1029/decisions/`; and the raw of the
  dates 09-09…09-13 under `<date>/[HHMM/]raw/`. `cleanup` moved 7 in this run; `archive`
  moved nothing (`raw/2026-09-14/0747` and `1029` both stay, above).
- `raw/2026-09-14/1029/materialize.yaml`: 60 entries (56 from the ledger and the Spec, 4
  appended at synthesis), 14 decision groups, 0 unparsed lines, 0 `incomplete`, 0 `failed`,
  0 `near`, 2 `exists`, 4 `librarian: synthesis`. `raw/2026-09-14/0747/materialize.yaml`:
  1 `failed` (112.6, `superseded_by`).
