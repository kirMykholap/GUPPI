# InstructionsLoaded probe. Temporary: it exists to answer whether a `paths:`-scoped rule in
# .claude/rules/ reaches a subagent that reads a matching file, which the vendor documentation
# does not say and which every task in this project depends on, because every task here is
# reviewed by a subagent.
#
# IT IS A SECOND OBSERVABLE, NOT THE ONLY ONE. The primary observable is the model quoting the
# nonce out of .claude/rules/_probe-paths.md. This log corroborates it and adds the load reason.
# That split is deliberate: if the matcher spelling is wrong this hook never fires, and a probe
# that depends on a single instrument cannot tell "it did not load" from "I did not measure".
#
# The exit code of this event is ignored by the harness, so this cannot block anything. It writes
# a file and gets out of the way; every failure path exits 0 in silence rather than risking a
# broken session for a measurement.
#
# PowerShell rather than bash, for the reason check-the-journal.ps1 records: a hook is spawned by
# the OS, and `bash` on this machine's system PATH is the WSL shim that cannot execute.
#
# PURE ASCII ON PURPOSE. Windows PowerShell 5.1 reads a .ps1 in the system ANSI codepage unless
# it carries a BOM, so a literal em dash arrives as mojibake and can break parsing outright.

try { [Console]::InputEncoding  = [System.Text.Encoding]::UTF8 } catch { }
try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch { }

try {
    $raw = [Console]::In.ReadToEnd()

    $root = $env:CLAUDE_PROJECT_DIR
    if (-not $root) { $root = Split-Path (Split-Path $PSScriptRoot) }
    $log = Join-Path $root 'probe\instructions-loaded.log'

    $dir = Split-Path $log
    if (-not (Test-Path -LiteralPath $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
    }

    # The whole payload is kept, on one line, rather than a field this probe guesses the name of.
    # The field names of this event are not documented; recording everything is the difference
    # between reading the answer later and having to run the measurement twice.
    $flat = ($raw -replace '\s+', ' ').Trim()
    if (-not $flat) { $flat = '(empty payload)' }

    $stamp = (Get-Date).ToString('yyyy-MM-dd HH:mm:ss')
    Add-Content -LiteralPath $log -Encoding utf8 -Value "$stamp  $flat"
} catch { }

exit 0
