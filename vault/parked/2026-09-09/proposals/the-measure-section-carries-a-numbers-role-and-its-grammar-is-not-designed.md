---
title: "The marked section a measurement lives in, with its grammar and its build deliberately not designed"
type: proposal
status: current
authority: measure-section-design
basis: human
sprint: S3
created: 2026-08-24
decided_by: [[the-measure-section-is-a-marked-region-legal-in-any-folder-and-required-nowhere]]
sources: ["archive/2026-08-24/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause/handoffs/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause.md", "scripts/vault-inject.sh", "scripts/vault-check.sh"]
tags: [vault, record-schema, harness]
---

# What is decided, and it is only the shape

**A marked section in the body — an opening `measure` comment and its closing partner — legal in any
folder, required nowhere, with no frontmatter flag beside it.** That is the owner's selection and it
is settled ([[the-measure-section-is-a-marked-region-legal-in-any-folder-and-required-nowhere]]).

# The ground it rests on, which is what makes the section necessary at all

**A number here is one of two things and they behave differently**
([[a-measurement-is-testimony-or-a-gauge-and-the-role-decides-where-it-lives]]):

- **testimony** — evidence for a claim. It lives with that claim, in any folder, and **never
  mutates**, because the claim was made against it.
- **a gauge** — an answer to *how much now*. It has one true value at a time and **mutates**, and it
  lands on an entity page as a consequence of what it is.

**A section that cannot tell those apart is a section that lets a gauge be edited into testimony**,
which is how a page ends up asserting that a claim was made against a number nobody measured
([[a-page-that-says-measured-can-carry-a-figure-nobody-measured]]).

# What is not designed, listed so nobody mistakes this page for a specification

- **The grammar inside the markers.** What a line must carry — the number, its conditions, its date,
  its subject — and whether a gauge is spelled differently from testimony.
- **How a gauge is addressed** so the uniqueness check has something to compare
  ([[a-gauge-is-checked-for-uniqueness-and-the-check-waits-for-subjects]]).
- **The build.** Which script writes the region, which rule checks both ends, and whether the
  injector is the writer.

**The grammar has to be checked against the numbers already written across the corpus**, which is
reading rather than design, and that is why it is a session of its own rather than an hour.

# What it would cost, and what makes it cheap

**It is a second customer of an existing mechanic.** The text slice on a rule page is already a
machine-read region inside a body, with a writer and a rule checking both ends
([[wiki-rules-holds-the-rules-of-the-repository-claude-md]],
[[a-check-asks-by-running-the-writer-it-checks]]). Nothing has to be invented to find a region or to
verify it.

# What it obliges while it waits

**Every `measure:` line written from 2026-08-24 names a destination and has nowhere structured to
land** ([[a-measure-line-names-its-destination-in-brackets-after-the-kind]]). The destinations
accumulate as prose in `log.md` until this is built.

# The grammar half was decided on 2026-08-25, and this page's title now runs behind its body

**The title above says the grammar is not designed. That stopped being true on 2026-08-25**, and the
title is left as it stands rather than patched, dated to the day it was written
([[the-region-coverage-figure-is-dated-where-it-stands]]).

**What was decided**: one line per number, opening with the role; a gauge line names the command that
prints it and carries no value; the check rides the gate's existing shared pass
([[the-measure-section-grammar-is-one-line-per-number]]).

**What was decided about the writer**: a script takes the page and the subject, runs the command and
writes the number, and a refresh pass walks every region
([[a-gauge-is-written-by-a-script-that-runs-the-command]]). **The design that remains open is on a
page of its own** ([[the-measure-writer-script-and-what-it-refuses-to-do]]).

**Nothing was built**, so this proposal is not implemented and does not move.
