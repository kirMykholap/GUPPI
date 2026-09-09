---
title: "`/pre-task` reads too much, and the rework is a `vault-ask` topic rather than cleanup work"
type: decision
status: current
authority: pre-task-reading-scope
binding: deferral
basis: human
sprint: S3
decided: 2026-08-31
created: 2026-08-31
target_kind: none
target: none
sources: ["archive/2026-08-31/2026-08-31-the-families-become-rules/handoffs/2026-08-31-the-families-become-rules.md", ".claude/agents/pre-task.md", "scripts/vault-catalogue.sh"]
tags: [agents, retrieval, process]
---

# Context

**`/pre-task` phase 1 enumerates rather than searches.** It reads the frontmatter of every page the
catalogue prints and opens what the titles implicate — a deliberate design, because a ranked partial
answer to *what constrains this plan* is the dangerous one
([[the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch]]). The run this session made
named **148 pages on its shortlist and opened 33 in full**.

**The cleanup removed the folder that enumeration was mostly about.** 129 decisions moved to
`archive/` on 2026-08-31, and `bash scripts/vault-catalogue.sh` stopped printing `archive/` on
2026-08-30 — so the obliges-and-rejected half of every archived prohibition now sits one wikilink
deeper than any instruction sends a reader, and phase 1 cannot see it at all.

**Nothing in the corpus says what `/pre-task` reads once `decisions/` is emptied.**
[[the-prohibition-families-become-rule-pages-served-by-a-hook]] names the question as open and decides
nothing about it.

# The question

**Is the `/pre-task` rework part of the cleanup, or a subject of its own?**

# How it works after

**A subject of its own, and it belongs to `vault-ask`.** Nothing about `/pre-task` changes as part of
the cleanup, and the cleanup does not wait on it.

**The direction he gave, recorded as direction and not as a design.** Search should hand `/pre-task`
relevant pages instead of making it read the whole enumeration; **relevance is judged by whether an
`authority:` slug matches in meaning** — «Смысл совпал? - читаем» — and deepening happens only from
there.

**What is not decided by this page:** who does the meaning-matching, whether the enumeration survives
at all, what replaces the catalogue for the archived half, and whether phase 1 keeps its two-count
report. All of it is the topic's, not this page's.

# Recommendation

**Record the direction, defer the work, and name where it lands.** A direction he gave in passing is
lost if it is not written down, and written down as a design it becomes a plan nobody agreed to.

**Rejected: folding the rework into the cleanup**, which would have made the cleanup answerable for a
retrieval redesign it had no scope for.

# Ratification

**owner, 2026-08-31:** «мы вообще должны переработать pre-task. Сейчас он читает слишком много. Поиск
должен давать ему релевантные страницы, а не заставлять читать все и только там pre-task иожет
углубится. Что такое релвантная страница? - може судить по authority. Смысл совпал? - читаем. Но это
отдельный разбор vault-ask.»

# The consequence of leaving it

**`/pre-task` starts answering with claims rather than with what a decision obliges.** A family rule's
clause is a title; the reasoning and the rejected alternative are in `archive/`, which nothing sweeps
and phase 1 does not read. **That is a real loss of answer quality dated from the sweep**, and it is
carried here rather than discovered later ([[vault-scripts]]).

*(Compiled from `raw/handoffs/2026-08-31-the-families-become-rules.md`.)*
