---
title: "The order of a refusal and its archive move rests on a written rule, and nothing mechanical enforces it"
type: concept
status: current
authority: refusal-archive-ordering
basis: code
sprint: S3
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md", "scripts/vault-archive.sh", "scripts/vault-check.sh"]
tags: [vault, harness, record-schema]
---

# What each half actually checks

**`scripts/vault-archive.sh:177` refuses a `status: refused` page that carries no `decided_by:`, and
it checks presence only.** Any value satisfies it.

**Rule 5c of `scripts/vault-check.sh` checks the type of the target** — that `decided_by:` names a
page whose `type` is `decision` — and it reads `sources` under `wiki/` alone. **So it binds only
while the page is still live**, and a refused proposal is in `archive/` by the time anyone would ask.

# So what forces the decision page to exist first is a sentence

**The written requirement is that `decided_by:` names *the decision that refused it*.** No script
checks *which* decision. A page could be released naming any decision at all, or naming the right one
written afterwards, and both halves above would pass.

**The order is a discipline the librarian keeps rather than a breach anything catches**
([[knowing-a-rule-is-not-a-mechanism]], [[a-conditional-requirement-is-refused-by-the-script-that-moves-the-page]]).

# Why the two checks are placed where they are, which is not a defect

**The presence check is in the script because the requirement is conditional on a status**, and no
per-folder schema can state a conditional — the same route `paths` under `render: whole` took
([[a-refused-proposal-is-archived-and-takes-status-refused]]).

**The type check is in the gate because that is where frontmatter is read.** Its blindness to
`archive/` is deliberate and general: nothing in `archive/` is checked, swept, or read by `/pre-task`
([[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]],
[[what-an-archived-page-asserts-is-frozen-and-how-it-is-found-is-live]]).

**The gap is the join between them**, and it is named here so that whoever performs a refusal knows
the order is theirs to get right.
