# UserPromptSubmit reminder. Speaks only when the VAULT-FEEDBACK channel has gone quiet for three
# of the owner's prompts in a row, and says nothing at all while it is being used.
#
# WHY THIS EVENT, ON THE OWNER'S CORRECTION OF 2026-08-28. The first build of this file fired on
# `PostToolUse` when /grill-me was invoked - once, at the door. He replaced it: the thing that must
# not be lost is the ruling HE writes, and that arrives with HIS prompt, so the reminder belongs at
# the moment the ruling lands rather than at the moment a conversation opens.
#
# WHY IT COUNTS RATHER THAN SPEAKING EVERY TIME, AND THIS IS THE WHOLE DESIGN. Two defences against
# this failure were built before this one and both fire unconditionally: a rendered rule read once
# at invocation, and a demand at the head of `remind-the-smoke.ps1`. Neither stopped anything,
# because an unconditional message on every turn is read three times and then becomes furniture. A
# reminder that only speaks when something is actually wrong keeps its meaning, and it makes the
# channel measurable: the number of times this hook spoke in a session is a reading, and zero means
# the channel worked.
#
# THE SIGNAL IS THE FEEDBACK FILE'S WRITE TIME, and it is a signal this hook does not have to be
# told about. `catch-the-feedback.ps1` writes `.superpowers/sdd/vault-feedback.md` whenever it lifts
# a block out of a reply, so a filed block moves that file's timestamp and nothing else has to be
# coordinated between the two hooks. This hook never writes the feedback file and never reads its
# contents.
#
# IT DOES NOT READ THE PROMPT TEXT, deliberately. Whether a prompt carries a ruling is a judgement,
# and a keyword test for one would fire on `soglasen` and miss a paragraph of reasoning - the exact
# inversion that a vocabulary-keyed test produced when this repository tried to classify citations
# on 2026-08-28. Silence is the condition, not content. It also means the payload's field name for
# the prompt is not needed, which matters: it is the one part of this event that is not confirmed.
#
# WHAT IT DOES NOT DO. It never blocks and it never modifies the prompt. Whether exit 2 could block
# on this event is undocumented and untested here, and a hook that refuses owes a page arguing the
# three conditions - this one refuses nothing, so it owes none.
#
# THE COUNTER RESETS WHEN IT SPEAKS, so it says its piece on every third quiet prompt rather than on
# every prompt after the third. The second shape is the furniture this design exists to avoid.
#
# THIS FILE IS PURE ASCII ON PURPOSE. Windows PowerShell 5.1 reads a .ps1 in the system ANSI
# codepage unless it carries a BOM, so a literal em dash arrives as mojibake and can break parsing.
# Message text is single-quoted because in a double-quoted PowerShell string a backtick is an
# escape, and this repository has shipped four instances of that.

try { [Console]::InputEncoding  = [System.Text.Encoding]::UTF8 } catch { }
try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch { }

# THE THRESHOLD IS THREE AND IT IS A GUESS, stated as one. Nothing has measured how long the channel
# may be quiet before a ruling is lost; three is short enough to catch the failure of 2026-08-28 at
# its fourth turn and long enough that an ordinary working session never hears from this file. The
# number to revisit is this one, and the reading that would revisit it is how often it speaks.
$QUIET_LIMIT = 3

# AND FIVE FOR THE SESSION'S OWN REPLIES, ALSO A GUESS AND ALSO SAID TO BE ONE. It is a different
# unit from the three above rather than a different opinion about the same one: replies outnumber
# the owner's prompts several times over in a working session, so three of them is a much shorter
# window than three of his. Owner's choice, 2026-08-29.
$REPLY_LIMIT = 5

# ONE FILE, TWO EVENTS FROM 2026-08-29, SO THE REPLY MUST NAME THE EVENT IT IS ANSWERING.
# `hookSpecificOutput` carries `hookEventName` and a reply naming the wrong event is dropped by the
# harness without saying so. The default is `UserPromptSubmit`: that is the shape this file has
# always had and the shape every existing case sends, so a payload without the field behaves exactly
# as it did before.
$eventName = 'UserPromptSubmit'

function Write-Note([string] $text) {
    @{ hookSpecificOutput = @{ hookEventName = $eventName; additionalContext = $text } } |
        ConvertTo-Json -Depth 4
}

$raw = [Console]::In.ReadToEnd()
if ([string]::IsNullOrWhiteSpace($raw)) { exit 0 }
try { $payload = $raw | ConvertFrom-Json } catch { exit 0 }

# THE EVENT IS READ OFF THE PAYLOAD'S SHAPE AND NOT OFF `hook_event_name`. A tool event carries
# `tool_name` and a prompt event does not, which is the same test `remind-the-smoke.ps1` has always
# used. `hook_event_name` was tried first and is the wrong reader here: the selftest's own tool
# payload does not carry it, so a branch keyed on it would never run in a case and would be decided
# in production by a field nothing in this repository has measured on this event.
$isToolEvent = ($payload.tool_name -is [string])
if ($isToolEvent) { $eventName = 'PostToolUse' }

# THE RITUAL BRANCH, AND THIS FILE NOW OWNS THE REQUIREMENT FOR BOTH EVENTS (2026-08-29). The same
# demand used to be written out twice - in prose at the head of `remind-the-smoke.ps1` for `/retro`,
# and in full here for every prompt - and two copies of one text drift, with the repair landing on
# one of them. The smoke reminder keeps the smoke half, which is its own subject, and lost this.
#
# IT IS NOT COUNTER-GATED, and that is the difference between the two halves rather than an
# oversight. The counter below is about a session that has been DRIFTING; a ritual that has just
# opened has no silence to count yet, and the door is the moment the demand is worth making.
#
# THE RITUAL IS NAMED RATHER THAN ASSUMED. Only `/retro` has an obligation of its own today, and a
# second one arriving is a new arm here rather than a second file. A plugin-scoped invocation
# arrives as `<plugin>:retro`, so the tail identifies it; the narrowing lives in the body because a
# matcher can only name the tool.
if ($isToolEvent) {
    if ($payload.tool_name -ne 'Skill') { exit 0 }
    $skill = $null
    if ($payload.tool_input) { $skill = $payload.tool_input.skill }
    if ($skill -isnot [string]) { exit 0 }
    $skill = $skill.Trim()
    if ($skill -ne 'retro' -and -not $skill.EndsWith(':retro')) { exit 0 }

    Write-Note ('FILE A `VAULT-FEEDBACK` BLOCK IN EVERY TURN OF THIS RETRO. Not once at the end ' +
        'and not folded into the retro file - in the turn the thing happens, as the rule says ' +
        'everywhere else. This is the ritual where the channel has failed three times: a retro ' +
        'once ran eight exchanges carrying twenty-one decisions and filed nothing, and the retro ' +
        'after it ran nine replies with nothing. A retro writes an artefact of its own, which is ' +
        'exactly why recording feels already done and is not: that file holds what was RESOLVED, ' +
        'the block holds what was OBSERVED. A turn that genuinely produced nothing recordable ' +
        'says so in a line.')
    exit 0
}

# The prompt event carries no matcher, so every prompt of every session reaches this line.
# Everything below is the narrowing.
$sessionId = ''
try { if ($payload.session_id -is [string]) { $sessionId = $payload.session_id } } catch { }

$root = $null
try { $root = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path } catch { exit 0 }

$sdd = Join-Path $root '.superpowers\sdd'
if (-not (Test-Path -LiteralPath $sdd)) { exit 0 }

$feedback = Join-Path $sdd 'vault-feedback.md'
$statePath = Join-Path $sdd '.feedback-silence'

# Ticks rather than a formatted date: a culture-dependent string parsed back is a bug waiting for a
# machine with a different locale, and this repository has already paid for one locale assumption.
$fbTicks = 0
try {
    if (Test-Path -LiteralPath $feedback) {
        $fbTicks = (Get-Item -LiteralPath $feedback).LastWriteTimeUtc.Ticks
    }
} catch { $fbTicks = 0 }

# THE SESSION'S OWN REPLIES, COUNTED NEXT DOOR. `catch-the-feedback.ps1` runs on every assistant
# message and writes this number; it cannot speak, measured 2026-08-29, so it counts and this file
# says the sentence. Absent or unreadable means zero, which is the state of every fixture that does
# not exercise this half and of every session before the counter existed.
$replies = 0
try {
    $replyState = Join-Path $sdd '.reply-silence'
    if (Test-Path -LiteralPath $replyState) {
        $rline = (Get-Content -LiteralPath $replyState -First 1 -ErrorAction Stop)
        if ($rline) { [void][int]::TryParse(($rline -split "`t")[0].Trim(), [ref] $replies) }
    }
} catch { $replies = 0 }

$storedSession = ''
$storedTicks   = 0
$quiet         = 0
$spokenAt      = 0
try {
    if (Test-Path -LiteralPath $statePath) {
        $line = (Get-Content -LiteralPath $statePath -First 1 -ErrorAction Stop)
        if ($line) {
            $parts = $line -split "`t"
            if ($parts.Count -ge 3) {
                $storedSession = $parts[0]
                [void][int64]::TryParse($parts[1], [ref] $storedTicks)
                [void][int]::TryParse($parts[2], [ref] $quiet)
            }
            # A FOURTH FIELD, ADDED 2026-08-29, AND AN OLDER THREE-FIELD LINE STILL PARSES. It is
            # the reply count this hook last spoke about, which is how the reply half avoids
            # repeating itself without writing to the file the other hook owns: each hook writes
            # only its own state.
            if ($parts.Count -ge 4) { [void][int]::TryParse($parts[3], [ref] $spokenAt) }
        }
    }
} catch { $storedSession = ''; $storedTicks = 0; $quiet = 0; $spokenAt = 0 }

# A new session starts its own count. Carrying a previous session's quiet run forward would make the
# first prompt of a fresh session speak for something that happened yesterday.
if ($storedSession -ne $sessionId) { $storedTicks = $fbTicks; $quiet = 0; $spokenAt = $replies }

# A block was filed since the last prompt: the channel is working, so the count goes back to zero.
if ($fbTicks -gt $storedTicks) { $storedTicks = $fbTicks; $quiet = 0 }

$quiet = $quiet + 1
$speakQuiet = ($quiet -ge $QUIET_LIMIT)

# THE REPLY HALF ASKS HOW MANY REPLIES HAVE PASSED SINCE IT LAST SPOKE, not how many there are. The
# other hook resets its count only when a block is filed, so a count that stayed above the limit
# would make this speak on every prompt from then on - the furniture this whole design exists to
# avoid. Comparing against what was last spoken about gives the same silence-then-speak rhythm the
# prompt half has, in a unit this file does not own and must not write.
$speakReplies = (($replies - $spokenAt) -ge $REPLY_LIMIT)

$speak = ($speakQuiet -or $speakReplies)
if ($speakQuiet) { $quiet = 0 }
if ($speakReplies) { $spokenAt = $replies }

try {
    [System.IO.File]::WriteAllText($statePath,
        ($sessionId + "`t" + $storedTicks + "`t" + $quiet + "`t" + $spokenAt + "`n"),
        (New-Object System.Text.UTF8Encoding($false)))
} catch { }

if (-not $speak) { exit 0 }

# THE REPLY HALF SAYS WHAT IT COUNTED, because the two conditions are about different things and a
# session told the wrong number looks for the wrong thing. It is deliberately not folded into the
# prompt message: that one names the owner's prompts, which is a fact about him, and this one names
# the session's own replies, which is a fact about the session.
if ($speakReplies) {
    Write-Note ('YOU HAVE WRITTEN ' + ($replies - 0) + ' REPLIES SINCE THE LAST `VAULT-FEEDBACK` ' +
        'BLOCK WAS FILED. That is what this line means and it means nothing else - no hook has ' +
        'read what you wrote or judged it.' + "`n`n" +
        'This counter exists because the one beside it counts the OWNER''S prompts, so a long ' +
        'stretch of the session working alone registers as a single quiet prompt however many ' +
        'replies it contained. It arrives late by construction: the event that can see your ' +
        'replies cannot speak, measured 2026-08-29, so this is said at his next prompt.' + "`n`n" +
        'Look back over those replies for what should have been filed - a RULING above all, but ' +
        'also a measurement you took, a miss the vault handed you, or a change to the files that ' +
        'instruct an agent. If they genuinely carried nothing recordable, that is a legitimate ' +
        'answer and costs one line saying so.')
    exit 0
}

Write-Note ('THE `VAULT-FEEDBACK` CHANNEL HAS BEEN QUIET FOR THREE OF THE OWNER''S PROMPTS. That ' +
    'is what this line means and it means nothing else - no hook has read what you wrote or ' +
    'judged it.' + "`n`n" +
    'Look back at those three prompts for RULINGS, which is the kind that goes missing. Measured ' +
    '2026-08-28: a session ran eleven owner answers and filed zero `decision:` lines while filing ' +
    '`measure:` and `miss:` lines freely throughout. The findings were recorded and the rulings ' +
    'were not, and it surfaced only because he asked whether anything had been missed.' + "`n`n" +
    'Name the shape of each ruling, which is what the line is for: the owner SAID it in his own ' +
    'words, the owner SELECTED it from something you put to him, or the session UNDERSTOOD it from ' +
    'what he did. An agreement to a recommendation you wrote is SELECTED and never SAID, and his ' +
    'own sentence is never demoted to understood.' + "`n`n" +
    'If those three prompts genuinely carried nothing recordable, that is a legitimate answer and ' +
    'costs one line saying so. This reminder returns after three more quiet prompts.')

exit 0
