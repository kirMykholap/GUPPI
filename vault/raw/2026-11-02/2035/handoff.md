# Handoff — 2026-11-02, sprint plugin: the note of names narrowed, three readings put off

## Notes from memory

- The person took the recommended option at each question: three short-form defers (C3, C4, C5), then Case 1010 through four rounds of `case-guppi`. For Q3 of the third round the person answered "Ok" without naming a threshold; the agent passed that on, and `case-guppi` asked again with 20 as the recommended threshold, which the person took. The number 20 rests on the probe of session 1548, not on a count per name.
- The person put off C1 (push of `plugin` and a tag `prod-x.y.z`, reading the CI run) to a later session, as a line of the sprint left for later.
- `/pre-spec` sent Case 1010 back once on five findings (one of `guppi prespec --check`, four of `ask-guppi`); `ask-guppi` confirmed its four closed, and the person ratified the Case again. `ask-guppi` reported that it made searches of code beyond the one its frame allows.
- The first real note of names came during the build of Case 1010, in the hundreds of files, as the probe predicted; `case-guppi` answered it by naming the names in `context` rather than reading each file.

## Direct instructions to the librarian

- Cases 1007, 1008 and 1009 defer Estimates that already stand; each names its page and `guppi backlog` should list three new lines.
- Case 1010.1 and 1010.2 both update `rule-case-check`: two `replace` items on different passages of the same page.
- The decision lines of Case 1010 stand twice in the chat, at the first ratification and after `/pre-spec`; the ledger should hold them once.

## What actually got done

- Cases ratified: 1007, 1008, 1009 (short-form defers); 1010 with 1010.1, 1010.2, 1010.3.
- Code: `.guppi/guppi/casecheck.py` — `changed_targets` takes the task lines by `read_tasks` and of each only its first code span; `names_notes` counts the files that hold each name and gives one note with the count for a name held by more than `BROAD_NAME` (20) files; docstrings follow. `.guppi/tests/test_casecheck.py` gains four tests (first code span; 21 files, 20 files, a narrow name kept beside a broad one).
- `uv run --project .guppi guppi test`: 1908 passed, 6 skipped, 1 deselected. `uv run --project .guppi guppi style`: clean.
- Readings: L10 `estimate-case-check-notes-the-files-that-name-what-a-case-changes` passed; L11 `estimate-case-check-sends-one-note-for-a-broad-name` passed. Lessons: L12, L13 (error).

## Debt

- No box is debt.
- 10 boxes wait for the librarian.
- `estimate-case-build-searches-the-names-of-what-it-changes` — waits for the `/pre-spec` of the first session, after the librarian's render of `.claude/agents/case-guppi.md`, in which the hook of `rule-case-check` sends `case-guppi` a note on a file or on a name.
- `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec` — waits for an acknowledging reply after `/pre-spec` that waits for the person's word; no such reply came in this session.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — waits for the owner's push of `plugin` and a tag `prod-x.y.z`, before the close of `plugin`.

## Observations

- The full `guppi test` of Work Mode failed once on `test_the_live_code_holds_no_pointer_outside_a_bracket` for a comment of a new test; fixed in Work Mode (L13).
- No red before the work; no expected red.
- The hook and `case-guppi` still run the old breadth of the note until the librarian renders `.claude/agents/case-guppi.md`; the code of the hook is live from this session's commit.

## For the next session

- C1: the owner pushes `plugin` and a tag `prod-x.y.z`, and the session reads the CI run.
- Whether the threshold of 20 files fits, once a real note under the new code is seen.

## Ask the person
