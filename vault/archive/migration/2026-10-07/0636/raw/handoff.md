# Handoff — 2026-10-07, migration: the tag check, the shell-write hook, the pairs of the session

## Notes from memory

- C7 and C6 were closed with a reading by the person's word, not by a Case. On C7 no earlier reply of the session closed a line with no ratification; the reply that closed C7 was itself the first such reply. On C6 no decision was put off in this session or in 0425, so no reply that puts one off was read against the Criterion. The two readings rest on the person's word alone, and their ledger lines say so.
- On A1 (`estimate-permissions`) the person said no permission prompt came. The agent did not check which paths the `case-guppi` dispatches read.
- On C5 the person chose no Case. The reading of `estimate-case-build-writes-the-case` is to be taken whole in the next session, after the render. Splitting the Estimate into one Estimate per rare condition was proposed and declined.
- On Case 705 the person chose to drop only the change. Taking back the whole decision of a ratified Case is left not done.
- On Case 706 and Case 710 the person chose no check that sends back an `actioned` Insight with no `addressed_by` before ratification. `make lint` stays the only check.
- `addressed_by` of the two Insights of Cases 710.2 and 711.3 stands bare (`decision-case-710.1`, `decision-case-711.3`). The check of the Case file refused the quoted wikilink to a decision of the same session, and the person chose the bare form in that case. The field description of `rule-insights-schema` asks for the quoted wikilink.
- C1, C2 and C9 were closed `[-] · sprint · defer` for the session that closes the sprint. C9 is the brief's copy of C1 and C2, so it was closed the same way and not as `defer case N`.
- For Case 710 the person asked for the round to be explained again in plain words before they answered.

## Direct instructions to the librarian

- Cases 703 and 711 both change `rule-case-check`. 711.3 rewords the Purpose sentence on the checks of pre-spec and of the Spec hook, and names the tag check of 703.1 as its second exception. 703.1 adds its own sentence after "(case 688.1)." Count the `replace` anchors of `rule-case-check` in yaml order before `generate`.
- Cases 705.1 and 711.4 both change `rule-case-build`, in different paragraphs: the drop paragraph, and the sentence on the case files `case-guppi` reads.
- Cases 704 and 706 both update `insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out`. 704 is a History line only. 706 sets `addressed_by: '[[decision-case-701.1]]'`.
- Case 704 declares the tag `orchestration` by a tag line. `tags.md` should gain its row, and `generate` should print no warning for it.
- The render writes `.claude/settings.json` (the `shellwrite` hook on `PostToolUse` of `Bash|PowerShell`), `.claude/agents/case-guppi.md` and `vault/wiki/orchestration.md`.
- Case 710.2 sets `insight-workflow-file-changed-through-a-shell-command` `actioned`. Case 711.3 sets `insight-workflow-edit-pair-signed-from-a-grep-fragment` `actioned`. Both should leave `backlog.md`.

## What actually got done

- Cases ratified: 703 (703.1, 703.2, 703.3), 704, 705 (705.1, 705.2), 706, 710 (710.1, 710.2), 711 (711.1–711.4). Cases 707, 708 and 709 were dropped with their files emptied, and none of them has a decision line.
- Code:
  - `guppi/tags.py`, new: `registered_tags`, `declared_tags`, `ratified_tags`.
  - `guppi/casecheck.py`:
    - `unlisted_tags`;
    - `read_outputs` and `unread_sentences`;
    - `check_answer` runs the pairs of the session in order and adds the notes of a shared sentence.
  - `guppi/ledger.py`: `refused_tags`, `tag_message`; a line refused for its tags is passed to `unmarked_lessons`.
  - `guppi/prespec.py`: `sentence_around`, `shift_spans`, `sentence_parts`, `shared_sentence_note`; `check_pairs` takes `own`, `notes` and `trace`.
  - `guppi/generate.py`: `reword_pattern`; `register_tags` reads its rows through `guppi/tags.py`, and `TAG_ROW` moved there.
  - `guppi/shellwrite.py`, new.
  - `guppi/cli.py`: the `shellwrite` command.
- Tests:
  - `tests/test_casecheck.py` (tag, `session_pairs`, `shared_sentence`, `unread_sentence`). The helpers `transcript` and `answer_file` now hold a `Read` of the page of `rule-x`. One layout test changed its case 7 to carry no pair.
  - `tests/test_ledger.py` (tag, hold).
  - `tests/test_shellwrite.py`, new.
- `make test`: 1407 passed, 6 skipped. `make style`: clean.
- Readings:
  - Plan Mode: L11, L12 and L13, `passed` by the person's word.
  - Retro, `passed`: `estimate-case-check-sends-back-an-unlisted-tag`, `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag`, `estimate-ledger-write-asks-for-the-mark-of-a-lesson`, `estimate-shell-write-check-repairs-and-reports`, `estimate-case-check-applies-the-pairs-of-the-session-in-order`, `estimate-case-check-notes-a-sentence-two-cases-change`, `estimate-case-check-sends-back-a-pair-whose-sentence-was-not-read`, `estimate-orchestration-shows-the-built-case`.
  - Retro, `failed`, not read: `estimate-case-build-writes-the-case`, `estimate-case-build-checks-the-finished-case`.
- Lessons: none.

## Debt

- No box of code, test, command or migration is left unticked.
- The boxes that wait for the librarian are the `create`, `update`, `read` and `guppi render` lines of the Spec.
- `estimate-hi-writes-frontier`, `estimate-hi-takes-a-conserved-spec`, `estimate-brief-written`, `estimate-sprint-close-next-session-opens-the-sprint`: wait for the `/hi`, or the librarian's run, of the session after the close of the sprint.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, `estimate-backlog-renders`, `estimate-sprint-close-runs-in-the-librarian-run`, `estimate-sprint-close-takes-the-readings-in-groups`, `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges`: wait for the session that closes the sprint.

## Observations

- `make lint` was red before the work, exit 2, with 17 finding lines (1 `schema`, 1 `deferred`, 15 `unread`). After the work it printed the same 17 lines, and it was not run in Retro.
- The checks of this session run from the working tree at once. The `SubagentStop` check of a Case file now judges unlisted tags, the pairs of the session in order and the read of each sentence. The ledger hook judges the tags of a lesson. The `shellwrite` hook fires only once the render writes `.claude/settings.json`.
- The read check of 711.3 compares the text a `Read` returned with the sentence. A sentence in a section of a page whose text differs from its Markdown file, such as a fenced Render, was not tried live.
- `git ls-files -m` lists a file whose only change is CRLF line endings under `* text=auto eol=lf`. This was tried in a temporary repository.
- At `/pre-spec`, the `Stop` check once refused the showing of Case 705 because its file differed from the stored text. Its `case-guppi` restored the file, and the showing went through on the second try. What changed the file was not found.
- `ask-guppi` at pre-spec searched the Estimates three times by Grep over their text, not through the `estimates` field, and said so. Two of its findings rest on those searches.

## For the next session

- Taking back the whole decision of a ratified Case is left not done (Case 705, Q1).
- No check sends back a Case that sets an Insight `actioned` with no `addressed_by` before ratification; `make lint` stays the only signal (Case 706, Q2).
- The `method` of `estimate-orchestration-shows-the-frontier-after-a-closed-line` waits for a later session, so the next Case that changes it leaves it `failed` at its own Retro (C7).
- `addressed_by` of a Case of the same session cannot be the quoted wikilink the schema asks for, because the check of the Case file refuses a link to a decision not yet written. One of the two needs a decision.

## Ask the person
