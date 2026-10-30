## Case 945 — A stop writes each command it asks the person to run whole

> **context:**
> When Work Mode stops for the person to do something by hand, the agent's reply lists the steps. No rule sets how those steps are written. At the stop of Work Mode of session 2005, the steps wrote out the start command with `UV_OFFLINE=1` and `UV_CACHE_DIR` only for the second test project. The step for the fourth project said "the same two variables as in step 4". The person started it in a new window, which kept neither variable, and the fourth project installed online. So the reading of `estimate-plugin-install-sets-aside-the-files-of-the-project` did not happen (lesson `lesson-plugin-install-steps-named-the-offline-variables-by-reference`, ledger line L56 of session 2005). The steps came from one `then` line of Case 943.1, which asked for "the steps for each project" and set no form.
>
> `rule-where-to-stop` renders `vault/wiki/where-to-stop.md`, which `/work`, `/box` and `/hi` load. It sets when the agent stops and that the reply ends with the question to the person. It says nothing on the form of steps the person runs by hand. The person chose to add the guard there, for every stop, and to check it by a new Estimate, read at the next stop whose reply gives the person commands to run. The new sentence goes after the sentence that ends the reply with the question, so the eight numbered conditions keep their numbers. The page has `core: true`, so the pointer to this Case stands in a bracket at the end of its sentence.
>
> `estimate-where-to-stop-stops-only-on-its-conditions` stands `passed`. Its Criterion speaks of when the agent stops and that it asks. One of its lines also speaks of what a reply holds: on a refusal of the auto mode classifier, the reply gives the shell command that does what the refused call would do, for the person to type after `!`. That line promises that the command is given; the new sentence sets how a command the person runs is written, and its own Estimate checks that. The new text adds one sentence after the eight conditions and leaves the text that sets each line of that Criterion word for word, so each line still holds and its Criterion stands. This Case does not set it `pending`. Its `method` names a reading at the Retro of the session that changes the Render; the new Render makes no line of its Criterion false, so that reading would find what its last Result found, and this Case does not ask for it. The deferral of the reading of `estimate-plugin-install-sets-aside-the-files-of-the-project` is Frontier item C6, and this Case leaves it out.
>
> A Grep of `.guppi/` for `where-to-stop|where_to_stop` printed `.guppi/tests/test_gate.py`, `.guppi/guppi/gate.py`, `.guppi/tests/test_onward.py` and `.guppi/guppi/onward.py`; each hit names the path inside a message string, and none reads the text of the file, so no test needs a change. A Grep of `.claude/` for `where-to-stop|stop:` printed `.claude/skills/work/SKILL.md`, `.claude/skills/box/SKILL.md`, `.claude/skills/hi/SKILL.md`, `.claude/skills/pr-review/SKILL.md`, `.claude/skills/sprint-open/SKILL.md` and `.claude/skills/retro/SKILL.md`; they load the file or name a condition by its number, and the new sentence changes no number. A Grep of `vault/wiki/rules/` for `STOP:|reply that stops|the question to the person` printed `rule-prespec-onward.md`, `rule-where-to-stop.md`, `rule-retro-onward.md` and `rule-retro.md`, and the same Grep of `.claude/` printed `.claude/skills/retro/SKILL.md`. Each of the other hits sets that a stop reply opens with `STOP:`, and none sets what the steps of the reply hold, so this Case does not cover the `STOP:` opening. The lesson stands in the ledger of session 2005, and the ledger of this session holds no `error` lesson, so no line carries `{addresses:...}`.

> **problem:**
> A stop reply may write a command once and then point to it from a later step. A new window keeps none of the variables, so the person runs a different command than the check needs.

> **recommend:**
> - **Which text carries the guard?**
>   - Recommended: (a) `rule-where-to-stop`, a paragraph on the stop reply.
>   - Answer: agreed, (a).
> - **Which check closes the Case?**
>   - Recommended: (a) a new check, read at the next stop with steps by hand.
>   - Answer: agreed, (a).

> **given:**
> `rule-where-to-stop`: sets when Work Mode stops and how the reply ends.
> **＋** `vault/wiki/where-to-stop.md`: the Render of `rule-where-to-stop`, loaded by `/work`, `/box` and `/hi`.
> **＋** `estimate-where-to-stop-writes-each-step-whole`: the new check of the steps of a stop reply.

> **when:**
> Work Mode stops on a condition of `vault/wiki/where-to-stop.md`, and the reply asks the person to run commands by hand.

> **then:**
> Each step of the reply writes out whole each command it asks the person to run, as the person types it, with each variable, folder and flag the command needs.
> **＋** A step that starts a program in a new window or terminal writes the variables that the start needs in its own command.
> **－** No step names a part of its command by a reference to another step.

> **tasks:**
> - [ ] update `rule-where-to-stop`
>   - old: `To stop, end the reply with the question to the person.`
>   - new: `To stop, end the reply with the question to the person. Where the question asks the person to run commands by hand, write each command whole in each step that runs it, as the person types it, with each variable, folder and flag it needs; a step names no part of its command by a reference to another step, since a new window or terminal keeps none of them (as set in case 945).`
>   - change: `a stop reply writes each command it asks the person to run whole`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/where-to-stop.md`
> - [ ] create `estimate-where-to-stop-writes-each-step-whole`
>   - ref: `rule-where-to-stop`
>   - kind: `QA`
>   - purpose: `Whether a stop reply that asks the person to run commands by hand writes each command whole in each step, its variables included, with no reference to another step`
>   - method: `by hand, after the first stop of Work Mode under the new text of vault/wiki/where-to-stop.md whose reply asks the person to run commands by hand: that reply read against each line of the Criterion, recorded in the estimate line`
>   - tags: `[session, workflow, harness]`
> - [ ] read `estimate-where-to-stop-writes-each-step-whole`

> **ratification:**
> ```
> - decision[case 945][update][rule-where-to-stop]{ref:rule-where-to-stop}
> - decision[case 945][create][estimate-where-to-stop-writes-each-step-whole]{ref:rule-where-to-stop}{tags:session,workflow,harness}
> ```
