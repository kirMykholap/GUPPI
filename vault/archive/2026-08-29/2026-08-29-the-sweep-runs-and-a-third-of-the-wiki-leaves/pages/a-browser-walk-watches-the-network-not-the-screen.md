---
title: "On a browser walk, read the network requests — the screen shows the consequence, not the fact"
type: lesson
status: archived
authority: browser-walk-method
basis: measurement
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [testing, web]
---

# Watch the requests, not the screen

**Playwright types text but does not drive htmx triggers bound to `keyup`.**
`pressSequentially` fills the field and the DOM value is correct — and no request goes out, so
search *looks broken* during a walk. One real key press and it works. The same trap in another
disguise: Cyrillic typed through `insertText` fires no `keyup` at all.

The general rule the harness taught: **the screen shows the consequence; you need the fact of
sending.**

## The other harness traps, which have cost three slices between them

- **a first batch of 50 is not a full list** — do not conclude from the first page;
- **collection runs are shorter than hand timing suggests**;
- **one tool call's observation of the *previous* call's page state is seven-plus seconds late**,
  which is half a run.

The single rule covering the last two: **issue the action and its observation in the same call, or
record the timeline in the page and read the recording afterwards.**

## Comparing screenshots proves nothing if a script paints any of the page

The theme button ships in the markup with `hidden` and is revealed by a script, so a shot taken
"before the script ran" differs from one taken after **with no relation to the change under test**.
That cost ten minutes of suspicion during the stylesheet move.

The honest method is **old code against new, captured within one minute**: `git stash` the
template, restart, shoot; `git stash pop`, restart, shoot. And before trusting any difference,
**take two frames of the same state**: if those differ, the method is noisy and the difference
means nothing.

## And a CSS rule can be dead by specificity while looking mandatory

`.chip-off:has(:checked)` was written for the composition "off and checked" and did nothing:
`.chip:has(:checked)` weighs 0-2-0 against `.chip-off`'s 0-1-0. Checked in seconds on a live page —
delete the rule through the CSSOM and read the computed value. It had not changed by one bit. The
technique applies to any rule kept "just in case".

## And one harness artefact that is not a defect at all

**Setting `data-theme` on `<html>` by hand leaves the theme button's icon stale.** The icon follows
`data-mode` on the button, which only the button's own click handler writes; clicking cycles both
correctly. **Drive the theme by clicking, not by setting the attribute** — recorded so the next walk
does not report it as a bug.

See [[empty-state-must-bring-the-panel]] for a defect a walk missed because it reached the state
through the CLI rather than through the page.

The harness itself, and what a configuration change to it does not do until the next process: [[playwright-mcp]].
