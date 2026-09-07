# Records that a /pre-task or a /vault-ask ran, into the ledger the hooks read.
#
# WHY THE RITUAL RECORDS ITSELF RATHER THAN BEING DETECTED. A /pre-task is a `vault-librarian`
# dispatch - and so is a /vault-ask. The two are indistinguishable by `subagent_type`, and the only
# thing that separates them is the wording of the prompt. Matching on that wording is the antipattern
# this repository already has a case for: assert the condition, not the sentence that introduces it.
# A sentence can be reworded into silence while everything still reports green.
#
# SO THE SKILL WRITES ITS OWN MARK, and the failure direction is the one that is safe. The skill not
# run at all leaves no mark and the advisory fires, which is right. The skill run but this step
# missed leaves no mark and the advisory fires spuriously, which is a nag rather than a silence.
# There is no path on which a pre-task that did not happen is recorded as having happened.
#
# `-Kind` IS WHAT SEPARATES THE TWO, AND IT IS THE CALLER'S WORD RATHER THAN A GUESS. Added
# 2026-08-21: a /vault-ask left no trace at all, so nothing afterwards could say whether the vault
# had been asked. It rides the EVENT column rather than a new one, because the ledger is a
# fixed six-column TSV and a seventh column breaks the split for every reader. `vault-ask` matches
# no case in Read-LedgerState's switch, so it is visible in the record and decides nothing - the
# same property `startup`, `resume` and `compact` already rely on. A vault-ask is NOT a pre-task and
# must never satisfy the advisory that asks for one.
#
# THE COUNTS RIDE THE PATH COLUMN, which is free text the hooks never parse. Phase 1 of /pre-task
# picks a shortlist from a catalogue pass and phase 2 reads only that shortlist, so the one thing
# worth knowing over ten runs is whether phase 1 discards too much. Neither number can be recovered
# after the fact.
#
# NOT IN .claude/hooks/. Nothing here is a hook: it is a command the session runs. The registration
# check treats every .ps1 under .claude/hooks/ as owing either a settings.json entry or a dot-source,
# and this file would owe neither.
#
# PURE ASCII, and message text single-quoted: in a double-quoted PowerShell string a backtick is an
# escape character.

param(
    # What the pre-task covered, for the human reading the ledger at a retro. Free text; the hooks
    # never parse it.
    [string] $Scope = '',

    # Which ritual this row is about. Only these two write here.
    [ValidateSet('pre-task', 'vault-ask')]
    [string] $Kind = 'pre-task',

    # How many pages phase 1 named, and how many were opened in full. Negative means not reported,
    # which is different from zero: zero candidates is a real and common answer.
    [int] $Candidates = -1,
    [int] $Opened = -1
)

try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch { }

$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
. (Join-Path $root '.claude\hooks\pre-task-state.ps1')

# The session identifier comes from the stamp, which is written by the SessionStart hook and
# refreshed by every ledger write. If it is absent, the hooks have not run in this session at all -
# and that is itself the finding, because it means the guard they provide is not there either.
$sessionId = Get-SessionStamp $root
if (-not $sessionId) {
    Write-Output ('record-pre-task: NO SESSION STAMP. The ritual was NOT recorded, because ' +
        'nothing in this session has proved it knows the session identifier - which means the ' +
        'hooks in .claude/settings.json have not run here. Treat that as the finding: the ' +
        'advisory that asks for this ritual is not present either. A guard that is silently ' +
        'absent is worse than none.')
    exit 1
}

$detail = $Scope
if ($Candidates -ge 0 -or $Opened -ge 0) {
    $c = if ($Candidates -ge 0) { [string] $Candidates } else { '?' }
    $o = if ($Opened -ge 0) { [string] $Opened } else { '?' }
    $detail = ($Scope + ' [candidates=' + $c + ' opened=' + $o + ']').Trim()
}

# A vault-ask asserts NOTHING about the ritual, so its flag column is `-` rather than `no`. `no`
# would be a claim that the pre-task did not run, which this row is in no position to make.
$flag = $null
if ($Kind -eq 'pre-task') { $flag = $true }

Add-LedgerLine -root $root -sessionId $sessionId -event $Kind `
    -permissionMode '' -preTask $flag -path $detail

Write-Output ('record-pre-task: recorded ' + $Kind + ' for session ' + $sessionId)
exit 0
