---
title: "Our own JavaScript does not choose which rows are on screen, and the test for it is still owed"
type: rule
status: deprecated
basis: human
sprint: S2
created: 2026-08-17
sources: ["CLAUDE.md", "src/jobhunt/web/templates/base.html", "[[javascript-policy]]", "[[claude-md-is-a-map-and-four-rules]]"]
decided_by: [[javascript-policy]]
tags: [harness, frontend, architecture]
superseded_by: [[javascript-policy]]
---

# What travels

<!-- text -->
**Our own JavaScript may not participate in which rows are on screen.** Presentation is fine;
anything that assembles request parameters or filters a list in the browser is not. Before
writing any of it, ask — the rule has an exact shape and an owed test.
<!-- /text -->

**That is rule 3 of the repository's `CLAUDE.md`, to the word** — the third item of a numbered list,
dedented and nothing else. Verified as the rest of this migration was: the lines were cut out of the
file by line number, the ordinal and the list indent stripped mechanically, and the result diffed
byte for byte against the slice above rather than read against it.

Everything below this line stays on this page
([[what-travels-from-a-rule-page-is-a-marked-slice]]).

# Why it cannot wait for a question

**Asked afterwards, the code is written and the review is a rewrite**
([[claude-md-is-a-map-and-four-rules]]). The text itself says to ask *before* writing any of it,
which is the only moment at which asking costs a sentence instead of a branch.

The reason underneath is not architectural taste. **No test here executes JavaScript**: `pytest`
renders templates and asserts attributes, a JavaScript runner would mean npm, and npm is forbidden.
So our own JavaScript is code that only a browser walk can check, and the rule keeps that unchecked
surface away from the answer to *what is in the table* ([[javascript-policy]],
[[server-renders-the-table]]).

# Where the exact shape is recorded

**On [[javascript-policy]], which is where the rule's "exact shape" lives, and nowhere else.** The
slice above says the shape is exact and does not carry it — deliberately, because the line is about
*what the code can affect* rather than how much of it there is, and stating it takes both halves:

- **allowed** — presentation and interaction that no query depends on: the theme toggle, disclosure,
  focus, highlighting, sticky headers, a keyboard shortcut that clicks a control the user could have
  clicked;
- **not allowed** — anything that participates in which rows are on screen: assembling request
  parameters, filtering or sorting a list in the browser, deciding what a fragment asks for.

That page also records **where our own JavaScript actually is**: three inline blocks in
`src/jobhunt/web/templates/base.html`, and nothing of ours under `static/`, which holds `app.css`
and the vendored `htmx.min.js`. That location is load-bearing for the owed test — a test written
from an earlier version of the page would scan `static/*.js`, find nothing of ours, and pass having
read nothing ([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

The rule as it stands is also a **narrowing** of an earlier blanket ban on our own JavaScript,
decided by the owner on 2026-08-12; the rejected alternative and the measurement behind it are on
that same page, and the wider question of what the front end is at all is
[[the-stack-stays-htmx]].

# The owed test, and what is known about it

**It is owed, it is unwritten, and its trigger is the next piece of our own JavaScript.** It would
join the AST family that already holds the layering ([[architectural-boundaries]]), and it belongs
beside the code that forces it rather than in a list of intentions — a debt nothing forces is a debt
that is not paid ([[a-deferred-check-must-be-run-when-its-condition-arrives]]).

It has been re-checked at each ingest since the rule was narrowed and is still unwritten, for the
same reason each time: no new JavaScript of ours has been written, so nothing has forced it
([[javascript-policy]]).

**This is the one of the four rules whose own text tells the reader that its enforcement does not
exist yet**, and that is the honest state to render. The day the test is written, the rule's text
stops being true in that clause and the page is the single place it is corrected; the region follows
on the next injector run ([[what-travels-from-a-rule-page-is-a-marked-slice]]). Changing that clause
is the owner's, not the librarian's — this page records that the debt is open, and nothing more.

# Where it renders

`governs: CLAUDE.md` — a path from the repository root, resolved against nothing else
([[governs-is-a-path-from-the-repository-root]]). The text lands in a paired comment named for this
page's slug ([[a-region-is-a-paired-comment-named-for-a-rule]]), in a file on its way to being a
dispatch table ([[the-repository-claude-md-becomes-a-dispatch-table]]).

**The page and its region belong in one change, and this page arrived first.** The librarian writes
`wiki/`; marking the region and running the injector are the session's, in the same commit. Until
then rule 12 reports this rule as governing a file that carries no region for it. If the rule is
ever replaced, the successor renders and this page does not
([[a-deprecated-rule-does-not-render]]).

> [!CAUTION] CONTRADICTION
> **The gate is red on a second line, and that one is not about the missing region.** This page is
> one of several current rules governing `CLAUDE.md`, and `governs:` is required to be unique across
> current rules, so `vault-check.sh` prints *two current rules govern the same destination:
> `CLAUDE.md`*. The injector renders them all into that file without complaint — measured.
> Unresolved, and not the librarian's to choose:
> [[a-deprecated-rule-does-not-render]] carries the measurement, [[rules-becomes-a-type-of-its-own]]
> carries the migration it collides with.

> [!NOTE] RESOLVED BY THE OWNER, 2026-08-17
> **The uniqueness went out of the check, and the migration stands.** At `e478c19` the owner removed
> `governs:` uniqueness from `scripts/vault-check.sh`, on the first day it met a real tree: it was
> stricter than the schema it guarded, which says a rule names the one destination *its own* text
> goes to and says nothing about a destination taking one rule. What it appeared to protect is held
> by verdicts that read the tree instead — one slug marking two regions in one file, and a region
> sitting in a file its rule does not govern — and its selftest case **flipped rather than
> disappearing**: two rules on one file with two regions is now asserted green. The gate no longer
> prints that line. The block above is left standing as the record of the alarm that produced the
> decision, which is the point of marking rather than choosing
> ([[ask-before-weakening-or-working-around-a-rule]]).

# The instruction and the decision are different pages

[[javascript-policy]] answers `authority: js-scope` — what is allowed, what was rejected, where the
code is, and what is owed. This page carries only the instruction, and carries `governs:` in place
of an `authority:`, so the pair does not read as two answers to one question
([[rules-becomes-a-type-of-its-own]]).

# This page is decided to leave `wiki/rules/` — 2026-08-26

**It becomes a `decisions/` page with `binding: prohibition`**, minting an `authority:` slug and
losing `governs:` and `render:`
([[the-javascript-rule-becomes-a-decision-and-leaves-wiki-rules]]).

**Nothing has moved.** The region is still in `CLAUDE.md`, `governs:` still names it, and the text
slice above is unchanged — the move is an S3 line and the region leaves in the same change as the
field ([[the-plans-remaining-phase-moves-to-s3-and-the-ritual-runs-whole]],
[[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]]).

# It did not become a page of its own: it is retired into [[javascript-policy]] — 2026-08-26, later the same day

**The section above is struck in its shape and stands in its destination.** The owner ruled that the
rule folds into [[javascript-policy]], which already carries `authority: js-scope` — *what our own
JavaScript may and may not do* — rather than minting a second slug for a second page. So there is no
new `decisions/` page and no register edit: this page is `deprecated` with
`superseded_by: [[javascript-policy]]`, `governs:` and `render:` are off it, and it moved to
`archive/` in the same pass ([[the-javascript-rule-becomes-a-decision-and-leaves-wiki-rules]],
[[no-new-entity-where-an-existing-one-can-carry-the-claim]]).

**The instruction it carried is on [[javascript-policy]] verbatim**, quoted as the slice stood.
Everything else on this page is history and stays here — including the `governs:`-uniqueness alarm
above and the owner's resolution of it, which is about the delivery mechanism and not about
JavaScript.

**What happened to the region in `CLAUDE.md` is recorded on
[[the-javascript-rule-leaves-claude-md-and-is-not-yet-removed]]**, which is the page that answers
whether it is gone. It is not answered here, because this page is leaving and nothing in `archive/`
is ever re-read by a check.

*(Compiled from `raw/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md`.)*
