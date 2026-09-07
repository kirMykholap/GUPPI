# Serve the rule that governs the file being touched.
#
# WHAT THIS REPLACES. Until 2026-08-30 a prohibition lived as a page in `wiki/decisions/` and
# reached a reader only if that reader ran `/pre-task` and read the whole folder. 282 of the 320
# pages there were prohibitions, they were the largest fixed cost any dispatch paid, and most of a
# session never saw them at all. This hook is the other delivery: the rule arrives at the moment
# the file it governs is touched, and nothing has to be remembered or enumerated to get it.
#
# TWO MATCHERS, AND THEY ARE DIFFERENT IN KIND. That is the whole design and it is not an
# implementation detail:
#
#   - BY PATH, for files that carry no frontmatter and cannot carry a slug. The repository's own
#     `CLAUDE.md` has no frontmatter at all and eleven rules render into it, so one field with one
#     value could never address it. This half reads `governs:` off `wiki/rules/` and asks which
#     rules name the file being written. It is the `governs:` table made active.
#   - BY `authority:`, for pages under `wiki/`, where the slug IS the address. Read a page about X
#     and the rule about X arrives. WRITTEN 2026-08-31; before that day the slug was parsed into a
#     variable that nothing read, so this half was described here and did not exist.
#
# THE `authority:` HALF MATCHES EXACTLY AND RESOLVES NOTHING. A family rule carries the slug of one
# of the decisions it discharged, and the other members of that family are reached by making their
# slugs converge along `decision -> proposal/rule -> concept/entity`, never by teaching this hook to
# look a slug up in `authority.md`. That was proposed and refused by the owner on 2026-08-30: the
# family register is an instrument of the cleanup, and a runtime that reads it would outlive the
# cleanup as a dependency nobody asked for. The consequence is stated rather than hidden - on the
# day the family rules are written, zero slugs are shared across types, so this half serves nothing
# and its coverage grows only as the convergence is done by hand.
#
# WHY A FILE OF ITS OWN RATHER THAN A BRANCH IN `ask-the-vault.ps1`. Three reasons and the first is
# the binding one. That script is a chain that PICKS EXACTLY ONE NOTE, by its own comment and by
# design; this one has to be able to speak on the same edit that trips one of those. Second, it
# needs a matcher that script does not have - `Read` - so it is a separate `settings.json` entry
# whatever happens. Third, failure isolation: if the lookup breaks, the pre-task net keeps working.
# Measured before deciding: a bare PowerShell spawn is 99 ms on this machine and this script with
# its vault discovery and its grep is 141 ms, against a write path that fires 71 to 108 times in a
# working session.
#
# THE READ MATCHER, and the measurement that had to come before it. Nobody had ever measured how
# often `Read` fires in a session here, and it is the most frequent tool call there is; the owner
# deferred the registration to a measurement rather than accepting an unbounded multiplier on a
# 141 ms cost. The measurement is taken and recorded on the entity page; the registration in
# `settings.json` is what makes the `authority:` half reachable at all, because that half fires on
# a Read of a vault page and this hook saw no Reads before.
#
# IT NEVER REFUSES. The ruling in this repository is that a hook refuses only when the action is
# IRREVERSIBLE and the refusal CANNOT BE WRONG, both at once. Neither holds here: an edit is
# reversible, and a rule that merely governs a file is not a reason to stop the edit.

try { [Console]::InputEncoding = [System.Text.Encoding]::UTF8 } catch { }
try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch { }

function Write-Note([string] $text) {
    @{ hookSpecificOutput = @{ hookEventName = 'PreToolUse'; additionalContext = $text } } |
        ConvertTo-Json -Depth 4
}

$path = $null
$sessionId = $null
$toolName = ''
try {
    $raw = [Console]::In.ReadToEnd()
    if (-not $raw) { exit 0 }
    $payload = $raw | ConvertFrom-Json
    $path = $payload.tool_input.file_path
    try { $sessionId = $payload.session_id } catch { }
    try { if ($payload.tool_name) { $toolName = [string]$payload.tool_name } } catch { }
} catch {
    exit 0          # malformed or unexpected payload: say nothing, block nothing
}

if (-not $path) { exit 0 }
if ($path -isnot [string]) { exit 0 }

# .Replace and not -replace: the right-hand side of -replace is a regular expression and a lone
# backslash is not a valid one. Written that way a hook in this repository errored on every
# payload, printed nothing at all, and still exited 0.
$p = $path.Replace('\', '/')

$root = $null
$vault = $null
try {
    $root = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
    . (Join-Path $PSScriptRoot 'vault-path.ps1')
    $vault = Find-Vault $root
} catch { }
if ($null -eq $vault) { exit 0 }      # no vault found: this hook has nothing to say

$vaultPath = $vault.FullName.Replace('\', '/').TrimEnd('/')
$rulesDir  = Join-Path $vault.FullName 'wiki/rules'
if (-not (Test-Path -LiteralPath $rulesDir)) { exit 0 }

# THE SILENCE IS SCOPED BY PATH AND, SINCE 2026-08-31, BY MODE. The original scoping stands and its
# reason is unchanged: a WRITE inside `wiki/` is the librarian doing its job, and serving it a rule
# about the page it is writing is noise on every page of an ingest. There is no documented way to
# exclude one subagent from a hook declared in `settings.json`, and hooks DO reach subagents here -
# proved in this repository on 2026-08-20 - so scoping by the agent is not available and scoping by
# the path is.
#
# WHAT THE MODE HALF ADDS is the opposite case, and it is the owner's own ground for the whole
# lookup delivery: a READ inside `wiki/` is somebody going to look something up, and the search is
# where a rule can catch you. Silencing reads as well would leave the `authority:` half with no
# occasion to fire at all - the write side is silent exactly where a slug exists.
#
# `archive/` STAYS SILENT IN BOTH DIRECTIONS. It is a warehouse: nothing in it is live, nothing
# sweeps it, and a rule served off a frozen page would be the text that WAS true. The six registers
# stay silent in both directions for the same reason they always were - they carry no slug.
$isRead = ($toolName -eq 'Read')
foreach ($register in 'index.md', 'tags.md', 'log.md', 'brief.md', 'sprint.md', 'authority.md') {
    if ($p -eq "$vaultPath/$register") { exit 0 }
}
if ($p -like "$vaultPath/archive/*") { exit 0 }
$inWiki = $p -like "$vaultPath/wiki/*"
if ($inWiki -and -not $isRead) { exit 0 }

# A READ OUTSIDE THE VAULT ENDS THE RUN, so the two halves fire on one mode each: `governs:` on a
# write, `authority:` on a read. The `governs:` note is about a WRITE - it says the text is rendered
# here and that editing the region alone reads as drift - and there is nothing for a reader of that
# file to do with it. Firing it on reads as well would have bought noise and paid the folder scan
# for it. Measured across every transcript this project has: Bash 5088, Edit 1102, Read 490, Write
# 392 - so `Read` is a third of the write path here rather than the multiplier the deferral feared,
# and this narrowing keeps the added cost to reads of vault pages alone.
if ($isRead -and -not $inWiki) { exit 0 }

# THE SLUG OF THE FILE BEING TOUCHED, which is the address the `authority:` half matches on. Only a
# page under `wiki/` can carry one, so nothing outside the vault is opened - a file with no
# frontmatter has no slug and is reached by `governs:` or by nothing. The head is read to the same
# depth as a rule page's own, and for the same reason.
#
# A PAGE UNDER `wiki/` WITH NO SLUG ENDS THE RUN. `authority:` is required in every folder but
# `wiki/rules/`, so its absence means a schema fault or a rules page - and neither is something to
# scan seventy files for.
$touchedSlug = ''
if ($inWiki) {
    try {
        $head = Get-Content -LiteralPath $path -TotalCount 30 -ErrorAction Stop
        if ($head.Count -ge 3 -and $head[0].Trim() -eq '---') {
            for ($i = 1; $i -lt $head.Count; $i++) {
                if ($head[$i].Trim() -eq '---') { break }
                if ($head[$i] -match '^authority:\s*(.+?)\s*$') {
                    $touchedSlug = $Matches[1].Trim('"').Trim("'")
                    break
                }
            }
        }
    } catch { }
    if (-not $touchedSlug) { exit 0 }
}

# The path as `governs:` writes it: from the repository root, forward slashes, no leading `./`.
$rootPrefix = $root.Replace('\', '/').TrimEnd('/') + '/'
$rel = $p
if ($p.StartsWith($rootPrefix, [System.StringComparison]::OrdinalIgnoreCase)) {
    $rel = $p.Substring($rootPrefix.Length)
}

# ONE PASS OVER `wiki/rules/` AND NOT A GENERATED TABLE. Seventeen files today and perhaps seventy
# after the families land. A generated table would be a second artefact that can disagree with the
# tree, which is the drift this store repairs rather than creates. The owner reads the same list as
# a `pages.base` view; the hook reads the folder.
#
# ONLY THE HEAD OF EACH FILE IS READ, and that is not a micro-optimisation. A rule page runs to
# seventeen kilobytes and everything this hook needs is in the frontmatter; reading them whole was
# measured at roughly two hundred milliseconds of the run, on a path that fires seventy to a
# hundred times a session. Thirty lines is more than any frontmatter here has ever held and the
# closing `---` is what actually stops the parse.
$hits = @()
foreach ($file in Get-ChildItem -LiteralPath $rulesDir -Filter '*.md' -File -ErrorAction SilentlyContinue) {
    $lines = @()
    try { $lines = Get-Content -LiteralPath $file.FullName -TotalCount 30 -ErrorAction Stop } catch { continue }
    if ($lines.Count -lt 3 -or $lines[0].Trim() -ne '---') { continue }

    $close = -1
    for ($i = 1; $i -lt $lines.Count; $i++) { if ($lines[$i].Trim() -eq '---') { $close = $i; break } }
    if ($close -lt 0) { continue }

    $status = ''
    $governs = @()
    $slug = ''
    $render = ''
    for ($i = 1; $i -lt $close; $i++) {
        if ($lines[$i] -match '^status:\s*(.+?)\s*$')    { $status = $Matches[1].Trim('"').Trim("'") }
        if ($lines[$i] -match '^authority:\s*(.+?)\s*$') { $slug   = $Matches[1].Trim('"').Trim("'") }
        # `render:` NAMES WHICH DELIVERY THIS RULE TAKES and this hook read it not at all until
        # 2026-08-31. Without it a lookup rule and a region rule are indistinguishable here, and
        # the note said the wrong thing about one of them.
        if ($lines[$i] -match '^render:\s*(.+?)\s*$')    { $render = $Matches[1].Trim('"').Trim("'") }
        if ($lines[$i] -match '^governs:\s*(.+?)\s*$') {
            $value = $Matches[1].Trim()
            # `governs: path` and `governs: [one, two]` mean the same thing and both are legal. The
            # YAML block form is refused by the gate rather than read, so it is not parsed here
            # either - a half-parsed spelling is what this repository forbids the injector to do.
            if ($value.StartsWith('[')) {
                foreach ($piece in ($value.Trim('[', ']') -split ',')) {
                    $piece = $piece.Trim().Trim('"').Trim("'").Trim()
                    if ($piece) { $governs += $piece }
                }
            } elseif ($value) {
                $governs += $value.Trim('"').Trim("'")
            }
        }
    }

    # A deprecated or repealed rule does not render and must not be served either: it is the text
    # that WAS true, and handing it over as current is worse than handing over nothing.
    if ($status -ne 'current') { continue }

    # BY `authority:`, AND THE MATCH IS EXACT. Such a page carries a slug and no destination, so it
    # can never be reached by the path test below - which is why the two branches are exclusive
    # rather than sequential. Nothing is resolved through `authority.md`; see the header.
    if ($render -eq 'authority') {
        if ($touchedSlug -and $slug -eq $touchedSlug) {
            $title = ''
            for ($i = 1; $i -lt $close; $i++) {
                if ($lines[$i] -match '^title:\s*(.+?)\s*$') { $title = $Matches[1].Trim('"').Trim("'"); break }
            }
            $hits += [pscustomobject]@{
                Slug  = [System.IO.Path]::GetFileNameWithoutExtension($file.Name)
                Title = $title
                Kind  = 'authority'
            }
        }
        continue
    }

    foreach ($dest in $governs) {
        if ($dest.Replace('\', '/') -eq $rel) {
            $title = ''
            for ($i = 1; $i -lt $close; $i++) {
                if ($lines[$i] -match '^title:\s*(.+?)\s*$') { $title = $Matches[1].Trim('"').Trim("'"); break }
            }
            $hits += [pscustomobject]@{
                Slug  = [System.IO.Path]::GetFileNameWithoutExtension($file.Name)
                Title = $title
                Kind  = 'governs'
            }
            break
        }
    }
}

if ($hits.Count -eq 0) { exit 0 }

# SAID ONCE PER FILE PER SESSION, AND THE LEDGER IS ONLY OPENED WHEN THERE IS SOMETHING TO SAY. A
# reminder that fires every time becomes furniture, and this one would otherwise fire on every edit
# of `CLAUDE.md` in a session that edits it eleven times.
#
# THE ORDER IS MEASURED RATHER THAN CHOSEN. Asking the ledger first looks cheaper - a repeat would
# skip the folder scan - and it is not: dot-sourcing `pre-task-state.ps1` and deriving the state
# costs more than reading the head of seventeen files, and it would be paid on EVERY write,
# including the great majority that govern nothing. Scanning first means an ungoverned path never
# touches the ledger at all.
#
# If the ledger cannot be read the note is said again, which is the safe direction: a repeated note
# costs a paragraph, a silenced one costs the rule.
$alreadySaid = $false
try {
    if ($root -and $sessionId) {
        . (Join-Path $PSScriptRoot 'pre-task-state.ps1')
        $state = Read-LedgerState $root $sessionId
        if ($state -and $state.ServedRuleFiles -and ($state.ServedRuleFiles -contains $rel)) {
            $alreadySaid = $true
        }
    }
} catch { }
if ($alreadySaid) { exit 0 }

# THE WORDING BRANCHES ON THE DELIVERY, and it did not until 2026-08-31. The sentence below about
# editing the region is TRUE of a rendered rule and FALSE of a looked-up one: a `render: authority`
# page is written into no file, so there is no region to edit and no drift for the gate to read.
# One wording for both would have been a hook telling a reader something untrue about the rule it
# had just handed over.
$vaultName = Split-Path $vaultPath -Leaf
$lines = @()
$governsHits   = @($hits | Where-Object { $_.Kind -eq 'governs' })
$authorityHits = @($hits | Where-Object { $_.Kind -eq 'authority' })

if ($governsHits.Count -gt 0) {
    $lines += 'This file carries a project rule. It is rendered here from the vault, and the page is where it is changed - editing the region alone leaves the gate reading the difference as drift.'
    foreach ($hit in $governsHits) {
        $lines += ("  - {0}`n    {1}/wiki/rules/{2}.md" -f $hit.Title, $vaultName, $hit.Slug)
    }
}
if ($authorityHits.Count -gt 0) {
    $lines += 'This page answers a question the vault has a rule about, and the rule found you by its slug rather than by a path. It is written into no file: read the page and change it there.'
    foreach ($hit in $authorityHits) {
        $lines += ("  - {0}`n    {1}/wiki/rules/{2}.md" -f $hit.Title, $vaultName, $hit.Slug)
    }
}
Write-Note ($lines -join "`n")

try {
    if ($root -and $sessionId) {
        Add-LedgerLine -root $root -sessionId $sessionId -event 'served-rule' -path $rel
    }
} catch { }

exit 0
