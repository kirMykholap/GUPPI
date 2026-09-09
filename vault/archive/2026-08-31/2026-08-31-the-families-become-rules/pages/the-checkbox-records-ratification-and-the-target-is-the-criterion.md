---
title: "The checkbox records ratification and not completion, and the target is the archiver's criterion"
type: decision
status: archived
authority: proposal-checkbox-meaning
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: action
target: date-scope-the-decision-fields
sources: ["archive/2026-08-30/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md", "wiki/proposals/_schema.yaml"]
tags: [vault, record-schema, process]
---

# Context

**A proposal carries a `# Decisions` section** — one line per decision it must close before it can be
implemented, written as a checkbox, a link and a verdict
([[a-decision-declares-its-target-and-the-handshake-closes-it]]). The question the checkbox raised is
what it asserts.

**The owner's own first proposal was that ratification plus a tick be the archiver's criterion.**

# The question

**Does the tick mean the decision was answered, or that the work is finished — and is it what the
archiver reads?**

# How it works after

**The tick records RATIFICATION and never completion.** An unanswered item is prose carrying no link
at all; an answered one is ticked and carries a resolving link plus its verdict.

**The archiver's criterion is that the TARGET received the decision, never the checkbox.** The tick is
display.

**The gate needs no verdict for it**, and that is what makes the arrangement cheap: a ticked line with
a dead link, or an unticked line carrying one, is **already** caught by the link sweep of rules 4 and
5. Nothing new has to be built or maintained.

**This removed a gate verdict and a selftest case from the plan**, and removed a stored copy of a
derived fact that the librarian would otherwise have had to keep true.

# Recommendation

**Display, not criterion.** The session's ground was that the librarian writes both the tick and the
decision's forward pointer in one act, so a criterion reading the tick would be an instrument reading
its own author's output — the shape that already produces false green smoke rows here
([[the-smoke-gate-hooks]]).

# Ratification

**The owner selected it, against his own proposal**, twice. On the display half: «Ты не хочешь
принимать галочку как критерий - окей. Оставляем ее для вида». On the meaning: «Case 7: принимаю
рекомендацию, ратифицирую».

**He stopped a design that was about to be built, and it was his own** — one of three times that day.

*(Compiled from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
