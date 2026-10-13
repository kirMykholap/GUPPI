---
type: decision
case: "802"
status: current
create: ["[[estimate-morph-sets-up-the-project-at-the-first-hi]]"]
update: ["[[rule-morph]]", "[[rule-guppi-config]]", "[[entity-sprint-plugin]]"]
supersedes: ["[[decision-case-239]]", "[[decision-case-745]]", "[[decision-case-750]]", "[[decision-case-758]]"]
origin: raw/2026-10-13/1753/ledger.md#case-802
sprint: plugin
created: 2026-10-13
tags: [session, harness, plugin, render, sprint, workflow]
---

## Problem

GUPPI has no step that sets a new install up. A second person's project would run on the settings of this machine, and the plan for that step is still a placeholder that has been put off again and again.

## Recommend

- **What is the install step, and how do its answers become settings?**
  - Recommended: (a) a skill whose answers become the project's first Case; the person ratifies it, and the render writes the settings files.
  - Answer: agreed, (a).
- **When does the install step run?**
  - Recommended: (a) `/hi` starts it when the settings are missing.
  - Answer: agreed, (a).
- **What does the install step ask, and what does it find for itself?**
  - Recommended: (a) it finds the branch, the remote and the transcripts folder, asks the rest, and shows every value in the one Case.
  - Answer: agreed, (a).
- **Does choosing the category set stay part of the install step?**
  - Recommended: (a) move it out to its own backlog item; every project uses the development set.
  - Answer: agreed, (a).
- **How do pages grow in a project that already has code?**
  - Recommended: (a) each Case covers the code it touches: `case-guppi` reads code that no page covers, and offers in a round a page for the thing the Case changes alone.
  - Answer: agreed, (a).
- **One Case or two?**
  - Recommended: (a) two separate Cases: this one on the install step, page growth as its own Case on `rule-case-build`.
  - Answer: agreed, (a).
- **What does this session deliver for the install step?**
  - Recommended: (a) write the design now and the check the built skill must pass; build it in the milestone The plugin.
  - Answer: agreed, (a).
- **Where does the install step run in relation to the session that `/hi` opens?**
  - Recommended: (a) the install Case is the first Case of the first session, and the Work Mode of that session writes the settings.
  - Answer: agreed, (a).
- **Where does the category set wait as its own backlog item?**
  - Recommended: (a) a plain line in the `## Backlog` of `entity-sprint-plugin`.
  - Answer: agreed, (a).

## History

- 2026-10-13 created · raw/2026-10-13/1753/ledger.md#case-802
