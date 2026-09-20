# Brief — 2026-09-20, after session 0958 of 2026-09-20 (the debts of the Frontier by Cases 264–266, the story sections of the Case protocol by 267, the Frontier in two lists by 268, Slice 3b deferred to 269)

Written by the librarian from `raw/2026-09-20/0958/handoff.md`, the yamls of
`raw/2026-09-20/0958`, `raw/2026-09-20/0740` and `raw/2026-09-20/0527`, and the Greps of
the indexes. The first brief by the frame of case 268.1: the section Next session stands
between Flags and Readings at the close.

## Where things stand

- Code, commit `ad57dc0` on `migration`: `guppi/prespec.py` — `plan_prose`, `known_slugs`,
  `check_bare_links`, called from `check`, the docstring bullet; `guppi/materialize.py` —
  `DEFER_KEYS`, the `defer` branch of `_lift_item`, the docstring; `tests/test_prespec.py`
  +9 (eight for 264.2, one for the `C1`/`W1` lines of 268.2); `tests/test_materialize.py`
  +1 with two new cases in the schema fixture. 443 green, style clean. By hand:
  `vault/wiki/estimates/estimate-generate-renames.md` History line of 262;
  `vault/wiki/case-schema.md` the story-sections paragraph; `vault/wiki/glossary.md` the
  `/hi`, Frontier row.
- Closed in the session: 264.1, 264.2, 265, 265.1–265.4, 266, 267, 268.1, 268.2; 269
  deferred. Readings `passed`, all in the 0958 ledger: `estimate-prespec-reconciles`,
  `estimate-prespec-catches-bare-wikilinks`, `estimate-event-log-records`,
  `estimate-plan-mode-verified`, `estimate-materialize-assembles`,
  `estimate-retro-commit-gates`, `estimate-case-protocol-case-form`. Lessons:
  `lesson-spec-change-text-quotes-a-wikilink-bare` (error),
  `lesson-estimate-update-must-carry-its-criterion-whole` (knowledge),
  `lesson-agent-memory-is-not-the-product` (error).
- Not done by the session's own account: the readings of `estimate-documentation-completes`
  (the librarian's run of this session — this run, read in the next), `estimate-brief-written`
  (this brief, read in the next session), `estimate-hi-writes-frontier` (the first `/hi` of
  the next session); Slice 3b (269); two open ideas for the next Plan Mode, no Case yet (Next
  session below).
- Three units in the walk. `raw/2026-09-20/0958`: 33 lines, 32 entries (line 26, the reading
  of `estimate-prespec-catches-bare-wikilinks`, folded into its `create`) — decisions: 12
  pages created (264.1, 264.2, 265, 265.1, 265.2, 265.3, 265.4, 266, 267, 268.1, 268.2,
  269); rules: 6 updated (`rule-prespec`, `rule-case-protocol`, `rule-brief`,
  `rule-skill-hi`, `rule-carry-over`, `rule-git-context`), 2 deferred (`rule-work-mode`,
  `rule-subagent-guppi` by 269); estimates: 1 created (`estimate-prespec-catches-bare-wikilinks`,
  `passed` by the folded line), 11 updated by 12 `update` entries (`estimate-generate-renames`,
  `estimate-hi-writes-frontier` twice — 265 then 268.2, the second the final Criterion and
  `method`, `estimate-generate-writes`, `estimate-generate-walks-dates`,
  `estimate-event-log-records`, `estimate-retro-commit-gates`, `estimate-plan-mode-verified`,
  `estimate-documentation-completes`, `estimate-materialize-assembles`,
  `estimate-case-protocol-case-form`, `estimate-brief-written`), 6 reading lines applied on 6
  pages (lines 25, 27–31, all `passed`); lessons: 3 created (`new`); 2 Rule-class files
  (`case-schema`, `glossary`) marked applied by hand. 37 pages written or changed.
  `raw/2026-09-20/0740`: 1 new entry (line 17, the reading of `estimate-generate-renames`,
  `passed`), 2 pages changed. `raw/2026-09-20/0527`: 0 new entries. Cleanup moved 0 pages.
- The order the handoff named held: line 17 of 0740 set `estimate-generate-renames`
  `pending → passed` before 264.1 applied its update with `passed` and the Criterion of 262;
  268.2 applied after 265 on `estimate-hi-writes-frontier`. Every `replace` of 264.2, 267,
  268.1, 268.2 applied; no entry marked `failed` or `incomplete`.
- Statuses computed by `generate`: `rule-prespec` `draft → built` (both Estimates `passed`);
  `rule-page-generation` `draft → built` (`estimate-generate-renames` `passed`); `rule-brief`,
  `rule-documentation`, `rule-skill-hi` `built → draft` (one Estimate each `pending`);
  `rule-case-protocol` stays `built` (`case-form` read and `passed`); `rule-event-log`,
  `rule-retro-commit`, `rule-plan-mode`, `rule-materialize` stay `built` — the update set the
  Estimate `pending` and the reading of the same session passed it in one run.
  `deferred_by` of `rule-work-mode` and `rule-subagent-guppi` now ends at
  `decision-case-269`.
- `guppi render` wrote `.claude/skills/pre-spec/SKILL.md`, `CLAUDE.md`,
  `.claude/agents/librarian-guppi.md`, `.claude/skills/carry/SKILL.md`,
  `.claude/skills/hi/SKILL.md` — the five the handoff named, no other. `guppi sprint`
  rewrote `vault/wiki/sprint.md`: Slice 3b current, both items `draft`, their defers ending
  at 269.
- The check of Spec line 191 of 0958, as read after `generate`: `unmigrated: 25`; the words
  `pre-task` and `pretask` stand on six of the seven pages of 265 only in History lines
  ("the word moved …", "ref `rule-pretask` → …") and in the Result of 2026-09-17 on
  `estimate-generate-walks-dates`; none in a Criterion or a `method`.
- Tests: 443 green (`make test`), style clean at `ad57dc0`.

## Readings due

- `estimate-documentation-completes` — `rule-documentation` stands `draft` — read at line 308
  of `raw/2026-09-20/0958/spec.md`: `make test-documentation`; live — the librarian's run of
  this session, read in the next. This run is that reading's object.
- `estimate-brief-written` — `rule-brief` stands `draft` — read at line 488 of the 0958 Spec:
  the brief after the librarian's run of this session, by hand — in the next session. This
  brief is that reading's object.
- `estimate-hi-writes-frontier` — `rule-skill-hi` stands `draft` — read at line 544 of the
  0958 Spec: the first `/hi` of the next session, by hand.
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` — by its `method`:
  `make lint` exit 0, or only unread lines on the sprint page's own Estimates, at the close
  of the sprint.
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` — by its `method`:
  one reading of the tree by hand at the close of the sprint.
- `estimate-sprint-migration-merges` — `entity-sprint-migration` — by its `method`:
  `make test` on the last commit of `migration`, then `git log` of `main` after the merge.

No Estimate stands `failed`.

## Deferred

Nothing stands in the list.

Left out, the sprint page names them (case 229.4): `rule-work-mode` and
`rule-subagent-guppi` (defer 269 this walk, the eleventh; 183, 206, 218, 231, 242, 248,
252, 254, 260, 263 before — Slice 3b, the current milestone);
`insight-workflow-code-live-before-the-page-it-reads` (`open`, severity 2, defer 238; in the
text of the `rule-work-mode` item); `rule-git-context`, `rule-github-issues` (defers 220,
243; Slice 5, in the text of the `estimate-sprint-migration-merges` item); `rule-spec-box`
(defers 207, 219, 232; Slice 5); `rule-morph` (defer 239; Slice 5).

## Flags

- Index check, `near`: `lesson-spec-change-text-quotes-a-wikilink-bare` is marked
  `near: lesson-spec-change-line-with-a-colon-breaks-the-then-block` in the 0958 yaml — both
  are a form error in the `change` string of a `then` item that a check finds; the causes
  differ (a bare wikilink lint reads as a ref against a YAML scalar ended by a colon). Not
  the same page; both stand.
- Lint, new this run: `lessons/lesson-spec-change-text-quotes-a-wikilink-bare: ref: body
  names decision-case-N, which no live or archived page carries`. The lesson's Trigger quotes
  the History line of 262 — `"the two placeholders [[decision-case-N]] of the Criterion in
  code spans"` — in double quotes, not a code span, as the ledger line wrote it; the page
  written from that line carries the bare link. Not repaired; a lesson page changes by an
  `update`. The finding on `estimate-generate-renames` of the previous brief is gone (264.1).
- Synthesis, as the handoff asked: `lesson-estimate-update-must-carry-its-criterion-whole`
  was compared with every live lesson and Insight by cause. No live lesson on the Estimate
  recut of 193 or 211 stands in the index; `lesson-plan-mode-contract-change-skips-the-estimates-blocks`
  is the nearest (the Criterion of an Estimate changed through a Case), its cause the agent
  not reading the Estimate page under the block-append before 193, not the mechanism of
  `lift_criterion`; `lesson-ledger-estimate-line-carried-a-count-not-read` shares tags only.
  `lesson-agent-memory-is-not-the-product`: no lesson or Insight on a per-machine memory;
  `insight-session-vault-knowledge-not-loaded` runs the other way (a vault fact not reaching
  the session). `lesson-spec-change-text-quotes-a-wikilink-bare`: the `near` above; the
  earlier cases it names (130.1, 140, 160) have no live lesson in the index. No cluster;
  the three lessons stay `new`.
- Spec boxes unticked after this run, each with its reading `passed` and applied: 0958
  line 249 (`estimate-retro-commit-gates`, ledger line 30), line 432
  (`estimate-case-protocol-case-form`, line 31); 0740 line 172
  (`estimate-prespec-reconciles`, read in 0958, line 25). Line 191 of 0958, the `make lint`
  after the librarian, unticked: its facts stand in Where things stand. Work Mode ticks a
  reading; the librarian does not.
- `estimate-plan-mode-verified` `passed` with its Result naming what was not exercised: the
  one `create` of the session carries a `ref`, so the flag part of the Criterion — a
  `create` without a `ref` and its vault query — was not read live.
- `estimate-prespec-hook-gates`'s live part, the approval of a plan through the rendered
  `/pre-spec`, happened this session (the Result of `estimate-plan-mode-verified`: ExitPlanMode
  let through after the `prespec` mark of 12:23:17); no line of its own was written for it,
  the page stands `passed` on pytest from 0740.
- Two `exists` marks on the defers of 269 (expected: a `defer` with a `ref`). No entry
  marked `incomplete`, `failed` or `unparsed` in the three yamls; no failed Estimate; no MOC
  candidate.
- Standing: the defer of 238 on `insight-workflow-code-live-before-the-page-it-reads`
  without a `purpose`; `estimate-hi-no-read-calls` in the shape before case 193 by choice;
  `rule-spec-box` placeholder findings (`kind`, `estimates`, orphan). `materialize` on the
  archived yamls of 2026-09-18/1252 and 2253: not printed this run, the walk named 0527,
  0740 and 0958 only.
- Stale defers by lint: `rule-work-mode` and `rule-subagent-guppi` 23 times since case 29;
  `rule-morph` 1 time since case 239.
- Lint, 76 findings: 2 `rules/rule-spec-box` schema (`kind`, `estimates`) and 1 orphan;
  62 `decisions/decision-case-<1–28>` missing `## Context` and `## Problem` (31 pages,
  Slice 5); 1 `ref` on `lesson-spec-change-text-quotes-a-wikilink-bare` (above); 3 deferred
  (`rule-morph` 1, `rule-subagent-guppi` 23, `rule-work-mode` 23); 6 unread pending (the
  Readings due); `estimates: unmigrated: 25 pages in the shape before case 193`.

## Next session

Cases

- Slice 3b — `rule-work-mode`, `rule-subagent-guppi` (defer 269, "the first item of the next
  session"), with the sentence of `insight-workflow-code-live-before-the-page-it-reads`
  written into `rule-work-mode`; from the handoff and the sprint page.
- A `replace` inside an Estimate's Criterion signed as the pair alone, without the whole
  Criterion — from the handoff's open ideas and
  `lesson-estimate-update-must-carry-its-criterion-whole`.
- A line in `rule-claude-md` that the agent writes no local memory — from the handoff's open
  ideas and `lesson-agent-memory-is-not-the-product`.
- The lint `ref` finding on `lesson-spec-change-text-quotes-a-wikilink-bare`: the bare
  `[[decision-case-N]]` in its Trigger — from `make lint` of this run; the page changes by an
  `update` of the lesson or stays a finding.

Work

- Read `estimate-documentation-completes`: `make test-documentation`; live — this run
  (Spec 0958 line 308).
- Read `estimate-brief-written`: this brief, by hand (Spec 0958 line 488).
- Read `estimate-hi-writes-frontier`: the first `/hi` of the next session, by hand (Spec 0958
  line 544).
- Read `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-leftovers-gone`,
  `estimate-sprint-migration-merges` — at the close of the sprint, by their `method`.
- Tick the boxes whose readings passed: 0958 lines 249, 432; 0740 line 172; and 0958
  line 191 once its check is taken as read (the facts above).
- No ledger line of the walk left unapplied; the tree is clean after the commit of this run.

## Readings at the close

- `make test`: 443 passed.
- `make lint`: 76 findings, exit 1 (the list above).
- Pages: entities 2, rules 44, estimates 69, lessons 38, insights 14, decisions 370.
