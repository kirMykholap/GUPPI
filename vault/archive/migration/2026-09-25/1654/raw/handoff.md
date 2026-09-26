# Handoff — 2026-09-25, session 1654: the leftovers of 1228, the reading rule, the context note

## Notes from memory

- Case 428 went through two mechanisms. The first build (a refusal judged by the ticks of the Case's tasks, with a memory of refused lines in the event log) was not ratified; the person chose rule B: what a session changes, it does not measure, judged by the ledger alone. Only B was ratified.
- At pre-spec, ask-guppi found 18 points. Points 1–5 made 428 and 429 rebuilt and ratified again (428.4 is new; 429 gained `estimate-case-protocol-ledger-line-form`). Points 6–11 were prose fixes of `context` in 426, 427, 430, 432, shown as a DIFF, not ratified again.
- Point 12 of pre-spec, decided by the person as a note here, not a Case: a `read` line of an Estimate this session changes is ticked by a later reading only while its unit lies in `raw/`. `tick_read` does not read the archive, and `kept_reason` does not look at open `read` lines. The debt is carried by the Estimate's `pending` and lint's `unread`. The same holds for the two read lines of 1228 that Case 432 rewrote (W1, W2), since 427 makes unit 1228 archivable.
- The person asked whether a Case can be copied into the chat mechanically. The docs (claude-code-guide) name no such mechanism; `systemMessage` is plain text. The person chose to keep the present flow (the Stop comparison guards the showing); no Case.
- The lesson line L12 names "the SubagentStop comparison of casecheck"; it was the comparison on `Stop` that refused the showing of 428.3. The line stands as written.
- Past 400 000 tokens the context hook gave its note (the new text of Case 430 was live in this session after Work Mode).

## Direct instructions to the librarian

- Materialize with the code of commit 6ffb2c9: ledger line L16 carries four `{supersedes:case N}` blocks (404, 409, 418, 422); only the new `parse_line` (Case 429) reads them as a list.
- Unit 1228: its yaml entry of line 40 now carries `superseded_by: '427'` and no `failed` (one-off migration of Case 427). Check that `generate` prints nothing for `estimate-frame-check-finds-a-contradiction` and that `render` ticks the render lines of `raw/2026-09-25/1228/spec.md` (W26). That is the by-hand task of Case 427.
- Case 425 applies the lost `rename` of `rule-frame-check` to `rule-case-build`; after `generate`, Grep `rule-frame-check` over `vault/wiki/`: only History lines, `brief.md` and `log.md` should hold it (the by-hand task of Case 425).
- `rule-retro` gets pairs from 428.3 and 428.4; `rule-case-protocol` from 428.1 and 429; `rule-prespec` from 426 and 432. Pre-spec found each anchor once and apart; apply in entry order.
- Case 428 in the ledger: the decision lines of 428.1–428.3 stand once (the re-ratification did not repeat them); 428.4 and the second line of 429 came with the re-ratification.
- Readings of every Estimate this session changed wait for a later session (Case 428.1); list them in the brief.

## What actually got done

- Ratified: 425, 426, 427, 428 (428.1–428.4), 429, 430, 431, 432. Frontier: C3–C9, C12, C13 closed by Cases; C1, C2 `[-] · sprint`; C10, C11 `[-] · deferred · kept`.
- Code, commit 6ffb2c9: `guppi/prespec.py` (a second item of one slug is a finding, 426; `superseded_in_window` walks a list, 429; `estimates_to_read` gives the slug of a `rename`, 432), `guppi/materialize.py` (`parse_line` gives `supersedes` as a list, each Case marked and refolded, `cases_of` reads the old single value, 429; the docstring names the writer of `superseded_by` on an `estimate` entry, 427), `guppi/ledger.py` (the refusal of 428.1: `changed_by_session`, `refused_readings`; exit 2 only for the reply just finished), `guppi/context.py` (the note past 400 000, 430); tests in `test_prespec.py`, `test_materialize.py`, `test_casecheck.py`, `test_ledger.py`, `test_context.py`. `make test`: 680 passed, 2 skipped; `make style` clean.
- Migrations: yaml of 1228 line 40 (427); two read lines of `raw/2026-09-25/1228/spec.md` rewritten to the new slugs (432). `git rm .claude/agents/frame-guppi.md` (W25), line 154 of the 1228 Spec ticked.
- Readings: `estimate-case-protocol-shows-the-built-case` failed (the retyped ratification of 428.3); passed: `estimate-case-check-shows-only-the-checked-case`, `estimate-page-read-cuts-the-history`, `estimate-harness-pipeline`, `estimate-spec-write-copies-the-ratified-case`, `estimate-spec-write-checks-the-written-case`, `estimate-prespec-checks-the-frontier`, `estimate-hi-writes-frontier`.
- Not done: every page, render, sprint and glossary line of the Spec (the librarian's); the by-hand checks of 425 and 427 (at the librarian's run); the `read` lines of the Estimates this session changed (a later session); Work readings W2 (needs a `create` without a `ref`), W3 (needs a live send-back on `SubagentStop`), W9, W10 (need a defer), W13–W24 (need `/carry`, the librarian or the close of the sprint), W26 (the librarian's render), W28 (the same readings).
