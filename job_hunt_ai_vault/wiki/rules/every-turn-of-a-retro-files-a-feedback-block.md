---
title: "Every turn of a retro files a `VAULT-FEEDBACK` block, in the turn the thing happens"
type: rule
status: current
governs: .claude/skills/retro/SKILL.md
render: region
basis: human
sprint: S3
created: 2026-08-26
sources: [".claude/skills/retro/SKILL.md", ".claude/hooks/remind-the-smoke.ps1", "CLAUDE.md", ".claude/templates/retro.md"]
decided_by: [[divergence-the-retro-filed-no-feedback-block-while-it-ran]]
tags: [harness, process, vault]
---

# What travels

<!-- text -->
**Every turn of this retro files a `VAULT-FEEDBACK` block.** Mandatory, on the owner's ruling — not
once at the end, and not folded into the retro file: in the turn the thing happens.

**The two artefacts hold different things.** `.superpowers/sdd/retro.md` holds what was **resolved**;
the block holds what was **observed**, in the turn it was observed. A retro writes an artefact of its
own, which is exactly why the recording feels already done here and is not.

**A turn that genuinely produced nothing recordable says so in one line**, rather than filing nothing
silently.
<!-- /text -->

Everything below this line stays on this page
([[what-travels-from-a-rule-page-is-a-marked-slice]]). The slice carries no `[[wikilink]]`, which is
a verdict rather than a preference — the destination is a file where Obsidian syntax is inert
([[a-wikilink-inside-a-rendered-slice-is-red]]) — so every citation on this page sits outside the
marks above.

**It is short on purpose.** The destination is a skill that already runs to 232 lines and eight
steps, and every line rendered into it is read at every invocation. What travels is the obligation
and the one property that makes it stick; the count of failures behind it, the argument, and the
measurements are below and reach nobody who has not come looking.

# Why this rule exists when a general one already says the same thing

**[[speak-the-feedback-in-the-turn-and-the-hook-files-it]] already binds every session in every
turn.** This one does not widen it, contradict it or replace it. It says the same obligation **at
the one ritual where it has been broken repeatedly**, and adds the two clauses that are specific to
that ritual: the retro's own file is not a substitute, and a barren turn is declared rather than
skipped.

**The general rule was not extended to a fourth destination instead.** Its slice is 21 lines and
carries a fenced block of the four kinds; rendering it into `/retro` would deliver the channel's
grammar to a party that already has it, and would deliver none of the two clauses above. The
question this rule answers is not *how do I file a line* — it is *why does this particular ritual
stop filing them*.

# The history it rests on, and it is a count of failures rather than an argument

**Three recorded silences, and the third happened while the repair for the second was owed.**

| when | what happened |
|---|---|
| before 2026-08-26 | the owner records a first occurrence; nothing was written down at the time |
| 2026-08-26 | a retro ran **eight exchanges** carrying **twenty-one decisions, four measurements and three of the session's own errors** and filed **not one block**. The owner caught it and said it was the second time. Its own extract for the day: 4 blocks across 65 replies, all of them before the retro |
| 2026-08-26, the next session | the retro ran **nine replies with zero blocks** before he caught it again |

**The divergence page of the second occurrence closes with *"until it is, the same silence is one
session away"*, and it was exactly one session away**
([[divergence-the-retro-filed-no-feedback-block-while-it-ran]]). The sentence was written about an
instruction that had been ruled and not written; the next retro is what it was predicting, and it
is the reason this page exists rather than a fourth reminder.

**The ruling is the owner's and the wording is the session's.** The journal recorded it in the
session's own English rather than in his Russian, so nothing here is signed as a quotation
([[a-block-attributed-to-the-owner-is-written-in-his-own-russian]]).

# Two shapes were ordered and both are built, and neither is a per-turn mechanism

**The rule was ordered in one shape and delivered in two, deliberately.**

| shape | where it lives | when it speaks |
|---|---|---|
| a demand at the head of the reminder hook | `.claude/hooks/remind-the-smoke.ps1`, `PostToolUse` on matcher `Skill`, narrowed to `retro` | once, at the moment `/retro` is invoked |
| this rule's rendered region | `.claude/skills/retro/SKILL.md` | once, when the skill is read at invocation |

**Saying that plainly is the point of this section.** Prose in a skill is read once, at invocation;
the hook speaks once, at the same moment. **Neither fires per turn, which is the cadence the rule
is about**, and the failure being repaired is a channel that goes quiet in exchange five of eight.
So the honest claim is that the obligation is now *stated where it is performed and spoken when it
begins* — not that the problem is closed ([[knowing-a-rule-is-not-a-mechanism]]).

**What would close it is not designed here.** A per-turn observer would have to read what the
assistant says and notice the absence of a block, which is the shape
`.claude/hooks/catch-the-feedback.ps1` already half has — it reads the message and lifts the fence
out ([[the-feedback-catcher-hook]]). Whether it should also speak when it finds none is a question
nobody has put to the owner, and it is not answered by this page.

# The instrument this rule owes, and what it can and cannot have

**Every page in `wiki/rules/` owes a mechanical instrument**
([[every-rule-in-wiki-rules-owes-a-mechanical-instrument]]), and criterion 1 of S3 is decided by the
two selftests reporting `missed 0`.

**Half of it exists, and one case is this rule's own.** `scripts/hook-selftest.ps1` carries
*the reminder demands a feedback block every turn of the retro*, which asserts that the hook's output
holds both `VAULT-FEEDBACK` and *every turn*; beside it are the cases that the reminder fires on a
plugin-scoped `retro`, is silent on any other skill, is silent when the tool is not `Skill`, and
exits 0 on a malformed payload. Those observe the **hook**. Rule 12 of the gate observes that the
**region** in the skill agrees with the slice above
([[a-check-asks-by-running-the-writer-it-checks]]).

**The case's own comment says why it exists rather than being trusted**: the failure it addresses is
a session reading the instruction and not acting on it, so at minimum the instruction has to be
there to be read.

**The half that cannot be had is the compliance.** No check can read a retro's turns and say a block
was owed and not filed; *this turn produced something recordable* is a judgement, which is the same
boundary the general feedback rule already names ([[rules-becomes-a-type-of-its-own]]). The
instrument holds the channel, never the noticing.

# Where it renders, and what that does to the sprint's fourth criterion

**`governs: .claude/skills/retro/SKILL.md`** — a path from the repository root, resolved against
nothing else ([[governs-is-a-path-from-the-repository-root]]). One region, a paired comment named for
this page's type and slug, alone at column zero
([[a-region-is-a-paired-comment-named-for-a-rule]], [[the-marker-carries-the-records-type]]).

**The skill is one of the seven files the gate's advisory names as covered by neither a region nor a
whole generation.** Read on 2026-08-26, before this page was written: *a region or whole generation
covers 8 of 15 harness markdown files*, with `.claude/skills/retro/SKILL.md` in the uncovered list.
Marking the region moves that reading to 9 of 15 — **the denominator does not grow, because the file
was already in the swept set** ([[a-governed-file-with-no-region-is-an-advisory]],
[[the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count]]).

**Nothing here reads criterion 4.** That criterion asks for 15 of 15 and reading it is the owner's
([[a-sprint-closes-on-its-goal]]). What this page contributes is one file's worth of movement,
stated as a reading rather than as progress.

**The page arrives before its region, which is the expected state of a half-finished landing.** The
librarian writes `wiki/`; marking the region and running the injector are the session's. Until that
happens the injector reports that the skill carries no region for this page and rule 12 is red — not
a defect in the page ([[a-check-asks-by-running-the-writer-it-checks]]).

# What the destination already carries, and what the region has to displace

**The prose is already typed into the skill**, at the head of `.claude/skills/retro/SKILL.md` under
the heading *Every turn of this retro files a `VAULT-FEEDBACK` block*, and it is longer than the
slice above and carries a `[[wikilink]]`.

**The ordering is the one this store has already paid to learn: verify the rendered region is
present, then delete the typed prose, and never the reverse**
([[the-maps-region-replaces-the-prose-it-duplicated]],
[[claude-md-can-lose-an-assertion-but-cannot-strand-a-page]],
[[a-mechanisms-first-use-outside-its-home-is-where-it-drifts]]). A duplicate paragraph beside its own
region is the failure that lesson records, and it is available here today.

**The wikilink in the typed prose is why the slice is not a straight cut of it.** A rendered
`[[slug]]` arrives in a skill as punctuation pointing nowhere, so the citation moved onto this page
and the sentence around it was shortened to survive without it. **That is a rewording during a move**,
which this store normally refuses ([[the-suite-never-runs-against-the-production-database]]) — it is
declared here rather than hidden, because the alternative was a red slice.

# What this page does not claim

**It carries no `authority:`**, which is the folder's rule rather than a declined question: a rule
answers with `governs:` ([[authority-beside-governs-is-forbidden-on-any-page]]).

**It does not claim the retro's channel is fixed.** Three silences are recorded and the third
happened after the ruling; the fourth would be evidence that a rendered rule is not enough either,
and that is worth knowing rather than assumed away.

**It does not say what a session does with a block once filed.** `/handoff` drains the file and
`/ingest` files each line under the kind it names, and that is the general rule's to state
([[speak-the-feedback-in-the-turn-and-the-hook-files-it]]).
