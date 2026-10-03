# Brief — 2026-10-03, session 0115: the answer of case-guppi and the number of a Case built again

## Where things stand

- Ratified (handoff): 607 (607.1, 607.2), 609, 610 (610.1, 610.2). Case 608 is superseded by 610.1; 607 and 609 were ratified again after `/pre-spec` with unchanged decision lines.
- Code (handoff): `guppi/casecheck.py` — `is_fact`, the one test of a Fact answer that `is_round` and `answer_of` share; `answer_of` stops at the newest Case, round or Fact answer; `new_number`, `shape_findings`, `clashes`, `ledger_records`, `key_case`, `in_family`; `check_answer` takes the store; `subagent` stores `agent_id` and keeps an answer under a number another agent holds apart, under `<case>@<agent_id>`. Tests: `tests/test_casecheck.py`, 15 new. `make test` 1117 passed, 6 skipped; `make style` clean.
- Readings (handoff): ledger lines 7, 15, 16, 17 (`passed`) and 18 (`failed`). Lessons: ledger lines 9, 19, 20.
- Yaml: `raw/2026-10-03/0115/materialize.yaml`, 20 entries from `materialize` (12 decision lines — 3 `create`, 9 `update`; 5 `estimate`; 3 `lesson`), 3 added by the librarian (synthesis). 0 `failed`, 1 `incomplete` (line 3, superseded), 0 `exists`; `unparsed: []`. 4 entries carry `superseded_by: 610.1` (ledger lines 3–6, Case 608) and were not applied. The ledger has 20 lines; each is held by an entry of the yaml (lines 1 to 20). The yaml of 2300 extended with 0 entries.
- `generate`: 32 pages written or changed from the 0115 yaml, 0 from the 2300 yaml.
- Index check: no `create` outside `estimates`; the three lessons go through the synthesis Grep. `lesson-session-frontier-rewritten-through-powershell` marked `near: lesson-bash-tool-heredoc-escapes-interpreted` (a file text changed by a Windows shell layer on an edit route outside the Edit and Write tools; escapes there, the code page here). No merge.
- Synthesis: Greps `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, 74 lines, and `^(pattern|deferred_by):` over `vault/wiki/insights/`, 31 lines.
  - `lesson-orchestration-own-text-before-a-prespec-round` — joined `insight-case-form-chat-form-read-by-no-script`, whose children hold the archived `lesson-case-protocol-own-text-before-a-round`.
  - `lesson-orchestration-own-sentence-between-heading-and-list` — joined `insight-case-form-chat-form-read-by-no-script`.
  - `lesson-session-frontier-rewritten-through-powershell` — none: no index line names a file changed through PowerShell 5.1 and its code page. Stays `new`.
  - Pair beside the synthesis: `insight-case-form-chat-form-read-by-no-script` was `actioned` (`addressed_by` `decision-case-601.1`, kept); the `update` adds both children and sets it `open`, severity 0 → 2. Neither lesson entry carries `addressed_by`.
- Pages, decisions: 8 created (607, 607.1, 607.2, 608, 609, 610, 610.1, 610.2). `decision-case-608` marked superseded by `decision-case-610.1`; `decision-case-475` and `decision-case-585` marked superseded by 608 and by 610.1. All three moved to `archive/migration/2026-10-03/0115/decisions/`.
- Pages, rules: 3 updated by Cases (`rule-case-check` `estimates` gains the two new Estimates; `rule-case-protocol`, a `replace` in Splitting; `rule-spec-write`, its defer by 475 superseded). Cascade: `rule-case-protocol` and `rule-skill-grill-me` draft → built.
- Pages, estimates: 2 created (`estimate-case-check-sends-back-a-ratified-case-in-another-shape` by 610.1, `estimate-case-check-sends-back-a-case-number-held-by-another-agent` by 610.2); 3 updated by Cases and set `pending` (`estimate-case-check-sends-back-a-faulty-case`, `estimate-case-check-sends-back-a-faulty-round`, `estimate-orchestration-defers-in-one-reply`); 5 readings (`estimate-skill-grill-me-asks-in-rounds` failed → passed, `estimate-case-check-refuses-text-before-a-round`, `estimate-prespec-onward-reads-the-decisions-of-the-session` and `estimate-case-protocol-case-form` pending → passed, `estimate-orchestration-shows-the-built-case` failed → failed).
- Pages, insights: 2 updated. `insight-spec-write-parent-body-kept-on-re-ratification` open → `actioned`, `addressed_by` `decision-case-610.1`, its defer by 585 superseded, severity 3 → 0; its 3 lessons moved to the archive by the cascade. `insight-case-form-chat-form-read-by-no-script` reopened by the synthesis.
- Pages, lessons: 3 created; 2 updated to `clustered` by the synthesis. Moved to `archive/migration/2026-10-03/0115/lessons/`: `lesson-spec-write-keeps-the-body-of-a-case-rebuilt-as-a-parent`, `lesson-spec-write-keeps-the-body-of-a-case-that-gains-sub-cases`, `lesson-spec-write-keeps-the-body-of-case-603-split-at-prespec`.
- `cleanup` moved 6 pages. The render wrote `vault/wiki/case-schema.md` (the sentence of 610.1 in Splitting); `CLAUDE.md`, `.claude` and `guppi.toml` unchanged. `backlog.md` 20 → 19 items: `rule-spec-write` and `insight-spec-write-parent-body-kept-on-re-ratification` gone, `insight-case-form-chat-form-read-by-no-script` added. `sprint.md` and `glossary.md` unchanged.
- Spec boxes ticked by this run: 9 of `raw/2026-10-03/0115/spec.md`, 3 `read` boxes of `raw/2026-10-02/2300/spec.md`. `log.md` 50 lines added.
- Archive: `guppi archive` moved `raw/2026-10-02/2300` to `archive/migration/2026-10-02/2300/raw`; `raw/2026-10-03/0115`, the session of the run, stays. No `pending` Estimate's `method` names the archive step.

## Readings due

1 Estimate `failed`, 37 `pending` (the 38 `unread` lines of `make lint`). Every target named below stands `draft`. Lines with a `read` line in `raw/2026-10-03/0115/spec.md` give it; the others give the page's `method`.

- `estimate-orchestration-shows-the-built-case` (failed) — `rule-orchestration` (draft) — result: the showing of Case 610 in the batch after /pre-spec put a sentence of its own between the heading of the top-level Case and its list — method: by hand, the Cases of a session at its close, against the Agent, SendUserFile, Skill and SendMessage calls of the transcript
- `estimate-case-check-sends-back-a-faulty-case` — `rule-case-check` (draft) — spec 0115: read `estimate-case-check-sends-back-a-faulty-case` — method: `uv run pytest tests/test_casecheck.py -k subagent`, then by hand the first answer the hook sends back, the first file of cases/ it writes, and the first live round after a built Case
- `estimate-case-check-sends-back-a-faulty-round` — `rule-case-check` (draft) — spec 0115: read `estimate-case-check-sends-back-a-faulty-round` — method: `uv run pytest tests/test_casecheck.py -k round_form`; then by hand the first round the hook sends back live
- `estimate-orchestration-defers-in-one-reply` — `rule-orchestration` (draft) — spec 0115: read `estimate-orchestration-defers-in-one-reply` — method: by hand, the first decision the person asks to put off after the render, closed in a reply that leaves no line under the Cases heading of frontier.md open
- `estimate-case-check-sends-back-a-ratified-case-in-another-shape` — `rule-case-check` (draft) — spec 0115: read `estimate-case-check-sends-back-a-ratified-case-in-another-shape` — method: `uv run pytest tests/test_casecheck.py -k shape`, then by hand the first answer the hook sends back for this reason
- `estimate-case-check-sends-back-a-case-number-held-by-another-agent` — `rule-case-check` (draft) — spec 0115: read `estimate-case-check-sends-back-a-case-number-held-by-another-agent` — method: `uv run pytest tests/test_casecheck.py -k clash`, then by hand the first answer the hook sends back for this reason
- `estimate-case-build-writes-the-case` — `rule-case-build` (draft) — method: by hand, live dispatches in a session after the render: one item with a fork, one Case with a create without a ref, one that changes a hook
- `estimate-case-check-requires-each-question-of-the-rounds` — `rule-case-check` (draft) — method: `pytest tests/test_casecheck.py -k rounds`; then by hand the first Case the hook sends back for a missing title
- `estimate-synthesis-clusters` — `rule-synthesis` (draft) — method: by hand, the yaml and the report after a live librarian run whose yaml holds at least two lesson entries — this run: the yaml holds three lesson entries (ledger lines 9, 19, 20); Greps `^(root_cause|deferred_by):` over lessons/ 74 lines, `^(pattern|deferred_by):` over insights/ 31 lines; `lesson-orchestration-own-text-before-a-prespec-round` and `lesson-orchestration-own-sentence-between-heading-and-list` joined the live `insight-case-form-chat-form-read-by-no-script` by one `update` of the Insight (children, status open) and one `update` per lesson (`clustered`), all three `librarian: synthesis`; `lesson-session-frontier-rewritten-through-powershell` joined none and stays `new`; no lesson page read at synthesis; one Insight page read, `insight-case-form-chat-form-read-by-no-script`, named in the report; no page under `vault/archive/` read; the 2300 yaml read, named on the stdout of `materialize`
- `estimate-generate-rewords` — `rule-page-generation` (draft) — method: `pytest tests/test_generate.py` on a temp vault; the live reading the librarian's run that applies the first reword — this run: no entry of the 0115 yaml carries a `reword`
- `estimate-prespec-onward-sends-the-agent-on` — `rule-prespec-onward` (draft) — method: `uv run pytest tests/test_onward.py tests/test_ledger.py`; by hand at the first Plan Mode at which the ledger hook refuses a line of the reply that acknowledges the last ratification
- `estimate-retro-onward-sends-the-agent-to-the-handoff` — `rule-retro-onward` (draft) — method: `uv run pytest tests/test_onward.py tests/test_ledger.py`; by hand at the first end of Retro at which the ledger hook refuses a line
- `estimate-retro-runs-on-to-the-handoff` — `rule-retro` (draft) — method: by hand at the first run from `/work` to the librarian after the render, and at the first Retro where the ledger hook refuses a line
- `estimate-where-to-stop-stops-only-on-its-conditions` — `rule-where-to-stop` (draft) — method: by hand at the first run from `/work` to the librarian after the render, and at the first run of `/box`
- `estimate-orchestration-signs-a-batch-together` — `rule-orchestration` (draft) — method: by hand at the first Plan Mode of a later session after the render in which the person's word asks that a ratified Case change
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
- `estimate-ask-finds` — `rule-ask` (draft) — method: by hand in a later session: three dispatches of ask-guppi, read against the event log
- `estimate-compact-recall-reloads` — `rule-compact-recall` (draft) — method: `pytest tests/test_recall.py`; live, the first compaction of a working session
- `estimate-event-log-records` — `rule-event-log` (draft) — method: pytest in `tests/test_event.py` and `tests/test_gate.py`; by hand, one /hi outside plan mode and one in it
- `estimate-plan-mode-verified` — `rule-plan-mode` (draft) — method: `make test-plan-mode`; one live reading by hand
- `estimate-session-start-context` — `rule-session-start` (draft) — method: `make test-session-start`; by hand, one session opened without /hi whose reply carries a LEDGER block
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` (draft) — method: one reading of the tree by hand at the close of the sprint
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` (draft) — method: `make lint`, exit 0, or only unread lines on the Estimates of entity-sprint-migration
- `estimate-sprint-migration-merges` — `entity-sprint-migration` (draft) — method: `make test` on the last commit of migration, then git log of main after the merge

## Flags

- `near`: `lesson-session-frontier-rewritten-through-powershell` near `lesson-bash-tool-heredoc-escapes-interpreted`.
- `incomplete`: line 3 of the 0115 yaml (`create` of `estimate-case-check-sends-back-a-ratified-case-in-another-shape` by Case 608) lacks `criterion`; it carries `superseded_by: 610.1` and was not applied; the `create` of 610.1 wrote the page.
- `failed`, `unparsed`: none in the 0115 yaml.
- Failed Estimates: `estimate-orchestration-shows-the-built-case` (failed → failed, ledger line 18).
- Stale defers (`make lint`): `rule-subagent-guppi` deferred 31 times since case 29; `rule-case-rebuild-cost` 2 times since case 566; `rule-complaint-becomes-a-lesson` 1 time since case 504; `rule-ledger-line-withdrawn-on-re-ratification` 1 time since case 594; `rule-morph` 1 time since case 239.
- The handoff says `generate` does not read `vault/archive/`, so the `read` boxes of the archived Specs of 1202, 1834 and 2049 are never ticked, whatever readings are taken.
- The handoff says the check of a clash (610.2) reads `agent_id` from the `SubagentStop` payload and no live payload of this session was read for that field.
- MOC candidates, contradictions: none printed by any step of this run.
- `make lint`: exit 2, 43 lines of `guppi lint` — 5 `deferred`, 37 `unread: pending`, 1 `unread: failed`.

## Next session

Cases:
- The close of the sprint (Slice 5), left on the sprint page again (handoff, For the next session).
- Whether the showing of a Case may carry a note under the heading of the top-level Case, or whether the `Stop` check of `rule-case-check` should refuse text between that heading and its list, as it refuses text before a round (handoff, For the next session); `insight-case-form-chat-form-read-by-no-script` stands `open` on it.
- `estimate-orchestration-shows-the-built-case` `failed` (ledger line 18).

Work:
- Pending readings: `estimate-case-check-sends-back-a-faulty-case`, `estimate-case-check-sends-back-a-faulty-round`, `estimate-orchestration-defers-in-one-reply`, `estimate-case-check-sends-back-a-ratified-case-in-another-shape`, `estimate-case-check-sends-back-a-case-number-held-by-another-agent`, `estimate-case-build-writes-the-case`, `estimate-case-check-requires-each-question-of-the-rounds`, `estimate-synthesis-clusters`, `estimate-generate-rewords`, `estimate-prespec-onward-sends-the-agent-on`, `estimate-retro-onward-sends-the-agent-to-the-handoff`, `estimate-retro-runs-on-to-the-handoff`, `estimate-where-to-stop-stops-only-on-its-conditions`, `estimate-orchestration-signs-a-batch-together`, `estimate-ratification-ledger-line-form`, `estimate-spec-capture-offers-the-fork`, `estimate-lint-runs-every-step`, `estimate-carry-over-writes`, `estimate-end-of-work-order`, `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, `estimate-work-mode-takes-the-work-readings`, `estimate-retro-loads`, `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`, `estimate-handoff-dispatches`, `estimate-handoff-holds-each-fact-once`, `estimate-hi-takes-a-conserved-spec`, `estimate-spec-box-runs-a-conserved-spec`, `estimate-spec-write-reaches-the-approved-spec`, `estimate-ledger-write-lifts`, `estimate-ask-finds`, `estimate-compact-recall-reloads`, `estimate-event-log-records`, `estimate-plan-mode-verified`, `estimate-session-start-context`, `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges`.
- Unticked boxes of the Specs: 5 `read` boxes of `raw/2026-10-03/0115/spec.md`; 5 `read` boxes of `archive/migration/2026-10-02/2300/raw/spec.md`; 12 of `archive/migration/2026-10-02/1202/raw/spec.md`, 4 of `archive/migration/2026-10-02/1834/raw/spec.md`, 5 of `archive/migration/2026-10-02/2049/raw/spec.md` (counts by `grep -c`).
- Ledger lines this run did not apply: lines 3–6 of `raw/2026-10-03/0115/ledger.md`, Case 608, superseded by 610.1.
- Dirty tree: no file outside `vault`, `CLAUDE.md`, `.claude` and `guppi.toml` was changed by this run.

Ask the person:
- none

## Readings at the close

- `make test`: 1117 passed, 6 skipped.
- `make lint`: exit 2, 43 lines of `guppi lint` (5 `deferred`, 37 `unread: pending`, 1 `unread: failed`).
- Pages under `vault/wiki/`: decisions 1003, rules 77, estimates 195, lessons 74, insights 29, entities 4. Files `*.md` under `vault/archive/`: 755, after `guppi archive`.
