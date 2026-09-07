# MessageDisplay hook. Lifts a fenced VAULT-FEEDBACK block out of the session's own reply and
# files it in `.superpowers/sdd/vault-feedback.md`, so that the session never writes that file.
#
# WHY THE SESSION MUST NOT WRITE IT. The rule obliging a session to record a miss "in that same
# turn" broke EIGHT recorded times, and not once through forgetfulness: plan mode forbids a
# session to write files, so the party the rule binds is disarmed exactly when it notices
# something. Saying it in a reply is something plan mode permits. The hook does the writing.
#
# WHAT WAS MEASURED, 2026-08-24, rather than read out of documentation. The payload carries
# `session_id`, `transcript_path`, `cwd`, `prompt_id`, `turn_id`, `message_id`, `index`, `final`,
# `delta` and `hook_event_name`. A 1,251-character message fired this event ONCE, with `index` 0,
# `final` true, and `delta` holding the whole message rather than a batch of new lines - which is
# not what the event's own description promises. So this file accumulates by `message_id` and
# parses at `final`: correct whether the message arrives in one piece or in twenty.
#
# PURE ASCII, and it must stay that way: a .ps1 with no BOM is read in the ANSI codepage, and a
# hook whose subject is Cyrillic feedback is the worst place to learn that. It also must never
# contain the literal string that `scripts/hook-selftest.ps1` greps for to decide whether a hook
# refuses anything - this one speaks and never refuses, and that is fixed by the event rather
# than chosen: a refusal is possible on PreToolUse alone.
#
# IT PRINTS NOTHING AND EXITS 0 ON EVERY PATH. A hook that can break the turn it observes is
# worse than no hook, and this one observes the turn's own words.

try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch { }
# Without this the payload's Cyrillic arrives as UTF-8 bytes read in the console codepage. This
# is not hypothetical: the probe that measured the event above did exactly that on its first run.
try { [Console]::InputEncoding = [System.Text.Encoding]::UTF8 } catch { }

$FENCE = [string][char]96 + [char]96 + [char]96
$MARK = 'VAULT-FEEDBACK'

# The kinds a SESSION writes. `lint:` and `process:` are the librarian's words in `log.md` and
# are not filed from here. An unrecognised kind is written anyway, with a note: a wrong record
# is acceptable and an invisible one is not.
$KINDS = @('miss', 'measure', 'decision', 'harness')

# THE SHAPE A `decision:` RECORD NAMES WHEN IT CLAIMS HIS OWN WORDS. One of the three shapes, and
# the only one that is a quotation: `advisory-is-the-default-for-a-hook` carried a block signed
# `owner:` that he had never said, and it decided three things over three days.
$SAID = 'the owner said it'
# BUILT FROM A CHARACTER CODE, like the fence above and for its reason. A guillemet written
# literally here is one more layer of encoding between the author and the byte, and this repository
# has seven recorded instances of a tool eating exactly that.
$QUOTE_OPEN = [char]0x00AB

# WHAT OPENS A RECORD, and the anchor is the whole rule. A record starts at COLUMN ZERO, optionally
# behind a markdown list dash, and nowhere else.
#
# The dash is there because the rendered rule shows one. `CLAUDE.md` renders this block as a
# markdown list - `- miss: ...` - while the template inside `vault-feedback.md` shows the same line
# bare, and until 2026-08-24 this parser read only the bare form. Its regex was `^\s*([A-Za-z-]+)\s*:`
# and a dash is not whitespace, so `^\s*` never passed it while `[A-Za-z-]+` swallowed it as the
# kind and then found no colon: no match, no kind, and the whole block filed as `unknown:`. NINE
# blocks of one session went in that way, about forty lines under a word that is not a kind.
#
# The leading `\s*` is GONE rather than widened, and that is the load-bearing half. Whitespace in
# front of a `word:` is what tells a continuation from a record, and a `miss:` is obliged to say
# WHERE it surfaced - a sentence that lands on the next line and may itself open with a word and a
# colon. Matching those would tear one entry into two. The indent is the test and never the word.
$OPENS = '^(?:-[ \t]+)?([A-Za-z][A-Za-z-]*)[ \t]*:'

function Read-Blocks {
    # Fenced VAULT-FEEDBACK blocks at the TOP LEVEL of a message.
    #
    # Depth is counted, never judged. A VAULT-FEEDBACK fence opens a record only while no other
    # fence is open, which is how this rule can be written about - in a four-backtick example -
    # without the act of describing it filing a line.
    param([string]$text)

    $blocks = @()
    $collecting = $null
    $depth = 0

    foreach ($line in ($text -split "`r?`n")) {
        $trimmed = $line.Trim()
        if ($trimmed.StartsWith($FENCE)) {
            $info = $trimmed.TrimStart([char]96).Trim()
            if ($null -ne $collecting -and $info -eq '') {
                $blocks += , (($collecting -join "`n").Trim())
                $collecting = $null
                $depth = 0
                continue
            }
            if ($depth -eq 0 -and $info -eq $MARK) {
                $collecting = @()
                $depth = 1
                continue
            }
            if ($depth -eq 0) { $depth = 1 } else { $depth = 0 }
            continue
        }
        if ($null -ne $collecting) { $collecting += $line }
    }
    return $blocks
}

function Split-Records {
    # ONE RECORD PER LINE THAT OPENS A KIND, and its continuations with it.
    #
    # It used to be one record per FENCE: the first line's kind was read and applied to everything
    # in the block. The rendered rule shows four kinds in one block, so a session speaking a miss
    # and a decision in one turn had both filed as a miss - and the kind is the one thing this
    # channel exists to carry, so a block that flattens it hands the librarian nothing to sort by.
    #
    # Text before the first opener is kept as a record of its own rather than dropped: it will read
    # as `unknown:` downstream, and a wrong record is acceptable where an invisible one is not.
    param([string]$block)

    $records = @()
    $current = $null
    foreach ($line in ($block -split "`r?`n")) {
        if ($line -match $OPENS -and $null -ne $current) {
            $records += , (($current -join "`n").TrimEnd())
            $current = @($line)
        } elseif ($null -eq $current) {
            $current = @($line)
        } else {
            $current += $line
        }
    }
    if ($null -ne $current) { $records += , (($current -join "`n").TrimEnd()) }
    return $records
}

try {
    if (-not [Console]::IsInputRedirected) { exit 0 }
    $raw = [Console]::In.ReadToEnd()
    if (-not $raw) { exit 0 }
    $payload = $raw | ConvertFrom-Json

    $messageId = $payload.message_id
    $turnId = $payload.turn_id
    $delta = $payload.delta
    if (-not $messageId) { exit 0 }

    $root = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
    $sdd = Join-Path $root '.superpowers\sdd'
    if (-not (Test-Path -LiteralPath $sdd)) { exit 0 }
    $target = Join-Path $sdd 'vault-feedback.md'
    $state = Join-Path $sdd '.message-display'
    if (-not (Test-Path -LiteralPath $state)) {
        New-Item -ItemType Directory -Force -Path $state | Out-Null
    }

    # THE DRAIN WINDOW, and it is two numbers rather than a judgement.
    #
    # `/handoff` empties this file back to its header once it has copied the lines into the
    # journal, and it does that DURING a turn this hook also fires in. Refilling the file behind
    # it is a recorded bug that has already stranded five entries; an automatic catcher would
    # make that window permanent instead of occasional. So: remember the size at this turn's
    # first sighting, and if the file has shrunk since, the drain has run and nothing more is
    # filed this turn. The line is not lost - it left with the journal.
    $sizeNow = 0
    if (Test-Path -LiteralPath $target) { $sizeNow = (Get-Item -LiteralPath $target).Length }
    $sizeFile = Join-Path $state ("turn-" + $turnId + ".size")
    if (Test-Path -LiteralPath $sizeFile) {
        $sizeThen = 0
        [int]::TryParse((Get-Content -Raw -LiteralPath $sizeFile).Trim(), [ref]$sizeThen) | Out-Null
        if ($sizeNow -lt $sizeThen) { exit 0 }
    } else {
        Set-Content -LiteralPath $sizeFile -Value $sizeNow -Encoding ASCII
    }

    # ACCUMULATE, THEN PARSE AT `final`. One measured message arrived whole in a single call, but
    # the event's own description says it fires per batch of completed lines. Both are handled by
    # keeping the parts and only reading them when the message is finished.
    $partFile = Join-Path $state ($messageId + ".part")
    if ($null -ne $delta -and $delta -ne '') {
        Add-Content -LiteralPath $partFile -Value $delta -Encoding UTF8 -NoNewline
    }
    if (-not $payload.final) { exit 0 }

    $filedFile = Join-Path $state ($messageId + ".filed")
    if (Test-Path -LiteralPath $filedFile) { exit 0 }

    $whole = ''
    if (Test-Path -LiteralPath $partFile) {
        $whole = Get-Content -Raw -Encoding UTF8 -LiteralPath $partFile
    }
    if (-not $whole) { exit 0 }

    $blocks = Read-Blocks $whole
    if ($blocks.Count -gt 0) {
        $lines = @()
        foreach ($block in $blocks) {
            foreach ($record in (Split-Records $block)) {
                if ($record.Trim() -eq '') { continue }
                $parts = $record -split "`r?`n"
                # The list dash the rendered rule shows is markup rather than content, and this
                # writer adds its own below. Keeping both would file `- - miss:`.
                $parts[0] = $parts[0] -replace '^-[ \t]+', ''
                $kind = ''
                if ($parts[0] -match '^([A-Za-z][A-Za-z-]*)[ \t]*:') { $kind = $Matches[1].ToLower() }
                if ($kind -eq '') {
                    $parts[0] = 'unknown: ' + $parts[0]
                } elseif ($KINDS -notcontains $kind) {
                    # Kept, not dropped, and marked so a reader can see the channel was used with a
                    # word the file does not declare.
                    $parts += '  (kind not declared by this file - filed as written)'
                }
                # A MARK CLAIMING HIS WORDS AND CARRYING NONE OF THEM, in the same shape as the
                # note above: kept as written, marked so a reader can see it. NEVER A REFUSAL - the
                # verdict is advisory by decision, and a genuine quotation punctuated some other
                # way would otherwise be blocked at the channel rather than filed with a question
                # against it.
                #
                # THE TEST IS THE ABSENT QUOTATION AND NOT THE ALPHABET, which is a measurement
                # rather than a preference. Measured over `log.md` on 2026-08-26: 125 `decision:`
                # records, 81 carrying this shape, 66 with a guillemet quotation and 15 without -
                # and ALL FIFTEEN of those are Cyrillic, so a Cyrillic test fires on none of them.
                # The absent quotation is a STRICT SUPERSET: it catches every record an alphabet
                # test would, including the English paraphrase that test was written for, plus the
                # fifteen it cannot see. Nothing is given up by not building the narrower one.
                #
                # WHAT IT STILL CANNOT SEE, written down rather than left implied: a record that
                # quotes words he did not say. An alphabet separates a quotation from a paraphrase;
                # only he separates a faithful paraphrase from a wrong one, and the ratification
                # step in `/retro` is what does that.
                # THE SHAPE IS DECLARED AT THE HEAD OF THE RECORD, NOT MENTIONED ANYWHERE IN IT,
                # and this cost a false positive on the guard's FIRST live encounter. A record
                # reading `decision: the owner selected it - the catcher's note on a mark carrying
                # `the owner said it` fires on...` was flagged: it discusses the phrase rather
                # than claiming it. Anchoring after the kind is the whole repair, and it is the
                # same shape the kind parser above already uses.
                if ($kind -eq 'decision' -and $parts[0] -match "^decision:\s*$SAID\b" `
                        -and $record.IndexOf($QUOTE_OPEN) -lt 0) {
                    $parts += ('  (marked as his words and carrying no quotation - a quotation ' +
                        'keeps his own words in guillemets; if these are yours rather than his, ' +
                        'the shape is `the session understood it`)')
                }
                # Continuation lines are indented so the entry stays one list item.
                $entry = '- ' + $parts[0]
                for ($i = 1; $i -lt $parts.Length; $i++) { $entry += "`n  " + $parts[$i] }
                $lines += $entry
            }
        }
        Add-Content -LiteralPath $target -Value ($lines -join "`n") -Encoding UTF8
    }

    # THE REPLY-SILENCE COUNT, AND IT IS A NUMBER RATHER THAN A VOICE (2026-08-29). The guarantee at
    # the head of this file is kept: it writes a count and prints nothing, on this path as on every
    # other.
    #
    # WHY THE COUNT LIVES HERE AND THE SENTENCE LIVES NEXT DOOR. Measured 2026-08-29 by a probe that
    # fired three times and was deleted afterwards: a hook on `MessageDisplay` CANNOT return
    # `additionalContext` to a session. So the only party that can see the session's own replies
    # cannot speak, and the only party that can speak - `remind-the-feedback.ps1`, on the owner's
    # prompt - cannot see them. This writes the number that one reads.
    #
    # WHAT IT CLOSES. That hook counts the OWNER'S prompts, so an hour of the session working alone
    # and filing nothing registers as ONE quiet prompt however many replies it contained. Two pages
    # name that gap as the thing a counter here would cover, and it is why this item exists.
    #
    # ONE WRITER PER FILE. This hook writes this file and reads nothing else; the reminder reads it
    # and writes only its own state. Two hooks reading and writing one file is the shape this store
    # has already ruled against for the ledger.
    try {
        $replyState = Join-Path $sdd '.reply-silence'
        $replies = 0
        if ($blocks.Count -eq 0) {
            if (Test-Path -LiteralPath $replyState) {
                $prior = (Get-Content -LiteralPath $replyState -First 1 -ErrorAction Stop)
                if ($prior) { [void][int]::TryParse(($prior -split "`t")[0].Trim(), [ref] $replies) }
            }
            $replies = $replies + 1
        }
        [System.IO.File]::WriteAllText($replyState, ([string]$replies + "`n"),
            (New-Object System.Text.UTF8Encoding($false)))
    } catch { }

    Set-Content -LiteralPath $filedFile -Value $blocks.Count -Encoding ASCII
    Remove-Item -LiteralPath $partFile -Force -ErrorAction SilentlyContinue

    # Sweep state older than a day. Without this the directory grows one file per message for
    # ever, and a state directory nobody empties is a slow version of the same bug.
    $cutoff = (Get-Date).AddDays(-1)
    Get-ChildItem -LiteralPath $state -File -ErrorAction SilentlyContinue |
        Where-Object { $_.LastWriteTime -lt $cutoff } |
        Remove-Item -Force -ErrorAction SilentlyContinue
} catch { }

exit 0
