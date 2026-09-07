---
title: "The collection frame is checked against the stored location string, not against the site's current one"
type: decision
status: current
authority: frame-source-of-truth
binding: prohibition
basis: code
sprint: S0
decided: 2026-08-06
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [deactivation, data]
---

# The frame is checked against what we stored

If a vacancy left the frame because of an edit on the site, a miss is counted against it — we
judge it by the location we have, not the one it now has.

**Damage is low: the profile no longer wants it anyway.** Accepting that is cheaper than re-fetching
every candidate to confirm it still matches.

See [[deactivation-cycle]] for the condition this feeds, and [[collection-frame-city-check]] for
how the stored string is interpreted.
