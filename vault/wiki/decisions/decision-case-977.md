---
type: decision
case: "977"
status: current
create: ["[[estimate-ledger-write-refuses-a-bare-link-to-no-page]]"]
update: ["[[rule-ledger-write]]"]
origin: raw/2026-11-01/0141/ledger.md#case-977
sprint: plugin
created: 2026-11-01
tags: [session, hooks, harness, ledger]
---

## Problem

A reading or a lesson line can carry a `[[name]]` outside a code span that names no page; the hook writes it, the librarian copies it into a page, and the broken link is found only by `guppi check` after it stands in the vault.

## Recommend

- **Where a bare link to no page is stopped**
  - Recommended: (a) the ledger hook refuses the line, with a new Estimate on `rule-ledger-write`.
  - Answer: agreed, (a).
- **What counts as a page for the hook**
  - Recommended: (a) a live or archived page, a hub file, or a slug that a `create` decision line of the session creates.
  - Answer: agreed, (a).
- **Whether a schema file counts as a page**
  - Recommended: (a) the answer of `guppi check`: a schema file is no page, for all three readers.
  - Answer: agreed, (a).

## History

- 2026-11-01 created · raw/2026-11-01/0141/ledger.md#case-977
