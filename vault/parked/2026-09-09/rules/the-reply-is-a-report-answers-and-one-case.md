---
title: "A reply is a report, then answers, then one case worked by the decision schema"
type: rule
status: current
governs: CLAUDE.md
render: region
basis: human
sprint: S3
created: 2026-08-30
sources: ["archive/2026-08-30/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md", "CLAUDE.md"]
decided_by: [[the-reply-format-becomes-a-rule-and-the-context-rule-is-absorbed-whole]]
supersedes: [[every-question-to-the-owner-carries-its-context]]
tags: [process, harness, agents]
---

# What travels

<!-- text -->
**Every reply opens with the frontier**, printed as a numbered list with a one-line description and a
status per item — discussed, ratified, deferred, open. It is not a summary and it is not optional:
the form held on 2026-08-30 because it was re-stated at the top of every message, and nothing else
carries it forward.

**Then the reply is three things, in this order:** what the session did since the last message; the
answers to the owner's questions; and **exactly one case**.

**A case is worked by the decision schema, all five parts and in this order:**

1. **Context** — what the thing is, how it works today, and which pages, modules and files it touches.
2. **The question** — the problem, or the fork between the options, stated so it can be answered.
3. **How it works after** — what the state is once this is decided, naming the target that receives it.
4. **Recommendation** — the session's own, with its ground.
5. **Ratification** — left for the owner, and filled with his words when he gives them.

**No case is opened until the previous one is ratified or explicitly deferred.** Two open cases is
how a session stops being answerable.

**And any question carries its context, case or not.** What the thing is, how it works today, what
would be built, the fork if there is one, and a recommendation with its ground. A clarifying question
is not exempt.

**The frontier is one concept with three carriers, and they are not interchangeable.**

- **`sprint.md` is the frontier between sessions**, and it is where a deferred item lands.
- **`brief.md` is its view at session start** — **generated** from `sprint.md`, never written by hand.
- **`grill-me` extends it** with what an interview opens.

**It is walked twice in a session** — before the plan is written, and again at the retro — and never
at the retro alone. **Every item not discussed is marked deferred**, in the chat, through the
feedback channel.
<!-- /text -->

# Why the printing obligation is in the slice

**The rule carries an instruction to print rather than only a description of the format, and that is
the one thing about it a later reader must not tidy away.** On 2026-08-30 the form held for
seventy-eight replies with nothing in the harness enforcing it; what carried it was the frontier line
at the top of each message, which re-stated the rule's own state every turn. A rule that describes a
shape is remembered until it is not. A rule that obliges a visible artefact is checkable by the owner
at a glance and, once the hook below exists, by a machine.

# What was absorbed, and the one line that had to be carried

**[[every-question-to-the-owner-carries-its-context]] is superseded by this page and not amended.**
Its five obligations map one-to-one onto four of the five parts above and the schema adds a fifth,
so the older rule is strictly contained
([[the-reply-format-becomes-a-rule-and-the-context-rule-is-absorbed-whole]]).

**The absorption was not lossless by default, and the line that closes the gap is in the slice.** The
older rule bound *every question*; the case schema binds a *case*. Without the sentence beginning
*And any question carries its context*, a clarifying question would have escaped the obligation the
older rule existed for — which the session that proposed the absorption named before the owner
ratified it, rather than discovering afterwards.

**Its two remaining paragraphs did not travel and did not need to.** *The cost is the asker's* is
ground, and ground stays off a slice by construction
([[what-travels-from-a-rule-page-is-a-marked-slice]]). *One question per message* is a bullet of
[[write-plainly-name-the-source-and-say-what-is-not-done]], which renders into the same section and
is untouched — all six of its bullets were compared and none overlaps.

# Where it lands, and beside what

**The region sits inside `## How to write it` in the repository's `CLAUDE.md`, in the place the
superseded rule's region held.** `governs:` is not unique across rules, so two rules rendering into
one section is the normal case ([[a-region-is-a-paired-comment-named-for-a-rule]]).

**The page and the markers are written by different parties, and that is why this rule could not
land in the session that decided it.** The librarian writes the page; the session places the paired
`<!-- rule: -->` markers. Three mechanisms make the split unavoidable rather than merely tidy, and
they are set out on [[a-decision-with-a-rule-target-cannot-close-inside-a-single-ingest]].

# The frontier's definition lives here on the owner's instruction

**It is not a separate rule page.** He ruled on 2026-08-30 that the frontier's three carriers belong
in `CLAUDE.md` as part of this rule, so the definition travels in the slice above rather than in a
page of its own ([[the-frontier-is-one-concept-with-three-carriers]]).

**One of the three carriers does not exist yet.** `brief.md` does not generate its frontier section
from `sprint.md` — nothing does — so the items deferred on 2026-08-30 reach the next session as
decision pages found by a grep rather than as a list. The obligation is written here as it was
ratified, and the gap is a decision of its own
([[the-brief-generates-its-frontier-section-from-sprint-md]]).

# The instrument it owes

**A `MessageDisplay` hook checking that the reply opens with the frontier line**, and it is not built
([[the-reply-format-rule-gets-a-hook-that-checks-the-form-and-not-the-fact]]). The obligation to name
an instrument or say why there is none is standing
([[every-rule-in-wiki-rules-owes-a-mechanical-instrument]]).

**Why a hook is admissible here where one was refused a few hours earlier the same day.** The
ratification hook the session argued against had to judge a **fact** that the session itself writes
into a ledger — the class that already produces false green smoke rows
([[the-smoke-gate-hooks]]). This one checks **form**, which is visible whole in the message and
cannot be faked without being performed. The two are different classes and the earlier objection does
not reach this one.

*(Compiled from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
