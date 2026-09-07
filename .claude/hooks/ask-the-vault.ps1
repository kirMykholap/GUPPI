# PreToolUse guard. Fires when a file that carries a rule, or a file with exactly one legal
# writer, is about to be written, and injects a reminder. Advisory: it never blocks, never
# fails the tool, and always exits 0.
#
# The matcher is narrow on purpose. A guard on every edit becomes a ritual performed without
# reading; a guard on rule-bearing paths fires exactly where the recorded divergences happened.
#
# PowerShell rather than bash, and that is not a preference. On this machine `bash` on the
# system PATH is the WSL shim in WindowsApps, and with no distro installed it answers
# `execvpe(/bin/bash) failed`. Git's bash is not on PATH at all. A hook is spawned by the OS,
# not by the agent's own shell, so it gets the broken one. PowerShell is always there.
#
# ConvertFrom-Json rather than a regex over the payload: a Write call carries the whole file
# content in the same JSON object, so a file that itself contains the text "file_path": "..."
# can redirect a greedy pattern onto a path that is nobody's business.

try { [Console]::InputEncoding = [System.Text.Encoding]::UTF8 } catch { }
try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch { }

function Write-Note([string] $text) {
    @{
        hookSpecificOutput = @{
            hookEventName    = 'PreToolUse'
            additionalContext = $text
        }
    } | ConvertTo-Json -Depth 4
}

# Strips what the native delivery strips, so that both triggers hand out the same text.
#
# MEASURED, not assumed: probe 3 read a rule file through the harness's own path-scoped delivery
# and found the frontmatter AND the HTML comment on line 6 both absent from what reached either
# reader. This branch takes the frontmatter off by construction - it starts after the closing
# `---` - and would otherwise deliver the comment, which the other trigger does not. That
# difference is not cosmetic: the `generated, do not edit` banner a generated rule file is to
# carry is free ONLY because it is stripped, and delivering it here would spend it on every edit
# of every governed file.
#
# A comment inside a fenced block is left alone. This corpus documents its own markers inside
# fences, and a rule explaining a marker would otherwise lose the thing it is explaining. What
# the native delivery does inside a fence is NOT measured; this is the conservative half.
function Remove-HtmlComments([string[]] $lines) {
    $out = @(); $inFence = $false; $inComment = $false
    foreach ($line in $lines) {
        if (-not $inComment -and $line -match '^\s*```') { $inFence = -not $inFence; $out += $line; continue }
        if ($inFence) { $out += $line; continue }

        $text = $line
        if ($inComment) {
            $end = $text.IndexOf('-->')
            if ($end -lt 0) { continue }                  # still inside: the whole line goes
            $text = $text.Substring($end + 3); $inComment = $false
        }
        while ($true) {
            $start = $text.IndexOf('<!--')
            if ($start -lt 0) { break }
            $end = $text.IndexOf('-->', $start)
            if ($end -lt 0) { $text = $text.Substring(0, $start); $inComment = $true; break }
            $text = $text.Substring(0, $start) + $text.Substring($end + 3)
        }
        if ($text.Trim() -ne '' -or $line.Trim() -eq '') { $out += $text }
    }
    return (($out -join "`n") -replace '(\r?\n){3,}', "`n`n").Trim()
}

# Reads the path-scoped rules of .claude/rules/ and returns the text of every one whose
# `paths:` list matches the file about to be written, or nothing.
#
# Why this exists: a governed file read before a /compact and edited after it is edited with the
# rule gone from context and no signal that it is missing. The native Read delivery fires once,
# on the read; this fires on the operation the probe measured going through unguarded. So a guard
# is not a reminder - it is a second trigger, bound to something that recurs.
#
# It reads no marker. A file here that no vault page backs is somebody's hand-written rule and is
# legitimate; the marker is the injector's permission to DELETE, and delivering is not deleting.
function Get-ScopedRules([string] $forward, [string] $repoRoot) {
    if (-not $repoRoot) { return '' }
    $dir = Join-Path $repoRoot '.claude/rules'    # forward slashes: PowerShell takes them and nothing here has to carry an escape
    if (-not (Test-Path -LiteralPath $dir)) { return '' }

    # The globs are written from the repository root, the same origin `governs:` uses, so the
    # payload's absolute path is reduced to that origin before matching.
    $rootForward = $repoRoot.Replace([char]92, '/').TrimEnd('/')
    $rel = $forward
    if ($rel -like "$rootForward/*") { $rel = $rel.Substring($rootForward.Length + 1) }

    $found = @()
    foreach ($file in (Get-ChildItem -LiteralPath $dir -Filter '*.md' -File | Sort-Object Name)) {
        try { $lines = Get-Content -LiteralPath $file.FullName -Encoding UTF8 } catch { continue }
        if ($lines.Count -lt 2) { continue }
        if ($lines[0].Trim() -ne '---') { continue }

        # Both spellings of a YAML list, because `paths:` is authored on a vault page whose other
        # list fields are written inline, and synced into a file whose own were written in block
        # form. A parser that knew only one would be silently blind to half the rules it is for.
        $globs = @(); $inList = $false; $close = -1
        for ($i = 1; $i -lt $lines.Count; $i++) {
            if ($lines[$i].Trim() -eq '---') { $close = $i; break }
            if ($lines[$i] -match '^paths:\s*\[(.*)\]\s*$') {
                foreach ($piece in ($Matches[1] -split ',')) {
                    $piece = $piece.Trim().Trim('"').Trim("'").Trim()
                    if ($piece) { $globs += $piece }
                }
                continue
            }
            if ($lines[$i] -match '^paths:\s*$') { $inList = $true; continue }
            if ($inList) {
                if ($lines[$i] -match '^\s+-\s*(.+?)\s*$') { $globs += $Matches[1].Trim('"').Trim("'") }
                else { $inList = $false }
            }
        }
        if ($close -lt 0) { continue }          # no closing ---: not frontmatter, not a rule file

        foreach ($glob in $globs) {
            if ($rel -like $glob) {
                $body = Remove-HtmlComments $lines[($close + 1)..($lines.Count - 1)]
                if ($body) { $found += $body }
                break
            }
        }
    }
    return ($found -join ("`n`n" + ('-' * 60) + "`n`n"))
}

$sessionId = $null
$permMode = $null
try {
    $raw = [Console]::In.ReadToEnd()
    if (-not $raw) { exit 0 }
    $payload = $raw | ConvertFrom-Json
    $path = $payload.tool_input.file_path

    # Read off the same parse rather than a second one. `session_id` is what tells a repeated note
    # from a first one, and `permission_mode` is the only place the harness says which mode this
    # session ACTUALLY started in - the VS Code extension takes that from its own user settings and
    # ignores this repository's, so a value written into `.claude/settings.json` can be true on disk
    # and false in the session reading it. Both may legitimately be absent; nothing below requires
    # them.
    try { $sessionId = $payload.session_id } catch { }
    try { $permMode = $payload.permission_mode } catch { }
} catch {
    exit 0          # malformed or unexpected payload: say nothing, block nothing
}

if (-not $path) { exit 0 }
if ($path -isnot [string]) { exit 0 }

# Backslashes normalised first, so one set of patterns covers both spellings of a Windows path.
# .Replace, not -replace: the right-hand side of -replace is a regular expression and a lone
# backslash is not a valid one. Written that way the script errored on every payload, printed
# no reminder at all, and still exited 0 - a guard that is silently never there.
$p = $path.Replace('\', '/')

# Which files belong to the vault is answered by finding the vault, not by matching the word
# `wiki` anywhere in a path: `docs/wiki/notes.md` is not the librarian's, and the vault's own
# directory is named whatever the owner last called it.
$inWiki = $false
$isRegister = $false
$isRaw = $false
# A FLAG OF ITS OWN, AND NARROWING `$inWiki` WOULD HAVE BEEN THE WRONG REPAIR. `$inWiki` feeds two
# unrelated consumers: the one-writer note below, and the pre-task net at the bottom of this file,
# which excludes every vault path class from its question. Taking the schemas out of `$inWiki`
# would have taken them out of that exclusion too, against the decision that the whole vault is
# excluded from the net - so the schemas leave the NOTE by a flag only the note reads
# ([[the-schema-files-leave-the-one-writer-note-by-a-flag-of-their-own]],
# [[the-vault-is-excluded-from-the-pre-task-net]]).
$isSchema = $false
try {
    $root = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
    . (Join-Path $PSScriptRoot 'vault-path.ps1')
    $vault = Find-Vault $root
    if ($null -ne $vault) {
        $vaultPath = $vault.FullName.Replace('\', '/').TrimEnd('/')
        if ($p -like "$vaultPath/wiki/*" -or $p -like "$vaultPath/archive/*") { $inWiki = $true }
        if ($p -like "$vaultPath/wiki/*/_schema.yaml") { $isSchema = $true }
        if ($p -like "$vaultPath/raw/*" -and (Test-Path -LiteralPath $path)) { $isRaw = $true }
        # `authority.md` joined this list on 2026-08-21, with the register itself. It is the
        # librarian's dictionary of authority families - the grouping that is nowhere in the tree
        # and cannot be derived from it - so it is a register in exactly the sense `tags.md` is,
        # and a second writer would break it the same way
        # ([[authority-becomes-the-index-and-is-required-outside-rules]]).
        foreach ($register in 'index.md', 'tags.md', 'log.md', 'brief.md', 'sprint.md', 'authority.md') {
            if ($p -eq "$vaultPath/$register") { $isRegister = $true }
        }
    }
} catch { }

# Session state for the two notes below that must not repeat. Loaded once, before the chain, so a
# failure to load it costs the notes their de-duplication and nothing else: `$state` stays null and
# every branch behaves exactly as it did before this file learned about sessions.
$state = $null
try {
    if ($root) {
        . (Join-Path $PSScriptRoot 'pre-task-state.ps1')
        $state = Read-LedgerState $root $sessionId
    }
} catch { }

# THE CHAIN STILL PICKS EXACTLY ONE NOTE; WHAT CHANGED IS THAT IT NO LONGER PRINTS IT ITSELF. The
# pre-task net below has to be able to speak on the SAME edit that trips one of these, and a branch
# added to this chain could only do that by shadowing whichever branch it sat above. Placed above
# the scoped-rules branch at the bottom, it would lose rule delivery on exactly the edits a missing
# pre-task is most dangerous on. So the net is not a branch in this chain: it appends after it. The
# chain's own behaviour is untouched, and the case pinning `an earlier branch still wins its path`
# still holds because the branch that used to win still wins.
#
# It is also a correctness fix that was owed regardless: two calls to Write-Note would put two JSON
# objects on one stdout, and nothing downstream is prepared to read that.
$note = $null
$gaveWikiNote = $false

if ($isRaw) {
    # Only for a file that already exists: a new journal is exactly what /handoff is for.
    $note = ("You are about to overwrite a file in the vault's raw/, which is immutable. " +
        "What a session believed at the time is data, and a correction belongs in a later " +
        "handoff rather than in a rewrite of an earlier one. The coverage sidecar beside it is " +
        "keyed by LINE NUMBER: rewriting a line in place keeps the key and silently re-points " +
        "its verdict at different text, while the gate still reports INGEST COMPLETE.")
} elseif ($inWiki) {
    # ONCE PER SESSION, NOT ONCE PER PAGE. The scope of this branch is unchanged - it still trips on
    # every wiki write, and narrowing it was rejected: when this hook's scope and the written rule
    # last disagreed, the owner ruled the HOOK's scope was right and moved the text up to meet it.
    # What changes is the channel. An ingest writes about fifty pages, so the librarian was reading
    # this same paragraph fifty times in its own context, and an alarm that fires when nothing is
    # wrong is one you learn not to read.
    #
    # WITHOUT A SESSION IDENTIFIER IT ALWAYS SPEAKS. A repeat can only be recognised against a
    # session, so a payload carrying none gets the note every time - which is the safe direction and
    # is also why every existing selftest case, none of which sends a session_id, is unaffected.
    #
    # AND THE PER-FOLDER SCHEMAS ARE EXCEPTED, because the note is simply FALSE there: a
    # `wiki/*/_schema.yaml` is the session's to write by the decision of 2026-08-19, and telling a
    # session to stop and dispatch the librarian for a file it owns is an alarm that fires when
    # nothing is wrong - the same defect the once-per-session channel was built against
    # ([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]).
    #
    # SILENCED INSIDE THE BRANCH RATHER THAN BY NARROWING THE `elseif`. The branch that used to win
    # this path still wins it and simply says nothing, so the case pinning `an earlier branch still
    # wins its path` cannot be moved by this change. Narrowing the condition would let a schema
    # write fall through to the branches below and pick up a note meant for something else.
    if ($isSchema) {
        $note = $null
    } elseif ($sessionId -and $state -and $state.WikiNote) {
        $note = $null
    } else {
        $note = ("You are writing to the vault's wiki. It has exactly one writer, the " +
            "vault-librarian agent - a second writer is how a knowledge base starts disagreeing " +
            "with itself. If you are the librarian, this is your job: proceed. If you are not, " +
            "stop and dispatch it instead.")
        $gaveWikiNote = $true
    }
} elseif ($isRegister) {
    $note = ("You are writing to one of the vault's registers. The librarian owns all of " +
        "them, and brief.md is derived: it is regenerated by /ingest and is never a source, " +
        "so a hand edit that survives a session is immediate divergence. If the brief is " +
        "wrong, fix the vault or the ingest skill. If you are the librarian, proceed.")
} elseif ($p -like '*CLAUDE.md') {
    $note = ("You are editing a file that carries a project rule. Before you weaken, " +
        "remove or work around a written rule, run /vault-ask about it. All three recorded " +
        "divergences in this project looked like the rule seemed unnecessary. If you have " +
        "already consulted the vault, proceed.")
} elseif (($scoped = Get-ScopedRules $p $root)) {
    # Last in the chain, and the scan runs only if nothing above matched - so the branch costs
    # its 17 ms on the paths that reach it and nothing on the ones that do not. The consequence
    # is that a rule scoped at a vault path or at CLAUDE.md would be shadowed by the branch above
    # it. Nothing scopes there today; a rule that did would need this chain to accumulate its
    # notes rather than pick one, and that is a change to make when there is such a rule.
    $note = $scoped
}

# THE NET, AND IT IS NOT THE RITUAL. The ritual is /pre-task before a plan is presented, and the
# hook that asks for it sits on ExitPlanMode, where a finished plan exists and no source has been
# touched. This is the backstop for the paths that never pass through a plan at all: a session that
# left plan mode by hand - no hook event exists for a permission-mode change, so that transition is
# invisible - or one that started in another mode because the setting that would have started it in
# plan mode lives in VS Code user settings and cannot be committed to this repository.
#
# THE VAULT IS EXCLUDED, ALL FOUR OF ITS PATH CLASSES. The librarian writes only the vault, and a
# vault write is not implementation: it is governed by the one-writer rule and by the branches
# above, not by this one. Excluding it is what keeps an agent that writes fifty pages per ingest out
# of a ritual it structurally cannot perform - it executes a brief someone else planned.
#
# ONCE PER SESSION AND NEVER AGAIN. The first write is where a missing pre-task is still cheap to
# repair; the fiftieth is nagging about a decision taken long ago.
#
# THE FIRST WRITE IS RECORDED WHETHER OR NOT ANYTHING IS OWED, and that line is the heartbeat: a
# session that edited files and left no line here has hooks that never loaded, which no static
# check of settings.json can detect, because the file on disk is correct in exactly that case.
# A SESSION IDENTIFIER IS REQUIRED HERE, AND THAT IS NOT THE SAME CHOICE THE WIKI NOTE MAKES ABOVE.
# `once per session` is undefined without a session: with no identifier nothing can be recognised as
# a repeat, so this would speak on EVERY edit - which is the exact noise this design exists to
# avoid, and it would arrive attached to a ritual the reader has no way to satisfy. The wiki note
# can afford to repeat because repeating is merely annoying; the net cannot, because repeating is
# its failure mode.
#
# Measured: without this condition, eight cases that assert the guard's SILENCE went red at once -
# every one of them a payload with no session, which is what a fabricated payload looks like. A real
# payload always carries one.
if ($state -and $sessionId -and -not ($isRaw -or $inWiki -or $isRegister)) {
    try {
        $owed = Test-PreTaskOwedForWrite $state

        # THE COLUMN SAYS WHETHER A PRE-TASK IS ON THE RECORD, NOT WHETHER ONE IS OWED. Those come
        # apart on the second write of a session that skipped the ritual: nothing is owed any more,
        # because the advisory was already given, and writing `not owed` into a column a human reads
        # as `the ritual ran` turns the artefact into the opposite of what it is for. Caught by
        # reading the real ledger rather than the tests.
        if (-not $state.FirstWrite) {
            Add-LedgerLine -root $root -sessionId $sessionId -event 'first-write' `
                -permissionMode $permMode -preTask ([bool] $state.PreTaskAt) -path $path
        }

        if ($owed) {
            Add-LedgerLine -root $root -sessionId $sessionId -event 'advised-write' `
                -permissionMode $permMode -preTask $false -path $path

            $net = 'This is the first write of this session and no /pre-task has run. No plan was ' +
                'presented for approval either, so the ritual was never asked for at the moment it ' +
                'is worth most. It is late now but not too late: what a pre-task returns is a ' +
                'constraint the plan had already assumed away, and that is still cheaper to find ' +
                'here than after the change is built on it.'

            $rule = Get-PreTaskMessage $root
            if ($rule) { $net = $net + "`n`n" + $rule }

            if ($note) { $note = $note + "`n`n" + ('-' * 60) + "`n`n" + $net }
            else       { $note = $net }
        }
    } catch { }
}

if ($gaveWikiNote -and $state) {
    try {
        Add-LedgerLine -root $root -sessionId $sessionId -event 'wiki-note' `
            -permissionMode $permMode -preTask $false -path $path
    } catch { }
}

# One note, one JSON object, one write to stdout.
if ($note) { Write-Note $note }

exit 0
