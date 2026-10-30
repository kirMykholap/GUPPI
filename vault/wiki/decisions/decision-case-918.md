---
type: decision
case: "918"
status: current
children: ["[[decision-case-918.1]]", "[[decision-case-918.2]]", "[[decision-case-918.3]]", "[[decision-case-918.4]]"]
origin: raw/2026-10-29/2341/ledger.md#case-918
sprint: plugin
created: 2026-10-29
tags: [session, workflow, harness, plugin]
---

## Problem

Four checks that ship, or will ship once they pass, hold sentences true only in the repository of GUPPI: two name English as the language of the repository, one names the code page of GUPPI's machine, and one starts from a command and a rule that the clean version does not hold.

## Recommend

- **Which checks does this Case rewrite now?**
  - Recommended: (a) the four that cost little now — the two case-build checks, the UTF-8 check and the package check; the four put off stay put off.
  - Answer: agreed, (a).
- **How does the package check say that it holds only in GUPPI's repository?**
  - Recommended: (a) open the trigger and the method with "In the repository of GUPPI", and keep the method's wait.
  - Answer: agreed, (a).
- **How does the UTF-8 check name the character it prints?**
  - Recommended: (a) outside the code page of the locale, as the purpose and method say.
  - Answer: agreed, (a).
- **Change**
  - Asked: at `/pre-spec`, item C1 was put off with no Case, so the defer of `decision-case-893.1` stands and holds the four, and the note to C1 goes.
  - Taken: the `context` says so, and the summary carries no line `Other Case`.
- **Change**
  - Asked: at `/pre-spec`, name the five other Estimates that the last reading listed and leave them to the next session, with no change of status.
  - Taken: the `context` names the five and says that their rewrite is not part of this Case, and that a line of the handoff leaves them to the next session.

## History

- 2026-10-30 created · raw/2026-10-29/2341/ledger.md#case-918
