---
title: "A block attributed to the owner is written in his own Russian, and a paraphrase is not signed"
type: rule
status: current
governs: [.claude/skills/handoff/SKILL.md, .claude/skills/ingest/SKILL.md]
render: region
basis: human
sprint: S2
created: 2026-08-22
sources: [".claude/skills/handoff/SKILL.md", ".claude/skills/ingest/SKILL.md", "scripts/vault-check.sh", "archive/2026-08-21/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md"]
decided_by: [[the-quote-is-cyrillic-rule-stands-as-an-advisory-and-stays-out-of-the-core]]
tags: [vault, process, harness]
---

# What travels

<!-- text -->
The owner's words enter a journal verbatim and in Russian. Where a session understood rather than
heard, it writes its own understanding in its own voice and does not sign it `owner:`.
<!-- /text -->

The decision behind it is [[the-quote-is-cyrillic-rule-stands-as-an-advisory-and-stays-out-of-the-core]],
taken by the owner on 2026-08-21; this page carries the text that decision obliges, and everything
below the line stays here ([[what-travels-from-a-rule-page-is-a-marked-slice]]). The design it was
built from is [[a-quote-is-cyrillic-rule-with-an-advisory-verdict]].

# It states its own exemption from the English rule, and the exemption is a mirror

**Everything written into this repository is English** — code, comments, documents, commit messages,
and the journals this rule is rendered into ([[english-in-the-repository-russian-with-the-owner]]).
**A quotation of the owner is exempt, and the exemption is not a softening of that rule.**

**It is the same clause read from the other side.** That rule already says an English technical term
keeps its own alphabet inside a Russian sentence — *"vault", not «ваулт»* — because an identifier is
the repository's own vocabulary and transliterating it makes it something else
([[english-terms-are-not-transliterated-into-cyrillic]]). **A quotation is the same kind of object:
its alphabet is part of what it is**, and rendering his Russian into English does not translate the
sentence, it replaces the speaker.

**So the two exemptions have one ground.** A word that is being *quoted* — an identifier quoted from
the code, a sentence quoted from the owner — keeps the alphabet it was said in. A word that is being
*written* is written in English.

# What the rule cannot do, and it is the larger half

**An alphabet separates a quotation from a paraphrase. It says nothing about whether a paraphrase is
faithful.** A session that writes a wrong English paraphrase in its own voice and does not sign it
has obeyed this rule completely, and the paraphrase can still be wrong.

**The forward-facing guard is the ratification step in `/retro`, not the verdict** — every attributed
line is put to the owner before `/handoff` routes it, which is before it can become a page
([[the-retro-ratifies-every-line-before-it-is-attributed-to-the-owner]]). Only he can separate a
faithful paraphrase from a wrong one, so the mechanical half was always the weaker one.

**And the verdict is an advisory rather than red, on his own counter-example**: a genuine English
quotation from him exists as a case, so a red verdict would fire on a correct page
([[the-quote-is-cyrillic-rule-stands-as-an-advisory-and-stays-out-of-the-core]],
[[the-filename-verdict-is-an-advisory-while-the-title-verdict-is-red]]).

# What it is worth, measured

**The chain this rule interrupts runs every session and has already cost a rule nobody gave.** The
owner speaks Russian, a session paraphrases him into English under the journal template's `owner:`
marker, the librarian compiles the paraphrase into a quote block stamped `basis: human`, and later
sessions reason from it as his word — with nothing ever showing him the paraphrase
([[a-paraphrase-signed-owner-becomes-a-quote-and-is-reasoned-from-as-his-word]]). One such page stood
for three days and decided three things.

**The convention costs nothing at the source, which is why it is a rule rather than a mechanism.**
The journal that found the defect had already written every attributed line in verbatim Russian and
everything it had merely understood in its own unsigned voice.

# Where it renders, and it is the first rule here to name two destinations

**`governs: [.claude/skills/handoff/SKILL.md, .claude/skills/ingest/SKILL.md]` under
`render: region`** — the two places an attributed line is written down. `/handoff` writes the journal
in which a line is first signed, and `/ingest` compiles that line into a page; a rule delivered to
one of them would leave the other free to do the thing the rule forbids.

**This is the first page in the corpus to use the inline-list form of the field**, which landed on
2026-08-21 partly for it ([[governs-takes-a-bare-path-or-an-inline-list-and-the-block-form-is-red]],
[[the-governs-list-is-expanded-at-the-walk-and-the-address-verdict-asks-membership]]). The block form
is refused, and refused loudly rather than silently, for the reason that applies here exactly: a
half-parsed list would render this text into one of these two files and leave the other reading as
drift.

**It carries no `authority:`, and that is required rather than chosen.** A rule answers with
`governs:`; the two fields on one page would make the decision and the rule stating it share a slug
and read as a duplicate ([[authority-beside-governs-is-forbidden-on-any-page]]).

# What is owed at the destination, and it is not the librarian's

**The page and its regions belong in one change, and this page arrived first.** The librarian writes
`wiki/`; marking the region in each skill file and running the injector are the session's. Until
that happens, `bash scripts/vault-inject.sh` reports that each skill carries no region for this page
and rule 12 is red — **the expected state of a half-finished landing, not a defect in this page**
([[a-region-is-a-paired-comment-named-for-a-rule]], [[a-check-asks-by-running-the-writer-it-checks]],
[[a-governed-file-with-no-region-is-an-advisory]]).

**Both markers are `<!-- rule: … -->`**, derived from the folder, and the injector writes the blank
line after the slice itself — it is not typed onto this page and must not be
([[the-marker-carries-the-records-type]], [[the-injector-writes-the-separator-inside-the-region]]).

**And the rendered slice is read against the file it lands in before the region is accepted**, which
is the check the gate cannot make: it guarantees that a region agrees with this page, never that it
belongs where it sits ([[a-gate-guarantees-agreement-never-truth]],
[[a-mechanisms-first-use-outside-its-home-is-where-it-drifts]]).

# Its verdict is built, and it is behind `--lint`

**Rule 14 of `bash scripts/vault-check.sh` prints one advisory line per owner-attributed block that
carries no Cyrillic**, behind `--lint` and not on a bare run
([[the-quote-is-cyrillic-rule-stands-as-an-advisory-and-stays-out-of-the-core]]). **The rule and its
verdict are not the same instrument**: this page reaches the session writing the line, and the
verdict reads the corpus afterwards.

# The regions landed the same day, and the section above is dated rather than corrected — 2026-08-22

**The section *What is owed at the destination* describes the state this page was written in, and it
lasted a few hours.** Both skills now carry a `<!-- rule: … -->` pair, the session marked them and
ran the injector, and `bash scripts/vault-inject.sh --check` reports **every rule agrees with the
region it governs**. `bash scripts/vault-check.sh` exits 0.

**What that section says is unchanged in its substance and is kept as written**: marking a region in
a destination is the session's and not the librarian's, and a rule page arriving before its region
is a half-finished landing rather than a defect
([[the-region-coverage-figure-is-dated-where-it-stands]]).

**Both regions were read against the file they landed in**, which is the check the gate cannot make:
in `/handoff` the slice sits under the paragraph about what a journal owes the owner's own words, and
in `/ingest` under the paragraph about compiling a paraphrase as testimony
([[a-gate-guarantees-agreement-never-truth]]).

**The harness coverage advisory moved in its numerator and not its denominator** — two files left
the *neither yet* list and the rest are unchanged. **No criterion is read off that**, which is the
owner's ([[the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count]],
[[a-sprint-closes-on-its-goal]]).
