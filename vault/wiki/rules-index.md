rule-ask: Prevents a create from being proposed without the vault having been asked whether it already holds the thing, or forbids it
rule-case-protocol: Prevents a decision from being acted on before it is ratified, or ratified without its content in view
rule-event-log: Prevents the ledger from being written into a session nothing recorded
rule-git-context: Prevents a session from starting on a branch it does not know, or pulling mid-session
rule-github-issues: Prevents deferred bugs, tracked outside the vault, from being forgotten at session start
rule-hook-registry: Prevents a hook from being registered by hand, outside a ratified decision
rule-index: Prevents a pre-task check from reading every page of a category to learn what already exists
rule-internal-context: Prevents work starting without the current sprint and the previous session's handover
rule-ledger-write: Prevents a ratified line from existing only in a chat reply, or landing in a session no /hi opened
rule-lint: Prevents a page that breaks the schema, points nowhere, or claims a status its Estimates do not support from sitting in the vault unnoticed
rule-plan-mode: Prevents work being planned against stale or contradictory vault state
rule-pretask: Prevents a set of ratified decisions from reaching the Spec with a contradiction between them or with the vault
rule-pretask-hook: Prevents a Spec from being approved before its decisions were checked against each other and the vault
rule-render-harness: Prevents a Rule page and the harness file it governs from becoming two copies of one text
rule-session-start: Prevents a working session from starting against unknown state
rule-skill-hi: Prevents a session from being loaded piecemeal by read-tool calls
rule-spec-capture: Prevents an approved Spec from existing only in Claude Code's plan file, outside the repository
