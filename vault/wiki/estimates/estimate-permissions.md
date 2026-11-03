---
type: estimate
kind: QA
status: passed
target: "[[rule-permissions]]"
method: "the allow list of the rendered .claude/settings.json against the Criterion, and the JSON case of .guppi/tests/test_render.py; by hand, after a Case file that case-guppi writes in Plan Mode: the person's word on whether the client asked at that write, and at a Grep of a subagent whose path is the folder of the project's saved transcripts itself and at one whose path is a file under it, recorded in the estimate line, never the agent's, which cannot see the prompt"
checked: 2026-10-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, session]
core: true
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

2026-10-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
