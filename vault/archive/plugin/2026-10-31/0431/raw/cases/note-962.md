# Note — Case 962 (C8, rule-work-mode backlog line)

## Questions
Round 1 (answered "Согласен" = agreed with each):
- **What happens to the open work of Work Mode?** — rec (a) note line in Backlog of live sprint entity-sprint-plugin — Answer: agreed, (a).
- **What happens to the second part of the Spec box?** — rec (a) back the same way as Q1 (note line) — Answer: agreed, (a).
Round 2 (sent):
- **How is it checked that the list keeps the open work?** — rec (a) new Estimate on rule-backlog, `estimate-backlog-keeps-the-work-taken-out-of-a-built-page`, by hand after the librarian's run, vault/wiki/backlog.md read; (b) new Estimate on entity-sprint-plugin (changes sprint DoD); (c) estimate-backlog-renders stands (made-up vault only, not on a changed page).

- Person asked (Fact): one-off or general? Answered: (a) is one-off on two data lines; the general behaviour (a note line stands whatever the page status, closed or live) is already tested by test_backlog.py test_a_line_of_a_closed_sprint_leaves_once_taken_or_finished (lines 240-275) and test_the_backlog_of_an_archived_sprint_page_stays_beside_the_live_one (209-237), under estimate-backlog-renders. Round 2 Q still unanswered.

## Read
- .guppi/tests/test_backlog.py lines 209-276
- case-schema.md, ratification.md; rule-work-mode.md whole (Purpose last sentence "not decided yet (case 479.2)" stays true)
- backlog.md; backlog.py whole; sprint.py item_slugs (note = no [[slug]] before first " — "), is_done, item_statuses
- rule-backlog.md Purpose; estimate-backlog-renders (Criterion covers note lines; method pytest made-up vault)
- entity-sprint-plugin.md whole (Backlog has rule-morph note case 802); its estimates: none on Backlog (one hit in ci-writes-a-clean-branch line 35, unread)
- archive entity-sprint-migration.md Backlog lines 30-32
- rule-spec-box line 21 sentence "Both wait for a second part (a line of the Backlog of entity-sprint-migration, case 591)" — stands (archived line still exists)
- case-959/960/961; brief.md Flags (guppi check 13 core-draft lines, rule-work-mode among them; rule-backlog built)
- tests grep: no test reads live entity-sprint-plugin/rule-spec-box/rule-work-mode/backlog.md (test_ship 872 to check)

- Round 2 answer: agreed, (a); one-time Estimate split is Frontier C9, not in this Case.

## Open forks
- none

## To do
- Case written to cases/case-962.md (single Case, no sub-cases); summary sent. Fix findings by Edit if the hook sends any.
- Pre-spec 1.8 fixed: then line 3 now "whatever the status of rule-work-mode and of rule-spec-box, built included" (matches purpose); method names backlog.md as repo file of evidence, read in the session whose brief puts it under Work. Do not read files of 956/959/960/961 (built in same send).
