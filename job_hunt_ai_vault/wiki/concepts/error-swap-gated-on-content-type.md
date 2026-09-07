---
title: "The global error handler honours hx-swap only for text/html, or an unhandled server error kills the panel permanently"
type: concept
status: current
authority: error-swap-safety
basis: code
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md", "src/jobhunt/web/templates/base.html"]
tags: [web, htmx]
---

# The error swap is gated on `Content-Type: text/html`

**Where it is: `src/jobhunt/web/templates/base.html`, lines 66–76** — an `htmx:responseError`
listener inside the second inline `<script>` of `<head>`. It is not a FastAPI exception handler and
it is not in `src/jobhunt/web/app.py`, which registers none; a reader who greps the Python for
"the global error handler" finds nothing and concludes there is no such thing. It is listened for
on `document` rather than `document.body` because at parse time in `<head>` the body does not yet
exist. It is one of the three pieces of our own JavaScript ([[javascript-policy]]).

It exists because htmx 2 does not swap the body of a 4xx/5xx response at all
(`responseHandling: swap:false`), so a refusal the server rendered on purpose would otherwise be
invisible — a native `<select>` keeps showing the user's choice while the server has kept the old
one.

Honouring `hx-swap` in it was right for the 409 refusal — that response *is* a fragment.

**But `outerHTML` applies just as well to an error body that is not one.** An `HTTPException`
answers JSON; an unhandled 500 answers plain text. Either one replaced the whole
`<div id="collection">` — **including its `hx-trigger`** — and the panel then never polled again.
The `innerHTML` it replaced had healed itself on the next poll.

*(The title read "The global error handler honours hx-swap only for text/html, or a 500 kills the
panel permanently" until 2026-08-18, and the sentence above is where the status code now lives.
**500 was never a count**: it is the name of a class of response, like the 409 just above, and
no second one of it can arrive and make this page stale. That reasoning stood in a `quantity:` line
on this page until the field was rejected and the rule made unconditional in both halves
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]); the title now names the
failure the number stood for instead of numbering it
([[a-title-names-what-is-counted-instead-of-counting-it]]). Wrapping the number in a code span was
available and is not the answer: this page writes 4xx/5xx, 409 and 500 in plain prose throughout, so
backticks here would be typography chosen to make a check skip a string.)*

**Fixing a nesting bug made a rare failure unrecoverable.** That is the shape worth remembering:
the fix was correct for the case it was written for, and the case it was not written for got worse.

The swap is now gated on `Content-Type: text/html`, with a non-vacuity test in the shape of its
sibling.

This is the same family as [[htmx-swap-target-invariant]]: htmx failing in a way that leaves no
trace on screen and none in the network panel, because after the swap there is nothing left to
make a request.
