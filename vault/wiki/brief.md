# Brief — 2026-10-02, session 1202: make lint, the Estimate update, the language finding, one turn judgment, the Spec box

## Where things stand

- Ratified (handoff): 587, 588.1, 588.2, 588.3, 589.1, 589.2, 590.2, 590.3, 591.1, 591.3, 591.4, 591.7, 591.8, 591.9, 591.10, 591.11, 591.12, 592, 593.1, 593.2, 593.3. Deferred: 594 (`rule-ledger-line-withdrawn-on-re-ratification`). Superseded in the session: 590.1 (by 592), 591.2 (by 593.1), 591.5 (by 593.2), 591.6 (by 593.3).
- Code (handoff): `Makefile` (`lint` runs every step, exits non-zero when any is red); `guppi/materialize.py`, `guppi/config.py`, `guppi/ratified.py`, `guppi/prespec.py`, `guppi/ledger.py`, `guppi/casecheck.py`, `guppi/context.py`, `guppi/box.py` (new), `guppi/spec.py`, `guppi/cli.py` (the command `box`). Tests: `tests/test_box.py` new, seven test files changed. `make test` 1074 passed, 6 skipped; `make style` clean.
- Pages by hand (handoff): `## How it works` removed from `rule-case-check`, `rule-ledger-write` and `rule-context-size`.
- Readings (handoff): ledger lines 55 and 56 (`estimate-case-protocol-shows-the-frontier-after-a-closed-line`, `estimate-prespec-gathers-the-answers-after-findings`), both `passed`. Lessons: none.
- Yaml: `raw/2026-10-02/1202/materialize.yaml`, 56 entries from `materialize` — 38 `update`, 12 `create`, 3 `delete`, 1 `defer`, 2 `estimate`. 43 `applied`; 13 carry `superseded_by` and were not applied; 0 `failed`; 7 `incomplete`, all among the superseded; `unparsed` empty. The ledger has 56 lines, each held by an entry of the yaml (lines 1 to 56). `raw/2026-10-01/1237`, `1441` and `1725` yamls extended with 0 entries; `materialize` marked the entry of line 7 of the 1725 yaml (the defer of 586) `superseded_by` 592, and the decision record of 586 there `superseded_by` 590.1 and 592.
- Handoff check: `materialize` marked every line of 590.1 (lines 11 to 14), 591.2 (19, 20, 39), 591.5 (25, 26, 27, 40) and 591.6 (28, 41) `superseded_by`. No page `estimate-hi-takes-a-saved-plan`, `estimate-spec-box-runs-a-saved-plan` or `estimate-spec-box-refuses-a-stale-plan` was written. `rule-case-check` got one History line from 589.2 and nothing else. `rule-spec-box` holds `parent: "[[rule-end-of-work]]"`; `rule-end-of-work` holds `rule-spec-box` last in `children`; `make lint` printed no orphan line.
- Index check: the yaml holds no `create` outside `estimates`; no Grep ran, the yaml was not edited.
- Synthesis: the yaml holds no `lesson` entry; no Grep ran, no entry was added.
- `generate`: 82 pages written or changed from the 1202 yaml, 0 from the 1237, 1441 and 1725 yamls.
- Pages, decisions: 31 created (587, 588, 588.1–588.3, 589, 589.1, 589.2, 590, 590.1–590.3, 591, 591.1–591.12, 592, 593, 593.1–593.3, 594). 1 updated by a Case (`decision-case-13`, 591.11, the code fence of When closed). 12 superseded and moved by `generate` and `cleanup` to `archive/migration/2026-10-02/1202/decisions/`: 207, 219, 232, 481, 532, 540, 565, 586, 590.1, 591.2, 591.5, 591.6.
- Pages, rules: 14 updated by Cases (`rule-lint`, `rule-materialize`, `rule-case-check`, `rule-context-size`, `rule-carry-over`, `rule-spec-capture`, `rule-end-of-work`, `rule-work-mode`, `rule-retro`, `rule-handoff`, `rule-where-to-stop`, `rule-ledger-write`, `rule-skill-hi`, `rule-spec-box`). 1 placeholder created (`rule-ledger-line-withdrawn-on-re-ratification`, deferred by 594). 2 deleted and moved to `archive/migration/2026-10-02/1202/rules/` (`rule-prespec-script-skips-code-spans`, `rule-turn-start-one-judgment`). Cascade: `rule-context-size`, `rule-language`, `rule-lint`, `rule-materialize`, `rule-skill-hi`, `rule-spec-capture`, `rule-where-to-stop` built → draft; `rule-prespec` draft → built.
- Pages, estimates: 5 created (`estimate-lint-runs-every-step`, `estimate-ledger-write-names-the-kind-of-a-user-record`, `estimate-hi-takes-a-conserved-spec`, `estimate-spec-box-runs-a-conserved-spec`, `estimate-spec-box-refuses-a-stale-spec`); 15 updated by Cases; 2 readings, both `passed`.
- Pages, entities: 1 updated (`entity-sprint-migration`, 593.2). Insights, lessons: none.
- `cleanup` moved 14 pages. Render wrote `.claude/skills/box/SKILL.md` (new), `.claude/skills/carry/`, `handoff/`, `hi/`, `retro/`, `work/` `SKILL.md` and `vault/wiki/where-to-stop.md`; `CLAUDE.md` and `guppi.toml` unchanged. `backlog.md` changed; `sprint.md` and `glossary.md` unchanged. The run ticked 46 boxes of `raw/2026-10-02/1202/spec.md` and 2 `read` boxes of `raw/2026-10-01/1441/spec.md`; `log.md` 142 lines added.
- Archive: `guppi archive` moved `raw/2026-10-01/1237`, `1441` and `1725` to `archive/migration/2026-10-01/<HHMM>/raw`; no stderr line. `raw/2026-10-02/1202`, the session of the run, stays.

## Readings due

0 Estimates `failed`, 40 `pending` (the 40 `unread` lines of `make lint`). Every target named below stands `draft`.

- `estimate-lint-runs-every-step` — `rule-lint` (draft) — spec 1202: by hand at the Baseline of the first `/work` of a later session whose backlog step is red
- `estimate-estimates-schema-checked` — `rule-estimates-schema` (draft) — spec 1202: in a later session, `uv run pytest tests/test_schemas.py -k estimate` on the live schema, and the live reading `make lint`, no schema finding on `wiki/estimates/`
- `estimate-materialize-changes-a-named-part-alone` — `rule-materialize` (draft) — spec 1202: in a later session, `uv run pytest tests/test_materialize.py`
- `estimate-materialize-lifts-when-and-then` — `rule-materialize` (draft) — spec 1202: in a later session, `uv run pytest tests/test_materialize.py` on a temp Spec
- `estimate-language-spec-prose-in-english` — `rule-language` (draft) — spec 1202: in a later session, `uv run pytest tests/test_prespec.py -k script`
- `estimate-case-check-refuses-a-letter-outside-the-script` — `rule-case-check` (draft) — spec 1202: in a later session, `uv run pytest tests/test_casecheck.py -k script`
- `estimate-context-size-shown-after-each-reply` — `rule-context-size` (draft) — spec 1202: in a later session, `uv run pytest tests/test_context.py`
- `estimate-case-check-refuses-text-before-a-round` — `rule-case-check` (draft) — spec 1202: in a later session, `uv run pytest tests/test_casecheck.py -k round`
- `estimate-carry-over-writes` — `rule-carry-over` (draft) — spec 1202: by hand, at the first `/carry` of a later session
- `estimate-spec-capture-offers-the-fork` — `rule-spec-capture` (draft) — spec 1202: `uv run pytest tests/test_spec.py -k 'fork or box'`, and by hand at the first `ExitPlanMode` of a session that took a conserved Spec
- `estimate-end-of-work-order` — `rule-end-of-work` (draft) — spec 1202: `make test-end-of-work`, and by hand at the close of the first session that `/box` runs
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `rule-work-mode` (draft) — spec 1202: by hand, in a later session, the first `/work` that `/box` calls among them
- `estimate-retro-loads` — `rule-retro` (draft) — spec 1202: by hand, at the first `/retro` of a session that `/box` runs
- `estimate-handoff-dispatches` — `rule-handoff` (draft) — spec 1202: by hand, at the `/handoff` of the first session that `/box` runs
- `estimate-where-to-stop-stops-only-on-its-conditions` — `rule-where-to-stop` (draft) — spec 1202: by hand, at the first run of `/box`
- `estimate-work-mode-takes-the-work-readings` — `rule-work-mode` (draft) — spec 1202: by hand, at the first `/work` that `/box` calls
- `estimate-ledger-write-names-the-kind-of-a-user-record` — `rule-ledger-write` (draft) — spec 1202: in a later session, `uv run pytest tests/test_ledger.py -k kind`
- `estimate-hi-takes-a-conserved-spec` — `rule-skill-hi` (draft) — spec 1202: by hand, at the first session that takes a conserved Spec at the Frontier
- `estimate-spec-box-runs-a-conserved-spec` — `rule-spec-box` (draft) — spec 1202: by hand, at the first session that runs a conserved Spec by `/box`
- `estimate-spec-box-refuses-a-stale-spec` — `rule-spec-box` (draft) — spec 1202: `uv run pytest tests/test_box.py`, in a later session
- `estimate-ask-finds` — `rule-ask` (draft) — method: by hand in a later session, three dispatches of `ask-guppi`, one existing page asked in English and in Russian, one proposal that crosses a known rule, each read against the event log
- `estimate-case-build-writes-the-case` — `rule-case-build` (draft) — method: by hand, live dispatches in a session after the render — one item with a fork, one Case with a `create` without a `ref`, one that changes a hook
- `estimate-case-check-requires-each-question-of-the-rounds` — `rule-case-check` (draft) — method: `pytest tests/test_casecheck.py -k rounds` over a temp agent transcript; then by hand the first Case the hook sends back for a missing title
- `estimate-case-check-shows-only-the-checked-case` — `rule-case-check` (draft) — method: `uv run pytest tests/test_casecheck.py -k stop`, then by hand the first reply the hook refuses
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` (draft) — method: by hand, the ledger and the preview of the first session where a lesson and the Case that closes its cause stand together, and of the first Case that takes up a decision with more than one Case in its `deferred_by`
- `estimate-compact-recall-reloads` — `rule-compact-recall` (draft) — method: `pytest tests/test_recall.py` on a temp project; live, the first compaction of a working session, by hand
- `estimate-event-log-records` — `rule-event-log` (draft) — method: pytest in `tests/test_event.py` and `tests/test_gate.py`; the git-ignore and timing readings once by hand; one `/hi` outside plan mode and one in it
- `estimate-generate-rewords` — `rule-page-generation` (draft) — method: `pytest tests/test_generate.py`; the live reading the librarian's run that applies the first reword — this run: the 1202 yaml holds 0 entries with `reword`; `generate` printed no `reworded` line
- `estimate-handoff-holds-each-fact-once` — `rule-handoff` (draft) — method: one reading by hand at the first `/handoff` after the render, against the close of its Retro
- `estimate-ledger-write-lifts` — `rule-ledger-write` (draft) — method: pytest in `tests/test_ledger.py` and `tests/test_gate.py`; by hand once, the ledger of the first session whose reply that ends Retro follows a refusal of a Stop hook in the same stretch
- `estimate-plan-mode-verified` — `rule-plan-mode` (draft) — method: `make test-plan-mode`; the flagging one live reading by hand
- `estimate-retro-onward-sends-the-agent-to-the-handoff` — `rule-retro-onward` (draft) — method: `uv run pytest tests/test_onward.py`; by hand at the first end of Retro after the render that follows a refusal of another Stop hook in the same stretch
- `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — `rule-retro` (draft) — method: by hand at the first `/retro` after the render in a session whose `work.md` names a check under Expected red
- `estimate-retro-runs-on-to-the-handoff` — `rule-retro` (draft) — method: by hand at the first run from `/work` to the librarian after the render
- `estimate-session-start-context` — `rule-session-start` (draft) — method: `make test-session-start`; by hand, one session opened without `/hi`, and the ledger of the next working session after its first ratification
- `estimate-spec-write-reaches-the-approved-spec` — `rule-spec-write` (draft) — method: `uv run pytest tests/test_ratified.py -k approved_spec`; by hand, the first Case ratified in Work Mode after the change
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` (draft) — method: one reading of the tree by hand at the close of the sprint
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` (draft) — method: `make lint`, exit 0, or only unread lines on the Estimates of `entity-sprint-migration`
- `estimate-sprint-migration-merges` — `entity-sprint-migration` (draft) — method: `make test` on the last commit of `migration`, then `git log` of `main` after the merge
- `estimate-synthesis-clusters` — `rule-synthesis` (draft) — method: one reading by hand of the yaml and the report after a live librarian run whose yaml holds at least two lesson entries — this run: the 1202 yaml holds 0 lesson entries; no synthesis Grep ran; no entry was added

## Flags

- `incomplete` (criterion), all `superseded_by` and not applied: line 11 `estimate-ledger-write-names-the-kind-of-a-user-record` (590.1), line 20 `estimate-hi-takes-a-saved-plan` (591.2), line 27 `estimate-spec-box-runs-a-saved-plan` (591.5), line 28 `estimate-spec-box-refuses-a-stale-plan` (591.6), lines 39, 40, 41 `estimate-hi-takes-a-conserved-spec`, `estimate-spec-box-runs-a-conserved-spec`, `estimate-spec-box-refuses-a-stale-spec` (591.2, 591.5, 591.6). The pages stand whole from the entries of 592, 593.1, 593.2 and 593.3.
- `failed`: none. `near`: none. `unparsed`: none. Failed Estimates: none.
- `generate` stderr: `rule-work-mode: line 42 repeats line 29 of case 591.7; nothing applied`. Line 42 is the re-ratification line of 591.7 with `{supersedes:case 540}`; the yaml marks it `applied`; `log.md` records `decision-case-540 superseded by decision-case-591.7`.
- `cleanup`, `render`, `sprint`, `backlog`, `glossary`: no stderr line.
- MOC candidates: none printed. Contradictions: none found.
- Stale defers, from `make lint`: `rule-subagent-guppi` deferred 31 times since case 29; `rule-orchestration` 3 times since case 424; `rule-case-rebuild-cost` 2 times since case 566; `rule-complaint-becomes-a-lesson` 1 time since case 504; `rule-morph` 1 time since case 239; `rule-ledger-line-withdrawn-on-re-ratification` 1 time since case 594.
- `make lint` exit 2: `guppi render --check`, `sprint --check`, `backlog --check`, `glossary --check` exit 0; `guppi lint` printed 46 lines — 6 `deferred`, 40 `unread: pending`. No `fence` line on `decision-case-13`, no schema or orphan line on `rule-spec-box`.
- Reads outside the frame's need: none.

## Next session

Cases
- The close of the sprint (Slice 5) and `rule-orchestration` were put off at the end of Plan Mode with no Case, as a sprint item and a backlog item kept (handoff, For the next session).

Work
- Readings `pending`: `estimate-lint-runs-every-step`, `estimate-estimates-schema-checked`, `estimate-materialize-changes-a-named-part-alone`, `estimate-materialize-lifts-when-and-then`, `estimate-language-spec-prose-in-english`, `estimate-case-check-refuses-a-letter-outside-the-script`, `estimate-context-size-shown-after-each-reply`, `estimate-case-check-refuses-text-before-a-round`, `estimate-carry-over-writes`, `estimate-spec-capture-offers-the-fork`, `estimate-end-of-work-order`, `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, `estimate-retro-loads`, `estimate-handoff-dispatches`, `estimate-where-to-stop-stops-only-on-its-conditions`, `estimate-work-mode-takes-the-work-readings`, `estimate-ledger-write-names-the-kind-of-a-user-record`, `estimate-hi-takes-a-conserved-spec`, `estimate-spec-box-runs-a-conserved-spec`, `estimate-spec-box-refuses-a-stale-spec`, `estimate-ask-finds`, `estimate-case-build-writes-the-case`, `estimate-case-check-requires-each-question-of-the-rounds`, `estimate-case-check-shows-only-the-checked-case`, `estimate-case-protocol-ledger-line-form`, `estimate-compact-recall-reloads`, `estimate-event-log-records`, `estimate-generate-rewords`, `estimate-handoff-holds-each-fact-once`, `estimate-ledger-write-lifts`, `estimate-plan-mode-verified`, `estimate-retro-onward-sends-the-agent-to-the-handoff`, `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`, `estimate-retro-runs-on-to-the-handoff`, `estimate-session-start-context`, `estimate-spec-write-reaches-the-approved-spec`, `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges`, `estimate-synthesis-clusters`
- Unticked box of `raw/2026-10-02/1202/spec.md` line 930: by hand, `make lint` after the librarian's run of this session prints no `fence` line on `decision-case-13` — this run's `make lint` printed none.

Ask the person
- none

## Readings at the close

- `make test`: 1074 passed, 6 skipped.
- `make lint`: exit 2; 46 lines of `guppi lint` (6 `deferred`, 40 `unread`); the other four steps exit 0.
- Pages in `vault/wiki/`: decisions 954, rules 76, estimates 188, lessons 75, insights 29, entities 4. `vault/archive/`: 698 `.md` files after `guppi archive`.
