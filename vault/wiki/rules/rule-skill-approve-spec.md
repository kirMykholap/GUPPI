---
type: rule
kind: Leaf
purpose: Prevents a Spec from staying unapproved where the Claude Code CLI withholds the approval of a plan longer than it can show
status: built
enforcement: render
governs: .claude/skills/approve-spec/SKILL.md
render_mode: full
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-skill-approve-spec-takes-the-spec]]"]
origin: raw/2026-11-01/1721/ledger.md#case-987.1
sprint: plugin
created: 2026-11-01
tags: [session, workflow, harness, plugin, render]
core: true
---

## Purpose

Prevents a Spec from staying unapproved where the Claude Code CLI withholds the approval of a plan longer than it can show. The CLI shows a plan whole before it offers approval and offers none for a plan above the size it can show, whatever the window, while the VS Code extension approves the same plan; GUPPI writes each ratified Case whole into the plan file, so a Spec of a few Cases could not leave Plan Mode in the CLI. There the person presses Esc at the dialog, leaves Plan Mode with Shift+Tab and types `/approve-spec`. The hook that judges that prompt and takes the plan file into `spec.md` is the hook of `rule-spec-capture`, which sets when it blocks the prompt and what it writes; this page sets the text of the skill, which tells the agent to follow the line that hook gives. The skill carries `disable-model-invocation: true`: the agent cannot start it, since the approval is the person's.

## Render

<!-- rule-skill-approve-spec -->
---
name: approve-spec
description: The person's approval of the Spec where the Claude Code CLI withholds it, typed out of Plan Mode after /pre-spec; a hook takes the plan file into spec.md and gives the next step.
disable-model-invocation: true
---

The person typed `/approve-spec`: the approval of the Spec where the Claude Code CLI withholds the approval of a plan longer than it can show. The hook of `rule-spec-capture` on `UserPromptSubmit` judged the prompt before it reached you, and let it through: the session is out of Plan Mode, `/pre-spec` ran, the check of the plan finds nothing, and the plan file of the session now stands in `raw/<hi date>/<hi HHMM>/spec.md`.

Follow the line of that hook in your context, as after `ExitPlanMode`: ask the person the fork between `/work` and `/carry` by `AskUserQuestion` and call the skill picked, or, where the line names a conserved Spec, call `/box` with its folder and ask the person nothing. Write nothing into the plan file.
<!-- /rule-skill-approve-spec -->

## History

- 2026-11-01 created · [[decision-case-987.1]]
- 2026-11-01 estimate estimate-skill-approve-spec-takes-the-spec added · [[decision-case-987.1]]
- 2026-11-02 status: draft → built · cascade
