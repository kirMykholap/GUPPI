# PostToolUse gate. Fires when a journal is written into the vault's raw/handoffs/ and runs
# `scripts/vault-check.sh`, so that a malformed journal is reported at the one moment it can
# still be corrected: while it is being written, before /ingest reads it and before raw/
# immutability makes the form permanent.
#
# WHY POST AND NOT PRE. The event a rule can be checked against is the journal existing, and it
# does not exist until the write has happened. Blocking is not on the table for the same reason -
# by the time this runs the file is on disk - so the hook is loud rather than obstructive: it
# prints what the check found into a channel the session cannot skip past.
#
# WHY A HOOK AND NOT A LINE IN THE SKILL. /handoff carries that line too, and it is the only one
# that works in a session that started before this file existed - hooks are read at session start.
# But a step written in a skill is prose, and prose does not stop an agent; that is the same
# argument that put the title rule into vault-check.sh instead of leaving it in the vault.
#
# PowerShell rather than bash, and that is not a preference: on this machine `bash` on the system
# PATH is the WSL shim in WindowsApps and answers `execvpe(/bin/bash) failed`, while Git's bash is
# not on PATH at all. A hook is spawned by the OS, not by the agent's shell, so it gets the broken
# one. Which is the whole difficulty here, and the next block is the answer to it.
#
# THIS FILE IS PURE ASCII ON PURPOSE. Windows PowerShell 5.1 reads a .ps1 in the system ANSI
# codepage unless it carries a BOM, so a literal em dash here arrives as mojibake and can break
# parsing outright.

try { [Console]::InputEncoding  = [System.Text.Encoding]::UTF8 } catch { }
try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch { }

function Write-Note([string] $text) {
    @{
        hookSpecificOutput = @{
            hookEventName     = 'PostToolUse'
            additionalContext = $text
        }
    } | ConvertTo-Json -Depth 4
}

# Find-Bash moved into vault-path.ps1 on 2026-08-20, when the librarian lock became its second
# caller. It is dot-sourced below, in the same block that brings in Find-Vault, and that block runs
# before the only call to it. One definition rather than two: two discovery rules that can disagree
# are worse than either of them, which is the reason Find-Vault lives there already.

# ConvertFrom-Json rather than a regex over the payload: a Write call carries the whole file
# content in the same JSON object, so a file that itself contains the text "file_path": "..."
# can redirect a greedy pattern onto a path that is nobody's business.
try {
    $raw = [Console]::In.ReadToEnd()
    if (-not $raw) { exit 0 }
    $payload = $raw | ConvertFrom-Json
    $path = $payload.tool_input.file_path
} catch {
    exit 0
}

if (-not $path) { exit 0 }
if ($path -isnot [string]) { exit 0 }

# .Replace, not -replace: the right-hand side of -replace is a regular expression in which a lone
# backslash is invalid. Written that way this would error on every payload, print nothing, and
# still exit 0 - a gate that is silently never there, which this project has shipped once already.
$p = $path.Replace('\', '/')

$root = $null
try { $root = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path } catch { exit 0 }

# THE `write` ROW IS WRITTEN HERE, AND THE BRANCH LIVES INSIDE A HOOK THAT ALREADY RUNS. A fourth
# registration on `Write|Edit` would spawn a second PowerShell on every edit in this repository to
# record a row, and a design of exactly that shape was rejected here before: the latency of THIS
# script is already sunk, so the row costs nothing beyond one append.
#
# IT IS WRITTEN BEFORE EVERY NARROWING BELOW, DELIBERATELY. What reads this row is the handoff gate,
# which asks whether anything at all was written after the last smoke run - not whether a journal
# was. A row filed only for journals would answer a different question and would answer it green.
#
# THE EVENT IS `write` AND THE PATH RIDES THE PATH COLUMN, which is the shape the ledger already
# uses. No seventh column is added: every reader of this file splits by position.
$sessionId = $null; $mode = $null
try { $sessionId = $payload.session_id }      catch { }
try { $mode      = $payload.permission_mode } catch { }
try {
    . (Join-Path $PSScriptRoot 'pre-task-state.ps1')
    Add-LedgerLine -root $root -sessionId $sessionId -event 'write' -permissionMode $mode -path $p
} catch { }

$vault = $null
try {
    . (Join-Path $PSScriptRoot 'vault-path.ps1')
    $vault = Find-Vault $root
} catch { }
if ($null -eq $vault) { exit 0 }

# Narrow to journals. The sidecar is a .tsv and does not match; the older TEMPLATE.md does, and is
# left to the check itself, which distinguishes a journal from a form by whether `session:` carries
# a date. One place decides that, and it is not this one.
$handoffs = $vault.FullName.Replace('\', '/').TrimEnd('/') + '/raw/handoffs/'
if ($p -notlike "$handoffs*") { exit 0 }
if ($p -notlike '*.md')       { exit 0 }

$bash = Find-Bash
if ($null -eq $bash) {
    Write-Note ("A journal was written to the vault's raw/ and THE GATE DID NOT RUN: this hook " +
        "could not find a usable bash. git was not on the PATH the harness spawns hooks with, or " +
        "it is not a Git-for-Windows install. Run ``bash scripts/vault-check.sh`` by hand before " +
        "/ingest, and treat this message as the finding: a gate that cannot run must say so, " +
        "because a guard that is silently absent is worse than none.")
    exit 0
}

$script = (Join-Path $root 'scripts\vault-check.sh').Replace('\', '/')
if (-not (Test-Path -LiteralPath $script)) { exit 0 }

$out = & $bash $script 2>&1 | Out-String
$code = $LASTEXITCODE

# Advisories print and do not fail; only a real violation is worth interrupting for. The check's
# own exit code is the arbiter, not a grep over its output - two readers of one condition disagree
# eventually, and this project has the scar.
if ($code -ne 0) {
    $lines = ($out -split "`n" | Where-Object { $_ -notmatch 'advisory' }) -join "`n"
    Write-Note ("The journal you just wrote does not pass the vault gate. Fix it NOW, before " +
        "/ingest: raw/ is immutable once the journal has been read, and its coverage sidecar is " +
        "keyed by line number, so a later correction cannot be a rewrite. What the gate said:" +
        "`n`n" + $lines.Trim())
}

exit 0
