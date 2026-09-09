---
title: "The hand-written palette grows into a design system; no framework is vendored"
type: decision
status: current
authority: stylesheet-approach
binding: prohibition
basis: human
sprint: S0
decided: 2026-08-12
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md", "docs/superpowers/specs/2026-08-06-shell-and-two-pages-design.md"]
tags: [frontend, web]
---

# The palette became a design system instead of a vendored framework

**Decided 2026-08-12.** The visual slice grew the hand-written palette into a small design system.
It did **not** vendor a framework, and the reason is evidence rather than taste: slice 3's Task 6
had already implemented a vendored one, reviewed it, walked it in a browser and reverted it whole
(`c8cc50f`, reverted by `7abf211`) — **and three of the owner's four complaints are not what a
framework fixes.** The plan's separability clause is what made that revert cost almost nothing.

## What the slice changed

- the stylesheet is a **file** now, `src/jobhunt/web/static/app.css`, and a token layer — spacing,
  type, radii, an accent kept separate from `--link`, the row tints, one hue per status — lives in
  all three theme blocks;
- titles are weight rather than link-blue, the header has a bottom edge, and **the navigation moved
  left in CSS with `order`**: document order stays content-before-navigation for the screen reader;
- rows alternate instead of being ruled;
- seven columns became six — «Теги» joined the source on one muted line under the title;
- the status keeps its **native `select`** and gains `data-status`, which colours it;
- the filters became one panel of three rows, and «показать вакансии, у которых нет тега фильтра»
  became «без тега фильтра» with the full sentence moved into `title`;
- the chips lost the native checkbox and are pills coloured from `:has(:checked)`, with an
  `@supports` fallback that puts the box back.

None of this touches which rows are on screen, which is the line [[javascript-policy]] draws.

## The framework research, verified against downloaded files rather than blog copy

- **Pico's *classless* build was chosen for a property this markup cannot use.** It was picked
  because it switches themes on `data-theme`, which the existing toggle already writes — but its
  distinguishing feature, `header`/`main`/`footer` acting as containers, is **inert here, because
  `<main>` is not a direct child of `<body>`**. The cost was real: it has no `.secondary` opt-out
  (all 53 occurrences of the word in the file are variable names), so every button rendered
  primary-blue, «Показать ещё» and the theme toggle included. Pico's *default* build has
  `.secondary`, `.outline` and `.contrast` and the same `[data-theme]` switching, at 83 KB against
  71 KB.
- **Bulma matches this project's theme toggle exactly** — `data-theme` on any element plus a
  `prefers-color-scheme` fallback inside its own CSS, so the three-state toggle would need no
  change — and it ships **no JavaScript**, which *removes* the htmx re-initialisation question
  rather than answering it.
- **daisyUI's plain CDN file** is already compiled and uses the same `data-theme`, at **1.1 MB**.
- **Icons are a separate and cheap decision**: individual SVGs in a Jinja macro with `currentColor`
  already baked in, rather than a 0.5–1.8 MB sprite for twenty glyphs.

A vendored stylesheet would not be a dependency in the sense the project bans — that is how
`htmx.min.js` already ships. See [[the-stack-stays-htmx]]. The separate question of a *table*
library, which is not a styling question at all, is [[server-renders-the-table]].

**The spec that Task 6 pointed at carries a banner saying it is history.** §6 of
`2026-08-06-shell-and-two-pages-design.md` chose the classless build for the container property
above, and the abandoned implementation is exactly what disproved that reasoning.

## How this slice is judged

**The success criterion the owner set is not «it looks designed».** It is **that he starts opening
`/vacancies`** — and nothing else measures it. The open action item the source leaves is to ask him
whether he has.

## What this slice did not get, and it is the rule's only recorded exception

**The final three-lens review was skipped, by the owner's decision on 2026-08-12.**
[[how-a-slice-is-executed]] asks for three reviewers with different lenses at the end of a slice,
and that step is what found slice 3's Critical. What did run: an independent test cycle per task
with every literal-scanning assertion shown red by breaking exactly what it guards, a full suite per
task, and a browser walk per task in the main session.

**Treat the visual slice as unreviewed by a second party**, and weigh that if something in the
interface behaves oddly.

One earlier finding of the same shape closed with it: **no test fetched `/static/`** — see
[[a-test-green-under-any-implementation]]. And the walk that covered the earlier styling gap found
only one defect, that the elements introduced by slice 2a's tasks 3–8 had no CSS at all; it was
closed by describing them with existing palette variables, so both themes work without a second
edit.

The traps this slice met while checking its own work by eye are in
[[a-browser-walk-watches-the-network-not-the-screen]] — a screenshot proves nothing if a script
paints part of the page, and a CSS rule can be dead by specificity while looking mandatory.
