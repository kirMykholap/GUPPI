---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the check of the file of a Case sends case-guppi a note once for each file that names a page the Case changes or the file in the first code span of a task line and that the agent did not read, with its path, the name it holds and the purpose line of a page
method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py, passed and not skipped
checked: 2026-11-02
origin: raw/2026-11-02/1548/ledger.md#case-1005.1
sprint: plugin
created: 2026-11-02
tags: [hooks, harness, workflow, case-build]
---

## Criterion

When:
The `SubagentStop` hook `uv run --project .guppi guppi casecheck --subagent` of `.guppi/guppi/casecheck.py` checks a file `raw/<date>/<hi HHMM>/cases/case-<N>.md` that `case-guppi` wrote, whose Case updates or deletes a page, or writes in the first code span of a task line the path of a file of the repository outside `vault/wiki/`.
**＋** Or `.guppi/tests/test_casecheck.py` runs it over a made-up file, transcript, plan file and store.

Then:
The hook searches the files under `vault/wiki/`, `.claude/`, `.guppi/guppi/` and `.guppi/tests/` for every name of each such page and file.
**＋** The names of a page are its slug, the file name of each path of its `governs`, `implementation_ref` and `code_ref`, the name of the agent, or of the skill with its slash, whose file those paths name, and `guppi <command>` for each command that `COMMANDS` of `.guppi/guppi/cli.py` maps to a module of those paths.
**＋** The names of a file are its file name and the name of the agent, the skill or the command it carries.
**＋** A task line names a changed file only by its first code span, where that span holds the path of a file of the repository outside `vault/wiki/`.
**＋** For each file that holds a name and that the subagent, in `agent_transcript_path`, read by no `Read` call of the file and no `Grep` call whose `path` is the file, it sends a note that names the Case, the path, the name the file holds and, for a page, its `purpose`, `root_cause` or `pattern` line, and asks the agent to read the file or to name it in `context` with the reason it stands.
**＋** Each note is sent once by exit 2 beside any findings, stored under `notes` in `<plan>.checked.json`, and not sent again for the same Case id.
**－** A later code span of a task line and a code span of a sub-point name no changed file.
**－** A name that many files hold is checked by `estimate-case-check-sends-one-note-for-a-broad-name`, not here.
**－** The note leaves out the file of the page or the file itself, the pages under `vault/wiki/decisions/`, `log.md` and `brief.md`.
**－** A note is no finding: the `Stop` check of `guppi casecheck` refuses no showing for it, and a transcript the hook cannot read gives no such note.

## Result

2026-11-02, Retro of session 2035, uv run --project .guppi pytest .guppi/tests/test_casecheck.py: 254 passed, none skipped; test_names_note_takes_only_the_first_code_span_of_a_task_line gives a note for the path in the first code span and none for a later span or a sub-point, and the earlier tests of the note for each unread file pass on the Criterion of Case 1010.1

## History

- 2026-11-02 created · [[decision-case-1005.1]]
- 2026-11-02 status: pending → passed · raw/2026-11-02/1548/ledger.md#L10
- 2026-11-02 updated: the Criterion replaced whole — only the first code span of a task line names a changed file · [[decision-case-1010.1]]
- 2026-11-02 status: pending → passed · raw/2026-11-02/2035/ledger.md#L10
