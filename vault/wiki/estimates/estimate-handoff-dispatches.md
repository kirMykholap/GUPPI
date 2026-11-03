---
type: estimate
kind: QA
status: passed
target: "[[rule-handoff]]"
purpose: /handoff stops on a dirty tree, writes handoff.md from memory into the session's folder, dispatches the librarian with its path, shows report.md and commits it alone after the librarian's commit, or, in a session that /box runs, hands back to /box
method: "by hand, after a /handoff whose .claude/skills/handoff/SKILL.md holds the Render of rule-handoff that commits report.md: the event log vault/raw/<date>/event_log.md, handoff.md and git log, and the dispatch line and the text shown to the person read in the transcript of that session under ~/.claude/projects/, against the Criterion, the transcript named in the estimate line; by hand, after a /handoff in a session that /box runs: the event log, and the step of /box that follows read in the transcript of that session under ~/.claude/projects/, against the Criterion, the transcript named in the estimate line"
checked: 2026-11-01
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
The agent calls `/handoff` on `PreToolUse Skill` after the reply that ends Retro, or the person types `/handoff` on `UserPromptSubmit`, the gate of `.guppi/guppi/gate.py` reads the tree, and the agent runs the skill `.claude/skills/handoff/SKILL.md` as rendered from `rule-handoff`.

Then:
The skill's context holds `git status --porcelain`. On a dirty tree the skill stops and says "commit first", and nothing is written.
**＋** On a clean tree the day's event log `vault/raw/<date>/event_log.md` holds the `handoff` mark of the call.
**＋** The agent writes `handoff.md` into the session's folder `vault/raw/<date>/<hi HHMM>/`: one document with no `---` and the sections that `rule-handoff` names, with no Read call on the artifacts.
**＋** Then the agent dispatches `librarian-guppi` with one line, `Materialize <date> from <path of handoff.md>.`, the path being that of the file just written.
**＋** After the librarian's report, the agent shows the text of `vault/raw/<date>/<hi HHMM>/report.md` unchanged, or, when no `report.md` stands there, the returned report unchanged and one line that says that `report.md` is missing.
**＋** When `report.md` stands, the agent commits it alone, in one commit after the librarian's, with the message `docs(vault): librarian report, <date>`, and never with `--amend`.
**－** In a session whose `raw/<date>/<hi HHMM>/work.md` holds `## Conserved Spec` — one that `/box` runs — the agent dispatches nothing after `handoff.md` and goes back to the step of `/box` that follows `/handoff`.
**－** No commit follows the handoff but the librarian's and the commit of `report.md`, and no reply between the call and the librarian's report carries a `LEDGER` block.

## Result

2026-11-01, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
