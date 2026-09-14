---
type: decision
case: "119"
status: current
defer: [rule-brief]
origin: raw/2026-09-14/0747/ledger.md#case-119
sprint: migration
created: 2026-09-14
tags: [harness, workflow, librarian]
---

## Context

Today an Insight is "never a Decision target" (glossary, `insights/schema.md`); it reaches the Frontier only as the "Related Insight" of a deferred Case. `insight-session-vault-knowledge-not-loaded` (severity 3, four lessons after today, the heredoc trap among them) and `insight-ledger-hook-reads-only-the-final-text` (severity 3, four after today) have Proposals nobody was ever asked to ratify or reject; the same trap returns every session.

## Problem

Lessons pile up, the librarian writes the Insight, and nothing puts it in front of the person as a Case. The owner's design: the librarian surfaces an open Insight in the brief as a Case for the next Plan Mode, where it is ratified into a decision on its Proposal, or rejected, or deferred with a count — the same lifecycle a deferred Case has.

## History

- 2026-09-14 created · raw/2026-09-14/0747/ledger.md#case-119
