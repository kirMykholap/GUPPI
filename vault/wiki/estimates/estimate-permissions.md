---
type: estimate
kind: QA
status: passed
target: "[[rule-permissions]]"
method: the allow list of the rendered .claude/settings.json against the Criterion, and the JSON case of tests/test_render.py; the live probe is the person's word on the client's prompt at a Write of work.md in Work Mode, recorded in the estimate line; the live probe of the transcripts and of the mode of case-guppi is the person's word on the client's prompt, in a session after the librarian's render, at a Grep of a subagent whose path is the folder ~/.claude/projects/c--PROJECTS-GUPPI itself and at one whose path is a file under it, at the Write of the Case file of case-guppi, and at a Read of case-guppi on a path outside the project that no rule names, recorded in the estimate line — never the agent's, which cannot see the prompt; the Estimate stays pending until the person gives that word
checked: 2026-10-07
origin: raw/2026-09-12/ledger.md#case-85.5
sprint: migration
created: 2026-09-12
tags: [harness, session]
---

## Criterion

When:
The agent writes or edits a working file of the session — `frontier.md`, `spec.md`, `handoff.md`, `work.md` or `carry.md` under `vault/raw/**` — or `vault/wiki/brief.md`; or `case-guppi` writes the file of its Case.
**＋** Or an agent of the session, `case-guppi` among them, calls Read, Grep or Glob with the folder `~/.claude/projects/c--PROJECTS-GUPPI` itself as its path, or a path under it.
**＋** Or `case-guppi` calls Read, Grep or Glob on a path outside the project that no rule of the allow list names.

Then:
The allow list of `.claude/settings.json` holds Edit and Write for `frontier.md`, `spec.md`, `handoff.md` and `work.md` under `vault/raw/**`, Write for `carry.md` under `vault/raw/**`, Edit and Write for `vault/wiki/brief.md`, `Read(~/.claude/projects/c--PROJECTS-GUPPI)` and `Read(~/.claude/projects/c--PROJECTS-GUPPI/**)`.
**＋** `.claude/settings.json` is rendered from `rule-permissions`; the JSON case of `tests/test_render.py` fixes the shape of the block.
**＋** Whether the client asked is seen by the person only; the agent's reply does not tell an approved call from one not asked.
**＋** The client's prompt is the person's word: the reading line records whether the client asked, from the person, never from the agent.
**＋** In Plan Mode the client asks before every edit of the main agent outside the plan file, allow list or not.
**＋** A Read, Grep or Glob whose path is `~/.claude/projects/c--PROJECTS-GUPPI` itself or a path under it runs with no prompt, in Plan Mode too.
**＋** `case-guppi` writes the file of its Case with no prompt in Plan Mode, and its Read, Grep or Glob on a path outside the project that no rule of the allow list names runs with no prompt to the person.
**－** A prompt in Plan Mode on an edit of the main agent, approved by the person, is not a finding and not a `failed`.
**－** `deny` and `ask` are empty; nothing else under `vault/wiki/` is allowed, no path under `cases/` is on the allow list, no other path outside the project is on it, and no Edit or Write rule names `~/.claude/projects/c--PROJECTS-GUPPI`.

## Result

2026-10-07, Plan Mode of session 0636, the person's word: no permission prompt came while case-guppi built and wrote the files of Cases 703–708, in permissionMode auto; the agent did not count which paths those dispatches read; the person: "A1 я думаю passed. Никаких разрешений не было"

## History

- 2026-09-12 created · [[decision-case-85.5]]
- 2026-09-13 status: pending → passed · raw/2026-09-13/ledger.md#L47
- 2026-09-16 updated: the Criterion replaced whole by case 200.5 — nine allow entries, carry.md and brief.md among them (case 200.5) · [[decision-case-200.5]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L39
- 2026-09-17 updated: the Criterion replaced whole by the facts — nine entries named, the given and when about permissions; method as a field, the old sections dropped (case 215) · [[decision-case-215]]
- 2026-09-17 status: pending → passed · raw/2026-09-16/2238/ledger.md#L38
- 2026-09-18 updated: the Criterion replaced whole — the prompt is read by the person, a prompt in Plan Mode is not a finding (case 237) · [[decision-case-237]]
- 2026-09-18 status: pending → passed · raw/2026-09-18/1252/ledger.md#L12
- 2026-09-28 updated: the Criterion replaced whole — Edit and Write for work.md join the allow list (case 479.5) · [[decision-case-479.5]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/1736/ledger.md#L3
- 2026-10-05 updated: the Criterion replaced whole — the prompt in Plan Mode binds the main agent, and case-guppi writes its Case file with no prompt and no allow rule (case 645.16) · [[decision-case-645.16]]
- 2026-10-05 updated: the Criterion replaced whole — the allow list holds a Read rule for this project's saved transcripts, and a search of case-guppi there runs with no prompt (case 656) · [[decision-case-656]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/1831/ledger.md#L9
- 2026-10-07 updated: the Criterion replaced whole — the allow list also names the folder of the saved transcripts itself, and a search with that folder as its path runs with no prompt · [[decision-case-693]]
- 2026-10-07 updated: the Criterion replaced whole — case-guppi runs in permissionMode auto beside the read rules of the saved transcripts, and a call they do not match is judged by that mode with no prompt (case 698) · [[decision-case-698.2]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/0636/ledger.md#L12
