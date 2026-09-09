---
title: "The hook was stricter than the text it enforced, and nothing noticed until a session met the gap"
type: lesson
status: archived
authority: hook-versus-text-scope
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md", ".claude/hooks/session-brief.ps1"]
tags: [harness, vault, agents]
---

# Two enforcement surfaces, two scopes

**The written rule says `wiki/`** — in the vault's `CLAUDE.md` and in the librarian's own
definition, the two places that state it. **The guard hook also fires on the registers**:
`index.md`, `tags.md`, `sprint.md`, `log.md`.

Nobody had noticed, because until 2026-08-17 nobody had edited a register by hand.

# What it did to the session that met it

The session read the one-writer rule **two ways in one day and acted on both**:

- **Literally**, to justify editing the vault's own `CLAUDE.md`: the rule names `wiki/`, and the
  schema file sits above `wiki/`. Under that reading the write was outside the rule.
- **Broadly**, over `index.md`, after the hook fired mid-edit and said otherwise.

**Neither edit was wrong at the retro** — both were the right call in the moment, and both are
recorded as divergences ([[hand-edits-of-the-wiki-are-a-recorded-divergence]]). What went unnoticed
is that the session was **holding two readings of one rule at once**, and it took the hook
contradicting one of them for that to become visible.

# The general shape

**When the enforcement is stricter than the text, the text is what people plan against and the
enforcement is what they discover.** The gap is invisible for exactly as long as nobody does the
thing that falls between them, so its age tells you nothing about its size — this one had stood
since the hook was written.

It is the mirror of this project's more familiar failure, prose that nothing enforces
([[no-rule-reads-a-harness-file]]). Both are the same defect: **a rule whose written form and whose
mechanical form were never compared.** Marked regions exist so that comparison is a check rather
than an accident ([[marked-regions-and-the-prose-outside-them]]).

**The resolution the owner chose:** the hook's scope is right and the text moves up to meet it —
[[the-one-writer-rule-covers-the-registers-too]].
