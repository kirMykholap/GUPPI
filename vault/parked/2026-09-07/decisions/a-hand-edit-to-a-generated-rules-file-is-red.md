---
title: "A hand edit to a generated `.claude/rules/` file is red, because the repair moves no address"
type: decision
status: current
authority: generated-file-hand-edit-verdict
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-19
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", "scripts/vault-inject.sh", "scripts/vault-check.sh"]
tags: [harness, vault, testing]
---

# The ruling, 2026-08-19

> **owner: a hand edit to a generated `.claude/rules/` file is RED, not advisory.**

**Rejected: advisory.** In this store advisory is the shape for a verdict whose **repair moves an
address** — that is why the filename half of the title rule prints instead of failing
([[the-filename-verdict-is-an-advisory-while-the-title-verdict-is-red]]). **This repair moves
nothing.** It regenerates the file, or it puts the text on the page, and no inbound link is
touched either way.

**And a region already treats a hand edit as red.** Rule 12 asks by running the injector and
comparing ([[a-check-asks-by-running-the-writer-it-checks]]). Two delivery modes disagreeing about
the same act would be an exception to remember rather than a rule.

## Which open question this closes

[[generating-a-claude-rules-file-whole-from-its-vault-page]] listed it: *"what the checker does with
a hand edit it finds — red, or advisory, is not decided"*. That page had been carrying the question
since 2026-08-18, and the ruling reaches the corpus only through this page — the behaviour was
already verifiable in `scripts/vault-inject.sh`, so what was missing was never the code.

**The third of that page's open questions closed by measurement rather than by ruling**: the
marker's cost. An HTML comment is stripped on the native path
([[what-reaches-a-subagent-a-scoped-rule-does-and-an-html-comment-does-not]]) and, since the guard's
comment-stripping fix of the same day, on the guard path as well — so the *generated, do not edit*
banner is free on both.

## What it obliges

- **The check regenerates and compares byte for byte**, and a difference exits the gate non-zero
  ([[the-rendered-form-is-defined-once-and-read-by-the-writer-and-the-comparison]]).
- **A write run is the repair**, and it restores the file in place — hand-probed on 2026-08-19
  before any suite case was written ([[hand-probe-a-new-mechanism-before-running-the-suite]]).
- **An unmarked file in that directory is still nobody's to touch.** Red applies to a file carrying
  the writer's own marker, which is the only fact the deleting branch may read
  ([[a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker]]).
