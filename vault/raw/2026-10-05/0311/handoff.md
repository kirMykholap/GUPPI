# Handoff — 2026-10-05, the Spec hook after a refusal, case-guppi writes its own Case file, the schema by example

## Notes from memory

- The person recalled that a subagent is not asked for a permission to write in Plan Mode; `rule-permissions` and a lesson said the opposite. The documentation (https://code.claude.com/docs/en/sub-agents.md) settled it: a subagent with no `permissionMode` inherits the main conversation's mode, and in `plan` mode it runs in the mode it declares. So 645.1 sets `permissionMode: acceptEdits` for `case-guppi`; no allow rule. Not yet seen live: a `case-guppi` writing in Plan Mode, which is the first reading of `estimate-case-build-writes-the-case`.
- The person first chose one new Estimate for 644; `/pre-spec` found it held two conditions (`rule-atomicity`), and the person chose the split (644.8).
- The person withdrew C7, a line of a Criterion changed by a `replace` pair, after learning that cases 193 and 378.4 had refused it; no Case.
- The person deferred C1, C2 (sprint, no Case) and C3, C5, C6 (Cases 647–649) to go to work; the context of the session passed 500,000 tokens in Work Mode.
- 645 was built three times (first build, the findings of `/pre-spec`, the split of 644 for 645.5) and grew to sixteen sub-cases; 644 and 645 each cost a case-guppi about ten minutes a build.

## Direct instructions to the librarian

- `rule-spec-write` takes pairs from two Cases: 644.1 (the error sentence, the reason, the re-fire sentence, the sentence of case 554) and 645.5 (the Purpose, `set` of `purpose`, "for the answer of `case-guppi` stored under Case N", "no such call made after the time of the store", "differs from that answer"). `guppi prespec --check` found no clash of anchors; check each anchor hits once after the other Case's pairs.
- `rule-case-build` takes eleven pairs in 645.1, one of them on its frontmatter block `tools: Read, Grep, Glob`, whose `new` adds the line `permissionMode: acceptEdits`; the render of `.claude/agents/case-guppi.md` must carry both.
- 645.2 deletes `estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent`; its slug leaves the `estimates` of `rule-case-check`.
- The six Estimates of `rule-spec-write` that 644 replaces get their Criteria from 644.2–644.7; 645.5 leaves them alone.
- 646 writes a new section with a four-backtick block tagged `case` inside a five-backtick `new`; after the render, `vault/wiki/case-schema.md` must hold the block, and `uv run pytest tests/test_case_schema.py` then runs instead of skipping.

## What actually got done

- Cases ratified: 644 (644.1–644.8), 645 (645.1–645.16), 646; each of them built again on the findings of `/pre-spec` and ratified again. Short-form defers: 647, 648, 649.
- Code: `guppi/ratified.py` — the Stop run no longer returns at `stop_hook_active`; its reasons and its error pass through `own_refusals` and `untold` of `guppi/ledger.py` under `COMMAND`; the guard lets `case-guppi` alone write under `cases/` by `agent_type` and refuses it elsewhere; the Spec hook refuses a Case whose file differs from the store. `guppi/casecheck.py` — `written_case_files`, `file_differences`, `changed_file`, `judge_and_store`; `subagent` reads the files the subagent wrote, keeps the old path of the answer text; `stored_parents` removed; `stop` refuses a showing whose file differs. `guppi/ledger.py` — the docstring of `refusals`.
- Tests: `tests/test_ratified.py` (the re-fire tests rewritten; `-k answers_a_refusal`, `-k tells_each_reason_once`, `-k changed_file`, flagged `-k approved_spec`, `-k superseded`, `-k defer`, `-k guard` for `case-guppi`), `tests/test_casecheck.py` (`-k lone` removed; file tests of 645.2; `-k changed_file`; the tests `-k script`, `-k note`, `-k subagent_clash`, `-k backlog`, `-k shape` read a case file by `answer_file`), `tests/test_case_schema.py` (new, skipped until the render; run against the example of Case 646 by hand in Work Mode: no finding, no note, and the unpadded span gives its finding).
- The probe of 645.3: a subagent of type `claude` wrote a file in the scratchpad with no permission prompt; the `PreToolUse` input held `agent_id` and `agent_type` (`claude`), `permission_mode` `auto`.
- `make test`: 1190 passed, 8 skipped; `make style` clean.
- Readings: L1 (`estimate-synthesis-clusters`, failed, at `/hi`). Lessons: L31, L40, L41.

## Debt

- No box of code, test, command or migration is left unticked.
- 62 boxes wait for the librarian or a later session: page, render and read lines.
- Each Estimate this session creates or updates waits for its next moment:
  - `estimate-spec-write-answers-a-refusal`, `estimate-spec-write-tells-each-reason-once`, `estimate-spec-write-copies-the-ratified-case`, `estimate-spec-write-checks-the-written-case`, `estimate-spec-write-writes-a-defer`, `estimate-spec-write-removes-a-superseded-case`, `estimate-spec-write-exits-2-on-an-error`, `estimate-spec-write-refuses-a-changed-case-file`: their pytest at the Work readings of a later session; `answers-a-refusal` also a live case at a later `/hi`.
  - `estimate-spec-write-reaches-the-approved-spec`: pytest and a Case ratified in Work Mode.
  - `estimate-case-check-sends-back-a-faulty-case`, `estimate-case-check-refuses-a-changed-case-file`, `estimate-case-check-refuses-a-letter-outside-the-script`, `estimate-case-check-notes-a-criterion-line-not-carried`, `estimate-case-check-sends-back-a-case-number-held-by-another-agent`, `estimate-case-check-shows-only-the-checked-case`, `estimate-case-check-requires-a-backlog-item-decided-on-its-page`, `estimate-case-check-sends-back-a-ratified-case-in-another-shape`, `estimate-spec-reconcile-refuses-an-edit-of-the-plan`: their pytest in a later session; the faulty-case and guard ones also live, in a session after the render.
  - `estimate-case-build-writes-the-case`, `estimate-case-build-answers-what-done-means`, `estimate-case-build-records-the-rounds-in-recommend`, `estimate-orchestration-shows-the-built-case`, `estimate-case-protocol-case-form`, `estimate-permissions`: live dispatches of `case-guppi` in a session after the render of `.claude/agents/case-guppi.md`.
  - `estimate-case-protocol-example-passes-the-check`: `uv run pytest tests/test_case_schema.py` after the librarian's render, passed and not skipped.

## Observations

- Red before the work: `make lint` exit 2, 25 finding lines, in `## Baseline` of `work.md`.
- The old path of 645.2 stays live in the code: this session's `case-guppi` still answers with text until the render is read at the next session start; a later Case removes the path after `estimate-case-build-writes-the-case` passes live.
- Both `ask-guppi` runs at the `/pre-spec` of this session broke the search rule of `.claude/rules/search-leaves-out-decisions.md` and reported it: one put `!**/decisions/**` before other filters in the glob, one ran a Grep over the repository root with `*.py` and no exclusion. These runs are the moment of `estimate-search-leaves-out-decisions-in-every-agent` and `estimate-ask-finds`, read at the next `/hi`.
- A second agent that builds a Case under a number another agent holds now overwrites that Case's file before the check sends it back; the comparison refuses the showing until the file is fixed (Not done of Case 645).

## For the next session

- Remove the old path of `guppi casecheck --subagent` (the answer text, `write_case_files`) once `estimate-case-build-writes-the-case` passes live.
- Remove the skip of `tests/test_case_schema.py` after `estimate-case-protocol-example-passes-the-check` passes.
- `orchestration.md` still calls the reply of `case-guppi` "the answer"; two lessons of `insight-workflow-case-schema-silent-on-what-the-scripts-accept` are about forms the main agent writes there.
- Whether a guard stops a second agent from overwriting the file of a Case another agent holds.

## Ask the person
