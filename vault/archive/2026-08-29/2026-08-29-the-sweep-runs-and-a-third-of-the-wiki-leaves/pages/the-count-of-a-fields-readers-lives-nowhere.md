---
title: "The count of a field's readers lives nowhere, so an unmirrored parser stays invisible until a page exercises the difference"
type: lesson
status: archived
authority: field-reader-count
basis: code
sprint: S2
created: 2026-08-22
sources: ["archive/2026-08-22/2026-08-22-the-strike-lands-and-a-quote-gets-a-verdict/handoffs/2026-08-22-the-strike-lands-and-a-quote-gets-a-verdict.md", "scripts/vault-check-selftest.sh", "scripts/vault-inject.sh", "scripts/vault-check.sh"]
tags: [harness, testing, vault]
---

# What happened

**`governs:` learned an inline-list form on 2026-08-21.** The gate and `scripts/vault-inject.sh` were
both taught it, written from the same four rules and **deliberately not shared**, so that a writer
and its check cannot agree by sharing a bug
([[the-governs-list-is-expanded-at-the-walk-and-the-address-verdict-asks-membership]],
[[a-check-asks-by-running-the-writer-it-checks]]).

**There was a reader nobody counted.** The sandbox builder inside `scripts/vault-check-selftest.sh`
reads the same field with a scalar `sed`, and it was not touched.

**The first rule page in this corpus to govern two files handed it `[a/one.md, b/two.md]` as one
destination.** It materialised a file under that literal name, copied neither real destination, and
rule 12 went red in every case: **`caught 112, missed 44` against three real failures**
([[a-block-attributed-to-the-owner-is-written-in-his-own-russian]]).

# The cost the argument for separate parsers does not name

**Two implementations written from one set of rules beat one shared copy** — that is the corpus's
own position and it is not disturbed here. **What it is silent about is the third one.** Nothing
anywhere says how many readers a field has, so a parser that was never told about a change is
indistinguishable from one that does not exist, right up until a page exercises the difference.

**And the difference is exercised late by construction.** A syntax nothing in the corpus uses cannot
red anything; the first real customer of the list form arrived a day after the two intended readers
learned it ([[a-mechanisms-first-use-outside-its-home-is-where-it-drifts]],
[[the-fixture-corpus-goes-red-before-the-rule-it-was-never-written-for]]).

# Why the sandbox was the one that was missed

**It is a mirror in the places somebody remembered to mirror.** `.claude/` is copied one file deep —
`templates/handoff.md` — and everything else under it is either materialised from a `governs:` sweep
or faked as an empty placeholder. That held while every rule governed `CLAUDE.md` or a file the sweep
already found ([[the-selftest-sandbox-is-a-mirror-rather-than-a-renamed-copy]],
[[a-fixture-must-materialise-what-the-subject-reads]]).

**So the missed reader was inside the instrument rather than inside the subject**, which is the
position from which a defect looks like a suite going red for its own reasons
([[a-test-that-fails-for-its-own-reasons-proves-nothing]]).

# The repair is a list that is also a test

**The count of readers becomes a selftest case rather than a sentence on a page** — the shape the
owner ratified for the hook register on 2026-08-21, which paid for itself inside the same week
([[a-refusal-is-possible-on-pretooluse-alone-and-the-register-is-a-test]],
[[a-copied-list-drifts-and-a-sweep-cannot]]).

**A sentence saying *there are three* would be the next thing to drift**, and this corpus already
knows that a stated count drifts from the list it heads
([[a-stated-count-drifts-from-the-list-it-heads]],
[[a-rule-comparing-a-stated-count-against-its-list]]).

*(Compiled from `raw/handoffs/2026-08-22-the-strike-lands-and-a-quote-gets-a-verdict.md`.)*
