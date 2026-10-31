## Case 952 — The opening Case offers no sprint goal made up from the vault

> **context:**
> `/sprint-open` tells the opening Case of a sprint to ask the person for the goal of the sprint in one sentence, but not how. `case-guppi` then offers goals it made up from the vault. In a new project the vault knows nothing of what the project builds, so in install A of session 0327 the first round offered made-up goals, such as a test run of GUPPI, while `CLAUDE.md` said the project description was not set yet; `lesson-sprint-open-asks-no-goal-of-a-new-project` records it. `decision-case-910` put the fix off, naming the questions of `/sprint-open` or the setup skill of `rule-morph` as the place. The person chose `/sprint-open`, for every project and every sprint: step 2 of the Render of `rule-skill-sprint-open` now has the opening Case ask the goal by a question of the shape that `.claude/skills/grill-me/SKILL.md` sets for every question of a round, options and a recommended answer included. Its options come only from the project description that `CLAUDE.md` holds between its `project-description` markers (set by `rule-claude-md`), with one more option, the goal in the person's own words, which its `➡️` line recommends; no option is a goal made up from the vault. Where the description is not set, the own-words option is the only one. At `/pre-spec`, `ask-guppi` found that the first build, an open question with no options, did not fit the grill-me shape, which says that every question takes it; the person chose to keep that shape and leave the rule of grill-me unchanged. The new Estimate keeps the slug of its decision line, since the person's own words stay the recommended answer. The setup skill of `rule-morph` stays `draft` and is not touched; this Case fixes the half of the lesson's root cause that lies in the opening Case. The decision line on `rule-skill-sprint-open` carries `{supersedes:case 910}`, so the defer of the page is retired. The Criterion of `estimate-skill-sprint-open-asks-the-opening-questions` stands: it checks that the prompt holds the goal question, the Definition of done, the first milestone, the backlog and the close line, and the words it quotes, its goal in one sentence, stay in the Render; how the goal is asked is a promise of its own, so a new Estimate checks it. No other live page or file of `.claude/` holds the words of that step: a Grep `goal in one sentence|its goal` over `vault/wiki/` printed only `rules/rule-skill-sprint-open.md` and `estimates/estimate-skill-sprint-open-asks-the-opening-questions.md`, and over `.claude/` only `skills/sprint-open/SKILL.md`. A Grep `sprint-open|sprint_open` over `.guppi/tests/` printed `test_sprint.py` and `test_ledger.py`, a test of the text of the hook on `/hi` and a comment; neither reads `.claude/skills/sprint-open/SKILL.md`, so no test reads the changed text live. A Glob `vault/**/*sprint-open-asks-the-goal*` printed nothing, so the new slug is free. The ledger of this session holds no `error` lesson, so no `{addresses:...}` mark stands; the lesson is of session 0327.

> **problem:**
> The opening Case of a sprint offers goals made up from the vault, and in a new project those goals miss what the project builds.

> **recommend:**
> - **What to do with the deferred item**
>   - Recommended: (b) the opening Case asks what the project builds, as an open question.
>   - Answer: (b).
> - **Which sprints the open question covers**
>   - Recommended: (a) every sprint, in every project.
>   - Answer: (a), agreed.
> - **Which Estimate checks the open question**
>   - Recommended: (b) a new Estimate, `estimate-skill-sprint-open-asks-the-goal-as-an-open-question`.
>   - Answer: (b), agreed.
> - **Change**
>   - Asked: at `/pre-spec`, the person chose that the goal question keep the grill-me shape: its options come only from the project description in `CLAUDE.md`, plus an option in the person's own words; no option is made up from the vault; the `➡️` line recommends the own-words option; the rule of grill-me does not change.
>   - Taken: `then`, the new Render text and the new Estimate say this in place of an open question with no options.

> **given:**
> `rule-skill-sprint-open`: step 2 of its Render, the questions of the opening Case.
> **＋** `.claude/skills/sprint-open/SKILL.md`: the skill rendered from `rule-skill-sprint-open`.
> **＋** `rule-claude-md`: sets the `project-description` markers of `CLAUDE.md`.
> **＋** `.claude/skills/grill-me/SKILL.md`: sets the shape of every question of a round; it does not change.
> **＋** `estimate-skill-sprint-open-asks-the-goal-as-an-open-question`: the new check of how the goal is asked.

> **when:**
> The main agent starts `/sprint-open` of `.claude/skills/sprint-open/SKILL.md`, rendered from `rule-skill-sprint-open`, on `PreToolUse Skill`, or the person types `/sprint-open` on `UserPromptSubmit`, and the main agent dispatches `case-guppi` for the opening Case.

> **then:**
> The prompt of the call asks that the opening Case ask the goal of the sprint, in every project and at every sprint, by a question of the shape that `.claude/skills/grill-me/SKILL.md` sets.
> **＋** Each option of that question but one is a goal taken from the description of the project that `CLAUDE.md` holds between its project-description markers, as `rule-claude-md` sets them.
> **＋** One option is the goal in the person's own words, and the recommended answer of the question is that option.
> **＋** Where `CLAUDE.md` holds no description of the project, the option in the person's own words is the only option.
> **－** No option of that question is a goal made up from the vault.

> **tasks:**
> - [ ] update `rule-skill-sprint-open`
>   - old: `` its goal in one sentence, the `purpose` and the `## Purpose` of the page; ``
>   - new: `` its goal in one sentence, the `purpose` and the `## Purpose` of the page, asked in every project and at every sprint by a question of the shape that `.claude/skills/grill-me/SKILL.md` sets: its options are goals taken only from the description of the project that `CLAUDE.md` holds between its lines `<!-- project-description -->` and `<!-- /project-description -->`, and one option more, the goal in the person's own words, which its `➡️` line recommends and which stands alone where no description is set; no option is a goal made up from the vault (as set in case 952); ``
>   - change: `the opening Case asks the goal of the sprint by options taken only from the description of the project and an option in the person's own words, which it recommends, and offers no goal made up from the vault`
> - [ ] create `estimate-skill-sprint-open-asks-the-goal-as-an-open-question`
>   - ref: `rule-skill-sprint-open`
>   - kind: `QA`
>   - purpose: `Whether /sprint-open has the opening Case ask the goal of the sprint in every project and at every sprint by a question of the grill-me shape whose options are goals taken only from the description of the project in CLAUDE.md and one option in the person's own words, which it recommends, and offer no goal made up from the vault`
>   - method: `by hand: the Render of rule-skill-sprint-open in .claude/skills/sprint-open/SKILL.md read against the Criterion`
>   - tags: `[sprint, workflow, harness]`
> - [ ] `uv run --project .guppi guppi render`: `.claude/skills/sprint-open/SKILL.md`
> - [ ] read `estimate-skill-sprint-open-asks-the-goal-as-an-open-question`

> **ratification:**
> ```
> - decision[case 952][update][rule-skill-sprint-open]{ref:rule-skill-sprint-open}{supersedes:case 910}
> - decision[case 952][create][estimate-skill-sprint-open-asks-the-goal-as-an-open-question]{ref:rule-skill-sprint-open}{tags:sprint,workflow,harness}
> ```
