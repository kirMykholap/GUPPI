---
type: estimate
kind: QA
status: passed
target: "[[rule-compact-recall]]"
purpose: After a compaction of a working session the hook's header, the paths of the /hi files, the Spec and the Frontier's text stand in the context; an ordinary session and another source get nothing
method: pytest tests/test_recall.py on a temp project; live — the first compaction of a working session, by hand, the hook's text in the context after it
checked: 2026-09-22
origin: raw/2026-09-21/0019/ledger.md#case-287
sprint: migration
created: 2026-09-21
tags: [session, hooks, harness]
---

## Criterion

Given:
`SessionStart` fires after a compaction with `source: compact`; the hook's stdout on exit 0 enters the context as text; output over 10,000 characters is saved to a file and the agent gets a preview and the path (Claude Code docs, hooks guide).
**＋** A `SessionStart` hook cannot block (`lesson-hooks-sessionstart-cannot-block`).
**＋** The session's window and folder are the ones the ledger hook finds: `session_dir` in `guppi/ledger.py`, the first `hi` of the stamp after its first `session-start`; `compact` does not close the window (case 14).
**＋** The files `/hi` imports are the `@` lines of `.claude/skills/hi/SKILL.md`, the Render of `rule-internal-context`; the glossary joins them by C4.1.
**＋** The Spec of a session is `spec.md` in its folder after the approval; before it, the plan file the event log names last under `.claude/plans/`, as `guppi gate` reads it (case 122).
**＋** `tests/test_recall.py` fixes the behaviour on a temp project with an event log, a skill file and a session folder.

When:
The client compacted the context of the session — `/compact` or on its own — and `SessionStart` fired with `source: compact`.

Then:
With a `hi` in the session's window, stdout holds: the line `recall: the context was compacted at HH:MM:SS; the session is raw/<date>/<HHMM>/. Read before the next reply:`; then one path per line — the `@` files of the `/hi` skill in their order, the session's `frontier.md` when it exists, the Spec when one exists; then the line `Frontier:` and the text of `frontier.md` as it stands.
**＋** The list of paths is the `@` lines of the skill file at the moment the hook fires, no copy in the code: a file added to `rule-internal-context` — the glossary by C4.1 — is in the list without a change to the hook.
**＋** The texts of the files, the Frontier apart, are not printed — the paths only; the output stays under 10,000 characters.
**－** Without a `hi` in the window — nothing on stdout, exit 0.
**－** Another `source` — nothing: the matcher keeps the hook from firing, and the code checks `source` itself.
**－** Exit 0 always; an error prints nothing and blocks nothing; the hook writes no file and no event line — `session-start compact` is already written by `guppi event`.

## Result

2026-09-22, uv run pytest tests/test_recall.py, 7 passed: with a hi in the window the hook prints the recall header, the @ paths of the /hi skill in order, frontier.md and the Spec when they exist, then Frontier: and its text; a fourth @ line of the skill is a fourth path; the Spec is the plan file before the approval and spec.md after; without a hi, on another source or on a payload that is not JSON — nothing, exit 0; the live leg, the first compaction of a working session by hand, not taken

## History

- 2026-09-21 created · [[decision-case-287]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/0014/ledger.md#L2
