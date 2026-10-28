---
type: insight
pattern: ask-guppi, at /pre-spec, reads the text of a Decision page under vault/wiki/decisions/ for a reason its frame does not name, before any finding names the page that points to it, and nothing but the agent's own judgment stops that read, since the hook leaves a Grep or Read whose path lies under vault/wiki/decisions/ unchanged
status: open
children: ["[[lesson-ask-guppi-read-a-decision-page-without-a-reason]]", "[[lesson-prespec-ask-guppi-opened-a-decision-outside-its-frame]]"]
severity: 2
origin: raw/2026-10-28/1907/ledger.md#L22
sprint: plugin
created: 2026-10-28
tags: [workflow, prespec, harness]
---

## Pattern

Two lessons, one cause. At the /pre-spec of session 1426 ask-guppi ran a Grep of decision-case-616.md for its Problem because entity-guppi carries deferred_by, though no finding named entity-guppi. At the /pre-spec of session 1907 ask-guppi ran a Grep for ^## over decision-case-882.3.md, a Decision no finding named. Both times the agent reported the break itself. A Grep or Read whose path is a file under vault/wiki/decisions/ is left unchanged by the hook of case 664.1, so only the agent's judgment holds the rule that a Decision page is read for a reason its frame names.

## Proposal

A Case could have the hook of case 664.1, for ask-guppi alone, refuse a Read or Grep whose path lies under vault/wiki/decisions/ unless the path is that of a Decision a finding names, or have the frame of ask-guppi name the one reason it reads a Decision page and that a deferred_by on a page it only looked at is no such reason. A suggestion, not a decision.

## History

- 2026-10-28 created · raw/2026-10-28/1907/ledger.md#L22
