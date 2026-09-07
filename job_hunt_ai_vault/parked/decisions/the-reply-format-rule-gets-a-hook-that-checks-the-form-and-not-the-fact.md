---
title: "The reply-format rule gets a hook that checks the form, and the earlier objection does not reach it"
type: decision
status: current
authority: reply-form-instrument
binding: prohibition
basis: inference
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: action
target: build-the-reply-form-hook
sources: ["archive/2026-08-30/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md"]
tags: [harness, testing, process]
---

# Context

**Every rule in `wiki/rules/` owes a mechanical instrument or a page saying why it has none**
([[every-rule-in-wiki-rules-owes-a-mechanical-instrument]]). The reply-format rule
([[the-reply-is-a-report-answers-and-one-case]]) obliges a visible artefact — the frontier printed as
a numbered list at the top of every reply — so an instrument is available to it in a way it was not
available to the rule it supersedes, where the four parts of a question are a judgement about prose.

**The same session argued against a hook a few hours earlier.** A hook watching for an unratified
decision before letting the next case open was deferred as a proposal of its own, and the owner
accepted the ground: «Хук откладывается как отдельный proposal. Если я замечу, что ты пропускаешь
ратификацию - укажу и мы вернемся к этому proposal».

# The question

**Does the earlier objection to a hook in this area also forbid this one?**

# How it works after

**No — and the distinction is the class of thing being checked.** A `MessageDisplay` hook reads the
reply and verifies that it opens with the frontier line.

- **The refused hook had to judge a FACT the session itself writes** into the ledger. That is exactly
  the class that already produces false green smoke rows here
  ([[the-smoke-gate-hooks]]): the instrument reads the actor's own output and believes it.
- **This one checks FORM**, which is visible whole in the message and **cannot be faked without being
  performed**. To pass, the reply must actually carry the list.

**So the rule gets its instrument and the deferred hook stays deferred**, each on its own ground.

# Recommendation

**Build it**, and the session withdraws its earlier blanket recommendation against a hook in this
area — which was stated more widely than its own argument supported.

# Ratification

**The session understood it** from the two mechanisms side by side. The owner has ratified the rule
that requires an instrument and ratified the rule this one serves; he has not separately been asked
about the hook.

**Not built.**

*(Compiled from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
