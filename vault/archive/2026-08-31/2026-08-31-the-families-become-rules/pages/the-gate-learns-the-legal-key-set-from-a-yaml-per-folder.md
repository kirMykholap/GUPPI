---
title: "The gate learns the legal frontmatter keys from a yaml per folder, rather than from a list inside itself"
type: decision
status: archived
authority: frontmatter-key-set-gate
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-19
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys/handoffs/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys.md", "scripts/vault-check.sh", "job_hunt_ai_vault/wiki/decisions/_schema.yaml"]
tags: [record-schema, harness, vault]
---

# Decided by the owner on 2026-08-19

> **owner: the gate learns the set of legal frontmatter keys, from a yaml per folder.**

Until that night `vault-check.sh` had **no verdict over the set of frontmatter keys at all**. Rule 2
asked what named fields answer for; a key nobody had named was invisible to every rule there is. The
artefact is [[the-per-folder-frontmatter-schema]].

# What was rejected, and the rejections are the argument

**Rejected: a targeted verdict per prose-only rule.** That was the queue as it stood — one owed
verdict for `authority:` beside `governs:`, another for a returning `quantity:` — each with its own
selftest case, each written for one field. **One general mechanism closed three holes, and nobody
had listed the third.** The finding that produced it is worth carrying forward on its own:
*the next "this rule has no mechanism" finding is worth checking against the general gate before a
verdict is written for it.*

**Rejected: a key list inside `vault-check.sh`.** The store's schema already states the core, so a
list in the script would be a second copy of one set. This project does not argue that hypothetically:
rule 11 exists because two lists drift, and **two selftest cases have already been lost to exactly
that**. The yaml is read; nothing restates it.

**Rejected: a permissive default for a folder with no schema.** A missing file means *the check
cannot judge these pages* and it is red, not silent — because the failure to design around is the one
that passes.

# The principle the files were built on, and it is the owner's

> **owner: the schema files encode what is decided, not what is observed.**

**`basis` is carried by 321 of 321 pages and is `optional:` on all six.** A field carried by
everything is not thereby required — *that reasoning is how `quantity:` entered the store*, around
the admission procedure, and it took a day to remove
([[a-field-admitted-around-the-admission-procedure-outlives-the-rule-it-softens]],
[[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]). A field moves from `optional`
to `required` when a decision says so, and the schema names the page that decision is written on.

# The `basis` question is open and is the owner's, and one line settles it

Three sources disagreed on which fields are required, measured 2026-08-19:

| source | what it said |
|---|---|
| `vault-check.sh`, before this change | six, hardcoded — `title type status created sources tags` |
| [[the-frontmatter-core-is-fixed-and-updated-joins-it]] | seven, adding `sprint` |
| the corpus | `basis` on **321 of 321** pages, and named on that same decision page as *"the only field conflict resolution rests on"* |

The schemas encode the decided seven and leave `basis` optional. **The omission looks like an
oversight rather than a decision**, and it is recorded rather than assumed: either `basis` belongs in
the core and the decision page should say so, or it is genuinely optional and every page carries it
out of habit. **It is one line either way, and the schema files can change in the same minute the
ruling lands.**

# What it obliged

The hardcoded six left rule 2. The three verdicts and their messages are on
[[the-per-folder-frontmatter-schema]]; their selftest cases were each proved against the pre-change
script, which is what makes them evidence ([[a-case-that-passes-before-the-change-tests-nothing]]).

**This is the field half of S2's first acceptance criterion and not the whole of it.** The wide
reading — what a record of each type *asserts* and what *expires* it — is deferred
([[the-wide-half-of-the-per-type-schema-is-a-conversation-not-a-task]],
[[a-schema-per-type-says-what-a-record-asserts]]). **No criterion is read off here**; that is the
owner's ([[a-sprint-closes-on-its-goal]]).

**The price was quoted wrong when he agreed to it** — "one verdict, one selftest case", re-priced in
two readings before any code was written ([[a-claim-that-runs-ahead-of-its-measurement-is-corrected-in-the-same-session]]).
