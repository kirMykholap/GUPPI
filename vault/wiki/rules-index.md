rule-ask: Prevents a create from being proposed without the vault having been asked whether it already holds the thing, or forbids it
rule-bash-guard: Prevents a heredoc from carrying a backslash escape or writing a file through the Bash tool
rule-brief: Prevents the next session from starting without the facts and the flags of this one
rule-case-protocol: Prevents a decision from being acted on before it is ratified, or ratified without its content in view
rule-claude-md: Prevents the system prompt from holding a line nobody ratified
rule-cleanup: Prevents an archived page from staying among the live ones, or the indexes from lagging behind the vault
rule-close: Prevents the librarian's writes from landing in the session's own commit, or from ending without a commit at all
rule-default-mode: Keeps a session from writing anything before a Case is ratified
rule-documentation: Prevents a ratified decision from ending the session without becoming a vault page
rule-end-of-work: Prevents a session being handed over without a settled account of what happened
rule-event-log: Prevents the ledger from being written into a session nothing recorded
rule-git-context: Prevents a session from starting on a branch it does not know, or pulling mid-session
rule-github-issues: Prevents deferred bugs, tracked outside the vault, from being forgotten at session start
rule-governed-files-hook: Prevents a harness file rendered from a Rule page from being edited by hand
rule-handoff: Prevents the session's memory from being lost between the commit and the librarian
rule-harness: Prevents the tools of the harness from drifting apart from the pages that describe them
rule-hook-registry: Prevents a hook from being registered by hand, outside a ratified decision
rule-index: Prevents a pre-task check from reading every page of a category to learn what already exists
rule-index-check: Prevents a page from being born twice under two names
rule-internal-context: Prevents work starting without the current sprint and the previous session's handover
rule-ledger-tail: Shows at /hi every ledger line that no vault page holds yet, so a reading or a lesson written after the librarian's commit reaches the next session's Frontier
rule-ledger-write: Prevents a ratified line from existing only in a chat reply, or landing in a session no /hi opened
rule-lint: Prevents a page that breaks the schema, points nowhere, or claims a status its Estimates do not support from sitting in the vault unnoticed
rule-materialize: Prevents the librarian from reading the ledger and the Spec itself, or from routing a decision by guesswork
rule-page-generation: Prevents a ratified decision from ending the session without a page, or a page from carrying a field nobody ratified
rule-permissions: Lets the session write its own working files without asking, and nothing else
rule-plan-mode: Prevents work being planned against stale or contradictory vault state
rule-pretask: Prevents a set of ratified decisions from reaching the Spec with a contradiction between them or with the vault
rule-pretask-hook: Prevents a Spec from being approved before its decisions were checked against each other and the vault
rule-raw-archive: Keeps raw/ to the sessions not yet turned into pages, by moving an applied session whole into the archive
rule-render-harness: Prevents a Rule page and the harness file it governs from becoming two copies of one text
rule-retro: Prevents a session from closing on work nobody reviewed, or on a change that traces to no decision
rule-retro-commit: Prevents the handoff from starting on an uncommitted tree
rule-session-start: Prevents a working session from starting against unknown state
rule-settings: Keeps the three rules that share .claude/settings.json from becoming two copies of one file
rule-skill-hi: Prevents a session from being loaded piecemeal by read-tool calls
rule-spec-capture: Prevents an approved Spec from existing only in Claude Code's plan file, outside the repository
rule-subagent-guppi: Prevents implementation drifting from the ratified plan while it is being executed · deferred_by: decision-case-141
rule-synthesis: Prevents a pattern of failures from staying a list of unrelated incidents
rule-work-mode: Prevents implementation starting before the plan, branch and baseline exist · deferred_by: decision-case-141
