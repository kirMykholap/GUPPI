---
type: decision
case: "69"
status: archived
defer: ["[[rule-materialize]]"]
superseded_by: ["[[decision-case-76]]"]
origin: raw/2026-09-12/ledger.md#case-69
sprint: migration
created: 2026-09-12
tags: [harness, workflow, ledger]
---

## Context

In Work Mode the agent ran `uv run guppi materialize --date 2026-09-12` to see how the
day's ledger lines would parse. The command has one mode: it wrote
`raw/2026-09-12/materialize.yaml`, the librarian's artifact, which the agent deleted at
once. Nothing was committed.

## Problem

The only way to see what the ledger and the Spec will become is to write the yaml. A
`--check` or `--show` mode — the entries, the unparsed lines and the incomplete marks on
stdout, nothing written — would let the agent and pre-task look before the librarian
runs. An `update` of `rule-materialize` with its Estimate; the next Plan Mode (the owner,
2026-09-12).

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-69
- 2026-09-12 superseded by decision-case-76 · [[decision-case-76]]
- 2026-09-13 archived · superseded
- 2026-09-13 archived · cleanup
