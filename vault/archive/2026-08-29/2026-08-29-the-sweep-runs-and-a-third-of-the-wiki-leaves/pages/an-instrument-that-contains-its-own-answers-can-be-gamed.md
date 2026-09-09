---
title: "An instrument that contains its own answers can be gamed by its subject — the same failure shape, one level up"
type: lesson
status: archived
authority: instrument-gaming
basis: inference
sprint: S0
created: 2026-08-14
sources: ["archive/2026-08-14/2026-08-14-acceptance-and-the-shortened-claude-md/handoffs/2026-08-14-acceptance-and-the-shortened-claude-md.md", "docs/superpowers/plans/2026-08-13-acceptance-questions.md"]
tags: [testing, vault, agents]
---

# The check that grades the vault is inside the vault's search path

The acceptance file states each question **and the answer it should produce**, written in advance —
which is exactly what makes it a fair test and exactly what makes it forgeable. It lives in the
repository the agent is told to search. An agent that greps for a distinctive phrase in the
question can land in the answer key and produce a **flawless run having read nothing of the
corpus**.

Nothing about this is exotic. It is [[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]
one level up: not a check that examines nothing, but a check whose *subject can satisfy it without
being examined*.

## What was done, and why it is weaker than it looks

On 2026-08-14 each of the five dispatches carried an **explicit prohibition** against reading the
acceptance file, and each agent reported compliance. That is an instruction plus self-report — the
two things this project has already decided not to trust on their own
([[the-librarian-writes-unattended]], where testimony was replaced by `git diff`). It held. It
would hold less well on a run that was not being watched by the person who wrote the prohibition.

**The mechanical fixes exist and none is free**: keep the answer key outside the repository the
agent searches; or write the questions so that no phrase in them appears in the key; or check the
agent's cited sources against the key's path afterwards, which is the only one that produces
evidence rather than a promise. The third is cheap — an answer already lists the pages it used
([[one-librarian-behind-every-caller]]) — and is the one to reach for if this run is ever repeated
unattended.

## The general form worth carrying

**When you write down what a good answer looks like, you have created a shortcut to it.** Ask where
that document lives relative to the thing being tested. This applies to acceptance questions, to
expected-output fixtures, and to any plan that quotes the assertion a test should make.
