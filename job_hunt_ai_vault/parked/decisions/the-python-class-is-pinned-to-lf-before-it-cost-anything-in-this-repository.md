---
title: "`*.py` is pinned to LF against the principle that a class is pinned after it costs something"
type: decision
status: current
authority: python-line-ending-pin
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-24
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-feedback-line-is-spoken-and-the-floor-under-a-session-is-read/handoffs/2026-08-24-the-feedback-line-is-spoken-and-the-floor-under-a-session-is-read.md", ".gitattributes"]
tags: [harness, process, testing]
---

# Ratified 2026-08-24, from a menu

**The owner selected "Закрепить".** `.gitattributes` pins `*.py` to LF, alongside `*.sh`, `*.md`,
`*.ps1`, `*.json`, `*.yaml` and `*.tsv`.

**Chosen against leaving it unpinned until the class costs something**, which is what that file's
own stated principle says ([[a-file-class-is-pinned-after-it-costs-something]]).

# The ground for overriding the principle: the failure is not speculative

**The identical mechanism was paid for on `*.ps1` on 2026-08-17** — an edit script's LF anchors
matching nothing in a CRLF file — and **`sed -i` with LF anchors was run against a `.py` file twice
on the day of this ruling**, which added three Python files to a repository that had none under
`scripts/`.

**Git had already warned on `git add`**: *"LF will be replaced by CRLF the next time Git touches
it."* The warning is the cost arriving, one step ahead of the debugging pass
([[line-endings-make-git-status-overstate-what-changed]],
[[the-lf-pin-protects-the-blob-and-git-status-is-silent-about-the-working-copy]]).

# The departure is recorded rather than smoothed over

**The principle it overrides is a live decision of this store, and it is not amended here.** What
this page records is a ruling that departs from it on a named ground: the mechanism already has a
receipt in this repository, so waiting buys nothing but the receipt again.

**It was put to the owner rather than taken.** That is the difference from `*.yaml`, where the pin
was written first and ratified afterwards
([[the-yaml-pin-was-written-before-the-owner-ratified-it]],
[[ask-before-weakening-or-working-around-a-rule]]).
