# PreToolUse lock on the librarian dispatch. Refuses to launch `vault-librarian` while
# `scripts/vault-check.sh` exits non-zero, and says what is red so the refusal can be cleared.
#
# WHY THIS ONE REFUSES WHEN NO OTHER HOOK IN THIS REPOSITORY DOES. The ruling is that a hook is
# advisory unless the action is IRREVERSIBLE and the refusal CANNOT BE WRONG, both at once. A
# librarian round trip runs fifteen to thirty minutes and writes coverage sidecars keyed by LINE
# NUMBER, against a raw/ that is immutable - so an ingest run over a broken input cannot be fixed
# by correcting the input and running again: the lines have moved and the verdicts point at the
# wrong claims. And the refusal is decided by reading an exit code, not by forming a judgement.
#
# PRE RATHER THAN POST, unlike the journal gate beside it, and for the mirror reason: here the
# condition is knowable BEFORE the act, and the act is the expensive half.
#
# THE REFUSAL NAMES ITS CONDITION, WHICH IS THE OWNER'S RULE OF 2026-08-20: a refusal either states
# what must be true and can be cleared and retried, or it is absolute and has no appeal. This one is
# the first kind, so it carries the gate's own output. A denial the session cannot clear is a gate
# that gets disabled.
#
# WHY IT ALLOWS WHEN IT CANNOT MEASURE. If bash is not findable the gate did not run, and refusing
# on a measurement that did not happen is a refusal that can be wrong - which the ruling forbids.
# It says so loudly instead. A guard that is silently absent is worse than none.
#
# THE MATCHER IS `Agent|Task` AND BOTH HALVES ARE LOAD-BEARING. The dispatch tool was renamed from
# `Task` to `Agent` in 2.1.63 and the old name still resolves as an alias, so a matcher naming only
# one of them is a lock that silently does not exist on some version. `SubagentStart` looks like the
# right event and is not: its exit code is ignored, it cannot block, and a lock built on it would
# look identical to one that works.
#
# COST: one full gate run, about 8.5 seconds, paid only on a librarian dispatch and only by the
# main session. Against fifteen minutes it is noise, and it buys the whole of that fifteen.
#
# PowerShell for the reason every hook here is: a hook is spawned by the OS, and on this machine the
# bash on the system PATH is a WSL shim with no distro behind it.

try { [Console]::InputEncoding = [System.Text.Encoding]::UTF8 } catch { }
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

# ConvertFrom-Json rather than a regex, for the reason the guard beside it uses one: a payload
# carries arbitrary caller text, and a greedy pattern over it can be steered by that text.
try { $payload = $raw | ConvertFrom-Json } catch { exit 0 }

$tool = $payload.tool_name
if ($tool -isnot [string]) { exit 0 }
if ($tool -ne 'Agent' -and $tool -ne 'Task') { exit 0 }

# The matcher can only narrow by tool name, so the agent type is read here. Both spellings are
# accepted: the tool's own input names it `subagent_type`, while the subagent lifecycle events
# spell it `agent_type`, and a lock that knows only one spelling is a lock with a hole in it.
$type = $null
if ($payload.tool_input) {
    if ($payload.tool_input.subagent_type) { $type = $payload.tool_input.subagent_type }
    elseif ($payload.tool_input.agent_type) { $type = $payload.tool_input.agent_type }
}
if ($type -isnot [string]) { exit 0 }
if ($type -ne 'vault-librarian') { exit 0 }

$root = $null
try {
    $root = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
    . (Join-Path $PSScriptRoot 'vault-path.ps1')
} catch { exit 0 }

$bash = Find-Bash
if ($null -eq $bash) {
    Write-Note ("The librarian is about to be dispatched and THE LOCK DID NOT RUN: this hook " +
        "could not find a usable bash, so the vault gate was never asked. Run " +
        "``bash scripts/vault-check.sh`` by hand and do not dispatch on a red tree - an ingest " +
        "over a broken input cannot be re-run, because raw/ is immutable and the coverage " +
        "sidecar is keyed by line number. This message is the finding: a lock that cannot " +
        "measure must say so rather than refuse on a measurement it did not take.")
    exit 0
}

$script = (Join-Path $root 'scripts\vault-check.sh').Replace('\', '/')
if (-not (Test-Path -LiteralPath $script)) { exit 0 }

$out = & $bash $script 2>&1 | Out-String
$code = $LASTEXITCODE

# The gate's own exit code is the arbiter, never a grep over its output: two readers of one
# condition disagree eventually, and this project has the scar. Advisories print and do not fail,
# so they are dropped from the reason - the caller needs what it must fix, not the corpus-wide
# statistics, and those now need --lint anyway.
if ($code -ne 0) {
    $lines = ($out -split "`n" | Where-Object { $_ -notmatch 'advisory' }) -join "`n"
    Write-Deny ("The vault gate is red, so the librarian is not dispatched. THE CONDITION IS: " +
        "``bash scripts/vault-check.sh`` must exit 0. Fix what it reports below, then dispatch " +
        "again - this refusal clears itself the moment the tree is green. It exists because an " +
        "ingest cannot be re-run over a corrected journal: raw/ is immutable and the coverage " +
        "sidecar is keyed by line number, so a run against a broken tree costs fifteen to thirty " +
        "minutes and leaves verdicts pointing at the wrong lines. What the gate said:" +
        "`n`n" + $lines.Trim())
}

exit 0
