---
title: "The end of a run resets the chips first and re-reads the table after them, through one listener"
type: concept
status: current
authority: post-collection-refresh
basis: code
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md", "src/jobhunt/web/templates/_tag_chips.html", "src/jobhunt/web/templates/vacancies.html", "src/jobhunt/web/templates/_filters.html"]
tags: [htmx, filters]
---

# The chips reset first, the table re-reads after them

The chain, in order:

1. the run ends, and `HX-Trigger: jobhunt-collected` rides on the panel's last poll;
2. **`#tag-chips`** hears it — `hx-trigger="jobhunt-collected from:body"` — and asks
   `GET /vacancies/chips` for a fresh row;
3. that response announces its own swap with `HX-Trigger-After-Swap: jobhunt-chips-reset`;
4. **`#collected-refresh`**, a small stable element, hears the announcement and requests the rows;
5. the rows are answered with **`HX-Replace-Url`**, not `HX-Push-Url` — see
   [[address-bar-updated-by-header]].

*(The title read "The end of a run resets the chips first and re-reads the table second, through one
listener" until 2026-08-18, and the chain above is where the order lives. **`second` was sequencing
rather than counting** — the table re-reads because the chips response announced itself, not because
it holds position two in a list. It goes anyway: the owner has ruled ordinals into rule 10's word
list ([[ordinals-count-and-first-does-not]]), and the mechanism that used to let a page declare a
number harmless has been withdrawn, so there is no longer any way for this page to say so
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]).
The title is repaired here, before the predicate that will read it exists, so that tightening the
check reddens nothing ([[a-title-names-what-is-counted-instead-of-counting-it]]). This page never
carried a `quantity:` line, so nothing was stripped from its frontmatter.
**The heading above still read "the table re-reads second" after that repair**, and is brought
into line on the same date. No check reads a body heading and counting them is out of scope, but
this divergence was made by our own retitle, and a reader opening the page met the repair
half-done.)*

## The filters form does not listen, and that is the whole point

**The filters form no longer listens for `jobhunt-collected` at all.** Two listeners on one event
raced, and the losing order **hid what the run had just found** — that was the Critical of slice
3's whole-branch review, fixed in `dd1b446`.

`_filters.html` says so in the template itself: the form has one job, and this is not it.

## Why the chain has the shape it has

The reasoning was re-read in the main session on 2026-08-11 rather than sent to an agent, and this
is what was checked:

- the chain is **causal rather than raced** — one listener on `jobhunt-collected`, and the rows
  wait on the chips response's own `HX-Trigger-After-Swap`;
- `from:body` is right because `outerHTML` removes the requesting element before htmx fires the
  event — **which is also why `#collected-refresh` sits outside the chip row**;
- `vacancy_chips` re-renders the same template, so the new row brings its own trigger and a second
  run behaves like the first;
- `hx-include="#filters, .chips"` loses nothing, because the search field is inside the form.

The visible consequence of resetting the chips first was accepted deliberately: see
[[collection-end-resets-the-chips]].

> **This page recorded the slice 2b behaviour until 2026-08-13.** It said the *filters form* hears
> the event, which was true before `dd1b446` and false after — and it contradicted its own second
> half, which already described the corrected chain. The source carried both versions: the
> **corrected** one at line 151, naming `dd1b446`, and the superseded one at line 363, inside §0.4
> «What slice 2b built», which was frozen at that slice's date. The migration took its topic
> sentence from the later passage because that passage opens with this page's own title words, and
> used nothing from the earlier one. That is the same failure the vault exists to prevent,
> committed by the migration itself; see [[ingest-is-units-and-verdicts]].
>
> *Corrected 2026-08-13:* this note said until then that the older version «came earlier in the
> file» and that the migration «copied the first it met». Both are false of that document — it grew
> by prepending, and position separates nothing in it. The rule that does is
> [[a-long-source-contradicts-itself-and-the-first-hit-is-the-old-one]].

See [[htmx-swap-target-invariant]] for the class of silent failure this chain would otherwise join,
and [[polling-only-during-a-run]] for what the panel does not do.
