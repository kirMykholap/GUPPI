---
type: estimate
kind: QA
status: passed
target: "[[entity-guppi-repository]]"
purpose: Whether the repository of GUPPI has its remote origin on GitHub
method: "by hand: git remote -v in the repository, its output written into the estimate line"
origin: raw/2026-10-17/1805/ledger.md#case-880.7
sprint: plugin
created: 2026-10-17
tags: [git, github]
---

## Criterion

When:
Someone runs `git remote -v` in the repository of GUPPI.

Then:
It prints `origin` with the URL of the repository `GUPPI` on GitHub, once for fetch and once for push.

## Result

2026-10-17, Retro of session 1805: git remote -v prints origin https://github.com/kirMykholap/GUPPI.git (fetch) and origin https://github.com/kirMykholap/GUPPI.git (push)

## History

- 2026-10-17 created · [[decision-case-880.7]]
- 2026-10-17 status: pending → passed · raw/2026-10-17/1805/ledger.md#L64
