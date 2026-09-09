---
title: "The missing decision pages behind the empty `decided_by:` fields are written by the nearest `/ingest`"
type: decision
status: archived
authority: missing-decision-compilation
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-24
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause/handoffs/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause.md", "archive/2026-08-21/2026-08-21-a-claim-is-looked-up-before-a-page-is-written/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md"]
tags: [vault, process, record-schema]
---

# The ruling, 2026-08-24

> **owner:** «написать их»

and, on who writes them,

> **owner:** «согласен»

**Writing them is compiling a journal, so it is the ingest's work and not a separate dispatch.** The
rulings exist in the journals; what is missing is the page, which is exactly what an ingest produces.

**Rejected: a session dispatching an agent to back-fill them.** That is the shape that had just cost
two dispatches and most of an hour for the `decided_by:` fill itself, and it would have re-read
journals the ingest reads anyway.

# What was missing, and where it came from

**Rulings taken and never compiled leave a proposal with nothing to name.** The journal of
2026-08-21 is the clearest case: its `Deferred` section produced several proposal pages and exactly
one `decisions/` page.

**And the fields then close without a second pass over the proposals**, because the ingest writing
the decision is the ingest that can fill the field.

# Corrected at the ingest of 2026-08-24, and the correction is small

**The journal says four of the six missing causes come from the session of 2026-08-21. Three do.**
Read off the proposals' own `sources:` lines: three name that journal, one names 2026-08-20 and two
name 2026-08-23. The claim was a count stated in a report and not checked against its own list,
which is the defect the same journal records twice elsewhere
([[a-count-in-a-report-about-a-ritual-was-not-checked-against-the-rituals-own-list]]).
