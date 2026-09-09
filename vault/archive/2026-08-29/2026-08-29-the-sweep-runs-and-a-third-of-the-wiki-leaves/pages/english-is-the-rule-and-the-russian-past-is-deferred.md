---
title: "English is the rule for the whole repository; the product UI stays Russian, and what predates 2026-08-05 is deferred rather than exempt"
type: decision
status: archived
authority: language-scope
binding: prohibition
basis: human
sprint: S1
decided: 2026-08-15
created: 2026-08-15
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md", "CLAUDE.md"]
tags: [process, testing]
supersedes: [[the-language-rule-applies-only-to-new-work]]
---

# The rule has no exemption any more; it has a backlog

**English for everything written into the repository** — code, identifiers, docstrings, comments,
test names, `docs/`, commit messages, plans, specs, and any brief or report handed to a subagent.
**Unchanged**, and this is the part that was never in question.

**Russian for two things, and they are not the same kind of thing.** Chat with the owner, which is
conversation and leaves no artefact; and **what he sees while using the tool** — the web page and
the CLI output. The second is **product content, not documentation**, it stands on its own ground
permanently, and it is not a leftover of anything ([[statuses-stay-english-identifiers]] for the
one case that looks like an exception and is not).

## What changed on 2026-08-15

The rule used to carry a third clause: *it applies to new work, and everything written before
**2026-08-05** stays Russian*. **That clause is withdrawn as a standing rule.** The owner's words
for it, on 2026-08-15: all knowledge should be in English; he added the new-work boundary **because
he did not want to deal with the rest at the time**, and in that form it has gone stale.

**What predates 2026-08-05 is therefore not exempt. It is deferred.**

In practice, today, nothing changes: **nothing is mass-translated and no test is renamed now.**
What changes is what that sentence *is*. A boundary with a date says the old text is a different
country and invites nobody to ask about it. A deferral says the work is owed, has a size, and is
waiting on a decision — and the size is measured: **10,947 lines across 107 files**, in four buckets
that need four different answers ([[migrating-the-repository-to-english]]).

**Rejected: a translation pass, now.** The reasons the earlier page gave are unchanged and are
still the reasons — renaming 263 tests produces a diff nobody can review and breaks every reference
in the older plans, which are records and will not be rewritten to match.

**Also rejected: keeping the exemption as a rule**, which is what this page supersedes. Its
practical effect and this one's are identical this afternoon; they differ in what the next session
is allowed to assume.

## What it obliges

- **When you substantially rewrite an existing docstring or comment for other reasons, write the
  new text in English.** Unchanged, and it is the only clause of the old boundary that was ever an
  instruction rather than a permission.
- **Do not translate the templates.** They are the product, and they are not part of the deferral
  at all.
- **A bucket taken out of the backlog is a decision with a date**, and it supersedes this page for
  that bucket rather than quietly widening it.

## Why this page exists, and what it says about `elsewhere:` verdicts

The rule had no page of its own until 2026-08-14, and for one day it had no home anywhere. When the
2026-08-12 handoff was migrated, the unit carrying it was given the verdict `elsewhere:CLAUDE.md —
the language rule, and the ban on mass-translating what predates it`. Then, on 2026-08-14,
`CLAUDE.md` was cut to a map and four rules ([[claude-md-is-a-map-and-four-rules]]), the paragraph
went with the rest of the language section, and nothing anywhere held it — found by reading every
removed block against the page that was meant to carry it.

**The correction, made by the owner on 2026-08-15: the paragraph was not lost. He deleted it
deliberately**, and said so. That changes what the `elsewhere:` verdict means without making it
wrong:

- **The verdict was correct when it was written.** It named the file that held the rule, and that
  file did hold it.
- **The disappearance was a decision, not an accident** — which is not what the ingest of
  2026-08-14 concluded, and it is worth having the two readings side by side, because the sprint's
  fourth acceptance criterion rests on the shrinking-`CLAUDE.md` problem and one of its two
  instances is this one. Whether that changes the criterion is the owner's call, not this page's.
- **The general form still stands** and is on [[the-verdict-is-the-write]]: an `elsewhere:` verdict
  is a claim about a file **the vault does not own**, and nothing re-checks it when that file
  changes. A deliberate deletion and an accidental one leave the same hole in the store; the
  difference is only in whom to ask about it.

## The restated English list carries `plans`, and that word was struck on 2026-08-22

**The first line of this page restates the rule's English list, `plans` included. The word left the
rule that day** and this restatement is dated rather than rewritten
([[the-plan-the-owner-reads-to-approve-it-is-written-in-russian]],
[[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).

**What this page says about the rule's shape is unaffected.** The strike is not an exemption of the
kind this page withdrew in 2026-08-15: the plan the owner reads in order to approve it lives outside
the repository, so the rule's own opening clause — *everything written into the repository* — never
reached it, and only the bare word in the list did. **A rule made consistent with its own predicate
is not a rule weakened**, and no plan inside the tree lost its cover: `docs/` and a subagent brief
are each named by other items of the same list.

**It is also the shape this page prescribes.** *"A bucket taken out of the backlog is a decision with
a date, and it supersedes this page for that bucket rather than quietly widening it"* — the same
discipline applied to a carve-out rather than to a translation bucket, which is why the ruling is its
own dated page under `authority: approval-plan-language` instead of an unsigned edit here.
