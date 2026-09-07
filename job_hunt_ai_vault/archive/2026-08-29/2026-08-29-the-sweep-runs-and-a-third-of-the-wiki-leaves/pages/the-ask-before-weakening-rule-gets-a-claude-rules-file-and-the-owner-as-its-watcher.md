---
title: "The ask-before-weakening rule gets a `.claude/rules/` file, and the owner is its watcher"
type: decision
status: archived
authority: ask-before-weakening-instrument
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-25
created: 2026-08-25
sources: ["archive/2026-08-25/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs/handoffs/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs.md", "job_hunt_ai_vault/wiki/rules/ask-before-weakening-or-working-around-a-rule.md"]
tags: [harness, process, vault]
---

# The ruling, 2026-08-25

> **owner:** «да, это важно правило. Закрывать его нельзя, значит оно должно плучимть свой дом.»

**The rule that guards every other rule does not close by a page saying no instrument is possible.**
It gets a mechanism instead ([[ask-before-weakening-or-working-around-a-rule]]).

And the mechanism was his:

> **owner:** «нам не нужен хук. У нас есть конструкция claude/rules, где описываются правила. А
> значит мы можем просто описать новый claude/rules/X который будем смотреть только на страницы
> wiki/rules и давать инструкции.»

> **owner:** «Тогда делаем .claude/rules/. Наблюдать буду пока что я сам.»

**The delivery half is a `.claude/rules/` file scoped to the rule pages**, generated whole from a
rule page carrying `render: whole` and `paths:`, on the model that already exists
([[a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker]],
[[an-ast-boundary-test-is-fixed-at-its-cause-not-in-the-test]],
[[paths-lives-on-the-vault-page-and-is-written-widest]]).

**The observing half is the owner, for now.** He watches whether a rule is weakened, and the
mechanical check that would notice it is deferred rather than refused
([[the-slice-against-supersession-check-for-a-weakened-rule]]).

# Rejected: a hook

**He refused it, on the ground that he could not see what it would do.** The mechanism was proposed
because a page records the obstacle as *no event exists at which a session's end can be noticed*,
and that framing was inherited without being tested
([[the-session-end-rule-is-instrumented-by-asking-the-tree]]).

# Why the closure matters more here than elsewhere

**This is the rule the other rules rest on.** Acceptance criterion 1 of S3 asks that every rule in
`wiki/rules/` owe a mechanical instrument or a page saying why it cannot have one
([[every-rule-in-wiki-rules-owes-a-mechanical-instrument]]), and this one had its obstacle recorded
in a single table row with nothing weighing what closing it would cost.

# Not done

**No `.claude/rules/` file was written, no rule page carries `render: whole` for this, and the
observing half is a human.** Whether the owner's own watch counts as the instrument the criterion
asks for is his reading, and nothing here reads it.
