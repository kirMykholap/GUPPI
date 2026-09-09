---
title: "English for everything written into the repository; Russian for chat and for what the owner sees in the tool"
type: rule
status: current
governs: CLAUDE.md
render: region
basis: human
sprint: S2
created: 2026-08-17
sources: ["CLAUDE.md", "[[english-is-the-rule-and-the-russian-past-is-deferred]]", "[[statuses-stay-english-identifiers]]", "[[claude-md-is-a-map-and-four-rules]]"]
decided_by: [[english-is-the-rule-and-the-russian-past-is-deferred]]
tags: [harness, process, web]
---

# What travels

<!-- text -->
**English for everything written into the repository**: code, identifiers, docstrings,
comments, test names, documents under `docs/`, commit messages, specs, and any
brief or report handed to a subagent.

**Russian only for chat with the owner** — and for what the owner sees while using the  
tool: the web page and CLI output are product content, not documentation, and stay in  
Russian. Status values remain English identifiers (`new`, `applied`, …).
**And the plan the owner reads in order to approve it is Russian**: it is written for him, and it
lives outside the repository.

**English technical terms are not transliterated into Cyrillic**: "vault", not «ваулт»;
"proposal", not «пропозал». They are the repository’s own vocabulary, and an identifier keeps
its own alphabet inside a Russian sentence.
<!-- /text -->

**That is the body of the repository's `## Language` section, to the byte.** The heading itself
stays outside the region, as prose the file owns; a region carries a rule's text and not the
furniture around it ([[marked-regions-and-the-prose-outside-them]]). Verified the way the rest of
this migration was: the lines were cut out of `CLAUDE.md` at `e478c19` by number and diffed against
the slice above rather than read against it. The diff is empty.

**The trailing double spaces at the end of the Russian paragraph's first and second lines are
content.** They are markdown hard breaks, they are what makes that paragraph render as three lines
rather than one, and the injector compares byte for byte — so an editor that trims trailing
whitespace on save turns this rule red on the next `vault-check.sh`, on a change nobody typed. It is
the one rule of this file whose text is not whitespace-indifferent, and that is worth knowing before
it is diagnosed as a bug in the injector.

Everything below this line stays on this page
([[what-travels-from-a-rule-page-is-a-marked-slice]]).

# Why it moved as one slice and not as one region per paragraph

**This section has already lost a paragraph to an edit of this file.** The cut of 2026-08-14 that
turned `CLAUDE.md` into a map dropped the language section's clause about what predates 2026-08-05,
and nothing in the vault held it for a day ([[claude-md-is-a-map-and-four-rules]]). The clause was
deliberately deleted rather than mislaid — the owner said so on 2026-08-15 while withdrawing it
([[english-is-the-rule-and-the-russian-past-is-deferred]]) — but the store was homeless either way,
and it was found by reading the removed text beside the page meant to carry it, not by any check.

A region is rewritten **whole** by the injector. With the section as one slice, a paragraph cannot
fall out of the file without this page changing first, and rule 12 says so by running the renderer.
With one region per paragraph, deleting a region and its page together is still a one-keystroke
operation and still leaves the remaining regions green.

# Why it cannot wait for a question

**Language is chosen at the first keystroke of every artefact, and asked afterwards the artefact is
already written.** There is no cheap moment to apply this rule late: a docstring, a test name or a
commit message in the wrong language is fixed by rewriting it, and the cost scales with how long
nobody asked. That is the admission test for the rules that reach this file, word for word
([[claude-md-is-a-map-and-four-rules]]).

**The clause about subagents is the one that earns the delivery.** The rule names *any brief or
report handed to a subagent* because that is where the language leaks: a subagent writes in whatever
language its brief arrived in, it has no way to ask, and in this project every task is reviewed by
one. A rule the reviewer has to find by searching is a rule the reviewer does not have.

# The clause that looks like an exception and is not

`new`, `applied`, `call` surface inside a Russian interface and stay English
([[statuses-stay-english-identifiers]]). **They are identifiers, not copy** — stored, compared and
queried — so they belong to the first sentence of this rule even though they are visible in the
second. The rule's own last line says it, and that is why it is inside the slice: a reader who meets
the Russian-interface sentence without it will localise the values.

The general boundary is the same one: **the web page and the CLI output are product content, and
product content is not documentation.** It stands on its own ground permanently and is not a
leftover of anything.

# What this rule deliberately does not carry

The rule is the instruction. Everything that makes it arguable is on
[[english-is-the-rule-and-the-russian-past-is-deferred]] under `authority: language-scope`:

- that what predates 2026-08-05 is **deferred rather than exempt**, and the withdrawn clause that
  used to say otherwise;
- the size of that deferral — 10,947 lines across 107 files, in four buckets needing four different
  answers ([[migrating-the-repository-to-english]]);
- the standing obligations that are not in the rule's text: a substantially rewritten docstring or
  comment is rewritten **in English**, the templates are not translated at all, and a bucket taken
  out of the backlog is a dated decision that supersedes that page for the bucket rather than
  quietly widening it.

**None of that belongs in a rendered rule.** A rule carrying a measured number would put a figure
into a file nothing greps, which is how the count of boundary tests drifted here before
([[a-stated-count-drifts-from-the-list-it-heads]]).

# Why no test holds it

`ruff` does not read natural language and no linter here distinguishes a Russian identifier from an
English one. The nearest mechanical thing this project has is a grep for Cyrillic, and it would fire
on every template, every CLI string and every alias in `tags.md` — all of them correct. **The rule's
boundary is between product content and documentation, and that is a judgement about what a string
is for**, which is exactly the class the `rules` folder exists for
([[rules-becomes-a-type-of-its-own]]).

# Where it renders

`governs: CLAUDE.md` — a path from the repository root, resolved against nothing else
([[governs-is-a-path-from-the-repository-root]]). The text lands in a paired comment named for this
page's slug ([[a-region-is-a-paired-comment-named-for-a-rule]]), in a file on its way to being a
dispatch table ([[the-repository-claude-md-becomes-a-dispatch-table]]).

**The page and its region belong in one change, and this page arrived first.** The librarian writes
`wiki/`; marking the region and running the injector are the session's. Until then rule 12 reports
this rule as governing a file that carries no region for it, which is the expected red and not a
defect ([[a-governed-file-with-no-region-is-an-advisory]]). If the rule is ever replaced, the
successor renders and this page does not ([[a-deprecated-rule-does-not-render]]).

# The instruction and the decision are different pages

[[english-is-the-rule-and-the-russian-past-is-deferred]] answers `authority: language-scope`. This
page carries only the instruction and carries `governs:` in place of an `authority:`, so the pair
does not read as two answers to one question ([[rules-becomes-a-type-of-its-own]]).

# One more instruction about the Russian half, and it is not in the slice

**English technical terms are not transliterated into Cyrillic in chat**: "vault", not «ваулт»;
"proposal", not «пропозал» ([[english-terms-are-not-transliterated-into-cyrillic]], owner,
2026-08-18).

**It is not in the region above and nothing has been rendered from it.** Whether it joins the slice
is the owner's call: it would change what every session reads, and adding text to a rendered rule
is a decision about that file rather than a correction to this page. Raised in the brief.

**It belongs to the same boundary the rule already draws** — an identifier keeps its own alphabet
inside a Russian sentence, which is the reasoning that keeps `new` and `applied` English inside a
Russian interface ([[statuses-stay-english-identifiers]]).

## The owner answered, and the sentence is now inside the slice — 2026-08-18

> **owner: the register instruction joins the language rule's slice.** It is about how to write, and
> the language rule is the only place that is read.

**So the section above, which says it is not in the region and that whether it joins is the owner's
call, is answered rather than wrong** — it is kept because it records the question and the reason it
had to be asked: adding text to a rendered rule changes what every session reads.

**What travels is the instruction only.** The reasoning — why a transliterated term defeats both
retrieval and the alias list — stays on
[[english-terms-are-not-transliterated-into-cyrillic]], which is the decision this sentence
renders, and none of it enters the slice
([[what-travels-from-a-rule-page-is-a-marked-slice]]).

**It is one rule, not two.** The slice is the boundary between what is written where, and the
register clause is the same boundary applied inside the Russian half — the identifier keeps its own
alphabet, exactly as `new` and `applied` do inside a Russian interface
([[statuses-stay-english-identifiers]], [[a-rule-ships-one-piece-of-text-or-it-is-more-than-one-rule]]).

# The slice changed on 2026-08-22: `plans` is struck, and the plan the owner approves is named on the Russian side

**The owner ruled that the plan he reads in order to approve it is written in Russian**
([[the-plan-the-owner-reads-to-approve-it-is-written-in-russian]]). Two edits to the slice, and they
are one change:

- the word **`plans`** leaves the English list;
- **one clause joins the Russian paragraph**, naming the plan he reads in order to approve it.

**The section above says the slice is the `## Language` body at `e478c19` *to the byte*, and that
sentence is dated rather than struck.** It records a verification that was performed and was true;
what is true from today is that the slice and that file's section have both moved, together, because
the injector rewrites the region from this page ([[a-check-asks-by-running-the-writer-it-checks]],
[[the-region-coverage-figure-is-dated-where-it-stands]]).

**The trailing double spaces on the Russian paragraph's first two lines were left untouched**, which
is the hazard the section above names about this page and the one edit here had to be careful of. The
new clause is a plain line with no trailing whitespace and it joins the same paragraph, so the two
hard breaks are exactly where they were ([[a-rule-ships-one-piece-of-text-or-it-is-more-than-one-rule]]
for why they are content and not formatting).

# Why striking the word makes the rule consistent rather than weaker

**The rule's own opening clause is *everything written into the repository*, and the plan the owner
approves was never in the repository.** It lives in `C:\Users\kir\.claude\plans\`. So the general
clause never reached it and only the bare word `plans` in the list did — the list was wider than the
sentence that heads it, which is a rule disagreeing with itself rather than a rule with an exception.

**No plan inside the repository loses its cover, and nothing has to be remembered for that.** They
are already named by other items of the same list: a plan under `docs/` by *documents under `docs/`*,
and a plan under `.superpowers/sdd/plan-a/` by *any brief or report handed to a subagent*, which is
what such a plan is. **So the strike adds no exception**, which is the property the repair was
chosen for: the rule
gets shorter and covers exactly what it always meant to cover.

**Rejected: splitting by audience and location** — an approval plan in Russian, a committed plan in
English. More precise, and it replaces one struck word with two properties a writer must hold at
once. The decision page carries the full reasoning and the date
([[the-plan-the-owner-reads-to-approve-it-is-written-in-russian]]).

# One other page restates the struck word and is corrected on its own

[[english-is-the-rule-and-the-russian-past-is-deferred]] opens by restating the English list,
`plans` included. It carries `authority: language-scope` and holds everything that makes this rule
arguable, so the restatement is corrected there, dated, rather than here.
