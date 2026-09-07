---
title: "A case that passes before its mechanism exists is proved by removing the guard, not by running it green"
type: lesson
status: archived
authority: pre-existing-green-case
basis: measurement
sprint: S3
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause/handoffs/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause.md", "scripts/hook-selftest.ps1", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, vault]
---

# The incident, and there were two of them in one session

**Two cases were green before the mechanisms they test existed** — the continuation guard in the
feedback catcher, and the `deferral` exemption in the narrowed `idea` verdict.

**Each was turned over by breaking the mechanism deliberately.** Making the parser eager tore an
indented `note:` into a record of its own and filed it as `unknown:`. Making the exemption match
nothing reddened the page the exemption exists to spare.

**Neither case would have been worth anything without that step.**

# Why a green case is not evidence

**A case that passes before the change passes for a reason nobody has established.** It may be
testing the mechanism, or it may be testing something the tree happens to satisfy — the vacuous pass
this store keeps meeting ([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]],
[[a-verdict-that-cannot-fire-is-worse-than-no-verdict]]).

# The procedure

**Break the mechanism in the sandbox, watch the case go red, restore it.** That is the same
procedure a new verdict is proved by, and it is cheap while the change is in front of you
([[a-new-verdict-is-proved-in-the-real-tree-because-the-check-cannot-see-a-sandbox]]).

# The neighbouring failure: a case red against a correct mechanism

**The same suite reported a miss against something already right**, because the assertion was
anchored at end-of-line in a CRLF file
([[an-assertion-anchored-at-end-of-line-fails-against-platform-newlines]]). **The two are the same
question asked from opposite sides** — is the case about the mechanism, or about something else the
tree happens to do.
