---
title: "The type words are swept off the tree as `singular:plural` pairs and listed nowhere"
type: decision
status: archived
authority: type-word-source
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-18
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind/handoffs/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind.md", "scripts/vault-check.sh", "scripts/vault-inject.sh"]
tags: [harness, record-schema, vault]
---

# Decided 2026-08-18: derive it, do not write it down

**The folder set already exists in four places and was forgotten in one of them within a day.** A
fifth copy — a literal list of the six type words inside the check — would have been a fifth thing
to keep in step, and this corpus has measured what a copied list does
([[a-copied-list-drifts-and-a-sweep-cannot]],
[[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).

**So the words are swept off `wiki/` as `singular:plural` pairs** and passed into both `awk`
programs, replacing the inline `sub(/s$/)` derivation rule 2 used to do for itself. **A marker's
type is legal because its folder exists**, which rule 1 already checks — so legality is a
consequence of an existing rule rather than a new list to maintain.

## The correspondence is derived in one place per script, and never twice

`entities` → `entitie` is the one case a naive `s$` strip gets wrong, and the check already carried
that special case at `scripts/vault-check.sh:176` before any of this. **That one line is the whole
of the mapping**, read forwards to make a marker's word and backwards to resolve it to a folder — a
fact the retired design missed when it priced the singular spelling as needing *"a pluralisation
the check does not currently do anywhere"* ([[a-proposal-misprices-by-overcharging-one-row-and-undercharging-another]]).

**A second place computing the folder from the word would be a second answer waiting to differ**,
which is the argument the marker's address rests on
([[a-marker-with-its-type-is-a-complete-address]],
[[the-mapping-is-documented-at-each-hop-and-copied-nowhere]]).

## What this does not soften

**The judge is still strict.** Detection takes anything shaped like a marker, including a
capitalised or unknown word, and only then asks whether the word names a folder this vault has. An
unknown one is **malformed**, by name and by line — never *a marker for a type nobody has heard of*
([[a-marker-is-detected-loosely-and-judged-strictly]]). Deriving the legal set from the tree widens
what is legal; it does not widen what passes.
