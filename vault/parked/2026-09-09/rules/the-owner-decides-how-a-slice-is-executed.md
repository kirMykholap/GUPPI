---
title: "The owner decides how a slice is executed, and that decision overrides any skill"
type: rule
status: current
governs: CLAUDE.md
render: region
basis: human
sprint: S2
created: 2026-08-17
sources: ["CLAUDE.md", "archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md", "[[how-a-slice-is-executed]]"]
decided_by: [[how-a-slice-is-executed]]
tags: [harness, process, agents]
---

# What travels

<!-- text -->
**How a slice is executed is the owner's decision, and it overrides any skill that says
otherwise.** Ask the vault before you start one; the skills will confidently tell you a
different thing.
<!-- /text -->

**That is the text the repository's `CLAUDE.md` has carried since the cut of 2026-08-14, to the
word.** The migration changed its form and nothing else: it was the fourth item of a numbered list
and is now three unindented lines, because a region is rendered into a file rather than typed into
one, and a list position is a property of the file it happens to sit in. **Rewording a rule while
moving it would be a change nobody decided**, and it would be invisible in the diff of a migration
that is supposed to be a move.

Everything below this line stays on this page. That is the whole mechanism: what ships is what the
mark encloses, and the argument, the links and the history reach nothing
([[what-travels-from-a-rule-page-is-a-marked-slice]]).

# Why it cannot wait for a question

The admission test for the rules that stayed in the repository's `CLAUDE.md` is a single
sentence: **obeying them late is the same as not obeying them at all**
([[claude-md-is-a-map-and-four-rules]]). Of the four, this one is the sharpest, and it fails
differently from the others.

The other three are rules you might break in ignorance. **This one another document will actively
argue you out of.** `superpowers:subagent-driven-development` describes implementer subagents as
the way a slice is run, and it is not wrong about itself — it states a default. This project
measured that default and refused it: slice 3 cost a session of eight to ten hours, and the
recalibration cut *round trips around checking* while refusing every proposal that cut *checking*
([[how-a-slice-is-executed]], [[agent-round-trip-cost]]).

So a reader who has only the skill never forms the question. There is no moment at which they
wonder whether to ask the vault, because nothing they have read looks uncertain. A rule with that
failure mode has to **arrive before the work** rather than be found by searching, which is exactly
the property the injector preserves and the reason this text is delivered instead of cited.

# Why no test can ever hold it

The admission test for the folder is the same shape one level down: **a paragraph becomes a rule
page if it is imperative and not enforced by a test, and where a test holds the rule, the test is
the rule** ([[rules-becomes-a-type-of-its-own]]). This rule is the one of the four that no test can
ever take over, and that is why the owner sent it first.

- the test-database rule is already half-held by the fixture that builds and drops the schema
  ([[the-test-database-is-built-and-truncated-by-its-fixtures]]);
- the boundary rule *is* a statement about tests, and the AST tests are its enforcement
  ([[architectural-boundaries]]);
- the JavaScript rule has an owed test with an exact shape ([[javascript-policy]]).

**This one is about the conduct of a session, and a session leaves no artefact a test can read.**
Whether the code was written in the main session or by an implementer subagent, whether a fix was
re-reviewed, whether the browser walk happened inside an agent's turn — none of it is in the tree
afterwards. A check could at best confirm that some document still says the words, and what that is
worth is on the record: seven harness divergences, none caught by anything mechanical
([[no-rule-reads-a-harness-file]]).

The rule therefore rests on `basis: human` and stays there. It is not weaker for being unmechanised
— it is the class of rule the `rules` folder was created for.

# What stays here, and what is on the decision instead

**This page carries the instruction; [[how-a-slice-is-executed]] carries the decision.** The six
bullets of what was adopted, the four rejected alternatives, the sources each renegotiated rule
came from, and the two post-hoc confirmations — including the one that found three of four agent
reports wrong in the direction of *it went fine* — all live there, under
`authority: slice-execution`.

That split is also why this page carries `governs:` and **no** `authority:` field. A rule states
what a decision decided, so the pair would otherwise claim the same question and rule 3 of
`vault-check.sh` would print a contradiction on every normal decision-and-rule pair — whose
obvious repair is to break one of two pages that are both correct.

# Where it renders, and why the slug is not the obvious one

`governs: CLAUDE.md` — the repository's own file, written as a path from the repository root and
resolved against nothing else ([[governs-is-a-path-from-the-repository-root]]). The destination is
where that file is going: a dispatch table pointing at callable things, with the four rules moved
out into this folder ([[the-repository-claude-md-becomes-a-dispatch-table]]). The text lands in a
paired comment named for this page's slug, and the page and its region are written in the same
change ([[a-region-is-a-paired-comment-named-for-a-rule]]).

**The slug is `the-owner-decides-how-a-slice-is-executed` on purpose.** `how-a-slice-is-executed` is
taken by the decision page, and two pages sharing a basename would make every `[[wikilink]]` to
either of them ambiguous — in a store whose entire retrieval is grep plus links, that is an
address collision and not a naming preference.

If this rule is ever replaced, the successor renders and this page does not: a deprecated rule is
skipped by the injector, so retiring it does not put its text back into the file
([[a-deprecated-rule-does-not-render]]).

# The first of the four to move, 2026-08-17

**This is the first rule page in the vault.** The order was the owner's and it was not a preference:
the migration is exactly the moment a region can land in the wrong file, so it was scheduled behind
the address verdict that catches a marker pair copied into the wrong `SKILL.md`
([[a-region-is-checked-against-its-rules-governs]]). That verdict was built and proved before this
page was written.

**Three rules remain in the repository's `CLAUDE.md`** and are unaffected by this move. Nothing here
closes S2's criterion 4, which asks for that file to be pointers and for every skill or agent it
names to exist.
