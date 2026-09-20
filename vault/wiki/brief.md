# Brief — 2026-09-20, after session 0527 of 2026-09-20 (the fork of `guppi spec` as `additionalContext`, `--session` is the session id, `update` with `rename` in materialize and generate; the rename to `prespec` deferred to 259, Slice 3b to 260)

Written by the librarian from `raw/2026-09-20/0527/handoff.md`, the yamls of
`raw/2026-09-20/0527` and `raw/2026-09-18/2253`, and the Greps of the indexes.

## Where things stand

- Code, commit `8252674` on `migration`: `guppi/spec.py` — the fork printed as JSON
  `hookSpecificOutput.additionalContext` (255), three tests parse it; `guppi/materialize.py`
  — `rename` carried into an update entry, named in the docstring (258.2), one test;
  `guppi/generate.py` — `Vault.rename`, `reword`, `retarget`: the move, History
  `renamed from`, the walk of every live page with `ref old → new` History lines (Decision
  pages retargeted without one), the refusal on a taken (live or archived) or foreign slug,
  an archived page refused (258.1), four tests. By hand: `index.md` §3 and §5,
  `case-schema.md`, `decisions/schema.md`, `glossary.md`. 434 tests green, style clean.
- Spec 0527: 13 lines ticked in the session — code, tests, four files, three readings;
  this run ticked the 12 page lines and the `render` line. Two `read` lines stay unticked
  (below). Spec 2054: its four `read` lines ticked in the session; nothing unticked.
- Readings in the session: `estimate-case-protocol-loaded`, `estimate-materialize-assembles`,
  `estimate-pretask-reconciles`, `estimate-retro-loads` — all `passed`. The reading of
  `estimate-pretask-reconciles` ran on the old skill text and followed the new Criterion
  (`--session 8ce3afdd`, the first line of the output read); the person counted it.
- Not done: Case 257 — the rename `pretask → prespec` in every form (skill, pages, module,
  command, mark, tests, the word in Renders and live pages) — deferred by 259, first next
  session; Slice 3b — defer 260, the ninth; the live parts of two readings (below); F4 to
  Slice 5.
- Two units materialized. `raw/2026-09-20/0527`: 23 entries — 7 Decision pages created
  (255, 256, 258.1, 258.2, 258.3, 259, 260); rules: 4 updated (`rule-spec-capture`,
  `rule-pretask`, `rule-page-generation`, `rule-materialize`), 4 deferred (`rule-pretask`,
  `rule-pretask-hook` by 259; `rule-work-mode`, `rule-subagent-guppi` by 260); estimates:
  1 created (`estimate-generate-renames`, `pending`), 3 updated
  (`estimate-spec-capture-offers-the-fork` to `pending`; `estimate-pretask-reconciles` and
  `estimate-materialize-assembles` to `pending`, then `passed` by their readings later in the
  ledger), 4 readings applied (`passed`); lessons: 2 created
  (`lesson-hooks-posttooluse-stdout-not-in-context`,
  `lesson-spec-change-line-with-a-colon-breaks-the-then-block`), both `new`; insights: 1
  updated (`insight-pretask-session-flag-takes-the-id-not-the-hi-line`, `actioned`,
  `addressed_by: [[decision-case-256]]`); 4 Rule-class files (`index`, `case-schema`,
  `decisions-schema`, `glossary`) marked applied by hand by `generate`. 27 pages written or
  changed. `raw/2026-09-18/2253`: 2 entries new since the last run — the readings of
  `estimate-sprint-ticks-the-spec` and `estimate-render-harness-ticks-the-spec` (`passed`);
  4 pages changed. Cleanup moved 2 pages: the two lessons of the actioned Insight, to
  `archive/migration/2026-09-20/0527/lessons/`.
- Statuses computed by `generate`: `rule-sprint`, `rule-render-harness`, `rule-case-protocol`,
  `rule-retro` `draft` → `built` (their readings passed); `rule-spec-capture` and
  `rule-page-generation` `built` → `draft` (one Estimate of each `pending`); `rule-pretask`
  and `rule-materialize` stay `built` (set `pending`, then `passed` in the same unit).
  `deferred_by` of `rule-pretask` and `rule-pretask-hook` is `decision-case-259`; of
  `rule-work-mode` and `rule-subagent-guppi` now ends at `decision-case-260`.
- Rendered: `.claude/skills/pre-task/SKILL.md` (256, one line: the eight-character session
  id as `--session`, the first line of the output read). `CLAUDE.md` unchanged
  (`rule-case-protocol` was not touched). `vault/wiki/sprint.md` rewritten by `guppi sprint`:
  Slice 3b current, both items `draft` with defers to 260.
- Tests: 434 green (`make test`), style clean at `8252674`.

## Readings due

- `estimate-spec-capture-offers-the-fork` — `rule-spec-capture` stands `draft` — read at
  line 46 of `raw/2026-09-20/0527/spec.md`: pytest and the `ExitPlanMode` result of a
  session after the change. Pytest is green; every `ExitPlanMode` of session 0527 ran the
  old code, so the live part is the first `ExitPlanMode` of the next session.
- `estimate-generate-renames` — `rule-page-generation` stands `draft` — read at line 160 of
  the 0527 Spec: pytest, and the librarian's run on the first real rename. Pytest is green;
  the first real rename is Case 259, next session; no entry of this unit carried `rename`.
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` — by its `method`:
  `make lint` exit 0, or only unread lines on the sprint page's own Estimates, at the close
  of the sprint.
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` — by its `method`:
  one reading of the tree by hand at the close of the sprint.
- `estimate-sprint-migration-merges` — `entity-sprint-migration` — by its `method`:
  `make test` on the last commit of `migration`, then `git log` of `main` after the merge.

No Estimate stands `failed`.

## Deferred

1. `rule-pretask` — defer 259, first brief. Purpose of the defer: rename to `rule-prespec`
   by an `update` with `rename` (case 258), with the skill `/pre-spec`, the module
   `guppi/prespec.py`, the command `guppi prespec`, the mark `prespec`, the three Estimates
   and the word in every Render and live page; the first item of the next session, so that
   the mechanism of 258 is used after it is built and tested. The handoff names it first.
2. `rule-pretask-hook` — defer 259, first brief. Purpose of the defer: rename to
   `rule-prespec-hook` in the same Case as `rule-pretask`; the refusal names `/pre-spec`,
   the mark it looks for is `prespec`.

Left the list: `insight-pretask-session-flag-takes-the-id-not-the-hi-line` — `actioned` by
256 (`addressed_by: [[decision-case-256]]`), its two lessons archived by the cascade.

Left out, the sprint page names them (case 229.4): `rule-work-mode` and
`rule-subagent-guppi` (defer 260 this walk; 183, 206, 218, 231, 242, 248, 252, 254 before —
Slice 3b, the current milestone); `insight-workflow-code-live-before-the-page-it-reads`
(`open`, severity 2, defer 238; in the text of the `rule-work-mode` item);
`rule-git-context`, `rule-github-issues` (defers 220, 243; Slice 5, in the text of the
`estimate-sprint-migration-merges` item); `rule-spec-box` (defers 207, 219, 232; Slice 5);
`rule-morph` (defer 239; Slice 5).

## Flags

- Handoff flags, each a Case of the next Plan Mode: Case 257, the rename `pretask →
  prespec` (defer 259, "the first item of the next session"); Slice 3b — `rule-work-mode`,
  `rule-subagent-guppi` (defer 260, after the rename), with the sentence of
  `insight-workflow-code-live-before-the-page-it-reads` written into `rule-work-mode`.
- `near`: `lesson-hooks-posttooluse-stdout-not-in-context` is close to
  `lesson-hooks-messagedisplay-cannot-block` — both are a fact on what a hook event delivers
  to the agent, on different events; not the same cause, no Insight. The second lesson,
  `lesson-spec-change-line-with-a-colon-breaks-the-then-block`, shares its cause with no live
  lesson and no Insight; `insight-ledger-line-written-unchecked` is a different mechanism
  (nothing reads a ledger line back; the `then` block was caught by `pretask --check`); no
  YAML-form lesson stands in the live lesson index. Both lessons stay `new`.
- Lint, new: `estimates/estimate-generate-renames: ref: body names decision-case-N, which no
  live or archived page carries` — the Criterion of 258.1 writes the History line with the
  placeholder `[[decision-case-N]]` literally, twice; ratified text, not repaired.
- Two readings cannot close this session and stand `pending` after this run:
  `estimate-spec-capture-offers-the-fork` (the fork line was absent a third time in 0527,
  on the old code) and `estimate-generate-renames` (the live part is the run on 259).
- The 2253 session wrote its two readings after its retro commit without ticking their
  Spec lines; ticked in 0527 by hand (2054 Spec lines 53, 95, 163, 194) and committed with
  the ledger of 2253. The cause is not known; no lesson.
- `render --sync` at `/hi` of 0527 hit a failed permission check (the classifier
  unavailable); no harness file differed.
- F4 of the Frontier: the failed `git pull` without an upstream and `gh` not logged in in
  `/hi` close as `work` until Slice 5 (the defer of 243 stands).
- The handoff's note on `rename` and History: History is not rewritten by design (258.1);
  lint reads wikilinks in History, `generate` writes History slugs bare; the one non-decision
  wikilink in a live History section is `[[entity-cart]]` in `estimates/schema.md`. A
  hand-written `[[slug]]` in a History section is the one case the rename of 259 would
  leave stale — a known boundary.
- `materialize`, standing: `raw/2026-09-18/1252/materialize.yaml` — "line 8 changed since
  the yaml was written; entry left alone". New this run: "line 3 changed since the yaml was
  written; entry left alone" — the script names no unit; the yaml whose line 3 the last run
  extended with the synthesis entries is `raw/2026-09-18/2253/materialize.yaml`.
- Standing: the defer of 238 on `insight-workflow-code-live-before-the-page-it-reads`
  without a `purpose`; `estimate-hi-no-read-calls` in the shape before case 193 by choice;
  `rule-spec-box` placeholder findings (`kind`, `estimates`, orphan).
- Stale defers by lint: `rule-work-mode` and `rule-subagent-guppi` 21 times since case 29;
  `rule-morph` 1 time since case 239.
- No entry marked `incomplete`, `failed` or `unparsed` in either yaml; one `near` (above);
  no failed Estimate; no MOC candidate; four `exists` marks on the defers of pages already
  on disk (expected: a `defer` with a `ref`).
- Lint, 75 findings: 2 `rules/rule-spec-box` schema (`kind`, `estimates`) and 1 orphan;
  62 `decisions/decision-case-<3–28>` missing `## Context` and `## Problem` (31 pages,
  Slice 5); 1 `ref` on `estimate-generate-renames` (above); 3 deferred (`rule-morph` 1,
  `rule-subagent-guppi` 21, `rule-work-mode` 21); 5 unread pending (the Readings due);
  `estimates: unmigrated: 29 pages in the shape before case 193`.

## Readings at the close

- `make test`: 434 passed.
- `make lint`: 75 findings, exit 1 (the list above).
- Pages: entities 2, rules 44, estimates 68, lessons 34, insights 14, decisions 356.
