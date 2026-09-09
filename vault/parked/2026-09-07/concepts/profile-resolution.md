---
title: "The selected profile lives in a cookie, so navigation links and saved links are not portable"
type: concept
status: current
authority: profile-selection
basis: code
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [web, profile]
---

# The selected profile lives in a cookie, not in the address

`resolve_profile` takes the profile from the address, then from the `jobhunt-profile` cookie, then
the earliest one.

Navigation links are bare `/vacancies` and `/collection` with no parameters, so **moving between
pages rests on the cookie alone**. A browser without it — incognito, another machine — opens the
earliest profile rather than the selected one.

A saved link from «Вакансии» carries `profile=` **only if the profile came from the address**:
`_page_url` puts it into `HX-Push-Url` in that case only, because a profile from a cookie is the
browser's memory rather than the user's choice. And only the profile selector can put it into the
address — and that selector is rendered only when there is **more than one** profile
(`_nav.html`).

**With a single profile, which is the ordinary case today, a saved link carries no `profile=` and
is not portable.** The wording here said "carries it and is therefore portable", unconditionally,
until 2026-08-06.

This is deliberate: a cookie is one browser's memory, and the address must not carry what the user
did not choose. Verified live — see the slice 3 walk, scenario 1.

One thing the schema does not guarantee about a profile: [[profile-name-not-unique]].
