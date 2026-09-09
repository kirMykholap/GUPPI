---
title: "A session ends with `/retro`, then `/handoff`, then `/ingest`"
type: rule
status: current
governs: CLAUDE.md
render: region
basis: human
sprint: S2
created: 2026-08-17
sources: ["CLAUDE.md", "[[the-end-of-a-session-is-a-retrospective]]", "[[retro-interrogates-and-handoff-routes]]", "[[ingest-runs-after-handoff-at-the-end-of-a-session]]"]
decided_by: [[the-end-of-a-session-is-a-retrospective]]
tags: [harness, process, vault]
---

# What travels

<!-- text -->
**A session ends with** `/retro`**, then** `/handoff`**, then** `/ingest`**.** Retro interrogates the
session and resolves every open question with the owner; handoff routes what it found into the
journal; ingest compiles. The journal those write is the only thing the next session inherits —
nothing else in this repository carries what happened here. Skipping them does not lose the code,
which git has; it loses the reasons, which nothing else does.
<!-- /text -->

**That is the closing-ritual paragraph of the repository's `CLAUDE.md`, to the byte** — cut out at
`e478c19` by line number and diffed against the slice above rather than read against it. The diff is
empty.

Everything below this line stays on this page
([[what-travels-from-a-rule-page-is-a-marked-slice]]).

# Why the order is inside the rule and not left to the reader

**Each step's output is the next one's input, so the sequence is the rule and not a preference.**

| step | what it does | why it cannot move |
|---|---|---|
| `/retro` | interrogates — finds what the session would not volunteer | it has to run while the session is still in the room; nothing later can ask it ([[the-retro-step]]) |
| `/handoff` | routes — files what retro found into the journal | it decides destinations, and it needs findings to route ([[retro-interrogates-and-handoff-routes]]) |
| `/ingest` | compiles — turns the journal into pages | it reads the journal, so the journal must exist ([[ingest-runs-after-handoff-at-the-end-of-a-session]]) |

**The genres are kept apart on purpose.** Folding the interrogation into the handoff was rejected:
it produces one document that asks and classifies at once, with sections that have no destination —
*went wrong* is not a folder ([[retro-interrogates-and-handoff-routes]]). The owner's own test for
the split is quoted there: *"handoff literally means lay out the session's data and let go"*.

# Why it cannot wait for a question

**The ritual is the last thing in a session, so a reader who has not met this rule by then has
already ended without it.** There is no later moment at which the question could be asked and
answered usefully; the session is over, and what it knew is gone with the transcript.

**Skipping it does not lose the code, which git has; it loses the reasons, which nothing else does.**
That sentence is inside the slice and it is the rule's whole argument. The corollary is worth
stating outside it: a session that skipped the ritual and a session that never happened leave the
same tree. There is no absence to notice.

**That is measured, not feared.** The session that produced `aebb308` wrote **no journal at all**,
so `raw/` holds nothing for it, and six feedback lines sat undrained until the next session carried
them forward verbatim and marked them as inherited — dating them to the day they were found would
have been false ([[vault-feedback-file]]).

# What "the only thing the next session inherits" means exactly

A next session does inherit a brief, a vault and a repository. **All three are downstream of the
journal**: `brief.md` is derived and regenerated at every ingest, and the wiki is compiled from
`raw/handoffs/`, which is immutable ([[journal-vault-brief-each-artefact-has-one-owner]],
[[the-vault-is-compiled-not-retrieved]]). Nothing upstream of the journal survives the session that
held it.

So the claim in the rule is about the **source**, and read that way it is exact rather than
rhetorical.

# The word beside it, which is not part of this rule

**The paragraph defining "retrospective" sits next to this one in `CLAUDE.md` and is deliberately
not a rule page.** It is a definition rather than an imperative, so it fails the folder's admission
test ([[rules-becomes-a-type-of-its-own]]), and whether a non-rule record may render at all is an
open question with the owner.

It is not decoration. **The word meant two rituals for three days, and that ambiguity put two live,
contradictory answers into this vault about when `/ingest` runs** — one page read "the
retrospective" as the sprint's and moved the ingest to it, while this file read it as the session's.
Both were `current`, both `basis: human`, both dated 2026-08-16; the owner retired one on 2026-08-17
([[the-end-of-a-session-is-a-retrospective]],
[[ingest-runs-after-handoff-at-the-end-of-a-session]]). **A word that names two cadences is read as
whichever one the reader already has in mind**, which is a retrieval failure and not a wording one.

The sprint-level ritual is now called a **sprint retrospective**, and nothing is designed for it.

# What the rule deliberately does not carry

- **the retro's sections and its gate** — the failure shapes it asks about, and the rule that it
  does not end while an open question has no verdict
  ([[the-retro-step]], [[the-open-questions-list-is-built-whether-or-not-it-is-discussed]]);
- **the transit files** — `.superpowers/sdd/retro.md` and
  `.superpowers/sdd/vault-feedback.md`, which are different files on purpose
  ([[the-retro-writes-its-own-transit-file]]);
- **the mapping between the hops**, which is documented at each hop and copied nowhere
  ([[the-mapping-is-documented-at-each-hop-and-copied-nowhere]],
  [[the-handoff-template-maps-onto-the-categories]]);
- **what the ritual produces after the journal is written**, which still has no home
  ([[the-closing-ritual-produces-what-the-journal-cannot-hold]]).

A rendered rule carrying any of that would be a copy of a page, and copies here diverge — six copies
of the handoff mapping drifted while every one of them was well formed.

# Why no test holds it

**A session leaves no artefact that says a session happened.** A journal in `raw/` is evidence the
ritual ran; its absence is indistinguishable from a day nobody worked. A check could count journals
against nothing, and what a check over harness prose is worth is on the record — seven divergences,
none found by anything mechanical ([[no-rule-reads-a-harness-file]]).

Imperative, and enforced by no test: the folder's admission test, passed exactly
([[rules-becomes-a-type-of-its-own]]).

# Where it renders

`governs: CLAUDE.md` — a path from the repository root, resolved against nothing else
([[governs-is-a-path-from-the-repository-root]]). The text lands in a paired comment named for this
page's slug ([[a-region-is-a-paired-comment-named-for-a-rule]]).

**The page and its region belong in one change, and this page arrived first.** Until the session
marks the region and runs the injector, rule 12 reports this rule as governing a file that carries
no region for it ([[a-governed-file-with-no-region-is-an-advisory]]). If the rule is ever replaced,
the successor renders and this page does not ([[a-deprecated-rule-does-not-render]]).

# The instruction and the decisions are different pages

Three decisions stand behind this one sentence — [[the-end-of-a-session-is-a-retrospective]]
(`authority: end-of-session-ritual-name`), [[retro-interrogates-and-handoff-routes]]
(`authority: retro-and-handoff-split`) and [[ingest-runs-after-handoff-at-the-end-of-a-session]]
(`authority: ingest-cadence`). This page carries only the instruction and carries `governs:` in
place of an `authority:`, so it does not read as a fourth answer to any of those questions
([[rules-becomes-a-type-of-its-own]]).
