# Brief — 2026-09-20, after session 0740 of 2026-09-20 (the rename `pretask → prespec` by Case 261, the placeholder of `estimate-generate-renames` by 262, Slice 3b deferred to 263)

Written by the librarian from `raw/2026-09-20/0740/handoff.md`, the yamls of
`raw/2026-09-20/0740` and `raw/2026-09-20/0527`, and the Greps of the indexes.

## Where things stand

- Code, commit `738e3ef` on `migration`: `guppi/pretask.py` → `guppi/prespec.py`,
  `tests/test_pretask.py` → `tests/test_prespec.py` by `git mv`; the word swapped in
  `guppi/cli.py`, `guppi/gate.py` (`MARKS = {"pre-spec": "prespec", …}`, the mark
  `prespec`), `guppi/pages.py`, `tests/test_gate.py`, `tests/test_ledger.py`, `Makefile`;
  the stderr prefix `prespec:`. By hand: `index.md`, `case-schema.md`, `glossary.md`; the
  word migrated in `rule-skill-hi`, `rule-case-protocol`, `rule-ask`, `rule-hook-registry`,
  `rule-event-log`, `rule-ledger-write`, `rule-retro-commit`, `entity-sprint-migration`;
  `guppi render` in the session rewrote `CLAUDE.md`, `.claude/agents/ask-guppi.md`,
  `.claude/skills/hi/SKILL.md`, `.claude/settings.json`; `.claude/skills/pre-task/` removed.
  434 tests green, style clean.
- Closed in the session: Case 261 (8 update lines, `{supersedes:case 259}`), Case 262
  (1 update), Case 263 (2 defer). Readings passed: `estimate-spec-capture-offers-the-fork`
  (the fork arrived as `PostToolUse` `additionalContext` at 08:55:25, the first time in four
  sessions), `estimate-prespec-checks-the-plan` (52 green in `tests/test_prespec.py`; the
  line of 09:10:20 said 72, the line of 09:26:38 corrects it and is the one applied),
  `estimate-prespec-hook-gates` (pytest; the live part is the approval of the next plan).
- Spec 0740: 17 lines ticked — 11 in the session, the five page updates of 261 and the
  update of 262 by this run; unticked: the read of `estimate-prespec-reconciles` (line 172,
  next session) and the read of `estimate-generate-renames` (line 224; below). Spec 0527:
  line 160, the same reading, unticked.
- Not done: the live part of `estimate-prespec-hook-gates`; `estimate-prespec-reconciles`;
  Slice 3b (defer 263, the tenth); the seven Estimates whose Criteria and `method` keep the
  old word until their next `update` — `estimate-hi-writes-frontier`,
  `estimate-event-log-records`, `estimate-retro-commit-gates`, `estimate-plan-mode-verified`,
  `estimate-generate-writes`, `estimate-generate-walks-dates`,
  `estimate-documentation-completes` — debt by 261.
- Two units in the walk. `raw/2026-09-20/0740`: 16 entries — 3 Decision pages created
  (261, 262, 263); rules: 2 updated with `rename` (`rule-pretask` → `rule-prespec`,
  `rule-pretask-hook` → `rule-prespec-hook`), 2 deferred (`rule-work-mode`,
  `rule-subagent-guppi` by 263); estimates: 4 updated (`estimate-pretask-reconciles` →
  `estimate-prespec-reconciles`, `estimate-pretask-checks-the-plan` →
  `estimate-prespec-checks-the-plan`, `estimate-pretask-hook-gates` →
  `estimate-prespec-hook-gates`, each `pending` with a written Criterion;
  `estimate-generate-renames`, the placeholders in code spans), 4 reading lines applied on 3
  pages (`estimate-spec-capture-offers-the-fork`, `estimate-prespec-checks-the-plan` twice,
  `estimate-prespec-hook-gates` — all `passed`); lessons: 1 created
  (`lesson-ledger-estimate-line-carried-a-count-not-read`, `new`); 3 Rule-class files
  (`index`, `case-schema`, `glossary`) marked applied by hand. 95 pages written or changed:
  the rename walk rewrote every live page with a link to one of the five old slugs, Decision
  pages included. `raw/2026-09-20/0527`: 0 new entries; its two defers of 259 marked
  `superseded_by: 261`. Cleanup moved 1 page: `decision-case-259` (superseded) to
  `archive/migration/2026-09-20/0740/decisions/`.
- The rename, as read after `generate`: the five files exist under the new slugs and none
  under the old; `children` of `rule-plan-mode`, `estimates` of the two rules, `target` of
  the three Estimates and every wikilink in live pages (32 Decision pages among them) name
  the new slugs — zero `[[rule-pretask…]]` or `[[estimate-pretask…]]` left in `wiki/`;
  `origin` of each page keeps the old ledger anchor; History keeps the old word in its
  earlier lines and gained `renamed from` and `ref old → new` lines under
  `[[decision-case-261]]`; the Result of `estimate-prespec-checks-the-plan` is the 52 line;
  `deferred_by: decision-case-259` left both rules through the `supersedes` on line 1 of
  261, and 259 is archived. `guppi render` wrote `.claude/skills/pre-spec/SKILL.md`; no other
  harness file differed.
- Statuses computed by `generate`: `rule-prespec` `built` → `draft`
  (`estimate-prespec-reconciles` `pending`); `rule-spec-capture` `draft` → `built` (its
  reading passed); `rule-prespec-hook` stays `built`; `rule-page-generation` stays `draft`
  (`estimate-generate-renames` `pending`). `deferred_by` of `rule-work-mode` and
  `rule-subagent-guppi` now ends at `decision-case-263`.
- `vault/wiki/sprint.md` rewritten by `guppi sprint`: Slice 3b current, both items `draft`
  with defers to 263.
- Tests: 434 green (`make test`), style clean at `738e3ef`.

## Readings due

- `estimate-generate-renames` — `rule-page-generation` stands `draft` — read at line 224 of
  `raw/2026-09-20/0740/spec.md` (and line 160 of the 0527 Spec): the librarian's run on
  Case 261. The run is done and every check of the Criterion held (the paragraph on the
  rename above). The `estimate[estimate-generate-renames][passed]` line is the main agent's
  to write; the librarian returned it in its report. The page stands `pending` until that
  line is applied.
- `estimate-prespec-reconciles` — `rule-prespec` stands `draft` — read at line 172 of the
  0740 Spec: the first `/pre-spec` after the render, one reading by hand written into the
  estimate line — the next session.
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

Left the list: `rule-pretask` and `rule-pretask-hook` — the defer of 259 retired by the
`supersedes` on line 1 of Case 261; the pages are `rule-prespec` and `rule-prespec-hook`.

Left out, the sprint page names them (case 229.4): `rule-work-mode` and
`rule-subagent-guppi` (defer 263 this walk, the tenth; 183, 206, 218, 231, 242, 248, 252,
254, 260 before — Slice 3b, the current milestone);
`insight-workflow-code-live-before-the-page-it-reads` (`open`, severity 2, defer 238; in the
text of the `rule-work-mode` item); `rule-git-context`, `rule-github-issues` (defers 220,
243; Slice 5, in the text of the `estimate-sprint-migration-merges` item); `rule-spec-box`
(defers 207, 219, 232; Slice 5); `rule-morph` (defer 239; Slice 5).

## Flags

- Handoff flag, a Case of the next Plan Mode: Slice 3b — `rule-work-mode`,
  `rule-subagent-guppi` (defer 263, "the first item of the next session"), with the sentence
  of `insight-workflow-code-live-before-the-page-it-reads` written into `rule-work-mode`.
- The handoff asked the librarian to write the `estimate[estimate-generate-renames]` line.
  A ledger line is the main agent's (a subagent returns a measurement); the librarian did
  not write it and returned the reading in its report: every check passed. Until the line
  is written and applied the Estimate stands `pending` and lint names it `unread`.
- Synthesis: `lesson-ledger-estimate-line-carried-a-count-not-read` was compared with
  `insight-ledger-line-written-unchecked`, as the handoff asked. The Insight is `actioned`
  (case 135, `addressed_by: [[decision-case-135]]`), not `open` as the handoff says; its
  pattern is a line that does not parse or does not match the Spec — a form checked by
  `prespec --check` since 75.2. The new lesson's line parsed and matched; its count was
  composed from memory after one combined pytest run. Not the same cause; not clustered;
  the lesson stays `new`. No live lesson shares the cause.
- Lint, standing after 262: `estimates/estimate-generate-renames: ref: body names
  decision-case-N, which no live or archived page carries`. The two placeholders of the
  Criterion are in code spans now (lines 26–27 of the page) and lint reads no link there;
  the finding comes from the History line of 262 itself, written from the ratified `change`
  text "the two placeholders [[decision-case-N]] of the Criterion in code spans…" — a bare
  wikilink in History, which lint counts as a ref. Not repaired.
- The reading of `estimate-prespec-checks-the-plan` at 09:10:20 carried "72 green in the
  file"; the true count is 52. The lesson above and the second estimate line at 09:26:38
  stand for it; `generate` applied both lines in order and the Result is the 52 line.
- Two readings cannot close this session and stand `pending` after this run:
  `estimate-prespec-reconciles` (the first `/pre-spec`, next session) and
  `estimate-generate-renames` (its line, above). The live part of
  `estimate-prespec-hook-gates` — the approval of the next plan through the rendered
  `/pre-spec` — is not an Estimate status; the page is `passed` on pytest.
- The word "pre-task" stands in live pages where it names the query before a Case (the
  `tags` rows of the schemas, `index.md`, `case-schema.md`, `rule-brief`, `entities/schema.md`,
  `decisions/schema.md`, `rule-index-check`, line 41 of `entity-sprint-migration`); by the
  Case, not a miss. The Criteria and `method` of seven Estimates keep the old word (the
  "Not done" item above); debt by 261.
- `make lint` no longer names `.claude/skills/pre-task/SKILL.md`; the render finding of the
  previous session is gone.
- `materialize`, standing: `raw/2026-09-18/1252/materialize.yaml` — "line 8 changed since
  the yaml was written; entry left alone"; `raw/2026-09-18/2253/materialize.yaml` — "line 3
  changed since the yaml was written; entry left alone". Neither was printed this run: the
  walk named 0527 and 0740 only.
- Standing: the defer of 238 on `insight-workflow-code-live-before-the-page-it-reads`
  without a `purpose`; `estimate-hi-no-read-calls` in the shape before case 193 by choice;
  `rule-spec-box` placeholder findings (`kind`, `estimates`, orphan).
- Stale defers by lint: `rule-work-mode` and `rule-subagent-guppi` 22 times since case 29;
  `rule-morph` 1 time since case 239.
- No entry marked `incomplete`, `failed`, `near` or `unparsed` in either yaml; no failed
  Estimate; no MOC candidate; two `exists` marks on the defers of 263 (expected: a `defer`
  with a `ref`).
- Lint, 75 findings: 2 `rules/rule-spec-box` schema (`kind`, `estimates`) and 1 orphan;
  62 `decisions/decision-case-<1–28>` missing `## Context` and `## Problem` (31 pages,
  Slice 5); 1 `ref` on `estimate-generate-renames` (above); 3 deferred (`rule-morph` 1,
  `rule-subagent-guppi` 22, `rule-work-mode` 22); 5 unread pending (the Readings due);
  `estimates: unmigrated: 29 pages in the shape before case 193`.

## Readings at the close

- `make test`: 434 passed.
- `make lint`: 75 findings, exit 1 (the list above).
- Pages: entities 2, rules 44, estimates 68, lessons 35, insights 14, decisions 358.
