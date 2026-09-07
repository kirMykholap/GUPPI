---
title: "The unrun migration tests are named S4 work rather than left against a condition that never arrives"
type: decision
status: current
authority: migration-test-debt-sprint
binding: deferral
basis: human
sprint: S3
decided: 2026-08-26
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md", "tests/integration/test_migrations.py"]
tags: [testing, process, db-schema]
---

# The ruling, 2026-08-26

*(the owner selected it, against keeping the debt filed under "when Docker is up".)*

**The fourteen unrun migration tests become S4 work with a name**, rather than a debt waiting on a
condition.

**The condition cannot arrive inside S3 by construction.** Product work does not interleave into a
vault sprint ([[product-work-does-not-interleave-into-the-vault-sprint]]), so nothing inside S3 will
ever be the occasion to bring Docker up — the debt would sit against a trigger the sprint forbids.

**Measured 2026-08-26:** `docker info` does not find the `dockerDesktopLinuxEngine` named pipe.
**The condition has not arrived once since 2026-08-20** ([[docker-desktop]]).

# Rejected

**Rejected: keeping the deferral as it stood.** A deferral repeated again names the sprint it happens
in, or it is refused ([[a-repeated-deferral-names-the-sprint-it-happens-in-or-is-refused]]) — this is
that rule applied rather than a new one.

**Rejected: running them now.** The suite hangs rather than failing when the database is down
([[the-integration-suite-hangs-rather-than-failing-when-docker-is-down]]), and bringing the database
up is product work.

# The occasion arrived and the fourteen ran — 2026-08-27

**All fourteen pass.** `uv run pytest tests/integration/test_migrations.py -q` → **14 passed, exit 0,
45.78 s**, taken on 2026-08-27 with the database up. They sit inside the full suite's 614, which ran
the same day — **`make test` → 614 passed, exit 0, 133 s**, nothing skipped and nothing errored — and
were run separately only to answer whether they were reached.

**The occasion this page says cannot arrive inside S3 arrived on the sprint's next working day.**
Item 30 of `sprint.md` — `make test` as the next session's first work — is what brought the database
up, and that item and this page were settled on the same day, 2026-08-26, on the owner's ruling in
both cases. **Neither cites the other.** That is the finding: two live records disagreed about
whether the database would come up inside S3, and nothing could see it. Item 30 is struck on
`sprint.md` as of today and carries this reading
([[an-answered-item-leaves-the-next-list-by-being-struck-in-place]]).

**What is discharged is the second rejected alternative above.** *"Rejected: running them now"* is
overtaken — they ran, and they pass. The clause is left standing where it is rather than edited
([[the-date-of-a-correction-note-is-the-date-the-text-became-false]]).

**What is not discharged is the owner's reading and not mine.** Whether the rest of what this page
assigns to S4 moves with that clause, and whether the deferral stands at all now that its stated
occasion has happened, is his call. I record that the clause is overtaken and take nothing further
([[product-work-does-not-interleave-into-the-vault-sprint]] is untouched by this section).

**How the disagreement was found: by `/pre-task` on 2026-08-27, checking a plan** ([[the-pre-task-agent]]).
No instrument found it and none could. **Nothing compares two `decisions/` pages for a disagreement
when they hold different `authority:` slugs** — rule 3 of the gate compares `current` pages sharing a
slug, and the CONTRADICTION marking is defined over a shared slug too. That is the same shape as the
CRLF pair the brief carries in prose ([[the-vault-crlf-files-are-renormalised-and-no-rule-is-written-for-them]],
[[a-cr-byte-census-of-the-working-copy-behind-lint]]). Here it is one step worse: item 30 lives on
`sprint.md` and carries no frontmatter at all, so there is no slug to compare even in principle.
