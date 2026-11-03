---
name: approve-spec
description: The person's approval of the Spec where the Claude Code CLI withholds it, typed out of Plan Mode after /pre-spec; a hook takes the plan file into spec.md and gives the next step.
disable-model-invocation: true
---

The person typed `/approve-spec`: the approval of the Spec where the Claude Code CLI withholds the approval of a plan longer than it can show. The hook of `rule-spec-capture` on `UserPromptSubmit` judged the prompt before it reached you, and let it through: the session is out of Plan Mode, `/pre-spec` ran, the check of the plan finds nothing, and the plan file of the session now stands in `raw/<hi date>/<hi HHMM>/spec.md`.

Follow the line of that hook in your context, as after `ExitPlanMode`: ask the person the fork between `/work` and `/carry` by `AskUserQuestion` and call the skill picked, or, where the line names a conserved Spec, call `/box` with its folder and ask the person nothing. Write nothing into the plan file.
