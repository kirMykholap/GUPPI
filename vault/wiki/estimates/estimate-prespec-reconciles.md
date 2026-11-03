---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
method: "by hand at Retro of the session that changes it: the new Render of rule-prespec and rule-ask in the Spec, read against the Criterion, recorded in the estimate line"
checked: 2026-11-02
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
The person invokes `/pre-spec`, or the agent calls the skill, before the Spec is approved, with `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec` and `.claude/agents/ask-guppi.md` rendered from `rule-ask`.

Then:
The agent runs `uv run --project .guppi guppi prespec --check` on the plan file with `--session <id>`, the eight-character id of the `hi:` line, and reads the first line of the output before the exit code — "no hi recorded for session …; nothing checked" means the wrong value; nothing is translated before the run.
**＋** A finding in a Case — in its prose or in its body, a wrong fact of its `context` included — goes to the `case-guppi` of that Case by `SendMessage`; its new answer is shown and ratified again, and the hook of `rule-spec-write` writes it into the plan; the agent does not edit the text of a Case in the plan file.
**＋** A finding in `vault/raw/<date>/<hi HHMM>/frontier.md` or in a line of the session's ledger is fixed there, and the command runs again until it prints no finding.
**＋** At the first run of `/pre-spec` in the session, the agent dispatches one `ask-guppi` over the plan, or over the conserved Spec that the plan's title line names, as `rule-skill-hi` sets that line, with the absolute path of the plan file, the instruction to judge every Case outside `## Deferred` with its sub-cases, and the instruction to read for each such Case its `context`, `when`, `then`, `then` block and `tasks` block and, for an `update` of a rule or an entity, the page's `estimates`; of a Case under `## Deferred` it reads only the slugs of its `defer` items.
**＋** The questions: which decisions contradict a page of the vault, a rule of the vault, or each other; whether an Estimate the Case does not name speaks of the thing the Case changes; which fact of a `context` — a page's status, a count, a case number, a claim that no page holds a thing — the vault does not bear out; whether, for each Case of the plan with a line of its `tasks` block that adds a file that is no page of `vault/wiki/`, its `context` names each search and reading that `.claude/agents/case-guppi.md` sets for the folders that hold that file, and which reader that takes every file of such a folder the Case does not name; and whether the `When` or `Then` of a Criterion a Case sets asks someone to read or see what only a later session, the librarian's run or a `/hi` produces, when the `method` of that Estimate, in the plan or else on its live page, cannot take that reading in the Case's own session.
**＋** The agent answers the findings with one report before any Case is sent back: the list of what the `ask-guppi` run did not check; each finding numbered, with the fix it proposes or why it is already known, the findings that need the person apart from those that do not, and the decisions it needs from the person; after the Cases built again on the findings are ratified, it does not call `/pre-spec` again, but runs the check, fixes what it prints, and exits Plan Mode when the check prints no finding.
**＋** `guppi gate` writes the stamped `prespec` line on the Skill call.
**－** The last question finds nothing where a part of the `method` waits for an event it names that brings that reading, nor in the Criterion of an Estimate whose target is a sprint page `entity-sprint-<id>`, whose `method` may wait for a later session of its sprint.
**－** No second `ask-guppi` is dispatched at the first run, and a later run of `/pre-spec` in the session dispatches none.
**－** The report never says that the whole Spec is checked.
**－** The agent writes no list of the decisions: the plan is the list.
**－** The body of a deferred decision is not read, and `ask-guppi` is not asked whether a Case changes a page that another Case of the plan defers: `uv run --project .guppi guppi prespec --check` notes such a pair at every run, as `estimate-prespec-notes-a-page-another-case-defers` sets it.

## Result

2026-11-02, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
