---
type: decision
case: "589.2"
status: archived
parent: "[[decision-case-589]]"
update: ["[[rule-case-check]]", "[[estimate-case-check-refuses-a-letter-outside-the-script]]"]
origin: raw/2026-10-02/1202/ledger.md#case-589.2
sprint: migration
created: 2026-10-02
tags: [hooks, harness, workflow, session]
---

## Recommend

- **Change**
  - Asked: a pre-spec finding showed that `vault/wiki/rules/schema.yaml` asks a Leaf to lose its `## How it works` at its next touch, and this sub-case added a sentence to that section of `rule-case-check`. The person agreed that the section leaves at this touch, and that what still holds of it moves into the docstring of `guppi/casecheck.py`.
  - Taken: the `replace` pair on the section is dropped, the docstring of `guppi/casecheck.py` takes the facts of the section, and the update of `rule-case-check` carries only its History line.
- **How does the `## How it works` section leave `rule-case-check`, when no script can remove a section?**
  - Recommended: (a) remove it by hand, as a one-off task of Work Mode. This Case takes the removal, and Case 590 makes no change of its own in that section and names this Case. It is how the section left three rule pages before, it keeps both Cases small, and the content only moves.
  - Answer: (a).

## History

- 2026-10-02 created · raw/2026-10-02/1202/ledger.md#case-589.2
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
