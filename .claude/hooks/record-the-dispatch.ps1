# PostToolUse record of a subagent dispatch. Writes one ledger row per RETURNED dispatch, naming
# the agent type it was, and says nothing to anybody.
#
# POST RATHER THAN PRE, AND THE COLUMN IS THE REASON. A returned result is evidence that work
# HAPPENED; a requested dispatch is only evidence that work was INTENDED. A human reading this
# ledger at a retro reads the rows as a record of what the session did, so a row written before the
# act would be a column filled from a branch condition rather than from the world - which is the
# exact defect this ledger already shipped once, in its pre-task flag.
#
# WHAT IT IS FOR, AND IT IS NOT BOOKKEEPING. `/pre-task` records itself by the session running
# `scripts/record-pre-task.ps1`. That is a WRITE, the rule places the ritual between the plan and
# its approval, and plan mode permits no writes - so the ritual performed at the exact moment the
# rule names leaves no trace, and the guard beside it then reports that none ran. It happened four
# times in one session on 2026-08-21 and once more on 2026-08-22, in the session that built this
# file. A HOOK can write during planning; the rows already in this ledger carrying `plan` in their
# permission-mode column are the proof. Once `/pre-task` is an agent, its dispatch is the evidence
# and this hook is what turns the evidence into a row.
#
# THE EVENT COLUMN STAYS FACTUAL AND THE MEANING IS DERIVED. The row says `dispatch:<type>` - what
# happened - and `Read-LedgerState` in pre-task-state.ps1 is what decides that `dispatch:pre-task`
# discharges the ritual. That split is this ledger's own philosophy: the state is read back out of
# the lines, so the record and the thing it records cannot drift apart. A hook that wrote `pre-task`
# directly would be asserting a conclusion in a column, and a later reader could not tell an
# inference from an observation.
#
# THE MATCHER IS `Agent|Task` AND BOTH HALVES ARE LOAD-BEARING, for the same reason the lock beside
# this file names both: the dispatch tool was renamed from `Task` to `Agent` in 2.1.63 and the old
# name still resolves as an alias, so a matcher naming one of them is a recorder that silently does
# not exist on some version.
#
# IT NEVER SPEAKS AND NEVER REFUSES. A refusal is possible on `PreToolUse` alone - `PostToolUse`
# fires after the act - so this file could not block if it wanted to, and it is not a candidate for
# the three-condition test at all. It exits 0 on every path, including every failure of its own:
# a recorder that broke a dispatch would cost more than the record is worth.
#
# PURE ASCII ON PURPOSE. Windows PowerShell 5.1 reads a .ps1 in the system ANSI codepage unless it
# carries a BOM, so a literal em dash here arrives as mojibake and can break parsing outright.

try { [Console]::InputEncoding  = [System.Text.Encoding]::UTF8 } catch { }
try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch { }

# ConvertFrom-Json rather than a regex over the payload, for the reason the two hooks beside this
# one give: a payload is a document and a regex over it matches whatever a description happens to
# contain.
$raw = [Console]::In.ReadToEnd()
if ([string]::IsNullOrWhiteSpace($raw)) { exit 0 }
try { $payload = $raw | ConvertFrom-Json } catch { exit 0 }

$tool = $null
try { $tool = $payload.tool_name } catch { }
if ($tool -isnot [string]) { exit 0 }
if ($tool -ne 'Agent' -and $tool -ne 'Task') { exit 0 }

# The matcher can only narrow by tool name, so the agent type is read here. Both spellings are
# accepted for the same reason the lock accepts both: the tool's own input names it `subagent_type`,
# while the subagent lifecycle events spell it `agent_type`.
$type = $null
if ($payload.tool_input) {
    if ($payload.tool_input.subagent_type) { $type = $payload.tool_input.subagent_type }
    elseif ($payload.tool_input.agent_type) { $type = $payload.tool_input.agent_type }
}

# NO TYPE IS STILL A DISPATCH AND IS STILL RECORDED. The default agent is dispatched with no
# `subagent_type` at all, and dropping those rows would make the ledger say that a session which
# dispatched ten agents dispatched none - an instrument failing towards "nothing happened here",
# which is the direction this repository has already been bitten by three times.
if ($type -isnot [string] -or [string]::IsNullOrWhiteSpace($type)) { $type = 'default' }

# Tabs would break the column count for every later reader; the ledger flattens the path column
# itself, but the event column is assembled here and nothing downstream cleans it.
$type = ($type -replace "[`t`r`n]", ' ').Trim()

$sessionId = $null; $mode = $null; $desc = ''
try { $sessionId = $payload.session_id } catch { }
try { $mode      = $payload.permission_mode } catch { }
try { if ($payload.tool_input.description) { $desc = [string] $payload.tool_input.description } } catch { }

$root = $null
try { $root = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path } catch { exit 0 }
try { . (Join-Path $PSScriptRoot 'pre-task-state.ps1') } catch { exit 0 }

# `-preTask` is deliberately omitted rather than passed as $false. The column has three states and
# `no` is a CLAIM ABOUT THE WORLD - that a pre-task was not on the record. A dispatch row asserts
# nothing either way about the ritual, so it carries `-`, the same as a `session-start` row. This is
# the distinction `Add-LedgerLine` takes an [object] rather than a [bool] to preserve.
try {
    Add-LedgerLine -root $root -sessionId $sessionId -event ('dispatch:' + $type) `
        -permissionMode $mode -path $desc
} catch { }

exit 0
