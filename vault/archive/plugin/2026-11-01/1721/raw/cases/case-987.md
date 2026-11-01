## Case 987 — The person approves a long Spec in the CLI by typing /approve-spec

> **context:**
> At the end of Plan Mode the main agent calls `ExitPlanMode`, and Claude Code shows the plan file for approval. GUPPI writes each ratified Case whole into that file. The Claude Code CLI shows a plan whole before it offers approval, and for a plan above the size it can show it offers none: the person can only press Esc or ask for a shorter plan. `lesson-plugin-cli-withholds-approval-of-a-long-plan` records this for a plan file of 15347 bytes in install A of session 2026-10-29/0327, and `lesson-plugin-cli-withholds-approval-in-every-window` records the same refusal in an empty folder with no GUPPI, in two windows of different size, while the VS Code extension approved a larger plan. The Spec capture, `guppi spec` on `PostToolUse` of `ExitPlanMode` in `.guppi/guppi/spec.py`, runs only after that approval, so in the CLI a Spec of a few Cases never reaches `spec.md` and Work Mode never starts. `insight-plugin-cli-withholds-approval-of-a-long-plan` is `open` and carries `deferred_by: decision-case-957`, whose Problem reads: "No Case of this session decides how GUPPI lets a long Spec be approved in the Claude Code CLI"; Case 957 put the item off to wait for a fix from Anthropic. The changelog of Claude Code read by `WebFetch` at https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md, its first 100 000 characters, versions 2.1.301 to 2.1.316, names no fix of this refusal; the rest of the file was not read. The page https://code.claude.com/docs/en/permission-modes says that Shift+Tab leaves plan mode without approving a plan, and states no size limit of a plan. The page https://code.claude.com/docs/en/hooks says that `UserPromptSubmit` receives a skill the person typed as the line typed, with `permission_mode` among its fields, one of whose values is `plan`, and that a hook that blocks the prompt stops the command. The page https://code.claude.com/docs/en/skills says that with `disable-model-invocation: true` Claude cannot invoke a skill on its own while the person can still type it.
>
> The person chose a typed approval: where the CLI withholds the approval, the person presses Esc, leaves Plan Mode with Shift+Tab and types `/approve-spec`. Case 987.1 adds the skill `/approve-spec` and a hook on `UserPromptSubmit`, `uv run --project .guppi guppi spec --typed`, which takes the plan file into `spec.md` as an approval does and gives the agent the same line. It refuses the prompt in Plan Mode, so that Work Mode can edit, and, before `/pre-spec` or while the check of the plan finds a finding, by the judgment the hook of `rule-prespec-hook` runs at `ExitPlanMode`. One page owns each part: the hook is code of `.guppi/guppi/spec.py`, so `rule-spec-capture`, whose `implementation_ref` names that file, owns it and its new text states the typed path whole; the new rule `rule-skill-approve-spec` owns only the text of the skill, and its Purpose and Render point to the hook of `rule-spec-capture`, with no `implementation_ref`. Its Estimate, `estimate-skill-approve-spec-takes-the-spec`, checks the command as the person meets it, skill and hook together, which is what that rule prevents. The skill takes `disable-model-invocation: true`, so the approval stays the person's. Case 987.2 has the main agent name that way. The person first chose that the agent names it after its call of `ExitPlanMode` is refused with no words, but the documentation shows the agent gets no reply at that moment: https://code.claude.com/docs/en/interactive-mode says "On a permission prompt, `Esc` declines the action, the same as **No** without a comment", and https://code.claude.com/docs/en/permissions says "If you select **No** without a comment on a prompt from the main conversation, Claude Code stops the turn". The agent also cannot tell a person who refused from a CLI that offered no approval. So, by the person's answer to a later round, the reply that calls `ExitPlanMode` holds, before the call, one line worded as a condition, which claims nothing the agent cannot know, as `rule-agent-writing` and `CLAUDE.md` ask ("Name a real source or remove the claim"). At `/pre-spec` the person agreed that the trials in the CLI wait for the librarian's run after this session, since the skill, its hook in `.claude/settings.json` and the new sentence of `orchestration.md` are rendered only then; the by-hand part of each method opens with `after` and that event, and only the test of 987.1 is read in this session. Case 989 of this session moves its trial of `/box` to the same moment. The README note of Case 957 is left to the item of `entity-sprint-plugin` that writes the README. Case 987.1 sets the insight `actioned` and carries `{supersedes:case 957}`, so that `generate` clears its defer. A Glob `vault/**/*approve*` printed only `estimate-spec-write-reaches-the-approved-spec.md`, so the new slugs are free; both `create` lines carry a `ref`.
>
> One judgment, one implementation: a Grep of `.guppi/guppi/` for `get\("prompt"\)|\["prompt"\]` printed `event.py` and `sprint.py`, which read a typed `/hi` by `is_hi_prompt` of `.guppi/guppi/event.py`, and `gate.py`, whose `skill_of` reads the first word of a typed prompt. I read `is_hi_prompt`, `hi_refusal` and `skill_of` whole: on a command alone, a command with arguments after a space, and a prompt with spaces around it, both answer alike, and both refuse a command followed by a tab or a line break. So 987.1 moves the body of `is_hi_prompt` into one function for a named command, which `is_hi_prompt` and `spec --typed` call, and reads Plan Mode by `PLAN_MODE` of `event.py`, the value `hi_refusal` reads. The gate is `gate` of `.guppi/guppi/prespec.py`, which I read whole with `window`, `prespec_mark` and `plan_findings`: its judgment moves into one function that returns the reason or nothing, which `gate` prints as before and `spec --typed` calls; `plan_path` of `.guppi/guppi/ledger.py` finds the plan file for both.
>
> The frame. A Grep for `ExitPlanMode` over `.claude/` printed `skills/box/SKILL.md`, `skills/work/SKILL.md`, `skills/carry/SKILL.md` and `settings.json`, and over `vault/wiki/rules/` printed `rule-prespec-hook`, `rule-hook-registry`, `rule-work-mode`, `rule-spec-box`, `rule-orchestration`, `rule-spec-capture`, `rule-carry-over` and `rule-session`. The renders of `rule-work-mode`, `rule-carry-over` and `rule-spec-box` say their skill follows the line printed after `ExitPlanMode`, which the typed path makes false, so 987.1 rewords them. I read whole each sentence those pairs touch: the description of the skill `/work`, which also says the person types it to resume and `/box` calls it with a conserved Spec; its Purpose sentence on when `/work` starts; the description and the opening sentence of `/carry`; and the description of `/box` and its sentence on its argument. Each stays true with the new words. Of the other Cases of this session, only Case 989 changes one of these pages: it changes the last sentence of the Purpose of `rule-spec-box`, on where the second part of `/box` is noted, and I read its finished file whole. The sentences differ, so the pairs do not meet. `rule-spec-capture` says the file has three writers, the hook on `ExitPlanMode` among them, and gains the typed path. `rule-prespec-hook` and `rule-session` say the hook on `ExitPlanMode` refuses an exit before `/pre-spec`, which stays true. `rule-hook-registry` gains the new command. `rule-orchestration` is 987.2: I read whole the sentence of its Render that its pair ends, which says that in a working session the rules of the harness come before the Plan Mode instructions of Claude Code, that the agent asks by a plain question and never by a picker tool, and that it calls `ExitPlanMode` only after `/pre-spec`. The new sentence after it agrees with each part. Case 984 of this session, whose finished file I read whole, changes another sentence of that Render, under `## Who builds a Case`, on which Cases the prompt of `case-guppi` names as related, and its Estimate; the pair of 987.2 stands under `## Plan Mode and the Frontier`, so the two pairs do not meet, and neither text speaks of the other's moment. The `.guppi/links.md` blocks of `rule-spec-capture`, `rule-hook-registry`, `rule-work-mode`, `rule-carry-over`, `rule-spec-box`, `rule-orchestration`, the insight, `.guppi/guppi/spec.py` and `.claude/settings.json` name no other neighbour that the change makes false. The glossary row of Spec says it is approved as Claude Code's plan, which stands, since `/approve-spec` takes the same plan file. `onward --plan` of `.guppi/guppi/onward.py`, whose docstring I read, sends the agent on toward `ExitPlanMode` after `/pre-spec`, after a reply with a `LEDGER` block or after a reply the ledger hook sent back (case 696.2); the reply that then calls `ExitPlanMode` carries the line of 987.2 as any such reply does, so the hook needs no change. `estimate-orchestration-puts-the-harness-before-plan-mode` stands: its Then says the agent calls `ExitPlanMode` only after `/pre-spec` has run and asks by no picker in Plan Mode, and the line of 987.2 is a plain line of the reply that keeps both. `estimate-skill-sprint-open-starts-at-hi` judges a `/hi` by `is_hi_prompt` of `.guppi/guppi/event.py`, and `estimate-event-log-records` judges a `/hi` by its `permission_mode` and says that any other prompt is silent there; both stand, since `is_hi_prompt` keeps its answer on every input when its body moves into the shared function, and the event hook does not judge `/approve-spec`, which `spec --typed` judges. `estimate-hook-registry-rendered` stands: its Then says every hook the harness runs is registered by a line of the Render of `rule-hook-registry`, and 987.1 registers the new hook there. `estimate-prespec-hook-reports-a-pointer-outside-a-bracket` stands: its When names the judgment the hook runs at `ExitPlanMode`, and that judgment keeps its findings when `spec --typed` calls it too. The Criteria of `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, `estimate-work-mode-takes-the-work-readings`, `estimate-carry-over-writes`, `estimate-spec-box-runs-a-conserved-spec`, `estimate-spec-capture-appends` and `estimate-spec-capture-offers-the-fork` speak of the path after `ExitPlanMode`, which still holds, and stand: the same line after `/approve-spec` is the promise of `estimate-skill-approve-spec-takes-the-spec`. `estimate-prespec-hook-gates` stands, since `gate` keeps its output.
>
> The new hook is one more member of the hooks of `UserPromptSubmit`. A Grep for the existing member `casecheck --prompt` over `vault/wiki/` printed `log.md`, `rules/rule-case-check.md`, `rules/rule-hook-registry.md` and three Estimates of the Case check; over `.claude/` it printed `settings.json`; over `.guppi/guppi/` it printed `casecheck.py` and `ledger.py`. Only the Render of `rule-hook-registry` and `settings.json` list the members; the hit in `rule-case-check` is a History line, and the others name that hook alone. The new skill file stands in `.claude/skills/`: a Grep of `.guppi/guppi/` for `\.claude/skills|skills/` printed `links.py`, `recall.py` and `ship.py`. `links.py` reads each skill of the folder into the graph, `recall.py` reads only the skill `/hi`, and `ship.py` writes the file of a Render of a page with `core: true`, so the new rule, `core: true`, ships its skill once it is no longer `draft`. No `.gitignore` stands under `.claude/`. A Grep of `.guppi/tests/` for `(REPO|ROOT|repo_root|PROJECT|parents\[\d\]).*(settings\.json|orchestration\.md|SKILL\.md|skills)` printed `test_guppi_package.py` and `test_orchestration.py`. The first checks that the command of each hook in its `HOOKS` stands in `settings.json`, and `spec` is not among them. The second reads the blocks tagged `showing` and `defer` of `orchestration.md`, which 987.2 does not touch. Both stand. The session's ledger holds no `error` lesson. Two lines of `then` share their words: in 987.1 the hook tells the person, when `/approve-spec` comes in Plan Mode, to leave it with Shift+Tab, and in 987.2 the reply that calls `ExitPlanMode` names Esc, Shift+Tab and `/approve-spec` before the call. They are two moments with two promises, so nothing is signed twice.

> **problem:**
> In the Claude Code CLI a Spec of a few Cases cannot be approved, so the session never reaches Work Mode, and GUPPI gives the person no other way to approve it.

> **recommend:**
> - **What GUPPI does when the CLI withholds the approval**
>   - Recommended: (c) approval by a typed command after leaving Plan Mode.
>   - Answer: agreed, (c).
> - **What the person types**
>   - Recommended: (a) `/approve`.
>   - Answer: the person's own name, `/approve-spec`.
> - **What the command checks before it takes the Spec**
>   - Recommended: (a) the same checks as the exit, through the same code, and the command refused while the session is still in Plan Mode.
>   - Answer: agreed, (a).
> - **How the person learns the way**
>   - Recommended: (a) the agent names the way after an exit refused with no words of the person.
>   - Answer: agreed, (a).
> - **How the Case is checked**
>   - Recommended: (a) a new Estimate, checked by a test of the hook and a by-hand trial in the CLI in this session's Work Mode.
>   - Answer: agreed, (a).
> - **What becomes of the insight and the README note**
>   - Recommended: (a) the insight closed as fixed by this Case, the README left to its item of the sprint.
>   - Answer: agreed, (a).
> - **How the agent's words after a refused exit are checked**
>   - Recommended: (a) a new Estimate, read in the record of the same CLI trial.
>   - Answer: agreed, (a).
> - **When the agent names the way**
>   - Recommended: (a) in the reply that calls `ExitPlanMode`, one line before the call, worded as a condition, since the documentation shows that after Esc at the dialog Claude Code stops the turn and the agent gets no reply.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec`, the person agreed that the trials in the CLI do not run in this session's Work Mode, since the skill `/approve-spec`, its hook in `.claude/settings.json` and the new sentence of `orchestration.md` exist only after the librarian's render after this session.
>   - Taken: the by-hand part of the method of each new Estimate waits for the librarian's run after this session; only the test of 987.1 is read in this session.

### Case 987.1 — /approve-spec takes the Spec where the CLI withholds the approval

> **given:**
> `rule-skill-approve-spec`: the new rule of the skill `/approve-spec`.
> **＋** `.claude/skills/approve-spec/SKILL.md`: the skill, rendered from that rule.
> **＋** `.guppi/guppi/spec.py`: the Spec capture, which gains the typed path.
> **＋** `.guppi/guppi/event.py`: the reading of a typed command and of Plan Mode.
> **＋** `.guppi/guppi/prespec.py`: the gate that the exit and the typed path share.
> **＋** `.guppi/tests/test_spec.py`: the tests of the Spec capture.
> **＋** `rule-spec-capture`: the writers of `raw/<hi date>/<hi HHMM>/spec.md`.
> **＋** `rule-hook-registry`: the hooks of `.claude/settings.json`.
> **＋** `rule-work-mode`, `rule-carry-over`, `rule-spec-box`: the rules of `/work`, `/carry` and `/box`, the skills that follow the line given after an approval.
> **＋** `/pre-spec` and `/hi`: the check of the plan, and the command that opens a working session.
> **＋** `insight-plugin-cli-withholds-approval-of-a-long-plan`: the insight this Case fixes.
> **＋** `estimate-skill-approve-spec-takes-the-spec`: the new check of `/approve-spec`.

> **when:**
> In a working session the person types `/approve-spec`, and `uv run --project .guppi guppi spec --typed` of `.guppi/guppi/spec.py` runs on `UserPromptSubmit`.

> **then:**
> Out of Plan Mode, after `/pre-spec`, with a plan file of the session that the check of the plan passes, the hook appends that plan file to `raw/<hi date>/<hi HHMM>/spec.md` under its stamp, once, as `rule-spec-capture` sets it for an approval by `ExitPlanMode`.
> **＋** The hook then gives the agent the line it gives after `ExitPlanMode`: the fork between `/work` and `/carry`, or the call of `/box` for a plan that names a conserved Spec.
> **＋** The skill `.claude/skills/approve-spec/SKILL.md` tells the agent to follow that line.
> **－** While the session is in Plan Mode, the hook blocks the prompt and tells the person to leave Plan Mode with Shift+Tab and type `/approve-spec` again.
> **－** Before `/pre-spec`, or while the check of the plan finds a finding, the hook blocks the prompt with the reason that `gate` of `.guppi/guppi/prespec.py` judges at `ExitPlanMode`, by the same function.
> **－** With no plan file of the session, or with no `/hi` of the session, the hook blocks the prompt and says why.
> **－** A blocked prompt leaves `spec.md` as it stands.
> **－** The agent cannot start `/approve-spec` itself.
> **－** Any other prompt passes the hook, and nothing is written.

> **tasks:**
> - [ ] create `rule-skill-approve-spec`
>   - ref: `rule-plan-mode`
>   - type: `rule`
>   - kind: `Leaf`
>   - purpose: `Prevents a Spec from staying unapproved where the Claude Code CLI withholds the approval of a plan longer than it can show`
>   - enforcement: `render`
>   - governs: `.claude/skills/approve-spec/SKILL.md`
>   - render_mode: `full`
>   - core: `true`
>   - tags: `[session, workflow, harness, plugin, render]`
>   - sections.Purpose:
>     ```
>     Prevents a Spec from staying unapproved where the Claude Code CLI withholds the approval of a plan longer than it can show. The CLI shows a plan whole before it offers approval and offers none for a plan above the size it can show, whatever the window, while the VS Code extension approves the same plan; GUPPI writes each ratified Case whole into the plan file, so a Spec of a few Cases could not leave Plan Mode in the CLI. There the person presses Esc at the dialog, leaves Plan Mode with Shift+Tab and types `/approve-spec`. The hook that judges that prompt and takes the plan file into `spec.md` is the hook of `rule-spec-capture`, which sets when it blocks the prompt and what it writes; this page sets the text of the skill, which tells the agent to follow the line that hook gives. The skill carries `disable-model-invocation: true`: the agent cannot start it, since the approval is the person's.
>     ```
>   - sections.Render:
>     ```
>     <!-- rule-skill-approve-spec -->
>     ---
>     name: approve-spec
>     description: The person's approval of the Spec where the Claude Code CLI withholds it, typed out of Plan Mode after /pre-spec; a hook takes the plan file into spec.md and gives the next step.
>     disable-model-invocation: true
>     ---
>
>     The person typed `/approve-spec`: the approval of the Spec where the Claude Code CLI withholds the approval of a plan longer than it can show. The hook of `rule-spec-capture` on `UserPromptSubmit` judged the prompt before it reached you, and let it through: the session is out of Plan Mode, `/pre-spec` ran, the check of the plan finds nothing, and the plan file of the session now stands in `raw/<hi date>/<hi HHMM>/spec.md`.
>
>     Follow the line of that hook in your context, as after `ExitPlanMode`: ask the person the fork between `/work` and `/carry` by `AskUserQuestion` and call the skill picked, or, where the line names a conserved Spec, call `/box` with its folder and ask the person nothing. Write nothing into the plan file.
>     <!-- /rule-skill-approve-spec -->
>     ```
> - [ ] update `rule-spec-capture`
>   - old: `` The file has three writers: the hook `guppi spec` on `PostToolUse` of `ExitPlanMode`, which appends the approved plan to `raw/<hi date>/<hi HHMM>/spec.md` once, stamped; ``
>   - new: `` The file has three writers: the hook `guppi spec` on `PostToolUse` of `ExitPlanMode`, which appends the approved plan to `raw/<hi date>/<hi HHMM>/spec.md` once, stamped, and, where the Claude Code CLI withholds that approval, on `UserPromptSubmit` when the person types `/approve-spec`, as `uv run --project .guppi guppi spec --typed`, which blocks the prompt while the session is in Plan Mode, before `/pre-spec` or while the check of the plan finds a finding — by the judgment of `gate` of `.guppi/guppi/prespec.py`, the same function the hook of `rule-prespec-hook` runs at `ExitPlanMode` — and with no plan file or no `/hi` of the session, and otherwise appends the plan file of the session in the same way and gives the agent the same line, the skill of `rule-skill-approve-spec` telling the agent to follow it; ``
>   - change: `the Spec capture takes the plan file when the person types /approve-spec`
> - [ ] update `rule-hook-registry`
>   - old: `{ "type": "command", "command": "uv run --project .guppi guppi sprint --hi", "timeout": 30 },`
>   - new: `{ "type": "command", "command": "uv run --project .guppi guppi sprint --hi", "timeout": 30 }, { "type": "command", "command": "uv run --project .guppi guppi spec --typed", "timeout": 30 },`
>   - change: `UserPromptSubmit → guppi spec --typed`
> - [ ] update `rule-work-mode`
>   - old: `` Its skill `/work` starts after `ExitPlanMode`: ``
>   - new: `` Its skill `/work` starts after the approval of the Spec, by `ExitPlanMode` or by `/approve-spec`: ``
>   - old: `at the fork ExitPlanMode prints;`
>   - new: `at the fork printed after the approval of the Spec, by ExitPlanMode or by /approve-spec;`
>   - change: `/work follows the approval by ExitPlanMode or by /approve-spec`
> - [ ] update `rule-carry-over`
>   - old: `at the fork ExitPlanMode prints.`
>   - new: `at the fork printed after the approval of the Spec, by ExitPlanMode or by /approve-spec.`
>   - old: `` Called after `ExitPlanMode`, when ``
>   - new: `` Called after the approval of the Spec, by `ExitPlanMode` or by `/approve-spec`, when ``
>   - change: `/carry follows the approval by ExitPlanMode or by /approve-spec`
> - [ ] update `rule-spec-box`
>   - old: `prints after ExitPlanMode.`
>   - new: `prints after the approval of the Spec, by ExitPlanMode or by /approve-spec.`
>   - old: `` the line printed after `ExitPlanMode` names ``
>   - new: `` the line printed after the approval of the Spec, by `ExitPlanMode` or by `/approve-spec`, names ``
>   - change: `/box follows the approval by ExitPlanMode or by /approve-spec`
> - [ ] update `insight-plugin-cli-withholds-approval-of-a-long-plan`
>   - set:
>     ```
>     status: actioned
>     addressed_by: decision-case-987.1
>     ```
>   - change: `actioned: the person approves a long Spec in the CLI by typing /approve-spec`
> - [ ] create `estimate-skill-approve-spec-takes-the-spec`
>   - ref: `rule-skill-approve-spec`
>   - kind: `QA`
>   - purpose: `Whether /approve-spec, typed by the person out of Plan Mode after /pre-spec, appends the plan file of the session to its spec.md and gives the agent the line of an approval, and is blocked in Plan Mode, before /pre-spec, while the check of the plan finds a finding, or with no plan file`
>   - method: `uv run --project .guppi pytest .guppi/tests/test_spec.py -k typed; by hand, after the librarian's run that applies the create of rule-skill-approve-spec and renders .claude/settings.json and .claude/skills/approve-spec/SKILL.md: in a standalone terminal window, the Claude Code CLI on a copy of the repository, a working session whose plan the CLI withholds and whose check of /pre-spec passes, /approve-spec typed once in Plan Mode and once after Esc and Shift+Tab, then the transcript of that session under ~/.claude/projects/ and its spec.md read against the Criterion`
>   - tags: `[session, workflow, harness, plugin]`
> - [ ] `.guppi/guppi/event.py`: the body of `is_hi_prompt` moves into one function that judges a typed prompt for a named command, which `is_hi_prompt` calls with `/hi`.
> - [ ] `.guppi/guppi/prespec.py`: the judgment of `gate` moves into one function that returns the reason of a refusal or nothing; `gate` prints that reason as before.
> - [ ] `.guppi/guppi/spec.py`: `--typed` on `UserPromptSubmit` reads `/approve-spec` by the function of `event.py` and Plan Mode by `PLAN_MODE`, runs the function of `prespec.py`, finds the plan file by `plan_path` of `ledger.py`, appends it by `append_plan` and prints the line of `fork_output` as `hookSpecificOutput` of `UserPromptSubmit`, or exits 2 with the reason; the docstring names the typed path.
> - [ ] `.guppi/tests/test_spec.py`: tests named with `typed` for each line of the `then` above.
> - [ ] `uv run --project .guppi guppi render`: `.claude/settings.json`
> - [ ] `uv run --project .guppi guppi render`: `.claude/skills/approve-spec/SKILL.md`
> - [ ] `uv run --project .guppi guppi render`: `.claude/skills/work/SKILL.md`
> - [ ] `uv run --project .guppi guppi render`: `.claude/skills/carry/SKILL.md`
> - [ ] `uv run --project .guppi guppi render`: `.claude/skills/box/SKILL.md`
> - [ ] read `estimate-skill-approve-spec-takes-the-spec`

> **ratification:**
> ```
> - decision[case 987.1][create][rule-skill-approve-spec]{ref:rule-plan-mode}{tags:session,workflow,harness,plugin,render}
> - decision[case 987.1][update][rule-spec-capture]{ref:rule-spec-capture}
> - decision[case 987.1][update][rule-hook-registry]{ref:rule-hook-registry}
> - decision[case 987.1][update][rule-work-mode]{ref:rule-work-mode}
> - decision[case 987.1][update][rule-carry-over]{ref:rule-carry-over}
> - decision[case 987.1][update][rule-spec-box]{ref:rule-spec-box}
> - decision[case 987.1][update][insight-plugin-cli-withholds-approval-of-a-long-plan]{ref:insight-plugin-cli-withholds-approval-of-a-long-plan}{supersedes:case 957}
> - decision[case 987.1][create][estimate-skill-approve-spec-takes-the-spec]{ref:rule-skill-approve-spec}{tags:session,workflow,harness,plugin}
> ```

### Case 987.2 — The agent names the typed approval before it leaves Plan Mode

> **given:**
> `rule-orchestration`: its Render, `vault/wiki/orchestration.md`, what the main agent does.
> **＋** `rule-skill-approve-spec`: the rule of `/approve-spec`, the command the line names.
> **＋** `/pre-spec`: the check after which the agent calls `ExitPlanMode`.
> **＋** `estimate-orchestration-names-the-typed-approval`: the new check of the line.

> **when:**
> In a working session the main agent writes the reply that calls `ExitPlanMode`.

> **then:**
> Before the call, the reply holds one line worded as a condition: if the Claude Code CLI offers no approval for this plan, press Esc, leave Plan Mode with Shift+Tab and type `/approve-spec`.
> **＋** The line claims nothing of the client: it does not say that the CLI withholds the approval.
> **－** The line adds no step and no question: the agent calls `ExitPlanMode` in the same reply, only after `/pre-spec`, as before.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` calls `ExitPlanMode` only after `/pre-spec` (case 561.14). ``
>   - new: `` calls `ExitPlanMode` only after `/pre-spec` (case 561.14). The reply that calls `ExitPlanMode` holds, before the call, one line worded as a condition: if the Claude Code CLI offers no approval for this plan, the person presses Esc, leaves Plan Mode with Shift+Tab and types `/approve-spec`. The agent cannot tell whether the CLI offered the approval, and after Esc at the dialog Claude Code stops the turn, so the line comes before the call and claims nothing of the client. ``
>   - change: `the reply that calls ExitPlanMode names /approve-spec, worded as a condition, before the call`
> - [ ] create `estimate-orchestration-names-the-typed-approval`
>   - ref: `rule-orchestration`
>   - kind: `QA`
>   - purpose: `Whether the reply in which the main agent calls ExitPlanMode holds, before the call, one line worded as a condition that names Esc, Shift+Tab and /approve-spec for a CLI that offers no approval, and claims nothing of the client`
>   - method: `by hand, after the librarian's run that applies the update of rule-orchestration naming /approve-spec and renders vault/wiki/orchestration.md: in the trial in the Claude Code CLI that reads estimate-skill-approve-spec-takes-the-spec, the reply that calls ExitPlanMode read in the transcript of that session under ~/.claude/projects/ against the Criterion`
>   - tags: `[session, workflow, harness, plugin]`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-orchestration-names-the-typed-approval`

> **ratification:**
> ```
> - decision[case 987.2][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 987.2][create][estimate-orchestration-names-the-typed-approval]{ref:rule-orchestration}{tags:session,workflow,harness,plugin}
> ```
