---
title: "A plan can be factually wrong about the tree, and the `/pre-task` is the step that reads the tree"
type: lesson
status: archived
authority: plan-versus-tree-defects
basis: measurement
sprint: S3
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-feedback-line-is-spoken-and-the-floor-under-a-session-is-read/handoffs/2026-08-24-the-feedback-line-is-spoken-and-the-floor-under-a-session-is-read.md", ".claude/agents/pre-task.md"]
tags: [process, agents, vault]
---

# Five items of one approved plan were wrong about the tree, and one run found all five

The plan had been written, revised and read. **The `/pre-task` on its second edition killed:**

- **a deadlock the plan had walked into** — a rule given `governs:` on a git-ignored file that
  `/handoff` empties, which would have exited the injector 1 and locked the librarian out
  ([[a-rule-may-not-govern-a-file-the-ritual-empties]]);
- **a ratification of something already ratified and built** — multi-target `governs:` was settled
  on 2026-08-21, is declared in `wiki/rules/_schema.yaml`, and is enforced by the `blockgoverns`
  verdict ([[governs-takes-a-bare-path-or-an-inline-list-and-the-block-form-is-red]]);
- **"rewrite the rule page"**, where a changed claim demands a supersession
  ([[a-title-corrected-in-place-is-not-a-supersession]]);
- **a count of nine plan-mode breakages** where the page recording them says eight;
- **a back-fill population of "46 pages, 0 filled"** where the tree holds **50, 17 filled, 33
  short**.

# Why the plan review could not have caught them

**Every one is a claim about the tree rather than about the design.** A reviewer reads the plan for
coherence; the tree is a second document, and only a step whose whole job is to enumerate it will
notice that a number in the plan and a number in the corpus disagree
([[a-proposal-can-be-wrong-about-the-hole-it-describes]],
[[the-pre-task-splits-into-a-cheap-enumeration-and-a-narrow-dispatch]]).

**Two of the five are the shape this store keeps recording**: a count copied into prose and gone
stale ([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]), and a settled ruling
re-argued because nothing pointed at where it was settled.

# What the run cost, which is the other half of the argument

**182,599 tokens, 13m40s, 57 tool uses.** The shortlist named **74 pages** drawn from an enumeration
of **388 rows**; the agent opened **25 in full**, plus two registers and nine tree files.

**Third point beside the pair of 2026-08-23** — 230,882 tokens / 14m58s and 225,195 / 16m. **Not a
rate**: three plans of similar size, and nothing here says what a larger one would cost
([[a-subagent-cannot-report-its-own-cost]]).

# It happened again on 2026-08-24, and the fifth item was a page that does not exist

**Five factual claims of an approved plan were killed by one run.** Two of them are the day's own
counting failures — a rule heading the plan said did not exist
([[a-pattern-requiring-a-dot-after-a-rule-number-cannot-see-a-shared-heading]]) and a
suite described by a subtotal ([[a-subtotal-read-as-a-total]]).

**The other three are about the tree itself.** The plan cited a corpus page about a variable leaking
between sections; there is no such page. It placed
[[a-verdict-pairing-the-idea-status-with-a-named-decision]] in `decisions/` when it lives in
`proposals/`. And it carried a projection with no instrument behind it
([[a-projection-is-published-with-its-instrument-or-not-at-all]]).

**A citation to a page that does not exist is the worst of them**, because it reads as evidence and
there is nothing to check it against until somebody opens it.

**The run's two counts: the shortlist named thirty-two pages and twenty-one were opened in full.**
Cost: 186,629 tokens, 63 tool uses, 11m52s — a fourth point beside 230,882/14m58s, 225,195/16m and
182,599/13m40s. **Four points, not a rate.**

**And the run itself broke a rule to happen.** The ritual may be performed only by dispatching the
agent, and the session's own instructions forbid dispatching one unasked; the session put the
contradiction to the owner rather than resolving it
([[divergence-the-session-dispatched-an-agent-where-its-instructions-forbid-one-unasked]]).

# A plan can quote a rule to the owner and break it an hour later — 2026-08-26

**The session cited the one-writer clause to the owner in conversation, and then wrote a plan whose
phase 1 put four `wiki/` files in the session's own hands** — plus one file under `raw/`, which is
immutable. **Nothing in the writing caught it. The `/pre-task` reading the plan did.**

**Knowing a rule and applying it to your own draft are different acts**, and the first is no evidence
about the second ([[knowing-a-rule-is-not-a-mechanism]],
[[hand-edits-of-the-wiki-are-a-recorded-divergence]]).

## Three more plan defects the same run found, and each needed the tree

- **Three refused proposals were to be archived. One was already in `archive/` since 2026-08-21, and
  a second has no proposal page at all** — it is a `decisions/` page with `status: current`, and a
  decision is refuted rather than refused.
- **Not one step named `authority.md`, against four archive moves**, while
  [[retiring-a-page-removes-its-slug-from-the-authority-register]] obliges the slug to leave first.
  `vault-authority.sh --check` was clean on 666 slugs, so the plan itself would have reddened it.
- **The four CRLF files were said to be outside `wiki/`** and four of five are inside it.

**Every one of these is a fact about the tree that no amount of care in drafting supplies**, which is
this page's claim, now with a second day of evidence behind it.

*(Compiled from `raw/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md`.)*
