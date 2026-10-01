# Brief — 2026-10-01, session 1441: the Stop hooks after a refusal, the later Frontier, related Cases in the dispatch, the waiting line of pre-spec

## Where things stand

- Ratified (handoff): 577.1 to 577.8, 578.1, 578.2, 579.1, 579.2, 581.1, 581.2. Case 580 was ratified, then ratified again as 580.1 and 580.2, then built again as 581.1 and 581.2, which supersede 580, 580.1 and 580.2. Cases 577, 578 and 579 were ratified again after `/pre-spec`; the ledger holds each of their decision lines once.
- Code (handoff): `guppi/ledger.py` — `own_refusals`, the one judgment of the stretch and of a hook's own refusals, `silenced` and `untold`; the ledger hook writes whatever `stop_hook_active` says and tells each refused line once a stretch. `guppi/onward.py` — the run without `--plan` judges its own refusal through `own_refusals` and `silenced`; `--plan` keeps the flag. `guppi/casecheck.py` — docstrings. Tests: `tests/test_ledger.py`, `tests/test_onward.py`; `make test` 1050 passed, 2 skipped; `make style` clean.
- Readings (handoff): ledger line 13 `estimate-case-build-writes-a-plain-round` passed, line 21 `estimate-spec-write-writes-a-defer` passed; Retro lines 33 to 36: `estimate-ask-finds` failed, `estimate-case-build-records-the-rounds-in-recommend`, `estimate-case-protocol-asks-in-the-grill-me-shape` and `estimate-governed-files-hook-refuses` passed. Lesson: ledger line 32.
- Yaml: `raw/2026-10-01/1441/materialize.yaml` 36 entries from `materialize` — 28 `update`, 1 `create` (an Estimate), 6 `estimate`, 1 `lesson` — plus 3 entries of the synthesis. 33 of the 36 entries and the 3 synthesis entries `applied`; the 6 entries of ledger lines 22 to 27 (cases 580, 580.1, 580.2) carry `superseded_by` 581.1 or 581.2 and were not applied, 3 of them also `incomplete: [criterion]`. None `failed` or `exists`; `unparsed` empty. Its ledger has 36 lines, each held by an entry of the yaml (lines 1 to 36). `raw/2026-10-01/1237/materialize.yaml` was extended with 0 entries; `materialize` marked its entry of line 22 and the decision record of 571 `superseded_by` 579.2. `generate` wrote 0 pages from the 1237 yaml and 52 from the 1441 yaml.
- Index check: the yaml holds one `create` other than a lesson, an Estimate (`estimate-case-protocol-names-related-cases-in-the-dispatch`), which has no index; no Grep for it. The lesson entry of line 32 was compared with the 74 lines of the Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/`: marked `near: lesson-spec-write-keeps-the-body-of-a-case-rebuilt-as-a-parent`.
- Synthesis: Greps `^(root_cause|deferred_by):` over `vault/wiki/lessons/` (74 lines) and `^(pattern|deferred_by):` over `vault/wiki/insights/` (29 lines). The lesson of line 32 and `lesson-spec-write-keeps-the-body-of-a-case-rebuilt-as-a-parent` (status `new`) share one root cause, and no Insight holds it: `insight-spec-write-parent-body-kept-on-re-ratification` created (severity 2), both lessons set `clustered` under it. The lesson entry carries no `addressed_by`.
- Pages, decisions: 21 created (577, 577.1 to 577.8, 578, 578.1, 578.2, 579, 579.1, 579.2, 580, 580.1, 580.2, 581, 581.1, 581.2). `decision-case-571` superseded by 579.2; `decision-case-580` and `decision-case-580.1` superseded by 581.1, `decision-case-580.2` by 581.2; `cleanup` moved these 4 pages to `archive/migration/2026-10-01/1441/decisions/`.
- Pages, rules: 7 updated — 6 by Cases (`rule-retro-onward` 577.1, 577.2; `rule-ledger-write` 577.3, 577.4; `rule-case-protocol` 578.2, 579.1; `rule-case-build` 579.2; `rule-prespec` 581.1; `rule-case-check` 581.2); cascade: `rule-governed-files-hook` draft → built, `rule-ledger-write` and `rule-retro-onward` built → draft.
- Pages, estimates: 1 created (`estimate-case-protocol-names-related-cases-in-the-dispatch`, 579.1); 13 updated by Cases, each set `pending` with its Criterion replaced (577.1 to 577.8, 578.1, 578.2, 579.2, 581.1, 581.2); 6 readings (5 `passed`, 1 `failed`).
- Pages, lessons: 1 created (`lesson-spec-write-keeps-the-body-of-a-case-that-gains-sub-cases`), 2 updated (clustered). Insights: 1 created.
- Render wrote `vault/wiki/case-schema.md`, `.claude/agents/case-guppi.md` and `.claude/skills/pre-spec/SKILL.md`. `backlog.md` changed; `sprint.md` and `glossary.md` unchanged. The run ticked 27 boxes of `raw/2026-10-01/1441/spec.md` and 1 `read` box of `raw/2026-10-01/1237/spec.md`; `log.md` 70 lines added.
- Archive: `guppi archive` printed nothing and moved nothing; it looks only at units dated before the day of the run, and `raw/2026-10-01/1237` and `raw/2026-10-01/1441` are of the run day.

## Readings due

1 Estimate is `failed`, 38 `pending` (the 39 `unread` lines of `make lint`). Every target named below stands `draft`.

- `estimate-ask-finds` — `rule-ask` — failed: two of three answers of `ask-guppi` (the English one and the SessionStart one) add a `Files:` list of six and five page paths after the five lines (ledger line 33); method: by hand in a later session, three dispatches of ask-guppi, one existing page asked in English and in Russian, one proposal that crosses a known rule
- `estimate-retro-onward-sends-the-agent-to-the-handoff` — `rule-retro-onward` — spec 1441: in a later session; method: `uv run pytest tests/test_onward.py`; by hand at the first end of Retro after the render that follows a refusal of another Stop hook in the same stretch
- `estimate-retro-onward-exits-2-on-an-error` — `rule-retro-onward` — spec 1441: in a later session; method: `uv run pytest tests/test_onward.py`, a function of the hook patched to raise
- `estimate-ledger-write-lifts` — `rule-ledger-write` — spec 1441: in a later session; method: pytest in `tests/test_ledger.py` and `tests/test_gate.py`; by hand once, the ledger of the first session after the change whose reply that ends Retro follows a refusal of a Stop hook in the same stretch
- `estimate-ledger-write-exits-2-on-an-error` — `rule-ledger-write` — spec 1441: in a later session; method: `uv run pytest tests/test_ledger.py`, a function of the hook patched to raise
- `estimate-ledger-write-refuses-a-line-it-cannot-read` — `rule-ledger-write` — spec 1441: in a later session; method: `uv run pytest tests/test_ledger.py`
- `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` — `rule-ledger-write` — spec 1441: in a later session; method: `uv run pytest tests/test_ledger.py`
- `estimate-ledger-write-refuses-a-lesson-without-its-prefix` — `rule-ledger-write` — spec 1441: in a later session; method: `uv run pytest tests/test_ledger.py`
- `estimate-ledger-write-refuses-a-mark-with-no-decision-line` — `rule-ledger-write` — spec 1441: in a later session; method: `uv run pytest tests/test_ledger.py`
- `estimate-case-protocol-shows-the-frontier-after-a-closed-line` — `rule-case-protocol` — spec 1441: by hand, in a later session after the render, the first Plan Mode reply after the first reply of `/hi` that closes a line of `frontier.md` with no ratification and no defer
- `estimate-case-protocol-acknowledging-reply` — `rule-case-protocol` — spec 1441: by hand, the first acknowledging reply of a later session after the render
- `estimate-case-protocol-names-related-cases-in-the-dispatch` — `rule-case-protocol` — spec 1441: by hand at the close of a later session after the render
- `estimate-case-build-checks-the-finished-case` — `rule-case-build` — spec 1441: by hand at `/pre-spec` of a later session after the render, the report of ask-guppi read for each Case
- `estimate-prespec-gathers-the-answers-after-findings` — `rule-prespec` — spec 1441: by hand at the `/pre-spec` of a later session after the render whose report sends findings to two or more `case-guppi`
- `estimate-case-check-refuses-text-before-a-round` — `rule-case-check` — spec 1441: `uv run pytest tests/test_casecheck.py -k round` and by hand in a later session, the first rounds of `case-guppi` shown before and after `/pre-spec`
- `estimate-documentation-completes` — `rule-documentation` — spec 1237: at the first librarian run whose agent file holds this Render, its event log against the Flags of its brief and its report; method: `make test-documentation`; the live reading by hand
- `estimate-brief-written` — `rule-brief` — spec 1237: by hand, the brief of the first librarian run whose agent file holds this Render; method: one reading by hand after the first librarian run — this run: the brief holds Where things stand, Readings due, Flags, Next session (`Cases`, `Work`, `Ask the person`) and Readings at the close, and no Deferred list
- `estimate-retro-runs-on-to-the-handoff` — `rule-retro` — spec 1237: in a later session; method: by hand at the first run from `/work` to the librarian after the render
- `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — `rule-retro` — spec 1237: in a later session; method: by hand at the first `/retro` after the render in a session whose `work.md` names a check under Expected red
- `estimate-carry-over-writes` — `rule-carry-over` — method: `uv run guppi render --check`; by hand, the first `/carry` after the fork of ExitPlanMode
- `estimate-case-build-writes-the-case` — `rule-case-build` — method: by hand, live dispatches in a session after the render — one item with a fork, one Case with a create without a ref and one that changes a hook
- `estimate-case-check-requires-each-question-of-the-rounds` — `rule-case-check` — method: `pytest tests/test_casecheck.py -k rounds`; then by hand the first Case the hook sends back for a missing title
- `estimate-case-check-shows-only-the-checked-case` — `rule-case-check` — method: `uv run pytest tests/test_casecheck.py -k stop`, then by hand the first reply the hook refuses
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` — method: by hand, the ledger and the preview of the first session where a lesson and the Case that closes its cause stand together, and of the first Case that takes up a decision with more than one Case in its `deferred_by`
- `estimate-compact-recall-reloads` — `rule-compact-recall` — method: `pytest tests/test_recall.py`; live, the first compaction of a working session
- `estimate-end-of-work-order` — `rule-end-of-work` — method: `make test-end-of-work`, plus by hand at the close of a later session
- `estimate-estimates-schema-checked` — `rule-estimates-schema` — method: `pytest tests/test_schemas.py -k estimate` on the live schema; the live reading `make lint`, no schema finding on `wiki/estimates/`
- `estimate-event-log-records` — `rule-event-log` — method: pytest in `tests/test_event.py` and `tests/test_gate.py`; by hand, one `/hi` outside plan mode and one in it
- `estimate-generate-rewords` — `rule-page-generation` — method: `pytest tests/test_generate.py`; the live reading the librarian's run that applies the first reword — this run: no entry of the 1441 yaml carries `reword`; `generate` printed two lines, 0 and 52 pages written or changed, and no reword line
- `estimate-handoff-dispatches` — `rule-handoff` — method: by hand at the `/handoff` of a later session
- `estimate-handoff-holds-each-fact-once` — `rule-handoff` — method: one reading by hand at the first `/handoff` after the render
- `estimate-plan-mode-verified` — `rule-plan-mode` — method: `make test-plan-mode`; the flagging one live reading by hand
- `estimate-session-start-context` — `rule-session-start` — method: `make test-session-start`; by hand, one session opened without `/hi` whose reply carries a LEDGER block
- `estimate-spec-write-reaches-the-approved-spec` — `rule-spec-write` — method: `uv run pytest tests/test_ratified.py -k approved_spec`; by hand, the first Case ratified in Work Mode after the change
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` — method: one reading of the tree by hand at the close of the sprint
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` — method: `make lint`, exit 0, or only unread lines on the Estimates of `entity-sprint-migration`
- `estimate-sprint-migration-merges` — `entity-sprint-migration` — method: `make test` on the last commit of migration, then git log of main after the merge
- `estimate-synthesis-clusters` — `rule-synthesis` — method: one reading by hand of the yaml and the report after a live librarian run whose yaml holds at least two lesson entries — this run: the 1441 yaml holds one lesson entry (line 32); Greps `^(root_cause|deferred_by):` over `vault/wiki/lessons/` (74 lines) and `^(pattern|deferred_by):` over `vault/wiki/insights/` (29 lines); 3 entries added, each `librarian: synthesis` — one `create` of `insight-spec-write-parent-body-kept-on-re-ratification` with `pattern`, two children, tags `harness`, `workflow`, `hooks`, `session`, `Pattern` and `Proposal`, and one `update` per lesson with `set: {status: clustered, insight: insight-spec-write-parent-body-kept-on-re-ratification}`; lesson page read: `lesson-spec-write-keeps-the-body-of-a-case-rebuilt-as-a-parent`
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `rule-work-mode` — method: `uv run guppi render --check`; by hand, the first `/work` the agent calls at the fork and the first `/work` the person types

## Flags

- `incomplete`: the entries of ledger lines 23, 25 and 27 (`estimate-prespec-gathers-the-answers-after-findings` of 580 and 580.1, `estimate-case-check-refuses-text-before-a-round` of 580.2) lack `criterion`; all three are `superseded_by` 581.1 or 581.2 and were not applied.
- `near`: the lesson entry of line 32, `lesson-spec-write-keeps-the-body-of-a-case-that-gains-sub-cases`, near `lesson-spec-write-keeps-the-body-of-a-case-rebuilt-as-a-parent`; both clustered under `insight-spec-write-parent-body-kept-on-re-ratification`.
- No entry `failed`; `unparsed` empty.
- Failed Estimate: `estimate-ask-finds` (ledger line 33).
- MOC candidates: none.
- Stale defers (`make lint`): `rule-case-rebuild-cost` deferred 2 times since case 566; `rule-complaint-becomes-a-lesson` 1 time since case 504; `rule-morph` 1 time since case 239; `rule-orchestration` 3 times since case 424; `rule-prespec-script-skips-code-spans` 1 time since case 481; `rule-subagent-guppi` 31 times since case 29.
- Contradiction (handoff, Observations): the module docstring of `guppi/casecheck.py` says a refusal of a `Stop` hook adds no `user` record (measured 2026-09-27); the transcripts of sessions 1237 and 1441 show it adds one, marked `isMeta`.
- Handoff, Observations: `estimate-estimates-schema-checked` not read — no test of `tests/test_schemas.py` covers the conditional `## Result` section of the Estimates schema.
- Handoff, Notes from memory: the person judged the length point of `estimate-case-protocol-acknowledging-reply` passed and does not want the length counted as a failure at its next reading.
- Handoff, Direct instructions to the librarian: no repair was asked. The run left `decision-case-580`, `580.1` and `580.2` and `decision-case-571` archived as superseded; `rule-case-protocol` took both pairs, of 578.2 and of 579.1.
- Lint (`make lint`, exit 2), 49 lines: `rules/rule-spec-box: schema: missing field kind`; `rules/rule-spec-box: schema: missing field estimates`; `decisions/decision-case-13: fence: ## When: a code fence open at the end of the section`; `rules/rule-spec-box: orphan: no other live page names it in its frontmatter`; the 6 deferred lines above; 39 `unread` lines, one per Estimate of Readings due (1 `failed`, 38 `pending`). The handoff's Baseline holds the same schema, orphan and fence findings, 6 deferred lines and 34 unread lines.
- Reads outside the frame: none.

## Next session

Cases:
- The Spec hook of `rule-spec-write` keeps the body a Case held when it stood alone once it is ratified again with sub-cases; whether the hook should replace the whole Case on re-ratification — handoff, For the next session; `insight-spec-write-parent-body-kept-on-re-ratification`.
- `estimate-ask-finds` failed: two of three answers of `ask-guppi` add a list of file paths after the five lines; whether the frame of `ask-guppi` forbids the list or the Criterion allows it — handoff, For the next session; ledger line 33.
- The test of a conditional section of the Estimates schema: write it, or change the Criterion of `estimate-estimates-schema-checked`; the defer of case 576 still stands — handoff, For the next session.
- The close of the sprint (Slice 5) stays put off — handoff, For the next session.
- The module docstring of `guppi/casecheck.py` contradicts the transcripts of sessions 1237 and 1441 on the `user` record a `Stop` refusal adds — handoff, Observations.

Work:
- Readings `pending`: `estimate-retro-onward-sends-the-agent-to-the-handoff`, `estimate-retro-onward-exits-2-on-an-error`, `estimate-ledger-write-lifts`, `estimate-ledger-write-exits-2-on-an-error`, `estimate-ledger-write-refuses-a-line-it-cannot-read`, `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session`, `estimate-ledger-write-refuses-a-lesson-without-its-prefix`, `estimate-ledger-write-refuses-a-mark-with-no-decision-line`, `estimate-case-protocol-shows-the-frontier-after-a-closed-line`, `estimate-case-protocol-acknowledging-reply`, `estimate-case-protocol-names-related-cases-in-the-dispatch`, `estimate-case-build-checks-the-finished-case`, `estimate-prespec-gathers-the-answers-after-findings`, `estimate-case-check-refuses-text-before-a-round` — each also an unticked `read` box of `raw/2026-10-01/1441/spec.md` (14 boxes).
- Readings `pending`: `estimate-documentation-completes`, `estimate-brief-written`, `estimate-retro-runs-on-to-the-handoff`, `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — each also an unticked `read` box of `raw/2026-10-01/1237/spec.md` (4 boxes).
- Readings `pending`: `estimate-carry-over-writes`, `estimate-case-build-writes-the-case`, `estimate-case-check-requires-each-question-of-the-rounds`, `estimate-case-check-shows-only-the-checked-case`, `estimate-case-protocol-ledger-line-form`, `estimate-compact-recall-reloads`, `estimate-end-of-work-order`, `estimate-estimates-schema-checked`, `estimate-event-log-records`, `estimate-generate-rewords`, `estimate-handoff-dispatches`, `estimate-handoff-holds-each-fact-once`, `estimate-plan-mode-verified`, `estimate-session-start-context`, `estimate-spec-write-reaches-the-approved-spec`, `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges`, `estimate-synthesis-clusters`, `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`.
- Ledger lines 22 to 27 of `raw/2026-10-01/1441/ledger.md` (cases 580, 580.1, 580.2) not applied: `superseded_by` 581.1 and 581.2.

Ask the person:
- none

## Readings at the close

- `make test`: 1050 passed, 2 skipped.
- `make lint`: exit 2, 49 lines — 3 schema and fence findings, 1 orphan, 6 deferred, 39 unread.
- Live pages: rules 70, entities 4, estimates 182, decisions 931, lessons 75, insights 29.
