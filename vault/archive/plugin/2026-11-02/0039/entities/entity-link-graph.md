---
type: entity
kind: Leaf
purpose: The links between the vault pages and the harness files, each written once, and a command that prints the neighbours of a page or a file with their purpose lines
status: archived
parent: "[[entity-guppi]]"
estimates: ["[[estimate-link-graph-prints-the-neighbours]]"]
rules: ["[[rule-link-graph-at-session-start]]"]
code_ref: [.guppi/guppi/links.py, .guppi/tests/test_links.py]
origin: raw/2026-10-31/1831/ledger.md#case-967.1
sprint: plugin
created: 2026-10-31
tags: [harness, workflow]
core: true
---

## Purpose

A builder that searches only for words misses a text that is linked to the change in other words. The graph reads each link where it is written — a field of a page, a `[[slug]]`, a slug named in the body, a path field, and the name of an agent, a skill or a command in a rendered file — and `uv run --project .guppi guppi links <slug or path>` prints the neighbours of one page or file, out and in, each with its purpose line, so the reader opens only the neighbours that bear on its question. A missed link is fixed by writing the name once where it belongs (as set in case 967.1).

## History

- 2026-10-31 created · [[decision-case-967.1]]
- 2026-10-31 estimate estimate-link-graph-prints-the-neighbours added · [[decision-case-967.1]]
- 2026-10-31 status: draft → built · cascade
- 2026-10-31 rules: [rule-link-graph-at-session-start] · cascade
- 2026-11-02 deleted · [[decision-case-999.1]]
- 2026-11-02 archived · cleanup
