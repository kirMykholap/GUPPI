---
title: "The repository's `CLAUDE.md` becomes a dispatch table pointing at skills and agents"
type: decision
status: current
authority: claude-md-dispatch-table
binding: prohibition
basis: human
sprint: S1
decided: 2026-08-16
created: 2026-08-16
sources: ["archive/2026-08-16/2026-08-16-the-structure-questioned/handoffs/2026-08-16-the-structure-questioned.md", "CLAUDE.md"]
tags: [process, vault, agents]
---

# Decided 2026-08-16: it points at callable things, not at knowledge

The shape the owner named: *"Need to know what is decided → call this skill. Need to start a slice
→ call this agent."* The file stops carrying assertions and carries entry points.

**Rejected: reversing [[claude-md-is-a-map-and-four-rules]] to re-admit wikilinks.** The owner does
not want them there. His argument is that **a pointer at a skill is checkable exactly as a pointer
at a page is** — the skill either exists in `.claude/skills/` or it does not — so the checkability
that made wikilinks attractive is available without them.

## What it obliges

- **The four rules move out**, into the `rules` type ([[rules-becomes-a-type-of-its-own]]). They
  are in that file because obeying them late is the same as not obeying them at all
  ([[claude-md-is-a-map-and-four-rules]]), and the injection mechanism is what has to preserve that
  property once they leave.
- **"Where things are" is dropped or generated.** It is the block that has already gone stale, and
  the newest instance was created inside one hour by a file move
  ([[claude-md-can-lose-an-assertion-but-cannot-strand-a-page]]).

**This supersedes nothing yet.** [[claude-md-is-a-map-and-four-rules]] still describes the file as
it stands on disk; this page describes what it becomes, and the retirement belongs to the session
that performs the change rather than to the one that recorded the intention.

The check that would guard the result — *it may point and may not assert* — is designed and not
taken: [[claude-md-may-point-and-may-not-assert]].

## Performed in part on 2026-08-17, and the owner read his own wording narrower than intended

**"This supersedes nothing yet" is no longer true.** The session of 2026-08-17 performed the change this
page described, so [[claude-md-is-a-map-and-four-rules]] is retired to `archive/` and its successor is
[[the-repository-claude-md-after-the-rules-left-it]]. Both obligations above are discharged: **the rules
moved out**, all nine of them ([[wiki-rules-holds-the-rules-of-the-repository-claude-md]]), and
**"where things are" was dropped** rather than generated, with the generator deferred
([[where-things-are-is-deleted-now-and-generated-later]]).

**And the owner narrowed the phrase this page opens with.** *"The file stops carrying assertions"* means
**no *unsourced* assertions** — because this decision was taken on 2026-08-16, before a renderer existed,
so its two options were a hand-written assertion or a pointer and **the third did not exist**. A rendered
assertion has a page behind it, is corrected in one place, and reddens the gate when it drifts
([[an-assertion-may-render-into-claude-md-but-not-be-typed-there]]).

**So the project description stays in that file** — as a rendered record, once a non-rule page can render
at all ([[governs-becomes-a-property-of-any-page]]).

**What is not done: the file is not a dispatch table.** It carries rendered rules, the routes into the
vault, a project description and a command list. Rule 5b still passes vacuously, because there are no
wikilinks in it to check ([[claude-md-may-point-and-may-not-assert]]).
