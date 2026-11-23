---
type: estimate
kind: QA
status: passed
target: "[[entity-guppi-repository]]"
purpose: Whether LICENSE at the root of the repository holds the whole MIT license with the copyright line of kirMykholap
method: "by hand, in the Work Mode of the session that writes LICENSE: the file at the root of the branch of that session read against the text of the MIT license at https://opensource.org/license/mit and against the Criterion"
origin: raw/2026-11-20/1353/ledger.md#case-1043.2
sprint: plugin
created: 2026-11-20
tags: [github, git]
---

## Criterion

When:
A person reads `LICENSE` at the root of the branch of the session whose Work Mode wrote it.

Then:
`LICENSE` holds the text of the MIT license, whole and unchanged.
**＋** Its copyright line reads `Copyright (c) 2026 kirMykholap`.

## Result

2026-11-23, Work Mode of session 1353: LICENSE at the root of the branch plugin (commit f2c2a43e) read against the MIT text of the SPDX list and of https://opensource.org/license/mit: the whole text, unchanged but for ASCII quotes where the web page shows typographic ones, with the line Copyright (c) 2026 kirMykholap

## History

- 2026-11-23 created · [[decision-case-1043.2]]
- 2026-11-23 status: pending → passed · raw/2026-11-20/1353/ledger.md#L22
