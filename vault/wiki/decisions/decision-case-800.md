---
type: decision
case: "800"
status: current
children: ["[[decision-case-800.1]]", "[[decision-case-800.2]]"]
origin: raw/2026-10-13/1753/ledger.md#case-800
sprint: plugin
created: 2026-10-13
tags: [session, workflow, harness]
---

## Problem

Two agents read a gap in their frame as permission. `case-guppi` closed the check of a sub-case on an answer that named no Estimate. `ask-guppi` opened a Decision page before any finding of its own named the page.

## Recommend

- **How should case-guppi stop reading "no new Estimate" as "no Estimate"?**
  - Recommended: (a) the question on the promise names the existing Estimate by slug, and an answer of no new Estimate closes the promise only with that Estimate named in `context`.
  - Answer: agreed, (a).
- **When may ask-guppi open the Decision behind a put-off page during the review?**
  - Recommended: (a) restrict the rule: at /pre-spec, the Decision is opened only after a finding names the page, never to judge whether a finding stands.
  - Answer: (a). In the first round the person asked why the agent opened that Decision at all, and whether the agent or the rule should be restricted.
- **Should the two fixes be one Case with two parts, or two separate Cases?**
  - Recommended: (a) one Case with two sub-cases.
  - Answer: agreed, (a).
- **How is the case-guppi fix checked?**
  - Recommended: (a) replace the Criterion of `estimate-case-build-answers-what-done-means`, read at the Retro of this session against the new Render.
  - Answer: agreed, (a).
- **How is the ask-guppi fix checked?**
  - Recommended: (a) a new narrow Estimate on `rule-ask`, read after the next /pre-spec on the new text.
  - Answer: agreed, (a).

## History

- 2026-10-13 created · raw/2026-10-13/1753/ledger.md#case-800
