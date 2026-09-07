---
title: "A test that is green under any implementation is worse than no test, and only removal proves otherwise"
type: lesson
status: archived
authority: test-evidential-power
basis: measurement
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md", "archive/2026-08-13/2026-08-13-second-brain-phase-2/handoffs/2026-08-13-second-brain-phase-2.md", "scripts/vault-check-selftest.sh"]
tags: [testing, process]
---

# A test green under any implementation is worse than none

It costs what a real test costs, and it buys nothing — while looking like coverage. This project
has met it **at least four times**, in four different disguises:

- **the deactivation guards, twice.** An edit created the pair without a link, so a newer condition
  filtered it out *before* the guard under test could fire. The tests passed for an unrelated
  reason. See [[deactivation-cycle]].
- **four chip tests.** Without the `tags_set` marker `tag_ids` was ignored, so each had silently
  become a test of the enabled-tag predicate instead of the chip set. See [[tags-set-marker]].
- **multi-session made them lie.** After `run_profile` moved to a session factory, tests that read
  state through their own session got a cached object and were green under any implementation.
  Cured by an explicit `session.expire_all()`.
- **the collection indicator hung on one value with no test at all.** Flip `"page": "vacancies"`
  in the fragment route's context and the whole suite stays green while the indicator goes blank
  mid-run. The only request to that route used a *finished* batch, so the running response — the
  one the feature **is** — was never rendered.

- **nothing fetched `/static/`.** The whole suite stayed green if the static mount was removed, the
  directory renamed, or a file dropped from the image — and every page then rendered completely
  unstyled. Closed on 2026-08-12 by **three** assertions, and three because the guarantee has two
  halves: `tests/integration/test_web_static.py` holds that `/static/app.css` and
  `/static/htmx.min.js` each answer 200, and `test_both_pages_link_the_stylesheet` holds that the
  document asks for the stylesheet at all. **A served file nobody links is as unstyled as a missing
  one.** See [[the-palette-grows-into-a-design-system]].

## The remedy

**Prove the test by removing the guard, not by running it green.** Take out the protection it
claims to check; if it still passes, it was never checking it.

Two sharper forms of the same trick:

- **a check run against a file that is already clean proves nothing.** The test that
  `renormalize` does not become "permitted to everyone" called the same function on the same file
  as a neighbouring test that the file already bypasses — the exception could have been widened
  without failing anything. Cured by a **synthetic** source: text and path handed to the check
  rather than read from disk. That technique fits any boundary phrased as "what would happen if
  someone wrote this".
- **replacing a test file wholesale carries regressions off with it.** It happened three times;
  once it hid a defect for four tasks. Compare the old coverage with the new before replacing, and
  restore anything without a successor.

## The vacuum failure mode lives on a suite's negative half

Recorded 2026-08-13, from `scripts/vault-check-selftest.sh` ([[vault-scripts]]). A suite that
mutates a subject and asserts an outcome has a way of testing **nothing at all**: reshape what it
mutates, and the mutation stops applying. **A `sed` that matches nothing leaves a tree that is
clean by construction**, and a case asserting *nothing happens* then passes for the emptiest
possible reason.

It bit three cases at once when the corpus was reshaped, and **all three were on the negative half**
— the cases that assert the check stays green. That is where it will bite again: a positive case
goes red when its mutation stops working, and a negative one goes quiet.

Two guards, and they are cheap:

- **assert that the mutation changed the tree at all** — `diff -rq` against a pristine copy, run
  before the thing under test;
- **pick the subject by what the case needs**, never by sort order or by "the first page in the
  folder". A subject chosen by position is a subject that changes when the corpus does.

This is the same failure as *"a check run against a file that is already clean proves nothing"*
above, one level up: there the input was vacuous, here the *mutation* is.

See [[an-example-inside-a-code-block-satisfies-a-search]] for the text-matching variant.
