---
type: estimate
kind: QA
status: passed
target: "[[rule-retro-commit]]"
purpose: guppi gate refuses /handoff on a dirty tree and /retro with nothing to review or a Spec ahead of the ledger, and marks each call it lets through
method: pytest in .guppi/tests/test_gate.py with piped payloads against a temp repository; the live reading once by hand
checked: 2026-09-30
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, hooks, harness, git]
core: true
---

## Criterion

When:
`guppi gate` receives a `PreToolUse` payload of a `Skill` call, or a `UserPromptSubmit` payload whose prompt, trimmed, opens with one of the three commands the gate marks, with or without arguments.

Then:
A `/handoff` on a dirty tree, where `git status --porcelain` is not empty, exits 2 with the reason "commit first" on stderr, and the client blocks the call; on a clean tree it exits 0.
**＋** A `/retro` in a session with a `hi` but no `spec.md` in its folder, no plan file named by the event log and no `- decision[`, `- estimate[` or `- lesson[` line in its window exits 2 with "gate: /retro refused — nothing to review: no Spec and no ledger line in raw/<date>/<HHMM>/. Ratify a Case or write a reading or a lesson first, then type /retro again."; on the `Skill` path the end reads "…first. This refusal is a stop of vault/wiki/where-to-stop.md: end your reply with the question to the person."
**＋** Otherwise a `/retro` whose Spec holds an item with no decision line of its Case exits 2 with "gate: /retro refused — N item(s) of the Spec have no ledger line (case A). Ask the agent to end its reply with the LEDGER block, then type /retro again".
**＋** A call it lets through, on either path, writes the same mark `prespec`, `retro` or `handoff` into the day's event log `vault/raw/<date>/event_log.md`; a refusal writes no mark.
**＋** Any other prompt or skill, `/hi` included, exits 0 with no output and no mark.
**－** Without a `hi` in the session, the checks of `/retro` do not run.
**－** On the `Skill` path the refusal "nothing to review" asks for no call in a next reply.

## Result

2026-09-30, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
