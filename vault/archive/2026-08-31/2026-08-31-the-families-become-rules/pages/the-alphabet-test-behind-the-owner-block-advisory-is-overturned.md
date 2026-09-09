---
title: "The alphabet test behind the owner-block advisory is overturned, and the ratification step carries the weight"
type: decision
status: archived
authority: quote-language-verdict
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-25
created: 2026-08-25
supersedes: [[the-quote-is-cyrillic-rule-stands-as-an-advisory-and-stays-out-of-the-core]]
sources: ["archive/2026-08-25/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs/handoffs/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs.md", "scripts/vault-check.sh"]
tags: [vault, harness, process]
---

# The ruling, 2026-08-25

> **owner:** «мы когда-то заудмали ловить кириллицу как мои слова и теперь это вызвало ошибку.
> Предлгаю отменить это. Кириллица не означает, что слова мои.»

**The alphabet is not the discriminator and the verdict resting on it goes.** Rule 14 of
`scripts/vault-check.sh` finds an owner-attributed block carrying no Cyrillic byte and prints it
under `--lint`. That predicate is cancelled.

**What it superseded said the opposite**, and said it on the owner's own instruction of 2026-08-21:
the rule stands, its verdict is an advisory, it stays out of the core. The middle clause is what
falls here ([[the-quote-is-cyrillic-rule-stands-as-an-advisory-and-stays-out-of-the-core]]).

# What stands, and it is most of it

**The rule itself is untouched.** A block attributed to the owner is still written in his own
Russian ([[a-block-attributed-to-the-owner-is-written-in-his-own-russian]]). What is withdrawn is
the claim that an alphabet can tell whether he said it.

**What carries the weight instead is the ratification step in `/retro`**, which puts every
attributed line to him before it can become a page
([[the-retro-ratifies-every-line-before-it-is-attributed-to-the-owner]],
[[the-ratification-is-one-decision-over-a-shown-list-and-not-a-signature-per-block]]). That step is
a human instrument and it is the only one that ever separated a faithful paraphrase from a wrong
one ([[a-paraphrase-signed-owner-becomes-a-quote-and-is-reasoned-from-as-his-word]]).

# Rejected: replacing the predicate with a guillemet test

**Measured on the corpus the same day.** `wiki/` holds 122 owner-attributed blocks in two
spellings — 73 as `> **owner: text**` and 49 as `> **owner:** «text»` — and 47 carry guillemets
against 75 that do not. **Among the 75 are genuine quotations in the older spelling**, so a
guillemet predicate reddens correct pages exactly the way the alphabet one did.

**And in `log.md` the two predicates disagree in the other direction**: 32 records carry
`the owner said it`, of which 15 carry no guillemet quotation and all 15 are Cyrillic. The byte
test flags none of them. **The discriminator that would have worked there is the absent quotation,
not the alphabet** — and it is not built, and nothing here builds it.

# The order is forced, and cancelling first destroys the instrument

**Freeze the list, run the sweep, then overturn.** The advisory's output is today the only index of
which owner-attributed blocks the ratification of 2026-08-24 ranged over, and the sweep that
rewrites them destroys that index as it goes. **The list is frozen by page and claim, never by line
number**, since the same edit moves the lines
([[a-sweep-may-run-inside-a-session-when-the-list-is-assembled-in-advance-and-shown-whole]]).

**The sweep's acceptance becomes what was rewritten against what was frozen**, rather than an empty
advisory, because the advisory is going away.

# Nothing in the code changed on the day this was decided

**Rule 14 still runs and still prints.** The session that decided this wrote no script and edited no
rule page; the whole of it is a plan. **This page records a ruling and a sweep that has not been
run**, and the successor state of the tree is the next session's
([[the-plan-is-committed-and-the-execution-moves-to-a-session-of-its-own]]).

**One selftest case comes down with the rule and is not repaired here.**
`scripts/vault-check-selftest.sh:1758` grades with `run_lint_absent`, which requires the string
about owner-attributed blocks carrying no Cyrillic to **appear** — and it appears only because the
corpus holds English blocks. Zeroing the advisory makes that case report no and the suite report a
miss; **the repair is one line in the mutation and belongs in the same change**
([[a-case-green-before-its-mechanism-is-proved-by-removing-the-guard]]).

# The absent-quotation test was built over `log.md`, and it is a different population — 2026-08-26

**The section above ends *"it is not built, and nothing here builds it."* It is built now**, in
`.claude/hooks/catch-the-feedback.ps1` rather than in the gate
([[the-feedback-catcher-hook]]). The owner selected it against the plan's letter, which specified an
alphabet test ([[divergence-the-b3-note-was-built-against-the-plans-letter-and-reported-after]]).

**The two populations are not the same and the page's own measurement holds for the one it was taken
over.** Over `wiki/` the guillemet predicate reddens correct pages, because genuine quotations exist
in the older spelling — that finding stands and nothing built here touches `wiki/`. **Over
`log.md` the predicate is a strict superset of the alphabet one**: 1218 records, 125 `decision:`, 81
carrying `the owner said it`, 66 with a quotation, 15 without, **and all 15 Cyrillic**, so the
alphabet test fires on none of them and the quotation test catches all 15.

**It is scoped to `decision:` records deliberately.** The three no-Cyrillic records a naive test
would flag are one `ingest:` and two `measure:` records *about* the phrase — and the note's first
live firing was exactly that class, repaired by anchoring the match to the shape declaration at the
head of the record ([[a-guard-that-matches-a-phrase-anywhere-flags-the-record-that-discusses-it]]).

**Rule 14 is still live and the sweep is still unrun.** Nothing here retires it; the order recorded
above — freeze the list, run the sweep, then overturn — is untouched.
