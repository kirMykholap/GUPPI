# Brief — 2026-09-21, after session 0019 of 2026-09-21 (tick_read skips the read lines of a superseded Case by 286; `guppi recall` on `SessionStart compact` by 287; the glossary leaves `CLAUDE.md` for `/hi` by 288.1, the one rule enters the Case schema by 288.2, `CLAUDE.md` cut to the Render of `rule-claude-md` by 288.3; the texts of 290.x; Slice 3b deferred to 289)

Written by the librarian from `raw/2026-09-21/0019/handoff.md`, the yamls of
`raw/2026-09-21/0019` and `raw/2026-09-20/2106`, and the Greps of the indexes.

## Where things stand

- Code, commit `d4f3479` on `migration`: `guppi/generate.py` — `superseded_cases`,
  `superseded_beside`, `tick_read` takes `superseded` and skips the marked Cases in every Spec
  (the run's entries for the Spec beside the yaml, the `materialize.yaml` beside each other
  Spec), `Vault.tick` passes it for `estimate` and folded `create` entries; `tests/test_generate.py`
  +4. `guppi/recall.py` new — the `SessionStart compact` hook; `guppi/cli.py` — the `recall`
  command; `tests/test_recall.py` +7. By hand, committed: `vault/wiki/glossary.md` (290.1: the
  header and the `CLAUDE.md` row); `vault/archive/migration/2026-09-20/1749/raw/spec.md` (286:
  line 39 `[ ]`, line 88 `[x]`). 475 green, style clean. Spec 0019: 6 task lines ticked by the
  session.
- Closed in the session: 286, 287, 288.1, 288.2, 288.3, 290.1, 290.2, 290.3; 289 the defer of
  Slice 3b (`rule-work-mode`, `rule-subagent-guppi`, the fifteenth). Readings in the 0019
  ledger, `passed`: `estimate-case-protocol-ledger-line-form` (L1, at `/hi`),
  `estimate-retro-loads` (L21, at Retro). No lesson line.
- Not done by the session's own account: the pages, the four renders and `guppi sprint` — this
  run; the five `read` lines of Spec 0019 (56, 158, 214, 251, 299) — later sessions by their
  `method`; Slice 3b — defer 289. No red test, no patch. The registration of `guppi recall`
  landed with this run's render of `.claude/settings.json`.
- Two units in the walk. `raw/2026-09-21/0019`: 21 entries lifted from the ledger, as the
  handoff expected — 2 readings, 19 decision entries — plus 9 Decision pages added by
  `generate`; all 30 applied, no stderr, `unparsed` empty. Decisions: 9 pages written (286,
  287, 288.1, 288.2, 288.3, 289, 290.1, 290.2, 290.3). Rules: 1 created (`rule-compact-recall`,
  Leaf, child of `rule-session-start`, `draft`), 7 `update` entries applied on 6 pages
  (`rule-page-generation` 286; `rule-session-start` 287 and 290.2; `rule-hook-registry` 287;
  `rule-internal-context` 288.1; `rule-case-protocol` 288.2 and 290.3; `rule-claude-md`
  288.3), 2 deferred (`rule-work-mode`, `rule-subagent-guppi` by 289, both marked `exists`).
  Estimates: 1 created (`estimate-compact-recall-reloads` on `rule-compact-recall`,
  `pending`), 6 `update` entries applied on 4 pages (`estimate-generate-ticks-the-spec` 286
  and 290.3, `estimate-internal-context-loaded` 288.1 and 290.3, `estimate-case-protocol-loaded`
  288.2, `estimate-claude-md-rendered` 288.3 — the Criterion replaced whole and `pending` on
  each), 2 reading lines applied on 2 pages (`passed`). Lessons: none. Insights: none.
  Rule-class `file` item: 1 reported by `generate` as applied by hand (`glossary` 290.1). 26
  pages written or changed. `raw/2026-09-20/2106`: 0 new entries. Cleanup moved 0 pages.
- The checks the handoff asked first held: 21 entries in the yaml in the order named (286's
  `update` of `estimate-generate-ticks-the-spec` at line 3 before 290.3's at line 18; 288.1's
  at 9 before 290.3's at 19; 288.2's at 10 before 290.3's at 20; 287's `update` of
  `rule-session-start` at 6 before 290.2's at 17; the create of `rule-compact-recall` at 4
  before line 6). The `sections: Render` of 287's `update` of `rule-hook-registry` equals the
  page's Render plus one `{ "matcher": "compact", ... "uv run guppi recall" }` entry under
  `SessionStart` (a diff of the two: three lines). After `generate` the Render of
  `rule-case-protocol` reads `# Case — schema`, `## The one rule`, the paragraph, then the
  sections as before. `rule-session-start` lists `rule-compact-recall` once as its fourth
  child.
- Statuses computed by `generate`: `rule-internal-context` `built → draft`
  (`estimate-internal-context-loaded` `pending`); `rule-claude-md` `built → draft`
  (`estimate-claude-md-rendered` `pending`); `rule-compact-recall` `draft`
  (`estimate-compact-recall-reloads` `pending`); `rule-page-generation` stays `draft`
  (`estimate-generate-rewords`, `estimate-generate-ticks-the-spec` `pending`);
  `rule-case-protocol` stays `draft` (`estimate-case-protocol-loaded` `pending`); `rule-retro`
  `draft → built` (`estimate-retro-loads` `passed`); `rule-session-start` and
  `rule-hook-registry` stay `built`. `deferred_by` of `rule-work-mode` and
  `rule-subagent-guppi` now ends at `decision-case-289`.
- `guppi render` wrote `.claude/settings.json` (287), `.claude/skills/hi/SKILL.md` (288.1),
  `vault/wiki/case-schema.md` (288.2) and `CLAUDE.md` (288.3) — the four the handoff named,
  no stderr; `uv run guppi render --check` after it exits 0. `guppi sprint` rewrote
  `vault/wiki/sprint.md`: Slice 3b current, both items `draft`, their defers ending at 289.
- The `read` lines ticked by this run's `generate`: 2106 line 44 (`estimate-retro-loads`, L21)
  and 2106 line 119 (`estimate-case-protocol-ledger-line-form`, L1) — the first unticked
  `read` of each slug in the oldest Spec of `raw/`. `tick_read` read the 2106 yaml through
  `superseded_beside` (`guppi/generate.py`): no superseded Case there, nothing skipped. Spec
  0019: 16 page lines ticked by `generate`, 4 render lines (157, 213, 250, 298) by `guppi render`
  (6 by the session before, 26 in all); its 5 `read` lines stay `[ ]`.
- `guppi archive` moved one applied unit whole — `raw/2026-09-20/2106` — to
  `archive/migration/2026-09-20/2106/raw/`; `raw/2026-09-21/0019`, the session of the run,
  stays. The 2106 Spec lines this brief names are read there now.
- Tests: 475 green (`make test`), style clean.

## Readings due

No Estimate stands `failed` after `generate`.

- `estimate-generate-ticks-the-spec` — `rule-page-generation` stands `draft` — read at line 56
  of `raw/2026-09-21/0019/spec.md`: pytest now; live — the first librarian's run whose ledger
  holds a `{supersedes:case N}` and a reading of a slug with a `read` line under the superseded
  Case. None in this walk. No date.
- `estimate-compact-recall-reloads` — `rule-compact-recall` stands `draft` — read at line 158
  of `raw/2026-09-21/0019/spec.md`: pytest; live — the first compaction of a working session,
  by hand, the hook's text in the context after it. No date.
- `estimate-internal-context-loaded` — `rule-internal-context` stands `draft` — read at line
  214 of `raw/2026-09-21/0019/spec.md`: the `/hi` of the next session, by hand.
- `estimate-case-protocol-loaded` — `rule-case-protocol` stands `draft` — read at line 251 of
  `raw/2026-09-21/0019/spec.md`: the `/hi` of the next session, by hand.
- `estimate-claude-md-rendered` — `rule-claude-md` stands `draft` — read at line 299 of
  `raw/2026-09-21/0019/spec.md`: `render --check` after the build; the start of the next
  session, by hand.
- `estimate-materialize-carries-addresses` — `rule-materialize` stands `draft` — read at line
  158 of the 2106 Spec, now `archive/migration/2026-09-20/2106/raw/spec.md` (moved by this
  run's `guppi archive`): pytest; live — the librarian's run on the first marked lesson. No
  marked lesson in this walk. No date.
- `estimate-synthesis-keeps-actioned-by-the-mark` — `rule-synthesis` stands `draft` — read at
  line 210 of the same archived 2106 Spec: the librarian's run on the first marked lesson under
  an actioned Insight, by hand. No date.
- `estimate-generate-rewords` — `rule-page-generation` stands `draft` — read at line 745 of
  the 1308 Spec, `archive/migration/2026-09-20/1308/raw/spec.md`: pytest now; live — the first
  `reword` applied (case 277.4). No `reword` in this walk. No date.
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` stands `draft` — by its
  `method`: `make lint`, exit 0 — or only unread lines on the Estimates of
  `entity-sprint-migration`; at the close of the sprint.
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` — by its `method`:
  one reading of the tree by hand at the close of the sprint, each path and decision named in
  the estimate line.
- `estimate-sprint-migration-merges` — `entity-sprint-migration` — by its `method`: `make test`
  on the last commit of `migration`, then `git log` of `main` after the merge.

## Deferred

The list is empty. The previous brief's list was empty; the two `defer` targets of this walk
(289) and the one `open` Insight are named on the sprint page.

Left out, the sprint page names them (case 229.4): `rule-work-mode` and `rule-subagent-guppi`
(defer 289 this walk, the fifteenth; 183, 206, 218, 231, 242, 248, 252, 254, 260, 263, 269,
276, 281, 285 before — Slice 3b, the current milestone);
`insight-workflow-code-live-before-the-page-it-reads` (`open`, `severity` 2, defer 238; in the
text of the `rule-work-mode` item); `rule-git-context`, `rule-github-issues` (in the text of
the `estimate-sprint-migration-merges` item, Slice 5); `rule-spec-box` (Slice 5); `rule-morph`
(Slice 5).

## Flags

- Two `exists` marks on the defers of 289 (a `defer` with a `ref` on a page on disk, as with
  285). No entry marked `incomplete`, `failed` or `unparsed` in the two yamls; no `near`; no
  failed Estimate; no MOC candidate.
- Index check: `rule-compact-recall` (287) against the Grep `^(purpose|deferred_by):` over
  `vault/wiki/rules/`, 56 lines. No line names a session going on after a compaction:
  `rule-session-start` is its `ref`, the MOC; `rule-internal-context` and `rule-skill-hi` are
  the load at `/hi`, another moment. Not the same, not near; no page opened. The other create
  is an Estimate, no index. No lesson, no synthesis.
- The handoff expected 21 page lines of Spec 0019 ticked by `generate`; the Spec holds 16 page
  lines, all ticked by this run (no line for the defers of 289 or for `guppi sprint` exists in
  the Spec); the count in the handoff is not the Spec's.
- From the handoff, facts with no page: `estimate-hook-registry-rendered` says "four event
  keys" while `.claude/settings.json` has five — stale before this session, for its next
  reading; "Add no new dependencies, Python or otherwise" stands in `CLAUDE.md` under
  Commands (288.3) with no Rule behind it — a `check` if wanted, a Case; the hooks guide's
  10,000-character stdout cap is documented for `PostToolUse`, not stated for `SessionStart`
  — measured at the reading of `estimate-compact-recall-reloads`; `@` lines in a SKILL.md are
  not documented by Claude Code, they work here and `guppi recall` reads them.
- From the handoff, the tools: `guppi/generate.py` came out CRLF after an Edit-tool change
  (HEAD is LF; converted back before `d4f3479`) — `git diff --stat` before a commit shows the
  CRLF warning; none in this run. `bashguard` refuses a heredoc with a backslash — a Python
  script goes to the scratchpad by Write. A multi-line `old` in `replace` does not survive
  YAML indentation — `sections` whole instead (287's `rule-hook-registry`). The probe of
  `guppi recall` on session 0019: 2,552 characters — header, three `@` paths, `frontier.md`,
  `spec.md`, the Frontier text; `startup` prints nothing.
- Argued down in the chat, no Case: a separate `rule-info` page for the project description
  (no Rule by the glossary's check; it stays the own text of `rule-claude-md`'s Render); a
  "session page" rendered for `/hi` (`rule-internal-context` plus `case-schema.md` already).
  The one rule stands in `index.md` §0 and in the Case schema (288.2) — two texts, as before
  with `CLAUDE.md` and §0.
- Rule-class `file` item of 290.1 (`glossary`): `generate` reported "a Rule-class file, applied
  by hand" on stdout; ticked in Spec 0019 line 332 by the session.
- The `update` entries of 286, 288.1, 288.2 and 288.3 replaced the Criterion whole and set
  `pending` on four Estimates that stood `passed` (`estimate-generate-ticks-the-spec` by 2106,
  `estimate-internal-context-loaded`, `estimate-case-protocol-loaded` by 2106,
  `estimate-claude-md-rendered`); the History of each carries both, as the handoff expected.
- The 1749 Spec, archived: line 39 `[ ]` and line 88 `[x]` by hand (286), the swap the
  previous brief's second Case asked for; `tick_read` now skips a superseded Case's lines.
- Lint, gone since the previous brief: 2 `unread: pending` (`estimate-retro-loads`,
  `estimate-case-protocol-ledger-line-form`, `passed`). New: 5 `unread: pending`
  (`estimate-case-protocol-loaded`, `estimate-claude-md-rendered`,
  `estimate-compact-recall-reloads`, `estimate-generate-ticks-the-spec`,
  `estimate-internal-context-loaded`); the stale-defer count of `rule-work-mode` and
  `rule-subagent-guppi` 26 → 27. `unmigrated` stays 23.
- Standing: the defer of 238 on `insight-workflow-code-live-before-the-page-it-reads` without a
  `purpose`; `estimate-hi-no-read-calls` in the shape before case 193 by choice;
  `rule-spec-box` placeholder findings (`kind`, `estimates`, orphan).
- Stale defers by lint: `rule-work-mode` and `rule-subagent-guppi` 27 times since case 29;
  `rule-morph` 1 time since case 239.
- Lint, 80 findings: 2 `rules/rule-spec-box` schema (`kind`, `estimates`) and 1 orphan;
  62 `decisions/decision-case-<1–28>` missing `## Context` and `## Problem` (31 pages,
  Slice 5); 3 deferred (`rule-morph` 1, `rule-subagent-guppi` 27, `rule-work-mode` 27);
  11 unread pending (`estimate-case-protocol-loaded`, `estimate-claude-md-rendered`,
  `estimate-compact-recall-reloads`, `estimate-generate-rewords`,
  `estimate-generate-ticks-the-spec`, `estimate-internal-context-loaded`,
  `estimate-materialize-carries-addresses`, `estimate-synthesis-keeps-actioned-by-the-mark`,
  the three sprint Estimates); `estimates: unmigrated: 23 pages in the shape before case 193`.

## Next session

Cases

- Slice 3b — `rule-work-mode`, `rule-subagent-guppi` (defer 289, the fifteenth), with the
  sentence of `insight-workflow-code-live-before-the-page-it-reads` written into
  `rule-work-mode` and, by 289's `purpose`, a subagent loads `CLAUDE.md` and no glossary
  (288.1); from the handoff and the sprint page.
- "Add no new dependencies, Python or otherwise" — a line of `CLAUDE.md` with no Rule behind
  it (it came with the hand-written file of 59.8); a Rule with a `check` if the condition is
  wanted — from the handoff's notes.

Work

- Read `estimate-internal-context-loaded` (0019 line 214) and `estimate-case-protocol-loaded`
  (0019 line 251) at the next `/hi`, by hand.
- Read `estimate-claude-md-rendered` (0019 line 299) at the next session start: `render
  --check`, by hand.
- Read `estimate-compact-recall-reloads` (0019 line 158) at the first compaction of a working
  session, by hand; no date.
- Read `estimate-generate-ticks-the-spec` (0019 line 56) at the first librarian's run with a
  `{supersedes}` and a reading under the superseded Case; no date.
- Read `estimate-generate-rewords` at the first `reword` (1308 line 745, archived); no date.
- Read `estimate-materialize-carries-addresses` (2106 line 158, archived) and
  `estimate-synthesis-keeps-actioned-by-the-mark` (2106 line 210, archived) at the first
  marked lesson; no date.
- Read `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-leftovers-gone`,
  `estimate-sprint-migration-merges` — at the close of the sprint, by their `method`; the
  sprint page holds them under Slices 4 and 5.
- No ledger line of the walk left unapplied; no unticked box in Spec 0019 but the five `read`
  lines above; the tree is clean after the commit of this run.

## Readings at the close

- `make test`: 475 passed.
- `make lint`: 80 findings, exit 1 (the list above).
- Pages: entities 2, rules 47, estimates 76, lessons 41, insights 14, decisions 410.
