---
type: estimate
kind: QA
status: passed
target: "[[rule-rules-schema]]"
purpose: Whether no Leaf page of vault/wiki/rules/ carries How it works, each fact it held standing as the code bears it out in the docstring of its code or, for rule-internal-context, in its Purpose, a fact the code does not bear out standing corrected
method: "by hand at Retro of the session that changes it: a Grep for ^## How it works over vault/wiki/rules/ and the kind of each page it prints, no Leaf among them; the docstrings of .guppi/guppi/guard.py and .guppi/guppi/ratified.py read against the How it works sections that git show 9d19aafe prints as removed, recorded in the estimate line"
checked: 2026-10-31
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, schema]
core: true
---

## Criterion

When:
After Work Mode writes the docstrings of `.guppi/guppi/guard.py` and `.guppi/guppi/ratified.py`, an agent reads each Leaf page of `vault/wiki/rules/` and the docstring of the code that its `implementation_ref` names.

Then:
No Leaf page of `vault/wiki/rules/` carries a section `## How it works`.
**＋** Each fact that such a section held stands, as the code bears it out, in the docstring of the code that the page's `implementation_ref` names, and for `rule-internal-context` in its `## Purpose`; a fact that the code does not bear out stands there corrected.
**＋** The docstring of `.guppi/guppi/guard.py` says that Claude Code runs the hook on a call of a subagent too, and that the hook refuses such a call the same way.
**＋** The docstring of `.guppi/guppi/ratified.py` says that a parent whose own decision line a mark retires is named by that mark or lies under a Case it names, and leaves by that mark with its sub-cases.
**－** A remark on what stood before some Case does not move into the docstrings or the Purpose.
**－** A MOC page of `vault/wiki/rules/` keeps its `## How it works`.

## Result

2026-10-31, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
