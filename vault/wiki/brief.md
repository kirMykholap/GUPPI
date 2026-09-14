# Brief — 2026-09-14, after session P (the four open Insights actioned, the index files retired, the vault's refs as wikilinks, Cases 142–154)

Written by the librarian.

## Where things stand

What the handoff of session P records under "What actually got done":

- Ratified: 142.1–142.5, 143, 144.1–144.3, 145.1–145.3, 147.1–147.9, 148.1–148.3,
  149.1–149.4, 150, 150.1, 151, 153. Deferred: 146 (`rule-lint`), 152 (`rule-work-mode`,
  `rule-subagent-guppi`, supersedes 141), 154 (`rule-ask`).
- Code, commit `4586061` on `migration`: `guppi/materialize.py` (`lift_line`, the per-line
  guard, the retry, the unreadable-entry skip, `page_estimates` through `slug_of`, `run`
  keeps walking), `guppi/generate.py` (skip `failed`-without-`kind`, skip `superseded_by`
  after its Decision page, `wikilink()` in `frontmatter`), `guppi/pages.py` (`REF_FIELDS`,
  `slug_of`, `strip_refs` in `read_page`), `guppi/lint.py` (`hub_files`, `check_refs` with
  hubs), `guppi/cleanup.py` and `guppi/cli.py` without the index, `guppi/index.py` deleted,
  Makefile (`lint` two steps, `test-harness` two files); tests: `tests/conftest.py` (the
  pinned clock), `tests/test_conftest.py`, `tests/test_pages.py`, additions in
  `test_materialize.py` (+5), `test_generate.py` (+2), `test_lint.py` (+1),
  `tests/test_index.py` deleted, three CLI tests moved to the fixture: 368 green (359
  before), `make style` clean.
- The migration of 148.1: 357 of 399 pages under `wiki/` and `archive/` rewritten,
  frontmatter only; lint identical before and after; the owner saw 2 backlinks on
  `insight-tests-clock-not-pinned` and 15 on `rule-harness`.
- By hand: `index.md` (§11 rewritten, §1 index lines and the table row removed, the
  hub-links paragraph, the example page), `glossary.md`, `case-schema.md`, the six
  `schema.md`, `insights/schema.md` line 31, `log.md`; the four `wiki/*-index.md` deleted.
- Readings: `estimate-brief-written` (124.1), `estimate-materialize-assembles` (142.1),
  `estimate-materialize-walks-dates` (142.4), `estimate-tests-clock-pinned` (145.1),
  `estimate-generate-writes` (142.2, 148.1, 151) — all `passed`. Lessons: two `knowledge`
  with `source`.
- Not done: the librarian's 29 tasks (this run); the nine readings listed under "What the
  next session does first"; the Obsidian graph still shows orphans (owner) — next session,
  with 146.

`uv run guppi materialize` walked four units, exit 0: `raw/2026-09-14/0747`, `1029` and
`1229` extended with 0 entries; `raw/2026-09-14/1633/materialize.yaml` written with 76
entries (its stdout says 77: the folded reading counted) from the session ledger (60 lines)
and `1633/spec.md`: 1 `create` (rules) with its derived Estimate, 60 `update` (25 rules,
15 estimates, 4 insights, 3 lessons, 13 `file`), 2 `delete`, 4 `defer`, 2
`remove_criterion`, 4 `estimate`, 2 `lesson`; 35 decision groups; 0 unparsed lines. The
reading of ledger line 57 (`estimate-tests-clock-pinned`) folded into the `create` of
145.1, no entry of its own. The librarian merged nothing at
the index check, marked nothing `near`, appended nothing at synthesis.

`uv run guppi generate`: 0 pages for `0747`, `1029`, `1229`; 87 for `1633`; exit 0, stderr
empty. Stdout: 13 `file` entries "a Rule-class file, applied by hand" (147.8 ×3, 148.2 ×7,
149.1, 149.2 ×2); the two `remove_criterion` of 152 "case 141: no Estimate holds a block"
(a defer, no block). Entry 112.6 of `0747` (`failed`, `superseded_by: '130.1'`) skipped
without a line, as 151 says; its `failed` mark kept. The three defers of 141 in `1229`
marked `superseded_by: '152'`. `uv run guppi cleanup`: 11 pages moved, stderr empty.
`uv run guppi render`: stdout and stderr empty; four governed files differ from HEAD —
`CLAUDE.md` (144.1, 150.1), `.claude/agents/ask-guppi.md` (147.2, 147.9),
`.claude/agents/librarian-guppi.md` (147.3–147.5, 142.5, 147.9),
`.claude/skills/retro/SKILL.md` (150). `guppi render --check` exit 0 after.

| category | created | updated |
|---|---|---|
| decisions | 35 (`decision-case-142.1`…`154`, the list above) | 1 set `archived` by the supersedes cascade and moved by `cleanup` to `vault/archive/migration/2026-09-14/1633/decisions/`: `141` (by 152) |
| rules | 1 (`rule-tests-clock-pinned`, Leaf, `check`, child 7 of `rule-harness`, `built` by cascade) | 1 deleted (`rule-index`, 147.1, moved to `…/1633/rules/`); 17 by decision: `rule-materialize` (142.1, 142.4), `rule-page-generation` (142.2, 148.1, 151), `rule-case-protocol` (144.1), `rule-harness` (145.2, 153; child `rule-index` dropped by cleanup, `rule-tests-clock-pinned` last), `rule-ask` (147.2, 147.9), `rule-index-check` (147.3), `rule-synthesis` (147.4), `rule-documentation` (147.5, 149.4, 142.5, 147.9), `rule-cleanup` (147.6), `rule-lint` (147.7, 149.3), `rule-brief`, `rule-skill-hi`, `rule-claude-md` (149.4; 150.1), `rule-retro` (150), `rule-render-harness` (147.9); 3 `deferred_by`: `rule-lint` ← `decision-case-146`, `rule-ask` ← `decision-case-154`, `rule-work-mode` and `rule-subagent-guppi` `decision-case-141` → `decision-case-152`; 9 `built` → `draft` by the `pending` cascade (`rule-ask`, `rule-case-protocol`, `rule-cleanup`, `rule-documentation`, `rule-harness`, `rule-index-check`, `rule-lint`, `rule-retro`, `rule-synthesis`) |
| estimates | 1 (`estimate-tests-clock-pinned`, `passed` on line 57) | 1 deleted (`estimate-index-lists`, 147.1, moved); 13 criterion blocks appended: `estimate-materialize-assembles` +142.1, `estimate-generate-writes` +142.2 +148.1 +151, `estimate-case-protocol-loaded` +144.1, `estimate-ask-finds` +147.2, `estimate-index-check-merges` +147.3, `estimate-synthesis-clusters` +147.4, `estimate-documentation-completes` +147.5, `estimate-cleanup-moves` +147.6, `estimate-materialize-walks-dates` +142.4, `estimate-lint-catches` +149.3, `estimate-retro-loads` +150, `estimate-harness-pipeline` +153; 1 `replace` (`estimate-materialize-assembles`, 148.3); 4 readings written, all `passed`: `estimate-brief-written` (line 1), `estimate-materialize-assembles` (55), `estimate-materialize-walks-dates` (56), `estimate-generate-writes` (58); `pending` → `passed`: those three; 9 left `pending` |
| lessons | 2 (`lesson-obsidian-cli-needs-the-running-app`, `lesson-obsidian-property-links-need-wikilink-form`), `knowledge`, with `source`, `new` | 3 `source` added (144.2: `lesson-gate-plan-path-cut-by-the-event-log-detail-limit`, `lesson-agents-read-at-session-start-in-claude-code-2-1-228`, `lesson-retro-typed-by-the-person-bypasses-the-skill-tool-and-the-gate`); 8 set `archived` by the cascade of the four actioned Insights and moved to `…/1633/lessons/` |
| insights | 0 | 4 set `status: actioned` with `addressed_by`: `insight-harness-yaml-entry-shape-assumed` (142.3), `insight-librarian-frame-omits-required-reads` (143), `insight-materialize-lift-loses-a-schema-field` (144.3), `insight-tests-clock-not-pinned` (145.3); `severity` 0 on all four |
| entities | 0 | 0 |

The checks the handoff asks for, after the run:

- `rule-page-generation`: both inserts after "No entry ends the run." applied in ledger
  order (142.2 then 151), no failure.
- `rule-materialize`: blocks `142.1` on `estimate-materialize-assembles` (with `73.5`,
  `76`, `87`, `90.1`, `105.2`, `130.2`) and `142.4` on `estimate-materialize-walks-dates`
  (with `103.2`); both `passed`. `estimate-generate-writes`: blocks `142.2`, `148.1`,
  `151` appended after `124.2`; one reading, `passed`.
- `rule-tests-clock-pinned` created; `estimate-tests-clock-pinned` derived, block `145.1`,
  `passed`; `rule-tests-clock-pinned` `built`, `rule-harness` `draft` (its
  `estimate-harness-pipeline` `pending` by 153).
- `rule-harness` children: `rule-render-harness`, `rule-settings`, `rule-lint`,
  `rule-governed-files-hook`, `rule-claude-md`, `rule-bash-guard`, `rule-tests-clock-pinned`
  — no `rule-index`, the new Rule last; Purpose rewritten by 153.
- The four Purposes of 149.4 carry `[[brief]]`, `[[sprint]]`, `[[tags]]`, `[[glossary]]`,
  `[[case-schema]]`, `[[index]]`; lint raises no `ref` finding on them.
- The four renders listed above; `guppi render --check` exit 0.
- The Greps in place of the index files (147.2–147.4): `^(purpose|deferred_by):` over
  `wiki/rules/` 46 lines and over `wiki/entities/` 2 (both `schema.md`);
  `^(root_cause|deferred_by):` over `wiki/lessons/` 31 lines (29 lessons, 2 `schema.md`);
  `^(pattern|deferred_by):` over `wiki/insights/` 11 lines (10 Insights, 1 `schema.md`).
- Two `knowledge` lessons with `source`, no `incomplete`; no `near` candidate; no live
  lesson names Obsidian.
- `sprint.md` unchanged: the handoff says "no change".

## What the next session does first

1. The nine readings `pending` after this run: `estimate-lint-catches` (149.3: lint clean
   of `ref` on the four rules — the run of this brief already shows it, the line is not
   written), `estimate-cleanup-moves` (147.6: the run wrote no index — likewise),
   `estimate-harness-pipeline` (153), `estimate-ask-finds` (147.2),
   `estimate-index-check-merges` (147.3), `estimate-synthesis-clusters` (147.4),
   `estimate-documentation-completes` (147.5), `estimate-case-protocol-loaded` (144.1),
   `estimate-retro-loads` (150, at the next `/retro`). Nine Rules stand `draft` until then.
2. `estimate-brief-written` (124.1) against this brief; the live refusal of `guppi gate`
   (122) when it first happens.
3. Plan Mode over the Deferred list below: 146 (the orphan in lint) with the owner's
   Obsidian graph, 154 (`rule-ask`), Slice 3b.

## Deferred

1. **Slice 3b: Work Mode** — Case 152 (supersedes 141), `rule-work-mode` and
   `rule-subagent-guppi` (placeholders, `draft`, `deferred_by: [[decision-case-152]]`, the
   two lint orphans): the Spec as tasks with code, the ticked boxes, what a subagent may do,
   and the fork that comes back as a Case; the Plan Mode of a session of its own. Related
   Insight `insight-harness-agent-visibility`, `actioned`, severity 0. (postponed 11 times)
2. **`rule-ask`** — Case 154, `deferred_by: [[decision-case-154]]`: replace "One short
   question per Case" by "one question before a create without a ref, and one at pre-task;
   an update with a ref reads the page itself" — the Render's description line and the
   Purpose; a Case at the next Plan Mode. No related Insight. (stood in 1 brief)
3. **`rule-lint`** — Case 146, `deferred_by: [[decision-case-146]]`: decide whether an
   actioned Insight is exempt from the orphan check, or whether lint adopts Obsidian's
   notion of an orphan (no inbound link of any kind, decision pages included) once
   frontmatter refs are wikilinks (147); a Case at the next Plan Mode. The owner sees
   orphans in the graph after 148.1 (handoff). No related Insight; the ten actioned Insights
   are the ten `orphan` findings of lint. (stood in 1 brief)

Of the previous brief's five items, items 1–4 were the four `open` Insights and left it by
an `update` to `actioned` (142.3, 143, 144.3, 145.3); item 5 (Slice 3b, 141) was retired
by 152's `supersedes` and deferred again by 152, item 1 above. Items 2 and 3 are the
`defer` entries of this yaml, tied at count 1 and ordered by slug. No Insight is `open`;
none stands in the list.

## Flags

- **13 `file` entries marked `incomplete: [then]`**: the Rule-class updates of 147.8
  (`index`, `glossary`, `insights-schema`), 148.2 (`rules-schema`, `entities-schema`,
  `estimates-schema`, `lessons-schema`, `insights-schema`, `decisions-schema`, `index`),
  149.1 (`index`), 149.2 (`glossary`, `case-schema`). `generate` skips a `file` entry
  ("applied by hand"); the handoff records the hand edits as done. Same class as 133 in the
  previous run.
- **4 entries marked `exists`**: the defers of 146, 152 (×2), 154 on live Rule pages; the
  pages get `deferred_by`, no placeholder is written. Expected.
- **0 `failed`, 0 `near`, 0 `unparsed`, 0 `librarian`** in `1633`. Entry 112.6 of `0747`
  stays `failed` with `superseded_by: '130.1'`; since 151 it is skipped without a stderr
  line. It stays as it is; no repair.
- **1 new `ref` finding: `lessons/lesson-obsidian-property-links-need-wikilink-form`, "body
  names `slug`"**. The root cause quotes the literal form `"[[slug]]"`, and lint reads it as
  a wikilink to a page `slug`. The page is as the ledger line wrote it; the entry is not
  repaired. The same shape as `decision-case-140` (literal `decision-case-N`), still
  present.
- **Four new lint orphans**: the four actioned Insights; their eight children are
  archived, and no live page names them in its frontmatter. All ten Insights are now
  `orphan` findings — the matter of 146.
- **Nine Estimates `pending`, nine Rules `draft` by cascade** (the list under "What the
  next session does first"). No Estimate `failed`.
- **The 142.1 caveat of the handoff**: the code treats an entry carrying `librarian` as
  readable; the ratified text of `rule-materialize` says "a mapping without `line` and
  without `derived`". Recorded here as the handoff states it; no page opened.
- **Stale defers:** `rule-work-mode` and `rule-subagent-guppi` have stood as placeholders
  since Case 29 (now 152), without `kind`, `estimates` or `tags`; 8 `schema` findings and 2
  orphans.
- **No MOC candidate.** The vault holds no Entity page.
- **The handoff's instructions were all within the frame**; none was refused. Its
  expectations held: the two `path` findings on `rule-index` and the three `source`
  findings are gone; the two placeholders and the 62 of Cases 1–28 stay; the orphan count
  rose by four.
- **Archive (run after the brief): nothing moved.** `uv run guppi archive` exit 0, stdout
  and stderr empty. `raw/2026-09-14/0747`, `1029` and `1229` are kept by the date guard (a
  unit dated today is skipped without a line); `1633` is the session of the run, never
  moved. The three units move at the first run on a later date.
- **Lint.** `make lint` exits 1 at its second step (`guppi lint`); `guppi render --check`
  exit 0. `guppi lint`: 84 findings, exit 1 — 70 `schema` (31 missing `## Context`, 31
  `## Problem`, on the decision pages of Cases 1–28; `kind`, `estimates`, `tags`,
  `## Estimates` on the two placeholders), 2 `ref` (`decision-case-140`,
  `lesson-obsidian-property-links-need-wikilink-form`), 12 `orphan` (the two placeholders,
  the ten actioned Insights). 84 before this run: −2 `path` (`rule-index`), −3 `schema`
  (`source`), +1 `ref`, +4 `orphan`.

## Readings at the close

- `make test` → 368 passed.
- `make lint` → exit 1 at `guppi lint`; `guppi render --check` → exit 0; `guppi lint` → 84
  findings, exit 1.
- Live pages, 341: rules 40 (29 `built`, 11 `draft`), entities 0, estimates 42 (33
  `passed`, 9 `pending`), lessons 23 (all `new`), insights 10 (all `actioned`), decisions
  226 (all `current`).
- `vault/archive/migration/` holds 97 pages: the 86 of the previous brief and 11 under
  `2026-09-14/1633/`: 1 `decisions/` (`141`), 1 `rules/` (`rule-index`), 1 `estimates/`
  (`estimate-index-lists`), 8 `lessons/`; and the raw of the dates 09-09…09-13 under
  `<date>/[HHMM/]raw/`. `cleanup` moved 11 in this run.
- `raw/2026-09-14/1633/materialize.yaml`: 76 entries, all `applied`, 35 decision groups,
  0 unparsed lines, 13 `incomplete`, 0 `failed`, 0 `near`, 4 `exists`, 0 `librarian`.
  `0747`: 1 `failed` (112.6, `superseded_by`). `1229`: the three entries of 141
  `superseded_by: '152'`.
