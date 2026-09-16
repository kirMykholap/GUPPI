# Handoff — 2026-09-16, session 2238: the sprint as a page, the recut rule, the session bound by its stamp

## Notes from memory

- The person asked for the plain meaning under the Case form three times — on the sprint
  page (why a page and a render, not the librarian's hand), on the recut (why `set.method`
  and a refusal), on the lift by the schema (why an allow-list beats a skip list) — and on
  the `pretask --check` refusal of a ref to a page the same plan creates. Each answer stands
  in the chat only; the Cases carry the decisions.
- Slice 3b was put aside at the start ("not today, with this many items"); the sprint page
  (209) came out of the F7 hand edit of `sprint.md` — the person named the pattern, that
  closing a Frontier item never reaches the sprint, and asked for a system.
- Case 209 was ratified with a position promise for `rule-sprint` among `children`
  ("after `rule-raw-archive`") that `generate` does not give; case 222 dropped the line.
  `rule-sprint` lands wherever the `ref` puts it.
- Case 216 ticked the 21 open task lines of the 1955 Spec by hand; case 217 defers the
  general answer — `generate` ticks the page lines of a Spec — to Slice 3b. So this Spec's
  page lines (35 unticked) stay open after this run too; the next Retro counts them by
  the same rule and should not read them as debt.
- The ledger lines of case 222 were lost once: the reply carried the `LEDGER` block and
  then a tool call; they were written again the next turn, with an `error` lesson
  (`lesson-ledger-block-followed-by-a-tool-call`). Expect that lesson alone; no cluster.
- `estimate-case-protocol-loaded` was read `passed` again on this session's first turn,
  which stated the two rules; the person accepted the 1955 reading and this one.

## Direct instructions to the librarian

- Unit `raw/2026-09-16/2238`: 42 decision lines (Cases 209–222, defers 217–220, 223 from
  Retro), 12 estimate lines, 1 lesson line. `materialize` has new code: fields are lifted
  by the category's `schema.yaml`, a stray key is marked `unknown` and never reaches a
  page (214.1); `--show` over the four units of the date printed no `unknown` in Work
  Mode. A `ref` on a rule's item goes to the entry, not to `fields`.
- `generate` has new code: an Estimate `update` whose `set` carries `method` drops
  `## Context` and `## Method`; an `update` with `sections.Criterion` on a page without a
  `method` field and no `set.method` fails alone as `a recut without method (case 211)`.
  Every recut of this Spec carries `set.method` — 209.5, 209.6, 211.1, 213.2, 215 — after
  the corrections of case 222; 211.3 sets `method` on five pages (one of them
  `estimate-generate-writes`, a second update after 211.1 in ledger order — two History
  lines, expected). `estimate-pretask-checks-the-plan` gets two Criterion replacements,
  213.1 then 221; the later contains the earlier, and the page ends with 221's text.
  `estimate-documentation-completes` (209.5) keeps its `### case` blocks by the Case's
  word — a page with a `method` field and the old blocks, counted by `unmigrated`.
- Creates: `rule-sprint` (`ref: rule-documentation`, `enforcement: check`, `governs:
  vault/wiki/sprint.md` — `governs` on a `check` rule is new, `rules/schema.md` says so
  since 209.7; `rules/schema.yaml` already lists it optional), `entity-sprint-migration`
  (an Entity MOC with three sections, the first live page under `entities/`), four
  Estimates under them. New tag `sprint` under `new_tags` of Case 209.
- The frame of `rule-documentation` gains step 5, `uv run guppi sprint`, after `render` and
  before the brief (209.5). Run it in this very run once `generate` and `render` are done:
  it needs `entity-sprint-migration` live, reads every item's status and writes
  `vault/wiki/sprint.md` whole — the first render, the task line of 209.2. Every line on
  its stderr is a flag; if it fails, `sprint.md` stays the hand-written text under the
  guard of `rule-sprint`, and that is a flag for the next Plan Mode, not a hand edit.
- `rule-brief` loses the sentence on editing `sprint.md` (209.6): a handoff flag that asks
  for a sprint change goes into Flags as a Case. `sprint.md` is not yours any more.
- Renders after `generate`: `.claude/agents/librarian-guppi.md` (209.5),
  `.claude/skills/pre-task/SKILL.md` (213.3 — the command line takes `--session <stamp>`);
  `render --check` exit 0 at the close.
- Supersedes: case 222 carries two lines on
  `insight-ledger-hi-tied-to-its-session-by-position`, `{supersedes:case 205}` and
  `{supersedes:case 192}` — one item under Case 222 with `change` only; both lines find
  it; `decision-case-192` and `decision-case-205` become `superseded` and archived, the
  Insight loses its `deferred_by` and is `actioned` by 213.4 (`addressed_by:
  decision-case-213.1`); its four lessons archive by the cascade.
  `insight-materialize-lift-loses-a-schema-field` is `actioned` by 214.2; its three
  lessons archive.
- Index check: `rule-sprint` against the rules Grep — nothing near; `entity-sprint-migration`
  is the only entity. Synthesis: one lesson (`lesson-ledger-block-followed-by-a-tool-call`,
  `error`) against the lesson and insight lines; I expect no shared root cause.
- Readings due after this run, for the brief: `estimate-sprint-renders-the-backlog` (its
  pytest half is green, 5 tests; the live half is the `sprint.md` you write in this run —
  name the result in the brief, the reading is the next session's line),
  `estimate-documentation-completes` (this run, with step 5), `estimate-brief-written`
  (the brief you write, without a sprint edit), `estimate-pretask-reconciles` (the next
  `/pre-task` with `--session`), `estimate-carry-over-writes` (a live `/carry`, none yet),
  and the three Estimates of `entity-sprint-migration` (the close of the sprint;
  `-lint-clean` passes only with the `unread` of its siblings as the sole findings).
- `make lint` at the close: expect the 62 of Cases 1–28, `unmigrated: 34`, `unread` on
  the pending pages above, `rule-spec-box` (3), the two `deferred` (now 15 times), and
  `rule-carry-over` unchanged (its stray `ref` is defer 223, next Plan Mode). The `ref:
  body names slug` finding on `estimate-lint-catches` leaves with its new Result. The
  `method` finding on `estimate-plan-mode-names-its-estimates` left in Work Mode.
- Flags for the brief, each a Case of the next Plan Mode: (1) `rule-carry-over` stray `ref`
  (223); (2) `generate` ticking the page lines of a Spec (217, with 3b); (3) whether
  `sprint.md` should also be checked at `SessionStart` like `render --sync` — not in 209,
  the person did not ask; (4) the 35 unticked page lines of this Spec.

## What actually got done

- Cases 209–216, 221, 222 ratified and built where Work Mode could: `guppi/sprint.py` (new,
  `guppi sprint` in `cli.py`, `tests/test_sprint.py`), `guppi/generate.py` (211.1, 211.2),
  `guppi/lint.py` (212), `guppi/pretask.py` (213.1, 213.2, 221), `guppi/materialize.py`
  (214.1); tests 396 → 411, all green; `make style` clean; `render --check` 0. Commit
  `a4c3509` on `migration`.
- One-off: the stray `ref` field removed from 15 Estimate pages by a script, History line
  with the pointer `raw/2026-09-16/2238/spec.md#case-210` (210); the 21 open task lines of
  `raw/2026-09-16/1955/spec.md` ticked (216).
- Rule-class by hand: `index.md` §1 (`sprint.md` a render) and §7 (the recut), `glossary.md`
  (the Sprint row), `case-schema.md` (`set.method` on a recut), `rules/schema.md`
  (`governs` on a `check` rule), `estimates/schema.md` and `schema.yaml` (the sections
  dropped by the update that sets `method`).
- Readings in the ledger: `-materialize-marks-superseded`, `-end-of-work-order`,
  `-brief-written` (the 1955 brief), `-case-protocol-loaded`, `-permissions`,
  `-generate-writes`, `-generate-fails-alone`, `-lint-catches`,
  `-pretask-checks-the-plan`, `-pretask-hook-gates`, `-materialize-assembles` — all
  `passed`. `estimate-carry-over-writes` stays `pending` (no live `/carry`).
- Deferred: 217 (`rule-page-generation`, the ticks), 218 (`rule-work-mode`,
  `rule-subagent-guppi`, Slice 3b), 219 (`rule-spec-box`), 220 (`rule-git-context`,
  `rule-github-issues`, the close of the sprint), 223 (`rule-carry-over`).
- Not done: every page create and update (this run); the three renders (this run); the
  first `guppi sprint` (this run, step 5); the readings listed above; `rule-carry-over`.
- `sprint.md` was not edited by hand this session: F7 dissolved into the first render.
