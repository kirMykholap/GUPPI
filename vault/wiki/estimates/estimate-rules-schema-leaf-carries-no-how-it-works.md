---
type: estimate
kind: QA
status: pending
target: "[[rule-rules-schema]]"
purpose: Whether no Leaf page of vault/wiki/rules/ carries How it works, each fact it held standing in the docstring of its code or, for rule-internal-context, in its Purpose
method: "by hand at Retro of the session that changes it: each new docstring and the new Purpose of rule-internal-context read against the How it works it takes, recorded in the estimate line; by hand, after the librarian's run of that session: a Grep for ^## How it works over vault/wiki/rules/ and the kind of each page it prints, no Leaf among them"
origin: raw/2026-10-30/2005/ledger.md#case-942.1
sprint: plugin
created: 2026-10-30
tags: [harness, schema]
---

## Criterion

When:
After Work Mode writes the new docstrings and the librarian's run applies the updates of the session, an agent reads a Leaf page of `vault/wiki/rules/` and the docstring of its code.

Then:
No Leaf page of `vault/wiki/rules/` carries a section `## How it works`.
**＋** Each fact that such a section held stands in the docstring of the code that the page's `implementation_ref` names, and for `rule-internal-context` in its `## Purpose`, as the failure that a line of its list prevents.
**－** A remark on what stood before some Case does not move into the docstrings or the Purpose.
**－** A MOC page of `vault/wiki/rules/` keeps its `## How it works`.

## History

- 2026-10-30 created · [[decision-case-942.1]]
