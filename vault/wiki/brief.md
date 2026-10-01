# Brief — 2026-10-01, session 1725: the check of ask-guppi, the test of section conditionals, the casecheck docstring

## Where things stand

- Ratified (handoff): 582, 583, 584; deferred: 585, 586. Case 583 was ratified, built again on a `/pre-spec` finding and ratified again; the ledger holds its decision line once (line 4).
- Code (handoff): `guppi/casecheck.py` — the module docstring gives the measured shape of a `Stop` refusal, a `user` record marked `isMeta`. Tests: `tests/test_schemas.py` — `test_a_section_conditional_not_met_is_one_finding_where_the_schema_has_one`; `tests/test_casecheck.py` — `test_stop_a_sending_before_a_refusal_counts_in_the_turn_of_the_reply`. `make test` 1053 passed, 6 skipped; `make style` clean.
- Readings (handoff): ledger lines 1 and 2 at `/hi` (`estimate-documentation-completes`, `estimate-brief-written`), lines 8 to 16 in Work Mode and Retro; all 11 `passed`. Lessons: none.
- Yaml: `raw/2026-10-01/1725/materialize.yaml` 16 entries from `materialize` — 3 `update`, 2 `defer`, 11 `estimate`; all 16 `applied`. None `failed`, `incomplete` or `near`; `unparsed` empty; the defer of 585 carries `exists: true`, the defer of 586 `exists: false`. Its ledger has 16 lines, each held by an entry of the yaml (lines 1 to 16). `raw/2026-10-01/1237/materialize.yaml` and `raw/2026-10-01/1441/materialize.yaml` were extended with 0 entries; `materialize` marked the entry of case 576 and the decision record of 576 in the 1237 yaml `superseded_by` 583. `generate` wrote 0 pages from the 1237 yaml, 0 from the 1441 yaml and 24 from the 1725 yaml.
- Index check: the yaml holds no `create` entry. The defer of 586 writes a placeholder page, `rule-turn-start-one-judgment`; it was compared with the 89 lines of the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`: no live rule holds the same thing; the yaml was not edited.
- Synthesis: the yaml holds no `lesson` entry; no Grep ran, no entry was added.
- Pages, decisions: 5 created (582, 583, 584, 585, 586). `decision-case-576` superseded by 583; `generate` and `cleanup` moved it to `archive/migration/2026-10-01/1725/decisions/`.
- Pages, rules: 1 updated by a Case (`rule-case-check`, 584, a History line); 1 placeholder created (`rule-turn-start-one-judgment`, deferred by 586); cascade: `rule-brief` and `rule-documentation` draft → built.
- Pages, estimates: 2 updated by Cases — `estimate-ask-finds` (582: Criterion replaced, `purpose` set, `status: pending`) and `estimate-estimates-schema-checked` (583: Criterion replaced, `status: pending`, as it stood); 11 readings, all `passed`. No Estimate created.
- Pages, insights: 1 updated (`insight-spec-write-parent-body-kept-on-re-ratification`, deferred by 585). Lessons: none.
- Render wrote no governed file that changed (`CLAUDE.md`, `.claude/` and `guppi.toml` clean). `backlog.md` changed; `sprint.md` and `glossary.md` unchanged. The run ticked 3 `update` boxes of `raw/2026-10-01/1725/spec.md`, 2 `read` boxes of `raw/2026-10-01/1237/spec.md` and 8 `read` boxes of `raw/2026-10-01/1441/spec.md`; `log.md` 26 lines added.
- Archive: `guppi archive` printed nothing on stdout or stderr and moved nothing; `raw/2026-10-01/1237`, `1441` and `1725` are of the run day.

## Readings due

0 Estimates `failed`, 28 `pending` (the 28 `unread` lines of `make lint`). Every target rule named below stands `draft`; `entity-sprint-migration` stands `draft`.

- `estimate-ask-finds` — `rule-ask` (draft) — spec 1725: by hand in a later session, three dispatches of `ask-guppi`, one existing page asked in English and in Russian, one proposal that crosses a known rule, each read against the event log and the Criterion
- `estimate-estimates-schema-checked` — `rule-estimates-schema` (draft) — spec 1725: in the next session, `uv run pytest tests/test_schemas.py -k estimate` on the live schema, and the live reading `make lint`, no schema finding on `wiki/estimates/`
- `estimate-retro-onward-sends-the-agent-to-the-handoff` — `rule-retro-onward` (draft) — spec 1441: in a later session; method: `uv run pytest tests/test_onward.py`; by hand at the first end of Retro after the render that follows a refusal of another Stop hook in the same stretch
- `estimate-ledger-write-lifts` — `rule-ledger-write` (draft) — spec 1441: in a later session; method: pytest in `tests/test_ledger.py` and `tests/test_gate.py`; by hand once, the ledger of the first session after the change whose reply that ends Retro follows a refusal of a Stop hook in the same stretch
- `estimate-case-protocol-shows-the-frontier-after-a-closed-line` — `rule-case-protocol` (draft) — spec 1441: by hand, in a later session after the render, the first Plan Mode reply after the first reply of `/hi` that closes a line of `frontier.md` with no ratification and no defer
- `estimate-prespec-gathers-the-answers-after-findings` — `rule-prespec` (draft) — spec 1441: by hand at the `/pre-spec` of a later session after the render whose report sends findings to two or more `case-guppi`
- `estimate-case-check-refuses-text-before-a-round` — `rule-case-check` (draft) — spec 1441: `uv run pytest tests/test_casecheck.py -k round` and by hand in a later session, the first rounds of `case-guppi` shown before and after `/pre-spec`
- `estimate-retro-runs-on-to-the-handoff` — `rule-retro` (draft) — spec 1237: in a later session; method: by hand at the first run from `/work` to the librarian after the render
- `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — `rule-retro` (draft) — spec 1237: in a later session; method: by hand at the first `/retro` after the render in a session whose `work.md` names a check under Expected red
- `estimate-carry-over-writes` — `rule-carry-over` (draft) — method: `uv run guppi render --check`; by hand, the first `/carry` after the fork of ExitPlanMode
- `estimate-case-build-writes-the-case` — `rule-case-build` (draft) — method: by hand, live dispatches in a session after the render — one item with a fork, one Case with a create without a ref and one that changes a hook
- `estimate-case-check-requires-each-question-of-the-rounds` — `rule-case-check` (draft) — method: `pytest tests/test_casecheck.py -k rounds`; then by hand the first Case the hook sends back for a missing title
- `estimate-case-check-shows-only-the-checked-case` — `rule-case-check` (draft) — method: `uv run pytest tests/test_casecheck.py -k stop`, then by hand the first reply the hook refuses
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` (draft) — method: by hand, the ledger and the preview of the first session where a lesson and the Case that closes its cause stand together, and of the first Case that takes up a decision with more than one Case in its `deferred_by`
- `estimate-compact-recall-reloads` — `rule-compact-recall` (draft) — method: `pytest tests/test_recall.py`; live, the first compaction of a working session
- `estimate-end-of-work-order` — `rule-end-of-work` (draft) — method: `make test-end-of-work`, plus by hand at the close of a later session
- `estimate-event-log-records` — `rule-event-log` (draft) — method: pytest in `tests/test_event.py` and `tests/test_gate.py`; by hand, one `/hi` outside plan mode and one in it
- `estimate-generate-rewords` — `rule-page-generation` (draft) — method: `pytest tests/test_generate.py`; the live reading the librarian's run that applies the first reword — this run: no entry of the 1725 yaml carries `reword`; `generate` printed three lines, 0, 0 and 24 pages written or changed, and no reword line
- `estimate-handoff-dispatches` — `rule-handoff` (draft) — method: by hand at the `/handoff` of a later session
- `estimate-handoff-holds-each-fact-once` — `rule-handoff` (draft) — method: one reading by hand at the first `/handoff` after the render
- `estimate-plan-mode-verified` — `rule-plan-mode` (draft) — method: `make test-plan-mode`; the flagging one live reading by hand
- `estimate-session-start-context` — `rule-session-start` (draft) — method: `make test-session-start`; by hand, one session opened without `/hi` whose reply carries a LEDGER block
- `estimate-spec-write-reaches-the-approved-spec` — `rule-spec-write` (draft) — method: `uv run pytest tests/test_ratified.py -k approved_spec`; by hand, the first Case ratified in Work Mode after the change
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` (draft) — method: one reading of the tree by hand at the close of the sprint
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` (draft) — method: `make lint`, exit 0, or only unread lines on the Estimates of `entity-sprint-migration`
- `estimate-sprint-migration-merges` — `entity-sprint-migration` (draft) — method: `make test` on the last commit of migration, then git log of main after the merge
- `estimate-synthesis-clusters` — `rule-synthesis` (draft) — method: one reading by hand of the yaml and the report after a live librarian run whose yaml holds at least two lesson entries — this run: the 1725 yaml holds 0 lesson entries; no synthesis Grep ran; 0 entries added
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `rule-work-mode` (draft) — method: `uv run guppi render --check`; by hand, the first `/work` the agent calls at the fork and the first `/work` the person types

## Flags

- No entry `incomplete`, `failed` or `near`; `unparsed` empty.
- Failed Estimates: none.
- MOC candidates: none.
- Stale defers (`make lint`): `rule-case-rebuild-cost` deferred 2 times since case 566; `rule-complaint-becomes-a-lesson` 1 time since case 504; `rule-morph` 1 time since case 239; `rule-orchestration` 3 times since case 424; `rule-prespec-script-skips-code-spans` 1 time since case 481; `rule-subagent-guppi` 31 times since case 29; `rule-turn-start-one-judgment` 1 time since case 586.
- Contradiction: the handoff (Direct instructions) and the `context` of case 583 say its `update` of `estimate-estimates-schema-checked` carries only `change`, "sets no `status` and writes no Criterion, so the scripts keep the whole Criterion of the page". The yaml entry of ledger line 4 carries `set: {status: pending}` and `sections: Criterion` (the `then` of the Case), and `generate` applied it: the page's Criterion was replaced whole by the `then` of 583; its old Criterion (the Render of `rule-estimates-schema` written to `schema.yaml`, the fields, values and sections lint reads, the finding on a missing `method`, the `description` lines) is no longer on the page. Its `status` was `pending` before and after. Not repaired.
- Handoff, Direct instructions to the librarian: no repair was asked. `decision-case-576` was superseded by 583 and archived; `estimate-estimates-schema-checked` carries no `deferred_by`; 586 wrote the placeholder `rule-turn-start-one-judgment`; 582 replaced the Criterion of `estimate-ask-finds` and set its `purpose` and `status: pending`.
- Handoff, Notes from memory: the person put off the close of the sprint as a sprint item with no Case.
- Handoff, Observations: the Baseline `make lint` exited 2 at its backlog step (`backlog: vault/wiki/backlog.md differs from its sources`); the page step run alone gave the schema, orphan and fence findings, 6 deferred lines and 39 unread lines. After this run's `guppi backlog`, `make lint` reaches its page step.
- Lint (`make lint`, exit 2), 40 lines: `rules/rule-spec-box: schema: missing field kind`; `rules/rule-spec-box: schema: missing field estimates`; `decisions/decision-case-13: fence: ## When: a code fence open at the end of the section`; `rules/rule-spec-box: orphan: no other live page names it in its frontmatter`; the 7 deferred lines above; 28 `unread: pending` lines, one per Estimate of Readings due; the `make` error line.
- Reads outside the frame: none.

## Next session

Cases:
- `make lint` stops at its first red step; once a session puts an item off, its backlog step is red until the librarian runs `guppi backlog`, and the page findings of the Baseline are not printed; whether `make lint` should run every step and report each, or the Baseline should run the page step on its own — handoff, For the next session.
- `materialize` lifted the `then` of case 583 as the Criterion and `status: pending` into the `update` of `estimate-estimates-schema-checked`, which the Case said carries only `change`; `generate` replaced the page's Criterion — defect found by the librarian, yaml entry of ledger line 4 of `raw/2026-10-01/1725/ledger.md` and `git diff` of the page.

Work:
- Readings `pending`: `estimate-ask-finds`, `estimate-estimates-schema-checked` — each also an unticked `read` box of `raw/2026-10-01/1725/spec.md` (2 boxes).
- Readings `pending`: `estimate-retro-onward-sends-the-agent-to-the-handoff`, `estimate-ledger-write-lifts`, `estimate-case-protocol-shows-the-frontier-after-a-closed-line`, `estimate-prespec-gathers-the-answers-after-findings`, `estimate-case-check-refuses-text-before-a-round` — each also an unticked `read` box of `raw/2026-10-01/1441/spec.md` (5 boxes).
- Readings `pending`: `estimate-retro-runs-on-to-the-handoff`, `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — each also an unticked `read` box of `raw/2026-10-01/1237/spec.md` (2 boxes).
- Readings `pending`: `estimate-carry-over-writes`, `estimate-case-build-writes-the-case`, `estimate-case-check-requires-each-question-of-the-rounds`, `estimate-case-check-shows-only-the-checked-case`, `estimate-case-protocol-ledger-line-form`, `estimate-compact-recall-reloads`, `estimate-end-of-work-order`, `estimate-event-log-records`, `estimate-generate-rewords`, `estimate-handoff-dispatches`, `estimate-handoff-holds-each-fact-once`, `estimate-plan-mode-verified`, `estimate-session-start-context`, `estimate-spec-write-reaches-the-approved-spec`, `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges`, `estimate-synthesis-clusters`, `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`.

Ask the person:
- none

## Readings at the close

- `make test`: 1053 passed, 6 skipped.
- `make lint`: exit 2, 40 lines — 3 schema and fence findings, 1 orphan, 7 deferred, 28 unread, the `make` error line.
- Live pages (`*.md` per folder): rules 77, entities 4, estimates 183, decisions 935, lessons 75, insights 29.
