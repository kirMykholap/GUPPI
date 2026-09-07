---
title: "A rule with no instrument behind it is a rule a fixture can violate for a week"
type: lesson
status: current
authority: uninstrumented-rule-fixture
basis: code
sprint: S3
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md", "scripts/vault-check-selftest.sh"]
tags: [testing, vault, harness]
---

# What happened

**The selftest's archive fixture planted a `status: deprecated` page carrying no `superseded_by:`**,
and had done since 2026-08-22. **It passed, because nothing read the field.**

**The successor check built on 2026-08-29 reads it. The fixture went red and the fixture was
repaired** — not the check
([[a-deprecated-page-needs-a-live-successor-named-in-superseded-by-before-it-may-leave]]).

**So the corpus's supersession rule had no instrument behind it until that day**, though it has been
written in the vault's own `CLAUDE.md` since the store was built and has been obeyed by every page a
librarian retired.

# Why a fixture is the worst place for it to happen

**A fixture is written to be minimal**, so it carries exactly the fields the check under test reads —
which means it will violate every rule nothing reads, by construction and without anyone deciding to.

**And a fixture is trusted.** A green suite that runs against a corpus violating a rule is evidence
*for* the rule being satisfied, in the reading a person actually does
([[a-test-can-be-green-on-placeholders-its-own-setup-created]],
[[a-clean-case-built-on-a-helper-that-plants-a-red-tree-can-never-be-green]]).

# The rule

**The first instrument for a rule is also the first honest reading of whether it was ever obeyed**, and
it should be expected to go red. When it does, the fixture is the suspect before the check is
([[a-case-green-before-its-mechanism-is-proved-by-removing-the-guard]]).

**Where a rule cannot get an instrument, that is the thing to write down** — which is the whole shape
of S3's first acceptance criterion.

# A second instance, 2026-08-30: a status value that obliges a page to leave, and nothing that notices it has not

**`status: repealed` was minted without joining the gate's `retired` verdict.** So a cancelled page
could have sat in `wiki/` indefinitely with **every check green** — the value said *leave* and no
instrument read it ([[a-cancelled-page-takes-a-status-of-its-own]]).

**It is the same shape as this page's own incident and one step worse.** A rule with no instrument is
violated and nobody notices; a **value** with no instrument is violated **by the mechanism's own
design**, because the value's whole job is to be read by something.

**Caught while writing the selftest fixture** — not by the plan and not by `/pre-task` — and **closed
the same turn**. The `retired` verdict now knows three marks and gives each its own sentence, because
naming the wrong one sends a reader to write a `superseded_by:` that the archiver would refuse.

**The generalisation this instance adds**: when a schema mints a value, the question is not only
*what does it mean* but *which reader changes behaviour on it*. A value nothing reads is a comment
with a colon in it.

# A third instance, and it names the moment rather than the disposition — 2026-08-30

**A new obligatory section reddened the suite's own fixtures and nobody looked.** Making
`# The rule text` mandatory for a decision carrying `target_kind: rule` broke one of the two fixtures
in `scripts/vault-check-selftest.sh` that carry that value. **The check that would have found it costs
one grep and was not run.**

**What is stronger than the disposition already on this page.** *"When it does, the fixture is the
suspect before the check is"* is advice for a reader looking at a red suite. **This says when to
look**: the moment an obligation is minted, before anything is red, by grepping the suite for the
value the obligation is scoped to. There were two fixtures carrying it, and finding them was one
command.

**And the same day produced a second value with no reader**, which is this page's own subject:
`render: authority` was minted with a gate that branches on it in three places and a hook that has no
branch to deliver it — so it fails the test its own schema comment asserts it passes
([[the-hooks-authority-branch-is-not-written-and-the-read-matcher-is-downstream]],
[[a-rule-under-render-authority-is-written-into-no-file-and-found-by-its-slug]]).

*(Extended 2026-08-30 from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`, and extended from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
