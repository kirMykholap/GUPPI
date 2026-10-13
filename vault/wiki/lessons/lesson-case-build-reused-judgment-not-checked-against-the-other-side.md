---
type: lesson
kind: error
root_cause: case-guppi named an existing function as the judgment both sides share without reading the function the other side calls, so CLAUDE.md "One judgment, one implementation" was claimed and not checked
status: clustered
insight: "[[insight-case-build-claims-what-code-does-without-reading-it]]"
origin: raw/2026-10-12/2252/ledger.md#L16
sprint: plugin
created: 2026-10-12
tags: [session, workflow, harness]
---

## Trigger

Case 783 had /pre-spec reuse page_exists of guppi/materialize.py for a defer that guppi generate judges by its own find, and the ask-guppi run found that the two answer differently for an Estimate archived outside a folder estimates/, so the Case was built again around a new shared has_page

## Root cause

case-guppi named an existing function as the judgment both sides share without reading the function the other side calls, so CLAUDE.md "One judgment, one implementation" was claimed and not checked

## History

- 2026-10-12 created · raw/2026-10-12/2252/ledger.md#L16
- 2026-10-14 updated: clustered under insight-case-build-claims-what-code-does-without-reading-it (synthesis) · raw/2026-10-13/2118/ledger.md#L27
