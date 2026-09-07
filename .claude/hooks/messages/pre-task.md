<!-- vault-inject: generated from rule: a-pre-task-runs-between-the-plan-and-its-approval - do not edit -->

`/pre-task` runs between the plan and its approval: the plan you present has already been checked
against the vault. If work starts without a plan, it runs before the first write.

You perform it by dispatching the `pre-task` agent — `subagent_type: "pre-task"` — and by nothing
else. It is no longer a skill anybody can type.
