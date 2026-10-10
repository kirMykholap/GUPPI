---
type: decision
case: "450"
status: archived
update: ["[[estimate-agent-writing-followed]]"]
origin: raw/2026-09-27/1255/ledger.md#case-450
sprint: migration
created: 2026-09-27
tags: [harness, render, workflow]
---

## Context

`rule-agent-writing` renders the section `## How the agent writes` into `CLAUDE.md`: keep the facts, name a real source, make no claim wider than its output, write short active sentences, give the answer first, name what is not done. Its one promise, `estimate-agent-writing-followed`, is read by the agent against its own replies. Its last two readings failed. Each time, one claim in a long session did not match a file. In session 2300 a reply said the ledger gained amended lines of 445.6. The ledger hook runs after the reply and adds no line it already holds, so only the line of 445.7 was new. Another reply gave W32 a closer meant only for sprint items, and the next reply corrected it. The rule text already forbids both slips. The test failed, not the text.
The person decided the following. The section `## How the agent writes` stays as it is. The Criterion is replaced whole, and the person's complaint becomes the test, as Case 449 did for the story sections. A slip that the agent corrected itself is no fault. The W32 slip stays out of this Case, because the Frontier file never held the wrong closer. The form of the Frontier is promised by `estimate-hi-writes-frontier`. Its check, `estimate-prespec-checks-the-frontier`, is changed by Case 451.2 of this session, which also refuses a closer that does not agree with its source.
This Case creates no page, so no vault query was run. `CLAUDE.md` is rendered again by Case 452.5 for its `## Language` section. The section this rule renders does not change, so `estimate-claude-md-rendered` is not touched.

## Problem

The promise of `rule-agent-writing` rests on the agent reading its own replies. It fails whenever one claim in a long session slips, even a slip the agent corrected. No reading finds the text of the rule wrong. The test does not serve the person, who is the reader the rule exists for.

## Given

`estimate-agent-writing-followed` — the promise of the rule, whose Criterion this Case replaces whole
**＋** `rule-agent-writing` — the rule, whose Render is the section `## How the agent writes`
**＋** `CLAUDE.md` — the file the session loads, which holds that section

## History

- 2026-09-27 created · raw/2026-09-27/1255/ledger.md#case-450
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
