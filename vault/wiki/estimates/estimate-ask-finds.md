---
type: estimate
kind: QA
status: pending
target: "[[rule-ask]]"
purpose: Whether ask-guppi answers the questions of /pre-spec with one line on what it read, one numbered list of findings under each question and nothing else under it, each finding naming its Case and the page or Cases it bears on, then a list of what it did not check ending with a line per search rule it broke, of its frame or of .claude/rules/search-leaves-out-decisions.md, and a list of the paths of the files it read, and nothing else
method: "by hand at the /hi of a later session: the answer of ask-guppi at a /pre-spec after the render of .claude/agents/ask-guppi.md by case 639, read in its agent transcript against the event log, recorded in the estimate line"
checked: 2026-10-05
origin: raw/2026-09-09/ledger.md#case-23.1
sprint: migration
created: 2026-09-09
tags: [session, workflow, harness]
---

## Criterion

When:
At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` through the `Agent` tool with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

Then:
The answer opens with one line that names what the agent read: the plan file, or the Spec that the plan's title line names, and the Cases it checked.
**＋** Then stands one numbered list of findings under each question of `.claude/skills/pre-spec/SKILL.md`, in its order: what contradicts a page, a rule or another Case; an Estimate a Case does not name that speaks of the thing the Case changes; a fact of a `context` the vault does not bear out.
**＋** Each finding names its Case and the page or the Cases it bears on; a question with no finding says "none".
**＋** A finding that names a page carrying `deferred_by` gives the `## Problem` of the Decision that field names.
**＋** After the findings stands one list of what the questions ask that the agent did not check. The list says "none" when the agent checked all of it and its searches broke no rule of `.claude/agents/ask-guppi.md` or of `.claude/rules/search-leaves-out-decisions.md`. Its last lines name each rule of those files that a search broke, one line each, and say whether a finding rests on what that search printed. Then stands a list of the paths of the files the agent read.
**＋** The dispatch stands in `vault/raw/<date>/event_log.md`.
**－** The findings are not put under the lines `exists`, `near`, `missing`, `rules` and tags/slug: those lines answer a question whether a thing exists.
**－** Nothing but its numbered findings, or "none" alone, stands under a question. No sentence says what the agent checked and found sound, and this includes a clash with another Case that it did not find.
**－** No summary of the findings, no list of what holds, no index line and no page text reaches the caller.
**－** An answer with no list of paths holds the promise as well.

## Result

2026-10-05, at the /hi of session 0109, by hand: the first answers of the two ask-guppi runs at the /pre-spec of session 2245 (transcript 7086b96c, agent aab5addf1e347ccb8 on Case 636 and agent a390781c7f1241c18 on Case 637; event log `23:55:12 7086b96c tool Agent: ask-guppi`, twice), after the render of .claude/agents/ask-guppi.md by case 633.1 in commit 3b31fb80: each opens with one line on the plan file and the Cases it checked; three numbered lists stand in the order of the questions (636: none, 1, 2 findings; 637: 1, 1, 2), each finding names its Case and the page or Cases it bears on, a question with no finding says "none"; a list of what was not checked, then the list of files read; but under question 1 both answers hold a paragraph of what holds, which the Criterion excludes — 636 after "none" ("The `old` text of the `replace` on `rule-case-build` ... stands word for word in its Render ..."), 637 after its finding ("No clash found between Case 637 and Case 636. They change different pages ..."); not exercised: a finding that names a page carrying deferred_by

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-23.1
- 2026-09-10 status: pending → passed · written by hand, no generator yet
- 2026-09-13 criterion: case 105.1 added · [[decision-case-105.1]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L39
- 2026-09-14 criterion: case 147.2 added · [[decision-case-147.2]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1110/ledger.md#L4
- 2026-09-29 updated: the Criterion replaced whole — the head and the blocks 105.1 and 147.2 into one When and Then, the one-time questions and the index files out; purpose and method set, Context and Method out (case 500.1) · [[decision-case-500.1]]
- 2026-10-01 status: pending → failed · raw/2026-10-01/1441/ledger.md#L33
- 2026-10-01 updated: the Criterion replaced whole — a list of file paths may follow the five lines, as the general note of Claude Code asks of a sub-agent; nothing else follows them (case 582) · [[decision-case-582]]
- 2026-10-04 status: pending → failed · raw/2026-10-04/0004/ledger.md#L17
- 2026-10-04 deferred · [[decision-case-623]]
- 2026-10-04 updated: the Criterion replaced whole — the dispatch at /pre-spec answered by one numbered list of findings under each question, not by the five lines, the Problem of a deferred page in its finding; the lines on a page asked in either language, a crossed rule and an archived slug moved to estimate-ask-query-before-a-create (case 626.1) · [[decision-case-626.1]]
- 2026-10-04 status: pending → failed · raw/2026-10-04/1934/ledger.md#L1
- 2026-10-04 updated: the Criterion replaced whole — one line on what was read before the findings, a list of what was not checked after them and before the paths, no summary and no list of what holds; the line on the searches moved to estimate-ask-searches-at-prespec (case 633.1) · [[decision-case-633.1]]
- 2026-10-05 status: pending → failed · raw/2026-10-05/0109/ledger.md#L8
- 2026-10-05 updated: the Criterion replaced whole — only findings or "none" under a question, no sentence on a clash not found; the list of what was not checked ends with a line per search rule broken, of the frame or of .claude/rules/search-leaves-out-decisions.md (case 639) · [[decision-case-639]]
