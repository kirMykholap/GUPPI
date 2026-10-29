---
type: estimate
kind: QA
status: pending
target: "[[rule-permissions]]"
method: "the allow list of the rendered .claude/settings.json against the Criterion, and the JSON case of .guppi/tests/test_render.py; by hand, after a Case file that case-guppi writes in Plan Mode: the person's word on whether the client asked at that write, and at a Grep of a subagent whose path is the folder of the project's saved transcripts itself and at one whose path is a file under it, recorded in the estimate line, never the agent's, which cannot see the prompt"
checked: 2026-10-29
origin: raw/2026-09-12/ledger.md#case-85.5
sprint: migration
created: 2026-09-12
tags: [harness, session]
---

## Criterion

When:
The agent writes or edits a working file of the session — `frontier.md`, `spec.md`, `handoff.md`, `work.md` or `carry.md` under `vault/raw/**` — or `vault/wiki/brief.md`; or `case-guppi` writes the file of its Case.
**＋** Or an agent of the session, `case-guppi` among them, calls Read, Grep or Glob with the folder of saved transcripts under `~/.claude/projects/` that the Render of `rule-permissions` names, that folder itself as its path or a path under it.

Then:
The allow list of `.claude/settings.json` holds Edit and Write for `frontier.md`, `spec.md`, `handoff.md` and `work.md` under `vault/raw/**`, Write for `carry.md` under `vault/raw/**`, Edit and Write for `vault/wiki/brief.md`, a Read rule for the folder of saved transcripts that the Render of `rule-permissions` names, and a Read rule for the paths under it.
**＋** `.claude/settings.json` is rendered from `rule-permissions`; the JSON case of `.guppi/tests/test_render.py` fixes the shape of the block.
**＋** Whether the client asked is seen by the person only: the reading line records it from the person, never from the agent, whose reply does not tell an approved call from one not asked.
**＋** In Plan Mode the client asks before every edit of the main agent outside the plan file, allow list or not.
**＋** A Read, Grep or Glob whose path is that folder itself or a path under it runs with no prompt, in Plan Mode too.
**＋** `case-guppi` writes the file of its Case with no prompt in Plan Mode, since the guard of `rule-spec-reconcile` makes the write and stops its call.
**－** A prompt in Plan Mode on an edit of the main agent, approved by the person, is not a finding and not a `failed`.
**－** An error of the guard of `rule-spec-reconcile` while it writes that file lets the call run, and the client may ask the person that one time; that prompt is not a finding and not a `failed`.
**－** A Read, Grep or Glob of `case-guppi` on a path outside the project that no rule of the allow list names is not bound by this Criterion: it may ask the person.
**－** `deny` and `ask` are empty; nothing else under `vault/wiki/` is allowed, no path under `cases/` is on the allow list, no other path outside the project is on it, and no Edit or Write rule names that folder.

## Result

2026-10-29, Plan Mode of session 2312: the allow list of .claude/settings.json holds the thirteen entries of the Criterion, with no deny and no ask; uv run --project .guppi python -m pytest .guppi/tests/test_render.py -k "json or permission": 4 passed; case-guppi wrote and edited the files of Cases 896 and 897 through the guard of rule-spec-reconcile (two Write and twelve Edit calls, each written by the guard); the main agent ran Grep with paths under ~/.claude/projects/c--PROJECTS-GUPPI (the session folder and its subagents folder); no subagent called Grep with that folder itself as its path in this session; the person: "не спрашивал, все ок"

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
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-17 updated: the method names the folder of the project's saved transcripts by its role · [[decision-case-875]]
- 2026-10-28 updated: the Criterion replaced whole — case-guppi writes its Case file with no prompt in Plan Mode by the guard of rule-spec-reconcile, and a read outside the project that no rule names is not bound; the method follows (case 894.2) · [[decision-case-894.2]]
- 2026-10-29 status: pending → passed · raw/2026-10-28/2312/ledger.md#L18
- 2026-10-29 updated: method names a kind of moment, not the first Case file after a past change of the guard · [[decision-case-898.2]]
- 2026-10-29 updated: the Criterion replaced whole — the transcripts folder is named as the one the Render of rule-permissions names, not by the folder name of the repository of GUPPI · [[decision-case-908.1]]
