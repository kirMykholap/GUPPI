# Brief — 2026-10-02, session 2300: the round check, the synthesis report, by hand boxes, the onward reading

## Where things stand

- Ratified (handoff): 601 (601.1, 601.2, 601.3, 601.4, 601.5), 602, 604, 605, 606 (606.1, 606.2). Cases 603, 603.1 and 603.2 are superseded by 606.1 and 606.2.
- Code (handoff): `guppi/casecheck.py` (`is_round` the one test of a round, by the mark `❓`; new `round_form`, `option_with_after`, `faulty_round`, `subagent_outputs`, `spaces_aside`, `send_back`; `subagent` sends back a round out of form once per text; `round_titles` skips a round out of form), `guppi/onward.py` (`transcript_replies` replaces `stretch_replies`). Tests: `tests/test_casecheck.py` (13 new), `tests/test_onward.py` (1 new). `make test` 1102 passed, 6 skipped; `make style` clean. One-off of 606.2: the box of Case 591.11 in `raw/2026-10-02/1202/spec.md` ticked.
- Readings (handoff): ledger line 1 (`estimate-synthesis-clusters` `failed`, at /hi), lines 22–26 (five `passed`). Lessons: ledger lines 27 and 28.
- Yaml: `raw/2026-10-02/2300/materialize.yaml`, 28 entries from `materialize` (21 decision lines — 1 `create`, 20 `update`; 6 `estimate`; 2 `lesson`), 2 added by the librarian (synthesis). 0 `failed`, 0 `incomplete`, 0 `exists`; no `unparsed`. 5 entries carry `superseded_by` (ledger lines 8, 9, 15, 16 by 606.1; line 17 by 606.2) and were not applied. The ledger has 28 lines, each held by an entry of the yaml (lines 1 to 28). The yamls of 1202, 1834 and 2049 extended with 0 entries.
- `generate`: 42 pages written or changed from the 2300 yaml, 0 from the 1202, 1834 and 2049 yamls.
- Index check: the only `create` outside `estimates` are the two lessons. Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, 73 lines. `lesson-spec-write-keeps-the-body-of-case-603-split-at-prespec` has the root cause of `lesson-spec-write-keeps-the-body-of-a-case-that-gains-sub-cases` and `lesson-spec-write-keeps-the-body-of-a-case-rebuilt-as-a-parent`, on a different trigger (Case 603, session 2300): marked `near: lesson-spec-write-keeps-the-body-of-a-case-that-gains-sub-cases`. `lesson-orchestration-own-fork-frames-the-symptom`: no lesson with the same root cause; no merge.
- Synthesis: Greps `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, 73 lines, and `^(pattern|deferred_by):` over `vault/wiki/insights/`, 31 lines.
  - `lesson-spec-write-keeps-the-body-of-case-603-split-at-prespec` — joined `insight-spec-write-parent-body-kept-on-re-ratification` (status `open`, `deferred_by` case 585, kept): an `update` of the Insight adding the child and an `update` of the lesson to `clustered`, both `librarian: synthesis`.
  - `lesson-orchestration-own-fork-frames-the-symptom` — none: no index line of either Grep names the main agent offering its own fork before `case-guppi` reads the frame. Stays `new`.
- Pages, decisions: 15 created (601, 601.1–601.5, 602, 603, 603.1, 603.2, 604, 605, 606, 606.1, 606.2); 603, 603.1 and 603.2 marked superseded and moved to `archive/migration/2026-10-03/2300/decisions/`; no `decision-case-603*` page stands under `vault/wiki/decisions/`. `decision-case-13` updated (606.2). The rename of Case 604 changed `decision-case-597` and `decision-case-597.2`.
- Pages, rules: 4 updated by Cases (`rule-case-check`, `rule-synthesis`, `rule-prespec-onward`, `rule-case-protocol`). `rule-case-protocol` holds the sentence of 606.1 once and one History line from 606.1. `rule-prespec-onward` `estimates` names `estimate-prespec-onward-reads-the-decisions-of-the-session`. Cascade: `rule-case-protocol` built → draft, `rule-prespec` draft → built.
- Pages, estimates: 1 created (`estimate-case-check-sends-back-a-faulty-round`, in `rule-case-check` `estimates`); 7 updated by Cases and set `pending` (`estimate-case-check-sends-back-a-faulty-case`, `estimate-case-build-writes-the-case`, `estimate-synthesis-clusters`, `estimate-case-check-refuses-text-before-a-round`, `estimate-case-check-requires-each-question-of-the-rounds`, `estimate-case-protocol-case-form` with one History line from 606.1, `estimate-prespec-onward-reads-the-decisions-of-the-stretch` renamed to `estimate-prespec-onward-reads-the-decisions-of-the-session`); 6 readings (1 `failed`, then set `pending` by case 602; 5 `passed`).
- Pages, insights: 2 updated. `insight-case-form-chat-form-read-by-no-script` `actioned`, `addressed_by` `decision-case-601.1` (log order: `decision-case-601.1` created before the Insight's update), severity 1 → 0. `insight-spec-write-parent-body-kept-on-re-ratification` child added by synthesis, severity 2 → 3.
- Pages, lessons: 2 created; 2 updated to `clustered` (`lesson-case-check-question-line-without-colon-unseen` by case 605, `lesson-spec-write-keeps-the-body-of-case-603-split-at-prespec` by synthesis). The cascade moved `lesson-case-check-question-line-without-colon-unseen` and `lesson-case-protocol-own-text-before-a-round` to `archive/migration/2026-10-03/2300/lessons/`.
- `cleanup` moved 5 pages. The render wrote `.claude/agents/librarian-guppi.md` (rule-synthesis, case 602) and `vault/wiki/case-schema.md`; neither holds `{{`; `guppi render --check` exit 0; `CLAUDE.md` and `guppi.toml` unchanged. `backlog.md` 21 → 20 items (`insight-case-form-chat-form-read-by-no-script` gone); `sprint.md` and `glossary.md` unchanged.
- Spec boxes ticked by this run: 17 of `raw/2026-10-02/2300/spec.md`, 4 `read` boxes of `raw/2026-10-02/1834/spec.md`, 2 `read` boxes of `raw/2026-10-02/2049/spec.md`. `log.md` 58 lines added.
- Archive: `guppi archive` moved `raw/2026-10-02/1202`, `raw/2026-10-02/1834` and `raw/2026-10-02/2049` to `archive/migration/2026-10-02/<HHMM>/raw/`; `raw/2026-10-02/2300`, the session of the run, stays. No `pending` Estimate's `method` names the archive step.

## Readings due

2 Estimates `failed`, 38 `pending` (the 40 `unread` lines of `make lint`). Every target named below stands `draft`. Lines with a `read` line in `raw/2026-10-02/2300/spec.md` give it; the others give the page's `method`.

- `estimate-skill-grill-me-asks-in-rounds` (failed) — `rule-skill-grill-me` (draft) — result: the round of case-guppi on Case 599 opened its question with a title line without the colon after the bold title — method: `uv run guppi render --check`; by hand, one round read in the chat in a session after the render
- `estimate-orchestration-shows-the-built-case` (failed) — `rule-orchestration` (draft) — result: the showing of the round on Case 599 opened its question with a title line without the colon, as the answer held it — method: by hand, the Cases of a session at its close, against the Agent, SendUserFile, Skill and SendMessage calls of the transcript
- `estimate-case-check-sends-back-a-faulty-round` — `rule-case-check` (draft) — spec 2300: read `estimate-case-check-sends-back-a-faulty-round` — method: `uv run pytest tests/test_casecheck.py -k round_form`; then by hand the first round the hook sends back live
- `estimate-case-check-sends-back-a-faulty-case` — `rule-case-check` (draft) — spec 2300: read `estimate-case-check-sends-back-a-faulty-case` — method: `uv run pytest tests/test_casecheck.py -k subagent`, then by hand the first answer the hook sends back and the first file of cases/ it writes
- `estimate-case-build-writes-the-case` — `rule-case-build` (draft) — spec 2300: read `estimate-case-build-writes-the-case` — method: by hand, live dispatches in a session after the render
- `estimate-case-check-refuses-text-before-a-round` — `rule-case-check` (draft) — spec 2300: read `estimate-case-check-refuses-text-before-a-round` — method: `uv run pytest tests/test_casecheck.py -k round`; by hand in a later session, the first rounds shown before and after pre-spec
- `estimate-case-check-requires-each-question-of-the-rounds` — `rule-case-check` (draft) — spec 2300: read `estimate-case-check-requires-each-question-of-the-rounds` — method: `pytest tests/test_casecheck.py -k rounds`; then by hand the first Case the hook sends back for a missing title
- `estimate-synthesis-clusters` — `rule-synthesis` (draft) — spec 2300: read `estimate-synthesis-clusters` — by hand, the yaml and the brief after the first live librarian run after the render whose yaml holds at least two lesson entries — this run: the synthesis ran on the frame loaded before the render of case 602; the yaml holds two lesson entries (ledger lines 27 and 28); Greps `^(root_cause|deferred_by):` over lessons/ 73 lines, `^(pattern|deferred_by):` over insights/ 31 lines; `lesson-spec-write-keeps-the-body-of-case-603-split-at-prespec` joined `insight-spec-write-parent-body-kept-on-re-ratification` by an `update` of the Insight (children) and an `update` of the lesson (`clustered`), both `librarian: synthesis`; `lesson-orchestration-own-fork-frames-the-symptom` joined none and stays `new`; pages read at synthesis: `lesson-spec-write-keeps-the-body-of-a-case-that-gains-sub-cases`, `lesson-spec-write-keeps-the-body-of-a-case-rebuilt-as-a-parent`, `insight-spec-write-parent-body-kept-on-re-ratification`, named in the report
- `estimate-prespec-onward-reads-the-decisions-of-the-session` — `rule-prespec-onward` (draft) — spec 2300: read `estimate-prespec-onward-reads-the-decisions-of-the-session` — method: `uv run pytest tests/test_onward.py`; by hand at the first Case ratified again with unchanged decision lines in Plan Mode after the change
- `estimate-case-protocol-case-form` — `rule-case-protocol` (draft) — spec 2300: read `estimate-case-protocol-case-form` — by hand, the Cases of a later session at its close
- `estimate-prespec-onward-sends-the-agent-on` — `rule-prespec-onward` (draft) — method: `uv run pytest tests/test_onward.py tests/test_ledger.py`; by hand at the first Plan Mode at which the ledger hook refuses a line of the reply that acknowledges the last ratification
- `estimate-retro-onward-sends-the-agent-to-the-handoff` — `rule-retro-onward` (draft) — method: `uv run pytest tests/test_onward.py tests/test_ledger.py`; by hand at the first end of Retro at which the ledger hook refuses a line
- `estimate-retro-runs-on-to-the-handoff` — `rule-retro` (draft) — method: by hand at the first run from `/work` to the librarian after the render, and at the first Retro where the ledger hook refuses a line
- `estimate-where-to-stop-stops-only-on-its-conditions` — `rule-where-to-stop` (draft) — method: by hand at the first run from `/work` to the librarian after the render, and at the first run of `/box`
- `estimate-orchestration-signs-a-batch-together` — `rule-orchestration` (draft) — method: by hand at the first Plan Mode of a later session after the render in which the person's word asks that a ratified Case change
- `estimate-orchestration-defers-in-one-reply` — `rule-orchestration` (draft) — method: by hand, the first defer the person asks for after the render that leaves no line under `## Cases` of frontier.md open
- `estimate-ratification-ledger-line-form` — `rule-ratification` (draft) — method: by hand, the ledger and the preview of the first session where a lesson and the Case that closes its cause stand together, and of the first Case that takes up a decision with more than one Case in its `deferred_by`
- `estimate-spec-capture-offers-the-fork` — `rule-spec-capture` (draft) — method: `uv run pytest tests/test_spec.py -k 'fork or box'`; by hand, the first ExitPlanMode of a session after the render, and the first of a session that took a conserved Spec
- `estimate-lint-runs-every-step` — `rule-lint` (draft) — method: by hand, the `make lint` of the Baseline of the first /work of a later session whose backlog step is red
- `estimate-carry-over-writes` — `rule-carry-over` (draft) — method: `uv run guppi render --check`; by hand, the first /carry after the fork of ExitPlanMode
- `estimate-end-of-work-order` — `rule-end-of-work` (draft) — method: `make test-end-of-work`, plus by hand at the close of a later session
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `rule-work-mode` (draft) — method: `uv run guppi render --check`; by hand, the first /work the agent calls at the fork, the first /work the person types and the first /work that /box calls
- `estimate-work-mode-takes-the-work-readings` — `rule-work-mode` (draft) — method: by hand at the first /work after the render and at the first /work that /box calls
- `estimate-retro-loads` — `rule-retro` (draft) — method: by hand at the first /retro, and at the first /retro of a session that /box runs
- `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — `rule-retro` (draft) — method: by hand at the first /retro after the render in a session whose work.md names a check under Expected red
- `estimate-handoff-dispatches` — `rule-handoff` (draft) — method: by hand at the /handoff of a later session and at the /handoff of the first session that /box runs
- `estimate-handoff-holds-each-fact-once` — `rule-handoff` (draft) — method: by hand at the first /handoff after the render, against the close of its Retro
- `estimate-hi-takes-a-conserved-spec` — `rule-skill-hi` (draft) — method: `uv run guppi render --check`; by hand, at the first session whose person takes a conserved Spec at the Frontier
- `estimate-spec-box-runs-a-conserved-spec` — `rule-spec-box` (draft) — method: `uv run guppi render --check`; by hand, the first session that takes a conserved Spec and runs it by /box
- `estimate-spec-write-reaches-the-approved-spec` — `rule-spec-write` (draft) — method: `uv run pytest tests/test_ratified.py -k approved_spec`; by hand, the first Case ratified in Work Mode after the change
- `estimate-ledger-write-lifts` — `rule-ledger-write` (draft) — method: pytest in `tests/test_ledger.py` and `tests/test_gate.py`; by hand, the ledger of the first session whose reply that ends Retro follows a refusal of a Stop hook in the same stretch
- `estimate-generate-rewords` — `rule-page-generation` (draft) — method: `pytest tests/test_generate.py` on a temp vault; the live reading the librarian's run that applies the first reword — this run: no entry of the 2300 yaml carries a `reword`
- `estimate-ask-finds` — `rule-ask` (draft) — method: by hand in a later session: three dispatches of ask-guppi, read against the event log
- `estimate-compact-recall-reloads` — `rule-compact-recall` (draft) — method: `pytest tests/test_recall.py`; live, the first compaction of a working session
- `estimate-event-log-records` — `rule-event-log` (draft) — method: pytest in `tests/test_event.py` and `tests/test_gate.py`; by hand, one /hi outside plan mode and one in it
- `estimate-plan-mode-verified` — `rule-plan-mode` (draft) — method: `make test-plan-mode`; one live reading by hand
- `estimate-session-start-context` — `rule-session-start` (draft) — method: `make test-session-start`; by hand, one session opened without /hi whose reply carries a LEDGER block
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` (draft) — method: one reading of the tree by hand at the close of the sprint
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` (draft) — method: `make lint`, exit 0, or only unread lines on the Estimates of entity-sprint-migration
- `estimate-sprint-migration-merges` — `entity-sprint-migration` (draft) — method: `make test` on the last commit of migration, then git log of main after the merge

## Flags

- `near`: `lesson-spec-write-keeps-the-body-of-case-603-split-at-prespec` near `lesson-spec-write-keeps-the-body-of-a-case-that-gains-sub-cases` (same root cause, another trigger).
- `incomplete`, `failed`, `unparsed`: none in the 2300 yaml. The yamls of 1202 and 1834 still carry `incomplete` marks from earlier runs; this run added no entry to them.
- Failed Estimates: `estimate-skill-grill-me-asks-in-rounds`, `estimate-orchestration-shows-the-built-case` (left `failed` by the person at pre-spec, handoff).
- Stale defers (`make lint`): `rule-subagent-guppi` deferred 31 times since case 29; `rule-case-rebuild-cost` 2 times since case 566; `rule-complaint-becomes-a-lesson` 1 time since case 504; `rule-ledger-line-withdrawn-on-re-ratification` 1 time since case 594; `rule-morph` 1 time since case 239.
- The rename of Case 604 left an unticked box under the old slug: `archive/migration/2026-10-02/2049/raw/spec.md` line 410, `- [ ] read \`estimate-prespec-onward-reads-the-decisions-of-the-stretch\``; no page of that slug stands.
- The rename of Case 604 rewrote the old slug to the new one in `decision-case-597.2` (`create`) and in the body text of `decision-case-597` (a Recommended line).
- MOC candidates, contradictions: none printed by any step of this run.
- `make lint`: exit 2, 45 lines of `guppi lint` — 5 `deferred`, 38 `unread: pending`, 2 `unread: failed`.
- Read the librarian's frame says its job does not need: the `git diff` of `decision-case-597`, `decision-case-597.2` and `decision-case-13` (text of Decision pages), run for the check of the Case 604 rename and of 606.2 that the handoff asked for.

## Next session

Cases:
- The close of the sprint (Slice 5), left on the sprint page again (handoff, For the next session).
- Whether the check of a Case on `SubagentStop` should stop reading an earlier Case when the newest output is a round: a Case on `estimate-case-check-sends-back-a-faulty-case` (handoff, For the next session).
- Whether `estimate-orchestration-defers-in-one-reply` should cover the defer of a sprint item, which takes no Case, or wait for a short-form defer (handoff, For the next session).
- `insight-spec-write-parent-body-kept-on-re-ratification` came back on Case 603 (now 3 children, deferred by case 585): whether to take it up (handoff, For the next session).
- `estimate-skill-grill-me-asks-in-rounds` `failed`; the handoff says its line closes when the first round after the render is read.
- `estimate-orchestration-shows-the-built-case` `failed`; the handoff says its line closes when the first round after the render is read.
- The unticked box `read \`estimate-prespec-onward-reads-the-decisions-of-the-stretch\`` of `archive/migration/2026-10-02/2049/raw/spec.md` names a slug renamed by Case 604 (librarian, this run).

Work:
- Pending readings: `estimate-case-check-sends-back-a-faulty-round`, `estimate-case-check-sends-back-a-faulty-case`, `estimate-case-build-writes-the-case`, `estimate-case-check-refuses-text-before-a-round`, `estimate-case-check-requires-each-question-of-the-rounds`, `estimate-synthesis-clusters`, `estimate-prespec-onward-reads-the-decisions-of-the-session`, `estimate-case-protocol-case-form`, `estimate-prespec-onward-sends-the-agent-on`, `estimate-retro-onward-sends-the-agent-to-the-handoff`, `estimate-retro-runs-on-to-the-handoff`, `estimate-where-to-stop-stops-only-on-its-conditions`, `estimate-orchestration-signs-a-batch-together`, `estimate-orchestration-defers-in-one-reply`, `estimate-ratification-ledger-line-form`, `estimate-spec-capture-offers-the-fork`, `estimate-lint-runs-every-step`, `estimate-carry-over-writes`, `estimate-end-of-work-order`, `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, `estimate-work-mode-takes-the-work-readings`, `estimate-retro-loads`, `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`, `estimate-handoff-dispatches`, `estimate-handoff-holds-each-fact-once`, `estimate-hi-takes-a-conserved-spec`, `estimate-spec-box-runs-a-conserved-spec`, `estimate-spec-write-reaches-the-approved-spec`, `estimate-ledger-write-lifts`, `estimate-generate-rewords`, `estimate-ask-finds`, `estimate-compact-recall-reloads`, `estimate-event-log-records`, `estimate-plan-mode-verified`, `estimate-session-start-context`, `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges`.
- Unticked boxes of the Specs: 8 `read` boxes of `raw/2026-10-02/2300/spec.md`, 12 of `archive/migration/2026-10-02/1202/raw/spec.md`, 4 of `archive/migration/2026-10-02/1834/raw/spec.md`, 4 of `archive/migration/2026-10-02/2049/raw/spec.md` (its fifth, the renamed slug, stands under Cases); each names a pending reading above. No other unticked box.
- Ledger lines this run did not apply: lines 8, 9, 15, 16, 17 of `raw/2026-10-02/2300/ledger.md`, superseded by 606.1 and 606.2.
- Dirty tree: no file outside `vault`, `CLAUDE.md`, `.claude` and `guppi.toml` was changed by this run.

Ask the person:
- none

## Readings at the close

- `make test`: 1102 passed, 6 skipped.
- `make lint`: exit 2, 45 lines of `guppi lint` (5 `deferred`, 38 `unread: pending`, 2 `unread: failed`).
- Pages under `vault/wiki/`: decisions 998, rules 77, estimates 193, lessons 74, insights 29, entities 4. Files `*.md` under `vault/archive/`: 738, after `guppi archive`.
