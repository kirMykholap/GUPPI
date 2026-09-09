---
title: "The shared reading discipline renders into every agent that reads the vault, rather than being copied into each"
type: rule
status: current
governs: [.claude/agents/vault-librarian.md, .claude/agents/pre-task.md, .claude/agents/decisions-agent.md, .claude/agents/lessons-agent.md, .claude/skills/vault-ask/SKILL.md]
render: region
basis: human
sprint: S2
created: 2026-08-22
sources: [".claude/agents/vault-librarian.md", ".claude/agents/pre-task.md", "scripts/vault-inject.sh", "[[a-pre-task-agent-and-a-post-tool-use-hook-that-writes-its-row]]", "[[the-reading-funnel-is-delivered-as-a-procedure]]"]
decided_by: [[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]]
tags: [retrieval, agents, harness]
---

# What travels

<!-- text -->
## Start here, every time

**Find the vault.** It is the top-level directory containing a `wiki/`; its name is the name
Obsidian displays and the owner changes it, so never assume one:

```bash
VAULT=$(ls -d */wiki 2>/dev/null | head -1 | sed 's|/wiki$||')
```

**Then read `$VAULT/CLAUDE.md`.** It is the single source for the rules of this store — categories,
frontmatter, statuses, supersession, tags, contradictions. Do not rely on memory of those rules,
and do not restate them anywhere.

## How to search

**Grep first, then follow links.** You do not need to find every relevant page — only one, and
walk from there via `[[wikilinks]]`.

```bash
rg -il "<term>" "$VAULT/wiki"
rg -i "<term>" "$VAULT/tags.md"      # aliases catch synonyms and the other language
```

The corpus is part Russian and part English: the pages are English, and the questions often are
not. **If a query in one language returns little, look up the term in `tags.md` — the aliases exist
for exactly this — and search again with the tag's canonical word.**

`$VAULT/index.md` is a map, not a catalogue. It names the categories, the naming rule, the current
sprint, and hub pages that are entry points into large subjects. Read it when you do not know where
to start; it will not list the page you want.

**Narrow before you open anything.** A full-text grep is the widest possible net and it is already
too wide: at `94483b1`, `rg -il vault "$VAULT/wiki"` matches **116 of 118** pages and `check`
matches 84. Go in this order, and stop as soon as you have a page worth walking from.

**The folder comes first, when the question names its kind.** The five folders are a
classification the search was not using, and they are the cheapest narrowing there is - already
written, free to apply, and never stale:

| the question | the folder |
|---|---|
| what was decided about X, what may I not do | `decisions/` |
| how does X work, why is it built that way | `concepts/` |
| what burned us, what went wrong | `lessons/` |
| what exists, and what is it like | `entities/` |
| what did we plan and never do | `proposals/` |

**If the question does not name its kind, search `wiki/` whole.** A guessed folder is a silent
miss - the page exists, the grep is clean, and nothing tells you that you looked in the wrong half.

```bash
DIR="$VAULT/wiki"                                  # or one folder of it, when the kind is known
rg --files "$DIR" | rg -i "<term>"                 # filenames - they are written to be searched
rg -l "^tags:.*<tag>" "$DIR"                       # then the tag, looked up in tags.md first
rg -il "<term>" "$DIR"                             # full text last, and only if those found nothing
```

**The tag is applied inside the folder, not instead of it.** On its own it stopped narrowing some
time ago: `tags: vault` selects 51 pages at `94483b1`, five times the ceiling below, while the same
tag inside `concepts/` selects 11. `vault-check.sh` now measures tag density per folder for exactly
this reason and names the folder in its advisory.

If a full-text grep returns more than about fifteen files, do not start opening them: go back to
`tags.md` and narrow. That list will keep growing, and the day it stops being eyeball-able is not
announced.

**Never read the whole vault.** If you find yourself opening more than about ten pages for one
question, stop and say what you could not narrow down. That is a miss worth reporting, not a reason
to read everything. **The ceiling is about topic queries.** `/pre-task` asks a different question —
"what constrains this plan" — where a ranked partial answer is the dangerous one; there you
enumerate frontmatter cheaply across every `decisions/` page and open only what the titles
implicate.
<!-- /text -->

**That is `## Start here, every time` and `## How to search` from `.claude/agents/vault-librarian.md`
as they stood at `c9f4637`, to the byte.** Verified the way every migration here is verified: lines
12–83 were cut out of that file by number and diffed against the slice above rather than read
against it. The diff is empty ([[fidelity-to-a-source-and-fidelity-to-the-tree]] for why a move is a
third fidelity and is answerable exactly). Everything below this line stays on this page
([[what-travels-from-a-rule-page-is-a-marked-slice]]).

**Both headings are inside the slice, and that departs from the precedent deliberately.**
[[english-in-the-repository-russian-with-the-owner]] keeps `## Language` outside its region, as
furniture the destination owns. That cannot be done here: the slice spans two sections, so
`## How to search` sits in the middle of it and travels whether anybody likes it or not. **Once an
interior heading travels, leaving the outer one behind makes the rendered shape a property of where
somebody put the marker** — which is the objection this store already sustained against splitting
`## Language` into two pages ([[a-rule-ships-one-piece-of-text-or-it-is-more-than-one-rule]]).

**The slice carries three fenced blocks and no wikilink.** Fences survive into the destination
([[a-fenced-block-inside-a-slice-survives-into-the-destination]]); an Obsidian link would be red, so
every citation on this page is in the prose around the slice
([[a-wikilink-inside-a-rendered-slice-is-red]]). **No line of the slice carries trailing
whitespace** — measured, zero space-terminated and zero tab-terminated lines — so unlike the language
rule this one is whitespace-indifferent and an editor that trims on save cannot redden it.

# The owner ruled on 2026-08-22 that this is one page, and that `## Answering a topic query` is not in it

**He selected one rule page carrying the two sections above and not the third.** Two alternatives
were on the table and both were rejected.

**Rejected: one page carrying all three sections.** The proposal's arithmetic counted the topic
answer's shape as shared — about 100 of the librarian's 151 lines
([[a-pre-task-agent-and-a-post-tool-use-hook-that-writes-its-row]]) — and it is not. **The ten-page
ceiling and the stop-and-report discipline are written about *topic* queries**, and `/pre-task` asks
the opposite question, where a ranked partial answer is the dangerous one
([[one-librarian-behind-every-caller]],
[[one-pre-task-per-approved-scope-and-the-answer-comes-back-per-item]]). Rendering that section into
the pre-task agent would ship it a discipline it must not follow — a rule delivered correctly and
obeyed wrongly, which is worse than one that never arrived.

**Rejected: two pages, the second carrying the topic answer.** The second would render into exactly
one file, which is a mechanism with no second addressee: the injector exists because a rule copied
into two places diverges, and there would be nothing to diverge from
([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]], [[no-rule-reads-a-harness-file]]).

**This closes a fork that was left explicitly open.**
[[the-reading-funnel-is-delivered-as-a-procedure]] asks *whether it is one rule or two* and *whether
`/pre-task` is a caller of it or a separate change*. Both are answered here: one rule, and
`/pre-task` is a second addressee rather than a separate change — which is what made the inline
`governs:` list worth having
([[governs-takes-a-bare-path-or-an-inline-list-and-the-block-form-is-red]]).

# What the ruling accepts, recorded rather than repaired

**The two closing sections of an answer — Sources, and Not in the vault — fall outside this slice
and are stated twice.** `.claude/agents/pre-task.md` writes them in its own words, and the librarian
keeps them in `## Answering a topic query`. That is a duplication of a few lines, in exactly the
class the injector was built to end, and the owner's choice takes it knowingly: the alternatives were
a third rule page rendering four lines into two files, or shipping the pre-task agent a ceiling it
must break.

**It is named here so that a later reader does not find it and repair it as an oversight.** The
repair, if it is ever wanted, is a rule page of its own for those two sections alone — and it would
have two addressees, which is the test the rejected second page failed
([[a-rule-ships-one-piece-of-text-or-it-is-more-than-one-rule]]).

# Why a new page rather than an extension of an existing one

**`bash scripts/vault-authority.sh --near` was run before this page was written, and a rule page is
the one candidate the lookup cannot be run *on*.** A rule carries no `authority:`
([[authority-beside-governs-is-forbidden-on-any-page]]), so there is no slug to look the candidate up
under; the query was run against the nearest live owners instead.

**`--near retrieval-narrowing` returns the family *finding a page in this store*** — eleven slugs, of
which two are the real neighbours: [[the-folder-is-the-first-narrowing]] holds the funnel and its
measurements, and [[the-reading-funnel-is-delivered-as-a-procedure]] holds the design for delivering
it. **Neither can carry this claim, and for opposite reasons.** The first is a `concept` on
`basis: measurement`: it explains *why* the funnel is shaped this way, and its text is not written to
be rendered — moving it into `wiki/rules/` would send four measured numbers into two agent files,
which is the shape this store has already priced
([[a-cost-figure-attached-to-the-wrong-unit-discourages-the-thing-it-prices]],
[[a-title-names-what-is-counted-instead-of-counting-it]]). The second is a `proposal`, and a proposal
is never a record of something that exists; it is the page that asks whether this rule should exist
at all, and it is answered rather than extended.

**`--near reading-discipline` returns no group**, which is the shape of a candidate whose question
nobody has claimed — and it is also what a hole in the index looks like, so it was not read as an
answer on its own ([[authority-becomes-the-index-and-is-required-outside-rules]]).

**The text was not new either way.** It has lived in `.claude/agents/vault-librarian.md` since that
file was written; what is new is that a second reader needs it, and the repair for that is rendering
rather than copying — so this page ends a duplication rather than starting one
([[no-new-entity-where-an-existing-one-can-carry-the-claim]]).

# Where it renders, and what is owed at the destination

**`governs:` names four agent files under `render: region`, written in the inline form.** *(It named
two until 2026-08-29; the sentence below still reads as though it named two, and the correction is
the section at the end of this page rather than a rewrite here.)* The block form is red and refused loudly rather than ignored, because a
half-parsed list would render this text into one of the two agents and leave the other reading as
drift ([[governs-takes-a-bare-path-or-an-inline-list-and-the-block-form-is-red]],
[[the-governs-list-is-expanded-at-the-walk-and-the-address-verdict-asks-membership]]).

**This is the second page in the corpus to name more than one destination**, after
[[a-block-attributed-to-the-owner-is-written-in-his-own-russian]], and the first to name two agents.

**It carries no `authority:`, which is required rather than chosen**
([[authority-beside-governs-is-forbidden-on-any-page]]).

**The page and its regions belong in one change, and this page arrived first.** The librarian writes
`wiki/`; marking the `<!-- rule: … -->` pair in each agent file and running the injector are the
session's. Until that happens, `bash scripts/vault-inject.sh` reports that both agents carry no
region for this page — **the expected state of a half-finished landing, not a defect in this page**
([[a-region-is-a-paired-comment-named-for-a-rule]], [[a-governed-file-with-no-region-is-an-advisory]],
[[a-check-asks-by-running-the-writer-it-checks]]). The injector writes the blank line after the slice
itself and it is not typed onto this page
([[the-injector-writes-the-separator-inside-the-region]], [[the-marker-carries-the-records-type]]).

**One thing the gate cannot check and a human must**: that the region lands where the text makes
sense in the file it lands in. In the librarian it replaces the sections it was cut from, under
`# The librarian`; in the pre-task agent it belongs above `## Phase 1`, because the enumeration that
phase runs is a use of the funnel the slice describes ([[a-gate-guarantees-agreement-never-truth]],
[[a-mechanisms-first-use-outside-its-home-is-where-it-drifts]]).

# What the slice says that a second reader most needs

**The carve-out is already inside it.** The last paragraph ends by saying the ceiling is about topic
queries and names `/pre-task` as the question where a ranked partial answer is dangerous. So the
pre-task agent receives the ceiling **and** its own exemption in the same breath, which is why the
two sections could travel unchanged into a file whose whole job is the opposite discipline
([[the-folder-is-the-first-narrowing]] states the same shape: bound the reading where a partial
answer is safe, never where it is dangerous).

**And the wide half stays licensed.** *The ten-page ceiling is about opening a page, never about
searching for one* is the sentence the funnel's delivery was said to stand or fall on
([[the-reading-funnel-is-delivered-as-a-procedure]]); it is in the slice, in the librarian's own
words, and it now reaches the agent that runs `bash scripts/vault-catalogue.sh` over the whole
corpus ([[vault-scripts]], [[the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch]]).

# Two more destinations, and the librarian marked them itself — 2026-08-29

**`decisions-agent` and `lessons-agent` join the list**, which is what the section above predicted the
day the rule was written: every agent that reads this vault renders this text rather than carrying a
copy. Both were created on 2026-08-29, both grep the corpus, and neither had the discipline in front
of it ([[the-decisions-agent]], [[the-lessons-agent]]).

**The visible form of the obligation was the region-coverage advisory moving from `9 of 15` to
`9 of 17`.** The plan that built the two agents predicted the advisory would not move and was wrong;
the movement is correct, and it is the denominator growing by two governed files that carry no region
([[the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count]]).

## The librarian placed the marker pairs, and that is a crossing it is reporting

**The section above assigns marking to the session, and the ingest of 2026-08-29 was not given one.**
The dispatch ordered the `governs:` write and named no party for the regions — the unstated
prerequisite this store has already recorded, from the day the librarian marked up the repository's
`CLAUDE.md` to render the style rule ([[vault-librarian]]).

**What was typed by hand into each destination is two comment lines and nothing else.** The text
between them was written by `bash scripts/vault-inject.sh`, which is the boundary that matters: no
rule text was typed into a harness file.

**The two ways out were to refuse or to cross and say so**, and refusing would have left
`bash scripts/vault-check.sh` exiting 1 for the whole of an ingest whose last step is a gate run
([[a-check-asks-by-running-the-writer-it-checks]]).

**The general repair is still the one already written down**: a dispatch that orders a render names
who marks the region. Three landings have now taken the crossing shape instead.

## What the session is owed at both destinations, and it is a deletion

**Each of the two agent files carries a hand-written `## Find the vault first` section that the
rendered slice now says again**, in more words and with the search discipline attached. **The
duplicate is the hand-written one** and removing it is a session's edit, not the librarian's — the
librarian may add a marker pair and may not delete harness prose
([[the-harness-is-compiled-not-maintained]]).

**Placement was chosen to make that deletion safe rather than to look tidy today.** The region sits
immediately after the hand-written block in both files, so the two can be read side by side and the
older one cut without moving the marker.

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
