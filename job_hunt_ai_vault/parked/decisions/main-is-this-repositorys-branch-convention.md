---
title: "Commits go straight to `main` in this repository, against the harness default"
type: decision
status: current
authority: branching-convention
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md"]
tags: [process, harness]
---

# Recorded 2026-08-17, as a divergence and then as the convention

Four commits of 2026-08-17 went straight to `main`, against the harness's standing default of
branching before committing. **owner:** `main` is this repository's convention.

**Rejected: a branch and a merge per slice.** This is a single-owner local tool with no PR flow and
no second reviewer waiting on a diff; a branch would exist only to be merged by the person who made
it, and the review that actually happens here is the owner reading `git diff` before the commit
([[the-librarian-writes-unattended]]).

## Why it is written down at all

It is recorded **once**, so that no later session either branches silently — leaving the owner with
a topology he did not ask for — or spends a turn asking a question that has an answer. A convention
that lives only in what previous sessions happened to do is exactly the kind of unwritten rule this
store exists to remove ([[no-rule-reads-a-harness-file]]).

**The harness still says branch first**, and that text has not been changed. Until it is, a session
following it is not wrong, only slower — and the divergence stands recorded here rather than
argued away.

## Reported again rather than followed silently — 2026-08-20

**Every commit in this repository is on `main`, and the owner asked for the commit.** The standing
instruction to branch first on a default branch was set against that, and it is **reported rather
than followed silently** — which is the shape this page asks for: the convention wins, and the
divergence from the generic instruction is named each time it is taken.

**What makes reporting the right move rather than a formality**: the generic instruction is not
wrong anywhere else, so silently overriding it teaches nothing, while naming it leaves an artefact
that the override was deliberate ([[a-wrong-record-is-acceptable-and-an-invisible-one-is-not]]).

## Ruled standing practice a third time — 2026-08-24, and this time the session did not report it

> **owner: сейчас мы работает в одной ветке main. Пусть остается это решение**

**The convention is re-affirmed and the count is now 121 commits with no branch ever taken.**

**What changed is the session's conduct rather than the ruling.** The section above records the
shape this page asks for — *the convention wins, and the divergence from the generic instruction is
named each time it is taken*. **This session took it and did not name it**, and the fact reached the
record only because the retro asked ([[ask-before-weakening-or-working-around-a-rule]]).

**A ground this page did not carry before**: `/handoff` takes its `commits:` range from linear
history, and `/ingest` compares that range against `git status --short`. A branch per session
fragments both, so the closing ritual's own instrument is an argument for the convention rather
than a bystander to it ([[ingest-is-units-and-verdicts]]).

**Rejected again: branch-plus-merge**, on a second ground beside the one above — it adds a step to a
closing ritual already in three parts ([[a-session-ends-with-retro-then-handoff-then-ingest]]).
