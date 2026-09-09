---
title: "A case that grows becomes a proposal, announced at the moment it happens"
type: decision
status: archived
authority: proposal-opening-trigger
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: proposal
target: the-decision-lifecycle
sources: ["archive/2026-08-30/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md", ".claude/hooks/catch-the-feedback.ps1"]
tags: [process, vault, harness]
---

# Context

**A case worked in chat grew into a body of work holding a dozen decisions, and there was no way to
hand that object to the librarian.** The feedback channel has four kinds — `miss`, `measure`,
`decision`, `harness` — and **none of them carries a proposal**. The decisions would arrive as loose
lines with nothing saying they are one body of work.

# The question

**How does a conversation that has outgrown a single question become a page, and when?**

# How it works after

**The session records a decision the moment it notices**: *we open a proposal, its name is XXX.*

**owner:** «как только мы ловим такое событие - агент пишет descision вида "принято решение создания
proposal. Название для него - ХХХ". И все решения, которые мы обсуждаем в рамках этого proposal
помечать, что они относятся к "ХХХ" proposal».

**Every decision taken inside it carries the key in the feedback line's existing bracket**, as
`[proposal:<key>]`, so `/retro` and `/handoff` assemble the body of work by match.

**No new feedback kind and no new field.** The bracket already carries the page or topic a line is
about, and **the colon distinguishes a container from a page slug**.
`.claude/hooks/catch-the-feedback.ps1` validates only the **kind** and passes the bracket through as
free text, so the scheme needs no code change
([[a-measure-line-names-its-destination-in-brackets-after-the-kind]]).

**The first use is `decision-lifecycle`** ([[the-decision-lifecycle]]), opened on 2026-08-30 and
carrying twenty decisions.

# Recommendation

**Reuse the bracket**, against minting a fifth feedback kind. A kind is parsed and validated; a
container is free text about the same line, which is what the bracket already is.

# Ratification

**The owner said it**, on 2026-08-30, in his own words, quoted above; and separately for the form:
«Форма принимается, утверждаю».

# The rule was broken by its own author in the same conversation

**The session let this case grow into a proposal across three turns without opening one, and the owner
named the event before the session did.** The rule he had just written — a case that grows becomes a
proposal, **announced at the moment it happens** — was in force and was not applied by the party that
had just recorded it.

*(Compiled from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
