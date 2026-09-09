---
title: "A refused proposal takes every decision in its list, prohibitions included"
type: decision
status: archived
authority: refused-proposal-decision-release
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: action
target: a-refused-proposal-releases-the-decisions-in-its-list
sources: ["archive/2026-08-30/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md", "scripts/vault-archive.sh"]
tags: [vault, harness, process]
---

# Context

**A proposal now carries a `# Decisions` section**: one line per decision it must close before it can
be implemented ([[a-decision-declares-its-target-and-the-handshake-closes-it]]). A refused proposal
moves to `archive/` with `status: refused`. The question the section opened is what happens to the
decisions still on its list when it goes.

# The question

**Does a refused proposal take its unanswered decisions with it, or do they stay live — and does a
prohibition among them stay live either way?**

# How it works after

**It takes all of them, unclosed, and prohibitions are not exempt.** `scripts/vault-archive.sh` gains
a second release route: a proposal carrying `status: refused` releases every decision named in its
`# Decisions` section, without any mark of discharge, because nothing received them.

**That is what keeps `processed` and `archived` distinguishable in a single archiving pass** — a
decision released by this route leaves carrying no evidence that a target took it, and a discharged
one is named back by its target ([[processed-is-repealed-and-the-mark-it-carried-is-derived]]).

# Recommendation

**The session recommended the opposite** — that the archiver refuse to release a refused proposal
while its list held live decisions, on the ground that a prohibition is a constraint that outlives the
work it was raised in — **and was overruled.**

# Ratification

**The owner said it**, in his own words, and gave his ground: «Представь что мы обсужадем proposal и
понимаем, что он нам не нужен где-то на третьем descision из 10. Зачем отвечать на остальные 7? Это и
есть моя претензия, что мы ходим по кругу... Если мы отменили proposal - значит все его решения не
имеют ценности».

**And he distinguished the case the session was worried about:** «proposal отменяется - все его
решения уходят вместе с ним. Иначе мы будем ловить их потом частями и не понимать к чему они
относятся». A decision **inside** a proposal is part of that work; a decision **pointing at a rule**
lives by its own rules and is not an open item in the list.

**Not built.** The archiver has the refusal for a `target_kind: repeal` decision and the release route
for a `repealed` page; this route is not written.

# A live page enumerates two exits from `wiki/decisions/` and this is a third

> [!NOTE] RAISED, NOT RESOLVED — the `authority:` slugs differ, so rule 3 of the gate cannot see this
> disagreement and no `CONTRADICTION` block is legal for it.

**[[a-decisions-archival-condition-is-read-off-its-binding]]** (`decision-archival-condition`,
2026-08-28) rules that a `prohibition` leaves *"not while it stands"*, and its *What it does not say*
section names **exactly two** exits. This ruling opens a third: released unclosed, with a refused
proposal, prohibitions included.

**Both live, both `basis: human`, neither outranks the other.** Found by [[the-decisions-agent]] on
this ingest's dispatch. **The librarian marks both and chooses neither.**

*(Raised 2026-08-30.)*

*(Compiled from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*

# The counterparty was suspended later the same day, and this page was not — 2026-08-30

> [!NOTE] STILL RAISED, STILL NOT RESOLVED.

**[[a-decisions-archival-condition-is-read-off-its-binding]] is suspended for the cleanup** by
[[the-cleanup-suspends-the-rules-that-would-refuse-it]], which lifted it with three others on one
ratification. **This page is not suspended and nothing about it changed.**

**So during the cleanup this is the only live rule on the question.** A reader who checks this page and
not the other will not see that the field narrowed underneath it — the *"not while it stands"* clause
this page disagrees with is not in force for that operation.

**That is a change to the ground, not a resolution.** The disagreement is dormant while one side does
not apply, and it returns the moment the suspension ends — which has no stated date, because the
repeal names none. **Both pages keep the mark.**

**This page's own state is unchanged**: `target_kind: action`, its target
`a-refused-proposal-releases-the-decisions-in-its-list` is not built, and
`scripts/vault-archive.sh` gained no second release route.
