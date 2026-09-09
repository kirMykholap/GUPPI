---
title: "A `wiki/rules/` page leaves only on a decision saying so and a `deprecated` mark"
type: decision
status: archived
authority: rules-archival-criterion
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-29
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md", "wiki/rules/_schema.yaml", "scripts/vault-archive.sh"]
tags: [vault, record-schema, process]
---

# The ruling, 2026-08-29

**owner:** «страницы в rules/ попадают под архивацию только если есть решение, которое говорит об этом,
а само правило при этом помечено как refused или deprecated»

**He corrected himself the next turn: `refused` is not to be minted in `rules/`, and the status values
there stay as they are.**

**So the criterion is: a decision saying the rule is overturned, *and* the rule marked `deprecated`.**
Both, not either.

**Rejected: minting `refused` in `wiki/rules/`**, which he withdrew himself; and **either half alone** —
a decision with the rule still live means the rule is still rendering, and a `deprecated` rule with no
decision behind it is a rule somebody retired without anyone ruling on it.

# Why a rule needs both where other folders need one

**A rule's text is rendered into a file that instructs an agent.** Archiving it removes text from
`CLAUDE.md` or a skill, which is a change to what every session is told — so the mark alone is not
enough, and the decision is what makes the removal reviewable
([[governs-is-a-property-of-wiki-rules-alone]], [[a-deprecated-rule-does-not-render]]).

**It is the strictest of the four folder criteria** and it selected **zero** pages on the first sweep,
which is the expected reading rather than a fault
([[the-sweep-runs-for-real-over-every-criterion-and-records-what-it-moved]]).

# The schema paragraph this was found against

**`wiki/rules/_schema.yaml` carries a folder-specific archival criterion — `deprecated` plus a decision
behind the overturn — that names no decision page.** That is against the schema's own header rule, which
requires a field or a criterion to name the page the decision is written on, and it is the only
folder-specific archival paragraph of the six.

**It was surfaced by `/pre-task` against plan decision 10.** **This page is the decision it was
missing**, and the schema's paragraph may now cite it.

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*

# A repeal needs no field of its own, and the mechanism above is the general one — 2026-08-29

**owner:** «Для отмены нужно решение, которое об этом говорит. Решения пишем мы в процессе сессии,
бибилотекарь смотрит что такое решение есть и подписано человеком - инициализирует отмену.»

**The repeal decision *is* the mark.** A session writes the decision saying the thing is overturned;
the librarian sees a human-signed decision that says so and initiates the supersession. **Rejected: a
new field marking a repeal**, and with it the archiver-side repeal check that would have read it.

**This page's own rule is that mechanism, scoped to `wiki/rules/`** — a decision saying the rule is
overturned **and** the page marked `deprecated`, both and not either. **The ruling generalises it**, and
the generalisation is recorded here rather than on a page of its own.

**The worked instance is live and is not a rules page.**
[[the-authority-register-step-is-repealed-and-an-archived-page-keeps-its-slug]] carries `supersedes:`,
its predecessor is `deprecated` in `archive/`, and the successor carries the new claim. **So repeal by
supersession is already running; what was missing was anybody saying it is the general rule.**

**Rejected in the same turn: the owner's own suggestion** that a concept page about `authority:` carry
the mention of the repeal — it would put one fact in two places.

## The consequence he has not ruled on

**Nothing catches a repeal the librarian did not act on.** Between the moment a repeal is decided and
the moment the supersession is performed, the repealed page is `current` and every check is green on
it: the gate asks for a successor only on `deprecated`, and the archiver's refusal fires only at move
time.

**That window was open for hours on 2026-08-29** — `retiring-a-page-removes-its-slug-from-the-authority-register`
was false and live, and a `/pre-task` in that window would have returned it as a standing prohibition.
**The session named the gap and the owner has not answered it.**

# Reversed in one section on 2026-08-30, and the page's own rule stands

**This page's primary rule is untouched**: a `wiki/rules/` page leaves only on a decision saying so
and a `deprecated` mark. It is not retired and nothing above it is struck.

**What is reversed is the section rejecting a field.** That section says *"Rejected: a new field
marking a repeal, and with it the archiver-side repeal check that would have read it"*, and on
2026-08-30 the owner minted **exactly that field** — `target_kind: repeal`
([[a-decision-declares-its-target-and-the-handshake-closes-it]]) — **and the status value the archiver
reads** ([[a-cancelled-page-takes-a-status-of-its-own]]).

**He reversed the supersession half explicitly and ratified both mints knowingly**, in the same
session: «Вчерашнее решение, что отмена записывается через supersession - неверная». **So this is a
reversal, not a collision**, and it is written here because otherwise the rejection reads as standing.

**The window this page names as unruled is now closed** by the `repealed` status, which gives a
cancelled page a release route of its own without weakening the `deprecated` refusal.

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`, corrected 2026-08-30 from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
