---
title: "Our own JavaScript is allowed where it cannot show a wrong list"
type: decision
status: current
authority: js-scope
binding: prohibition
basis: human
sprint: S0
decided: 2026-08-12
created: 2026-08-13
sources: ["CLAUDE.md", "archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md", "src/jobhunt/web/templates/base.html", "archive/2026-08-26/2026-08-26-the-checks-get-an-entry-point-and-the-handoff-gets-a-gate/pages/our-javascript-does-not-choose-which-rows-are-on-screen.md"]
tags: [frontend, architecture, testing]
supersedes: [[our-javascript-does-not-choose-which-rows-are-on-screen]]
---

# Own JavaScript is allowed where it cannot show a wrong list

**Decided by the owner on 2026-08-12**, replacing «no JavaScript of our own beyond htmx and the
theme toggle».

**The line is what the code can affect, not how much of it there is.**

- **Allowed** — presentation and interaction no query depends on: the theme toggle (which already
  is this), disclosure, focus, highlighting, sticky headers, a keyboard shortcut that clicks a
  control the user could have clicked.
- **Not allowed** — anything that participates in *which rows are on screen*: assembling request
  parameters, filtering or sorting a list in the browser, deciding what a fragment asks for. That
  stays on the server, where the tests can reach it.

## The honest reason, which is not the one the old rule gave

Of the four silent defects slice 3 found, **three were plain test-coverage gaps that any
architecture would have had**; only the stale-chips one was genuinely htmx-shaped, because request
state is collected from a live DOM.

The real cost is that **no test here executes JavaScript** — `pytest` renders templates and asserts
attributes, and a JS runner would mean npm, which is forbidden. So our own JS is code only a
browser walk can check, and the rule keeps that untested surface away from the answer to "what is
in the table".

## What was rejected, and what is still owed

Rejected: the old blanket ban. The owner's argument stands and is a fair one — silent breakage is
something to watch for and cover with tests, not to architect around.

**Still owed:** the boundary is of the kind an AST test can pin, like the seven that already exist
([[architectural-boundaries]] — this page said *five* until 2026-08-14, from the same drift the
rule file had), and **no such test is written yet**. Write it with the first piece
of JavaScript that needs it.

The wider question this one sits inside — what the whole front end is, and on what condition React
would arrive — is [[the-stack-stays-htmx]].

**Still unwritten as of 2026-08-14**, re-checked at each of the two ingests since the rule was
narrowed on 2026-08-12; no new JavaScript has been written, so nothing has forced it.
**Still unwritten as of 2026-08-13.** The AST test was owed from the day the rule was narrowed;
no *new* JavaScript has been written since, so nothing has forced it, and a debt nothing forces is
a debt that is not paid. That is the shape
[[a-deferred-check-must-be-run-when-its-condition-arrives]] warns about — the trigger is "the next
piece of our own JavaScript", and the test belongs next to that code, not in a list.

## Where our own JavaScript actually is, so a test can find it

**All of it is inline in `src/jobhunt/web/templates/base.html`. There is no file of ours under
`static/`** — that directory holds `app.css` and the vendored `htmx.min.js`, and nothing else.
A test written from an earlier version of this page would scan `static/*.js`, find nothing of ours,
and pass having read nothing, which is this project's most repeated failure
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

| Where | What it is | Why it is where it is |
|---|---|---|
| `base.html`, line 7, in `<head>` | the theme bootstrap | **it cannot move.** It must run before the first paint, or every load flashes light before switching to dark |
| `base.html`, line 31, in `<head>` | the `htmx:responseError` handler — [[error-swap-gated-on-content-type]] | listens on `document`, not `document.body`, because in `<head>` the body does not exist yet |
| `base.html`, line 125, before `</body>` | the theme toggle — three modes cycled by one button | nothing holds it there; it could be a file under `static/` |

None of the three participates in which rows are on screen, so all three are on the allowed side
of the rule above. The middle one is the closest call and deserves its own sentence: it **swaps a
fragment the server sent** on an error response, which is presentation of an answer the server
already decided — and it is gated on `Content-Type: text/html` for exactly the reason that a swap
of something the server did not mean as a fragment is a different thing entirely.

# The rule page that rendered this into `CLAUDE.md` is folded in here — 2026-08-26

*(the owner selected it, against minting a second `authority:` slug and a second page.)*

**[[our-javascript-does-not-choose-which-rows-are-on-screen]] stops being a page.** Its instruction
is carried below, this page takes `supersedes:` for it, and the rule page is `deprecated` and
archived in the same pass — `deprecated` obliges a page to leave `wiki/` on sight and the gate says
so.

**Why it is folded rather than moved.** The slug it would have minted answers the question this page
already answers — *what may our own JavaScript do* — so a second `decisions/` page would have been a
second answer to one question, and the obvious name for it collides with this page's own filename.
The admission rule is the ground: no new entity where an existing one can carry the claim
([[no-new-entity-where-an-existing-one-can-carry-the-claim]]).

**What this supersedes.** [[the-javascript-rule-becomes-a-decision-and-leaves-wiki-rules]], taken the
same day, ruled that the rule becomes a `decisions/` page **of its own** with a new `authority:`.
The destination in that ruling stands and the second slug does not; the correction is recorded on
that page in a dated section.

## The instruction, exactly as it stood in the rule's `<!-- text -->` slice

> **Our own JavaScript may not participate in which rows are on screen.** Presentation is fine;
> anything that assembles request parameters or filters a list in the browser is not. Before
> writing any of it, ask — the rule has an exact shape and an owed test.

**Its "exact shape" is the two lists at the head of this page**, which is where it always was: the
slice said the shape is exact and deliberately did not carry it, because the line is about *what the
code can affect* rather than how much of it there is.

## Why asking cannot wait, which is the half the rule page carried

**Asked afterwards, the code is written and the review is a rewrite**
([[claude-md-is-a-map-and-four-rules]]). The instruction says to ask *before* writing any of it,
which is the only moment at which asking costs a sentence instead of a branch.

**And it is the one instruction of the four whose own text tells the reader that its enforcement
does not exist yet.** That clause is true exactly while the AST test above is unwritten. The day the
test is written, this page is the single place the clause is corrected, and changing it is the
owner's rather than the librarian's ([[a-deferred-check-must-be-run-when-its-condition-arrives]]).

**Where our own JavaScript is** was already on this page and is what the owed test has to be written
from — three inline blocks in `src/jobhunt/web/templates/base.html`, nothing of ours under
`static/`. A test written from an older reading would scan `static/*.js`, find nothing of ours, and
pass having read nothing ([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

## What the rule page carried that did not come with it

**The alarm and its resolution about `governs:` uniqueness** stay on the archived page: they are the
record of a gate verdict that was removed on 2026-08-17, and they are about the delivery mechanism
rather than about JavaScript ([[governs-uniqueness-is-removed-and-the-pair-carries-it]]).
