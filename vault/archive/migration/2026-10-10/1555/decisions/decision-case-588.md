---
type: decision
case: "588"
status: archived
children: ["[[decision-case-588.1]]", "[[decision-case-588.2]]", "[[decision-case-588.3]]"]
origin: raw/2026-10-02/1202/ledger.md#case-588
sprint: migration
created: 2026-10-02
tags: [harness, render, schema, workflow, ledger]
---

## Problem

An `update` meant only for the History of an Estimate replaced its Criterion, because `materialize` reads `change` alone as a whole replacement. The case schema asks for such an update when a put-off question is closed. The promise of `estimate-estimates-schema-checked` was lost without a decision. The question was how to repair the page, and whether the scripts change so that it cannot happen again.

## Recommend

- **How is the page of `estimate-estimates-schema-checked` repaired?**
  - Recommended: (a) restore the old Criterion word for word. The person ratified that it stands, it already covers the new test, and it is the only promise of `rule-estimates-schema`.
  - Answer: (a).
- **Do the scripts change, so that an update meant only for History can no longer replace a promise?**
  - Recommended: (a) the scripts change: an update with `change` alone writes only the History line, on an Estimate too. The case schema's own instruction then means the same thing on every page, and the judgment stays one function that all three scripts use.
  - Answer: (a). The person first found it strange that the scripts replace the page when only a History line was asked for, and asked what had to be written into the History of that page and why, since the script writes History. The answer: the Case gives the text of the line in `change`, and that line was to close the question put off on the Estimate, as the case schema asks. The person then agreed.

## History

- 2026-10-02 created · raw/2026-10-02/1202/ledger.md#case-588
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
