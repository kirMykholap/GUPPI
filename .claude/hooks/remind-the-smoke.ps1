# PostToolUse reminder. Fires when /retro is invoked and asks the session to run `make smoke` now,
# so the run and the retro conversation overlap instead of queueing behind each other.
#
# IT REMINDS AND NEVER LAUNCHES, WHICH IS THE OWNER'S DESIGN AND NOT A LIMITATION WORKED AROUND. A
# hook cannot hand a result back later: it would have to spawn the run detached and write a status
# file, and the session would then have to tell "still running" from "died quietly" - a distinction
# this project has already failed to make, once at 56 minutes. The agent running the command itself
# has the result in front of it, and `record-the-smoke.ps1` turns that into the row.
#
# IT NEVER REFUSES, so it owes no page arguing the three conditions of a refusing hook. What it says
# is advice; what enforces it is `gate-the-handoff.ps1`, which does owe that page and has one.
#
# THE MATCHER `Skill` IS ESTABLISHED AND ITS REGISTRATION HERE IS NOT, and those are two different
# claims. Measured 2026-08-21 by a probe on `PreToolUse` with matcher `Skill|Write` and `Write` as a
# control known to fire: the payload came back `tool=Skill`, `event=PreToolUse`,
# `input_keys=args,skill`. So the tool name is real and the field below is named from that reading
# rather than guessed. What has never been done is registering such a matcher in THIS repository's
# settings, and a hook that never fires is indistinguishable from one with nothing to say - this
# project has shipped that once already. A selftest case cannot close it either, because hooks are
# read at session start; the acceptance is a restart and a live /retro.
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

# ConvertFrom-Json rather than a regex over the payload, for the reason the hooks beside this one
# give: a payload is a document, and a greedy pattern over it matches whatever a caller's own text
# happens to contain.
$raw = [Console]::In.ReadToEnd()
if ([string]::IsNullOrWhiteSpace($raw)) { exit 0 }
try { $payload = $raw | ConvertFrom-Json } catch { exit 0 }

$tool = $payload.tool_name
if ($tool -isnot [string]) { exit 0 }
if ($tool -ne 'Skill') { exit 0 }

# THE FIELD IS `skill`, READ OFF A MEASUREMENT AND NOT OFF THE TOOL'S DOCUMENTATION. The 2026-08-21
# probe reported `input_keys=args,skill` from a live payload, so there is one spelling here rather
# than the two the librarian lock carries - that hook accepts `subagent_type` and `agent_type`
# because both are known to occur, and inventing a second name nobody has seen would be insurance
# against nothing that the selftest could never exercise.
$name = $null
if ($payload.tool_input) { $name = $payload.tool_input.skill }
if ($name -isnot [string]) { exit 0 }

# A plugin-scoped invocation arrives as `<plugin>:retro`, so the tail is what identifies it. The
# narrowing lives here rather than in the matcher because a matcher can only name the tool.
$name = $name.Trim()
if ($name -ne 'retro' -and -not $name.EndsWith(':retro')) { exit 0 }

# THE `VAULT-FEEDBACK` DEMAND LEFT THIS FILE ON 2026-08-29. It was written out here in full and
# again in `remind-the-feedback.ps1`, and one requirement in two texts is one repair landing on one
# of them. That hook owns it now and speaks it on this same event through a ritual branch of its
# own; this file keeps the smoke run, which is its actual subject. Both reminders still reach a
# `/retro`, because both are registered on `PostToolUse` with the `Skill` matcher.
Write-Note ('Run `make smoke` early, so it overlaps this conversation instead of queueing behind it. RUN ' +
    'IT IN THE FOREGROUND: a background launch is recorded by nothing, because the recorder reads ' +
    'the verdict the run prints and a backgrounded call reports only that it started.' + "`n`n" +
    'Two things about it that are easy to get wrong. Its red is not advice: `/handoff` refuses ' +
    'while the last run is red or missing, and the fix belongs in this retro, because after ' +
    '/handoff the journal is the librarian''s and nothing can be corrected. And a green run goes ' +
    'stale the moment anything git tracks is written after it - including a librarian''s writes - ' +
    'so `make smoke` has to run AGAIN as the very last thing before /handoff.' + "`n`n" +
    'Add `ONLY=<pattern>` if this session edited `scripts/vault-check.sh`: without it no case of ' +
    'the gate''s own selftest runs, and a rule removed from the gate leaves the corpus green.')

exit 0
