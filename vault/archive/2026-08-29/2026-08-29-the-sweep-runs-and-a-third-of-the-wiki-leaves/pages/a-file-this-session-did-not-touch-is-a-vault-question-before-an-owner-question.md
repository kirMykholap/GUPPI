---
title: "A file this session did not touch is a vault question before it is an owner question"
type: lesson
status: archived
authority: outside-change-triage
basis: human
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", ".claude/skills/retro/SKILL.md"]
tags: [process, vault, agents]
---

# The trigger

**A change a session did not make gets read as *unexplained*. It should be read as *unasked-about*.**

Those two words route to different places. *Unexplained* routes to the owner and costs a round.
*Unasked-about* routes to a grep and costs one command.

# The incident that produced it

**A retro put a question to the owner that the corpus had already answered**, and he replied «мы уже
говорили об этом». The line was `pages.base` gaining a filter on its *Every page* view;
[[pages-base-is-not-a-review-item]] settles it, and it was found in one grep **after** the round was
spent ([[a-question-the-corpus-answers-was-put-to-the-owner-at-the-retro]]).

**What separates the lines that got triaged from this one is the useful half.** Three other frontier
lines were checked against the tree in the same pass and dropped or closed — **and every one of them
was about something the session had built itself.** This one arrived through `git status` as
somebody else's change.

**So the habit was live and the classifier was wrong**, not absent. The session knew to check its
own work against the corpus and did not recognise that somebody else's work is the same question.

# Why the corpus is the right first stop, not the owner

**A change from outside is exactly the class the corpus is most likely to hold.** It is somebody
else's decision, and a decision that was taken is a decision that was recorded — that is what this
store is for ([[the-vault-is-compiled-not-retrieved]]).

**A question a session can answer for itself costs a round to ask** — the third instance of that
shape on the record, and the first inside `/retro`
([[deriving-what-the-vault-already-holds-costs-a-round]],
[[an-objection-priced-against-a-cost-already-paid-dissolves-on-a-page-nobody-opened]]).

# The form to remember

**Before a change you did not make goes into a question for the owner, grep for the file's name and
for what it does.** If nothing comes back, ask — and the asking is then worth the round, because the
answer is going to be written down for the first time.
