# SessionStart hook. Prints the vault's brief so that a new session starts knowing where the
# work stands, without anyone remembering to ask for it.
#
# This prints; it never generates. The brief is written at the end of the previous session by
# /ingest, while the owner is still in context and can see it lie. A SessionStart hook is a
# shell command whose stdout is injected - it cannot dispatch a subagent - and both
# alternatives (a headless run, or an injected "call the librarian first" instruction) charge a
# round trip before the first line is typed. Printing is deterministic, cannot fail and costs
# nothing.
#
# What it does check is whether the brief still describes the work. The ingest stamps it with
# the commit it was generated at and with the journal it was generated from; if HEAD has moved,
# or if a newer journal exists that the brief has never seen, the first thing the session reads
# is that fact. This exists because the branch that built the vault ended with a brief six
# commits old that said task 10 was not done, the skills were uncommitted and sprint.md did not
# exist - all three false, and a session believing them would either redo finished work or
# "restore" a file it thought had been truncated.
#
# THE BRIEF IS PRINTED WHATEVER ELSE HAPPENS. Every check below sits in its own try/catch and
# contributes at most a warning line, because the first version of the staleness check called
# `git` from inside the printing path: on a machine where git is not on the hook's PATH - and a
# hook is spawned by the harness, not by an agent's shell, a difference this project has already
# been bitten by once - the session got a PowerShell error where its brief should have been. A
# check that can cost the reader the thing it is checking is worse than no check.
#
# Every path is derived from this script's own location, not from the working directory and not
# from a hard-coded name. This file is pure ASCII: a .ps1 without a BOM is read in the ANSI
# codepage.

# The console this runs on is cp1252, and Windows PowerShell reads and writes in that codepage
# unless told otherwise. Without this the brief arrives in the session's context with every em
# dash and every Cyrillic word replaced by rubbish - the same failure
# `sys.stdout.reconfigure(encoding="utf-8")` exists for in our entry points. The case is in
# scripts/hook-selftest.ps1, which builds that text from char codes.
try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch { }

# AND THE INPUT SIDE, which this file lacked until 2026-08-24 while the five other hooks that
# read stdin all had it. Nothing had bitten yet because every field taken from the payload here
# was ASCII - but `transcript_path` is a user's profile path, and a non-ASCII account name would
# have arrived as rubbish and sent the reader to a file that does not exist. Measured on a probe
# of `MessageDisplay` the same day: without this line a Cyrillic payload comes back as UTF-8
# bytes read in the console codepage.
try { [Console]::InputEncoding = [System.Text.Encoding]::UTF8 } catch { }

# STAMP THE SESSION IDENTIFIER, AND PRINT NOTHING WHILE DOING IT. This hook's stdout is the brief
# itself, so anything written here lands in the session's context.
#
# WHY IT BELONGS HERE. A hook is handed `session_id` in its payload; a script the session runs from
# its shell is handed nothing, and `/pre-task` is such a script - it would otherwise write a ledger
# line under an identifier nothing could read back. Every ledger write refreshes the stamp too, but
# in the intended flow the ritual runs BEFORE any write, so the earliest possible moment is the only
# reliable one.
#
# `IsInputRedirected` FIRST, and it is load-bearing rather than defensive. The selftest runs this
# hook with no stdin attached; `ReadToEnd()` on a live console would sit there waiting for a human,
# and the suite would hang rather than fail - which is the worse of the two.
#
# AND RECORD THE START ITSELF, carrying `source`. Three things rest on that one field. It is the
# instrument for a question nobody had measured - whether a `/clear` keeps the session identifier -
# because two append-only rows can be compared and the stamp, overwritten in place, cannot. It is the
# reset: `Read-LedgerState` drops what this session accumulated before a `clear`, so an approved plan
# stops reading as though it survived a conversation that never saw it. And it is what tells the
# rotation below that this is a NEW session rather than the same one being resumed, compacted or
# cleared.
#
# NO `session_id`, NO ROW. A rate limit, a heartbeat and a scope are all claims about a key; where
# the key does not exist they are not merely loose, they are undefined, and a keyless row is one
# nothing can ever match.
#
# THE WHOLE BLOCK STAYS INSIDE ITS OWN try/catch, which is this file's standing rule rather than
# caution: the brief is printed whatever else happens, because a check that can cost the reader the
# thing it is checking is worse than no check. That has been paid here once already, with `git` off
# the hook's PATH.
try {
    if ([Console]::IsInputRedirected) {
        $payload = [Console]::In.ReadToEnd()
        if ($payload) {
            $parsed = $payload | ConvertFrom-Json
            $sid = $parsed.session_id
            $src = $parsed.source

            # STAMP THE TRANSCRIPT PATH. The harness writes a full record of every session and
            # nothing in this repository had ever read one: 37 files and 255 MB, unread, on
            # 2026-08-24. `scripts/session-dialogue.py` reads it at a retro, and this is the
            # only moment the path is handed to anybody - a script the session runs from its
            # shell is handed nothing.
            #
            # WITHOUT `$sid`, AND DELIBERATELY. The ledger row needs a key; this file is a path
            # and is useful whether or not the payload carried an identifier.
            #
            # The reader falls back to the newest transcript when this file is missing, and it
            # SAYS SO when it does. A fallback that is silent about being a fallback is how a
            # session ends up reading another session's words as its own.
            if ($parsed.transcript_path) {
                $sddDir = Join-Path (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path '.superpowers\sdd'
                if (Test-Path -LiteralPath $sddDir) {
                    Set-Content -LiteralPath (Join-Path $sddDir 'session-transcript.path') `
                        -Value $parsed.transcript_path -Encoding UTF8
                }
            }

            if ($sid) {
                . (Join-Path $PSScriptRoot 'pre-task-state.ps1')
                $hookRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
                Set-SessionStamp $hookRoot $sid

                # ROTATION FIRST, so the fresh ledger opens with the row written just below it.
                # ONLY on `startup`: a resume, a compaction and a clear are the same live session,
                # and filing its rows away underneath it would drop its approved scope mid-flight.
                if ($src -eq 'startup') { Invoke-LedgerRotation $hookRoot }

                # `-preTask` is deliberately NOT passed. Nothing had been asked of the ritual at this
                # moment, so the column carries `-` rather than a `no` that would assert something
                # untrue to whoever reads this file at a retro.
                if (-not $src) { $src = 'unknown' }
                Add-LedgerLine -root $hookRoot -sessionId $sid -event ('session-start:' + $src) `
                    -permissionMode $parsed.permission_mode -path ''
            }
        }
    }
} catch { }

$text = $null
$warnings = @()

try {
    $root = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
    . (Join-Path $PSScriptRoot 'vault-path.ps1')
    $vault = Find-Vault $root

    if ($null -eq $vault) {
        'No vault found in this project: no top-level directory contains a wiki/.'
        exit 0
    }

    $brief = Join-Path $vault.FullName 'brief.md'

    # Test-Path rather than -ErrorAction SilentlyContinue: a missing brief must produce a helpful
    # line and exit 0, not a PowerShell error that surfaces as a hook failure.
    if (-not (Test-Path -LiteralPath $brief)) {
        'No vault brief exists yet. Run /ingest at the end of this session to create one.'
        exit 0
    }

    $text = Get-Content -Raw -Encoding UTF8 -LiteralPath $brief
} catch {
    "The vault brief could not be read: $($_.Exception.Message)"
    exit 0
}

# Only the first few lines are searched for the stamp. Anywhere else in a brief it is
# quotation - and every other reader in this repository strips fences before matching, for
# reasons written at length in scripts/vault-check.sh.
# CR is stripped first: the stamps are matched with `$` anchors and a CRLF file leaves one
# before every line end, so the whole staleness check silently found nothing. Third time this
# project has met that character.
$head = (($text -replace "`r", '') -split "`n" | Select-Object -First 6) -join "`n"

# --- has the tree moved since the brief was written? ------------------------------------
# Asked of git history, not of the stamp. The stamp cannot answer it: a brief is generated,
# then committed, so `generated-at` is always one commit behind by construction and comparing
# it to HEAD would warn every single time - the false alarm this file removed once already,
# from the check beneath it. What is actually being asked is "has anything happened since the
# brief was written", and the commit that carries the brief is the honest zero point.
#
# A brief with uncommitted changes is newer than any commit and therefore never stale. The
# `generated-at:` line stays in the brief as provenance a human can read without running git.
try {
    $rel = $vault.Name + '/brief.md'
    $dirty = & git -C $root status --porcelain -- $rel 2>$null
    if ($LASTEXITCODE -eq 0 -and -not $dirty) {
        $written = & git -C $root log -1 --format=%h -- $rel 2>$null
        if ($LASTEXITCODE -eq 0 -and $written) {
            $since = & git -C $root rev-list --count "$written..HEAD" 2>$null
            if ($LASTEXITCODE -eq 0 -and $since -and [int]$since -gt 0) {
                $warnings += "> **This brief is out of date.** $since commits have landed since it was written at $written."
                $warnings += "> Its State section may describe work that is already done. Run ``git log --oneline $written..HEAD`` before trusting it."
                $warnings += ''
            }
        }
    }
} catch { }

# --- is there a journal no ingest has compiled? ------------------------------------------
# By the sidecar's existence: never by mtime, and never by which name sorts last.
#
# Not by mtime - an earlier version compared timestamps and fired on every fresh clone,
# deterministically: git writes the working tree in index order, so `brief.md` always lands
# microseconds before `raw/handoffs/...`.
#
# Not by name either, and that is the scar of 2026-08-17. The check took the newest journal
# as `Sort-Object Name -Descending | Select-Object -First 1` and compared it against the
# brief's `ingested:`. Two journals of one day sort by their slug rather than by time, so with
# `2026-08-16-the-harness-becomes-a-build.md` and `2026-08-16-the-structure-questioned.md`
# both compiled, the sort returned the earlier one and the alarm fired on a journal that had
# been ingested hours before. A date prefix orders sessions only while there is one a day.
#
# A journal is compiled when its sidecar exists - `<name>.coverage.tsv`, written by the ingest
# that gave every unit a verdict. That is a file-existence test, and no ordering can break it.
# The rule all of this violates is written in vault-check.sh: an alarm that fires on every run
# and cannot be acted on is one you learn not to read.
try {
    $uningested = @(Get-ChildItem -LiteralPath (Join-Path $vault.FullName 'raw/handoffs') -Filter '2*.md' `
                        -ErrorAction SilentlyContinue |
                    Where-Object { -not (Test-Path -LiteralPath ($_.FullName -replace '\.md$', '.coverage.tsv')) })
    if ($uningested.Count -gt 0) {
        $warnings += "> **A journal exists that no ingest has compiled** - $(($uningested | ForEach-Object Name) -join ', ')."
        $warnings += '> A session wrote its journal and did not run /ingest. Read that file before trusting'
        $warnings += '> anything below.'
        $warnings += ''
    }

    # A brief naming a journal that is not there is a brief to distrust outright - it was built
    # from something that has since moved, or from nothing.
    #
    # RESOLVED IN TWO PLACES SINCE 2026-08-21. `/ingest` archives the journal it compiled as its
    # last step, so `raw/handoffs/<name>` stops existing the moment an ingest finishes. Looking only
    # there would fire this alarm on EVERY session start - the exact class of false alarm this file
    # has already removed twice, and the one the store has a rule about. The filename is the
    # identity and survives the move; where the file lives is not what this check is asking.
    $ing = [regex]::Match($head, '(?m)^ingested:[ \t]*(\S+)[ \t]*$')
    if ($ing.Success) {
        $journalName = $ing.Groups[1].Value
        $journalFound = Test-Path -LiteralPath (Join-Path $vault.FullName "raw/handoffs/$journalName")
        if (-not $journalFound) {
            # -Filter rather than -Include: in 5.1 -Include returns nothing unless the path itself
            # ends in a wildcard, and silence here reads exactly like the journal being absent.
            $archived = @(Get-ChildItem -LiteralPath (Join-Path $vault.FullName 'archive') `
                            -Filter $journalName -Recurse -File -ErrorAction SilentlyContinue)
            $journalFound = ($archived.Count -gt 0)
        }
        if (-not $journalFound) {
            $warnings += "> **This brief names a journal that does not exist** - $journalName."
            $warnings += '> Not in raw/handoffs/ and not under archive/. Read the vault before'
            $warnings += '> trusting anything below.'
            $warnings += ''
        }
    }
} catch { }

$warnings
$text

exit 0
