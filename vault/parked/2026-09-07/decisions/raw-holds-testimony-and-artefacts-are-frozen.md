---
title: "`raw/` holds testimony; a spec and a plan are artefacts, frozen and cited rather than compiled"
type: decision
status: current
authority: raw-scope
binding: prohibition
basis: measurement
sprint: S1
decided: 2026-08-16
created: 2026-08-17
sources: ["archive/2026-08-16/2026-08-16-the-harness-becomes-a-build/handoffs/2026-08-16-the-harness-becomes-a-build.md", "docs/superpowers/specs/2026-08-16-harness-and-schemas-design.md"]
tags: [vault, process]
---

# Decided 2026-08-16: the line is testimony against artefact

**A journal is testimony** — an account of what a session believed. **A spec and a plan are
artefacts** — an instruction that was executed. Testimony is compiled into the wiki; artefacts are
**frozen and cited**. This settles what had been an open question about whether the documents under
`docs/superpowers/` should be ingested at all.

## The measurement that decided it, and it was not an argument

| | units | dispatch |
|---|---|---|
| the journal of 2026-08-16 | 75 | 15-29 minutes ([[agent-round-trip-cost]]) |
| a spec | 175-289 | — |
| a plan | 354-525 | — |

`docs/superpowers/` holds **16,644 lines of plans against 2,488 across all six journals** — roughly
**ten times the present ingest workload**, with every unit owing a verdict
([[ingest-is-units-and-verdicts]]). The mass was already measured once, on the same side:
[[the-unreadable-mass-is-in-the-plans-not-the-vault]]. This is the second question that session
settled by measuring instead of arguing ([[measurement-settled-what-argument-could-not]]).

**The mechanical proof is S1's own criterion 2** — *every source in `raw/` reports
`INGEST COMPLETE`*. A spec placed in `raw/` breaks that criterion **by construction**, because it
will never earn 289 verdicts ([[handoff-retires-only-when-every-unit-has-a-verdict]]).

## Freezing is what an artefact actually needs

**Thirteen pages cite `docs/superpowers/specs/2026-08-13-second-brain-design.md`, a mutable file.**
A citation into a moving target rots silently, which is precisely the gap
[[fidelity-to-a-source-and-fidelity-to-the-tree]] names: rule 11 of `vault-check.sh` proves a cited
path exists, never that the file still holds the claim.

**The sixteen artefacts under `docs/superpowers/` migrate** into the dated archive, in the same
wave as the pages citing `raw/`
([[archive-is-dated-by-session-and-holds-what-left-the-working-set]]). **Rejected: leaving them
where they are**, which preserves a mutable location that thirteen pages depend on.

**The long-run shape is that nothing moves at all** — the skill writes the artefact into its dated
folder from the start, since the date is known while it is being written. A move is the interim,
needed only until the skills are rewritten, and telling the spec-writing skill where to write is
the first intended use of the harness mechanism
([[the-harness-is-built-by-a-script-and-guarded-by-a-gate]]).

# A design document was written to a mutable `docs/` path and compiled from there — 2026-08-29

> [!NOTE] RAISED, NOT RESOLVED — this page and the ruling below sit under different `authority:` slugs
> **owner:** «Нужно сохранить его в docs/ для примера» — `docs/who-reads-the-vault.md`, the agent
> architecture written out as the worked example of a full proposal, saved at his instruction **and
> then compiled by the librarian**. This page says a spec or a plan is an artefact, frozen and cited
> rather than compiled, and that the long-run shape is the skill writing it into its dated folder from
> the start. **The document is at a mutable, undated path and it was compiled.** Both halves.

**And the document has already gone false where it stands.** Its `decided_by:` section widens the field
to `entities/` and `concepts/`; the owner ruled the opposite later the same session, so the file and
the artifact published from it are wrong as they stand. **Correcting them is owed and was not done**,
and the compilation carries the correction rather than the claim
([[who-reads-the-vault-and-who-writes-it]],
[[decided-by-is-legal-in-proposals-and-rules-and-required-in-rules]]).

**Which is the case this page makes, from the other end**: a mutable path cited by live pages goes
false without the citing pages knowing. **The measured cost it was written against was thirteen pages
citing a mutable `docs/` path**; this adds a fourteenth and it is one whose falsity is already known.

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
