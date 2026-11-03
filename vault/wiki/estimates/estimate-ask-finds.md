---
type: estimate
kind: QA
status: passed
target: "[[rule-ask]]"
purpose: Whether ask-guppi answers the questions of /pre-spec with one line on what it read, one numbered list of findings under each question and nothing else under it, each finding naming its Case and the page or Cases it bears on, then a list of what it did not check ending with a line per search rule it broke, of its frame or of .claude/rules/search-leaves-out-decisions.md, and a list of the paths of the files it read, and nothing else
method: "by hand, after a /pre-spec whose ask-guppi runs on the rendered .claude/agents/ask-guppi.md: the answer of ask-guppi in its agent transcript read against the Criterion and the event log, recorded in the estimate line"
checked: 2026-10-30
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` through the `Agent` tool with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

Then:
The answer opens with one line that names what the agent read: the plan file, or the Spec that the plan's title line names, and the Cases it checked.
**＋** Then stands one numbered list of findings under each question that `.claude/skills/pre-spec/SKILL.md` sets, in the order of that file.
**＋** Each finding names its Case and the page or the Cases it bears on; a question with no finding says "none".
**＋** A finding that names a page carrying `deferred_by` names the Decision that field names by its slug and quotes none of its text.
**＋** After the findings stands one list of what the questions ask that the agent did not check. The list says "none" when the agent checked all of it and its searches broke no rule of `.claude/agents/ask-guppi.md` or of `.claude/rules/search-leaves-out-decisions.md`. Its last lines name each rule of those files that a search broke, one line each, and say whether a finding rests on what that search printed. Then stands a list of the paths of the files the agent read.
**＋** The dispatch stands in `vault/raw/<date>/event_log.md`.
**－** The findings are not put under the lines `exists`, `near`, `missing`, `rules` and tags/slug: those lines answer a question whether a thing exists.
**－** `.claude/agents/ask-guppi.md` does not list the questions of `/pre-spec` itself.
**－** Nothing but its numbered findings, or "none" alone, stands under a question. No sentence says what the agent checked and found sound, and this includes a clash with another Case that it did not find.
**－** No summary of the findings, no list of what holds, no index line and no page text reaches the caller.
**－** An answer with no list of paths holds the promise as well.

## Result

2026-10-30, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
