---
title: "A new entity earns its place only when no existing one can carry the claim"
type: rule
status: current
governs: .claude/agents/vault-librarian.md
render: region
basis: human
sprint: S2
created: 2026-08-21
sources: [".claude/agents/vault-librarian.md", "scripts/vault-authority.sh", "CLAUDE.md"]
decided_by: [[occams-razor-is-the-ground-rule-for-the-vault]]
tags: [vault, agents, retrieval]
---

# What travels

<!-- text -->
**A new entity earns its place only when no existing one can carry the claim.** Before creating a
page, run `bash scripts/vault-authority.sh --near <candidate-slug>` and read the family it returns.
If an existing page can be corrected, extended or superseded instead, that is the repair. Say in
`log.md` what the lookup returned and why a new page was still right.

Appending to a page, reordering it, and marking a sentence false are all allowed. **A sentence a
source asserted is never rewritten** — `raw/` is immutable and the coverage sidecar is keyed by its
line, so a rewrite leaves a verdict pointing at text that is gone. Date every addition and name the
journal it came from.
<!-- /text -->

The decision behind it is [[occams-razor-is-the-ground-rule-for-the-vault]], taken by the owner on
2026-08-21; this page carries the text that decision obliges and everything below the line stays
here ([[what-travels-from-a-rule-page-is-a-marked-slice]]).

# Why it governs the librarian's own agent file and not the ingest skill

**The owner's choice, in his own words:** *"он касается только библиотекаря. То есть в нашей
архитектуре — это может быть рендер правила именно агенту библиотекарь."*

It is the right destination for a reason the store can state. **`wiki/` has exactly one writer**,
and the moment a page is created is a moment inside that writer — not inside `/ingest`, which is a
ritual that *dispatches* the librarian, and not inside a session, which may not write here at all.
A rule delivered to the skill would reach the party that asks for pages; delivered to the agent it
reaches the party that makes them. **The only party that can obey this rule is the one holding the
pen.**

It also reaches every caller for free. `/ingest` is one dispatch of the librarian; `/vault-ask` and
`/pre-task` are others, and all of them run the same definition
([[one-librarian-behind-every-caller]], [[vault-librarian]]). A rule rendered into the skill would
have had to be copied into the others, which is the shape this project has already been burned by
([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).

# What the rule costs, and why the lookup is named in the text rather than left implied

**A rule you cannot look anything up for is an exhortation.** "Do not multiply entities" was true
before 2026-08-21 and the corpus reached 479 pages in nine days anyway, because nothing in the
writing loop asked the question. The imperative therefore names the command, so obeying it is an
action rather than an attitude: `bash scripts/vault-authority.sh --near <slug>` prints the family a
candidate belongs to, from frontmatter only, without opening a page
([[authority-becomes-the-index-and-is-required-outside-rules]]).

**The lookup is cheap on purpose and stays outside the reading ceiling.** The ten-page limit in the
librarian's definition is about *opening* a page, never about searching for one; a frontmatter
sweep over the whole corpus is one pass and is the wide half of that rule.

# The two halves are one rule because splitting them was the failure mode

The second paragraph is not a footnote. **A rule that says "extend rather than create" and stops
there is a licence to rewrite the corpus**, and this store's one working fidelity instrument — the
coverage sidecar, keyed by a line number in an immutable `raw/` file — cannot survive that. A
rewritten sentence leaves the verdict green and pointing at text that no longer exists
([[fidelity-to-a-source-and-fidelity-to-the-tree]]). So the boundary travels with the permission,
in the same slice, and neither can be read without the other.

# Why the slice says `log.md` out loud

**The rule converts a mechanically visible failure into an invisible one.** Two `current` pages
sharing an `authority` are caught by rule 3 of `vault-check.sh` on every run; a claim wrongly folded
into a page that does not own it looks like a healthy page and always will. The trail is the whole
compensation, and it was accepted as a weaker one knowingly
([[a-wrong-record-is-acceptable-and-an-invisible-one-is-not]]). A merge that is not written down is
not reviewable, and an unreviewable merge is the failure this rule was supposed to be worth.

# Where it renders

`governs: .claude/agents/vault-librarian.md` under `render: region` — a marked region inside a file
that has a life of its own, so the injector owns the slice and nothing else
([[governs-is-a-path-from-the-repository-root]]). The agent file was in the uncovered set the gate's
harness advisory prints until this page landed; it is the first rule rendered into an agent
definition rather than into `CLAUDE.md` or a generated file.

# Its first audit — 2026-08-29

**Ten pages judged: the ten the ingest of 2026-08-26 created.**

- **4 could have been a dated section on an existing page.**
- **4 genuinely needed a page of their own.**
- **2 turn on a ruling nobody has given.**

**The log trail this rule requires is present for 8, partial for 2, absent for none.**

**So the rule is obeyed in form. It does not show that the lookup was run before the write** — and
nothing can: `bash scripts/vault-authority.sh --near` leaves no trace, and this page's own text calls
the log entry *the whole compensation*. **A rule whose only evidence is the record its subject writes
about itself cannot be audited for compliance, only for plausibility.**

**And the audit found a question this rule does not ask.** Two of the ten restate a claim an existing
page already carried **in a dated section written by the same ingest** — archive-path-length against
[[vault-archive-sh]], and smoke-gate-inference against [[the-pre-task-state-library]]. The admission
lookup ran and the log recorded why a new page was still right, so the rule did not fail. **What it
does not ask is whether the claim was already being written elsewhere in the same pass**, which no
lookup against the tree can see, because the other write had not landed yet.

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*
