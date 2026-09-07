---
title: "Removing the JavaScript rule from `CLAUDE.md` is agreed and is not yet done"
type: decision
status: current
authority: javascript-rule-delivery
binding: deferral
basis: human
sprint: S2
decided: 2026-08-18
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls/handoffs/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls.md", "CLAUDE.md"]
tags: [harness, frontend, process]
---

# Agreed by the owner on 2026-08-18, and this is the dated page it needs

**Ceasing unconditional delivery is a change of guarantee, not a change of address**, so it needs
its own decision before anything moves ([[a-rule-moving-to-conditional-delivery-needs-its-page-first]]).
This is that decision for [[our-javascript-does-not-choose-which-rows-are-on-screen]]. **Nothing has
moved yet**: the rule still renders into `CLAUDE.md` and the region is still there.

**The owner's ground:** the system is *"about to write something → ask the vault"*. `/pre-task`
enumerates the constraints on a plan rather than answering a topic query, so **a rule nobody knows
exists is still surfaced** — the reader does not have to know its name to be handed it.

**The session argued the opposite and conceded.** Its case was that a rule you must ask for is a
rule you can fail to ask for; what settled it was the session's own transcript, where `/pre-task`
surfaced constraints three times that could not have been queried by name — eight `decisions/` pages
in the first answer alone ([[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]]).

**Rejected: leave it in `CLAUDE.md`.** Refused on the criterion for what that file carries — a rule
that is reached by asking, and whose breach is caught in review rather than being irreversible, is
not what bootstraps the asking
([[core-is-what-bootstraps-the-asking-and-what-is-irreversible-if-missed]]).

## What this is not

**It is not the path-scoped move.** The JavaScript rule fails the criterion for that
([[moving-a-rule-into-claude-rules-with-a-paths-scope]]): our JavaScript is inline in a template,
nothing of ours sits under `static/`, and writing a *new* file matches no read
([[a-scoped-rule-fires-on-a-read-and-an-edit-implies-one]]). The rule stays a vault page reached by
a question; what ends is the unconditional copy in `CLAUDE.md`.

**What it obliges when it is executed:** the region leaves `CLAUDE.md` in the same change as the
page's `governs:`, or rule 11's address verdict fires on the leftover
([[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]]). The rule page itself does not
disappear — a rule with no destination is a decision page's text, and which shape it takes is
unsettled here.

# The ground under this page moved on 2026-08-20, and re-reading it is owed

**This page's ground is that `/pre-task` surfaces a rule nobody knows exists** — the reader does not
have to know its name to be handed it. **That rested on `/pre-task` arriving unconditionally**, and
on 2026-08-20 the `/pre-task` rule itself left `CLAUDE.md` for a hook message
([[the-pre-task-rule-leaves-claude-md-for-a-hook-message]],
[[a-pre-task-runs-between-the-plan-and-its-approval]]).

**So the argument now has a step in it that it did not have when it was accepted**: the JavaScript
rule may leave because `/pre-task` will surface it, and `/pre-task` arrives only when a hook event
fires — a plan presented, or a first write in a session that presented none.

**Nothing here decides anything.** The journal of 2026-08-20 names this page as owing a re-reading in
that light, and this section is that flag rather than the re-reading. **Whether the ground still
holds is the owner's**, and the state is unchanged in the meantime: the rule still renders into
`CLAUDE.md` and the region is still there
([[the-librarian-writes-unattended]], [[ask-before-weakening-or-working-around-a-rule]]).

# The re-reading was done and the ground holds — 2026-08-26

*(the owner selected it.)* **`/pre-task` arriving by hook is not a weakening of the argument.** He had
already judged hook delivery **more reliable** than a region a reader skips, when the `/pre-task`
rule itself made that move ([[the-pre-task-rule-leaves-claude-md-for-a-hook-message]]).

**So this decision is executed rather than re-opened**, and what was left unsettled here — *which
shape the rule page takes when it has no destination* — is now decided: it becomes a `decisions/`
page with `binding: prohibition`, minting an `authority:` and losing `governs:` and `render:`
([[the-javascript-rule-becomes-a-decision-and-leaves-wiki-rules]]).

**What remains is work, not a question**, and it waits with the plan's third phase
([[the-plans-remaining-phase-moves-to-s3-and-the-ritual-runs-whole]]). **The region is still in
`CLAUDE.md` as of this ingest.**

*(Compiled from `raw/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md`.)*

# The rule page is gone and the region is not — 2026-08-26, later the same day

**Executed, and the two halves did not land together.** The rule page is `deprecated` with
`superseded_by: [[javascript-policy]]`, has lost `governs:` and `render:`, and is in
`archive/2026-08-26/…/pages/`. **The region is still in `CLAUDE.md`, at line 102.**

**It was not left standing by choice: the injector cannot remove it.** A `region`-mode retirement is
handled by skipping the page and letting a successor overwrite the region, and there is no successor
rendering here — the rule folded into [[javascript-policy]], which renders nothing
([[a-deprecated-rule-does-not-render]]). `bash scripts/vault-inject.sh` reported *0 region(s)
rewritten, 0 file(s) generated, 0 removed, 0 problem(s)*.

**So rule 11's address verdict fired, exactly as this page said it would**, and the gate is red on
one line ([[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]]). **Removing the
marker pair and the text between it is the session's**, and the librarian was ordered to leave the
file alone rather than guess at it.

**Until that edit lands, the answer to this page's question is: agreed, the page has moved, and the
copy in `CLAUDE.md` is still being delivered to every session that reads the file.**
