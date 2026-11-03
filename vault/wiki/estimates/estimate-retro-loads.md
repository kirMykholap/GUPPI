---
type: estimate
kind: QA
status: passed
target: "[[rule-retro]]"
method: by hand, the text of .claude/skills/retro/SKILL.md as rendered, or, at the Retro of the session that changes it, the new Render of rule-retro in the Spec, read against the Criterion, recorded in the estimate line
checked: 2026-10-12
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
The agent calls `/retro` of `.claude/skills/retro/SKILL.md` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, and the agent takes the readings of the session's Estimates.

Then:
A reading measures the Criterion the page carries at the moment of the reading — the one ratified last; its line is written only when the work that Criterion names is built.
**＋** Each Estimate this session creates or updates — by a decision line of its slug, or by an `update` that renames a page to it — is read in the reply that ends Retro, on the Criterion of `raw/<date>/<hi HHMM>/spec.md`: the `when` and `then` of its Case, or the Criterion its item writes.
**＋** For an Estimate of a rule whose Render a Case of the Spec changes, the reading reads the new text of the Render in `raw/<date>/<hi HHMM>/spec.md` against that Criterion.
**＋** Each such Estimate that Retro cannot read gets a `failed` line in the same `LEDGER` block, whose result opens with the date and says that Retro did not read it and why.
**＋** When `raw/<date>/<hi HHMM>/work.md` holds `## Conserved Spec`, the Spec is the `spec.md` of the folder that section names, and the decision lines of that folder's `ledger.md` count as this session's for its boxes, for the scope of an edit and for the readings above.
**＋** Retro closes the open `W` line of each Estimate it reads or sets `failed` `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`.
**－** An Estimate whose `target` is the live sprint page `entity-sprint-<id>` and whose work is not done yet is neither read, nor put to the person, nor set `failed`: it stays `pending` for the Retro of the session that finishes its work or for the closing Case of `/sprint-close`, and its `read` box in `raw/<date>/<hi HHMM>/spec.md` waits for that moment, neither debt nor the librarian's.
**－** Once its work is done, the Retro of that session reads it, or, when its `method` names the person's answer, names it under `## Ask the person` of `raw/<date>/<hi HHMM>/handoff.md`.
**－** An Estimate this session creates or updates whose `method` waits for an event — a part of it that opens with `after`, or with `by hand, after`, and names the event before a colon — and whose event has not come in this session is neither read, nor put to the person, nor set `failed`: it stays `pending`, its `read` box in `raw/<date>/<hi HHMM>/spec.md` waits for that event, neither debt nor the librarian's, and when the event came in this session Retro reads it.
**－** An Estimate whose `update` sets `passed` or `failed` by the person's decision and writes its Criterion back unchanged, and one whose `update` names one part of the page alone, is neither read nor set `failed`.
**－** A reading whose `method` names the person's word is not taken: it is a line of `## Ask the person` of `raw/<date>/<hi HHMM>/handoff.md`, with its question, and its `read` line is neither debt nor the librarian's.
**－** A reading of an Estimate this session neither creates nor updates is taken as before, once its work is built.

## Result

2026-10-12, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
