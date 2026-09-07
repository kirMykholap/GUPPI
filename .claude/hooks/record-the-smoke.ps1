# PostToolUse recorder. Writes one ledger row per RETURNED `make smoke`, naming what it returned,
# and says nothing to anybody.
#
# POST RATHER THAN PRE, AND THE ROW IS THE REASON. A returned result is evidence that the check
# HAPPENED; a requested one is only evidence that it was INTENDED. `gate-the-handoff.ps1` reads
# these rows to decide whether the path to /handoff is open, so a row written before the run would
# open that path on an intention - which is the exact defect this ledger already shipped once, in
# its pre-task flag.
#
# THE VERDICT IS READ OFF THE PRINTED MARKER AND NOT OFF AN EXIT CODE, and that is a deliberate
# inversion of the rule the two gate hooks follow. Those hooks RUN the check themselves, so its exit
# code is theirs to read. This one observes somebody else's tool call, and what a PostToolUse
# payload carries about a shell command is not a contract this repository controls. So the Makefile
# prints one line that cannot be mistaken for prose, `SMOKE-EXIT: <n>`, immediately before exiting
# with the same number, and this file reads that line. ONE reader of one condition: two readers
# disagree eventually, and this project has the scar.
#
# NO MARKER MEANS NO ROW, AND THAT FAILS IN THE SAFE DIRECTION. A run that was interrupted, killed
# or crashed prints nothing, so nothing is recorded, so the handoff gate says no smoke has run and
# asks for one. The alternative - recording an absent marker as a pass - would open the gate on a
# run that never finished.
#
# `make suite` COUNTS TOO, because it runs `make smoke` inside itself and that inner run prints the
# same marker. `suite` is a superset of `smoke` by construction, so a session that ran the whole
# sweep has more than satisfied the thing the gate asks for.
#
# IT NEVER SPEAKS AND NEVER REFUSES. A refusal is possible on PreToolUse alone - PostToolUse fires
# after the act - so this file could not block if it wanted to. It exits 0 on every path, including
# every failure of its own: a recorder that broke a command would cost more than the record is worth.
#
# THIS FILE IS PURE ASCII ON PURPOSE. Windows PowerShell 5.1 reads a .ps1 in the system ANSI
# codepage unless it carries a BOM, so a literal em dash here arrives as mojibake and can break
# parsing outright.

try { [Console]::InputEncoding  = [System.Text.Encoding]::UTF8 } catch { }
try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch { }

function Write-Note([string] $text) {
    @{ hookSpecificOutput = @{ hookEventName = 'PostToolUse'; additionalContext = $text } } |
        ConvertTo-Json -Depth 4
}

$raw = [Console]::In.ReadToEnd()
if ([string]::IsNullOrWhiteSpace($raw)) { exit 0 }
try { $payload = $raw | ConvertFrom-Json } catch { exit 0 }

$tool = $null
try { $tool = $payload.tool_name } catch { }
if ($tool -isnot [string]) { exit 0 }
if ($tool -ne 'Bash') { exit 0 }

$command = $null
try { if ($payload.tool_input.command) { $command = [string] $payload.tool_input.command } } catch { }
if (-not $command) { exit 0 }

# TWO CONDITIONS AND NOT ONE. The marker alone would file a row for any command that happened to
# print that string - a `cat` of this file, for one. The command alone would file a row for a run
# that never reached its last line. Together they say: a make run was asked for, and it finished.
#
# THE COMMAND TEST IS THE NARROW ONE FROM 2026-08-30, AND IT USED TO BE `\bmake\b`. That form
# matched the SLUG of any vault page whose filename begins `make-` - a word boundary sits between
# `make` and the hyphen - so a read of the two pages documenting this marker satisfied both
# conditions and wrote `smoke:0` for a run that never happened. Three such rows stand in the ledger
# for 2026-08-29; two were written by a subagent that holds no write tool, while it was counting
# how often the defect fires. The pattern here is the same one the background branch below already
# used, and narrowing this one changes that branch not at all: it is reachable only for the two
# targets named here either way.
#
# WHAT IT STILL DOES NOT CLOSE, named rather than left to be rediscovered: a command whose own text
# happens to contain `make smoke` - a `grep` for that phrase, say - over output that carries the
# marker would still file a row. That is far narrower than reading a page by its filename, and
# closing it needs a stronger test than the command string, which nothing here has measured.
if ($command -notmatch 'make\s+(smoke|suite)\b') { exit 0 }

# A BACKGROUND LAUNCH IS SAID OUT LOUD RATHER THAN LEFT TO BE DISCOVERED AT THE GATE. A backgrounded
# call reports that it STARTED - a task id and an output path - so the marker this file reads is not
# there and cannot be, and nothing is recorded. Left silent, the session learns that only when
# /handoff refuses, with no clue why, which is the shape this repository keeps paying for.
#
# THE PROSE IN THE REMINDER IS NOT ENOUGH ON ITS OWN, and that is the whole argument for this branch:
# prose does not stop an agent, which is why the title rule left the vault for `vault-check.sh`. This
# fires at the moment of the mistake and names the fix.
$background = $false
try { if ($payload.tool_input.run_in_background) { $background = $true } } catch { }
if ($background -and $command -match 'make\s+(smoke|suite)') {
    Write-Note ('That `make` run was launched in the BACKGROUND, so NOTHING was recorded and ' +
        '/handoff will still refuse. A backgrounded call reports only that it started; the ledger ' +
        'row carries the exit code, which is read off the `SMOKE-EXIT:` line the run prints at the ' +
        'end, and that line does not exist yet. Run it again in the foreground.')
    exit 0
}

# The response shape for a shell call is not a contract this repository controls, so the whole of it
# is flattened and searched rather than a named field being trusted to exist.
$response = ''
try { $response = ($payload.tool_response | ConvertTo-Json -Depth 8 -Compress) } catch { }
if (-not $response) {
    try { $response = [string] $payload.tool_response } catch { }
}
if (-not $response) { exit 0 }

# THE LAST MATCH WINS. A `make suite` prints the inner smoke's marker once, but a session pasting a
# transcript into a heredoc could carry an older one; the run that just finished printed last.
$found = [regex]::Matches($response, 'SMOKE-EXIT:\s*(\d+)')
if ($found.Count -eq 0) { exit 0 }
$code = $found[$found.Count - 1].Groups[1].Value

$sessionId = $null; $mode = $null
try { $sessionId = $payload.session_id }      catch { }
try { $mode      = $payload.permission_mode } catch { }

$root = $null
try { $root = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path } catch { exit 0 }
try { . (Join-Path $PSScriptRoot 'pre-task-state.ps1') } catch { exit 0 }

# `-preTask` is deliberately omitted rather than passed as $false. The column has three states and
# `no` is a CLAIM ABOUT THE WORLD - that a pre-task was not on the record. A smoke row asserts
# nothing either way about that ritual, so it carries `-`, the same as a dispatch row.
try {
    Add-LedgerLine -root $root -sessionId $sessionId -event ('smoke:' + $code) `
        -permissionMode $mode -path $command
} catch { }

exit 0
