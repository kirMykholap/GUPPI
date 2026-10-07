---
type: decision
case: "698"
status: current
children: ["[[decision-case-698.1]]", "[[decision-case-698.2]]"]
origin: raw/2026-10-07/0211/ledger.md#case-698
sprint: migration
created: 2026-10-07
tags: [session, workflow, harness]
---

## Problem

`case-guppi` still makes the client ask the person for permission when it reads this project's saved transcripts, though two read rules of the allow list were meant to stop that.

## Recommend

- **Whose prompt the Case removes**
  - Recommended: (a) the builder only, and say whether the prompt came before or after the builder started.
  - Answer: (a); the prompt came after the builder started.
- **Which mode the builder runs in**
  - Recommended: (a) `auto`.
  - Answer: (a).
- **Whether the two read rules stay in the allow list**
  - Recommended: (a) keep both rules.
  - Answer: (b), remove both rules.
- **Which check says the change is done**
  - Recommended: (a) the promise sits in `estimate-permissions`; `estimate-case-build-writes-the-case` names the new mode and goes back to pending.
  - Answer: (a).
- **Change**
  - Asked: at pre-spec, a call that no permission rule allows is judged by the classifier, which refuses it when its server gives no verdict; the person chose to keep both read rules beside `auto`.
  - Taken: both read rules stay in the allow list; a read they match passes with no verdict, and a call they do not match is judged by `auto` with no prompt; the update of `rule-morph` changes no text and keeps only a `change` line, and the Case is built again under its own number.

## History

- 2026-10-07 created · raw/2026-10-07/0211/ledger.md#case-698
