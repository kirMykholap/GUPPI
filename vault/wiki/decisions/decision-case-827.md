---
type: decision
case: "827"
status: current
children: ["[[decision-case-827.1]]", "[[decision-case-827.2]]", "[[decision-case-827.3]]", "[[decision-case-827.4]]"]
origin: raw/2026-10-15/1959/ledger.md#case-827
sprint: plugin
created: 2026-10-15
tags: [harness, workflow, ledger, session, hooks, librarian, render]
---

## Problem

A lesson that needs a new tag cannot have it where most lessons are written: from `/work` to the end of Retro no Case is ratified, so the ledger hook refuses the line, and the tag waits for a Case of a later session.

## Recommend

- **How may a new tag enter outside a Case**
  - Recommended: (a) a lesson line declares its new tag with its meaning and Russian aliases; the librarian's run registers it, and the one rule and the header of `tags.md` name this way.
  - Answer: agreed, (a).
- **Does the check of a Case file change too**
  - Recommended: (a) the check of a Case file stays; a Case still declares a new tag by a tag line.
  - Answer: agreed, (a).
- **How a lesson line writes its new tag**
  - Recommended: (a) one block `{newtag:<tag>|<meaning>|<aliases>}` per new tag, the tag also in `{tags:...}`, read by `parse_line`.
  - Answer: agreed, (a).
- **How the change is checked**
  - Recommended: (a) three sub-cases: the ledger hook with the Criterion of `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag` replaced, the lift with a new Estimate, and the texts with the Criterion of `estimate-ratification-ledger-line-form` replaced.
  - Answer: agreed, (a).
- **How the header of `tags.md` changes**
  - Recommended: (a) a one-off edit by hand in Work Mode, and an exception for that header alone in the pages that make the script the only writer.
  - Answer: agreed, (a).
- **Where the exception for the header of `tags.md` is written**
  - Recommended: (a) a fourth sub-case writes it into `rule-vault-layout`, `rule-page-generation`, `rule-documentation` and `entity-glossary`.
  - Answer: agreed, (a).
- **How the fourth sub-case is checked**
  - Recommended: (a) a new Estimate on `rule-vault-layout`, read by hand after the librarian's run.
  - Answer: (b) no new Estimate; `estimate-glossary-terms-defined` checks it.
- **Change**
  - Asked: a finding of `/pre-spec`: the hand edit of the header of `tags.md` runs in Work Mode, before the exceptions of Case 827.4 land; `context` should name the sentence of `rule-case-build` that allows it at that moment.
  - Taken: `context` names that sentence of `rule-case-build`; nothing else changed.

## History

- 2026-10-15 created · raw/2026-10-15/1959/ledger.md#case-827
