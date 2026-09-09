---
title: "A suite's fixture must materialise what the subject reads, not what an earlier rule read"
type: lesson
status: archived
authority: fixture-materialisation
basis: code
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, vault]
---

# The defect, and what it would have cost

**The selftest's sandbox created placeholder files for the paths named in `sources:` — and only those.**
That was correct while `sources:` was the one field naming a path outside the vault.

**Then `governs:` arrived, naming a path the sandbox did not create.** The first real rule page would have
reddened the **pristine copy** of the vault before a single case ran — taking every `run_clean` assertion
and every expected exit code with it, because the baseline is what every case's verdict is measured
against ([[a-test-that-fails-for-its-own-reasons-proves-nothing]]).

**It was found by a `/pre-task` reading the code, not by the suite** — and the suite could not have found
it, because the failure arrives with the first rule page and the suite was green until then
([[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]]).

## The fix, and why it is *whole* rather than a placeholder

**The sandbox now materialises every destination a current rule governs**: it sweeps the region markers out
of the rule pages and **copies the real file whole**.

**A placeholder would not have worked, and the reason is the mechanism.** A rule's destination has to
arrive *carrying the region it holds*, or rule 12 reddens on the copy for lack of a region — so the fixture
cannot invent the file, it has to bring the real one. And the markers have to be swept out of the *pages*
in the sandbox, so that mutating a page in one case does not redden a destination the case never touched
([[a-rule-over-every-page-makes-every-test-fragile]]).

**Three cases were repaired for cause and one was flipped from red to green**, and the counts moved from
**97 caught, 0 missed** to **99 caught, 0 missed** — level rather than unmoved: one case went with the rule
it tested and one arrived in its place ([[governs-uniqueness-is-removed-and-the-pair-carries-it]]).

## The general form

**A fixture is written against the fields the subject reads at the time it is written**, and every new
field that names a path is a new thing the fixture has to produce. Nothing in this project links the two:
the schema grew `governs:` and the sandbox did not hear about it
([[a-field-earns-its-place-by-being-read-or-by-being-a-checksum]]).

**The question to ask when a schema grows a path-valued field is: what does the test harness have to
create now?** It is the same question as *which cases are now coupled* when a global rule is added, asked
of the fixture instead of the assertions.

# The same class again, and this time the fixture went quiet — 2026-08-20

**`.claude/hooks/ask-the-vault.ps1` dot-sources `.claude/hooks/pre-task-state.ps1`, and a failed
dot-source is swallowed by the `try` around it.** A sandbox missing that file therefore **did not
fail**: the state stayed null, every new branch was skipped, and the suite printed the same
`caught 70, missed 0` it prints when the code works
([[the-pre-task-state-library]]).

**The signal was the count that did not move.** Branches were added, cases were added, and the total
was unchanged — which was the only evidence available that nothing new had executed. **A suite
reporting identical green for working code and for code that never ran is worth distrusting on
exactly that evidence**, and the reading to take from it is the delta rather than the number
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]],
[[an-instrument-that-fails-towards-nothing-to-do]]).

**The generalisation on this page holds unchanged and gains a second field to ask about:** it is not
only path-valued frontmatter that a fixture has to produce, but every file the subject **loads at
run time** — a dot-source, an import, a generated rule file. The question is the same one: *what
does the harness have to create now?*
