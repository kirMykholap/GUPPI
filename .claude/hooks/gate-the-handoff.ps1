# PreToolUse gate. Refuses /handoff while the session has no green `make smoke` behind it.
#
# WHY /handoff AND NOT SOMEWHERE EARLIER. It is the point of no return: it hands the journal to the
# librarian, and after it nothing in this session can be corrected. The owner put the check exactly
# there for that reason, and refused a conditional version with an escape row - a red smoke sends
# the session back into the retro to fix what it found, which is the one moment fixing is still
# possible.
#
# THE THREE CONDITIONS A REFUSING HOOK OWES, argued on its page and repeated here only as a pointer:
#   1. the condition is MEASURED and not judged - it is a comparison of two ledger rows, the latest
#      `smoke:` exit code and the paths written after it. No judgement enters;
#   2. the measurement is RELIABLE where this hook stands - the rows are already in the file at
#      PreToolUse on the Skill call. Unlike the plan check, plan mode is not in play at /handoff, so
#      nothing prevents the writes that produce the rows;
#   3. the refusal SAYS HOW TO CLEAR IT - it names `make smoke` and which of the three states the
#      session is in, because "run smoke" is the wrong instruction for two of them.
#
# THREE STATES AND NOT TWO, and telling them apart is the whole of the design. Never run, run red,
# and run green then written over. `Get-HandoffRefusal` in pre-task-state.ps1 decides which, and the
# inference lives there rather than here for the reason the whole ledger runs on: the event column
# records an observation, the state derives the conclusion, and a reader at a retro can still tell
# which is which.
#
# THE MATCHER `Skill` IS MEASURED AT BOTH ENDS. A probe of 2026-08-21 read `tool=Skill`,
# `event=PreToolUse`, `input_keys=args,skill` off a live payload, which is where the field below
# comes from. And on 2026-08-26 the sibling reminder, registered under a `Skill` matcher during that
# same session, fired on that session's own `/retro` - so a registration in this repository's
# settings works, and this file is registered.
#
# A CLAIM THAT STOOD HERE UNTIL THAT MOMENT WAS FALSE AND IS CORRECTED RATHER THAN QUIETLY DROPPED:
# "hooks are read at session start, so registering does not arm it this session". It does. The same
# sentence went into the selftest's hook register and into a commit message, and the commit is left
# standing on the owner's ruling that a wrong record is evidence of the process that produced it.
#
# THIS FILE IS PURE ASCII ON PURPOSE. Windows PowerShell 5.1 reads a .ps1 in the system ANSI
# codepage unless it carries a BOM, so a literal em dash here arrives as mojibake and can break
# parsing outright.

try { [Console]::InputEncoding  = [System.Text.Encoding]::UTF8 } catch { }
try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch { }

function Write-Note([string] $text) {
    @{ hookSpecificOutput = @{ hookEventName = 'PreToolUse'; additionalContext = $text } } |
        ConvertTo-Json -Depth 4
}

function Write-Deny([string] $reason) {
    @{
        hookSpecificOutput = @{
            hookEventName            = 'PreToolUse'
            permissionDecision       = 'deny'
            permissionDecisionReason = $reason
        }
    } | ConvertTo-Json -Depth 4
}

$raw = [Console]::In.ReadToEnd()
if ([string]::IsNullOrWhiteSpace($raw)) { exit 0 }
try { $payload = $raw | ConvertFrom-Json } catch { exit 0 }

$tool = $payload.tool_name
if ($tool -isnot [string]) { exit 0 }
if ($tool -ne 'Skill') { exit 0 }

# One spelling, `skill`, read off the same 2026-08-21 measurement the reminder beside this file
# names. A second name nobody has ever seen in a payload is insurance the selftest could not
# exercise, and an unexercised branch in a REFUSING hook is worse than none.
$name = $null
if ($payload.tool_input) { $name = $payload.tool_input.skill }
if ($name -isnot [string]) { exit 0 }

$name = $name.Trim()
if ($name -ne 'handoff' -and -not $name.EndsWith(':handoff')) { exit 0 }

$sessionId = $null
try { $sessionId = $payload.session_id } catch { }

$root = $null
try { $root = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path } catch { exit 0 }

# A GATE THAT CANNOT MEASURE SAYS SO RATHER THAN REFUSING, and rather than going quiet. Both of the
# other guards here take that shape: a guard that is silently absent is worse than none, and one
# that refuses on a measurement it did not take teaches the session to route around it.
try { . (Join-Path $PSScriptRoot 'pre-task-state.ps1') } catch {
    Write-Note ('/handoff is about to run and THE SMOKE GATE DID NOT RUN: this hook could not load ' +
        'its state library. Run `make smoke` by hand and do not hand the journal over on a red ' +
        'run. Treat this message as the finding.')
    exit 0
}

if (-not $sessionId) {
    Write-Note ('/handoff is about to run and THE SMOKE GATE DID NOT RUN: the payload carried no ' +
        'session identifier, so this session''s rows cannot be told from another''s. Run ' +
        '`make smoke` by hand. Treat this message as the finding.')
    exit 0
}

$state = $null
try { $state = Read-LedgerState -root $root -sessionId $sessionId } catch { }
if ($null -eq $state) {
    Write-Note ('/handoff is about to run and THE SMOKE GATE DID NOT RUN: the ledger could not be ' +
        'read. Run `make smoke` by hand. Treat this message as the finding.')
    exit 0
}

$reason = Get-HandoffRefusal -root $root -state $state
if ($reason) {
    Write-Deny ('/handoff is refused. THE CONDITION IS: the last `make smoke` of this session ' +
        'exited 0, and nothing git tracks has been written since. ' + $reason)
}

exit 0
