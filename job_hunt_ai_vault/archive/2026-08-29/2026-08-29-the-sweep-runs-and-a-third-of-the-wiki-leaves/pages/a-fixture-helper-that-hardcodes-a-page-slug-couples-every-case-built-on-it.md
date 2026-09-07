---
title: "A fixture helper that hardcodes a page slug couples every case built on it"
type: lesson
status: archived
authority: fixture-slug-coupling
basis: code
sprint: S3
created: 2026-08-23
sources: ["archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md", "scripts/vault-check-selftest.sh"]
tags: [testing, harness, vault]
---

# The coupling, read off the suite on 2026-08-23

**`plant_rule_page` writes `decided_by: [[a-refused-proposal-is-archived-and-takes-status-refused]]`
into every rule page it plants**, because the field became required in `wiki/rules/` that day and a
planted page without it is red for the wrong reason
([[decided-by-is-legal-in-proposals-and-rules-and-required-in-rules]]).

**Forty-three cases stand on that helper.** Renaming or retiring that one page reddens all of them
at once, for a reason not one of them is about — and the report would name forty-three unrelated
rules.

# Why nothing would warn you

**The coupling is invisible from the page's end.** Nothing in
[[a-refused-proposal-is-archived-and-takes-status-refused]] says a test suite depends on its
filename, and the link sweep does not read the selftest: a rename is `sed` over `wiki/` and
`archive/`, and the suite is neither
([[a-page-rename-is-sed-and-verify]], [[log-md-is-outside-the-link-set-the-check-reads]]).

**And a rename here is cheap and encouraged**, which is what makes the trap live rather than
theoretical: this corpus renames pages when a title stops being true, and it has already done six in
one sweep.

# The safe shape

**A fixture plants what it needs, including the page it points at.** A helper that needs a decision
page should write one into its own sandbox rather than borrow a real slug — the sandbox is the
suite's own fixture and never reaches into the corpus for a file, which is a property this suite
already has and this helper broke
([[the-selftest-works-in-its-own-fixture-and-never-in-the-corpus]],
[[a-fixture-must-materialise-what-the-subject-reads]]).

**The wider rule: a test may not name a corpus artefact it does not create.** A fixture that renames
or borrows what the corpus names by name stops being a fixture of anything
([[a-fixture-that-renames-what-the-corpus-names-stops-being-a-fixture-of-it]]).
