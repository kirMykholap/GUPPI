---
type: decision
case: "646"
status: current
create: ["[[estimate-case-protocol-example-passes-the-check]]"]
update: ["[[rule-case-protocol]]"]
origin: raw/2026-10-05/0311/ledger.md#case-646
sprint: migration
created: 2026-10-05
tags: [session, workflow, harness, ledger]
---

## Problem

The Case schema describes the chat form in prose and shows no example of it. The agent writes forms that the check sends back, even where the prose states the rule. The question was how the schema shows the form without an untested second copy of the checks, whether this Case also fixes the page's wording about the agent's answer, and what happens to the Insight.

## Recommend

- **How the page describes the form**
  - Recommended: (a) a worked example, kept true by a test: one example Case in the form `case-guppi` writes, with a sub-case, `old` and `new` pairs, a padded value with a backtick, a fenced `set`, a `create` with its fields, a `given` that names each path its `when` and `then` use, and a `ratification` fence. A test runs the stop check over it and fails on any finding, and a new Estimate stands on that test. The prose limits stay.
  - Answer: agreed, (a).
- **The word "answer" on the page**
  - Recommended: (a) fix them in this Case, on `case-schema.md` alone: its sentences speak of the file `case-guppi` writes and the text the check stored, and `orchestration.md` waits for a later Case.
  - Answer: agreed, (a).
- **What happens to the Insight**
  - Recommended: (b) leave the Insight open and untouched until a later Case covers the main agent's forms too.
  - Answer: agreed, (b).
- **Change**
  - Asked: the pre-spec check found that a test red in Work Mode cannot pass Retro. The person chose that the test is skipped, with a reason, while `case-schema.md` holds no `case` block, runs and passes after the librarian's render, and that a later Case removes the skip.
  - Taken: a `－` line of `then` sets the skip, and the test task and `context` follow.
- **Change**
  - Asked: the pre-spec check found that the example did not say what the sentence around its `replace` match names, and gave no update of `estimate-checkout-orders-the-steps` where the Spec example gives one. The person agreed to the recommended fix.
  - Taken: the example's `context` says what that sentence names, and Case 1.1 of the example updates and reads `estimate-checkout-orders-the-steps`.
- **Change**
  - Asked: the pre-spec check found that the paragraph before the example restated limits of the check, one of them wrongly, with no test behind it. The person agreed that the paragraph lists no limit.
  - Taken: the paragraph says only that the example passes the check of the `SubagentStop` hook and that the check is the source of the limits. The `then` line on a paragraph naming each limit is gone.
- **Change**
  - Asked: the pre-spec check found that the pairs on lines 68, 80 and 84 describe behaviours whose Estimates this Case did not name. The person agreed to name them and to leave them to the Cases that replace them.
  - Taken: `context` names `estimate-case-check-requires-a-backlog-item-decided-on-its-page` and `estimate-case-check-sends-back-a-ratified-case-in-another-shape`, left to Case 645, and `estimate-spec-write-copies-the-ratified-case`, left to 644.2.

## History

- 2026-10-05 created · raw/2026-10-05/0311/ledger.md#case-646
