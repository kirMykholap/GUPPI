---
type: decision
case: "926"
status: current
update: ["[[rule-case-build]]", "[[estimate-case-build-reads-the-code-it-states]]", "[[insight-case-build-claims-what-code-does-without-reading-it]]"]
origin: raw/2026-10-30/0304/ledger.md#case-926
sprint: plugin
created: 2026-10-30
tags: [session, workflow, harness, case-build, ci]
---

## Problem

`case-guppi` read the function that decided a claim but not what the input of that function holds, and it took the name and the docstring of the function for its behaviour, so a Case was ratified on a false claim about a check.

## Recommend

- **What the Case changes in the sentence on a claim about code**
  - Recommended: (a) sharpen the sentence: a name or a docstring is no reading; read each function called on the way, and where the function walks over an input, the place where its caller takes that input; name each in `context`.
  - Answer: agreed, (a).
- **The second half of the lesson: the search for an existing judgment**
  - Recommended: (a) leave the sentence of case 752 as it stands; `context` says why.
  - Answer: agreed, (a).
- **How the change is checked**
  - Recommended: (a) replace the Criterion of `estimate-case-build-reads-the-code-it-states`.
  - Answer: agreed, (a).
- **Change**
  - Asked: the person agreed to the `/pre-spec` finding that the `method` of `estimate-case-build-reads-the-code-it-states` does not tie its event to the new Render, so the `/pre-spec` of this session, which runs before the render, would meet it.
  - Taken: the `method` waits for a `/pre-spec` of a session whose `case-guppi` runs on `.claude/agents/case-guppi.md` as rendered by case 926.

## History

- 2026-10-30 created · raw/2026-10-30/0304/ledger.md#case-926
