# Handoff — 2026-09-30, the Frontier of the 0138 brief: UTF-8, glossary rows, case-guppi quotes, /carry brief, the sprint move

## Notes from memory

- On the sprint move the person answered beyond the offered options: remove the move of `generate` altogether, since in practice it gets in the way; the finish conditions of a sprint stand under Done when only; a milestone line moves only on the person's request.
- On the `env` block the person first asked what it is and how it works (a `/wait-what` on Q3), then chose to build it in this session rather than leave it for later.
- The person added two items in the session: case-guppi quoting their Russian words, and the insight on the chat form of a Case, which they chose to close with a check in code.
- The person noticed that the two decisions of the pre-spec report were asked without the question shape and its icons.
- Case 538 was shown and ratified three times: first as built, then without the Flags line on moves (after Case 539 removed the move), then with `Cases` always "none" (after pre-spec).
- The person deferred the rest at the close of Plan Mode: the close of a sprint stays a sprint line, and `/work` taking up a conserved Spec is a short defer on `rule-work-mode`.

## Direct instructions to the librarian

- Cases 534 to 539 were ratified again after pre-spec; the ledger holds each decision line once, with the lines that the second ratification added after the others. Apply them by the Spec as it stands.
- `rule-brief` is updated by two sub-cases, 538.2 (the paragraph on the brief of `carry`) and 539.2 (the Flags item and the sentence on how the sprint page changes); their pairs touch different text. `rule-sprint` is updated by 539.1 and 539.3 the same way.
- Case 539.1 renames `estimate-sprint-moves-a-passed-over-item` to `estimate-sprint-items-move-only-by-a-case` and deletes `estimate-sprint-drops-an-emptied-milestone`; `generate` no longer moves sprint lines, so no move is to be flagged in the brief from this run on.
- Case 538.1 carries `{supersedes:case 533}` on `rule-carry-over`: its defer is retired and the page leaves the backlog. Case 540 is a new defer on `rule-work-mode`.
- Case 537 sets `insight-case-form-chat-form-read-by-no-script` `actioned`; the cascade then archives its two clustered lessons.
- The reading of `estimate-context-size-warns-past-the-limit` replaces its Result, which held a false sentence on U+FFFD.
- Case 534.1 creates `rule-python-utf8` as a fourth child of `rule-settings`; the render writes the `env` block into `.claude/settings.json`.

## What actually got done

- Ratified: 534.1, 534.2, 535, 536, 537, 538.1, 538.2, 539.1, 539.2, 539.3, 539.4; deferred: 540.
- Code: `guppi/casecheck.py` (the language finding on each answer of case-guppi), `guppi/generate.py` (the move and the drop removed), `guppi/backlog.py` (docstrings). Tests: `tests/test_casecheck.py` (English fixtures, `guppi.toml` in the fixture, the `script` tests), `tests/test_generate.py` (six tests of the move replaced by one that nothing moves).
- `make test`: 935 passed, 2 skipped. `make style`: clean.
- Readings: ledger lines 1 to 5, 10, and 34 to 40 — two of them `failed`: `estimate-case-build-writes-a-plain-round` and `estimate-skill-grill-me-asks-in-rounds`. Lessons: lines 11, 30, 41, 42.

## Debt

- none.
- 32 boxes wait for the librarian.
- The `read` lines of Estimates this session creates or updates: `estimate-python-utf8-output-intact`, `estimate-settings`, `estimate-case-check-refuses-a-letter-outside-the-script`, `estimate-carry-over-writes`, `estimate-brief-written`, `estimate-sprint-items-move-only-by-a-case`, `estimate-backlog-renders`.

## Observations

- `make lint` was red before the work, exit 2 with 88 lines, and stood the same line for line after it; nothing was expected red.
- The `!` commands of `/work` and `/retro` reached the agent as instructions to run them, not as their output; the agent ran them itself.
- A scratchpad Python script of Work Mode stopped at the print of a Cyrillic string until it ran with `PYTHONUTF8=1` — the case Case 534 closes once the render writes the `env` block.
- `work.md` was written through Bash, not the Write tool, so the live probe of `estimate-permissions` at its Write did not occur.
- Readings whose moment is this run, from `/work` to the librarian, not yet taken: `estimate-retro-runs-on-to-the-handoff`, `estimate-retro-onward-sends-the-agent-to-the-handoff`, `estimate-where-to-stop-stops-only-on-its-conditions`, `estimate-work-mode-takes-the-work-readings`, `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` (the `/work` at the fork only), `estimate-retro-loads`, `estimate-retro-red-in-the-baseline-is-not-charged`, `estimate-retro-commit-gates`, `estimate-handoff-dispatches`, `estimate-handoff-holds-each-fact-once`, `estimate-session-phases-in-order`, `estimate-documentation-completes`, `estimate-generate-writes`. The next session reads them from this session's transcript.
- `estimate-hi-takes-its-readings` waits for a brief with an Ask the person line; `estimate-case-protocol-ledger-line-form` waits for a Case that takes up a decision with more than one Case in its `deferred_by`.

## For the next session

- `estimate-case-build-writes-a-plain-round` failed: a round of case-guppi ended with a list of the files it checked, session ids in their names — the frame says the answer holds nothing but the round.
- `estimate-skill-grill-me-asks-in-rounds` failed: case-guppi indents the label `**Options:**` by four spaces under the Now block in most rounds, so it runs on as part of the paragraph above.
- No rule gives the question shape of grill-me to a question the main agent asks the person itself, as in a pre-spec report.
- case-guppi can build a Case that departs from the option the person chose in its round, and can sign a count over the frame from a partial search; both were found only at pre-spec.

## Ask the person

- none.
