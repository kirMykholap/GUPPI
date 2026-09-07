---
title: "The register file format is deferred to a discussion, and the no-new-dependencies rule is named rather than lifted"
type: decision
status: archived
authority: register-format-deferral
binding: deferral
basis: human
sprint: S2
decided: 2026-08-21
created: 2026-08-24
sources: ["archive/2026-08-21/2026-08-21-a-claim-is-looked-up-before-a-page-is-written/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md", "archive/2026-08-24/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause/handoffs/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause.md"]
tags: [vault, harness, process]
---

# The ruling, 2026-08-21

> **owner:** «Правило про лишние зависимости - окей. Но это то, что нам нужно. Нам нужен yaml или
> json или еще что-то для ведения тегов и authority. Запиши, обсудим на следующей сессии.»

**Nothing is built and nothing is lifted.** He names the standing rule against new dependencies,
says this is the case that may earn one, and sends the question to a discussion rather than
answering it.

**Rejected: deciding it that day, in either direction.** Building a parser change on an
undiscussed exception would have spent the rule; refusing outright would have answered a question
he asked to keep open.

# What it caused

**[[a-machine-readable-format-for-the-registers]]**, which carries the design and the measurement —
five hand-written YAML parsers in `scripts/`, and PyYAML present but transitive.

# Compiled late, and that is the point of the page

**This decision was taken on 2026-08-21 and had no page until 2026-08-24.** The proposal it caused
was written the same day it was taken; the ruling behind it was not, so `decided_by:` had nothing to
name for three days. **A proposal whose cause is uncompiled reads exactly like a proposal nobody
ruled on** ([[a-proposal-keeps-an-absent-decided-by-rather-than-a-false-idea-mark]]).

# What has happened since, and it does not close this

**[[pyyaml-is-declared-rather-than-added-and-the-dependency-rule-is-not-opened]]** settled the
dependency half on 2026-08-22: PyYAML is a declared `dev` dependency, and the rule was not opened.
**The format question is untouched** — the registers are still markdown and the scripts still parse
them by hand.
