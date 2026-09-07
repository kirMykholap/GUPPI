---
title: "`authority:` uniqueness becomes a question asked within a type, and a shared slug becomes the route between kinds"
type: decision
status: current
authority: authority-per-type-uniqueness
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: action
target: the-vault-claude-md-states-authority-uniqueness-within-a-type
sources: ["archive/2026-08-30/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md", "scripts/vault-check.sh", "job_hunt_ai_vault/CLAUDE.md"]
tags: [vault, record-schema, retrieval]
---

# Context

**`authority:` names the question a page is the sole answer to, and rule 3 of `vault-check.sh`
reddened any two `current` pages carrying the same slug.** That comparison was corpus-wide and blind
to type.

**It was also why `authority:` was forbidden in `wiki/rules/`**: a rule carrying a slug would share it
with the decision stating it, and the pair would read as a contradiction
([[authority-beside-governs-is-forbidden-on-any-page]]).

**Files this touches:** `scripts/vault-check.sh`, `job_hunt_ai_vault/wiki/rules/_schema.yaml`,
`job_hunt_ai_vault/CLAUDE.md`, `.claude/skills/vault-ask/SKILL.md`.

# The question

**Is a slug unique across the whole store, or unique within a type?**

# How it works after

**Rule 3 compares slugs within a type.** Two pages of the same type sharing a slug are a
contradiction, marked on both and chosen between by nobody. **Two pages of different types sharing a
slug are legal and expected**, and that is the route a reader walks: proposal → decision →
concept or entity → rule.

**Built as `permitted`. The `required` half is deferred** — twenty-two families hold concepts with no
entity, 54 pages, so requiring the pair now reddens them on the first run
([[the-required-half-of-paired-authority-waits-on-the-taxonomy]]).

**`authority:` became legal in `wiki/rules/` in the same change**, optional there and never required,
because a rule delivered by injection answers with `governs:` and one delivered by lookup answers with
a slug ([[a-rule-under-render-authority-is-written-into-no-file-and-found-by-its-slug]]).

**What it costs, named at the time:** the gate can no longer see a decision and a concept disagreeing
under one slug. **What looks for that now is the `contradicts` verdict of [[the-decisions-agent]]**,
by reading rather than by matching — a weaker instrument over a wider field, and the standing reason a
reader is dispatched at every ingest
([[a-slug-shared-across-types-is-the-graph-the-links-field-would-have-cached]]).

**Measured on the day it landed: zero slugs are shared across types anywhere in `wiki/`.** The
permission has no subject yet and nothing regressed; the first pages to use it are written from here
on.

**The target this decision is discharged by is a text edit the librarian may not make.**
`job_hunt_ai_vault/CLAUDE.md:199-200` still says *"Two `current` pages carrying the same value are a
contradiction"* and `:347` still says *"If two `current` pages claim the same `authority`, mark
both"*, neither qualified by type. Both are now false as they stand, and that file is what the gate
reads as its own input, so it is the session's to write
([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]).

# Recommendation

**Take the narrowing.** The old comparison bought one thing — a cross-type disagreement caught by
string equality — and it cost the only cheap way to walk from a question to every kind of page that
answers it. A reading verdict for the first is a real instrument; nothing else offered the second.

**Rejected: leaving uniqueness corpus-wide** and reaching the chain through `[[wikilinks]]` alone,
which is what the refused `Links:` field was for and which no reader ever got.

# Ratification

**owner, 2026-08-30:** «а что если мы расширим это до правила "две страницы одинакового типа не могут
нести один и тот же authority. А ращные - могут и даже должны, так как они перенимают его". То есть в
будущем мы будем создавать entities и concepts из proposal. Если разрешить им иметь один authority -
это упростит поиск и покажет близость этих страниц.»

**The session agreed with two reservations and both were taken**: the pair requirement waits until
`concepts/` and `entities/` have been sorted, and cross-type disagreement is handed to the reading
verdict rather than left unwatched.

# It disagrees with the taxonomy ruled the same day

> [!NOTE] RAISED, NOT RESOLVED — the `authority:` slugs differ, so rule 3 cannot see this and no
> `CONTRADICTION` block is legal for it.

**[[concepts-are-non-functional-requirements-and-entities-are-functional]]**
(`concepts-entities-taxonomy`) says a shared slug is permitted and required **only** in the
concept/entity pair. **This page says any two pages of different types may and should share one**, and
its own *How it works after* names the proposal → decision → concept → rule chain as the point.

**Both are the owner's words on the same day and neither outranks the other.** They may be
reconcilable — *required* only in that pair, *permitted* everywhere — but that reading is the
librarian's inference and is not what either sentence says. **The librarian marks both and chooses
neither.**

**The marker's counterparty left `wiki/` on 2026-08-31 and the disagreement is now one-sided.**
[[concepts-are-non-functional-requirements-and-entities-are-functional]] moved into
`archive/2026-08-31/2026-08-31-the-families-become-rules/pages/` with the cleanup's sweep. **That is not
a ruling and must not be read as one**: the marker stands, the taxonomy claim it named now has no live
carrier, and nobody chose. It is raised in the brief as a marker whose other side has gone quiet.

# The permission has a subject now, and the number measured on the day it landed is false — 2026-08-31

**"Measured on the day it landed: zero slugs are shared across types anywhere in `wiki/`."** That was
the reading on 2026-08-30 and it is wrong from the next day. **Fourteen of the nineteen rule pages
written on 2026-08-31 carry a slug a live `concepts/` or `entities/` page also carries**, which is the
first real use of the permission and is what makes the lookup delivery reach anything at all. The
sentence is corrected here and left standing above, because a number in prose goes false without saying
so and deleting it hides that it was ever taken.

**The chain named in *How it works after* is now the ratified target state rather than a possibility.**
One slug carried along decision → proposal or rule → concept or entity, propagating, **converged by
hand** and not by any mechanism — the owner's ruling of 2026-08-31, with rule 3's refusal named as the
point rather than as an obstacle ([[the-slug-converges-by-hand-along-the-chain-of-types]]).

**The target this decision declared is discharged.** `target:` names
`the-vault-claude-md-states-authority-uniqueness-within-a-type`, and `job_hunt_ai_vault/CLAUDE.md` now
reads *"The question a page is the **sole** answer to **within its own type**"* at its `authority:`
section and *"If two `current` pages **of the same type** claim the same `authority:`"* at its
contradictions section. The session wrote it, which is whose it was
([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]). **No mark is set here** — whether
that discharges the page is `scripts/vault-archive.sh`'s to decide, in one pass
([[the-archiver-marks-and-moves-a-decision-in-one-pass]]).

*(Added at the ingest of `raw/handoffs/2026-08-31-the-families-become-rules.md`.)*

*(Compiled from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
