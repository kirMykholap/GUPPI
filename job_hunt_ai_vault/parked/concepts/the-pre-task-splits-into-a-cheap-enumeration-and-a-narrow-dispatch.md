---
title: "`/pre-task` splits into a cheap enumeration and a narrow dispatch, and only the reading was narrowed"
type: concept
status: current
authority: pre-task-phase-split
basis: measurement
sprint: S2
created: 2026-08-21
sources: ["archive/2026-08-21/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work/handoffs/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work.md", ".claude/agents/pre-task.md", "scripts/vault-catalogue.sh"]
tags: [agents, retrieval, process]
---

# The measurement the shape follows from

**The cost of the old ritual was never the enumeration.** One dispatch over `decisions/` alone was
**5m54s, 98k tokens, 36 tool uses, and it opened 12 pages in full.** Reading those 12 was the cost
([[agent-round-trip-cost]], [[a-subagent-cannot-report-its-own-cost]]).

**So the way to make it cheap is to shrink what is read, not to parallelise the search.** That is
also why the scout design was refused: it parallelises a phase that runs as a script in 1.66 s
([[the-scouts-proposal-is-refused-and-its-correctness-case-is-untouched]]).

# Phase 1 — the catalogue, in the caller's own context

`bash scripts/vault-catalogue.sh` — one pass over every page, 1.66 s, 566 rows, each carrying the
page, its `authority`, `title`, `status`, `sprint` and `tags`. Nothing is written to disk, so
nothing here can be stale ([[the-page-list-is-a-query-not-a-generated-file]], [[vault-scripts]]).

Filtered: `lessons/` and `archive/` dropped; `decisions/` reduced to `binding: prohibition`;
`concepts/`, `entities/`, `proposals/` and `rules/` kept whole. That leaves about **342 rows**
against the 193 the ritual used to cover — **wider coverage and less reading in the same change**
([[the-pre-task-enumeration-covers-every-folder-but-lessons]]).

**It is still an enumeration and not a search.** The whole filtered list is in front of the reader,
and only the *reading* is narrowed. **That property is why the ritual exists at all**: a ranked
partial answer is dangerous, because the decision a plan violates may be twelfth when a search
returned eight ([[one-librarian-behind-every-caller]]).

# Phase 2 — dispatch, and only over what phase 1 named

**A narrow dispatch over named pages measured 1m24s and 21.6k tokens**, against the 5m54s of the
folder sweep it replaces. **No candidates is a real answer** and costs the ten seconds above
([[one-pre-task-per-approved-scope-and-the-answer-comes-back-per-item]]).

**The dispatch is asked what is missing from the shortlist, and that clause is what reviews phase
1.** The list is chosen by the party that wrote the plan, from titles and `authority` alone; a page
reachable only by a link is invisible to the way the list was built, and the librarian walks links
([[the-folder-is-the-first-narrowing]], [[vault-librarian]]).

**A fork resolved by the party that created it is not reviewed** — which is the general form, and
the reason that paragraph of the skill is not optional
([[a-gap-named-by-a-reviewer-is-closed-by-a-mechanism-rather-than-by-care]]).

# Why the cheap half may live in the main context

**The clause forbidding that read in the main context is lifted, by the owner, deliberately.** It
was written when the alternative was opening every file in `decisions/`; what it now forbids is one
script call and about 17 KB of titles. **The reversal is on the record so that it is not re-derived
as an oversight and quietly restored** ([[switching-permission-modes-is-cache-safe]],
[[a-skill-is-a-mask-and-a-subagent-is-a-body]]).

# `binding:` gets its first reader here

**It is carried by 193 of 193 pages in `decisions/` and was read by nothing until this split.**
Phase 1 keeps `prohibition` and drops `deferral` and `divergence`, which forbid nothing — the exact
reading the vault's own `CLAUDE.md` tabulates for the field
([[a-decision-declares-whether-it-binds]]).

# The price quoted for phase 2 on this page is the price of something else — 2026-08-21

**The figure `1m24s` and `21.6k tokens` above is a narrow WRITE** — two frontmatter lines on two
named pages — read off the wrong row of [[agent-round-trip-cost]]. **It is not the price of phase
2's read, and phase 2 has never been run**, so no measured price for it exists
([[a-cost-figure-attached-to-the-wrong-unit-discourages-the-thing-it-prices]]).

**The sentence is marked rather than rewritten**, and the same figure stands in
`.claude/skills/pre-task/SKILL.md`, which is a session's file and not the librarian's
([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]).

*(**That file is deleted as of 2026-08-22**, so the figure stands on this page alone and the sentence
above is a reading of 2026-08-21 rather than a description of the tree. Dated where it stands and
not rewritten — [[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]],
[[the-date-of-a-correction-note-is-the-date-the-text-became-false]].)*

**Phase 2 also did not run on 2026-08-21**, and the plan of that day was approved on phase 1 alone
([[the-pre-task-ran-at-half-strength-and-the-permission-to-dispatch-arrived-after-the-plan-was-approved]]).

*(Marked at the ingest of `raw/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md`.)*

# Phase 2 was read by hand on 2026-08-22, and the clause that reviews phase 1 went unasked — 2026-08-22

**The section above says the dispatch is asked what is *missing* from the shortlist, and that clause
is what reviews phase 1.** On this date phase 2 was **read by hand instead of dispatched**, so the
question was never put to anyone — and the shortlist was short by one.

**The concrete cost, measured on the run rather than argued.** The list of pages taking a
disposition from the rule the owner struck was built by the party that wrote the plan, from `title:`
and `authority:` alone, and it named four. **A fifth,
[[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]], carries the clause *"the gate that
watches for it stops advising and starts refusing"* and cites the struck page for it** — and its
title says nothing about hooks, so the way the list was built could not see it. It surfaced while
the work was being executed, which is the one place a missing entry is found by accident rather than
by review.

**This is the failure shape the clause exists for, met in the only way it can be met**: the shortlist
is chosen by the party that wrote the plan, and a fork resolved by the party that created it is not
reviewed ([[a-gap-named-by-a-reviewer-is-closed-by-a-mechanism-rather-than-by-care]]). **Skipping
the dispatch does not degrade phase 2 to a cheaper phase 2 — it removes the only review phase 1
has.**

**It is a finding about the ritual and not about any of the pages involved.** The pages were
re-pointed; what was missing was the mechanism that would have named the fifth before anyone started
([[knowing-a-rule-is-not-a-mechanism]]).

**Phase 2 has now failed to run on two of the days this page records** — 2026-08-21, when the plan
was approved on phase 1 alone, and 2026-08-22. **The price of phase 2's read is therefore still
unmeasured**, exactly as the section above says.

# The citation moved from the skill to the agent, and the shape it describes moved with it — 2026-08-22

**`sources:` cited `.claude/skills/pre-task/SKILL.md` until today and now cites
`.claude/agents/pre-task.md`.** The skill was deleted on 2026-08-22, when the ritual became an agent
([[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]]), and rule 5 of the gate requires every
repository path in `sources:` to resolve — *a citation to a file that is not there is worse than
none: it reads as provenance and is not* ([[vault-scripts]]). **The address moves and the history
stays readable**: this page was compiled while the skill existed, so the move is dated here rather
than made silently.

**What this page cites it for and what survived the move.** Phase 1 as a catalogue pass, the filter
that drops `lessons/` and `archive/` and reduces `decisions/` to `binding: prohibition`, the
*enumeration and not a search* property with its twelfth-of-eight argument, and `binding:` getting a
reader — all four are in the agent's own text.

**What did not survive, and the sections above are dated rather than corrected:**

- **Phase 2 is no longer a dispatch.** The agent performs both phases in its own body and is told in
  as many words that it dispatches nobody. The ground given there is the empty case: when the
  enumeration lived in the caller and only the reading was dispatched, *no candidates* left no
  dispatch at all, so nothing could tell **checked and found nothing** from **did not check**. The
  heading *Phase 2 — dispatch, and only over what phase 1 named* describes the skill's shape and not
  the agent's.
- **The cheap half no longer lives in the main context**, so the section arguing that it may is
  about a file that is gone. Phase 1 runs inside the agent, and the reversal it records — the owner
  lifting the clause on 2026-08-21 — is testimony about that day rather than a description of the
  tree.
- **The shortlist is no longer built by the party that wrote the plan.** It is built by the agent,
  and the walk that reviews it is performed by the same agent. Whether that is the review clause
  honoured or the review clause dissolved is not settled here
  ([[a-gap-named-by-a-reviewer-is-closed-by-a-mechanism-rather-than-by-care]]).
- **The counts are not carried at the new address.** `566 rows`, `1.66 s`, `342 rows` and the
  `168 / 19 / 6` split are the skill's; the agent says *about 1.7 s* and prints no totals. They stand
  here as a reading of 2026-08-21 and nothing in the tree asserts them now.

# The price of phase 2's read is measured, and the section above saying it is not is dated — 2026-08-22

**Measured: 233,165 tokens, 49 tool uses, 10m40s, 65 pages opened in full, over a 43-page
shortlist.** Read off the harness's usage report rather than reported by the subagent, which is the
only way this project can get such a figure at all
([[a-subagent-cannot-report-its-own-cost]], [[agent-round-trip-cost]]).

**It is roughly three times the *3–5 minutes* the store estimated** for an agent doing the whole
ritual, and about seven times the «90 секунд» the owner had in front of him when he ruled that the
ritual must always run ([[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]]). **Whether a
price that far from the quoted one changes his answer is his to say, and it is still unasked.**

**What the figure is a price of, exactly.** It was taken on a `vault-librarian` dispatch over a
named shortlist — phase 2 as the skill defined it — because the pre-task agent did not exist when the
dispatch was made. The agent now does the same reading inside its own body, after its own phase 1,
so this is the closest measurement available rather than a reading of the mechanism that exists
today ([[a-cost-figure-attached-to-the-wrong-unit-discourages-the-thing-it-prices]]).

**The two sentences above that say no such price exists are left standing.** They were true from
2026-08-21 until this date, and a statement about a day is dated where it stands
([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).

# The agent's own body has a price, and the shape it was measured on is the one that exists — 2026-08-22

**Measured: 146,705 tokens, 57 tool uses, 13m36s**, over **53 pages shortlisted from 362 filtered
catalogue rows**, with **16 opened in full and 16 in part** — plus **2 reached past the `binding:`
filter** and **5 reached only by following a link**. Read off the harness's usage report
([[a-subagent-cannot-report-its-own-cost]], [[agent-round-trip-cost]]).

**This is the first reading of the mechanism this page describes as it now stands**, rather than of
the skill's two-party arrangement: one agent runs the filtered enumeration, builds its own shortlist
and does its own reading, and the figure covers all three.

**The two numbers this page has carried for the enumeration are joined by a third and none is
patched.** `342 rows` was the skill's reading of 2026-08-21 and `362` is this agent's of 2026-08-22;
the corpus grew between them and neither is a correction of the other
([[the-region-coverage-figure-is-dated-where-it-stands]],
[[a-figure-measured-before-the-tree-moved-is-not-a-measurement-of-this-tree]]).

## The two numbers that answer the question this page's *what is missing* clause was for

**Seven of the 53 shortlisted pages were not reachable the way a shortlist is built.** Two came from
past the `binding:` filter and five only by following a link from a page already open. The
sections above argue that a page reachable only by a link is invisible to the way the list is built,
and that the clause asking *what is missing* is what reviews phase 1; **this is the first run where
the walk and the list were performed by the same party and the walk's yield was counted.**

**Whether that is the review clause honoured or dissolved is still not settled here**, and it is not
settled by a count: the same party built the list and audited it
([[a-gap-named-by-a-reviewer-is-closed-by-a-mechanism-rather-than-by-care]]). **What the count does
show is that the audit half was not decorative.**

**In-part reading is now a category this page did not have.** 16 opened in full and 16 in part is a
different funnel from *opened 65 in full*, and the ten-page opening ceiling was written before either
([[the-folder-is-the-first-narrowing]], [[the-reading-funnel-is-delivered-as-a-procedure]]).

# The filter this page describes is not the filter that runs — 2026-08-26

**The section headed *`binding:` gets its first reader here* says phase 1 *"keeps `prohibition` and
drops `deferral` and `divergence`"*. That is the arrangement of 2026-08-21 and it is not the one on
disk.** The owner ruled on 2026-08-26 that phase 1 enumerates `prohibition` **and** `deferral`, and
discards `divergence` alone — a deferral is context a plan needs, and it was being thrown away with
the one value that teaches nothing
([[the-pre-task-keeps-deferral-in-phase-one-and-drops-divergence-alone]]).

**The prose paragraph telling the agent to reach past the filter by judgement is deleted in the same
change**, so the *"two came from past the `binding:` filter"* figure above is a reading of a
mechanism that no longer has a licensed way past it. `.claude/agents/pre-task.md` carries both edits.

**The evidence came out of this mechanism.** The `/pre-task` checking the plan that carried the
ruling reached past its own filter four times; all four pages were `binding: deferral`, and three of
the four changed a plan item
([[a-plan-can-be-factually-wrong-about-the-tree-and-the-pre-task-is-what-reads-the-tree]]).

**The section above is dated rather than rewritten**, because it is a true description of the split
as it stood between 2026-08-21 and this date
([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).

# The reading from the check-system plan — 2026-08-26

**Shortlist 87 pages, opened 48 in full**, plus `sprint.md`, `authority.md`, the vault `CLAUDE.md`
and two `_schema.yaml`. **532 catalogue rows enumerated from a corpus of 551.**

**It is the widest funnel recorded on this page** and the ratio is the least aggressive: 55 per cent
of the shortlist was opened, against 65 of 43 on one earlier run and 16 of 53 on another. **The
counts come out of the agent's answer and nowhere else** — nothing records them, and neither can be
recovered afterwards.

**What it found is on its own page and is not restated here**: a seven-line block where the plan
named two lines, a missing `type:` change and a missing register entry
([[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]],
[[a-plan-can-be-factually-wrong-about-the-tree-and-the-pre-task-is-what-reads-the-tree]]).

**Its own dispatch cost 214,722 tokens and about 17 minutes** — read off the harness, not
self-reported ([[agent-round-trip-cost]]).
