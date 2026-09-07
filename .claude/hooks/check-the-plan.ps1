# The pre-task ritual, delivered at the one moment it is worth anything: while a plan exists and
# nothing has been written yet.
#
# WHY `ExitPlanMode` AND NOT AN EDIT. What a pre-task returns is a constraint the plan had already
# assumed away, and a plan with an assumed-away constraint reads as a good plan. By the first Edit
# that constraint is baked into a design nobody is going to revisit. `ExitPlanMode` is the only
# event in the harness where a finished plan exists and no source has been touched.
#
# WHY THE TRIGGER IS NOT `non-trivial` ANY MORE. Three skips in two sessions, three different
# causes, and in none of them did the session believe it was starting implementation - an
# unavailable ritual, a brief that felt pre-checked, a repair inside a test run. The old trigger
# asked the party that wants to start the work to judge whether the work is hard, which is the party
# least able to judge it. Presenting a plan is a fact about the session, not a judgement about it.
#
# ADVISORY AND NOT A DENY, deliberately, and the ruling is the owner's: a hook refuses only when the
# action is IRREVERSIBLE and the refusal CANNOT BE WRONG, both at once. Exiting plan mode is
# reversible - you can plan again - so the first half fails and the second half does not rescue it.
# Denying here would also be cheap, and cheapness is a temptation rather than an argument: the
# `irreversible` half of that rule is a limit on what a hook may decide, not a price.
#
# WHY A SEPARATE FILE FROM `ask-the-vault.ps1`. Measured: a bare PowerShell spawn on this machine is
# 133 ms, and the write path fires 71 to 108 times in a working session - a second process there
# would cost 9 to 14 seconds per session to guard a rare event. This event fires once or twice, so a
# file of its own is free. That is the same reasoning the owner used when he rejected matching `.*`
# and filtering inside the script.
#
# PURE ASCII ON PURPOSE (Windows PowerShell 5.1 reads a .ps1 in the system ANSI codepage unless it
# carries a BOM), and message text is single-quoted, because in a double-quoted PowerShell string a
# backtick is an escape - four shipped instances of that in two sessions, every one of them failing
# towards something plausible.

try { [Console]::InputEncoding  = [System.Text.Encoding]::UTF8 } catch { }
try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch { }

function Write-Note([string] $eventName, [string] $text) {
    @{
        hookSpecificOutput = @{
            hookEventName     = $eventName
            additionalContext = $text
        }
    } | ConvertTo-Json -Depth 4
}

# ConvertFrom-Json rather than a regex over the payload, for the reason both hooks beside this one
# use one: the payload carries arbitrary caller text, and a greedy pattern over it can be steered by
# that text.
$raw = [Console]::In.ReadToEnd()
if ([string]::IsNullOrWhiteSpace($raw)) { exit 0 }
try { $payload = $raw | ConvertFrom-Json } catch { exit 0 }

$tool = $null
$hookEvent = $null
$sessionId = $null
$mode = $null
try { $tool      = $payload.tool_name } catch { }
try { $hookEvent = $payload.hook_event_name } catch { }
try { $sessionId = $payload.session_id } catch { }
try { $mode      = $payload.permission_mode } catch { }

# The matcher already narrows to this tool; checking it again is not redundancy for its own sake.
# A matcher that names the wrong string produces a hook that never fires, and that looks identical
# to a hook with nothing to say - so the selftest pins the registration, and this line keeps the
# script honest if it is ever reached by a wider matcher.
if ($tool -ne 'ExitPlanMode') { exit 0 }

$root = $null
try { $root = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path } catch { exit 0 }
try { . (Join-Path $PSScriptRoot 'pre-task-state.ps1') } catch { exit 0 }

$state = Read-LedgerState $root $sessionId

if ($hookEvent -eq 'PostToolUse') {
    # THE SCOPE IS APPROVED HERE, and this is the machine-observable form of a thing that had no
    # observable form before: the owner choosing `Yes, and use auto mode` in the approval prompt.
    # There is no hook event for a permission-mode change and no hook output that can cause one -
    # the mode is input-only - so this tool call is the only place the transition is visible.
    #
    # WHETHER A REJECTED PLAN ALSO REACHES PostToolUse IS NOT MEASURED. If it does, a scope is
    # recorded that was never approved, and the effect is that the NEXT plan is asked for a fresh
    # pre-task. That fails towards asking more often rather than less, which is the direction a
    # guard is allowed to be wrong in.
    $owed = Test-PreTaskOwedForPlan $state
    Add-LedgerLine -root $root -sessionId $sessionId -event 'scope-approved' `
        -permissionMode $mode -preTask (-not $owed) -path ''
    exit 0
}

# Everything below is the PreToolUse half: the plan is about to be presented.
if (-not (Test-PreTaskOwedForPlan $state)) { exit 0 }

Add-LedgerLine -root $root -sessionId $sessionId -event 'advised-plan' `
    -permissionMode $mode -preTask $false -path ''

$rule = Get-PreTaskMessage $root

$note = 'You are about to present a plan for approval and no /pre-task has run for it. ' +
    'The ritual belongs HERE, before the plan is presented, not after it is approved: what it ' +
    'returns is a constraint the plan has already assumed away, and finding that after approval ' +
    'means the plan that was approved is not the plan that survives. Dispatch the pre-task agent, ' +
    'fold what it returns into the plan, and present the plan again. Every measured run on the ' +
    'record has returned at least one finding.'

if ($rule) { $note = $note + "`n`n" + $rule }

Write-Note 'PreToolUse' $note
exit 0
