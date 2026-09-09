---
title: "Retiring a page"
type: rule
status: current
authority: archive-script
render: authority
basis: human
sprint: S3
created: 2026-08-31
sources: ["docs/vault-cleanup-families.md", "authority.md"]
decided_by: [[archive-is-dated-by-session-and-holds-what-left-the-working-set]]
tags: [vault, process, harness]
---

# Retiring a page

How a page leaves the working set, what an archived one still asserts, when a proposal is retired, and what a text corrected in place owes instead. Answers "this page has gone false — is it retired or repaired".

**This rule is written into no file.** It is found by its `authority:` slug, by `.claude/hooks/serve-the-rule.ps1`, when a page carrying that slug is read. Each clause below is the claim of one decision, which keeps the reasoning and the rejected alternative it was taken against, and leaves for `archive/` when `scripts/vault-archive.sh` releases it.

# The rule text

- A `deprecated` page needs a live successor named in `superseded_by:` before it may leave ([[a-deprecated-page-needs-a-live-successor-named-in-superseded-by-before-it-may-leave]])
- A correction note is dated the day the text became false, not the day the session ran ([[the-date-of-a-correction-note-is-the-date-the-text-became-false]])
- A refused proposal moves to `archive/` and takes `status: refused`, and the value is not minted ([[a-refused-proposal-is-archived-and-takes-status-refused]])
- An implemented proposal moves to `archive/`, and the successor page carries its claim ([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]])
- The archive is a directory of the vault and gains a folder per session inside the date ([[the-archive-gains-a-folder-per-session-inside-the-date]])
- The archive sweep reports a refusal, and the gate stays silent about placement ([[the-archive-sweep-reports-a-refusal-and-the-gate-stays-silent-about-placement]])
- The archiver sets `status: archived` mechanically, and the value enters the schema before the sweep runs ([[the-archiver-sets-status-archived-and-the-value-enters-the-schema-first]])
- The authority register step is repealed, and a page goes to `archive/` keeping its slug ([[the-authority-register-step-is-repealed-and-an-archived-page-keeps-its-slug]])
- The lessons cycle is the owner's own, and a lesson leaves `lessons/` when a page outside `lessons/` cites it ([[the-lessons-cycle-is-the-owners-and-a-lesson-leaves-when-a-page-outside-lessons-cites-it]])
- What an archived page asserts is frozen, and how it is found is live ([[what-an-archived-page-asserts-is-frozen-and-how-it-is-found-is-live]])
- `archive/` is dated by session and holds everything that left the working set that day ([[archive-is-dated-by-session-and-holds-what-left-the-working-set]])
- `scripts/vault-archive.sh` gains a `pages` kind, and the archive's clause about retired pages becomes executable ([[the-archive-script-gains-a-pages-kind-and-a-retired-page-is-dated-by-its-session]])

# How this page was written

Drafted 2026-08-31 by `scripts/build-family-rules.py` from the family *retiring a page* of `authority.md`. The clause of each member is its title, because only two of the 295 prohibitions the cleanup surveyed carried a written rule text of their own.

**The slug is not the script's pick.** The script takes the `authority:` of the earliest-decided member, `archive-scope`, whose decision leaves for `archive/`. Three live pages of this family were available; the slug carried is `archive-script`, which [[vault-archive-sh]] carries and keeps. That entity is the tool every clause here ends up instructing — it moves the page and rewrites its citations — so reading it hands over the rules it is expected to obey. `deprecated-rule-rendering` and `refusal-archive-ordering` each answer one case inside that. `decided_by:` still names a member decision, which is what this folder requires.
