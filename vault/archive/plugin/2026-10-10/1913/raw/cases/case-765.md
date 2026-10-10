## Case 765 — The README check names its moment

> **context:**
> `estimate-sprint-plugin-readme-describes-the-project`, one of the five Estimates of `entity-sprint-plugin` (case 756.3), asks the person whether `README.md` says what GUPPI is, names its main parts and says how to install and use it. Its `method` reads "by hand, the person's answer on README.md, in a session of the sprint plugin before its close". Each session of the sprint is such a session, so `/hi` takes the reading as due at every opening. The README is not written yet: `README.md` still opens with the heading `# Vault harness`, and the README is a line of the milestone The plugin, the last of the page. So `/hi` of this session could not run the reading and wrote it as line C7 of the Frontier (case 670.6), and it would do so again at each opening until that milestone. The `purpose` and the Criterion of the page are sound and stand: they check what the README says, not when it is read. This Case changes only the `method`, so that it names the moment of the reading: the `/hi` of the session after the one whose Work Mode writes `README.md` under the milestone The plugin, before the close of the sprint. The first build named the Retro of the session that writes the README; pre-spec found that `rule-retro` does not let Retro take it, since `/retro` reads "A reading whose `method` names the person's word is not yours to take: it is a line of `## Ask the person` of `handoff.md`" and its reply "asks the person nothing (case 569.1)". So the Retro of the session that writes the README puts the check under `## Ask the person` of its handoff, the brief carries it into `Ask the person` of Next session, and `/hi` of the next session puts the question to the person. Case 764 of this batch sets what the brief, `/hi` and `/retro` do with a check of the live sprint page before its moment, and this Case does not cover that moment. Its file, as read at this build, keeps under 764.1 every reading of the live sprint page out of `Ask the person` of Next session; the person's answer on the pre-spec report rebuilds Case 764 so that 764.1 lets in a check of the live sprint page whose work is finished, and this Case rests on that change. This Case adds no Estimate: a `set` of the `method` alone leaves the Criterion and the status of the page as they stand (case 378.4), and what checks that the moment is kept is the rule of Case 764, through the Estimates whose Criteria it replaces. The new `method` names the person, so `lint.waits_for_another_session` of `guppi/lint.py`, which `pre-spec` runs over the plan, does not report it. A Grep `estimate-sprint-plugin-readme-describes-the-project` over `vault/wiki/` printed `vault/wiki/brief.md`, `vault/wiki/log.md` and `vault/wiki/entities/entity-sprint-plugin.md`; the brief and the log are not read, and the page lists the Estimate in `estimates` and in History only, and its Purpose, that each Estimate of the page is read before the close of the sprint, stays true. A Grep `sprint-plugin|readme` over `tests/` printed nothing, so no test reads this page live.

> **problem:**
> The `method` of the README check names no moment closer than any session of the sprint before its close, so each opening of the sprint takes as due a reading that cannot run until the README is written.

> **recommend:**
> - **What does this Case change on the README check?**
>   - Recommended: (a) name the moment in the method: the person reads `README.md` in the session of the sprint plugin that writes the README of the last milestone, before the close; the Criterion and the purpose stay.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: pre-spec found that Retro cannot take the person's answer, since Retro asks the person nothing; the person took its recommended fix: the answer is taken at the `/hi` of the session after the one whose Work Mode writes `README.md`, where the Retro of that session puts the check under `## Ask the person` of the handoff and the brief carries it into `Ask the person`.
>   - Taken: the `method` names the `/hi` of the session after the one that writes `README.md`, before the close of the sprint; Case 764 is rebuilt so that the brief lets in such a check.

> **given:**
> `estimate-sprint-plugin-readme-describes-the-project`: the README check, whose `method` changes.
> **＋** `entity-sprint-plugin`: the sprint page, whose milestone The plugin holds the README line.
> **＋** `README.md`: the description of the project at the root of the repository.
> **＋** `rule-retro`: Retro, which puts a reading that needs the person's word under `## Ask the person` of the handoff.
> **＋** `/hi`: the skill that puts the questions of `Ask the person` to the person.
> **＋** `vault/raw/2026-10-10/1913/cases/case-764.md`: the rule of this batch for the checks of a sprint page that wait for their moment.

> **when:**
> In a session of the sprint `plugin`, the agent reads the `method` of `estimate-sprint-plugin-readme-describes-the-project` to judge whether its reading is due.

> **then:**
> The `method` names the moment of the reading: the `/hi` of the session after the one whose Work Mode writes `README.md` under the milestone The plugin of `entity-sprint-plugin`, before the close of the sprint.
> **＋** The reading is the person's answer on `README.md`, by hand, to the question that the Retro of `rule-retro` in the session that writes `README.md` puts under `## Ask the person` of its handoff.
> **－** The Criterion and the `purpose` of `estimate-sprint-plugin-readme-describes-the-project` do not change.

> **tasks:**
> - [ ] update `estimate-sprint-plugin-readme-describes-the-project`
>   - set:
>     ```
>     method: by hand, the person's answer on README.md at the /hi of the session after the one whose Work Mode writes README.md under the milestone The plugin, before the close of the sprint
>     ```
>   - change: `the method names the moment of the reading: the /hi of the session after the one that writes the README`

> **ratification:**
> ```
> - decision[case 765][update][estimate-sprint-plugin-readme-describes-the-project]{ref:entity-sprint-plugin}
> ```
