## Case 768 — The install check waits for the plugin milestone

> **context:**
> `estimate-sprint-plugin-installs-as-a-plugin` is one of the five Estimates of `entity-sprint-plugin`, created by case 756.6. It checks that the clean branch installs as a Claude Code plugin into an empty project and that `/hi` opens a session there. Its method waits for an install of the clean branch in a session of the sprint `plugin` before its close. No clean branch exists today: a Glob `.git/refs/**/*` printed only `.git/refs/heads/main` and `.git/refs/heads/plugin`, and `.git/packed-refs` holds only the tag `vault-v1`. The plugin is the third milestone of `entity-sprint-plugin`, and the first milestone is not done: `entity-sprint-plugin` is still `draft`, and the Frontier of this session puts both items of that milestone off, C1 and C2 closed `· sprint · defer`. So `/hi` could not take the reading of W6, and `rule-skill-hi` made it the Cases line C10. Case 764 of this session, built in the same batch, sets when an Estimate of a sprint page is read and that Retro leaves it `pending`. That rule decides this item: the method of this Estimate already names a session of its sprint before its close, so neither the method nor the Criterion changes. This Case adds only a History line on the page that says why the reading waits. The promise does not change, so the Criterion stands and the status stays `pending`; the install itself is read by this same Estimate at its moment. A Grep `installs-as-a-plugin|entity-sprint-plugin` over `tests/` printed no file, so no test reads the page live.

> **problem:**
> The install check cannot be read now, since no clean branch exists before the plugin milestone, and its open reading came onto the Frontier as an item that needs a decision.

> **recommend:**
> - **What does this Case do with the install check?**
>   - Recommended: (a) keep the check as it stands, and record why it waits.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: pre-spec found that `context` said the first milestone stands open on the Frontier, while the Frontier puts both its items off; the person agreed to fix the wording.
>   - Taken: `context` says the milestone is not done, the sprint page still `draft` and both its items put off on the Frontier.

> **given:**
> `estimate-sprint-plugin-installs-as-a-plugin`: the check of the install, whose History gains a line.
> **＋** `entity-sprint-plugin`: the sprint page, whose third milestone makes the plugin.

> **when:**
> Someone reads `estimate-sprint-plugin-installs-as-a-plugin` before the third milestone of `entity-sprint-plugin` is reached.

> **then:**
> The page keeps its method, its Criterion and its status.
> **＋** Its History says that the reading waits for the third milestone of `entity-sprint-plugin`, since no clean branch exists to install before it.
> **－** The History line does not set the session of the reading.

> **tasks:**
> - [ ] update `estimate-sprint-plugin-installs-as-a-plugin`
>   - change: `the reading waits for the milestone The plugin of entity-sprint-plugin; no clean branch exists to install before it`

> **ratification:**
> ```
> - decision[case 768][update][estimate-sprint-plugin-installs-as-a-plugin]{ref:entity-sprint-plugin}
> ```
