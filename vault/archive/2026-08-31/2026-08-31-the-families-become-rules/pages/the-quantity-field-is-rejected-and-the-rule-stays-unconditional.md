---
title: "The `quantity:` field is rejected, the rule stays unconditional, and the corpus is cleaned before the check is tightened"
type: decision
status: archived
authority: quantity-field
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-18
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls/handoffs/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls.md", "scripts/vault-check.sh"]
tags: [vault, record-schema, harness]
---

# The ruling, 2026-08-18

> **owner: the rule is unconditional. No digits in a title, none in a filename. The `quantity:`
> field is rejected, and this question is closed permanently. The librarian checks everything
> standing in the rule's way and rewrites it; then the librarian renames the files.**

The rule itself is unchanged and is [[a-title-names-what-is-counted-instead-of-counting-it]],
extended to the address by [[the-title-rule-extends-to-filenames]]. What is decided here is that
the **escape hatch** attached to it — a free-text line saying why the number is not a count — is
withdrawn, and that the question is not reopened.

**Rejected, and named: give the field a decision page and keep it.** Refused because the owner had
already ruled the rule unconditional twice, `basis: human`, and had refused two specific exception
classes on the way — counts bound to a date, and design invariants where the count is the claim.
**Both of those classes are alive in `quantity:` values today**, which is the whole finding: the
field readmitted, one page at a time and judged by nobody, exactly what the rule had refused in
general ([[the-turn-that-explains-a-rule-adds-exceptions-to-it]]).

# What it obliges, in order, and the order is a dependency

1. **A decision page** — this one.
2. **The corpus**: strip `quantity:` from the pages carrying it and retitle each one the field was
   answering for. Twenty-four pages carry the field, counted at `c521a10` with
   `grep -c "^quantity:" wiki/*/*.md`. Every one of them is a judgement rather than a sweep — the
   line says why the number was thought not to be a count, and the retitle has to name what is
   counted instead ([[a-title-names-what-is-counted-instead-of-counting-it]]).
3. **The filenames**: rename the counting slugs, rewrite the inbound links, and close the `log.md`
   hole while doing it ([[log-md-is-outside-the-link-set-the-check-reads]],
   [[a-page-rename-is-sed-and-verify]]).
4. **The store's schema**: the `### quantity` section of the vault's own `CLAUDE.md` goes. It is not
   the librarian's file to write, so it is a work item and it is named as one.
5. **Only then the check**: remove the `answered` branch from both halves of rule 10 and retire the
   two selftest cases that exercise the escape hatch, `title_declared` and `filename_declared`.

**Tightening the check first reddens twenty-four pages at once**, because they are silent today only
because the field answers for them. A gate that is red on a corpus nobody can legally fix in one
session is the failure this project has already priced once
([[the-filename-verdict-is-an-advisory-while-the-title-verdict-is-red]]).

# The state this leaves behind, which is not a decision

**The field still stands on twenty-four pages and the check still reads it.** That is a measurement
of the tree, not a rule anyone may lean on: a page written after this date does not answer with a
declaration, it takes a title with no count in it.

**Rule 10's `answered` flag returns before the slug is evaluated**, so one `quantity:` line silences
the title half and the filename half together. Seven filenames are exempt on it today, and six print
in the advisory ([[the-title-check-asks-and-the-answer-is-a-retitle]]).

**How the field arrived without a decision at all** is a lesson rather than a decision, and it is
[[a-field-admitted-around-the-admission-procedure-outlives-the-rule-it-softens]].

# All five steps are executed, read on 2026-08-19

**The dependency held and nothing was reddened by it.** Step by step, in the order this page fixed:
the decision page is this one; **the corpus was stripped and retitled on 2026-08-18** — twenty-four
pages carried the field and twenty-seven titles were repaired; **the sixteen counting addresses were
renamed on 2026-08-19** ([[a-page-rename-is-sed-and-verify]]); **the store's schema lost the
field's section** and gained the sentence that there is no way for a page to declare itself exempt,
written by the owner's own session because that file is not the librarian's; and **only then the
check was tightened** — the short-circuit, the reader and the offer of the field in the note's
message are gone from rule 10.

**The state recorded above has inverted, and both readings stand.** *"The field still stands on
twenty-four pages and the check still reads it"* was a measurement of the tree on 2026-08-18. Today
`grep -rc '^quantity:' wiki archive` sums to 0, and `bash scripts/vault-check.sh` exits 0 with
nineteen advisories, no title verdict and an empty filename advisory. *"Rule 10's `answered` flag
returns before the slug is evaluated"* describes a branch that no longer exists; *"seven filenames
are exempt on it today, and six print"* describes a corpus that no longer exists either.

**One thing the tightening did not do, and it is filed rather than built.** The check reads no
whitelist of frontmatter keys, so **an unrecognised key is invisible to every rule** and nothing
mechanical stops `quantity:` from being written again. It would be inert — no verdict reads it — but
the rejection now lives only in this page, in the schema's prose and in a comment, which is the
shape this project has been burned by before ([[knowing-a-rule-is-not-a-mechanism]]). Recorded as a
finding on the owner's instruction, with nothing built for it.

**And the predicate the field used to answer for has been widened since.** Ordinals count, `first`
does not, and — because the appeal this page withdrew is what made a lenient list affordable —
**every word in the list is now a promise that the word is always a count**
([[ordinals-count-and-first-does-not]]). That page extends the rule's reach; it does not supersede
this one, and the two meet only at that sentence.
