---
title: "A verdict that cannot fire is worse than no verdict, and this one survived a design pass, an approval and a proposal page"
type: lesson
status: archived
authority: unreachable-verdict
basis: code
sprint: S2
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind/handoffs/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind.md", "scripts/vault-check.sh"]
tags: [testing, harness, vault]
---

# The incident

**A red verdict was designed, approved and specified, and it could never have fired.** *A marker
whose type disagrees with its page's `type:`* — the type word picks the folder, and rule 2 already
requires every page in a folder to carry that folder's singular. The disagreement it hunts is rule 2
failing on that page.

**Nobody asked *when could this fire* until the build.** It passed a full design pass, an owner's
approval and a written proposal page first
([[the-marker-carries-a-type-and-governs-is-read-as-a-field]]). It was caught at `/pre-task`,
reading the code ([[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]]).

# Why it is worse than not having it

**A check that can only fire as a second report of somebody else's failure is a green that examined
nothing.** It costs a selftest case, it costs check time, and — the expensive part — it makes the
gate *look* like it covers a class it does not. The next person reasoning about coverage counts it.

This is the project's most-recorded failure shape, met here inside a check rather than by one
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]],
[[a-gate-guarantees-agreement-never-truth]]).

# The question to ask of any new verdict

> **Name an input that makes this fire and nothing else fire.**

If the only such input is already caught by an existing rule, the verdict is a second report and not
a check. **The replacement passes that test**: where a marker's slug exists under a *different*
type, the red names the folder the page is actually in — a wrong address that still resolves, which
is the class the fifth verdict exists for at the file level
([[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]],
[[the-unreachable-verdict-is-dropped-and-replaced]]).

**The near-miss is the sibling of a test that passes with the code reverted**
([[a-test-built-from-a-specification-can-pass-without-the-code]],
[[reverting-the-code-tells-you-whether-a-test-tests-anything]]): both are green for a reason
unrelated to the claim.
