---
title: "Generated text can lie about the mechanism that generates it"
type: lesson
status: archived
authority: generated-text-self-description
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md", "scripts/vault-catalogue.sh"]
tags: [harness, vault]
---

# The instance, 2026-08-17

`scripts/vault-catalogue.sh` prints a header above its list. After `catalogue.md` was deleted and
rule 9 retired ([[the-page-list-is-a-query-not-a-generated-file]]), **that header went on saying
*run `--write` to update it* and *rule 9 fails while it is stale* for a full run.** Both statements
had been false since the commit before.

**It was found by reading the output of a script whose behaviour had just changed. No check caught
it, and none could have.**

## Why generated text is the blind spot rather than the safe part

The reasoning that makes a generated artefact trustworthy is: *it is derived from its inputs, so it
cannot drift from them.* That is true of the **rows**. It is not true of the **prose the generator
prints around them**, which is a string literal in the script — hand-written, exactly as stale as
any comment, and wearing the authority of the machine that emitted it
([[docstrings-drift-inside-their-own-commit]] is the same defect one level down).

A reader trusts a generated header **more** than a document, because it came out of the tool. That
is what makes this worse than a stale `README`.

## The rule

**When a mechanism changes, read what it prints.** Not what it produces — what it *says about
itself*. The list was correct throughout; only the sentence explaining how to keep the list correct
was wrong.

The same asymmetry is why the gate guarantees agreement rather than truth
([[a-gate-guarantees-agreement-never-truth]]), and why a claim taken from prose rather than from
the file is a recorded failure class here ([[a-claim-asserted-from-prose-rather-than-from-the-file]]).
