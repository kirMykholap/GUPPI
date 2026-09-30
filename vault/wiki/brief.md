# Brief — 2026-09-30, session 2042: Stop hooks on their own error, the librarian's reads, case-guppi's check and record

## Where things stand

- Ratified (handoff): 554, 555.1 to 555.5, 556, 557.1 to 557.3, 558.1 to 558.3, and the defer 560. Cases 554, 555, 557 and 558 were ratified more than once; the ledger holds each line once.
- Code (handoff): `guppi/ratified.py`, `guppi/casecheck.py` and `guppi/onward.py` exit 2 on their own `Stop` error once the payload is read; `guppi/context.py` shows its error as the `systemMessage` and exits 0. Tests: `tests/test_ratified.py`, `tests/test_casecheck.py`, `tests/test_context.py`, `tests/test_onward.py`. `make test` 997 passed, 2 skipped; `make style` clean. The check of 556 (`uv run pytest tests/test_schemas.py -k estimate --collect-only -q`): 6 of 33 tests collected.
- Yaml: `raw/2026-09-30/2042/materialize.yaml` 36 entries and 3 of the synthesis; 35 + 3 applied; ledger line 24 (defer 559 on `rule-case-protocol`) carries `superseded_by: '560'` and was not applied, as the handoff says. 18 decision records, all applied. None `failed` or `incomplete`; 1 `near`; `unparsed` empty. Its ledger has 36 lines, each held by an entry of the yaml. The yamls of `raw/2026-09-30/0138`, `0248`, `1306` and `1736` were extended with 0 entries; `generate` wrote 0 pages from them. `materialize` added `superseded_by: '557.3'` to one entry and `superseded_by: [decision-case-557.3]` to the record of 551 in the 1736 yaml.
- Pages, decisions: 18 created (554, 555, 555.1 to 555.5, 556, 557, 557.1 to 557.3, 558, 558.1 to 558.3, 559, 560); `decision-case-551` superseded by 557.3 and `decision-case-559` superseded by 560, both moved to the archive by `cleanup` (2 pages moved).
- Pages, rules: 13 updates on 11 pages (`rule-spec-write`, `rule-case-check`, `rule-context-size`, `rule-retro-onward`, `rule-case-build` ×3, `rule-case-protocol`, `rule-decisions-schema`, `rule-documentation`, `rule-materialize`, `rule-synthesis`, `rule-brief`); `rule-case-build` lost `deferred_by` 551 (557.3) and left `backlog.md`; `rule-case-protocol` got no `deferred_by` from 559. Cascade built → draft: `rule-brief`, `rule-context-size`, `rule-estimates-schema`, `rule-synthesis`; draft → built: `rule-decisions-schema`, `rule-ledger-write`, `rule-retro-commit`.
- Pages, estimates: 4 created (`estimate-spec-write-exits-2-on-an-error`, `estimate-case-check-exits-2-on-an-error`, `estimate-context-size-shows-its-error`, `estimate-retro-onward-exits-2-on-an-error`); 8 updated and set `pending` (`estimate-estimates-schema-checked` its `method`, 556; the Criterion replaced whole on `estimate-case-build-checks-the-finished-case` 557.1, `estimate-case-build-records-the-rounds-in-recommend` 557.2, `estimate-documentation-completes` 558.1, `estimate-synthesis-clusters` 558.2, `estimate-brief-written` 558.3, `estimate-retro-onward-sends-the-agent-to-the-handoff` 555.4, `estimate-context-size-shown-after-each-reply` 555.5); 1 deferred (`estimate-case-protocol-shows-the-built-case`, `deferred_by` 560); 7 readings `passed` from ledger lines 29 to 35 (`estimate-case-check-sends-back-a-faulty-case`, `estimate-decisions-schema-checked`, `estimate-ledger-write-exits-2-on-an-error`, `estimate-ledger-write-lifts`, `estimate-ledger-write-refuses-a-line-it-cannot-read`, `estimate-retro-commit-gates`, `estimate-retro-loads`).
- Pages, lessons: 2 created (`lesson-prespec-findings-relayed-piecemeal-lose-the-person`, `lesson-prespec-second-run-dispatches-ask-guppi-again`), both updated to `clustered`. Insights: 1 created.
- Synthesis: the two lessons of this run share one cause, the loop after pre-spec findings has no rule; no Insight of that pattern stood, so `insight-prespec-after-findings-loop-unruled` was created with both as children, tags `workflow`, `session`. Neither lesson carries `addressed_by`, so the Insight is `open`.
- Render wrote `.claude/agents/case-guppi.md`, `.claude/agents/librarian-guppi.md`, `vault/wiki/case-schema.md` and `vault/wiki/decisions/schema.yaml`. `backlog.md`: `rule-case-build` removed, `insight-prespec-after-findings-loop-unruled` added. `sprint.md` and `glossary.md` unchanged. The run ticked 33 boxes of `raw/2026-09-30/2042/spec.md`, 3 `read` boxes of `raw/2026-09-30/1736/spec.md` and 1 of `raw/2026-09-30/1306/spec.md`; `log.md` 74 lines added.

## Readings due

3 Estimates are `failed`, 39 `pending` (the `unread` lines of `make lint`).

- `estimate-case-build-writes-a-plain-round` — `rule-case-build` — failed: the sentence on what the round decides runs parallel clauses in one sentence on Cases 548 and 550, and the Context of Case 547 names five examples in one sentence (session 1736); spec 2042: in a later session after the render, one first round and one later round of `case-guppi`
- `estimate-case-protocol-shows-the-built-case` — `rule-case-protocol` — failed: before the first question of each round the main agent wrote a line of its own (session 1736); method: by hand, the Cases of a session at its close against the Agent, SendUserFile, Skill and SendMessage calls of the transcript; `deferred_by` 560
- `estimate-spec-write-writes-a-defer` — `rule-spec-write` — failed: at the first showing of Case 551 the hook raised on a malformed line, caught the error and exited 0, so nothing of 551 was written; method: `uv run pytest tests/test_ratified.py -k defer`, then by hand the first defer the person asks for after the change
- `estimate-ask-finds` — `rule-ask` — method: by hand in a later session, three dispatches of ask-guppi, one existing page asked in English and in Russian, one proposal that crosses a known rule, each read against the event log
- `estimate-brief-written` — `rule-brief` — spec 2042: by hand, the brief of the first librarian run whose agent file holds this Render — this run: the render of this run rewrote `.claude/agents/librarian-guppi.md`; the run itself worked from the frame it was dispatched with, before case 558.3 (handoff)
- `estimate-carry-over-writes` — `rule-carry-over` — method: `uv run guppi render --check`; by hand, the first `/carry` after the fork of ExitPlanMode — the tree, `brief.md`, `carry.md`, `backlog.md` and the commit
- `estimate-case-build-checks-the-finished-case` — `rule-case-build` — spec 2042: in a later session, at `/pre-spec` after the render
- `estimate-case-build-records-the-rounds-in-recommend` — `rule-case-build` — spec 2042: in a later session after the render, the Case files against the rounds in the chat
- `estimate-case-build-writes-the-case` — `rule-case-build` — method: by hand, live dispatches in a session after the render — one item with a fork, one Case with a create without a ref, one that changes a hook
- `estimate-case-check-exits-2-on-an-error` — `rule-case-check` — spec 2042: in a later session; method `uv run pytest tests/test_casecheck.py`
- `estimate-case-check-requires-each-question-of-the-rounds` — `rule-case-check` — method: `pytest tests/test_casecheck.py -k rounds`, then by hand the first Case the hook sends back for a missing title
- `estimate-case-check-shows-only-the-checked-case` — `rule-case-check` — method: `uv run pytest tests/test_casecheck.py -k stop`, then by hand the first reply the hook refuses
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` — method: by hand, the first session where a lesson and the Case that closes its cause stand together, and the first Case that takes up a decision with more than one Case in its `deferred_by`
- `estimate-case-protocol-shows-the-frontier-after-a-closed-line` — `rule-case-protocol` — method: by hand in a later session, the first reply in Plan Mode after a first reply of `/hi` that closes a line of `frontier.md` with no ratification and no defer
- `estimate-compact-recall-reloads` — `rule-compact-recall` — method: `pytest tests/test_recall.py`; live, the first compaction of a working session
- `estimate-context-size-shown-after-each-reply` — `rule-context-size` — spec 2042: in a later session; method `uv run pytest tests/test_context.py`, then the line after the replies in the VS Code chat
- `estimate-context-size-shows-its-error` — `rule-context-size` — spec 2042: in a later session; method `uv run pytest tests/test_context.py`
- `estimate-documentation-completes` — `rule-documentation` — spec 2042: by hand, the first librarian run whose agent file holds this Render: its event log against the Flags of its brief
- `estimate-end-of-work-order` — `rule-end-of-work` — method: `make test-end-of-work`, plus by hand at the close of a later session
- `estimate-estimates-schema-checked` — `rule-estimates-schema` — spec 2042: in a later session, `uv run pytest tests/test_schemas.py -k estimate`, then `make lint`
- `estimate-event-log-records` — `rule-event-log` — method: `pytest tests/test_event.py tests/test_gate.py`; by hand, one `/hi` outside plan mode and one in it
- `estimate-generate-rewords` — `rule-page-generation` — method: `pytest tests/test_generate.py`; the live reading, the librarian's run that applies the first reword — this run: the 2042 yaml holds no entry with `reword` (a Grep of `^\s+reword:` printed 0 lines); `generate` printed `2026-09-30/2042: 56 page(s) written or changed` and no reword line
- `estimate-governed-files-hook-refuses` — `rule-governed-files-hook` — method: `pytest tests/test_guard.py`, plus by hand one Edit of a governed file refused
- `estimate-handoff-dispatches` — `rule-handoff` — method: by hand at the `/handoff` of a later session
- `estimate-handoff-holds-each-fact-once` — `rule-handoff` — method: by hand at the first `/handoff` after the render, against the close of its Retro
- `estimate-plan-mode-verified` — `rule-plan-mode` — method: `make test-plan-mode`; one live reading by hand
- `estimate-python-utf8-output-intact` — `rule-python-utf8` — method: `uv run guppi render --check` and `json.load` of `.claude/settings.json`; by hand at a later session start
- `estimate-retro-onward-exits-2-on-an-error` — `rule-retro-onward` — spec 2042: in a later session; method `uv run pytest tests/test_onward.py`
- `estimate-retro-onward-sends-the-agent-to-the-handoff` — `rule-retro-onward` — spec 2042: in a later session; method `uv run pytest tests/test_onward.py`, then by hand the first run from `/work` to the librarian after the render
- `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — `rule-retro` — method: by hand at the first `/retro` after the render whose `work.md` names a check under Expected red
- `estimate-retro-red-in-the-baseline-is-not-charged` — `rule-retro` — method: by hand at the first `/retro` after the render whose Baseline holds a failing test or a lint finding line
- `estimate-retro-runs-on-to-the-handoff` — `rule-retro` — method: by hand at the first run from `/work` to the librarian after the render
- `estimate-session-phases-in-order` — `rule-session` — method: by hand at the close of a session, the hi line, `frontier.md`, the approved stamp, the Retro commit, `handoff.md`, the librarian's commit
- `estimate-session-start-context` — `rule-session-start` — method: `make test-session-start`; by hand, one session opened without `/hi` whose reply carries a LEDGER block
- `estimate-spec-write-exits-2-on-an-error` — `rule-spec-write` — spec 2042: in a later session; method `uv run pytest tests/test_ratified.py`
- `estimate-spec-write-reaches-the-approved-spec` — `rule-spec-write` — method: `uv run pytest tests/test_ratified.py -k approved_spec`; by hand, the first Case ratified in Work Mode after the change
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` — method: one reading of the tree by hand at the close of the sprint
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` — method: `make lint`, exit 0, or only unread lines on the Estimates of `entity-sprint-migration`
- `estimate-sprint-migration-merges` — `entity-sprint-migration` — method: `make test` on the last commit of migration, then git log of main after the merge
- `estimate-synthesis-clusters` — `rule-synthesis` — spec 2042: by hand, the yaml and the report of the first librarian run after the render whose yaml holds at least two lesson entries — this run: the 2042 yaml holds 2 lesson entries (ledger lines 25 and 36); the Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 71 lines, `^(pattern|deferred_by):` over `vault/wiki/insights/` 28 lines; 3 entries added with `librarian: synthesis` (a `create` of `insight-prespec-after-findings-loop-unruled` with both lessons as `children`, tags `workflow`, `session`, sections `Pattern` and `Proposal`; an `update` of each lesson with `set: {status: clustered, insight: insight-prespec-after-findings-loop-unruled}`), all 3 `applied` by `generate`; no lesson page was opened at synthesis
- `estimate-where-to-stop-stops-only-on-its-conditions` — `rule-where-to-stop` — method: by hand at the first run from `/work` to the librarian after the render
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `rule-work-mode` — method: `uv run guppi render --check`; by hand, the first `/work` the agent calls at the fork and the first `/work` the person types

## Flags

- `near`: `lesson-prespec-findings-relayed-piecemeal-lose-the-person` near `lesson-prespec-report-questions-still-off-the-shape` (both on what the main agent shows the person after `/pre-spec`; one on the order of the showing, the other on the shape of its question).
- `failed`, `incomplete`, `unparsed`: none. The stderr of `cleanup`, `render`, `sprint`, `backlog` and `glossary` was empty; `generate` printed nothing on stderr.
- Not applied: ledger line 24, the defer 559 on `rule-case-protocol`, superseded by 560 (handoff: `rule-case-protocol` gets no `deferred_by` from 559).
- Failed Estimates: `estimate-case-build-writes-a-plain-round`, `estimate-case-protocol-shows-the-built-case`, `estimate-spec-write-writes-a-defer`.
- Stale defers (`make lint`): `rule-subagent-guppi` deferred 31 times since case 29; `rule-orchestration` 2 times since case 424; `rule-complaint-becomes-a-lesson` 1 time since case 504; `rule-morph` 1 time since case 239; `rule-prespec-script-skips-code-spans` 1 time since case 481.
- MOC candidates: none found. Contradictions: none found.
- Handoff observation: the parent `recommend` of Case 558 already carries two items marked not answered, in the form Case 557.2 sets, before 557.2 was rendered.
- Reads beyond this run's frame: a `git status --short` over `vault` that printed paths under `vault/wiki/decisions/` and `vault/archive/`, and a count of `git status` lines under `vault/wiki/decisions/` — to learn what `generate` and `cleanup` wrote; an `ls` count of `vault/wiki/decisions/*.md` — for the page counts. No text of a Decision page or of the archive was read.
- `make lint` (exit 2, 51 finding lines):
  - `rules/rule-spec-box: schema: missing field kind`
  - `rules/rule-spec-box: schema: missing field estimates`
  - `decisions/decision-case-13: fence: ## When: a code fence open at the end of the section:` followed by the opening of a `markdown` fence
  - `rules/rule-spec-box: orphan: no other live page names it in its frontmatter`
  - 5 `deferred` lines (above) and 42 `unread` lines, one per Estimate of Readings due.

## Next session

Cases:
- The orchestration of the main agent after pre-spec findings: how Cases built again, rounds and its own questions reach the person as one list of what to answer; the person asked for this first (handoff, For the next session; `lesson-prespec-findings-relayed-piecemeal-lose-the-person`, `insight-prespec-after-findings-loop-unruled`, `rule-orchestration` in the backlog).
- A second `/pre-spec` run after fixes: whether `ask-guppi` runs again, over the whole plan or only over the Cases built again, and whether the person is told the cost first (handoff, For the next session; `lesson-prespec-second-run-dispatches-ask-guppi-again`).
- `estimate-case-build-writes-a-plain-round` failed; its `read` box of 557.3 is unticked in `raw/2026-09-30/2042/spec.md`, the reading needs a first and a later round of `case-guppi` after the render (handoff, Debt).
- `estimate-case-protocol-shows-the-built-case` failed; `deferred_by` 560.
- `estimate-spec-write-writes-a-defer` failed; read again on the first defer after case 554.
- Lint red that stands: `rule-spec-box` (missing `kind`, missing `estimates`, orphan) and the fence of `decision-case-13` at the end of `## When` (`make lint`).

Work:
- read `estimate-ask-finds`
- read `estimate-brief-written` (box of `raw/2026-09-30/2042/spec.md`)
- read `estimate-carry-over-writes` (box of `raw/2026-09-30/0248/spec.md`)
- read `estimate-case-build-checks-the-finished-case` (box of `raw/2026-09-30/2042/spec.md`)
- read `estimate-case-build-records-the-rounds-in-recommend` (box of `raw/2026-09-30/2042/spec.md`)
- read `estimate-case-build-writes-the-case`
- read `estimate-case-check-exits-2-on-an-error` (box of `raw/2026-09-30/2042/spec.md`)
- read `estimate-case-check-requires-each-question-of-the-rounds` (box of `raw/2026-09-30/1306/spec.md`)
- read `estimate-case-check-shows-only-the-checked-case`
- read `estimate-case-protocol-ledger-line-form`
- read `estimate-case-protocol-shows-the-frontier-after-a-closed-line` (box of `raw/2026-09-30/1736/spec.md`)
- read `estimate-compact-recall-reloads`
- read `estimate-context-size-shown-after-each-reply` (box of `raw/2026-09-30/2042/spec.md`)
- read `estimate-context-size-shows-its-error` (box of `raw/2026-09-30/2042/spec.md`)
- read `estimate-documentation-completes` (box of `raw/2026-09-30/2042/spec.md`)
- read `estimate-end-of-work-order`
- read `estimate-estimates-schema-checked` (box of `raw/2026-09-30/2042/spec.md`)
- read `estimate-event-log-records`
- read `estimate-generate-rewords`
- read `estimate-governed-files-hook-refuses`
- read `estimate-handoff-dispatches`
- read `estimate-handoff-holds-each-fact-once`
- read `estimate-plan-mode-verified`
- read `estimate-python-utf8-output-intact` (box of `raw/2026-09-30/0248/spec.md`)
- read `estimate-retro-onward-exits-2-on-an-error` (box of `raw/2026-09-30/2042/spec.md`)
- read `estimate-retro-onward-sends-the-agent-to-the-handoff` (box of `raw/2026-09-30/2042/spec.md`)
- read `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`
- read `estimate-retro-red-in-the-baseline-is-not-charged`
- read `estimate-retro-runs-on-to-the-handoff`
- read `estimate-session-phases-in-order`
- read `estimate-session-start-context`
- read `estimate-spec-write-exits-2-on-an-error` (box of `raw/2026-09-30/2042/spec.md`)
- read `estimate-spec-write-reaches-the-approved-spec` (box of `raw/2026-09-30/1306/spec.md`)
- read `estimate-sprint-migration-leftovers-gone`
- read `estimate-sprint-migration-lint-clean`
- read `estimate-sprint-migration-merges`
- read `estimate-synthesis-clusters` (box of `raw/2026-09-30/2042/spec.md`)
- read `estimate-where-to-stop-stops-only-on-its-conditions`
- read `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`

Ask the person:
- none

## Readings at the close

- `make test`: 997 passed, 2 skipped.
- `make lint`: exit 2, 51 finding lines — 4 findings (`rule-spec-box` ×3, `decision-case-13` ×1), 5 `deferred`, 42 `unread`.
- Live pages: rules 74, entities 4, estimates 174, lessons 73, insights 28, decisions 883.
