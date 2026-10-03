# Handoff — 2026-10-02, the round check, the synthesis report, by hand boxes, the onward reading

## Notes from memory

- On the by hand box item the person stopped the first round and asked why such a box stays unticked at all, saying the direction was wrong. The main agent had offered its own fork (tick the box later) before any dispatch, and the first round was built on it. case-guppi then turned the Case to the cause: a Case writes no by hand box that waits for the librarian's run.
- The person asked whether the librarian needs new instructions for ticking boxes. case-guppi answered that it does not: `generate` ticks the `read` lines, and the librarian's `make lint` is already in the brief.
- On the round check the person went against one recommendation and chose the wider check: the title line and the fixed labels (`**Now:**`, `**Options:**`, an option with `**After:**`, the `➡️` line), not the title line alone.
- At pre-spec the person chose to add `lesson-case-check-question-line-without-colon-unseen` to `insight-case-form-chat-form-read-by-no-script`, with `addressed_by` naming `decision-case-601.1`, and to leave the two failed Estimates `failed`. The person accepts that they come back as Cases at the next /hi.
- The close of the sprint was put off again by the person ("Откладываем и идём работать").
- Caveat: the ledger line of 606.2, an `update` of `decision-case-13` with `change` alone, was a form case-guppi chose itself. The person's ratification covers it.

## Direct instructions to the librarian

- Cases 603, 603.1 and 603.2 are superseded by 606.1 and 606.2, with the same content. The ledger holds both sets of lines. Check that the `{supersedes}` blocks leave no live page of 603 and that `rule-case-protocol` and `estimate-case-protocol-case-form` are written once, from 606.1.
- Case 605 sets `addressed_by` of `insight-case-form-chat-form-read-by-no-script` to `decision-case-601.1`, a page this same run creates. It also sets `lesson-case-check-question-line-without-colon-unseen` `clustered` under that Insight. Check the order, and that the cascade archives both clustered lessons.
- Case 604 renames `estimate-prespec-onward-reads-the-decisions-of-the-stretch` to `estimate-prespec-onward-reads-the-decisions-of-the-session` by a `rename` in its `update`. Check that the `estimates` field of `rule-prespec-onward` follows.
- Case 602 changes `rule-synthesis`, which renders into your own frame. Your synthesis in this run reads the frame as you loaded it, before the render.
- The lesson on the Spec hook keeping the body of Case 603 has the root cause of `insight-spec-write-parent-body-kept-on-re-ratification`. It may join that Insight.

## What actually got done

- Ratified: 601 (601.1, 601.2, 601.3, 601.4, 601.5), 602, 604, 605, 606 (606.1, 606.2).
- Code: `guppi/casecheck.py` — `is_round` is the one test of a round, by the mark `❓`. New `round_form`, `option_with_after`, `faulty_round`, `subagent_outputs`, `spaces_aside` and `send_back`. `subagent` sends back a round out of form once per text. `round_titles` skips a round out of form. Module docstring changed. `guppi/onward.py` — `transcript_replies` replaces `stretch_replies`: the decision lines of every reply of the transcript count.
- One-off of 606.2: `make lint` printed no `fence` line on `decision-case-13`. The box of Case 591.11 in `raw/2026-10-02/1202/spec.md` is ticked.
- Tests: `tests/test_casecheck.py` — 13 new tests, and the helper `round_of` writes the full grill-me form. `tests/test_onward.py` — one new test.
- `make test`: 1102 passed, 6 skipped. `make style`: clean.
- Readings: ledger line 1 (`estimate-synthesis-clusters` failed, at /hi), lines 22–26 (five passed). Lessons: lines 27 and 28.

## Debt

- No box of code, test or command is unticked, and no test was reverted.
- Boxes that wait for the librarian: 17.
- `read` lines whose slug this session creates or updates: `estimate-case-check-sends-back-a-faulty-round`, `estimate-case-check-sends-back-a-faulty-case`, `estimate-case-build-writes-the-case`, `estimate-case-check-refuses-text-before-a-round`, `estimate-case-check-requires-each-question-of-the-rounds`, `estimate-synthesis-clusters`, `estimate-prespec-onward-reads-the-decisions-of-the-session`, `estimate-case-protocol-case-form`.

## Observations

- Red before the work: `make lint` exit 2, 47 lines of `guppi lint` (5 `deferred`, 40 `unread: pending`, 2 `unread: failed`). The same 47 lines stood after the work. No expected red.
- The check of a Case on `SubagentStop` reads an earlier Case again when the newest output of `case-guppi` is a round. In this session it sent back the second round on Case 601 once, because the earlier Case 601 held no `recommend` item for that round's titles. Case 601 names this as not done.
- `round_form` was run over the rounds in earlier transcripts. Rounds in the current template pass. Rounds written before the `**Now:**`/`**Options:**` template would be sent back, and so would one round whose title lines lack the colon.
- The only defer of the session was an item of the sprint, which takes no Case. The Criterion of `estimate-orchestration-defers-in-one-reply` speaks only of a defer shown as a short-form Case, so its reading was not taken.
- The harness again marked answers of `case-guppi` as instruction-shaped (`settings-json`) when their text named `.claude/settings.json`.
- `ask-guppi` at pre-spec took 95 tool uses and about eight minutes.
- Readings still waiting for a moment of a later run: `estimate-retro-runs-on-to-the-handoff` and `estimate-where-to-stop-stops-only-on-its-conditions` (the end of this run, at the librarian), and `estimate-retro-loads` and `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` (their `/box` part).

## For the next session

- The close of the sprint (Slice 5), left on the sprint page again.
- Whether the check of a Case on `SubagentStop` should stop reading an earlier Case when the newest output is a round: a Case on `estimate-case-check-sends-back-a-faulty-case`.
- Whether `estimate-orchestration-defers-in-one-reply` should cover the defer of a sprint item, which takes no Case, or wait for a short-form defer.
- `estimate-skill-grill-me-asks-in-rounds` and `estimate-orchestration-shows-the-built-case` stay `failed`. Their line under Cases needs no decision: it closes when the first round after the render is read.
- `insight-spec-write-parent-body-kept-on-re-ratification` came back in this session, on Case 603. Whether to take it up.

## Ask the person
