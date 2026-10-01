# Handoff — 2026-09-30, Stop hooks on their own error, the librarian's reads, case-guppi's check and record

## Notes from memory

- The person asked twice for a plain explanation of a round: the `--subagent` question of the Case check, and the round on the method of the Estimate schema promise. Both were answered by `wait-what`, and the person then agreed with the recommendation.
- On the librarian's failed Estimate the person asked first why its reads are banned at all. They chose that the librarian decides what it reads and flags a read its frame does not name. Their reasoning: a read it keeps making shows a need of the job, and token cost is watched through the flags. They said the flag is not a Case, closer to a flag or a lesson.
- After the first `/pre-spec` the main agent showed rounds, Cases built again and its own question over several replies. The person said they no longer knew which questions to answer, and asked that the next session take up the orchestration of the main agent.
- The person did not expect the second `/pre-spec` to dispatch `ask-guppi` again, and asked about it.
- Case 555.5 came from the second pre-spec run. The main agent proposed it, and the person accepted it with "one last fix".
- The parent `recommend` of Case 558 already carries two items marked not answered, in the form Case 557.2 sets, before 557.2 is rendered.

## Direct instructions to the librarian

- Case 559 is superseded by Case 560. `rule-case-protocol` gets no `deferred_by` from 559. The defer of 560 lands on `estimate-case-protocol-shows-the-built-case`.
- Case 557.3 carries `{supersedes:case 551}`. `deferred_by` 551 leaves `rule-case-build`, and the page leaves the backlog.
- `rule-case-build` takes three `update` items (557.1, 557.2, 557.3), each on its own anchor.
- The decision lines of 555.4 and 555.5 update an Estimate with `ref` naming its rule, as some lines of earlier sessions do.
- Cases 554, 555, 557 and 558 were ratified more than once. The ledger holds each line once, and the Spec holds the last text.
- The renders are `.claude/agents/case-guppi.md`, `vault/wiki/case-schema.md`, `vault/wiki/decisions/schema.yaml` and `.claude/agents/librarian-guppi.md`. The last one is your own agent file: its new frame applies from the run after the next session, not to this run.

## What actually got done

- Ratified: 554, 555.1 to 555.5, 556, 557.1 to 557.3, 558.1 to 558.3, and the defer 560.
- Code: `guppi/ratified.py`, `guppi/casecheck.py` and `guppi/onward.py` exit 2 on their own `Stop` error once the payload is read. `guppi/context.py` shows its error as the `systemMessage` and exits 0. Each docstring says so.
- Tests: `tests/test_ratified.py`, `tests/test_casecheck.py`, `tests/test_context.py`, `tests/test_onward.py`.
- `make test`: 997 passed, 2 skipped. `make style`: clean.
- The check of 556, `uv run pytest tests/test_schemas.py -k estimate --collect-only -q`: 6 of 33 tests collected, namely the five shared tests on `estimates` and `test_an_estimate_without_method_is_one_finding`.
- Readings: ledger lines 29 to 35, seven `passed`.
- Lessons: ledger lines 25 and 36.

## Debt

- `read estimate-case-build-writes-a-plain-round`, the task of 557.3. Its method needs a first and a later round of `case-guppi` after the render, so it was not taken.
- Boxes that wait for the librarian: 33.
- `read` lines whose slug this session creates or updates:
  - `estimate-spec-write-exits-2-on-an-error`
  - `estimate-case-check-exits-2-on-an-error`
  - `estimate-context-size-shows-its-error`
  - `estimate-retro-onward-exits-2-on-an-error`
  - `estimate-retro-onward-sends-the-agent-to-the-handoff`
  - `estimate-context-size-shown-after-each-reply`
  - `estimate-estimates-schema-checked`
  - `estimate-case-build-checks-the-finished-case`
  - `estimate-case-build-records-the-rounds-in-recommend`
  - `estimate-documentation-completes`
  - `estimate-synthesis-clusters`
  - `estimate-brief-written`

## Observations

- Red before the work: `make lint` exited 2 in the Baseline of `work.md`. Its finding lines are `rules/rule-spec-box` (missing field `kind`, missing field `estimates`, orphan) and `decisions/decision-case-13` (a fence open at the end of `## When`), plus the deferred and unread lines. None of this is debt. `## Expected red` is empty.
- Work readings not taken, each because its moment has not come:
  - `estimate-ask-finds`: two dispatches of `ask-guppi`, and the method needs three.
  - `estimate-case-build-writes-the-case` and `estimate-plan-mode-verified`: no `create` without a `ref` in this session.
  - `estimate-case-check-requires-each-question-of-the-rounds` and `estimate-case-check-shows-only-the-checked-case`: the hook sent back no Case for a missing title and refused no reply live.
  - `estimate-case-protocol-shows-the-frontier-after-a-closed-line`: the one Plan Mode reply that closed a sprint line also carried a defer, which the Criterion leaves out.
  - `estimate-event-log-records`: no `/hi` outside plan mode.
  - `estimate-python-utf8-output-intact`: the `Stop` line of `guppi context` is shown to the person, not to the agent.
  - `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`: no `/work` typed by the person.
- Readings that this session's run from `/work` to the librarian can serve, read later from its transcript and this file: `estimate-retro-red-in-the-baseline-is-not-charged` (this Baseline holds lint lines), `estimate-retro-runs-on-to-the-handoff`, `estimate-retro-onward-sends-the-agent-to-the-handoff`, `estimate-where-to-stop-stops-only-on-its-conditions`, `estimate-handoff-holds-each-fact-once`, `estimate-handoff-dispatches`, `estimate-session-phases-in-order`.
- The harness marked two answers of `case-guppi` as instruction-shaped because they named `.claude/settings.json` in a `given`. It was a false alarm.

## For the next session

- The orchestration of the main agent after pre-spec findings: how Cases built again, rounds and its own questions reach the person as one list of what to answer. The person asked for this first. See the lesson at ledger line 25 and `rule-orchestration` in the backlog.
- A second `/pre-spec` run after fixes: whether `ask-guppi` runs again, over the whole plan or only over the Cases built again, and whether the person is told the cost first. See the lesson at ledger line 36.

## Ask the person

none
