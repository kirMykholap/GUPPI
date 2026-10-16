---
type: decision
case: "871"
status: current
create: ["[[estimate-case-build-checks-a-fact-of-an-outside-tool]]"]
update: ["[[rule-case-build]]", "[[insight-case-build-rests-on-an-unchecked-fact-of-a-tool]]"]
origin: raw/2026-10-16/2104/ledger.md#case-871
sprint: plugin
created: 2026-10-16
tags: [session, workflow, harness, case-build, tests, ci]
---

## Problem

`case-guppi` recommends options that rest on how a tool outside the repository behaves, with no means and no duty to check that behaviour. The fact proves false only in Work Mode, after the person ratified the Case, and the Case is built and ratified again.

## Recommend

- **What do we do with this Insight?**
  - Recommended: (a) act on it: `WebFetch` joins the tools of `case-guppi`, which reads the documentation of the tool before it recommends an option that rests on it and gives the address of the page in `context`.
  - Answer: agreed, (a).
- **What if the documentation does not settle the fact?**
  - Recommended: (a) the option's `**After:**` line and `context` say that the fact is not checked, and the option is not recommended; where each option rests on the fact, the round says so and the person decides.
  - Answer: agreed, (a).
- **Does `/pre-spec` check it too?**
  - Recommended: (a) no, only `rule-case-build` changes.
  - Answer: agreed, (a).
- **How is the change checked?**
  - Recommended: (a) a new Estimate `estimate-case-build-checks-a-fact-of-an-outside-tool`, read at the Retro of this session.
  - Answer: agreed, (a).

## History

- 2026-10-17 created · raw/2026-10-16/2104/ledger.md#case-871
