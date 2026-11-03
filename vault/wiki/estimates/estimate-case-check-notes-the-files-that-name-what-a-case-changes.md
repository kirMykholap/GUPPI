---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the check of the file of a Case sends case-guppi one note that lists each file that names a page the Case changes or the file in the first code span of a task line and that the agent did not read, with the purpose line of a page, however many files hold a name, each file listed once for the Case
method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py, passed and not skipped
checked: 2026-11-03
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
**＋** It sends one note that names the Case and lists each file that holds a name and that the subagent, in `agent_transcript_path`, read by no `Read` call of the file and no `Grep` call whose `path` is the file, once, under the first name it holds, with, for a page, its `purpose`, `root_cause` or `pattern` line, however many files hold the name.
**＋** The note asks the agent to read each listed file whose purpose line or path speaks of what the Case changes, or to name it in `context` with the reason it stands.
**＋** The note is sent by exit 2 beside any findings and stored under `notes` in `<plan>.checked.json`; a later check of the same Case id lists only the files that no earlier note of that id listed, and sends no note when none is left.
**－** A later code span of a task line and a code span of a sub-point name no changed file.
**－** The note leaves out the file of the page or the file itself, the pages under `vault/wiki/decisions/`, `log.md` and `brief.md`.
**－** A note is no finding: the `Stop` check of `guppi casecheck` refuses no showing for it, and a transcript the hook cannot read gives no such note.

## Result

2026-11-03, uv run --project .guppi pytest .guppi/tests/test_casecheck.py: 254 passed, none skipped; the tests of the note of names read one note per Case with the first line of NAMES_ASK and a line per unread file, 21 files that name rule-x in one note each on its own line with its purpose line, a file listed once under the first name it holds, a later check of the same Case id listing only rule-n0.md and sending no note when none is left, the Decision pages, log.md and brief.md left out, and no note with no transcript; read against the Criterion of Case 1011.1 in vault/raw/2026-11-02/2155/spec.md

## History

- 2026-11-02 created · [[decision-case-1005.1]]
- 2026-11-02 status: pending → passed · raw/2026-11-02/1548/ledger.md#L10
- 2026-11-02 updated: the Criterion replaced whole — only the first code span of a task line names a changed file · [[decision-case-1010.1]]
- 2026-11-02 status: pending → passed · raw/2026-11-02/2035/ledger.md#L10
- 2026-11-03 updated: the Criterion replaced whole — one note lists every unread file, with no limit of files · [[decision-case-1011.1]]
- 2026-11-03 status: pending → passed · raw/2026-11-02/2155/ledger.md#L18
