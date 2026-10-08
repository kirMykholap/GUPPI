---
name: sprint-open
description: "Open the next sprint. Run it when the hook on /hi says that no sprint is open, or when the person types /sprint-open."
---

No sprint is open: the first heading of `vault/wiki/sprint.md` marks the last sprint closed. This session opens the next one. The ledger hook refuses each decision line but a `defer` until a `create` of a page `entity-sprint-<id>` stands, so the opening Case is the first Case the session ratifies.

1. Assemble the Frontier as `/hi` sets it: the line `open the next sprint` of the brief stands first under `## Cases`, and no item of the closed sprint and no conserved Spec stands there.
2. When the person takes up that line, dispatch `case-guppi` for it as `vault/wiki/orchestration.md` sets it, and write into the prompt of the call that the opening Case asks the person, in its rounds:
   - the id of the sprint, which names the page `entity-sprint-<id>`;
   - its goal in one sentence, the `purpose` and the `## Purpose` of the page;
   - its Definition of done, one Estimate per condition, which the page lists in `estimates`;
   - the first milestone and its items, under `## Milestones`;
   - whether to take any item of `vault/wiki/backlog.md` into the sprint: the Case says how many items the file holds, and goes through no item the person does not name.
3. Write into the same prompt that the opening Case writes, as the last item of the last milestone of the page, the line ``- the close of `<id>` — `/sprint-close`, a session of its own``, so that the session that closes the sprint starts `/sprint-close` from it.
4. The skill decides none of the answers: `case-guppi` puts each to the person, and the person ratifies the opening Case as any other.
