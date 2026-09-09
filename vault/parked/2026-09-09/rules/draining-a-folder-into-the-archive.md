---
title: "Draining a folder into the archive"
type: rule
status: current
authority: sweep-mode-inheritance
render: authority
basis: human
sprint: S3
created: 2026-08-31
sources: ["docs/vault-cleanup-families.md", "authority.md"]
decided_by: [[a-decisions-archival-condition-is-read-off-its-binding]]
tags: [vault, process, record-schema]
---

# Draining a folder into the archive

Why the working wiki is swept at all, which criterion each folder leaves by, what a sweep does when a move is refused, and what the mark a drained page carries means. Answers "should this page still be in `wiki/`, and what decides that". Distinct from *retiring a page*, which answers "this one has gone false".

**This rule is written into no file.** It is found by its `authority:` slug, by `.claude/hooks/serve-the-rule.ps1`, when a page carrying that slug is read. Each clause below is the claim of one decision, which keeps the reasoning and the rejected alternative it was taken against, and leaves for `archive/` when `scripts/vault-archive.sh` releases it.

# The rule text

- A `wiki/rules/` page leaves only on a decision saying so and a `deprecated` mark ([[a-rules-page-leaves-only-on-a-decision-and-a-deprecated-mark]])
- A decision's archival condition is read off its `binding:` ([[a-decisions-archival-condition-is-read-off-its-binding]]) — **narrowed permanently on 2026-08-31**: a `prohibition` whose clause is carried by a live family rule leaves by the ordinary path, because the hook now delivers that clause to the reader `wiki/decisions/` was being kept full for ([[the-cleanup-suspends-the-rules-that-would-refuse-it]])
- A prohibition family becomes one rule page served by a hook, and the decisions behind it then leave ([[a-prohibition-family-becomes-one-rule-page-served-by-a-hook]])
- The archiver checks the criterion, marks and moves a decision in one pass, and the librarian sets no mark ([[the-archiver-marks-and-moves-a-decision-in-one-pass]])
- The cleanup suspends the rules that would refuse it, and says so in one place ([[the-cleanup-suspends-the-rules-that-would-refuse-it]])
- The deprecated-link advisory prints one line per dead target, not per citing page and not per edge ([[the-deprecated-link-advisory-prints-one-line-per-dead-target]])
- The output side is finished today, and it does not close the corpus's growth ([[the-output-side-is-finished-today-and-does-not-close-the-corpuss-growth]])
- The purpose of archiving is a cheaper working wiki, and `archive/` is a warehouse ([[the-purpose-of-archiving-is-a-cheaper-working-wiki-and-archive-is-a-warehouse]])
- The sweep runs for real over every criterion, and records what it moved in `log.md` ([[the-sweep-runs-for-real-over-every-criterion-and-records-what-it-moved]])
- The vault-root registers do not count as citers, and rendering them from rule pages is his idea and unbuilt ([[the-vault-root-registers-do-not-count-as-citers]])
- `processed` is repealed, and what it distinguished is derived from the tree instead ([[processed-is-repealed-and-the-mark-it-carried-is-derived]])
- `proposals/` and `lessons/` are not touched by the cleanup ([[proposals-and-lessons-are-not-touched-by-the-cleanup]])
- `wiki/decisions/` is censused before its type system is redesigned, and the delta rule is withdrawn ([[the-decisions-folder-is-censused-before-its-type-system-is-redesigned]])

# How this page was written

Drafted 2026-08-31 by `scripts/build-family-rules.py` from the family *draining a folder into the archive* of `authority.md`. The clause of each member is its title, because only two of the 295 prohibitions the cleanup surveyed carried a written rule text of their own.

**The slug is not the script's pick.** The script takes the `authority:` of the earliest-decided member, `decision-archival-condition`, whose decision leaves for `archive/`. Six live concepts of this family were available; the slug carried is `sweep-mode-inheritance`, which [[the-sweep-is-a-mode-of-the-archiver-and-inherits-its-refusals]] carries and keeps. The sweep **is** the draining this family names, and that concept states what the sweep is and why it holds no opinion of its own; the other five describe a predicate, a status, a selector or an advisory inside it. `decided_by:` still names a member decision, which is what this folder requires.
