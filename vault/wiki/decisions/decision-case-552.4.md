---
type: decision
case: "552.4"
status: current
parent: "[[decision-case-552]]"
create: ["[[estimate-ledger-write-exits-2-on-an-error]]"]
update: ["[[rule-ledger-write]]"]
origin: raw/2026-09-30/1736/ledger.md#case-552.4
sprint: migration
created: 2026-09-30
tags: [session, hooks, harness, ledger]
---

## Recommend

- **Which hooks stop the agent when they crash**
  Recommended: (a) the ledger hook only; the same change for the other hooks is its own item in a later session.
  Answer: (a) the ledger hook only.
- **Change**
  Asked: the sub-case contradicted itself, because an error while the payload is read comes before the hook knows it is a re-fire, and exit 2 there could loop; an error while reading the payload exits 0 with the error on stderr, and an error after the payload is read exits 2.
  Taken: `when` names an error after the payload is read; `then` exits 2 for it, and a `－` line exits 0 with the error on stderr for an error while the payload is read; the new text of `rule-ledger-write` and the tests say the same.

## History

- 2026-09-30 created · raw/2026-09-30/1736/ledger.md#case-552.4
