---
title: "The gate judges more writers than the librarian, which is why it exists even though `wiki/` has one writer"
type: concept
status: current
authority: gate-subject-writers
basis: code
sprint: S3
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names/handoffs/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names.md", "scripts/vault-check.sh"]
tags: [vault, testing, harness]
---

# The question, and it is the owner's

**If the librarian is the only writer of `wiki/`, what is the gate for?**

# More than half its rules do not judge librarian output

| rule | what it judges | who wrote that |
|---|---|---|
| 8 | a **journal** | the session |
| 11 and 12 | **regions in harness files** | `scripts/vault-inject.sh` |
| 5b | the repository's `CLAUDE.md` | the session ([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]) |
| the schema keys and values | `wiki/*/_schema.yaml` | the session, by the same clause |

**The librarian is one writer among several**, and the rules that do judge its output are judging a
store several parties write into.

# And the rest of the answer is on the gate's own instruction

> each rule exists because that failure has already happened here at least once

**A gate does not guarantee truth; it guarantees agreement** ([[a-gate-guarantees-agreement-never-truth]]).
What it defends is the set of properties this store has already lost once — a citation pointing at
nothing, a page with two claims to one question, a region that drifted from the page it renders
([[vault-scripts]]).

# Why the one-writer clause and the gate answer different questions

**The one-writer clause is about a knowledge base disagreeing with itself** — two parties writing
prose into the same corpus ([[parallel-librarians-break-the-one-writer-property]]).

**The gate is about the tree being addressable**: links resolve, slugs are unique, regions match their
pages, journals carry their sections. A single honest writer breaks all four routinely, and the
mechanical writers break them without knowing.
