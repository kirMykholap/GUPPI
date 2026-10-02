---
type: decision
case: "433"
status: current
update: ["[[lesson-case-show-sub-case-ratification-retyped]]"]
origin: raw/2026-09-26/1337/ledger.md#case-433
sprint: migration
created: 2026-09-26
tags: [workflow, harness]
---

## Context

`casecheck` has two hooks. On `SubagentStop` it checks the answer of `case-guppi` and stores each Case in `<plan>.checked.json`. On `Stop` it compares the Case the main agent shows with the stored one. Only the function `stop` in `guppi/casecheck.py` prints the message `differs from the answer of case-guppi — show that answer unchanged`. That is the comparison on `Stop`. The showing of 428.3 in session 1654 got this message. The result of `estimate-case-check-shows-only-the-checked-case`, the result of `estimate-orchestration-shows-the-built-case` and the handoff say so. But the `## Trigger` of the page `lesson-case-show-sub-case-ratification-retyped` names the comparison on `SubagentStop`. The page states a thing that did not occur.

The ledger line the page came from, its entry in the `materialize.yaml` of session 1654, the handoff and the brief are records. They stay as they are. The words of the handoff "the line stands as written" are about the ledger line and stay true: the Case changes only the page. `root_cause` and `## Root cause` are correct and do not change. A Grep of `SubagentStop comparison` over `vault/wiki/` found the phrase only on the lesson page and in `brief.md`, and the librarian writes the brief again at each run. `generate` applies `replace` to a page of any category. A pair whose `old` comes only from `## Trigger` matches once.

What `case-guppi` found in the frame. `rule-lessons-schema` says a lesson is "a recorded fact", it "does not go through a Case", and "nothing … is checked again" about it. These sentences describe how a lesson is born and that it has no Estimate. The Case does not create a lesson and does not add an Estimate to it. It corrects the account of a fact against the code, so these sentences stay true. The lesson has no Estimate. `estimate-lessons-schema-checked` promises the form of a lesson page, and the form does not change. `estimate-case-check-sends-back-a-faulty-case` and `estimate-case-check-shows-only-the-checked-case` promise the behaviour of the hooks, and it does not change. So no Estimate is touched.

This Case closes C4 of the Frontier.

## Problem

The `## Trigger` of the lesson names a check other than the one that refused the reply. A reader of the lesson will look for the cause in the check on `SubagentStop`, but the comparison on `Stop` refused the reply. The decision is whether to correct the page or to keep it as written.

## Given

`lesson-case-show-sub-case-ratification-retyped` — the lesson of the retyped ratification of a sub-case
**＋** `rule-case-check` — the rule of the two `casecheck` hooks: the check on `SubagentStop`, the comparison on `Stop`
**＋** `rule-lessons-schema` — the `## Trigger` of a Lesson holds the full account of what happened

## History

- 2026-09-26 created · raw/2026-09-26/1337/ledger.md#case-433
