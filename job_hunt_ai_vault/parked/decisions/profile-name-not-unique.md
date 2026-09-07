---
title: "Profile.name is not unique in the schema, only in the CLI"
type: decision
status: current
authority: profile-name-uniqueness
binding: prohibition
basis: code
sprint: S0
decided: 2026-08-06
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md", "src/jobhunt/db/models.py"]
tags: [profile, data, db-schema]
---

# `Profile.name` is not unique in the schema

The CLI refuses a duplicate, but that is an **application check**, not a constraint. A row created
before that check existed, or outside the CLI, resolves silently to the first profile.

Theoretical with one user, which is why it is recorded rather than fixed. It stops being
theoretical the moment a second profile exists — and so does
[[politeness-is-per-process]]. See [[profile-resolution]] for how one gets chosen per request.
