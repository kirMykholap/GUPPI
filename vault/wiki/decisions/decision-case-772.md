---
type: decision
case: "772"
status: current
children: ["[[decision-case-772.1]]", "[[decision-case-772.2]]", "[[decision-case-772.3]]", "[[decision-case-772.4]]", "[[decision-case-772.5]]"]
origin: raw/2026-10-10/1913/ledger.md#case-772
sprint: plugin
created: 2026-10-10
tags: [harness, workflow, librarian, session, render, ledger]
---

## Problem

Checks that cannot be read before a later moment of the sprint stand under `Work` and on the Frontier in every session, and turn into decision items though nothing is wrong with them. The rule that a check is read in its own session, Retro and pre-spec hold no exception for the checks of a sprint page.

## Recommend

- **When do the sprint page's own checks come back to be read?**
  - Recommended: (a) no new trigger: the Retro of the session that finishes the work, or the closing Case of `/sprint-close`.
  - Answer: agreed, (a).
- **Do Ask lines that wait for a sprint close leave the Frontier too?**
  - Recommended: (a) yes, the same rule: such a line is left out until the brief written at a sprint close.
  - Answer: agreed, (a).
- **What does Retro do with a sprint-page check it cannot read?**
  - Recommended: (a) it stays pending, and the handoff names it as a check that waits for its work.
  - Answer: agreed, (a).
- **Which checks may name a later session of the sprint?**
  - Recommended: (a) only checks whose target is a sprint page.
  - Answer: agreed, (a).
- **How does pre-spec judge the new wording?**
  - Recommended: (a) the predicate catches a session of a sprint and the session that closes one, and pre-spec spares a check of a sprint page.
  - Answer: agreed, (a).
- **What happens to W1, whose reading needs an old transcript?**
  - Recommended: (a) leave it out of this Case; a later Case fixes its method before the close of `plugin`.
  - Answer: agreed, (a).
- **Do the red lines of `make lint` stay for these checks?**
  - Recommended: (a) they stay.
  - Answer: agreed, (a).
- **Change**
  - Asked: pre-spec found that the open `read` box of a waiting sprint check would be debt at Retro and a `Work` line of the brief; the person agreed to the recommended fix.
  - Taken: Retro leaves that box waiting, neither debt nor the librarian's, and the brief takes no `Work` line from it.
- **Change**
  - Asked: pre-spec asked how a sprint check whose method names the person's answer is read; the person chose that the Retro of the session that finished its work names it under `## Ask the person` of the handoff, and the brief carries it into `Ask the person`.
  - Taken: the brief keeps a sprint check out of `Ask the person` only while its work is not done, and Retro names it there once its work is done.
- **Change**
  - Asked: pre-spec found that the judgment that a slug is a sprint page stands in more than one module; the person agreed to put it in one module that the others import.
  - Taken: `guppi/ledger.py` holds the constant and one predicate, and `guppi/materialize.py`, `guppi/prespec.py`, `guppi/sprint.py` and `guppi/sprint_close.py` import them.
- **Change**
  - Asked: pre-spec found that the test tasks did not require the names that the methods of the two pre-spec Estimates select; the person agreed to name them.
  - Taken: the new tests carry `waits` or `kept_method` in their names.

## History

- 2026-10-10 created · raw/2026-10-10/1913/ledger.md#case-772
