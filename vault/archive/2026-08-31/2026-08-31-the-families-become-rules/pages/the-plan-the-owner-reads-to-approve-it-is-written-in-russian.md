---
title: "The plan the owner reads in order to approve it is written in Russian, and `plans` leaves the English list"
type: decision
status: archived
authority: approval-plan-language
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-22
created: 2026-08-22
sources: ["CLAUDE.md", "[[english-in-the-repository-russian-with-the-owner]]", "[[english-is-the-rule-and-the-russian-past-is-deferred]]"]
tags: [process, harness]
---

# Ruled by the owner on 2026-08-22

**The plan he reads in order to approve it is Russian.** Not the code it produces, not the specs,
not the briefs handed to subagents — the artefact whose only reader is him, at the one moment he is
asked to say yes or no.

**What changed in the rule's text**, and it is one change in two places
([[english-in-the-repository-russian-with-the-owner]]):

- the word **`plans`** is struck from the English list;
- **one clause joins the Russian half**, naming the plan he reads in order to approve it.

# Why it is a repair of the rule rather than an exception to it

**The rule's opening clause is *everything written into the repository*, and that plan is not in the
repository.** It is written to `C:\Users\kir\.claude\plans\`, outside the tree, tracked by nothing
here. **So the general clause never reached it. Only the bare word `plans` in the list did** — the
list was wider than the sentence heading it, and a list wider than its own predicate is a rule
disagreeing with itself.

**Every plan that *is* in the repository stays English, and no new item was needed to keep it
there.** The same list already names them under other words:

| where the plan lives | which item of the list covers it |
|---|---|
| `docs/` | *documents under `docs/`* |
| `.superpowers/sdd/plan-a/` | *any brief or report handed to a subagent* — which is what such a plan is |
| `C:\Users\kir\.claude\plans\` | none, and none ever did: it is outside the repository |

**So striking the word makes the rule internally consistent and adds nothing to remember.** That is
the whole argument for this shape: the rule got shorter and now covers exactly what its first clause
always said it covered.

# Rejected: splitting by audience and by location

**The alternative was two properties instead of one struck word** — the plan presented for approval
is Russian, the plan committed to the repository is English. It is more precise, and it is precise
about a distinction nobody has to make once the word is gone.

**It was rejected on cost of memory rather than on correctness.** A writer would have to hold *who
reads this* and *where does it live* at the moment of the first keystroke, which is exactly when a
language rule is applied and exactly when nobody has time to classify
([[english-in-the-repository-russian-with-the-owner]] gives that as the reason the rule cannot wait
for a question). The struck word costs nobody a decision.

# What it obliges

- **A plan presented to the owner for approval is written in Russian**, including its headings, its
  item titles and its acceptance criteria.
- **English technical terms keep their own alphabet inside it** — *vault*, *proposal*, *pre-task* —
  which is not an exception to this page but the standing rule of the same slice
  ([[english-terms-are-not-transliterated-into-cyrillic]]).
- **Identifiers, paths, commands and quoted code stay as they are.** They are the repository's own
  vocabulary and this decision does not touch them.
- **Nothing is retranslated.** Plans already written are records; this binds the next one
  ([[english-is-the-rule-and-the-russian-past-is-deferred]] for the standing shape of a
  forward-only language ruling).

# What this decision does not decide

**Whether a plan that is later committed is translated.** It is covered by the list as it stands —
`docs/` and a subagent brief are both named — so the question does not arise today; the day a plan is
committed from `C:\Users\kir\.claude\plans\` verbatim, it does.

**Whether the same reasoning reaches anything else outside the repository.** It reaches nothing else
today, because the rule's own predicate stops at the repository boundary and that boundary was never
argued here; a second artefact outside it would be its own dated decision, on the shape this store
already uses for a bucket leaving a backlog
([[english-is-the-rule-and-the-russian-past-is-deferred]]).
