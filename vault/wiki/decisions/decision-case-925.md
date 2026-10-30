---
type: decision
case: "925"
status: current
children: ["[[decision-case-925.1]]", "[[decision-case-925.2]]", "[[decision-case-925.3]]", "[[decision-case-925.4]]", "[[decision-case-925.5]]", "[[decision-case-925.6]]"]
origin: raw/2026-10-30/0304/ledger.md#case-925
sprint: plugin
created: 2026-10-30
tags: [hooks, harness, session, workflow, render, prespec]
---

## Problem

A rule that only the agent's judgment holds failed twice: `ask-guppi` read a Decision page for a reason its frame does not name, and the stricter text of case 800.2 did not stop the second read.

## Recommend

- **How should a Decision read outside the frame of ask-guppi be stopped?**
  - Recommended: (a) a hook refuses every Decision read by `ask-guppi`, and the text drops its reasons: a finding or answer line on a put-off page names the Decision by its slug.
  - Answer: agreed, (a).
- **Where does the refusal of a Read run?**
  - Recommended: (a) the search guard `grepguard` also runs on Read.
  - Answer: agreed, (a).
- **One Case or one part per promise?**
  - Recommended: (a) five parts, one per promise.
  - Answer: agreed, (a).
- **How is the refusal checked?**
  - Recommended: (a) a new check, `estimate-search-leaves-out-decisions-refuses-ask-guppi`.
  - Answer: agreed, (a).
- **How is the new text of ask-guppi checked?**
  - Recommended: (a) rewrite the conditions of `estimate-ask-opens-a-decision-only-for-a-finding`, with its purpose and method.
  - Answer: agreed, (a).
- **Change**
  - Asked: the `/pre-spec` report, which the person agreed to, asked to put the pointers of the new texts in brackets of their own, to read the live refusal from the first `/pre-spec` after the render instead of a dispatch by hand, to set the Insight `actioned`, to settle the glossary rows and the schema line on `deferred_by`, to settle `estimate-page-read-cuts-the-history`, and to say which hook answer holds on a refused Read.
  - Taken: the pairs and methods rewritten; the `method` of the new check waits for that `/pre-spec`; Case 925.1 sets the Insight `actioned`; `context` says why the glossary rows and the schema line stand; Case 925.6 adds one exception line to the Criterion of `estimate-page-read-cuts-the-history`; `context` gives the order of precedence of the hooks documentation.

## History

- 2026-10-30 created · raw/2026-10-30/0304/ledger.md#case-925
