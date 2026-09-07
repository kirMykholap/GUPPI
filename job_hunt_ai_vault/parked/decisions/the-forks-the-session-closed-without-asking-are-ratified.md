---
title: "The forks the session closed without asking are ratified, and each one is named with where it landed"
type: decision
status: current
authority: session-closed-forks-ratification
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: none
target: none
sources: ["archive/2026-08-30/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md"]
tags: [process, agents, harness]
---

# Context

**A session that closes a fork without asking has made a decision the owner never saw.** The retro's
job is to find those and put them back to him, and this one found seven.

**They were closed during a day the owner had declared an emergency**, where asking about each would
have cost the day. That is the condition the carve-out exists for, not a licence.

# The question

**Do the forks the session closed on its own stand, or is any of them reopened?**

# How it works after

**All seven stand, and each has a home:**

| the fork | where it is written |
|---|---|
| `target:` written as an inline list of plain slugs | [[the-cleanup-suspends-the-rules-that-would-refuse-it]], which explains why a repeal cancelling four things cannot name one |
| `agent: Explore` for the forked search skill | [[the-vault-ask-skill]] — it loads no `CLAUDE.md`, which changes what the search sees |
| `background: false` for that skill | [[the-vault-ask-skill]] |
| the `ServedRuleFiles` field in the ledger | [[the-pre-task-ledger]] |
| the hook scanning `wiki/rules/` before it opens the ledger | [[the-rule-server-hook]], where the order is measured rather than chosen |
| the commit going on `main` with no branch | [[main-is-this-repositorys-branch-convention]], which already ruled it |
| the address the taxonomy is written to | [[concepts-are-non-functional-requirements-and-entities-are-functional]] |

**Two of the seven were already decided elsewhere** — the branch convention, and `target:` as a list —
so the ratification confirms them rather than creating them. **`agent: Explore` is the one with a
consequence nobody weighed**: that agent type loads neither `CLAUDE.md`, so the choice changes what the
search can see at all, and it survives only because the reading discipline is rendered into the skill
itself.

# Recommendation

**Put all seven back, in one list, with what each costs.** A fork closed silently is indistinguishable
from a fork nobody noticed, and the difference only shows up when the consequence arrives.

**Rejected: changing any of them.**

# Ratification

**owner selected, 2026-08-30: «ратифицирую»**, given against the session's own list of seven put to
him in prose. He chose from options the session composed, so the wording is the session's
([[the-retro-records-a-ruling-chosen-from-a-menu-and-ratifies-decisions-not-utterances]]).

*(Compiled from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
