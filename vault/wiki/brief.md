# Brief — 2026-09-21, after session 2106 of 2026-09-20 (a replaced Criterion is not read at the Retro of its session by 283; the mark `{addresses}` on a decision line by 284.2, carried by materialize by 284.3, kept by synthesis by 284.4; `insight-session-vault-knowledge-not-loaded` actioned by 284.1; Slice 3b deferred to 285)

Written by the librarian from `raw/2026-09-20/2106/handoff.md`, the yamls of
`raw/2026-09-20/2106`, `raw/2026-09-20/1749`, `raw/2026-09-20/1308`, `raw/2026-09-20/0958`,
`raw/2026-09-20/0740` and `raw/2026-09-20/0527`, and the Greps of the indexes.

## Where things stand

- Code, commit `17ffa7d` on `migration`: `guppi/materialize.py` — `parse_line` collects the
  `addresses` marks (one per lesson, the key repeated), `decision_entry` carries `addresses`,
  `mark_addressed` in `lift_line` sets `addressed_by: decision-case-N` on the lesson entries of
  the unit and `incomplete: [addresses]` on a decision entry without a pair; the docstring names
  `addresses`, `addressed_by` and the new `incomplete` value. `tests/test_materialize.py` +2.
  464 green, style clean. By hand, committed: `vault/wiki/index.md` §4 (the `addresses` item)
  and §8 (the exception), `vault/wiki/insights/schema.md` (the `status` row, a paragraph under
  Reopening), `vault/wiki/glossary.md` (the Status models row). Spec 2106: 7 task lines ticked
  by the session.
- Closed in the session: 283, 284.1, 284.2, 284.3, 284.4; 285 the defer of Slice 3b
  (`rule-work-mode`, `rule-subagent-guppi`, the fourteenth). Readings in the 2106 ledger,
  `passed`: `estimate-case-protocol-loaded` (L1, the schema as loaded at `/hi`),
  `estimate-generate-ticks-the-spec` (L2, the librarian's run of 1749 read by `git show`).
  Lesson: `lesson-retro-reading-of-a-replaced-criterion` (L5, error).
- Not done by the session's own account: the pages, the three renders and `guppi sprint` —
  this run; the readings of `estimate-retro-loads` and
  `estimate-case-protocol-ledger-line-form` — the next session; the readings of the two new
  Estimates — the first marked lesson, no date; Slice 3b — defer 285. No red test, no patch.
- Six units in the walk. `raw/2026-09-20/2106`: 18 entries lifted from the ledger, as the
  handoff expected — 2 readings, 1 lesson, 15 decision entries — plus 6 Decision pages added
  by `generate`; all 24 applied, no stderr. Decisions: 6 pages written (283, 284.1, 284.2,
  284.3, 284.4, 285). Rules: 4 updated by `replace` (`rule-retro` 283, `rule-case-protocol`
  284.2, `rule-materialize` 284.3, `rule-synthesis` 284.4), 2 deferred (`rule-work-mode`,
  `rule-subagent-guppi` by 285, both marked `exists`). Estimates: 2 created
  (`estimate-materialize-carries-addresses` on `rule-materialize`,
  `estimate-synthesis-keeps-actioned-by-the-mark` on `rule-synthesis`, both `pending`), 2
  `update` entries applied (`estimate-retro-loads` 283, `estimate-case-protocol-ledger-line-form`
  284.2, both the Criterion replaced whole and `pending`), 2 reading lines applied on 2 pages
  (`passed`). Lessons: 1 created (`new`, no pair at synthesis);
  `lesson-spec-render-line-form-unmatched-by-the-ticker` `archived` by the cascade of 284.1.
  Insights: 1 updated (`insight-session-vault-knowledge-not-loaded`, `open → actioned`,
  `addressed_by: [[decision-case-284.1]]`, `severity` 0). Rule-class `file` items: 4 reported
  by `generate` as applied by hand (`index` 284.2; `insights-schema`, `index`, `glossary`
  284.4). 21 pages written or changed. `1749`, `1308`, `0958`, `0740`, `0527`: 0 new entries.
  Cleanup moved 1 page.
- The check the handoff asked first held: 18 entries in the yaml; the `update` of
  `estimate-retro-loads` carries the Criterion of 283 and `set: {status: pending}`; after the
  run the page stands `pending` and `rule-retro` `built → draft`.
- Statuses computed by `generate`: `rule-retro` `built → draft` (`estimate-retro-loads`
  `pending`); `rule-materialize` and `rule-synthesis` `built → draft` (their new Estimates
  `pending`); `rule-case-protocol` stays `draft` (`estimate-case-protocol-ledger-line-form`
  `pending` by 284.2); `rule-page-generation` stays `draft` (`estimate-generate-rewords`
  `pending`). `deferred_by` of `rule-work-mode` and `rule-subagent-guppi` now ends at
  `decision-case-285`.
- `guppi render` wrote `.claude/skills/retro/SKILL.md` (283), `vault/wiki/case-schema.md`
  (284.2) and `.claude/agents/librarian-guppi.md` (284.4) — the three the handoff named, one
  line each, no other; `uv run guppi render --check` after it exits 0. `guppi sprint` rewrote
  `vault/wiki/sprint.md`: Slice 3b current, both items `draft`, their defers ending at 285.
- The `read` lines ticked by this run's `generate`: 1749 line 39
  (`estimate-case-protocol-loaded`, L1 — the first unticked `read` of that slug in the oldest
  Spec that holds one; line 88 of the same Spec stays `[ ]`) and 1749 line 179
  (`estimate-generate-ticks-the-spec`, L2). The 2106 Spec holds no `read` line of either slug,
  and its four `read` lines (44, 119, 158, 210) stay `[ ]`. 1308 line 132
  (`estimate-retro-loads`, the old Criterion) stays `[ ]` — not debt by 283.
- `guppi archive` moved five applied units whole — `raw/2026-09-20/0527`, `0740`, `0958`,
  `1308`, `1749` — to `archive/migration/2026-09-20/<HHMM>/raw/`; `raw/2026-09-20/2106`, the
  session of the run, stays. The Spec lines this brief names for 1308 and 1749 are read there
  now.
- Tests: 464 green (`make test`), style clean at `17ffa7d`.

## Readings due

No Estimate stands `failed` after `generate`.

- `estimate-retro-loads` — `rule-retro` stands `draft` — read at line 44 of
  `raw/2026-09-20/2106/spec.md`: the first `/retro` after the render, by hand — the next
  session, by the rule of 283. The Criterion is the one of 283; the line 132 of the 1308 Spec
  is the old Criterion's and is not read.
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` stands `draft` — read at
  line 119 of `raw/2026-09-20/2106/spec.md`: `case-schema.md` and `index.md` §4 after the
  render, by hand — at the next session start.
- `estimate-materialize-carries-addresses` — `rule-materialize` stands `draft` — read at line
  158 of `raw/2026-09-20/2106/spec.md`: pytest; live — the librarian's run on the first marked
  lesson. No marked lesson in this walk. No date.
- `estimate-synthesis-keeps-actioned-by-the-mark` — `rule-synthesis` stands `draft` — read at
  line 210 of `raw/2026-09-20/2106/spec.md`: the librarian's run on the first marked lesson
  under an actioned Insight, by hand. No date.
- `estimate-generate-rewords` — `rule-page-generation` stands `draft` — read at line 745 of
  the 1308 Spec, now `archive/migration/2026-09-20/1308/raw/spec.md` (moved by this run's
  `guppi archive`): pytest now; live — the first `reword` applied, in a later
  session (case 277.4). No `reword` in this walk. No date.
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` stands `draft` — by its
  `method`: `make lint`, exit 0 — or only unread lines on the Estimates of
  `entity-sprint-migration`.
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` — by its `method`:
  one reading of the tree by hand at the close of the sprint, each path and decision named in
  the estimate line.
- `estimate-sprint-migration-merges` — `entity-sprint-migration` — by its `method`:
  `make test` on the last commit of `migration`, then `git log` of `main` after the merge.

## Deferred

The list is empty. `insight-session-vault-knowledge-not-loaded`, item 1 of the previous brief,
is `actioned` by 284.1 this run and leaves the list.

Left out, the sprint page names them (case 229.4): `rule-work-mode` and `rule-subagent-guppi`
(defer 285 this walk, the fourteenth; 183, 206, 218, 231, 242, 248, 252, 254, 260, 263, 269,
276, 281 before — Slice 3b, the current milestone);
`insight-workflow-code-live-before-the-page-it-reads` (`open`, `severity` 2, defer 238; in the
text of the `rule-work-mode` item); `rule-git-context`, `rule-github-issues` (in the text of
the `estimate-sprint-migration-merges` item, Slice 5); `rule-spec-box` (Slice 5); `rule-morph`
(Slice 5).

## Flags

- The tick of `estimate-case-protocol-loaded` (2106 L1) landed on 1749 line 39, under the
  superseded 278, not on line 88 under 279.1 as the handoff expected; line 39 is the first
  unticked `read` of that slug in the oldest Spec that holds one, and the reading of 2106 is
  later than 278 and 279.1 alike, so the rule of 280 skips neither. Line 88 stays `[ ]`. Not
  repaired. The previous brief named line 39 as "not its line (282)"; 282 keeps the lines of a
  superseded Case out of the Retro count, and `generate` does not read `superseded_by` when it
  ticks.
- Two `exists` marks on the defers of 285 (expected: a `defer` with a `ref`). No entry marked
  `incomplete`, `failed` or `unparsed` in the six yamls; no `near`; no failed Estimate; no MOC
  candidate.
- Index check: the two `create` entries are Estimates, no index. The lesson (L5): the Grep
  `^(root_cause|deferred_by):` over `vault/wiki/lessons/` returned 43 lines; none names a
  reading taken on a Criterion a Case of the same session replaced, nor a Render that leaves
  unsaid which Criterion a reading measures. The nearest by subject,
  `lesson-estimate-update-must-carry-its-criterion-whole` (the mechanism of a Criterion
  replacement, heavy for a correction of a word) and
  `lesson-spec-render-line-form-unmatched-by-the-ticker` (a form held in one page and absent
  from the text the Spec is written from), are other causes. No `near`.
- Synthesis: the Greps `^(root_cause|deferred_by):` over `vault/wiki/lessons/` (43 lines) and
  `^(pattern|deferred_by):` over `vault/wiki/insights/` (16 lines).
  `insight-workflow-contract-change-leaves-its-derived-text-stale` (page read: Pattern and
  History) — not the same: its children are one contract in two places with only one changed
  and no pointer between them; here the Estimate page was replaced by 282 through the
  mechanism, and the gap is in the Retro Render itself (no text said which Criterion a reading
  measures), closed by 283 in the same session. `insight-session-vault-knowledge-not-loaded`
  (index line) — not the same: no page held the missing fact. Not clustered; the lesson stays
  `new`, no entry added. The Insight of 284.1 was not reopened.
- The lesson of 283 (L5) carries no `addresses` mark — 283's decision lines (L3–L4) were
  written before 284.2 existed; `mark_addressed` set no `addressed_by`. The cause is closed
  by 283 in this session (from the handoff). No `incomplete: [addresses]`, since 283's lines
  carry no mark at all.
- `lesson-spec-render-line-form-unmatched-by-the-ticker` `archived` by the cascade of 284.1
  (the lessons of an actioned Insight), moved by cleanup to
  `vault/archive/migration/2026-09-21/2106/lessons/`; `insight-session-vault-knowledge-not-loaded`
  keeps it in `children`, `severity` 0.
- The `update` of `estimate-case-protocol-ledger-line-form` (284.2) replaced the Criterion
  whole and set `pending` while the page stood `passed` by the reading of 1749; the History
  carries both. Same for `estimate-retro-loads` (283) — the `passed` of 1749 on the Criterion
  of 270.3 is undone by this `pending`, as the handoff expected.
- Rule-class `file` items of 284.2 and 284.4 (`index` ×2, `insights-schema`, `glossary`):
  `generate` reported "a Rule-class file, applied by hand" for each, on stdout; all four are
  ticked in the 2106 Spec by the session.
- The 2106 Spec's four `read` lines (44, 119, 158, 210) stay `[ ]`; 1308 line 132 stays `[ ]`
  and is not debt by 283; 1308 line 745 waits for the first `reword`; 1749 line 88 stays `[ ]`
  (see the first flag). The lines 38–39 of the 1749 Spec belong to the superseded 278: line 38
  `[x]` by 1749's librarian, line 39 `[x]` by this run.
- The Deferred list of the previous brief had one item, `insight-session-vault-knowledge-not-loaded`;
  it left by the `update` of 284.1 (`status: actioned`), not by a `supersedes`; no `defer` of
  this walk has a target outside the sprint page, and the one `open` Insight is named there.
- Lint, gone since the previous brief: none. New: 4 `unread: pending` (`estimate-retro-loads`,
  `estimate-case-protocol-ledger-line-form`, `estimate-materialize-carries-addresses`,
  `estimate-synthesis-keeps-actioned-by-the-mark`); gone: 2 (`estimate-case-protocol-loaded`,
  `estimate-generate-ticks-the-spec`, `passed`). `unmigrated` stays 23.
- Standing: the defer of 238 on `insight-workflow-code-live-before-the-page-it-reads` without a
  `purpose`; `estimate-hi-no-read-calls` in the shape before case 193 by choice;
  `rule-spec-box` placeholder findings (`kind`, `estimates`, orphan).
- Stale defers by lint: `rule-work-mode` and `rule-subagent-guppi` 26 times since case 29;
  `rule-morph` 1 time since case 239.
- Lint, 77 findings: 2 `rules/rule-spec-box` schema (`kind`, `estimates`) and 1 orphan;
  62 `decisions/decision-case-<1–28>` missing `## Context` and `## Problem` (31 pages,
  Slice 5); 3 deferred (`rule-morph` 1, `rule-subagent-guppi` 26, `rule-work-mode` 26);
  8 unread pending (`estimate-case-protocol-ledger-line-form`, `estimate-generate-rewords`,
  `estimate-materialize-carries-addresses`, `estimate-retro-loads`,
  `estimate-synthesis-keeps-actioned-by-the-mark`, the three sprint Estimates);
  `estimates: unmigrated: 23 pages in the shape before case 193`.

## Next session

Cases

- Slice 3b — `rule-work-mode`, `rule-subagent-guppi` (defer 285, the fourteenth), with the
  sentence of `insight-workflow-code-live-before-the-page-it-reads` written into
  `rule-work-mode`; from the handoff and the sprint page.
- The tick of `estimate-case-protocol-loaded` on 1749 line 39, under the superseded 278, while
  line 88 under 279.1 stays open — from the Flags; whether a `read` line of a superseded Case
  is one `generate` may tick is a contract question, a fact for the reading of
  `estimate-generate-ticks-the-spec` otherwise.

Work

- Read `estimate-retro-loads` at the first `/retro` after this render (2106 line 44).
- Read `estimate-case-protocol-ledger-line-form` on `case-schema.md` and `index.md` §4 at the
  session start (2106 line 119).
- Read `estimate-materialize-carries-addresses` (2106 line 158) and
  `estimate-synthesis-keeps-actioned-by-the-mark` (2106 line 210) at the first marked lesson;
  no date.
- Read `estimate-generate-rewords` at the first `reword` (1308 line 745); no date.
- Read `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-leftovers-gone`,
  `estimate-sprint-migration-merges` — at the close of the sprint, by their `method`.
- No ledger line of the walk left unapplied; the tree is clean after the commit of this run.

## Readings at the close

- `make test`: 464 passed.
- `make lint`: 77 findings, exit 1 (the list above).
- Pages: entities 2, rules 46, estimates 75, lessons 41, insights 14, decisions 401.
