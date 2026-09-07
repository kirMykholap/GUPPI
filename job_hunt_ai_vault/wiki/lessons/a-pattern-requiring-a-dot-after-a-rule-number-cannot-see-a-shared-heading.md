---
title: "A pattern requiring a dot after a rule number cannot see a heading shared by more than one rule"
type: lesson
status: current
authority: shared-rule-heading
basis: measurement
sprint: S3
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause/handoffs/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause.md", "scripts/vault-check.sh"]
tags: [harness, vault, testing]
---

# The incident

**An approved plan asserted that two rules of the gate carried no heading, and they share one.**
`scripts/vault-check.sh:565` reads `# 4 and 5. Links resolve, and no page is an orphan.` The grep
behind the claim required a digit followed by a dot, so a heading naming two numbers was invisible
to it.

**The register has fifteen headings where the plan counted fourteen**, and the script explains the
sharing on the very next line: two questions over one set, built once, because asking them per page
cost seventy-one seconds at seventy-five pages.

# Why it matters beyond the number

**The plan's conclusion was that a rule register could not be swept until those two were marked
up.** It could, and the work the plan scoped for that never needed doing.

**A pattern is a claim about the shape of what it reads**, and this one asserted that a rule heading
names exactly one rule. Nothing in the file promised that.

# The family it belongs to

**A grep's negative result is evidence about the grep as much as about the file**
([[an-example-inside-a-code-block-satisfies-a-search]],
[[a-grep-that-prints-one-line-is-a-report-about-the-first-match-and-not-a-count]]). The safe move is
to read what did match and ask what shape it assumed.
