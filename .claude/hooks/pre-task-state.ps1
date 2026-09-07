# Shared state for the pre-task ritual. Dot-sourced by the hooks that read and write it; it is
# NOT itself registered in settings.json and must never be, for the same reason vault-path.ps1 is
# not: a library that runs as a hook would answer every payload with silence and look identical to
# a hook that had nothing to say.
#
# WHAT THIS IS FOR. `/pre-task` leaves no artefact. The rule page says so in its own words - "nothing
# in the tree records whether a plan was checked before it was written" - and that is why three
# skips in two sessions were each found at a retro, from memory, rather than by anything mechanical.
# This file is the artefact. It does not prevent a skip; it makes one findable.
#
# ONE FILE, THREE JOBS, ON PURPOSE:
#   1. the record of a skipped ritual, drained by /handoff into the journal;
#   2. the HEARTBEAT that proves the hooks ran at all - a session that edited files and wrote no
#      line here has hooks that are not loaded, which no static check of settings.json can see;
#   3. the record of which permission mode the session ACTUALLY started in, because the VS Code
#      extension reads `claudeCode.initialPermissionMode` from user settings and ignores this
#      repository's `.claude/settings.json` entirely.
#
# APPEND-ONLY, TSV, AND DERIVED STATE. There is no separate state file. The state is read back out
# of the lines, so the record and the thing it records cannot drift apart. Appending is also what
# survives two writers: a subagent and its parent may both write, and `Add-Content` of one short
# line does not lose the other's, while a read-modify-write of a state file silently would - this
# project has that exact scar in `tags.md`.
#
# PURE ASCII ON PURPOSE. Windows PowerShell 5.1 reads a .ps1 in the system ANSI codepage unless it
# carries a BOM, so a literal em dash here arrives as mojibake and can break parsing outright.
#
# SINGLE-QUOTED STRINGS FOR ANY TEXT CARRYING A BACKTICK. In a double-quoted PowerShell string a
# backtick is an escape character, and this project has shipped that bug four times in two sessions,
# every time failing towards something plausible. Message text lives in single quotes or in a
# single-quoted here-string, never in double quotes.

# NO `Set-StrictMode` HERE. This file is dot-sourced, and a mode set inside a dot-sourced file lands
# in the CALLER's scope - it would silently change how `ask-the-vault.ps1` behaves on payloads that
# have nothing to do with the pre-task ritual. Changing a working file's behaviour as a side effect
# of adding something beside it is the divergence this session's predecessor recorded.

# The override exists for the selftest and for nothing else: a suite is a test environment and works
# in its own sandbox, so it never reaches into the real file. Deriving the path from `cwd` was
# rejected - `cwd` arrives in the payload the test itself fabricates, so the subject would be
# isolated by the very thing under test.
function Get-LedgerPath([string] $root) {
    if ($env:JOBHUNT_PRETASK_LEDGER) { return $env:JOBHUNT_PRETASK_LEDGER }
    return (Join-Path $root '.superpowers\sdd\pre-task-ledger.tsv')
}

# THE SESSION STAMP EXISTS BECAUSE THE RITUAL CANNOT SEE ITS OWN SESSION. A hook is handed
# `session_id` in its payload; a script the session runs from its shell is handed nothing. So
# `/pre-task` could write a line it could never key correctly, and the state it set would be read
# back by nobody.
#
# The stamp is written by whatever last proved it knew the identifier - the SessionStart hook, and
# every ledger write after it. One line, overwritten, never appended to: there is exactly one
# current session per working copy.
#
# TWO SESSIONS IN ONE WORKING COPY WOULD SHARE IT, and the second would stamp over the first. The
# consequence is bounded: a pre-task recorded under the wrong identifier reads as not-run for the
# session that ran it, so the ritual is asked for again. It fails towards asking twice rather than
# towards recording something that did not happen.
function Get-StampPath([string] $root) {
    $ledger = Get-LedgerPath $root
    return ($ledger + '.session')
}

function Set-SessionStamp([string] $root, [string] $sessionId) {
    if (-not $sessionId) { return }
    try {
        $stamp = Get-StampPath $root
        $dir = Split-Path -Parent $stamp
        if ($dir -and -not (Test-Path -LiteralPath $dir)) {
            New-Item -ItemType Directory -Path $dir -Force | Out-Null
        }
        $enc = New-Object System.Text.UTF8Encoding($false)
        [System.IO.File]::WriteAllText($stamp, $sessionId, $enc)
    } catch { }
}

function Get-SessionStamp([string] $root) {
    try {
        $stamp = Get-StampPath $root
        if (-not (Test-Path -LiteralPath $stamp)) { return $null }
        return ([System.IO.File]::ReadAllText($stamp)).Trim()
    } catch { return $null }
}

# Six columns, in the order the owner named them. A tab separator rather than JSON because every
# reader of this file is either a human at a retro or a `-split` in a hook, and neither is helped
# by a parser.
function Add-LedgerLine {
    param(
        [string] $root,
        [string] $sessionId,
        [string] $event,
        [string] $permissionMode,
        [object] $preTask,
        [string] $path
    )
    $ledger = Get-LedgerPath $root
    $dir = Split-Path -Parent $ledger
    if ($dir -and -not (Test-Path -LiteralPath $dir)) {
        try { New-Item -ItemType Directory -Path $dir -Force | Out-Null } catch { return }
    }

    # A timestamp the hook reads off the clock rather than one passed in: this line is the evidence
    # that the hook ran, and evidence that takes its own time from its caller proves less.
    $ts = (Get-Date).ToString('yyyy-MM-ddTHH:mm:ss')
    if (-not $sessionId) { $sessionId = 'unknown' }
    if (-not $permissionMode) { $permissionMode = 'unknown' }
    # THREE STATES, BECAUSE `no` IS A CLAIM ABOUT THE WORLD. Both `yes` and `no` assert something to
    # the human reading this at a retro: that a pre-task was on the record, or that it was not. A
    # `session-start` row asserts neither - nothing had been asked of the ritual at the moment it is
    # written - so it carries `-`. Writing `no` there would be the same defect this ledger already
    # shipped once, a column filled from the branch condition that produced it rather than from the
    # world.
    #
    # `[object]` RATHER THAN `[bool]` IS WHAT MAKES OMITTING IT MEAN `-`, and it leaves every caller
    # that passes a real boolean untouched: `$false` is not `$null`, so `no` still reaches the file
    # from the five places that mean it.
    $flag = '-'
    if ($null -ne $preTask) {
        if ($preTask) { $flag = 'yes' } else { $flag = 'no' }
    }

    # Tabs and newlines in a path would break the column count for every later reader, so they are
    # flattened here rather than at each read site.
    $safe = ''
    if ($path) { $safe = ($path -replace "[`t`r`n]", ' ') }

    # NOT `Add-Content -Encoding UTF8`. In Windows PowerShell 5.1 that writes a BOM when it creates
    # the file, and the BOM lands in front of the first line's first field - which is the timestamp
    # the plan path compares. Measured on the first real run: the first row arrived as
    # `<BOM>2026-08-20T20:58:16`, and a comparison against that is a comparison against a different
    # string than the one that was written. `AppendAllText` with a UTF8Encoding constructed as
    # `$false` emits no BOM on creation or on append, and LF alone keeps the file the same bytes on
    # any reader.
    $line = @($ts, $sessionId, $event, $permissionMode, $flag, $safe) -join "`t"
    try {
        $enc = New-Object System.Text.UTF8Encoding($false)
        [System.IO.File]::AppendAllText($ledger, ($line + "`n"), $enc)
    } catch { }

    # Every ledger write refreshes the stamp, so the identifier a script can read is the one that
    # most recently proved it was live. Cheaper than a second mechanism and it keeps working in a
    # session that started before this file existed.
    Set-SessionStamp $root $sessionId
}

# ONE SESSION PER LEDGER. The file is rotated WHOLE at the start of a session and is never pruned in
# place. A rename is the only write that cannot lose a concurrent appender's line the way a
# read-modify-write can, and this project lost a line in `tags.md` exactly that way; keeping the
# append-only rule intact was the point of the file.
#
# CALLED ONLY WHEN `source` IS `startup`. A `resume`, a `compact` and a `clear` are the SAME live
# session: filing its rows away underneath it would drop its approved scope mid-flight, and the guard
# would then ask for a ritual that had already run.
#
# NOT AT THE END OF A SESSION, which is where the owner first placed it. The closing ritual can be
# skipped and has been - three times in two sessions, which is why this ledger exists at all - and it
# does not touch this file today, although two vault pages say `/handoff` drains it. A trigger that
# fires mechanically beats one that fires when someone remembers.
#
# NOTHING WATCHES A ROTATION THAT FAILS, and that is the price of doing it at session start. If the
# move throws, the catch below swallows it, the ledger simply keeps growing, and no reader is told.
# `.superpowers/` is git-ignored, so no sweep of the tree finds it either - this repository has
# already measured that blind spot, on `vault-feedback.md`.
#
# TWO SESSIONS IN ONE WORKING COPY: the second one's startup files the first one's live rows away.
# The first is then asked for a `/pre-task` again - a miss in the direction of asking twice, never of
# staying silent, and the same bounded consequence already recorded for the shared session stamp.
#
# THE READER'S RACE IS ALREADY HANDLED, and is named here so a later reader does not take it for an
# oversight. `Read-LedgerState` reads this file 71 to 108 times a session; one landing between the
# `Test-Path` and the `Get-Content` in that function hits its try/catch, gets a fresh state, and asks
# for the ritual again. That is the direction a guard is allowed to be wrong in.
function Invoke-LedgerRotation([string] $root) {
    try {
        $ledger = Get-LedgerPath $root
        if (-not (Test-Path -LiteralPath $ledger)) { return }
        if ((Get-Item -LiteralPath $ledger).Length -eq 0) { return }

        # The override may be a bare filename in a test environment, and `Split-Path -Parent` returns
        # an empty string for one. `Join-Path` throws on that, inside a try that would swallow it and
        # leave rotation silently dead.
        $parent = Split-Path -Parent $ledger
        if (-not $parent) { $parent = $root }
        $dir = Join-Path $parent 'ledger'
        if (-not (Test-Path -LiteralPath $dir)) {
            New-Item -ItemType Directory -Path $dir -Force | Out-Null
        }

        # A READABLE NAME, NOT THE SESSION IDENTIFIER. The vault rejected naming an archived session
        # from the harness id, because a UUID names the file something no human can read. Its own
        # naming rule - name it from the journal - cannot be used here: `/handoff` writes that
        # filename at the END of a session and this runs at the start, so it does not exist yet.
        $stamp = (Get-Date).ToString('yyyy-MM-ddTHHmmss')
        $dest = Join-Path $dir ('pre-task-ledger.' + $stamp + '.tsv')
        $n = 2
        while (Test-Path -LiteralPath $dest) {
            $dest = Join-Path $dir ('pre-task-ledger.' + $stamp + '-' + $n + '.tsv')
            $n++
        }

        Move-Item -LiteralPath $ledger -Destination $dest -ErrorAction Stop

        # A POINTER BACK, because the store's habit is a link in both directions and the archive is
        # otherwise findable only by someone who already knows the folder is there. One field, so
        # every reader's `-split` yields fewer than three columns and skips it - the same guard that
        # already skips a short line.
        #
        # `AppendAllText` with a UTF8Encoding constructed as `$false`, never `Add-Content -Encoding
        # UTF8`, which writes a BOM when it CREATES a file. That path used to run once ever; after
        # this function it runs every session, so the BOM hazard stopped being historical.
        $enc = New-Object System.Text.UTF8Encoding($false)
        [System.IO.File]::AppendAllText($ledger, ('# rotated ' + (Split-Path -Leaf $dest) + "`n"), $enc)
    } catch { }
}

# The fresh state, in one function because it is built twice: at the top of a read, and again
# whenever a `/clear` resets it. Two copies would be a field added to one of them.
function New-PreTaskState {
    return [pscustomobject]@{
        PreTaskAt = $null      # the last /pre-task of this session
        ScopeAt   = $null      # the last plan this session had approved
        Advised   = $false     # the write-path advisory has already been given once
        WikiNote  = $false     # the one-writer note has already been given once
        SmokeAt   = $null      # when the last `make smoke` of this session returned
        SmokeCode = $null      # what it returned, as the string the row carries
        # THE PATHS WRITTEN SINCE THAT RUN, AND THE LIST IS EMPTIED BY A SMOKE ROW RATHER THAN
        # FILTERED LATER. A green smoke says the tree was sound at that instant and nothing after;
        # what makes it stale is a write, so the reader needs the writes that came AFTER it and
        # never the ones before. Emptying on the row is what makes the second run of a fix loop
        # clear the first run's writes without anybody comparing timestamps.
        WritesAfterSmoke = @()
        # THE HEARTBEAT KEYS ON ITS OWN LINE AND NOT ON `has this session written anything`. The
        # `pre-task` row is written by a SCRIPT the session runs, not by a hook, so a session that
        # performs the ritual before its first edit - which is the intended order - would have a
        # non-empty record and never write the one line that proves a HOOK ran. The heartbeat would
        # then be missing exactly where everything went right.
        FirstWrite = $false
        # THE FILES A RULE HAS ALREADY BEEN SERVED FOR, added 2026-08-30 with
        # `.claude/hooks/serve-the-rule.ps1`. Keyed by path and not by rule, because the reader is
        # about to touch a file and the question is whether this session has already been told what
        # governs THAT file. A session that edits `CLAUDE.md` eleven times gets the note once, and
        # a reminder that fires every time becomes furniture
        # ([[a-reminder-that-fires-every-time-becomes-furniture-and-a-silence-counter-avoids-it]]).
        #
        # IT IS NEVER EMPTIED. Unlike `WritesAfterSmoke` above, nothing makes a served rule stale
        # inside one session: the rule the reader was handed is still the rule. Across sessions the
        # ledger rotates and the list starts empty, which is the cadence the note wants anyway.
        ServedRuleFiles = @()
    }
}

# The state of one session, derived from its own lines. Other sessions' lines are read past rather
# than filtered out of the file: the ledger is a record of everything, and only the current session
# decides anything.
#
# WHY `/clear` RESETS IT AND `/compact` DOES NOT, and it IS a branch now. A compaction keeps the
# session identifier and changes nothing about the work: the same plan is approved, the same scope is
# open, only the context was squeezed. A `/clear` starts a conversation that knows nothing of the
# approved plan, so whatever this session had accumulated stops being evidence about the conversation
# in front of you.
#
# IT USED TO REST ON A PROPERTY NOBODY HAD MEASURED - that a `/clear` mints a new session identifier,
# so the rows above simply stopped matching and no branch was needed. If it does not, an approved
# plan reads as surviving a conversation that never saw it, and the guard stays silent exactly where
# it should speak. The SessionStart hook now writes a `session-start:<source>` row and the case below
# drops everything this session accumulated before a `clear`. It is correct under either answer: a
# new identifier makes the reset land on a state that is already empty.
#
# THE MEASUREMENT IS STILL OWED, and that row is the instrument for it. The session stamp cannot
# answer it - it is overwritten in place, so there is no `before` to compare - while two append-only
# rows can: run a `/clear` and read the identifiers off the two `session-start` rows.
function Read-LedgerState([string] $root, [string] $sessionId) {
    $state = New-PreTaskState
    if (-not $sessionId) { return $state }

    $ledger = Get-LedgerPath $root
    if (-not (Test-Path -LiteralPath $ledger)) { return $state }

    try { $lines = Get-Content -LiteralPath $ledger -ErrorAction Stop } catch { return $state }

    foreach ($line in $lines) {
        if (-not $line) { continue }
        $col = $line -split "`t"
        if ($col.Count -lt 3) { continue }
        if ($col[1] -ne $sessionId) { continue }
        switch ($col[2]) {
            # THE RESET, AND IT DROPS EVERYTHING RATHER THAN THE SCOPE ALONE. After a `/clear` the
            # conversation has not seen the advisory either, so re-firing it is right; keeping some
            # fields and clearing others would be a second rule to remember for no gain. File order
            # is chronological, so this simply forgets what came before it.
            #
            # `startup`, `resume` and `compact` write their own rows and match none of these cases,
            # which is the point: they are visible in the record without deciding anything.
            'session-start:clear' { $state = New-PreTaskState }
            'first-write'    { $state.FirstWrite = $true }
            'pre-task'       { $state.PreTaskAt = $col[0] }
            'scope-approved' { $state.ScopeAt   = $col[0] }
            'advised-write'  { $state.Advised   = $true }
            'wiki-note'      { $state.WikiNote  = $true }
            # THE DISPATCH ROW DISCHARGES THE RITUAL, AND THE INFERENCE LIVES HERE RATHER THAN IN
            # THE HOOK THAT WRITES IT. `record-the-dispatch.ps1` writes `dispatch:<type>` - what
            # happened - and this line is what decides that a returned `pre-task` dispatch IS the
            # ritual. Keeping the two apart is the same rule the rest of this file runs on: the
            # event column records an observation, the state derives the conclusion, and a reader
            # at a retro can still tell which is which.
            #
            # WHY IT MATTERS THAT A HOOK WRITES IT. `scripts/record-pre-task.ps1` is a write the
            # SESSION performs, and plan mode forbids the session to write - at exactly the moment
            # the rule places the ritual. So the ritual done right left no row and the guard asked
            # for it again. A hook writes during planning; the rows above carrying `plan` prove it.
            'dispatch:pre-task' { $state.PreTaskAt = $col[0] }

            # THE WRITE ROW CARRIES ITS PATH AND NOTHING IS DECIDED ABOUT IT HERE. Whether a path
            # matters is a question about `.gitignore`, which is answered once, in the handoff gate,
            # over the whole list - not per row, on every edit, by spawning git.
            'write' {
                if ($col.Count -ge 6 -and $col[5]) {
                    $state.WritesAfterSmoke = @($state.WritesAfterSmoke) + $col[5]
                }
            }

            # THE SERVED-RULE ROW, and it uses the same path column as the write row above for the
            # same reason: one column meaning one thing across every event is what lets a reader at
            # a retro scan the file without a legend.
            'served-rule' {
                if ($col.Count -ge 6 -and $col[5]) {
                    $state.ServedRuleFiles = @($state.ServedRuleFiles) + $col[5]
                }
            }
        }

        # THE SMOKE ROW IS MATCHED HERE RATHER THAN IN THE SWITCH because it carries the exit code
        # in its own event name - `smoke:0`, `smoke:2` - and the switch above matches exactly. The
        # event column stays an observation, as everything else in this file does: the row says what
        # the run returned, and what that OBLIGES is decided by Get-HandoffRefusal below.
        if ($col[2] -like 'smoke:*') {
            $state.SmokeAt          = $col[0]
            $state.SmokeCode        = $col[2].Substring(6)
            $state.WritesAfterSmoke = @()
        }
    }
    return $state
}

# Why the path to /handoff is closed, or $null if it is open.
#
# THREE STATES AND NOT TWO. A session arrives here having never run smoke, having run it red, or
# having run it green and then written something. All three must be refused and all three must be
# told apart, because the reader is an agent that has to know what to do next, and "run smoke" is
# the wrong instruction for two of them.
#
# `git check-ignore` IS SPAWNED HERE AND NOT PER EDIT. Asking it on every Write and Edit would put a
# git process on each one to guard a single event at the end of a session. It prints back the paths
# that ARE ignored, so what is left over is what counts.
#
# THE PATHS GO AS ARGUMENTS AND NEVER THROUGH `--stdin`, AND THAT IS A MEASUREMENT RATHER THAN A
# PREFERENCE. Measured 2026-08-26 in Windows PowerShell 5.1, in a fresh repository whose .gitignore
# holds `.superpowers/`: `git check-ignore '.superpowers/sdd/retro.md'` exits 0 and prints the path,
# while the same paths piped into `git check-ignore --stdin` exit 1 and print NOTHING. Piping into a
# native command's standard input does not deliver here. The `--stdin` form is the one that reads
# correctly and fails silently - it reports every path as not-ignored, which in this function means
# every write counts and /handoff is refused for ever. It was written that way first and the
# selftest case for the ignored path is what caught it.
#
# CHUNKED, because a command line has a length and a long session writes many files. Exit 1 from
# check-ignore means "none of these are ignored" and is not an error; anything above it is.
#
# IF GIT CANNOT BE RUN AT ALL, EVERY WRITE COUNTS. A gate that fails towards refusing costs a
# three-minute run; one that fails towards opening costs the thing it guards.
function Get-HandoffRefusal([string] $root, $state) {
    if (-not $state.SmokeAt) {
        return ('No `make smoke` has run in this session. Run it now: it is the check that stands ' +
            'between the work and the journal, and /handoff is the point of no return - after it ' +
            'the journal is the librarian''s and nothing here can be fixed.')
    }
    if ($state.SmokeCode -ne '0') {
        return ('The last `make smoke` of this session returned ' + $state.SmokeCode + '. Go back ' +
            'into the retro, fix what it found, and run `make smoke` again. /handoff opens on a ' +
            'green run and on nothing else.')
    }

    $written = @($state.WritesAfterSmoke)
    if ($written.Count -eq 0) { return $null }

    $counting = $written
    try {
        $git = Get-Command git -ErrorAction Stop
        $unique = @($written | Select-Object -Unique)
        $ignored = @()
        $answered = $true
        for ($i = 0; $i -lt $unique.Count; $i += 100) {
            $last  = [Math]::Min($i + 99, $unique.Count - 1)
            $chunk = @($unique[$i..$last])
            $res = & $git.Source -C $root check-ignore -- @chunk
            if ($LASTEXITCODE -gt 1) { $answered = $false; break }
            if ($res) { $ignored += $res }
        }
        if ($answered) {
            $counting = @($written | Where-Object { $ignored -notcontains $_ })
        }
    } catch { }

    if ($counting.Count -eq 0) { return $null }

    $shown = ($counting | Select-Object -Unique -First 5) -join ', '
    return ('`make smoke` was green at ' + $state.SmokeAt + ', and ' + $counting.Count +
        ' file(s) git tracks were written after it: ' + $shown + '. A green run says the tree was ' +
        'sound at that instant and nothing after it. Run `make smoke` again - it must be the last ' +
        'thing before /handoff.')
}

# Is the ritual owed right now?
#
# THE PLAN PATH asks for a pre-task that is NEWER than the last approved scope. A pre-task belongs
# to the plan it checked; once that plan is approved and the scope closes, the next plan is a
# different plan and inherits nothing. Comparing timestamps as strings is exact here because the
# format is fixed-width ISO-like and lexical order is chronological order.
function Test-PreTaskOwedForPlan($state) {
    if (-not $state.PreTaskAt) { return $true }
    if (-not $state.ScopeAt)   { return $false }
    return ($state.PreTaskAt -le $state.ScopeAt)
}

# THE WRITE PATH is the net and not the ritual: it asks only whether this session ever passed
# through either gate. A session with an approved scope has been through the plan path already, and
# nagging it at its first write would fire on every session that did the right thing.
function Test-PreTaskOwedForWrite($state) {
    if ($state.Advised)   { return $false }
    if ($state.PreTaskAt) { return $false }
    if ($state.ScopeAt)   { return $false }
    return $true
}

# The rule's text, read at runtime from the file the injector generates from the vault page. There
# is deliberately no fallback copy of the words here: a second copy is how a rule starts disagreeing
# with itself, and it is the whole reason the text lives in the vault and is rendered rather than
# written twice.
#
# WHEN THE FILE IS MISSING the hook says so loudly instead of going quiet. A guard that is silently
# absent is worse than none - this repository has shipped that once and now says it out loud in
# three places.
function Get-PreTaskMessage([string] $root) {
    $file = Join-Path $root '.claude\hooks\messages\pre-task.md'
    if (-not (Test-Path -LiteralPath $file)) {
        return ('THE PRE-TASK RULE COULD NOT BE DELIVERED: ' + $file + ' does not exist. It is ' +
            'generated from the vault by scripts/vault-inject.sh, so either the injector has not ' +
            'run or the rule page no longer governs this path. Treat this message as the finding ' +
            'and repair it; a rule that cannot be delivered is a rule that is not there.')
    }

    # The generated file leads with an HTML marker and may carry a frontmatter block; neither is the
    # rule. Stripping happens here rather than in the generator because the generated form is
    # defined once, in the injector, and is read by its own comparison - a second writer of that
    # form is exactly what the injector's comment forbids.
    try { $lines = Get-Content -LiteralPath $file -ErrorAction Stop } catch { return $null }

    $out = New-Object System.Collections.ArrayList
    $i = 0
    if ($lines.Count -gt 0 -and $lines[0].TrimEnd() -eq '---') {
        $i = 1
        while ($i -lt $lines.Count -and $lines[$i].TrimEnd() -ne '---') { $i++ }
        $i++
    }
    for (; $i -lt $lines.Count; $i++) {
        $t = $lines[$i]
        if ($t -match '^\s*<!--' -and $t -match '-->\s*$') { continue }
        [void] $out.Add($t)
    }
    return (($out -join "`n").Trim())
}
