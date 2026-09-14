# Brief — 2026-09-14, after session O (the state after N verified, six Insights actioned, session marks by stamp, the agent probe, Cases 133–141)

Written by the librarian.

## Where things stand

What the handoff of session O records under "What actually got done":

- Ratified: 133, 134, 135, 136.1, 136.2, 136.3 (supersedes 111.6), 136.4, 137, 138, 139.1,
  139.2, 140, 141 (defer, supersedes 129). Deferred: 141 only.
- Code, commit `d750bdd` on `migration`: `guppi/gate.py` (136.1, `MARKS`, `mark()`),
  `guppi/pretask.py` (136.2, `window()` and the docstring), `guppi/ledger.py` (136.3,
  `unstamped_hi_moment` removed); tests `test_gate.py` (+5), `test_pretask.py` (three window
  tests rewritten, +2 net), `test_ledger.py` (the 111.6 pair flipped): 359 green (352
  before), `make style` clean.
- Readings, all in `raw/2026-09-14/1229/ledger.md`: passed — `estimate-event-log-records`
  (125 live at 12:31; 136.1 at 13:53), `estimate-claude-md-rendered` (122/123 live),
  `estimate-bash-guard` (127 live, the first refusal at 12:34; a second at 13:5x),
  `estimate-handoff-dispatches` (73.7, session N's `/handoff`), `estimate-brief-written`
  (124.1 against session N's brief), `estimate-pretask-hook-gates` (136.2),
  `estimate-ledger-write-lifts` (136.3), `estimate-render-harness-reproduces` (139.1 probe),
  `estimate-retro-loads` (126 live at 14:45). Failed: none.
- Lessons: three, all `knowledge` — `lesson-gate-plan-path-cut-by-the-event-log-detail-limit`,
  `lesson-agents-read-at-session-start-in-claude-code-2-1-228`,
  `lesson-retro-typed-by-the-person-bypasses-the-skill-tool-and-the-gate`.
- Frontier: 16 lines `[x]`, F1 `[-] defer case 141`; nothing open.
- Not done: the Rule-page `replace`s and the three skill renders (they came with this run);
  the live refusal of `guppi gate` (122) — not observed in session O, every block was final
  text; `probe-guppi.md` does not exist.

`uv run guppi materialize` walked three units: `raw/2026-09-14/0747/materialize.yaml` and
`raw/2026-09-14/1029/materialize.yaml` extended with 0 entries — the entries of 111.6 in
both marked `superseded_by: '136.3'`, the entries of 129 in `1029` marked `superseded_by:
'141'` — and `raw/2026-09-14/1229/materialize.yaml` written with 38 entries from the
session ledger (31 lines) and `1229/spec.md`: 20 `update` (7 rules, 4 estimates, 6
insights, 2 decisions, 1 `file`), 10 `estimate`, 3 `lesson`, 2 `defer`, 3
`remove_criterion`; 7 derived; 13 decision groups; 0 unparsed lines. The librarian
appended nothing at synthesis and merged nothing at the index check; two `near` marks
added (Flags).

`uv run guppi generate`: 0 pages for `0747` and `1029`, 65 for `1229`; exit 1, one line on
stderr (entry 112.6 of `0747`, below). The `file` entry of 133 (`insights-schema-yaml`) was
skipped as a Rule-class file applied by hand. Two `remove_criterion` entries of 141 printed
"case 129: no Estimate holds a block" (a defer, no block) and applied; the one of 136.3
removed the `### case 111.6` block from `estimate-ledger-write-lifts`. Every entry of `1229`
is `applied`. `uv run guppi cleanup` moved 22 pages, stderr empty. `uv run guppi render`
printed nothing; three governed files differ from HEAD, each by one line — the `Recorded:
!`uv run guppi event <mark> …`` line removed from `.claude/skills/pre-task/SKILL.md`,
`.claude/skills/retro/SKILL.md` and `.claude/skills/handoff/SKILL.md` (136.1). `CLAUDE.md`,
`.claude/settings.json` and the agents are unchanged. `guppi render --check` exit 0 after.

| category | created | updated |
|---|---|---|
| decisions | 13 (`decision-case-133`, `134`, `135`, `136.1`, `136.2`, `136.3`, `136.4`, `137`, `138`, `139.1`, `139.2`, `140`, `141`) | 2 by `replace` (`decision-case-130.1`, `130.2`: the literal `decision-case-N` in backticks, 140); 2 set `archived` by the supersedes cascade and moved by `cleanup` to `vault/archive/migration/2026-09-14/1229/decisions/`: `111.6` (by 136.3), `129` (by 141) |
| rules | 0 | 7 by decision (`rule-event-log` 136.1 and its `### case 136.1` block; `rule-pretask`, `rule-retro`, `rule-handoff` 136.1, the `Recorded:` line dropped; `rule-ledger-write` 136.3, the 111.6 sentence; `rule-pretask-hook` 136.2; `rule-render-harness` 139.1); 2 `deferred_by` `decision-case-129` → `decision-case-141` (`rule-work-mode`, `rule-subagent-guppi`); 3 by status cascade only, `draft` → `built` (`rule-brief` on `estimate-brief-written`, `rule-handoff` on `estimate-handoff-dispatches`, `rule-retro` on `estimate-retro-loads`) |
| estimates | 0 | 9 pages: 4 criterion blocks appended (`estimate-event-log-records` +136.1, `estimate-pretask-hook-gates` +136.2, `estimate-ledger-write-lifts` +136.3 and −111.6, `estimate-render-harness-reproduces` +139.1); 10 readings written, all `passed` (the nine pages above plus `estimate-claude-md-rendered`, `estimate-bash-guard`, `estimate-handoff-dispatches`, `estimate-brief-written`, `estimate-retro-loads`; `estimate-event-log-records` twice); `pending` → `passed`: `estimate-brief-written`, `estimate-handoff-dispatches`; `failed` → `passed`: `estimate-retro-loads` |
| lessons | 3 (the list above), all `new` | 20 set `archived` by the cascade of the six actioned Insights (104.2) and moved by `cleanup` to `vault/archive/migration/2026-09-14/1229/lessons/` |
| insights | 0 | 6 set `status: actioned` with `addressed_by` and a derived `## Addressed by` section: `insight-session-vault-knowledge-not-loaded` (134, 5 children), `insight-ledger-line-written-unchecked` (135, 4), `insight-ledger-hi-tied-to-its-session-by-position` (136.4, 3), `insight-ledger-hook-reads-only-the-final-text` (137, 3 live + 1 archived), `insight-workflow-contract-change-leaves-its-derived-text-stale` (138, 3), `insight-harness-agent-visibility` (139.2, 2); `severity` recomputed to 0 on all six |
| entities | 0 | 0 |

The checks the handoff asks for, after `generate`:

- Six Insight pages read `status: actioned`, `addressed_by: decision-case-<N>`, `## Addressed
  by` with the wikilink; the handoff says "seven Insight `update` entries", the yaml holds
  six (134, 135, 136.4, 137, 138, 139.2). Their 20 `clustered` children are `archived` and
  moved. `insights-index.md` lists all ten Insights; an index line carries the pattern only,
  no status, so "the six as `actioned`" is read on the pages, not the index.
- `estimate-ledger-write-lifts`: blocks `103.1`, `111.3`, `122`, `136.3`; no `111.6`.
  `decision-case-111.6` `superseded` → `archived` by the cascade, moved.
- `rule-pretask`, `rule-retro`, `rule-handoff`: History line "the Recorded line dropped;
  guppi gate writes the stamped <mark> mark (case 136.1)". `rule-pretask-hook`,
  `rule-ledger-write` (trailing space kept), `rule-render-harness`, `rule-event-log`,
  `decision-case-130.1`, `130.2`: every `replace` applied, none on stderr.
- `estimate-retro-loads` `passed` (line 30, block 126); `rule-retro` `built`.
  `estimate-render-harness-reproduces` `passed` (line 28, block 139.1).
- Entry 112.6 of `0747`: `failed` again, one stderr line, left as it is.
- `sprint.md` unchanged: the handoff gives no instruction on it.

## What the next session does first

1. The readings due: `estimate-brief-written` (124.1, against this brief: the `open`
   Insights stand in Deferred by severity, with a count); the live refusal of `guppi gate`
   (122, `rule-retro-commit`) when it first happens; `estimate-hook-registry-rendered` only
   if a render changes `.claude/settings.json` (this run's did not).
2. Plan Mode over the deferred list below: the four `open` Insights, each in its first Plan
   Mode as a Case (Deferred items 1–4), and Slice 3b (item 5).

## Deferred

1. **`insight-harness-yaml-entry-shape-assumed`**, severity 2, `open`, two children
   (`lesson-generate-replace-mapping-crashes`,
   `lesson-materialize-assumes-every-entry-has-a-line`). Pattern: a script of the pipeline
   assumes every entry of `materialize.yaml` carries the fields and the shapes it wrote
   itself; an entry written by another hand ends the whole run instead of failing alone.
   Proposal: state the shape of a yaml entry in one place and have every script read an
   entry through it; extend the rule of Case 47 — an entry fails alone — from `generate` to
   `materialize`. (stood in 1 brief, below the cap)
2. **`insight-librarian-frame-omits-required-reads`**, severity 2, `open`, two children
   (`lesson-librarian-reads-beyond-the-four-inputs`,
   `lesson-frame-read-clauses-omit-candidate-check-and-brief`). Pattern: the frame of the
   librarian names the reads it allows one by one, and the list is shorter than the
   judgments the librarian must make; the agent then breaks a clause or judges on an index
   line alone. Proposal: derive the read clauses from the judgments — one clause per
   judgment, naming the page and the field it may open; change every rule that names a
   read in one pass. (stood in 1 brief, below the cap)
3. **`insight-materialize-lift-loses-a-schema-field`**, severity 2, `open`, two children
   (`lesson-materialize-standalone-estimate-keeps-criterion-as-a-field`,
   `lesson-materialize-lesson-line-source-dropped`). Pattern: `materialize` lifts a ledger
   line or a `then` item into an entry and loses a field the page schema needs; the page is
   written without it and lint names the page, never the parser. Proposal: name in one
   table the fields each category needs and where each comes from, and have `materialize`
   lift by that table; a field the source lacks is `incomplete`, a field the table lacks is
   a parser fault. The three lessons of this run are its case again (Flags). (stood in 1
   brief, below the cap)
4. **`insight-tests-clock-not-pinned`**, severity 2, `open`, two children
   (`lesson-tests-cli-date-pinned`, `lesson-tests-generate-history-date-unpinned`). Pattern:
   a test pins the date on one side of the call and lets the code read the real clock on
   the other; it passes on the day it is written and fails later. Proposal: every entry
   point that reads the clock takes `now`, every test helper passes the pinned date; a run
   of the suite under a shifted date catches the rest of the class. (stood in 1 brief,
   below the cap)
5. **Slice 3b: Work Mode** — Case 141 (supersedes 129), `rule-work-mode` and
   `rule-subagent-guppi` (placeholders, `draft`, `deferred_by: decision-case-141`, the two
   lint orphans): the Spec as tasks with code, the ticked boxes, what a subagent may do,
   and the fork that comes back as a Case. Related Insight `insight-harness-agent-visibility`,
   now `actioned`, severity 0. (postponed 10 times)

Of the previous brief's seven items, six were Insights and left it by an `update` to
`actioned` (134, 135, 136.4, 137, 138, 139.2); item 6 (Slice 3b, 129) was retired by
141's `supersedes` and deferred again by 141, item 5 above. The four Insights of items
1–4 stood below the cap in the previous brief. Ties of severity and count are ordered by
slug. No `open` Insight is outside the list.

## Flags

- **Entry 112.6 of `raw/2026-09-14/0747/materialize.yaml` is `failed` a third time**:
  `generate: rule-page-generation: replace: 'History and log lines end with ·
  [[decision-case-N]] when a ' is absent or not unique`. It carries `superseded_by:
  '130.1'` since session N's run; `generate` retries it every run. The entry stays as it
  is; no repair, as the handoff also says.
- **3 entries marked `incomplete: [source]`**: the three `knowledge` lessons. Their ledger
  lines carry no `{source:…}` brace; the pages are written without `source` and lint names
  them (3 `schema` findings). The class of `insight-materialize-lift-loses-a-schema-field`
  (Deferred 3) when a brace is present; here the lines had none.
- **2 entries marked `near`**, no merge, no page opened for the index check:
  `lesson-agents-read-at-session-start-in-claude-code-2-1-228` near
  `lesson-agents-loaded-at-session-start` (the same claim — agents are read at session
  start — with the mechanism, the client version and the counter-example's explanation
  added; the old page is archived this run by 139.2's cascade);
  `lesson-retro-typed-by-the-person-bypasses-the-skill-tool-and-the-gate` near
  `lesson-pretask-line-unstamped-and-bound-by-position` (the fix that page names — a hook
  on the Skill call — is what a typed `/retro` escapes; a different cause; also archived this
  run by 136.4's cascade).
- **Synthesis: no lesson clustered, no Insight made or reopened.** The agents lesson names
  the mechanism `insight-harness-agent-visibility` (actioned by 139.2) called "not
  established"; it is the reading of 139.1 as knowledge, not a new occurrence of the
  pattern, so the Insight is not reopened. The gate lesson (the event log cut at
  `DETAIL_LIMIT` read by the gate as truth) shares no cause with a live lesson;
  `lesson-ledger-hook-hi-lost-at-midnight` was opened as the candidate (the hook reads one
  day's log): a different cause, and `clustered` under the actioned
  `insight-ledger-hi-tied-to-its-session-by-position`. The retro lesson's cause is
  `disable-model-invocation: true` on the retro skill; no live lesson or Insight has it.
- **The `retro` mark of the event log disappears after this render** (the third lesson): a
  typed `/retro` never calls the Skill tool, so `guppi gate` does not see it and no
  `-------- retro` line is written by the skill any more. No reader in code needs it today.
- **The `/retro` gate is not seen for a typed `/retro`**; the live refusal of `guppi gate`
  (122) is still unobserved: every block of sessions N and O was final text.
- **The handoff's count: "seven Insight `update` entries"; the yaml holds six** (134, 135,
  136.4, 137, 138, 139.2). 133 is the `file` entry.
- **The handoff says `insights-index.md` "shows the six as `actioned`"**; an index line
  carries no status (`guppi index`: slug and pattern, `deferred_by` only). The six read
  `actioned` on their pages.
- **Six new lint orphans**: the six actioned Insights; their children are archived, and no
  live page names them in its frontmatter. Their `decision-case-<N>` pages carry them as
  `update` targets, not in a frontmatter field.
- **1 `ref` finding on `decision-case-140`**: the page's own body quotes the literal
  `decision-case-N` that 140 put in backticks on `130.1` and `130.2`; the two findings of
  130.1 and 130.2 are gone.
- **All 42 Estimates read `passed`; none `pending`, none `failed`.** `rule-brief`,
  `rule-handoff` and `rule-retro` went `built` by the cascade; the draft Rules are the two
  placeholders only.
- **`lesson-agents-loaded-at-session-start` and `lesson-agents-visible-in-session` are
  archived** with the actioning of `insight-harness-agent-visibility`; the settled fact lives
  on `lesson-agents-read-at-session-start-in-claude-code-2-1-228` (`new`) and in block 139.1
  of `estimate-render-harness-reproduces`.
- **Stale defers:** `rule-work-mode` and `rule-subagent-guppi` have stood as placeholders
  since Case 29 (now 141), without `kind`, `estimates` or `tags`; 8 `schema` findings and 2
  orphans.
- **No MOC candidate.** `entities-index.md` is empty; the vault holds no Entity page.
- **The handoff's instructions were all within the frame**; none was refused.
- **Archive (run after the brief): nothing moved.** `uv run guppi archive` exit 0, stdout
  and stderr empty. `raw/2026-09-14/0747` and `1029` are kept by the date guard of
  `guppi/archive.py` (a unit dated today is skipped without a line), as in the previous
  run; every entry of both is `applied` or `superseded_by`. `raw/2026-09-14/1229` is the
  session of the run, never moved. The two units move at the first run on a later date.
- **Lint.** `make lint` exits 1 at its third step. `guppi render --check` exit 0, `guppi
  index --check` exit 0. `guppi lint`: 82 findings, exit 1 — 73 `schema` (31 missing `##
  Context`, 31 `## Problem`, on the decision pages of Cases 1–28; `kind`, `estimates`,
  `tags`, `## Estimates` on the two placeholders; `source` on the three lessons), 1 `ref`
  (`decision-case-140`), 8 `orphan` (the two placeholders, the six actioned Insights). 74
  before this run: +3 `schema` (`source`), −2 +1 `ref`, +6 `orphan`.

## Readings at the close

- `make test` → 359 passed.
- `make lint` → exit 1 at `guppi lint`; `guppi render --check` → exit 0; `guppi index
  --check` → exit 0; `guppi lint` → 82 findings, exit 1.
- Live pages, 313: rules 40 (38 `built`, 2 `draft`), entities 0, estimates 42 (all
  `passed`), lessons 29 (21 `new`, 8 `clustered`), insights 10 (6 `actioned`, 4 `open`),
  decisions 192 (all `current`).
- `vault/archive/migration/` holds 86 pages: 21 under `2026-09-11/estimates/`, 1 under
  `2026-09-12/1156/lessons/`, 32 under `2026-09-13/0652/decisions/`, 3 under
  `2026-09-14/0747/decisions/`, 7 under `2026-09-14/1029/decisions/`, 2 under
  `2026-09-14/1229/decisions/`, 20 under `2026-09-14/1229/lessons/`; and the raw of the
  dates 09-09…09-13 under `<date>/[HHMM/]raw/`. `cleanup` moved 22 in this run.
- `raw/2026-09-14/1229/materialize.yaml`: 38 entries, all `applied`, 13 decision groups, 0
  unparsed lines, 3 `incomplete`, 0 `failed`, 2 `near`, 2 `exists` (the defers of 141 on
  the live placeholders), 0 `librarian`. `0747`: 1 `failed` (112.6, `superseded_by`).
