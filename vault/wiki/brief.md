# Brief — 2026-10-02, session 2049: the onward hook after a ledger refusal, joint ratification

## Where things stand

- Ratified (handoff): 596 (596.1, 596.2, 596.3), 597 (597.1, 597.2), 598 (598.1, 598.2, 598.3), 599, 600.
- Code (handoff): `guppi/ledger.py` (`stretch` and `refusals`, `own_refusals` kept on top of them), `guppi/onward.py` (`spent`, `told` per command, `stretch_replies`, `last_decisions` over the replies of the stretch, the `--plan` run guarded by `spent`). Tests: `tests/test_ledger.py` (one test), `tests/test_onward.py` (twelve tests, one renamed). `make test` 1088 passed, 6 skipped; `make style` clean.
- Readings (handoff): ledger lines 1–7 (at /hi), 22–24, 28–30 — 11 `passed`, 2 `failed` (`estimate-skill-grill-me-asks-in-rounds`, `estimate-orchestration-shows-the-built-case`). Lessons: ledger lines 25 and 31.
- Yaml: `raw/2026-10-02/2049/materialize.yaml`, 31 entries from `materialize` (16 decision lines — 2 `create`, 14 `update`; 13 `estimate`; 2 `lesson`), none added by the librarian. 0 `failed`, 0 `incomplete`, 0 `exists`; `unparsed` empty. The ledger has 31 lines, each held by an entry of the yaml (lines 1 to 31). `raw/2026-10-02/1202/materialize.yaml` and `raw/2026-10-02/1834/materialize.yaml` extended with 0 entries.
- `generate`: 52 pages written or changed from the 2049 yaml, 0 from the 1202 and 1834 yamls.
- Index check: no `create` outside `estimates` but the two lessons. Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, 76 lines: no lesson with the same root cause as either new lesson; no merge, no `near`.
- Synthesis: two lesson entries. Greps `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, 76 lines, and `^(pattern|deferred_by):` over `vault/wiki/insights/`, 31 lines. No index line of the insights names the onward hook. Both lessons stay `new`; no entry added.
- Pages, decisions: 13 created (596, 596.1–596.3, 597, 597.1, 597.2, 598, 598.1–598.3, 599, 600). `decision-case-575` superseded by 597.2 and moved to `archive/migration/2026-10-02/2049/decisions/`; the `deferred_by` of `rule-prespec-onward` is gone.
- Pages, rules: 4 updated by Cases (`rule-retro-onward`, `rule-retro`, `rule-prespec-onward`, `rule-orchestration`). Cascade: `rule-atomicity`, `rule-case-protocol`, `rule-claude-md`, `rule-context-size`, `rule-internal-context` draft → built; `rule-prespec-onward` built → draft.
- Pages, estimates: 2 created (`estimate-prespec-onward-reads-the-decisions-of-the-stretch`, `estimate-orchestration-signs-a-batch-together`); 6 updated by Cases and set `pending`; 13 readings.
- Pages, insights: 2 updated to `actioned` (`insight-prespec-main-agent-question-off-the-grill-me-shape` by `decision-case-561.13`, `insight-prespec-after-findings-loop-unruled` by `decision-case-561.1`); their 4 clustered lessons moved by the cascade and `cleanup` to `archive/migration/2026-10-02/2049/lessons/`. Lessons: 2 created.
- `cleanup` moved 5 pages. The render wrote `vault/wiki/orchestration.md` and `.claude/skills/retro/SKILL.md`, neither holds `{{`; `guppi render --check` exit 0; `CLAUDE.md` and `guppi.toml` unchanged. `backlog.md` 24 → 21 items (`rule-prespec-onward` and the two actioned Insights gone); `sprint.md` and `glossary.md` unchanged.
- Spec boxes ticked by this run: 19 of `raw/2026-10-02/2049/spec.md`, 12 `read` boxes of `raw/2026-10-02/1834/spec.md`, 1 `read` box of `raw/2026-10-02/1202/spec.md`. `log.md` 64 lines added.
- Archive: `guppi archive` printed no line and moved nothing; it looks only at units dated before the day of the run, so `raw/2026-10-02/1202`, `raw/2026-10-02/1834` and `raw/2026-10-02/2049`, the session of the run, stay. No `pending` Estimate's `method` names the archive step.

## Readings due

2 Estimates `failed`, 40 `pending` (the 42 `unread` lines of `make lint`). Every target named below stands `draft`. The `read` lines of `raw/2026-10-02/2049/spec.md` name no place, so each line gives the page's `method`.

- `estimate-skill-grill-me-asks-in-rounds` (failed) — `rule-skill-grill-me` (draft) — result: the round of case-guppi on Case 599 opened its question with `❓ **Q1** - **…**` with no colon after the title, against the numbered title line the Criterion sets — method: `uv run guppi render --check`; by hand, one round read in the chat in a session after the render
- `estimate-orchestration-shows-the-built-case` (failed) — `rule-orchestration` (draft) — result: the showing of the round on Case 599 opened its question with a title line without the colon after the bold title, as the answer held it — method: by hand, the Cases of a session at its close, against the Agent, SendUserFile, Skill and SendMessage calls of the transcript
- `estimate-retro-onward-sends-the-agent-to-the-handoff` — `rule-retro-onward` (draft) — method: `uv run pytest tests/test_onward.py tests/test_ledger.py`; by hand at the first end of Retro at which the ledger hook refuses a line
- `estimate-retro-runs-on-to-the-handoff` — `rule-retro` (draft) — method: by hand at the first run from `/work` to the librarian after the render, and for the answer to a refusal of the ledger hook at the first Retro where that hook refuses a line
- `estimate-retro-onward-exits-2-on-an-error` — `rule-retro-onward` (draft) — method: `uv run pytest tests/test_onward.py`, piped payloads, a function of the hook patched to raise
- `estimate-prespec-onward-sends-the-agent-on` — `rule-prespec-onward` (draft) — method: `uv run pytest tests/test_onward.py tests/test_ledger.py`; by hand at the first Plan Mode at which the ledger hook refuses a line of the reply that acknowledges the last ratification
- `estimate-prespec-onward-reads-the-decisions-of-the-stretch` — `rule-prespec-onward` (draft) — method: `uv run pytest tests/test_onward.py`; by hand at the first re-ratification in Plan Mode after the change
- `estimate-orchestration-signs-a-batch-together` — `rule-orchestration` (draft) — method: by hand at the first Plan Mode of a later session after the render in which the person's word asks that a ratified Case change
- `estimate-orchestration-acknowledging-reply` — `rule-orchestration` (draft) — method: one reading by hand of the first acknowledging reply of a session, and of the first reply that acknowledges Cases ratified together in one answer
- `estimate-prespec-gathers-the-answers-after-findings` — `rule-prespec` (draft) — method: by hand at the `/pre-spec` of a later session after the render whose report asks the person a question and sends findings to two or more `case-guppi`
- `estimate-orchestration-asks-in-the-grill-me-shape` — `rule-orchestration` (draft) — method: by hand at the close of a later session, each question of the main agent's own read in the transcript
- `estimate-orchestration-defers-in-one-reply` — `rule-orchestration` (draft) — method: by hand, the first defer the person asks for after the render that leaves no line under `## Cases` of `frontier.md` open
- `estimate-orchestration-forwards-a-discussion-question` — `rule-orchestration` (draft) — method: by hand in a later session, the first such question, the SendMessage call, the main agent's tool calls and the answer in the transcript
- `estimate-case-build-writes-the-case` — `rule-case-build` (draft) — method: by hand, live dispatches in a session after the render — one item with a fork, one Case with a `create` without a `ref`, one that changes a hook; tokens and seconds of each dispatch
- `estimate-ratification-ledger-line-form` — `rule-ratification` (draft) — method: by hand, the ledger and the preview of the first session where a lesson and the Case that closes its cause stand together, and of the first Case that takes up a decision with more than one Case in its `deferred_by`
- `estimate-spec-capture-offers-the-fork` — `rule-spec-capture` (draft) — method: `uv run pytest tests/test_spec.py -k 'fork or box'`; by hand, the first ExitPlanMode of a session after the render, and the first of a session that took a conserved Spec
- `estimate-ask-finds` — `rule-ask` (draft) — method: by hand in a later session, three dispatches of `ask-guppi`, each read against the event log
- `estimate-carry-over-writes` — `rule-carry-over` (draft) — method: `uv run guppi render --check`; by hand, the first `/carry` after the fork of ExitPlanMode
- `estimate-case-check-refuses-text-before-a-round` — `rule-case-check` (draft) — method: `uv run pytest tests/test_casecheck.py -k round`; by hand in a later session, the first rounds of `case-guppi` shown before and after pre-spec
- `estimate-case-check-requires-each-question-of-the-rounds` — `rule-case-check` (draft) — method: `pytest tests/test_casecheck.py -k rounds` over a temp agent transcript; then by hand the first Case the hook sends back for a missing title
- `estimate-compact-recall-reloads` — `rule-compact-recall` (draft) — method: `pytest tests/test_recall.py` on a temp project; live, the first compaction of a working session, by hand
- `estimate-end-of-work-order` — `rule-end-of-work` (draft) — method: `make test-end-of-work`, plus by hand at the close of a later session
- `estimate-event-log-records` — `rule-event-log` (draft) — method: pytest in `tests/test_event.py` and `tests/test_gate.py`; the git-ignore and timing readings once by hand; one `/hi` outside plan mode and one in it
- `estimate-generate-rewords` — `rule-page-generation` (draft) — method: `pytest tests/test_generate.py`; the live reading the librarian's run that applies the first reword — this run: the 2049 yaml holds 0 entries with `reword`; `generate` printed no `reworded` line
- `estimate-handoff-dispatches` — `rule-handoff` (draft) — method: by hand at the `/handoff` of a later session and of the first session that `/box` runs
- `estimate-handoff-holds-each-fact-once` — `rule-handoff` (draft) — method: one reading by hand at the first `/handoff` after the render, against the close of its Retro
- `estimate-hi-takes-a-conserved-spec` — `rule-skill-hi` (draft) — method: `uv run guppi render --check`; by hand, at the first session whose person takes a conserved Spec at the Frontier
- `estimate-ledger-write-lifts` — `rule-ledger-write` (draft) — method: pytest in `tests/test_ledger.py` and `tests/test_gate.py`; by hand once, the ledger of the first session whose reply that ends Retro follows a refusal of a Stop hook in the same stretch
- `estimate-lint-runs-every-step` — `rule-lint` (draft) — method: by hand, the `make lint` of the Baseline of the first `/work` of a later session whose backlog step is red
- `estimate-plan-mode-verified` — `rule-plan-mode` (draft) — method: `make test-plan-mode`; the flagging one live reading by hand
- `estimate-retro-loads` — `rule-retro` (draft) — method: one reading by hand at the first `/retro`, and one at the first `/retro` of a session that `/box` runs
- `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — `rule-retro` (draft) — method: by hand at the first `/retro` after the render in a session whose `work.md` names a check under Expected red
- `estimate-session-start-context` — `rule-session-start` (draft) — method: `make test-session-start`; by hand, one session opened without `/hi`, and the ledger of the next working session after its first ratification
- `estimate-spec-box-runs-a-conserved-spec` — `rule-spec-box` (draft) — method: `uv run guppi render --check`; by hand, the first session that takes a conserved Spec at the Frontier and runs it by `/box`
- `estimate-spec-write-reaches-the-approved-spec` — `rule-spec-write` (draft) — method: `uv run pytest tests/test_ratified.py -k approved_spec`; by hand, the first Case ratified in Work Mode after the change
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` (draft) — method: one reading of the tree by hand at the close of the sprint
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` (draft) — method: `make lint`, exit 0, or only unread lines on the Estimates of `entity-sprint-migration`
- `estimate-sprint-migration-merges` — `entity-sprint-migration` (draft) — method: `make test` on the last commit of `migration`, then `git log` of `main` after the merge
- `estimate-synthesis-clusters` — `rule-synthesis` (draft) — method: one reading by hand of the yaml and the report after a live librarian run whose yaml holds at least two lesson entries — this run: the 2049 yaml holds 2 lesson entries (lines 25 and 31); the synthesis ran `^(root_cause|deferred_by):` over `vault/wiki/lessons/` (76 lines) and `^(pattern|deferred_by):` over `vault/wiki/insights/` (31 lines); it added 0 entries; both lessons stand `new`; the report names both Greps and the outcome of each lesson
- `estimate-where-to-stop-stops-only-on-its-conditions` — `rule-where-to-stop` (draft) — method: by hand at the first run from `/work` to the librarian after the render, and at the first run of `/box`
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `rule-work-mode` (draft) — method: `uv run guppi render --check`; by hand, in a session after the render, the first `/work` the agent calls at the fork, the first the person types and the first that `/box` calls
- `estimate-work-mode-takes-the-work-readings` — `rule-work-mode` (draft) — method: by hand at the first `/work` after the render and at the first `/work` that `/box` calls

## Flags

- `incomplete`: none. `failed`: none. `near`: none. `unparsed`: none.
- Failed Estimates: `estimate-skill-grill-me-asks-in-rounds`, `estimate-orchestration-shows-the-built-case`; both rest on the one question line without its colon in the round on Case 599 (handoff).
- `materialize`, `generate`, `cleanup`, `render`, `sprint`, `backlog`, `glossary`, `archive`: no stderr line.
- MOC candidates: none printed. Contradictions: none found.
- The defer of case 575 is retired by 597.2 (`decision-case-575` archived, `rule-prespec-onward` has no `deferred_by`), while `lesson-prespec-onward-re-ratification-out-after-its-stretch` records a re-ratification with unchanged lines that stays out once the stretch has passed; the lesson stands `new`, with no Insight.
- Stale defers, from `make lint`: `rule-subagent-guppi` deferred 31 times since case 29; `rule-case-rebuild-cost` 2 times since case 566; `rule-complaint-becomes-a-lesson` 1 time since case 504; `rule-morph` 1 time since case 239; `rule-ledger-line-withdrawn-on-re-ratification` 1 time since case 594.
- `make lint` exit 2: `guppi lint` printed 47 lines — 5 `deferred`, 40 `unread: pending`, 2 `unread: failed`; no other step printed a line.
- Handoff observation: no test covers `rename` of `guppi/generate.py` leaving the status of an Estimate alone.
- Handoff observation: the harness marked the answers of `case-guppi` and of `ask-guppi` as instruction-shaped (pattern `settings-json`) at each answer whose text named `.claude/settings.json`.
- Reads outside the frame's need: none.

## Next session

Cases
- The close of the sprint (Slice 5), left on the sprint page again (handoff, For the next session).
- Whether `guppi onward --plan` should count a re-ratification across the whole session, not only within its stretch (handoff, For the next session; `lesson-prespec-onward-re-ratification-out-after-its-stretch`).
- Whether the round check of `rule-case-check` should refuse a question line that opens `❓ **Qn** - **…**` without the colon (handoff, For the next session; `lesson-case-check-question-line-without-colon-unseen`).
- Who ticks a `by hand` box of an earlier session's Spec that a later /hi reads, or whether such a box should leave the brief (handoff, For the next session).
- `estimate-skill-grill-me-asks-in-rounds` failed (ledger line 24).
- `estimate-orchestration-shows-the-built-case` failed (ledger line 30).

Work
- Reading `estimate-retro-onward-sends-the-agent-to-the-handoff`
- Reading `estimate-retro-runs-on-to-the-handoff`
- Reading `estimate-retro-onward-exits-2-on-an-error`
- Reading `estimate-prespec-onward-sends-the-agent-on`
- Reading `estimate-prespec-onward-reads-the-decisions-of-the-stretch`
- Reading `estimate-orchestration-signs-a-batch-together`
- Reading `estimate-orchestration-acknowledging-reply`
- Reading `estimate-prespec-gathers-the-answers-after-findings`
- Reading `estimate-orchestration-asks-in-the-grill-me-shape`
- Reading `estimate-orchestration-defers-in-one-reply`
- Reading `estimate-orchestration-forwards-a-discussion-question`
- Reading `estimate-case-build-writes-the-case`
- Reading `estimate-ratification-ledger-line-form`
- Reading `estimate-spec-capture-offers-the-fork`
- Reading `estimate-ask-finds`
- Reading `estimate-carry-over-writes`
- Reading `estimate-case-check-refuses-text-before-a-round`
- Reading `estimate-case-check-requires-each-question-of-the-rounds`
- Reading `estimate-compact-recall-reloads`
- Reading `estimate-end-of-work-order`
- Reading `estimate-event-log-records`
- Reading `estimate-generate-rewords`
- Reading `estimate-handoff-dispatches`
- Reading `estimate-handoff-holds-each-fact-once`
- Reading `estimate-hi-takes-a-conserved-spec`
- Reading `estimate-ledger-write-lifts`
- Reading `estimate-lint-runs-every-step`
- Reading `estimate-plan-mode-verified`
- Reading `estimate-retro-loads`
- Reading `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`
- Reading `estimate-session-start-context`
- Reading `estimate-spec-box-runs-a-conserved-spec`
- Reading `estimate-spec-write-reaches-the-approved-spec`
- Reading `estimate-sprint-migration-leftovers-gone`
- Reading `estimate-sprint-migration-lint-clean`
- Reading `estimate-sprint-migration-merges`
- Reading `estimate-synthesis-clusters`
- Reading `estimate-where-to-stop-stops-only-on-its-conditions`
- Reading `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
- Reading `estimate-work-mode-takes-the-work-readings`
- Unticked box of `raw/2026-10-02/1202/spec.md` line 930: by hand, `make lint` after the librarian's run of session 1202 prints no `fence` line on `decision-case-13` — this run's `make lint` printed none.

Ask the person
- none

## Readings at the close

- `make test`: 1088 passed, 6 skipped.
- `make lint`: exit 2; 47 lines of `guppi lint` (5 `deferred`, 40 `unread: pending`, 2 `unread: failed`); no other step printed a line.
- Pages in `vault/wiki/`: decisions 987, rules 78, estimates 193, lessons 75, insights 30, entities 5. `vault/archive/`: 705 `.md` files after `guppi archive`.
