# Brief — 2026-09-30, session 2356: the orchestration of the main agent (case 561), the round check (case 562)

## Where things stand

- Ratified (handoff): 561.1 to 561.14, 562, and the defers 563, 564, 565, 566. Cases 561 and 562 were each ratified three times; the ledger holds each decision line once.
- Code (handoff): `guppi/prespec.py` (`plan_findings` shared by `--check` and the `ExitPlanMode` hook, `check_same_target`, `open_case_items`, the docstring holds what the check compares), `guppi/onward.py` (the `--plan` run), `guppi/cli.py`, `guppi/casecheck.py` (`list_showing`, `showings`, `round_opening`), `guppi/ratified.py` (`find_showing` by `showings`). Tests: `tests/test_prespec.py`, `tests/test_onward.py`, `tests/test_casecheck.py`, `tests/test_ratified.py`. `make test` 1034 passed, 2 skipped; `make style` clean.
- By-hand measurement of case 562 (handoff): the answer to an `Agent` call stands in its `tool_result`; the answer to a `SendMessage` comes back as a later `user` record with `origin.kind` `task-notification`. The docstring of `guppi/casecheck.py` names it.
- Yaml: `raw/2026-09-30/2356/materialize.yaml` 46 entries — 26 `update`, 9 `create`, 4 `defer`, 6 `estimate`, 1 `lesson`; all 46 `applied`. Lines 32 (`estimate-case-protocol-shows-the-built-case`, repeats line 19 of 561.9) and 39 (`rule-prespec`, repeats line 1 of 561.1) applied nothing, as `generate` printed. None `failed` or `incomplete`; 1 `near`; `unparsed` empty. Its ledger has 46 lines, each held by an entry of the yaml. The yamls of `raw/2026-09-30/0138`, `0248`, `1306`, `1736` and `2042` were extended with 0 entries; `generate` wrote 0 pages from them. `superseded_by: '561.13'` was added to one entry of the 1306 yaml and `superseded_by: '561.9'` to one of the 2042 yaml.
- Pages, decisions: 20 created (561, 561.1 to 561.14, 562 to 566); `decision-case-503` superseded by 561.1, `decision-case-546` by 561.13, `decision-case-560` by 561.9, all three moved to `vault/archive/migration/2026-10-01/2356/decisions/` by `cleanup` (3 pages moved).
- Pages, rules: 2 created (`rule-prespec-onward`, 561.5; `rule-case-rebuild-cost`, a placeholder of the defer 566); 9 updated (`rule-prespec`, `rule-prespec-hook`, `rule-case-protocol`, `rule-plan-mode` its child `rule-prespec-onward`, `rule-hook-registry`, `rule-case-check`, `rule-case-build`, `rule-orchestration`, `rule-spec-box` the defer 565). Defers retired: 503 on `rule-prespec`, 546 on `rule-orchestration`; `rule-orchestration` keeps the defer of 424. Cascade built → draft: `rule-prespec`, `rule-prespec-hook`.
- Pages, estimates: 8 created (`estimate-prespec-gathers-the-answers-after-findings`, `estimate-prespec-catches-two-cases-on-one-target`, `estimate-prespec-onward-sends-the-agent-on`, `estimate-case-build-answers-what-done-means`, `estimate-case-protocol-forwards-a-discussion-question`, `estimate-case-protocol-asks-in-the-grill-me-shape`, `estimate-case-protocol-puts-the-harness-before-plan-mode`, `estimate-case-check-refuses-text-before-a-round`); 15 updated — 7 by Cases (`estimate-prespec-reconciles`, `estimate-prespec-hook-gates`, `estimate-case-protocol-shows-the-frontier-after-a-closed-line`, `estimate-case-protocol-defers-in-one-reply`, `estimate-case-protocol-acknowledging-reply`, `estimate-case-protocol-shows-the-built-case`, `estimate-case-check-shows-only-the-checked-case`), 2 by defers (`estimate-case-build-writes-a-plain-round` 563, `estimate-spec-write-writes-a-defer` 564), 6 readings from ledger lines 40 to 45: 4 `passed` (`estimate-case-check-exits-2-on-an-error`, `estimate-context-size-shows-its-error`, `estimate-retro-onward-exits-2-on-an-error`, `estimate-spec-write-exits-2-on-an-error`), 2 `failed` (`estimate-case-build-checks-the-finished-case`, `estimate-case-build-records-the-rounds-in-recommend`).
- Pages, lessons: 1 created (`lesson-sendmessage-answers-open-a-turn-of-their-own`, ledger line 46), status `new`. Insights: 0 created, 0 updated.
- Synthesis: the root cause of the one lesson matched no line of the 73 of `^(root_cause|deferred_by):` over `vault/wiki/lessons/` and no line of the 29 of `^(pattern|deferred_by):` over `vault/wiki/insights/`; no entry added.
- Render wrote `.claude/agents/case-guppi.md`, `.claude/settings.json` (`uv run guppi onward --plan` on `Stop`), `.claude/skills/pre-spec/SKILL.md` and `vault/wiki/case-schema.md`. `backlog.md`: `rule-case-rebuild-cost` added, `rule-prespec` removed, the purpose of `rule-orchestration` new, `rule-spec-box` put off in 6 sessions. `sprint.md` and `glossary.md` unchanged. The run ticked 45 boxes of `raw/2026-09-30/2356/spec.md` and 6 `read` boxes of `raw/2026-09-30/2042/spec.md`; `log.md` 86 lines added.
- Archive: `guppi archive` moved `raw/2026-09-30/0138`, `0248`, `1306`, `1736` and `2042` to `archive/migration/2026-09-30/<HHMM>/raw`; `raw/2026-09-30/2356`, the session of the run, stays. The Specs cited below as spec 0248, 1306, 1736 and 2042 now stand under `archive/migration/2026-09-30/<HHMM>/raw/spec.md`.

## Readings due

4 Estimates are `failed`, 46 `pending` (the `unread` lines of `make lint`). Every rule named below stands `draft`.

- `estimate-case-build-checks-the-finished-case` — `rule-case-build` — failed: at the `/pre-spec` of session 2356, 2 pages made false that the Case missed and 1 rule acting at the same moment that the Case missed; 561.1 also missed the defer of case 503 and put the mechanism of a Leaf into its Purpose (ledger line 44); method: by hand at `/pre-spec` of a later session after the render, the report of ask-guppi read for each Case case-guppi built
- `estimate-case-build-records-the-rounds-in-recommend` — `rule-case-build` — failed: the question of round 1 of 561 on what done means, whose answer changed only 561.11, stands in the parent's `recommend`, not under 561.11 (ledger line 45); method: by hand, the Case files of a later session after the render against the rounds in the chat
- `estimate-case-build-writes-a-plain-round` — `rule-case-build` — failed: parallel clauses in one sentence on Cases 548 and 550 and five examples in one sentence on Case 547 (session 1736); `deferred_by` 563; spec 2042: in a later session after the render, one first round and one later round of `case-guppi`
- `estimate-spec-write-writes-a-defer` — `rule-spec-write` — failed: at the first showing of Case 551 the hook raised on a malformed line, caught the error and exited 0, so nothing of 551 was written (session 1736); `deferred_by` 564; method: `uv run pytest tests/test_ratified.py -k defer`, then by hand the first defer the person asks for after the change
- `estimate-ask-finds` — `rule-ask` — method: by hand in a later session, three dispatches of ask-guppi, one existing page asked in English and in Russian, one proposal that crosses a known rule, each read against the event log
- `estimate-brief-written` — `rule-brief` — spec 2042: by hand, the brief of the first librarian run whose agent file holds this Render — this run: this brief holds Where things stand, Readings due, Flags, Next session and Readings at the close in that order, no Deferred list, and Next session holds `Cases`, `Work` and `Ask the person`
- `estimate-carry-over-writes` — `rule-carry-over` — spec 0248: at the first `/carry` after the render, and at the `/hi` after it
- `estimate-case-build-answers-what-done-means` — `rule-case-build` — spec 2356: in a later session
- `estimate-case-build-writes-the-case` — `rule-case-build` — method: by hand, live dispatches in a session after the render — one item with a fork, one Case with a create without a ref, one that changes a hook
- `estimate-case-check-refuses-text-before-a-round` — `rule-case-check` — spec 2356: in a later session
- `estimate-case-check-requires-each-question-of-the-rounds` — `rule-case-check` — spec 1306: read; method: `pytest tests/test_casecheck.py -k rounds`, then by hand the first Case the hook sends back for a missing title
- `estimate-case-check-shows-only-the-checked-case` — `rule-case-check` — spec 2356: in a later session
- `estimate-case-protocol-acknowledging-reply` — `rule-case-protocol` — spec 2356: in a later session
- `estimate-case-protocol-asks-in-the-grill-me-shape` — `rule-case-protocol` — spec 2356: in a later session
- `estimate-case-protocol-defers-in-one-reply` — `rule-case-protocol` — spec 2356: in a later session
- `estimate-case-protocol-forwards-a-discussion-question` — `rule-case-protocol` — spec 2356: in a later session
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` — method: by hand, the first session where a lesson and the Case that closes its cause stand together, and the first Case that takes up a decision with more than one Case in its `deferred_by`
- `estimate-case-protocol-puts-the-harness-before-plan-mode` — `rule-case-protocol` — spec 2356: in a later session
- `estimate-case-protocol-shows-the-built-case` — `rule-case-protocol` — spec 2356: in a later session
- `estimate-case-protocol-shows-the-frontier-after-a-closed-line` — `rule-case-protocol` — spec 2356: in a later session (also unticked in spec 1736)
- `estimate-compact-recall-reloads` — `rule-compact-recall` — method: `pytest tests/test_recall.py`; live, the first compaction of a working session
- `estimate-context-size-shown-after-each-reply` — `rule-context-size` — spec 2042: in a later session; method `uv run pytest tests/test_context.py`, then the line after the replies in the VS Code chat
- `estimate-documentation-completes` — `rule-documentation` — spec 2042: by hand, the first librarian run whose agent file holds this Render: its event log against the Flags of its brief
- `estimate-end-of-work-order` — `rule-end-of-work` — method: `make test-end-of-work`, plus by hand at the close of a later session
- `estimate-estimates-schema-checked` — `rule-estimates-schema` — spec 2042: in a later session, `uv run pytest tests/test_schemas.py -k estimate`, then `make lint`
- `estimate-event-log-records` — `rule-event-log` — method: `pytest tests/test_event.py tests/test_gate.py`; by hand, one `/hi` outside plan mode and one in it
- `estimate-generate-rewords` — `rule-page-generation` — method: `pytest tests/test_generate.py`; the live reading, the librarian's run that applies the first reword — this run: the 2356 yaml holds no `reword` (a count of `reword` in it printed 0); `generate` printed `2026-09-30/2356: 58 page(s) written or changed` and no reword line; the lines `log.md` gained hold no `reworded`
- `estimate-governed-files-hook-refuses` — `rule-governed-files-hook` — method: `pytest tests/test_guard.py`, plus by hand in a later session, one Edit of a governed file refused
- `estimate-handoff-dispatches` — `rule-handoff` — method: by hand at the `/handoff` of a later session, the event log, `handoff.md`, the dispatch line and git log
- `estimate-handoff-holds-each-fact-once` — `rule-handoff` — method: one reading by hand at the first `/handoff` after the render, against the close of its Retro
- `estimate-plan-mode-verified` — `rule-plan-mode` — method: `make test-plan-mode`; one live reading by hand
- `estimate-prespec-catches-two-cases-on-one-target` — `rule-prespec` — spec 2356: in a later session
- `estimate-prespec-gathers-the-answers-after-findings` — `rule-prespec` — spec 2356: in a later session
- `estimate-prespec-hook-gates` — `rule-prespec-hook` — spec 2356: in a later session
- `estimate-prespec-onward-sends-the-agent-on` — `rule-prespec-onward` — spec 2356: in a later session
- `estimate-prespec-reconciles` — `rule-prespec` — spec 2356: in a later session
- `estimate-python-utf8-output-intact` — `rule-python-utf8` — spec 0248: at a later session start
- `estimate-retro-onward-sends-the-agent-to-the-handoff` — `rule-retro-onward` — spec 2042: in a later session
- `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — `rule-retro` — method: one reading by hand at the first `/retro` after the render in a session whose `work.md` names a check under Expected red
- `estimate-retro-red-in-the-baseline-is-not-charged` — `rule-retro` — method: one reading by hand at the first `/retro` after the render in a session whose `work.md` Baseline holds a failing test or a lint finding line
- `estimate-retro-runs-on-to-the-handoff` — `rule-retro` — method: by hand at the first run from `/work` to the librarian after the render: the replies of the turn, the ledger, git log and `handoff.md`
- `estimate-session-phases-in-order` — `rule-session` — method: by hand at the close of a session, the hi line, `frontier.md`, the approved stamp of `spec.md`, the Retro commit, `handoff.md`, the librarian's commit
- `estimate-session-start-context` — `rule-session-start` — method: `make test-session-start`; by hand, one session opened without `/hi` whose reply carries a LEDGER block
- `estimate-spec-write-reaches-the-approved-spec` — `rule-spec-write` — spec 1306: read; method: `uv run pytest tests/test_ratified.py -k approved_spec`, then the first Case ratified in Work Mode after the change
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` — method: one reading of the tree by hand at the close of the sprint
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` — method: `make lint`, exit 0 — or only unread lines on the Estimates of `entity-sprint-migration`
- `estimate-sprint-migration-merges` — `entity-sprint-migration` — method: `make test` on the last commit of migration, then git log of main after the merge
- `estimate-synthesis-clusters` — `rule-synthesis` — spec 2042: by hand, the yaml and the report of the first librarian run after the render whose yaml holds at least two lesson entries — this run: the 2356 yaml holds 1 lesson entry; the Greps `^(root_cause|deferred_by):` over `vault/wiki/lessons/` (73 lines) and `^(pattern|deferred_by):` over `vault/wiki/insights/` (29 lines) were run; no entry marked `librarian: synthesis` was added
- `estimate-where-to-stop-stops-only-on-its-conditions` — `rule-where-to-stop` — method: by hand at the first run from `/work` to the librarian after the render: the context of `/work`, the replies of the turn and the Spec
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `rule-work-mode` — method: `uv run guppi render --check`; by hand, the first `/work` the agent calls at the fork and the first `/work` the person types

## Flags

- `near`: the create `rule-prespec-onward` (561.5) marked `near: rule-retro-onward` — both send the agent on by a `Stop` hook where no person is needed; `rule-retro-onward` after Retro, `rule-prespec-onward` in Plan Mode. The page was written.
- `generate`: `estimate-case-protocol-shows-the-built-case: line 32 repeats line 19 of case 561.9; nothing applied`.
- `generate`: `rule-prespec: line 39 repeats line 1 of case 561.1; nothing applied`.
- Failed Estimates: `estimate-case-build-checks-the-finished-case`, `estimate-case-build-records-the-rounds-in-recommend` (this run), `estimate-case-build-writes-a-plain-round` (`deferred_by` 563), `estimate-spec-write-writes-a-defer` (`deferred_by` 564).
- `incomplete`, `failed` entries: none. `unparsed`: empty. MOC candidates: none printed by any step. Contradictions: none found.
- Stale defers (`make lint`): `rule-case-rebuild-cost` 1 time since case 566; `rule-complaint-becomes-a-lesson` 1 time since case 504; `rule-morph` 1 time since case 239; `rule-orchestration` 2 times since case 424; `rule-prespec-script-skips-code-spans` 1 time since case 481; `rule-subagent-guppi` 31 times since case 29.
- `make lint` exit 2 at `guppi lint`, 60 lines: `rules/rule-spec-box: schema: missing field kind`; `rules/rule-spec-box: schema: missing field estimates`; `decisions/decision-case-13: fence: ## When: a code fence open at the end of the section`; `rules/rule-spec-box: orphan: no other live page names it in its frontmatter` (these four put off by case 565); the 6 `deferred` lines above; 50 `unread` lines (46 `pending`, 4 `failed`). `render --check`, `sprint --check`, `backlog --check` and `glossary --check` printed nothing.
- `cleanup`, `render`, `sprint`, `backlog`, `glossary`: nothing on stderr.
- Read beyond the frame: a grep of `- [ ]` over `vault/raw/` with a misplaced `--include` flag printed lines of `event_log.md` and `frontier.md` files of `vault/raw/`; it served the unticked boxes of the Specs for `Work`; the handoff did not ask for it.

## Next session

### Cases

- `rule-case-rebuild-cost` (case 566): rebuild only the changed sub-case, return a short answer to the main agent, keep the `context` short — handoff, For the next session.
- `estimate-case-build-checks-the-finished-case` failed: two pages made false and not named, a clash with another Case at one moment — ledger line 44, handoff.
- `estimate-case-build-records-the-rounds-in-recommend` failed: an item kept on the parent though its answer changed one sub-case — ledger line 45, handoff.
- `estimate-case-build-writes-a-plain-round` failed, deferred by case 563 — its page; its `read` box in `archive/migration/2026-09-30/2042/raw/spec.md` unticked.
- `estimate-spec-write-writes-a-defer` failed, deferred by case 564 — its page.
- The move of the main agent's rules into three files, held by `rule-orchestration` (defer of case 424) — handoff, For the next session.
- Whether `guppi onward --plan` should judge a Case still out by something other than the ledger's last line, since a re-ratification with unchanged lines adds none — handoff, For the next session and Observations.
- Whether the skip "no conditional on a field" of `uv run pytest tests/test_schemas.py -k estimate` (5 passed, 1 skipped) leaves untested the section the Criterion of `estimate-estimates-schema-checked` requires on `passed` and `failed` — handoff, Observations.

### Work

- `estimate-ask-finds`
- `estimate-brief-written`
- `estimate-carry-over-writes`
- `estimate-case-build-answers-what-done-means`
- `estimate-case-build-writes-the-case`
- `estimate-case-check-refuses-text-before-a-round`
- `estimate-case-check-requires-each-question-of-the-rounds`
- `estimate-case-check-shows-only-the-checked-case`
- `estimate-case-protocol-acknowledging-reply`
- `estimate-case-protocol-asks-in-the-grill-me-shape`
- `estimate-case-protocol-defers-in-one-reply`
- `estimate-case-protocol-forwards-a-discussion-question`
- `estimate-case-protocol-ledger-line-form`
- `estimate-case-protocol-puts-the-harness-before-plan-mode`
- `estimate-case-protocol-shows-the-built-case`
- `estimate-case-protocol-shows-the-frontier-after-a-closed-line`
- `estimate-compact-recall-reloads`
- `estimate-documentation-completes`
- `estimate-end-of-work-order`
- `estimate-estimates-schema-checked`
- `estimate-event-log-records`
- `estimate-generate-rewords`
- `estimate-governed-files-hook-refuses`
- `estimate-handoff-dispatches`
- `estimate-handoff-holds-each-fact-once`
- `estimate-plan-mode-verified`
- `estimate-prespec-catches-two-cases-on-one-target`
- `estimate-prespec-gathers-the-answers-after-findings`
- `estimate-prespec-hook-gates`
- `estimate-prespec-onward-sends-the-agent-on`
- `estimate-prespec-reconciles`
- `estimate-python-utf8-output-intact`
- `estimate-retro-onward-sends-the-agent-to-the-handoff` (handoff: its moment was the run of session 2356, from `/work` to the librarian's report)
- `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`
- `estimate-retro-red-in-the-baseline-is-not-charged` (handoff: its moment was the run of session 2356)
- `estimate-retro-runs-on-to-the-handoff` (handoff: its moment was the run of session 2356)
- `estimate-session-phases-in-order`
- `estimate-session-start-context`
- `estimate-spec-write-reaches-the-approved-spec`
- `estimate-sprint-migration-leftovers-gone`
- `estimate-sprint-migration-lint-clean`
- `estimate-sprint-migration-merges`
- `estimate-synthesis-clusters`
- `estimate-where-to-stop-stops-only-on-its-conditions` (handoff: its moment was the run of session 2356)
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`

### Ask the person

- `estimate-context-size-shown-after-each-reply` — needs the person: after the replies of this session in the VS Code chat, did the context size line stand under each reply?

## Readings at the close

- `make test`: 1034 passed, 2 skipped.
- `make lint`: exit 2 at `guppi lint`, 60 lines — 3 on `rule-spec-box`, 1 fence on `decision-case-13`, 6 `deferred`, 50 `unread`; the four `--check` steps clean.
- Live pages: rules 76, entities 4, estimates 182, decisions 900, lessons 74, insights 28. Files `*.md` under `vault/archive/`: 646 after `guppi archive`.
