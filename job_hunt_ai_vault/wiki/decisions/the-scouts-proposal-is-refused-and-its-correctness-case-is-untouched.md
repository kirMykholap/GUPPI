---
title: "The read-only scouts proposal is refused, and the correctness case it also carried is untouched"
type: decision
status: current
authority: scout-dispatch-design
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-21
created: 2026-08-21
supersedes: [[read-only-scouts-one-per-folder-ahead-of-the-librarian]]
sources: ["archive/2026-08-21/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work/handoffs/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work.md", "scripts/vault-catalogue.sh"]
tags: [agents, retrieval, vault]
---

# The ruling, 2026-08-21

> **owner: ретайрить как отклонённый.**

**Refused rather than built, and refused for the consumer it was designed for.** The proposal is in
`archive/` with `superseded_by:` pointing here
([[read-only-scouts-one-per-folder-ahead-of-the-librarian]],
[[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]).

# Why now, when it had stood for a day

**Its timing case had already failed its own measurement.** 20–30% of a librarian round trip is
read-only search; 4.13x on that removes three to five minutes of twenty-four, and the six scouts
that buy it cost 592k tokens against the 224k the whole ingest cost. Every one of those figures is
on the proposal's own page ([[agent-round-trip-cost]]).

**What this session added is that the consumer closed.** What the owner described a scout collecting
— page, `authority`, `title` — is exactly what `scripts/vault-catalogue.sh` prints in **1.66 s**, in
the caller's own context, with no dispatch at all ([[vault-scripts]],
[[the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch]]). **An agent for that phase
is strictly worse**: same output, minutes instead of seconds, and a token bill.

# What is not refused

**The correctness case stands and is untouched.** The scouts found a defect in work already reported
as verified, and a third of them refuted the shape of the proposed fix by citing a recorded lesson
([[a-hole-was-shipped-in-work-already-reported-as-verified]],
[[a-guard-remembered-per-file-is-forgotten-in-the-next-file]]). **That half never depended on the
timing holding**, and it can be had by dispatching a read-only agent for a single question at any
time — which is already permitted
([[parallel-librarians-break-the-one-writer-property]], [[dispatch-librarians-in-parallel-only-for-reading]]).

**So what is refused is one design for one consumer**, not the practice of asking a read-only agent
something.

# Where the retired page's content went

| what lived on it | where it is now |
|---|---|
| the six-folder wall-clock table, the 4.13x, the 592k tokens | already on [[agent-round-trip-cost]], copied there when the arithmetic was done |
| the correctness finding | [[a-hole-was-shipped-in-work-already-reported-as-verified]] |
| the timing refutation | [[agent-round-trip-cost]], and this page |
| the design itself | the retired page, which is read to answer *why did we not do this* |

**Nothing was moved that was not already elsewhere**, which is the check this project runs before a
proposal is retired rather than after.

# Re-affirmed on 2026-08-26, against re-evaluating it

*(the owner selected it, against a re-evaluation.)* **The refusal stands whole and the proposal is
not re-opened.**

**The arithmetic he took it on, updated to six dispatch points:** a dispatch costs **143,000–230,000
tokens**, so six scouts on one ingest is of the order of a million tokens
([[agent-round-trip-cost]]).

**What is refused is the re-reading**, not the design — the design is still what answers *why did we
not do this*.

*(Compiled from `raw/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md`.)*
