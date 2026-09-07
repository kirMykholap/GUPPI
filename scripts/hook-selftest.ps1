# Verification by removal for the two hooks.
#
# The hooks are the only part of this system that nothing else can check: they are spawned by
# the harness, not by an agent's shell, and they run before anyone is watching. A hook that
# fails prints its error where a session reads its brief; a hook that exits non-zero shows up as
# a hook failure; a guard that says nothing is indistinguishable from a guard that is not there.
# So every branch of both is exercised here against a throwaway project tree.
#
# THIS FILE IS PURE ASCII ON PURPOSE. Windows PowerShell 5.1 reads a .ps1 as the system ANSI
# codepage unless the file carries a BOM, so a literal em dash or a Cyrillic word here arrives
# as mojibake and can break parsing outright - which is exactly how the first run of this test
# failed, on its own fixture, before it reached a hook at all. Non-ASCII test data is built from
# char codes below.
#
# Run: powershell -NoProfile -ExecutionPolicy Bypass -File scripts/hook-selftest.ps1
$ErrorActionPreference = 'Continue'
try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch { }

$repo = Split-Path -Parent $PSScriptRoot
$pass = 0
$fail = 0

function Check([string] $name, [bool] $ok, [string] $detail) {
    if ($ok) { "CAUGHT   {0,-40}" -f $name; $script:pass++ }
    else     { "MISSED   {0,-40}" -f $name; ($detail -split "`n" | ForEach-Object { "           $_" }); $script:fail++ }
}

function Utf8([int[]] $codes) { -join ($codes | ForEach-Object { [char]$_ }) }
$emdash = Utf8 @(0x2014)
$cyril  = Utf8 @(0x00AB, 0x0432, 0x0430, 0x043A, 0x0430, 0x043D, 0x0441, 0x0438, 0x0438, 0x00BB)

function WriteUtf8([string] $path, [string] $text) {
    [System.IO.File]::WriteAllText($path, $text, (New-Object System.Text.UTF8Encoding($false)))
}

# A throwaway project: the two hooks, a vault whose name is nothing like ours, and a git repo,
# because the staleness check asks git what HEAD is.
$sandbox = Join-Path ([System.IO.Path]::GetTempPath()) ("hooktest-" + [System.Guid]::NewGuid().ToString('N').Substring(0, 8))
New-Item -ItemType Directory -Force -Path (Join-Path $sandbox '.claude/hooks') | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $sandbox 'a vault with spaces/wiki/decisions') | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $sandbox 'a vault with spaces/raw/handoffs') | Out-Null
Copy-Item (Join-Path $repo '.claude/hooks/session-brief.ps1') (Join-Path $sandbox '.claude/hooks')
Copy-Item (Join-Path $repo '.claude/hooks/ask-the-vault.ps1') (Join-Path $sandbox '.claude/hooks')
Copy-Item (Join-Path $repo '.claude/hooks/vault-path.ps1')    (Join-Path $sandbox '.claude/hooks')
Copy-Item (Join-Path $repo '.claude/hooks/check-the-journal.ps1') (Join-Path $sandbox '.claude/hooks')
Copy-Item (Join-Path $repo '.claude/hooks/lock-the-librarian.ps1') (Join-Path $sandbox '.claude/hooks')
# A FIXTURE MUST MATERIALISE WHAT THE SUBJECT READS. `ask-the-vault.ps1` dot-sources
# `pre-task-state.ps1`, and a dot-source that fails is swallowed by the try around it - so a sandbox
# missing this file does not fail, it goes QUIET: `$state` stays null and every branch that depends
# on it is skipped. The suite would report the same green it reports when the code works. Caught by
# noticing that adding the branches moved no count at all.
Copy-Item (Join-Path $repo '.claude/hooks/pre-task-state.ps1') (Join-Path $sandbox '.claude/hooks')
Copy-Item (Join-Path $repo '.claude/hooks/check-the-plan.ps1')  (Join-Path $sandbox '.claude/hooks')
Copy-Item (Join-Path $repo '.claude/hooks/remind-the-smoke.ps1')  (Join-Path $sandbox '.claude/hooks')
Copy-Item (Join-Path $repo '.claude/hooks/remind-the-feedback.ps1') (Join-Path $sandbox '.claude/hooks')
Copy-Item (Join-Path $repo '.claude/hooks/record-the-smoke.ps1')  (Join-Path $sandbox '.claude/hooks')
Copy-Item (Join-Path $repo '.claude/hooks/gate-the-handoff.ps1')  (Join-Path $sandbox '.claude/hooks')
Copy-Item (Join-Path $repo '.claude/hooks/serve-the-rule.ps1')    (Join-Path $sandbox '.claude/hooks')

# The gate hook shells out to scripts/vault-check.sh and the check reads the handoff template,
# so the sandbox needs both. The sandbox vault is a stub and will FAIL that check - which is what
# the reported-a-failure case wants. It proves the hook ran the gate and relayed a non-zero exit;
# whether the gate is right about any particular rule is vault-check-selftest.sh's job, and saying
# so here is cheaper than a reader assuming this file covers it.
New-Item -ItemType Directory -Force -Path (Join-Path $sandbox 'scripts') | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $sandbox '.claude/templates') | Out-Null
Copy-Item (Join-Path $repo 'scripts/vault-check.sh')       (Join-Path $sandbox 'scripts')
Copy-Item (Join-Path $repo 'scripts/vault-catalogue.sh')   (Join-Path $sandbox 'scripts')
Copy-Item (Join-Path $repo '.claude/templates/handoff.md') (Join-Path $sandbox '.claude/templates')

$briefHook = Join-Path $sandbox '.claude/hooks/session-brief.ps1'
$guardHook = Join-Path $sandbox '.claude/hooks/ask-the-vault.ps1'
$vault     = Join-Path $sandbox 'a vault with spaces'
$brief     = Join-Path $vault 'brief.md'
$fwd       = $sandbox.Replace('\', '/')

function RunBrief {
    $out = & powershell -NoProfile -ExecutionPolicy Bypass -File $briefHook 2>&1 | Out-String
    return @{ out = $out; code = $LASTEXITCODE }
}
function RunGuard([string] $json) {
    $out = $json | & powershell -NoProfile -ExecutionPolicy Bypass -File $guardHook 2>&1 | Out-String
    return @{ out = $out; code = $LASTEXITCODE }
}

# ---------------------------------------------------------------- the brief hook
$r = RunBrief
Check "no brief yet" ($r.code -eq 0 -and $r.out -match 'No vault brief exists yet') $r.out

WriteUtf8 $brief ("# Brief " + $emdash + " test`r`n`r`n" + $cyril + "`r`n")
$r = RunBrief
Check "the brief is printed" ($r.code -eq 0 -and $r.out.Contains($cyril)) $r.out
Check "and it is not mangled" ($r.out.Contains($emdash) -and $r.out -notmatch '\?\?\?') $r.out

Push-Location $sandbox
& git init -q 2>&1 | Out-Null
& git config user.email "selftest@example.com" 2>&1 | Out-Null
& git config user.name "selftest" 2>&1 | Out-Null
& git add -A 2>&1 | Out-Null
& git commit -q -m "first" 2>&1 | Out-Null
$head = (& git rev-parse --short HEAD).Trim()
Pop-Location

# Staleness is a question about git history: a committed brief with commits after it is stale,
# an uncommitted one never is. The stamp is provenance for a human and is not compared.
WriteUtf8 $brief "# Brief`r`ngenerated-at: $head`r`n`r`nfresh`r`n"
$r = RunBrief
Check "an uncommitted brief is fresh" ($r.code -eq 0 -and $r.out -notmatch 'out of date' -and $r.out -match 'fresh') $r.out

Push-Location $sandbox
& git add -A 2>&1 | Out-Null
& git commit -q -m "the brief" 2>&1 | Out-Null
Pop-Location
$r = RunBrief
Check "the brief's own commit is not stale" ($r.code -eq 0 -and $r.out -notmatch 'out of date' -and $r.out -match 'fresh') $r.out

WriteUtf8 (Join-Path $sandbox 'another.txt') "x"
Push-Location $sandbox
& git add -A 2>&1 | Out-Null
& git commit -q -m "second" 2>&1 | Out-Null
Pop-Location
$r = RunBrief
Check "a commit after it is announced" ($r.code -eq 0 -and $r.out -match 'out of date' -and $r.out -match '1 commits' -and $r.out -match 'fresh') $r.out

WriteUtf8 (Join-Path $sandbox 'a vault with spaces/raw/handoffs/2026-08-13-x.md') "session: 2026-08-13"
WriteUtf8 $brief "# Brief`r`ngenerated-at: $head`r`ningested: 2026-08-13-x.md`r`n`r`nfresh`r`n"
$r = RunBrief
Check "the journal the brief names" ($r.code -eq 0 -and $r.out -notmatch 'never built from' -and $r.out -match 'fresh') $r.out

# THE TWO-PLACE RESOLUTION, 2026-08-21. `/ingest` archives the journal it compiled as its last
# step, so the file this line names leaves `raw/handoffs/` on every successful ingest. Without the
# archive branch the alarm below fires on EVERY session start - the false-alarm class this hook has
# already had removed from it twice. The second case is what keeps that branch from swallowing a
# journal that is genuinely gone: a resolver with two places to look can go silent for the wrong
# reason, and only an absence case can tell the two silences apart.
$archDir = Join-Path $sandbox 'a vault with spaces/archive/2026-08-13/2026-08-13-x/handoffs'
New-Item -ItemType Directory -Force -Path $archDir | Out-Null
Move-Item (Join-Path $sandbox 'a vault with spaces/raw/handoffs/2026-08-13-x.md') `
          (Join-Path $archDir '2026-08-13-x.md')
$r = RunBrief
Check "the journal the brief names, after it was archived" ($r.code -eq 0 -and $r.out -notmatch 'does not exist' -and $r.out -match 'fresh') $r.out

Remove-Item (Join-Path $archDir '2026-08-13-x.md')
$r = RunBrief
Check "a journal in neither place is still named" ($r.code -eq 0 -and $r.out -match 'does not exist' -and $r.out -match '2026-08-13-x.md') $r.out

# Restored, so the cases below meet the sandbox they were written against.
WriteUtf8 (Join-Path $sandbox 'a vault with spaces/raw/handoffs/2026-08-13-x.md') "session: 2026-08-13"

WriteUtf8 (Join-Path $sandbox 'a vault with spaces/raw/handoffs/2026-08-14-y.md') "session: 2026-08-14"
$r = RunBrief
Check "a journal it was never built from" ($r.code -eq 0 -and $r.out -match '2026-08-14-y.md' -and $r.out -match 'fresh') $r.out

WriteUtf8 $brief "# Brief`r`ngenerated-at: $head`r`n`r`nfresh`r`n"
$r = RunBrief
Check "no ingested: line is silent" ($r.code -eq 0 -and $r.out -notmatch 'never built from' -and $r.out -match 'fresh') $r.out

Remove-Item (Join-Path $sandbox 'a vault with spaces/raw/handoffs/2026-08-14-y.md')
# The staleness check calls git. A hook is spawned by the harness, not by an agent's shell, so
# it can get a PATH without it - and the first version of that check lost the brief entirely.
$r = @{ out = (& powershell -NoProfile -ExecutionPolicy Bypass -Command `
        "`$env:PATH = [System.Environment]::GetFolderPath('System'); & '$briefHook'" 2>&1 | Out-String)
        code = $LASTEXITCODE }
Check "git missing: the brief survives" ($r.code -eq 0 -and $r.out -match 'fresh' -and $r.out -notmatch 'not recognized') $r.out

Rename-Item -Path $vault -NewName 'renamed vault'
$r = RunBrief
Check "the vault is renamed" ($r.code -eq 0 -and $r.out -match 'fresh') $r.out
Rename-Item -Path (Join-Path $sandbox 'renamed vault') -NewName 'a vault with spaces'

New-Item -ItemType Directory -Force -Path (Join-Path $sandbox '.hidden_vault/wiki') | Out-Null
WriteUtf8 (Join-Path $sandbox '.hidden_vault/brief.md') "HIDDEN"
$r = RunBrief
Check "a dot-directory is not a vault" ($r.code -eq 0 -and $r.out -notmatch 'HIDDEN' -and $r.out -match 'fresh') $r.out
Remove-Item -Recurse -Force (Join-Path $sandbox '.hidden_vault')

Rename-Item -Path $vault -NewName 'not-a-vault-any-more'
Remove-Item -Recurse -Force (Join-Path $sandbox 'not-a-vault-any-more/wiki')
$r = RunBrief
Check "no vault at all" ($r.code -eq 0 -and $r.out -match 'No vault found' -and $r.out -notmatch 'fresh') $r.out
New-Item -ItemType Directory -Force -Path (Join-Path $sandbox 'not-a-vault-any-more/wiki/decisions') | Out-Null
Rename-Item -Path (Join-Path $sandbox 'not-a-vault-any-more') -NewName 'a vault with spaces'

# ---------------------------------------------------------------- the guard

$cases = @(
  @{ n = 'a wiki page';             p = "$fwd/a vault with spaces/wiki/decisions/x.md"; want = 'one writer' },
  @{ n = 'an archived page';        p = "$fwd/a vault with spaces/archive/old.md";      want = 'one writer' },
  @{ n = 'a register';              p = "$fwd/a vault with spaces/brief.md";            want = 'registers' },
  # `authority.md` joined the registers on 2026-08-21 and is pinned here for the reason every
  # other member is: the list lives in this hook and would otherwise be a set nothing measures.
  # A register the one-writer note does not cover is a register a session edits by hand.
  @{ n = 'the authority register';  p = "$fwd/a vault with spaces/authority.md";        want = 'registers' },
  @{ n = 'the project CLAUDE.md';   p = "$fwd/CLAUDE.md";                               want = 'carries a project rule' },
  # THE PER-FOLDER SCHEMAS SIT INSIDE `wiki/` AND ARE NOT THE LIBRARIAN'S. They are the session's
  # to write by the decision of 2026-08-19, so the one-writer note is false there. This case and
  # `a wiki page` above it are the whole discrimination: same folder, same vault, opposite verdict.
  # ASSERTED ON THE OUTPUT AND NEVER ON THE EXIT CODE - the hook exits 0 whether it speaks or not,
  # so a case reading the code would pass before this change and after it.
  @{ n = 'a per-folder schema';     p = "$fwd/a vault with spaces/wiki/decisions/_schema.yaml"; want = '' },
  @{ n = 'an ordinary source file'; p = "$fwd/src/app.py";                              want = '' },
  @{ n = 'a wiki that is not ours'; p = "$fwd/docs/wiki/notes.md";                      want = '' },
  @{ n = 'overwriting a journal';   p = "$fwd/a vault with spaces/raw/handoffs/2026-08-13-x.md"; want = 'immutable' },
  @{ n = 'writing a NEW journal';   p = "$fwd/a vault with spaces/raw/handoffs/2026-08-14-y.md"; want = '' }
)
foreach ($c in $cases) {
    $r = RunGuard ('{"tool_input":{"file_path":"' + $c.p + '"}}')
    $silent = [string]::IsNullOrWhiteSpace($r.out)
    if ($c.want -eq '') {
        Check ("guard is silent: " + $c.n) ($r.code -eq 0 -and $silent) $r.out
    } else {
        $valid = $false
        try { $null = $r.out | ConvertFrom-Json; $valid = $true } catch { }
        Check ("guard fires: " + $c.n) ($r.code -eq 0 -and $valid -and $r.out -match $c.want) $r.out
    }
}

$backslash = ($sandbox + '\a vault with spaces\wiki\decisions\x.md').Replace('\', '\\')
$r = RunGuard ('{"tool_input":{"file_path":"' + $backslash + '"}}')
Check "guard fires: a backslash path" ($r.code -eq 0 -and $r.out -match 'one writer') $r.out

$adversarial = @(
  @{ n = 'content that lies';     j = '{"tool_input":{"file_path":"src/x.py","content":"\"file_path\": \"CLAUDE.md\""}}' },
  @{ n = 'file_path is an array'; j = '{"tool_input":{"file_path":["a","b"]}}' },
  @{ n = 'file_path is null';     j = '{"tool_input":{"file_path":null}}' },
  @{ n = 'no file_path';          j = '{"tool_input":{"command":"ls"}}' },
  @{ n = 'no tool_input at all';  j = '{"tool_name":"Edit"}' },
  @{ n = 'malformed json';        j = 'not json at all' },
  @{ n = 'empty stdin';           j = '' }
)
foreach ($c in $adversarial) {
    $r = RunGuard $c.j
    Check ("guard is silent: " + $c.n) ($r.code -eq 0 -and [string]::IsNullOrWhiteSpace($r.out)) $r.out
}

# ------------------------------------------------- the guard's path-scoped rules
# .claude/rules/ does not exist in this sandbox until the line below, so every guard case above
# ran with it absent - the branch is already proved silent on a tree that has no rules directory.
# This section builds one and exercises the branch that reads it.

$rulesDir = Join-Path $sandbox '.claude/rules'
New-Item -ItemType Directory -Force -Path $rulesDir | Out-Null

# Block-form paths, the spelling _probe-paths.md was written in.
WriteUtf8 (Join-Path $rulesDir 'blk.md') @"
---
paths:
  - "guarded/*.py"
---

NONCE-BLOCK-FORM
"@

# Inline-form paths, the spelling a vault page's other list fields are written in. Both are legal
# YAML, and the field is authored in one file and synced into another, so a parser that knew only
# one spelling would be blind to half the rules it exists for and would say nothing about it.
WriteUtf8 (Join-Path $rulesDir 'inl.md') @"
---
paths: ["guarded-inline/*.md"]
---

NONCE-INLINE-FORM
"@

# A file no vault page backs and that carries no generated-marker. It is somebody's hand-written
# rule, it is legitimate, and the guard delivers it: the marker is the injector's permission to
# DELETE, and delivering is not deleting.
WriteUtf8 (Join-Path $rulesDir 'hand.md') @"
---
paths: ["hand-written/*.txt"]
---

NONCE-HAND-WRITTEN
"@

# Two rules over one path. Whichever one loses is a rule that silently never arrives, so both go.
WriteUtf8 (Join-Path $rulesDir 'two-a.md') @"
---
paths: ["shared-scope/*.md"]
---

NONCE-TWO-A
"@
WriteUtf8 (Join-Path $rulesDir 'two-b.md') @"
---
paths: ["shared-scope/*.md"]
---

NONCE-TWO-B
"@

# Not frontmatter at all: a README somebody dropped into the directory. It has to be stepped over
# rather than parsed, and it must not take the rest of the guard down with it.
WriteUtf8 (Join-Path $rulesDir 'broken.md') @"
# Notes

paths: ["broken-scope/*.md"] appears here in prose, inside no frontmatter.
"@

# A rule scoped where an earlier branch already speaks. The chain picks one branch, so this rule
# does not arrive - a stated property rather than a discovered one, pinned here so that changing
# the chain to accumulate its notes shows up as this case turning over.
WriteUtf8 (Join-Path $rulesDir 'shadow.md') @"
---
paths: ["a vault with spaces/wiki/decisions/*.md"]
---

NONCE-SHADOWED
"@

$ruleCases = @(
  @{ n = 'block-form paths';    p = "$fwd/guarded/x.py";        want = 'NONCE-BLOCK-FORM' },
  @{ n = 'inline-form paths';   p = "$fwd/guarded-inline/x.md"; want = 'NONCE-INLINE-FORM' },
  @{ n = 'a rule with no page'; p = "$fwd/hand-written/x.txt";  want = 'NONCE-HAND-WRITTEN' },
  @{ n = 'two rules, first';    p = "$fwd/shared-scope/x.md";   want = 'NONCE-TWO-A' },
  @{ n = 'two rules, second';   p = "$fwd/shared-scope/x.md";   want = 'NONCE-TWO-B' }
)
foreach ($c in $ruleCases) {
    $r = RunGuard ('{"tool_input":{"file_path":"' + $c.p + '"}}')
    $valid = $false
    try { $null = $r.out | ConvertFrom-Json; $valid = $true } catch { }
    Check ("guard delivers: " + $c.n) ($r.code -eq 0 -and $valid -and $r.out -match $c.want) $r.out
}

$r = RunGuard ('{"tool_input":{"file_path":"' + "$fwd/guarded/x.py" + '"}}')
$whole = $false
try { $whole = (($r.out | ConvertFrom-Json).hookSpecificOutput.additionalContext).Trim() -eq 'NONCE-BLOCK-FORM' } catch { }
Check "the rule arrives whole, not summarised" ($r.code -eq 0 -and $whole) $r.out

$r = RunGuard ('{"tool_input":{"file_path":"' + "$fwd/broken-scope/x.md" + '"}}')
Check "a file that is not frontmatter is stepped over" ($r.code -eq 0 -and [string]::IsNullOrWhiteSpace($r.out)) $r.out

$r = RunGuard ('{"tool_input":{"file_path":"' + "$fwd/guarded/x.txt" + '"}}')
Check "a path the globs do not cover" ($r.code -eq 0 -and [string]::IsNullOrWhiteSpace($r.out)) $r.out

$r = RunGuard ('{"tool_input":{"file_path":"' + "$fwd/a vault with spaces/wiki/decisions/x.md" + '"}}')
Check "an earlier branch still wins its path" ($r.code -eq 0 -and $r.out -match 'one writer' -and $r.out -notmatch 'NONCE-SHADOWED') $r.out

$backslashRule = ($sandbox + '\guarded\x.py').Replace('\', '\\')
$r = RunGuard ('{"tool_input":{"file_path":"' + $backslashRule + '"}}')
Check "guard delivers: a backslash path" ($r.code -eq 0 -and $r.out -match 'NONCE-BLOCK-FORM') $r.out

# What the native delivery strips, this branch must strip too - measured by probe 3, which read a
# rule file through the harness's own path-scoped delivery and found the frontmatter and the HTML
# comment on line 6 both absent. The `generated, do not edit` banner a generated rule file carries
# is free ONLY because of that, and a guard that delivered it would spend it on every edit.
WriteUtf8 (Join-Path $rulesDir 'cmt.md') @"
---
paths: ["commented/*.md"]
---

<!-- NONCE-COMMENT-STRIPPED -->

NONCE-COMMENT-DELIVERED
"@

WriteUtf8 (Join-Path $rulesDir 'multi.md') @"
---
paths: ["multiline-scope/*.md"]
---

<!-- NONCE-MULTILINE-STRIPPED
     still inside the comment
     and still inside it here -->

NONCE-MULTILINE-DELIVERED
"@

# A comment inside a fenced block survives. This corpus documents its own markers inside fences,
# so a rule explaining a marker would otherwise lose the thing it explains. Single-quoted
# here-string: inside a double-quoted one a backtick is PowerShell's escape character.
WriteUtf8 (Join-Path $rulesDir 'fenced.md') @'
---
paths: ["fenced-scope/*.md"]
---

NONCE-FENCE-DELIVERED

```
<!-- NONCE-FENCE-KEPT -->
```
'@

$r = RunGuard ('{"tool_input":{"file_path":"' + "$fwd/commented/x.md" + '"}}')
$ctx = ''
try { $ctx = ($r.out | ConvertFrom-Json).hookSpecificOutput.additionalContext } catch { }
Check "an html comment is not delivered" `
      ($r.code -eq 0 -and $ctx -match 'NONCE-COMMENT-DELIVERED' -and $ctx -notmatch 'NONCE-COMMENT-STRIPPED' -and $ctx -notmatch '<!--') $r.out

$r = RunGuard ('{"tool_input":{"file_path":"' + "$fwd/multiline-scope/x.md" + '"}}')
$ctx = ''
try { $ctx = ($r.out | ConvertFrom-Json).hookSpecificOutput.additionalContext } catch { }
Check "a comment spanning lines is not delivered" `
      ($r.code -eq 0 -and $ctx -match 'NONCE-MULTILINE-DELIVERED' -and $ctx -notmatch 'still inside' -and $ctx -notmatch 'NONCE-MULTILINE-STRIPPED') $r.out

$r = RunGuard ('{"tool_input":{"file_path":"' + "$fwd/fenced-scope/x.md" + '"}}')
$ctx = ''
try { $ctx = ($r.out | ConvertFrom-Json).hookSpecificOutput.additionalContext } catch { }
Check "a comment inside a fence survives" `
      ($r.code -eq 0 -and $ctx -match 'NONCE-FENCE-DELIVERED' -and $ctx -match 'NONCE-FENCE-KEPT') $r.out

Remove-Item -Recurse -Force $rulesDir
$r = RunGuard ('{"tool_input":{"file_path":"' + "$fwd/guarded/x.py" + '"}}')
Check "the rules directory removed again" ($r.code -eq 0 -and [string]::IsNullOrWhiteSpace($r.out)) $r.out

# ---------------------------------------------------------------- the gate
$gateHook = Join-Path $sandbox '.claude/hooks/check-the-journal.ps1'

function Payload([string] $path) {
    return (@{ tool_input = @{ file_path = $path } } | ConvertTo-Json -Compress)
}
function RunGate([string] $json) {
    $out = $json | & powershell -NoProfile -ExecutionPolicy Bypass -File $gateHook 2>&1 | Out-String
    return @{ out = $out; code = $LASTEXITCODE }
}
# Git removed from PATH, PowerShell kept. The hook derives bash from where git is, so this is the
# one failure it must ANNOUNCE rather than swallow: a guard that is silently absent is worse than
# no guard, and this project has shipped one of those already.
function RunGateWithoutGit([string] $json) {
    # PowerShell is invoked by its own install path rather than found on PATH, because PATH is
    # exactly what this case takes away. The first version stripped PATH and then asked for
    # powershell by name, so the case failed for want of its own interpreter and proved nothing
    # about the hook - a test that fails for its own reasons is not a test of anything.
    $psExe = Join-Path $PSHOME 'powershell.exe'
    $saved = $env:PATH
    $env:PATH = Join-Path $env:SystemRoot 'System32'
    try {
        $out = $json | & $psExe -NoProfile -ExecutionPolicy Bypass -File $gateHook 2>&1 | Out-String
        $code = $LASTEXITCODE
    } finally { $env:PATH = $saved }
    return @{ out = $out; code = $code }
}

$journal = Join-Path $vault 'raw/handoffs/2026-08-18-probe.md'
WriteUtf8 $journal "---`nsession: 2026-08-18`nsprint: S1`ncommits: none`n---`n`n## State`nnone`n"

$r = RunGate (Payload $journal)
Check 'gate reports a journal that fails' `
      ($r.code -eq 0 -and $r.out -match 'does not pass the vault gate') $r.out

$r = RunGate (Payload (Join-Path $sandbox 'src/app.py'))
Check 'gate ignores a path outside raw/' `
      ($r.code -eq 0 -and [string]::IsNullOrWhiteSpace($r.out)) $r.out

$r = RunGate (Payload (Join-Path $vault 'raw/handoffs/2026-08-18-probe.coverage.tsv'))
Check 'gate ignores a sidecar' `
      ($r.code -eq 0 -and [string]::IsNullOrWhiteSpace($r.out)) $r.out

$r = RunGateWithoutGit (Payload $journal)
Check 'gate says so when it cannot run' `
      ($r.code -eq 0 -and $r.out -match 'THE GATE DID NOT RUN' `
       -and $r.out -match '`bash scripts/vault-check\.sh`') $r.out

foreach ($c in $adversarial) {
    $r = RunGate $c.j
    Check ("gate is silent: " + $c.n) ($r.code -eq 0 -and [string]::IsNullOrWhiteSpace($r.out)) $r.out
}

# ---------------------------------------------------------------- the librarian lock
$lockHook = Join-Path $sandbox '.claude/hooks/lock-the-librarian.ps1'

function LockPayload([string] $tool, [string] $field, [string] $type) {
    $inp = @{ }
    if ($field) { $inp[$field] = $type }
    return (@{ tool_name = $tool; tool_input = $inp } | ConvertTo-Json -Compress)
}
function RunLock([string] $json, [string] $hookPath) {
    $out = $json | & powershell -NoProfile -ExecutionPolicy Bypass -File $hookPath 2>&1 | Out-String
    return @{ out = $out; code = $LASTEXITCODE }
}
function RunLockWithoutGit([string] $json) {
    $psExe = Join-Path $PSHOME 'powershell.exe'
    $saved = $env:PATH
    $env:PATH = Join-Path $env:SystemRoot 'System32'
    try {
        $out = $json | & $psExe -NoProfile -ExecutionPolicy Bypass -File $lockHook 2>&1 | Out-String
        $code = $LASTEXITCODE
    } finally { $env:PATH = $saved }
    return @{ out = $out; code = $code }
}

# The sandbox vault is a stub and fails the gate, so this is the refusing case. It asserts the
# CONDITION is named as well as the decision: a denial the caller cannot clear is a gate that gets
# disabled, and the owner's rule is that a refusal states what must be true or has no appeal.
#
# THE COMMAND ITSELF IS MATCHED, NOT ONLY THE WORDS ANNOUNCING IT, and that is the whole lesson of
# 2026-08-20: this case was green while the refusal named `ash scripts/vault-check.sh`. A backtick
# inside a DOUBLE-quoted PowerShell string is an escape - `b is a backspace and a backtick before a
# space is an escaped space - so both delimiters and the b were eaten on the way out. `THE CONDITION
# IS` survived intact, so an assertion on the announcement could not see it. A condition the caller
# cannot run is not a condition that was named, which is why the literal is pinned here.
$r = RunLock (LockPayload 'Agent' 'subagent_type' 'vault-librarian') $lockHook
Check 'lock denies the librarian on a red gate' `
      ($r.code -eq 0 -and $r.out -match '"permissionDecision":\s*"deny"' `
       -and $r.out -match 'THE CONDITION IS' `
       -and $r.out -match '`bash scripts/vault-check\.sh`') $r.out

# THE LOCK'S GREEN PATH IS NOT TESTED HERE, AND THE PRICE WAS ACCEPTED RATHER THAN OVERLOOKED. A
# case stood here that ran the real hook against the real tree and asserted the lock stays silent
# on a green gate - the one thing that tells a working lock from a lock that refuses everything,
# because the sandbox vault can never be green. It was thrown out on 2026-08-26: it prints MISSED
# whenever the tree is red, which makes `missed 0` unreadable at exactly the moment criterion 1 of
# the sprint is read off it. Nothing replaces it, and it also cost this suite one full gate run.
$r = RunLock (LockPayload 'Task' 'subagent_type' 'vault-librarian') $lockHook
Check 'lock knows the Task alias too' `
      ($r.code -eq 0 -and $r.out -match '"permissionDecision":\s*"deny"') $r.out

$r = RunLock (LockPayload 'Agent' 'agent_type' 'vault-librarian') $lockHook
Check 'lock knows the agent_type spelling too' `
      ($r.code -eq 0 -and $r.out -match '"permissionDecision":\s*"deny"') $r.out

$r = RunLock (LockPayload 'Agent' 'subagent_type' 'Explore') $lockHook
Check 'lock ignores another subagent' `
      ($r.code -eq 0 -and [string]::IsNullOrWhiteSpace($r.out)) $r.out

$r = RunLock (LockPayload 'Bash' 'subagent_type' 'vault-librarian') $lockHook
Check 'lock ignores another tool' `
      ($r.code -eq 0 -and [string]::IsNullOrWhiteSpace($r.out)) $r.out

$r = RunLock (LockPayload 'Agent' '' '') $lockHook
Check 'lock ignores a dispatch with no type' `
      ($r.code -eq 0 -and [string]::IsNullOrWhiteSpace($r.out)) $r.out

# Refusing on a measurement that did not happen is a refusal that can be wrong, which the ruling
# forbids. So this must ANNOUNCE and allow, never deny.
$r = RunLockWithoutGit (LockPayload 'Agent' 'subagent_type' 'vault-librarian')
Check 'lock says so when it cannot measure, and does not refuse' `
      ($r.code -eq 0 -and $r.out -match 'THE LOCK DID NOT RUN' `
       -and $r.out -match '`bash scripts/vault-check\.sh`' `
       -and $r.out -notmatch 'permissionDecision') $r.out

foreach ($c in $adversarial) {
    $r = RunLock $c.j $lockHook
    Check ("lock is silent: " + $c.n) ($r.code -eq 0 -and [string]::IsNullOrWhiteSpace($r.out)) $r.out
}

# THE ONE CASE THAT READS THE REAL settings.json RATHER THAN THE SANDBOX, and it is deliberate.
# Every case above proves the lock's LOGIC; none of them proves it is WIRED, and a lock that is not
# wired is indistinguishable from one with nothing to say. The dispatch tool was renamed once
# already - Task to Agent, in 2.1.63, with the old name kept as an alias - so a second rename would
# leave the matcher naming two dead words and the lock would vanish in silence. This turns that
# from a silent disappearance into a red line on the next run, which is the whole of the owner's
# principle: erring is allowed, not being able to see it is not.
#
# It asserts REGISTRATION, never firing. Whether the harness actually calls the hook cannot be
# tested from here at all - hooks are read at session start - and the acceptance test for that is
# a restart, a deliberately reddened vault, and an attempted librarian dispatch.
$settings = Join-Path $repo '.claude/settings.json'
$wired = $false
try {
    $cfg = Get-Content $settings -Raw | ConvertFrom-Json
    foreach ($entry in $cfg.hooks.PreToolUse) {
        if ($entry.matcher -match 'Agent|Task') {
            foreach ($h in $entry.hooks) {
                if ($h.command -match 'lock-the-librarian') { $wired = $true }
            }
        }
    }
} catch { }
Check 'the lock is registered on the dispatch tool' $wired `
      "no PreToolUse entry in .claude/settings.json matches Agent|Task and runs lock-the-librarian"

# ---------------------------------------------------------------------------------------------
# The pre-task ritual: the plan hook, the write net, and the registration of both.
#
# THE LEDGER IS REDIRECTED INTO THE SANDBOX by `JOBHUNT_PRETASK_LEDGER`, which is what that variable
# exists for. A suite is a test environment and works in its own sandbox; reaching into the real
# `.superpowers/sdd/` would make every case depend on what a real session happened to do. Deriving
# the path from `cwd` was rejected for the mirror reason: `cwd` arrives in the payload these cases
# fabricate, so the subject would be isolated by the very thing under test.
$planHook   = Join-Path $sandbox '.claude/hooks/check-the-plan.ps1'
$savedLedger = $env:JOBHUNT_PRETASK_LEDGER

function PlanPayload([string] $event, [string] $session, [string] $tool) {
    if (-not $tool) { $tool = 'ExitPlanMode' }
    return (@{
        tool_name       = $tool
        hook_event_name = $event
        session_id      = $session
        permission_mode = 'plan'
        tool_input      = @{ }
    } | ConvertTo-Json -Compress)
}
function RunPlan([string] $json) {
    $out = $json | & powershell -NoProfile -ExecutionPolicy Bypass -File $planHook 2>&1 | Out-String
    return @{ out = $out; code = $LASTEXITCODE }
}
function GuardPayload([string] $path, [string] $session) {
    return (@{
        tool_name       = 'Edit'
        hook_event_name = 'PreToolUse'
        session_id      = $session
        permission_mode = 'plan'
        tool_input      = @{ file_path = $path }
    } | ConvertTo-Json -Compress)
}
# A fresh ledger per case, so no case can pass or fail because of one that ran before it.
function FreshLedger([string] $name) {
    $p = Join-Path $sandbox ("ledger-$name.tsv")
    Remove-Item -LiteralPath $p -Force -ErrorAction SilentlyContinue
    Remove-Item -LiteralPath ($p + '.session') -Force -ErrorAction SilentlyContinue
    $env:JOBHUNT_PRETASK_LEDGER = $p
    return $p
}

# THE ADVISORY IS ASSERTED ON ITS OUTPUT AND NEVER ON AN EXIT CODE. An advisory leaves the code at
# zero by construction, so a clean run proves nothing about whether it spoke.
FreshLedger 'plan-a' | Out-Null
$r = RunPlan (PlanPayload 'PreToolUse' 'S1' '')
Check 'plan hook asks for a pre-task that has not run' `
      ($r.code -eq 0 -and $r.out -match 'about to present a plan') $r.out

# The rule text is not in this script and must not be: the words live in the vault and are rendered.
# What is asserted here is that the hook says so LOUDLY when it cannot deliver them, because a guard
# that is silently absent is worse than none.
Check 'plan hook says so when the rule text cannot be delivered' `
      ($r.out -match 'COULD NOT BE DELIVERED' -or $r.out -match 'pre-task\.md') $r.out

$ledger = $env:JOBHUNT_PRETASK_LEDGER
[System.IO.File]::AppendAllText($ledger, "2026-01-01T00:00:00`tS1`tpre-task`tplan`tyes`tx`n",
    (New-Object System.Text.UTF8Encoding($false)))
$r = RunPlan (PlanPayload 'PreToolUse' 'S1' '')
Check 'plan hook is silent once a pre-task is recorded' `
      ($r.code -eq 0 -and $r.out -notmatch 'about to present a plan') $r.out

# A pre-task belongs to the plan it checked. Once that plan is approved the scope closes, and the
# next plan inherits nothing - otherwise one ritual would licence a whole session of plans.
[System.IO.File]::AppendAllText($ledger, "2026-01-02T00:00:00`tS1`tscope-approved`tplan`tyes`t`n",
    (New-Object System.Text.UTF8Encoding($false)))
$r = RunPlan (PlanPayload 'PreToolUse' 'S1' '')
Check 'plan hook asks again for a plan after the last scope closed' `
      ($r.code -eq 0 -and $r.out -match 'about to present a plan') $r.out

# Another session's lines are not this session's evidence.
$r = RunPlan (PlanPayload 'PreToolUse' 'S2' '')
Check 'plan hook does not read another session as its own' `
      ($r.code -eq 0 -and $r.out -match 'about to present a plan') $r.out

$r = RunPlan (PlanPayload 'PreToolUse' 'S1' 'Edit')
Check 'plan hook ignores another tool' ($r.code -eq 0 -and $r.out.Trim() -eq '') $r.out

$r = RunPlan ''
Check 'plan hook is silent: empty stdin' ($r.code -eq 0 -and $r.out.Trim() -eq '') $r.out

$r = RunPlan '{ not json'
Check 'plan hook is silent: malformed json' ($r.code -eq 0 -and $r.out.Trim() -eq '') $r.out

# The approval is the only machine-observable form of the owner accepting a scope: there is no hook
# event for a permission-mode change, and no hook output can cause one.
FreshLedger 'plan-b' | Out-Null
$r = RunPlan (PlanPayload 'PostToolUse' 'S3' '')
$rows = Get-Content -LiteralPath $env:JOBHUNT_PRETASK_LEDGER -ErrorAction SilentlyContinue
Check 'an approved plan is recorded as a scope' `
      ($r.code -eq 0 -and ($rows -join "`n") -match 'scope-approved') (($rows -join "`n"))

# --- the write net -----------------------------------------------------------------------------

FreshLedger 'net-a' | Out-Null
$r = RunGuard (GuardPayload "$fwd/src/anything.py" 'S4')
Check 'the net advises on the first write of a session' `
      ($r.code -eq 0 -and $r.out -match 'first write of this session') $r.out

$r = RunGuard (GuardPayload "$fwd/src/anything.py" 'S4')
Check 'the net advises once and not twice' `
      ($r.code -eq 0 -and $r.out -notmatch 'first write of this session') $r.out

# THE HEARTBEAT. A session that edited files and left no line here has hooks that never loaded -
# which no reading of settings.json can detect, because the file on disk is correct in that case.
$rows = Get-Content -LiteralPath $env:JOBHUNT_PRETASK_LEDGER -ErrorAction SilentlyContinue
Check 'the first write is recorded as a heartbeat' `
      (($rows -join "`n") -match 'first-write') (($rows -join "`n"))

# The permission mode is carried because it is the only place the harness says which mode the
# session ACTUALLY started in: the VS Code extension takes that from its own user settings and
# ignores this repository's entirely.
Check 'the ledger carries the permission mode the session is really in' `
      (($rows -join "`n") -match "`tplan`t") (($rows -join "`n"))

# THE HEARTBEAT SURVIVES A SESSION THAT DID EVERYTHING RIGHT. The `pre-task` row is written by a
# script the session runs, not by a hook, so keying the heartbeat on `this session has any line at
# all` would suppress it in exactly the sessions that performed the ritual first - which is the
# intended order. The proof that a HOOK ran has to key on a line a hook writes.
FreshLedger 'net-heartbeat' | Out-Null
[System.IO.File]::AppendAllText($env:JOBHUNT_PRETASK_LEDGER,
    "2026-01-01T00:00:00`tS6`tpre-task`tunknown`tyes`tx`n",
    (New-Object System.Text.UTF8Encoding($false)))
$r = RunGuard (GuardPayload "$fwd/src/anything.py" 'S6')
$rows = Get-Content -LiteralPath $env:JOBHUNT_PRETASK_LEDGER -ErrorAction SilentlyContinue
Check 'the heartbeat is written even when the ritual ran first' `
      (($rows -join "`n") -match 'first-write') (($rows -join "`n"))
Check 'and the net stays silent, because the ritual did run' `
      ($r.out -notmatch 'first write of this session') $r.out

# THE COLUMN A HUMAN READS AT A RETRO MEANS `a pre-task is on the record`, and it must not quietly
# come to mean `nothing is owed`. The two part company on the second write of a session that skipped
# the ritual, where nothing is owed only because the advisory was already spent.
FreshLedger 'net-column' | Out-Null
RunGuard (GuardPayload "$fwd/src/one.py" 'S7') | Out-Null
$rows = Get-Content -LiteralPath $env:JOBHUNT_PRETASK_LEDGER -ErrorAction SilentlyContinue
$fw = ($rows | Where-Object { $_ -match "`tfirst-write`t" })
Check 'a skipped ritual is recorded as skipped, not as not-owed' `
      ($fw -and $fw -match "`tno`t") ($rows -join "`n")

# THE VAULT IS EXCLUDED. The librarian writes only the vault and writes about fifty pages per
# ingest; a vault write is not implementation and the ritual is not addressed to it.
FreshLedger 'net-b' | Out-Null
$r = RunGuard (GuardPayload "$fwd/a vault with spaces/wiki/decisions/x.md" 'S5')
Check 'the net does not reach a wiki write' `
      ($r.code -eq 0 -and $r.out -notmatch 'first write of this session') $r.out
Check 'the one-writer note still fires on that same write' `
      ($r.code -eq 0 -and $r.out -match 'one writer') $r.out

# ONCE PER SESSION, NOT ONCE PER PAGE - the channel changes and the scope does not.
$r = RunGuard (GuardPayload "$fwd/a vault with spaces/wiki/decisions/y.md" 'S5')
Check 'the one-writer note does not repeat within a session' `
      ($r.code -eq 0 -and $r.out -notmatch 'one writer') $r.out

# THE SCHEMA EXCEPTION IS A FLAG OF ITS OWN, AND THIS PAIR IS WHY. Narrowing `$inWiki` would have
# silenced the note AND taken the schemas out of the pre-task exclusion, which is a different
# decision belonging to a different page. Both halves are asserted on one write: the note is
# silent, and the net still does not speak.
FreshLedger 'net-schema' | Out-Null
$r = RunGuard (GuardPayload "$fwd/a vault with spaces/wiki/decisions/_schema.yaml" 'S6')
Check 'the one-writer note is silent on a per-folder schema' `
      ($r.code -eq 0 -and $r.out -notmatch 'one writer') $r.out
Check 'and the net still does not reach it either' `
      ($r.code -eq 0 -and $r.out -notmatch 'first write of this session') $r.out

# WITHOUT A SESSION THERE IS NO REPEAT TO RECOGNISE, so it speaks every time. This is also why every
# case written before the ledger existed, none of which sends a session_id, is unaffected by it.
FreshLedger 'net-c' | Out-Null
$r = RunGuard (Payload "$fwd/a vault with spaces/wiki/decisions/x.md")
$r2 = RunGuard (Payload "$fwd/a vault with spaces/wiki/decisions/y.md")
Check 'the one-writer note repeats when there is no session to key on' `
      ($r.out -match 'one writer' -and $r2.out -match 'one writer') ($r.out + $r2.out)

# AND THE NET NEEDS A SESSION TO COUNT ONCE WITH. With no identifier nothing can be recognised as a
# repeat, so the net would speak on every edit for the rest of the session - the exact noise it was
# built to avoid, attached to a ritual the reader cannot satisfy. The wiki note above makes the
# opposite choice on purpose: repeating a note is annoying, repeating this one is its failure mode.
FreshLedger 'net-d' | Out-Null
$r = RunGuard (Payload "$fwd/src/anything.py")
Check 'the net is silent when there is no session to count once with' `
      ($r.code -eq 0 -and $r.out.Trim() -eq '') $r.out

# --- the session start, and one session per ledger -----------------------------------------------

# THE PAYLOAD PATH WAS UNTESTED UNTIL HERE. `RunBrief` pipes nothing, so every brief case above
# exercises the `IsInputRedirected` FALSE branch - and the row, the reset and the rotation all live
# on the true one. A runner that pipes is the whole reason those cases could be written.
function BriefPayload([string] $session, [string] $source) {
    return (@{
        hook_event_name = 'SessionStart'
        session_id      = $session
        source          = $source
        permission_mode = 'plan'
    } | ConvertTo-Json -Compress)
}
function RunBriefWith([string] $json) {
    $out = $json | & powershell -NoProfile -ExecutionPolicy Bypass -File $briefHook 2>&1 | Out-String
    return @{ out = $out; code = $LASTEXITCODE }
}
$enc = New-Object System.Text.UTF8Encoding($false)

FreshLedger 'start-a' | Out-Null
$r = RunBriefWith (BriefPayload 'S10' 'startup')
$rows = (Get-Content -LiteralPath $env:JOBHUNT_PRETASK_LEDGER -ErrorAction SilentlyContinue) -join "`n"
Check 'a session start is recorded, carrying its source' `
      ($r.code -eq 0 -and $rows -match 'session-start:startup') $rows

# THE BRIEF IS THE ONE THING THIS FILE GUARANTEES, and a throw on the ledger path would cost the
# reader exactly the thing the hook exists to deliver. That has been paid here once, with `git` off
# the hook's PATH.
Check 'and the brief is still printed on that path' ($r.out -match 'fresh') $r.out

# `no` WOULD BE A CLAIM ABOUT THE WORLD. Nothing had been asked of the ritual at the moment this row
# was written, so the column a human reads at a retro must not say the ritual was skipped. This
# ledger has already shipped one column filled from the branch condition rather than from the world.
$startRow = @(Get-Content -LiteralPath $env:JOBHUNT_PRETASK_LEDGER | Where-Object { $_ -match 'session-start' })
Check 'the session-start row claims nothing about the ritual' `
      ($startRow.Count -eq 1 -and ($startRow[0] -split "`t")[4] -eq '-') ($startRow -join "`n")

# NO KEY, NO ROW. A rate limit, a heartbeat and a scope are all claims about a key; a keyless row is
# one that nothing can ever match.
FreshLedger 'start-b' | Out-Null
$r = RunBriefWith (BriefPayload '' 'startup')
Check 'no session identifier writes no row' `
      ($r.code -eq 0 -and -not (Test-Path -LiteralPath $env:JOBHUNT_PRETASK_LEDGER)) $r.out

# THE RESET IS ASSERTED IN BOTH DIRECTIONS. A reset that fires on everything and a reset that fires
# on nothing each pass a single-sided case; only the pair pins the flag.
FreshLedger 'start-clear' | Out-Null
[System.IO.File]::AppendAllText($env:JOBHUNT_PRETASK_LEDGER,
    "2026-01-01T00:00:00`tS11`tpre-task`tplan`tyes`tx`n", $enc)
$r = RunPlan (PlanPayload 'PreToolUse' 'S11' '')
Check 'the plan hook is silent while a pre-task stands' `
      ($r.out -notmatch 'about to present a plan') $r.out

RunBriefWith (BriefPayload 'S11' 'compact') | Out-Null
$r = RunPlan (PlanPayload 'PreToolUse' 'S11' '')
Check 'a compaction does not drop it: the same work, a squeezed context' `
      ($r.out -notmatch 'about to present a plan') $r.out

RunBriefWith (BriefPayload 'S11' 'clear') | Out-Null
$r = RunPlan (PlanPayload 'PreToolUse' 'S11' '')
Check 'a clear does: the conversation never saw that plan' `
      ($r.out -match 'about to present a plan') $r.out

# ROTATION FIRES ON `startup` AND ON NOTHING ELSE, and the negative goes first so it cannot pass on a
# directory a later case created.
FreshLedger 'rotate-a' | Out-Null
$ledgerPath = $env:JOBHUNT_PRETASK_LEDGER
$archive = Join-Path $sandbox 'ledger'
[System.IO.File]::AppendAllText($ledgerPath, "2026-01-01T00:00:00`tS12`tpre-task`tplan`tyes`told`n", $enc)
foreach ($src in @('resume', 'compact', 'clear')) { RunBriefWith (BriefPayload 'S12' $src) | Out-Null }
$rows = (Get-Content -LiteralPath $ledgerPath) -join "`n"
Check 'a resume, a compaction and a clear do not rotate' `
      ($rows -match 'old' -and -not (Test-Path -LiteralPath $archive)) $rows

RunBriefWith (BriefPayload 'S12' 'startup') | Out-Null
$moved = @(Get-ChildItem -LiteralPath $archive -Filter 'pre-task-ledger.*.tsv' -ErrorAction SilentlyContinue)
Check 'a startup rotates the ledger whole' ($moved.Count -eq 1) `
      ('files under ' + $archive + ': ' + (($moved | ForEach-Object Name) -join ', '))
Check 'and the archived file keeps every old row' `
      ($moved.Count -eq 1 -and ((Get-Content -LiteralPath $moved[0].FullName) -join "`n") -match 'old') `
      ('archived: ' + (($moved | ForEach-Object Name) -join ', '))
$rows = (Get-Content -LiteralPath $ledgerPath) -join "`n"
Check 'while the live file opens with a pointer and this session alone' `
      ($rows -match '^# rotated' -and $rows -match 'session-start:startup' -and $rows -notmatch 'old') $rows

# A ROTATION THAT FINDS NOTHING MUST NOT COST THE BRIEF EITHER - and nothing watches this function,
# so a throw here would be swallowed and the file would simply grow forever with no reader told.
FreshLedger 'rotate-b' | Out-Null
$r = RunBriefWith (BriefPayload 'S13' 'startup')
Check 'a missing ledger rotates to nothing, not to an error' `
      ($r.code -eq 0 -and $r.out -match 'fresh') $r.out

FreshLedger 'rotate-c' | Out-Null
[System.IO.File]::WriteAllText($env:JOBHUNT_PRETASK_LEDGER, '', $enc)
$before = @(Get-ChildItem -LiteralPath $archive -Filter '*.tsv' -ErrorAction SilentlyContinue).Count
RunBriefWith (BriefPayload 'S14' 'startup') | Out-Null
$after = @(Get-ChildItem -LiteralPath $archive -Filter '*.tsv' -ErrorAction SilentlyContinue).Count
Check 'an empty ledger is not archived as though it were a session' ($after -eq $before) `
      ("before=$before after=$after")

$env:JOBHUNT_PRETASK_LEDGER = $savedLedger

# --- registration --------------------------------------------------------------------------------
# Same argument as the lock's registration case: every case above proves LOGIC, none proves WIRING,
# and a hook that is not wired is indistinguishable from one with nothing to say.
$planPre = $false
$planPost = $false
try {
    $cfg2 = Get-Content $settings -Raw | ConvertFrom-Json
    foreach ($entry in $cfg2.hooks.PreToolUse) {
        if ($entry.matcher -match 'ExitPlanMode') {
            foreach ($h in $entry.hooks) { if ($h.command -match 'check-the-plan') { $planPre = $true } }
        }
    }
    foreach ($entry in $cfg2.hooks.PostToolUse) {
        if ($entry.matcher -match 'ExitPlanMode') {
            foreach ($h in $entry.hooks) { if ($h.command -match 'check-the-plan') { $planPost = $true } }
        }
    }
} catch { }
Check 'the plan hook is registered before the plan is presented' $planPre `
      "no PreToolUse entry in .claude/settings.json matches ExitPlanMode and runs check-the-plan"
Check 'the plan hook is registered after the plan is approved' $planPost `
      "no PostToolUse entry in .claude/settings.json matches ExitPlanMode and runs check-the-plan"

# EVERY HOOK SCRIPT IS EITHER REGISTERED OR DOT-SOURCED, AS A PROPERTY RATHER THAN AN EXEMPTION
# LIST. A property is re-evaluated on every run and cannot go stale; a list is a second copy of a
# judgement nobody revisits. The class this catches is real and has happened here: a hook left on
# disk after its settings block was removed is inert, and looks exactly like one that has nothing
# to say. Shared libraries - `vault-path.ps1`, `pre-task-state.ps1` - are reached the other way, and
# the predicate finds that out by reading the files rather than by being told.
$unwired = @()
try {
    $settingsText = Get-Content $settings -Raw
    $hookFiles = Get-ChildItem -LiteralPath (Join-Path $repo '.claude/hooks') -Filter '*.ps1'
    $allText = ($hookFiles | ForEach-Object { Get-Content $_.FullName -Raw }) -join "`n"
    foreach ($f in $hookFiles) {
        $named = $settingsText -match [regex]::Escape($f.Name)
        $sourced = $allText -match ("\.\s+\(Join-Path[^\)]*" + [regex]::Escape($f.Name))
        if (-not $named -and -not $sourced) { $unwired += $f.Name }
    }
} catch { $unwired += "could not read: $_" }
Check 'every hook script is either registered or dot-sourced' ($unwired.Count -eq 0) `
      ("inert file(s) in .claude/hooks/: " + ($unwired -join ', '))

# ---------------------------------------------------- the dispatch recorder, added 2026-08-22
#
# WHAT IT IS FOR IS THE PART WORTH TESTING. `/pre-task` records itself by a script the SESSION runs,
# plan mode forbids the session to write, and the rule places the ritual inside plan mode - so the
# ritual done exactly right left no row and the guard asked for it again. Four times in one session.
# A hook can write during planning, and these cases pin the two halves of the repair: the row gets
# written, and the row discharges the ritual.
#
# THE ROW IS AN OBSERVATION AND THE DISCHARGE IS AN INFERENCE, and they are tested separately on
# purpose. The hook writes `dispatch:<type>`; `Read-LedgerState` decides that `dispatch:pre-task`
# means the ritual ran. If those were one step, a later reader could not tell which column recorded
# what happened and which recorded what somebody concluded from it.
$dispatchHook = Join-Path $repo '.claude/hooks/record-the-dispatch.ps1'
function DispatchPayload([string] $session, [string] $tool, [string] $type, [string] $mode) {
    $input = @{ description = 'a probe dispatch' }
    if ($type) { $input.subagent_type = $type }
    return (@{
        hook_event_name = 'PostToolUse'
        tool_name       = $tool
        session_id      = $session
        permission_mode = $mode
        tool_input      = $input
    } | ConvertTo-Json -Depth 5 -Compress)
}
function RunDispatch([string] $json) {
    $out = $json | & powershell -NoProfile -ExecutionPolicy Bypass -File $dispatchHook 2>&1 | Out-String
    return @{ out = $out; code = $LASTEXITCODE }
}

FreshLedger 'dispatch-a' | Out-Null
$r = RunDispatch (DispatchPayload 'S20' 'Agent' 'vault-librarian' 'default')
$rows = @(Get-Content -LiteralPath $env:JOBHUNT_PRETASK_LEDGER -ErrorAction SilentlyContinue)
Check 'a returned dispatch writes one row naming the agent type' `
      ($r.code -eq 0 -and $rows.Count -eq 1 -and ($rows[0] -split "`t")[2] -eq 'dispatch:vault-librarian') `
      ($rows -join "`n")

# `-` AND NOT `no`. A dispatch row asserts nothing about whether a pre-task is on the record, and
# `no` in that column is a claim about the world that a human reads at a retro. This ledger has
# already shipped one column filled from the branch condition that produced it.
Check 'a dispatch row claims nothing about the ritual' `
      ($rows.Count -eq 1 -and ($rows[0] -split "`t")[4] -eq '-') ($rows -join "`n")

# THE DEFAULT AGENT CARRIES NO `subagent_type` AT ALL, and dropping those rows would make a session
# that dispatched ten agents look like one that dispatched none - an instrument failing towards
# "nothing happened here", which is the direction this repository has already been bitten by.
FreshLedger 'dispatch-b' | Out-Null
$r = RunDispatch (DispatchPayload 'S21' 'Agent' '' 'default')
$rows = @(Get-Content -LiteralPath $env:JOBHUNT_PRETASK_LEDGER -ErrorAction SilentlyContinue)
Check 'a dispatch with no subagent_type is still recorded, as default' `
      ($rows.Count -eq 1 -and ($rows[0] -split "`t")[2] -eq 'dispatch:default') ($rows -join "`n")

# BOTH SPELLINGS OF THE TOOL. `Task` was renamed to `Agent` and still resolves as an alias, so a
# recorder that knows one name is a recorder that silently does not exist on some version.
FreshLedger 'dispatch-c' | Out-Null
RunDispatch (DispatchPayload 'S22' 'Task' 'vault-librarian' 'default') | Out-Null
$rows = @(Get-Content -LiteralPath $env:JOBHUNT_PRETASK_LEDGER -ErrorAction SilentlyContinue)
Check 'the old tool name Task is recorded too' `
      ($rows.Count -eq 1 -and ($rows[0] -split "`t")[2] -eq 'dispatch:vault-librarian') ($rows -join "`n")

# AND THE NEGATIVE, because a recorder that writes on everything is not a recorder of dispatches.
FreshLedger 'dispatch-d' | Out-Null
$r = RunDispatch (DispatchPayload 'S23' 'Write' 'vault-librarian' 'default')
Check 'a non-dispatch tool writes no row' `
      ($r.code -eq 0 -and -not (Test-Path -LiteralPath $env:JOBHUNT_PRETASK_LEDGER)) $r.out

# THE HALF THAT CLOSES THE PLAN-MODE HOLE: written while planning, and read back as the ritual.
# Asserted through the plan hook rather than by inspecting the state object, because what was broken
# was the guard asking again - not the parsing.
FreshLedger 'dispatch-e' | Out-Null
$r = RunPlan (PlanPayload 'PreToolUse' 'S24' '')
Check 'without a dispatch row the plan hook asks for the ritual' `
      ($r.out -match 'about to present a plan') $r.out

RunDispatch (DispatchPayload 'S24' 'Agent' 'pre-task' 'plan') | Out-Null
$rows = @(Get-Content -LiteralPath $env:JOBHUNT_PRETASK_LEDGER -ErrorAction SilentlyContinue)
$planRow = @($rows | Where-Object { $_ -match 'dispatch:pre-task' })
Check 'a hook writes its row in plan mode, which the session cannot' `
      ($planRow.Count -eq 1 -and ($planRow[0] -split "`t")[3] -eq 'plan') ($rows -join "`n")

$r = RunPlan (PlanPayload 'PreToolUse' 'S24' '')
Check 'a returned pre-task dispatch discharges the ritual' `
      ($r.out -notmatch 'about to present a plan') $r.out

# AND IT DISCHARGES NOTHING ELSE. Any other agent type is a dispatch and not the ritual; a case that
# only proved the positive would pass on a reader that treated every dispatch as a pre-task.
FreshLedger 'dispatch-f' | Out-Null
RunDispatch (DispatchPayload 'S25' 'Agent' 'vault-librarian' 'plan') | Out-Null
$r = RunPlan (PlanPayload 'PreToolUse' 'S25' '')
Check 'a dispatch of some other agent does not discharge it' `
      ($r.out -match 'about to present a plan') $r.out

# ---------------------------------------------------- the feedback catcher
#
# THIS HOOK IS AN INSTRUMENT FOR A RULE THAT HAD NONE, which is what these cases are really about.
# `write-the-miss-into-vault-feedback-before-the-turn-ends` is one of six rules in `wiki/rules/`
# owing a mechanical check, and its own divergence page records EIGHT breakages with a single
# cause: plan mode forbids the session to write, so the party the rule binds is disarmed exactly
# when it notices something. Speaking the line and letting a hook file it is the answer that page
# named and nobody applied. A live try proves it once; these prove it every run.
#
# THE FENCE IS BUILT FROM `[char]96` AND NEVER TYPED. A backtick is PowerShell's escape character,
# and a test whose fixture is one escaping mistake away from meaning something else is a test that
# will go green for the wrong reason.
Copy-Item (Join-Path $repo '.claude/hooks/catch-the-feedback.ps1') (Join-Path $sandbox '.claude/hooks')
$catchHook = Join-Path $sandbox '.claude/hooks/catch-the-feedback.ps1'
$catchSdd = Join-Path $sandbox '.superpowers/sdd'
$catchFile = Join-Path $catchSdd 'vault-feedback.md'
$fence = -join ([char]96, [char]96, [char]96)

function FreshFeedback {
    Remove-Item -Recurse -Force $catchSdd -ErrorAction SilentlyContinue
    New-Item -ItemType Directory -Force -Path $catchSdd | Out-Null
    WriteUtf8 $catchFile "# header`n`n---`n"
}
function CatchPayload([string] $turn, [string] $message, [string] $delta, [bool] $final) {
    return (@{
        hook_event_name = 'MessageDisplay'
        session_id      = 'S-catch'
        turn_id         = $turn
        message_id      = $message
        index           = 0
        final           = $final
        delta           = $delta
    } | ConvertTo-Json -Depth 5 -Compress)
}
$catchPayload = Join-Path $sandbox 'catch-payload.json'
function RunCatch([string] $json) {
    # DELIVERED THROUGH A FILE AND NOT A PIPE, AND THAT IS NOT A STYLE CHOICE. A pipe between two
    # PowerShell processes is encoded by THIS script's `[Console]::OutputEncoding`, which cannot
    # always be set - the try/catch at the top of this file swallows that failure by design - and
    # the codepage it falls back to represents neither a guillemet nor Cyrillic. Each character it
    # cannot encode becomes a literal `?`.
    #
    # MEASURED 2026-08-26, and it is why this exists: a payload carrying a seven-character Russian
    # quotation in guillemets arrived at the hook as EIGHT QUESTION MARKS, one per character. The
    # case built on it failed against a hook that was correct, which is the worst direction - it
    # accuses the subject and exonerates the instrument.
    #
    # AND NOTHING HAD EVER ASKED. This file held ZERO non-ASCII bytes until that case, in a
    # repository whose entire feedback channel is the owner's Russian. The bytes now go from a
    # UTF-8 file straight to the child's stdin, where no console encoding stands between them.
    [System.IO.File]::WriteAllText($catchPayload, $json, (New-Object System.Text.UTF8Encoding $false))
    $out = & cmd /c "powershell -NoProfile -ExecutionPolicy Bypass -File `"$catchHook`" < `"$catchPayload`"" 2>&1 | Out-String
    # `-Encoding UTF8` on the read back, for the same reason: the hook writes UTF-8 and the default
    # here is the ANSI codepage, so a case asserting anything non-ASCII would compare mojibake.
    return @{ out = $out; code = $LASTEXITCODE; body = (Get-Content -Raw -Encoding UTF8 -LiteralPath $catchFile) }
}

FreshFeedback
$r = RunCatch (CatchPayload 't1' 'm1' "$fence`VAULT-FEEDBACK`nmiss: the vault said X`n$fence" $true)
Check 'a fenced block in the message is filed' `
      ($r.code -eq 0 -and $r.body -match 'miss: the vault said X') $r.body

# THE HOOK MUST NEVER SPEAK. `MessageDisplay` is display-only and its stdout is not a channel this
# hook is entitled to; a recorder that talks changes what it is recording.
Check 'and it prints nothing while doing it' ($r.out.Trim() -eq '') $r.out

FreshFeedback
$nested = "$fence$fence`n$fence`VAULT-FEEDBACK`nmiss: documentation, not a record`n$fence`n$fence$fence"
$r = RunCatch (CatchPayload 't2' 'm2' $nested $true)
Check 'a block nested inside another fence is an example and is not filed' `
      ($r.body -notmatch 'documentation, not a record') $r.body

FreshFeedback
$r = RunCatch (CatchPayload 't3' 'm3' "$fence`bash`necho nothing`n$fence" $true)
Check 'an ordinary fenced block files nothing' ($r.body -notmatch 'echo nothing') $r.body

FreshFeedback
$two = "$fence`VAULT-FEEDBACK`nmiss: first`n$fence`nprose`n$fence`VAULT-FEEDBACK`nharness: second`n$fence"
$r = RunCatch (CatchPayload 't4' 'm4' $two $true)
Check 'two blocks in one message are both filed' `
      ($r.body -match 'miss: first' -and $r.body -match 'harness: second') $r.body

# A `miss:` is obliged to say WHERE it surfaced, which is rarely one line. A catcher that files the
# first line and drops the rest would satisfy every case above and lose the half that matters.
FreshFeedback
$r = RunCatch (CatchPayload 't5' 'm5' "$fence`VAULT-FEEDBACK`nmeasure: one`ntwo`nthree`n$fence" $true)
Check 'a multi-line block arrives whole and stays one list item' `
      ($r.body -match 'measure: one' -and $r.body -match "`n  two" -and $r.body -match "`n  three") $r.body

# ACCUMULATE UNTIL `final`. One measured message arrived in a single call with the whole text, but
# the event's own description promises a batch of newly completed lines - so a block split across
# two flushes must still arrive whole, and nothing may be filed before the message is finished.
FreshFeedback
$r = RunCatch (CatchPayload 't6' 'm6' "$fence`VAULT-FEEDBACK`nmiss: split across" $false)
Check 'nothing is filed while the message is still streaming' ($r.body -notmatch 'split across') $r.body
$r = RunCatch (CatchPayload 't6' 'm6' " two flushes`n$fence" $true)
Check 'a block split across two flushes is filed whole at final' `
      ($r.body -match 'miss: split across two flushes') $r.body

# THE SAME MESSAGE MUST NOT FILE TWICE. `message_id` is stable across every flush of one message,
# measured 2026-08-24, so it is the key - and a `final` flush arriving twice is the ordinary case
# rather than the exotic one.
FreshFeedback
RunCatch (CatchPayload 't7' 'm7' "$fence`VAULT-FEEDBACK`nmiss: only once`n$fence" $true) | Out-Null
$r = RunCatch (CatchPayload 't7' 'm7' "$fence`VAULT-FEEDBACK`nmiss: only once`n$fence" $true)
$hits = ([regex]::Matches($r.body, 'miss: only once')).Count
Check 'the same message does not file its block twice' ($hits -eq 1) ("occurrences: $hits`n" + $r.body)

# THE DRAIN WINDOW, and it is the reason this hook could have made a recorded bug permanent.
# `whoever-filed-a-feedback-line-empties-it` is a prohibition: `/handoff` empties the file once it
# has copied the lines into the journal. It does that DURING a turn this hook also fires in, so an
# automatic catcher refilling the file behind it would turn an occasional five-entry loss into a
# standing one. The test is two numbers - the size at the turn's first sighting against the size
# now - and never a judgement about what happened.
FreshFeedback
RunCatch (CatchPayload 't8' 'm8a' "$fence`VAULT-FEEDBACK`nmiss: before the drain`n$fence" $true) | Out-Null
WriteUtf8 $catchFile "# header`n"
$r = RunCatch (CatchPayload 't8' 'm8b' "$fence`VAULT-FEEDBACK`nmiss: after the drain`n$fence" $true)
Check 'a turn whose file was drained is not refilled behind the drain' `
      ($r.body -notmatch 'after the drain') $r.body

# AND THE NEXT TURN RESUMES. A skip keyed to the turn rather than to the file would silence the
# channel for the rest of the session, which is a worse failure than the one it prevents.
$r = RunCatch (CatchPayload 't9' 'm9' "$fence`VAULT-FEEDBACK`nmiss: the turn after`n$fence" $true)
Check 'the next turn files again' ($r.body -match 'miss: the turn after') $r.body

# A KIND THIS FILE DOES NOT DECLARE IS KEPT, MARKED, AND NEVER DROPPED. A wrong record is
# acceptable and an invisible one is not - and a catcher that silently discards what it does not
# recognise is the shape that produced the drain-and-template disagreement in the first place.
FreshFeedback
$r = RunCatch (CatchPayload 't10' 'm10' "$fence`VAULT-FEEDBACK`nbanana: not a declared kind`n$fence" $true)
Check 'an undeclared kind is filed as written, with a note' `
      ($r.body -match 'banana: not a declared kind' -and $r.body -match 'not declared by this file') $r.body

# A MARK CLAIMING HIS WORDS AND CARRYING NONE OF THEM, in the same shape: kept, marked, never
# dropped. THE PAIR IS THE WHOLE DISCRIMINATION - the same record with and without a quotation,
# and only one of them draws the note. A case asserting only that the note appears would pass
# against a hook that noted every `decision:` record, which is the shape of green this repository
# has shipped six times.
#
# THE GUILLEMETS ARE BUILT FROM CHARACTER CODES, like the fence, and the Russian inside them too:
# a literal in this file is one more layer of encoding between the author and the byte.
$GUIL_OPEN = [char]0x00AB
$GUIL_CLOSE = [char]0x00BB
FreshFeedback
$r = RunCatch (CatchPayload 't-said-1' 'm-said-1' `
      "$fence`VAULT-FEEDBACK`ndecision: the owner said it - we build four menu states`n$fence" $true)
Check 'a decision claiming his words with no quotation is filed, with a note' `
      ($r.body -match 'we build four menu states' -and $r.body -match 'carrying no quotation') $r.body

FreshFeedback
$his = $GUIL_OPEN + [string][char]0x0434 + [char]0x0435 + [char]0x043B + [char]0x0430 + `
       [char]0x0435 + [char]0x043C + $GUIL_CLOSE
$r = RunCatch (CatchPayload 't-said-2' 'm-said-2' `
      "$fence`VAULT-FEEDBACK`ndecision: the owner said it - $his`n$fence" $true)
# AND THE QUOTATION ITSELF REACHES THE FILE, asserted here rather than assumed. This is the first
# case in this file to carry a non-ASCII byte at all, and the delivery it proved broken was the
# harness's own - so the case pins the repair as much as the hook.
Check 'and the same mark carrying the quotation draws no note' `
      ($r.body -match 'the owner said it' -and $r.body -notmatch 'carrying no quotation' `
       -and $r.body.Contains($GUIL_OPEN)) $r.body

# THE SHAPE IS DECLARED AT THE HEAD, NOT MENTIONED ANYWHERE IN THE RECORD. This case exists
# because the guard's FIRST live encounter was a false positive: a record opening
# `decision: the owner selected it` and going on to DISCUSS the phrase `the owner said it` was
# flagged as an unquoted claim. A record that talks about the shape is not making it.
FreshFeedback
$r = RunCatch (CatchPayload 't-said-4' 'm-said-4' `
      ("$fence`VAULT-FEEDBACK`ndecision: the owner selected it - the note on a mark carrying " +
       "the owner said it fires on the absent quotation`n$fence") $true)
Check 'a record that DISCUSSES the shape is not flagged as claiming it' `
      ($r.body -match 'fires on the absent quotation' -and $r.body -notmatch 'carrying no quotation') $r.body

# SCOPED TO `decision:`, and that is measured rather than tidy. The phrase appears legitimately in
# a `measure:` line ABOUT this very phenomenon - three such records sit in `log.md` today - so a
# test reading every kind would note all three and teach a reader to skip the note.
FreshFeedback
$r = RunCatch (CatchPayload 't-said-3' 'm-said-3' `
      "$fence`VAULT-FEEDBACK`nmeasure: 15 records carry the owner said it and no quotation`n$fence" $true)
Check 'a measure line ABOUT the phrase is not noted' `
      ($r.body -match '15 records carry' -and $r.body -notmatch 'carrying no quotation') $r.body

# A LEADING `- ` IS THE FORM THE RENDERED RULE SHOWS, and the parser could not read it. The rule
# renders into `CLAUDE.md` as a markdown list - `- miss: ...` - while the template inside
# `vault-feedback.md` shows the same line bare. Two renderings of one rule disagreeing, and the
# hook understood only the bare one: NINE blocks of one session were filed as `unknown:`, about
# forty lines under a word that is not a kind. The cause is one character - a dash is not
# whitespace, so `^\s*` never passed it, while `[A-Za-z-]+` swallowed it as the kind and then
# found no colon.
FreshFeedback
$r = RunCatch (CatchPayload 't13' 'm13' "$fence`VAULT-FEEDBACK`n- miss: written as the rule renders it`n$fence" $true)
Check 'a line written with a leading dash is filed under its kind' `
      ($r.body -match 'miss: written as the rule renders it' -and $r.body -notmatch 'unknown:') $r.body

# ONE ENTRY PER LINE, NOT PER FENCE. The rendered rule shows four kinds in one block; the catcher
# read the FIRST line's kind and applied it to the whole. A session that speaks a miss and a
# decision in one turn had both filed as a miss - and the kind is the one thing this channel
# exists to carry, so a block that flattens it hands the librarian nothing to sort by.
FreshFeedback
$r = RunCatch (CatchPayload 't14' 'm14' "$fence`VAULT-FEEDBACK`n- miss: the first thing`n- decision: the second thing`n$fence" $true)
# ANCHORED AT THE LINE START AND NOT AT ITS END. The file is written with platform newlines, so a
# `(?m)$` sits after the `\r` and never matches the last word of a line - a first draft of this
# case read MISSED for that and for nothing else, against a mechanism that was already right.
$items = ([regex]::Matches($r.body, '(?m)^- ')).Count
Check 'a block of two kinds files two entries under their own kinds' `
      ($items -eq 2 -and $r.body -match '(?m)^- miss: the first thing' -and $r.body -match '(?m)^- decision: the second thing') ("items: $items`n" + $r.body)

# AND AN INDENTED LINE IS A CONTINUATION EVEN WHEN IT LOOKS LIKE A KIND. Splitting on any `word:`
# anywhere would break an entry whose second line opens with one - and a `miss:` is obliged to say
# WHERE it surfaced, which is exactly where such a line goes. So the test is the indent and never
# the word: a new entry starts at column zero, optionally behind a list dash, and nothing else does.
FreshFeedback
$r = RunCatch (CatchPayload 't15' 'm15' "$fence`VAULT-FEEDBACK`n- miss: the thing that broke`n  note: where it surfaced`n$fence" $true)
$items = ([regex]::Matches($r.body, '(?m)^- ')).Count
Check 'an indented line that looks like a kind stays a continuation' `
      ($items -eq 1 -and $r.body -match 'note: where it surfaced') ("items: $items`n" + $r.body)

# EXIT 0 ON EVERY PATH INCLUDING ITS OWN FAILURE. This hook watches the turn's own words; one that
# can break the turn it observes is worse than no hook at all.
FreshFeedback
$r = RunCatch 'this is not json at all'
Check 'a malformed payload exits 0 and files nothing' `
      ($r.code -eq 0 -and $r.body -notmatch '^- ') ("code $($r.code)`n" + $r.body)
$r = RunCatch (CatchPayload 't11' '' 'no message id here' $true)
Check 'a payload with no message id exits 0' ($r.code -eq 0) $r.out

FreshFeedback
$r = RunCatch (CatchPayload 't12' 'm12' 'prose with no fence anywhere' $true)
Check 'a message with no block leaves the file untouched' ($r.body -notmatch '^- ') $r.body

Remove-Item -Recurse -Force $catchSdd -ErrorAction SilentlyContinue

# ---------------------------------------------------- the smoke gate, added 2026-08-26
#
# THREE HOOKS AND ONE LEDGER. The reminder asks for a run when /retro starts; the recorder turns a
# returned `make smoke` into a row; the refusal reads the rows and closes /handoff. Only the last
# refuses, and it is deliberately NOT registered yet - the cases below exercise the file directly,
# which proves its logic and proves nothing about whether the harness would fire it.
#
# THE REFUSAL TEXT IS ASSERTED ON THE COMMAND STRING AND NOT ON THE ANNOUNCEMENT. This suite has
# already shipped the other shape: the lock's refusal case was green while the refusal named
# `ash scripts/vault-check.sh`, because it pinned the sentence and not the thing the caller has to
# run. A condition the caller cannot run is not a condition that was named.
$remindHook  = Join-Path $sandbox '.claude/hooks/remind-the-smoke.ps1'
$recordHook  = Join-Path $sandbox '.claude/hooks/record-the-smoke.ps1'
$handoffHook = Join-Path $sandbox '.claude/hooks/gate-the-handoff.ps1'

function SkillPayload([string] $skill, [string] $session, [string] $tool) {
    if (-not $tool) { $tool = 'Skill' }
    return (@{
        tool_name       = $tool
        session_id      = $session
        permission_mode = 'default'
        tool_input      = @{ skill = $skill }
    } | ConvertTo-Json -Compress)
}
function BashPayload([string] $command, [string] $printed, [string] $session) {
    return (@{
        tool_name       = 'Bash'
        session_id      = $session
        permission_mode = 'default'
        tool_input      = @{ command = $command }
        tool_response   = @{ stdout = $printed }
    } | ConvertTo-Json -Compress)
}
function RunSmokeHook([string] $json, [string] $hookPath) {
    $out = $json | & powershell -NoProfile -ExecutionPolicy Bypass -File $hookPath 2>&1 | Out-String
    return @{ out = $out; code = $LASTEXITCODE }
}
function LedgerText { (Get-Content -LiteralPath $env:JOBHUNT_PRETASK_LEDGER -ErrorAction SilentlyContinue) -join "`n" }
function AppendRow([string] $stamp, [string] $session, [string] $event, [string] $path) {
    [System.IO.File]::AppendAllText($env:JOBHUNT_PRETASK_LEDGER,
        ($stamp + "`t" + $session + "`t" + $event + "`tdefault`t-`t" + $path + "`n"),
        (New-Object System.Text.UTF8Encoding($false)))
}

# --- the reminder ---------------------------------------------------------------------------
$r = RunSmokeHook (SkillPayload 'retro' 'K1' '') $remindHook
Check 'the reminder names the command when the retro starts' `
      ($r.code -eq 0 -and $r.out -match 'make smoke') $r.out
Check 'the reminder says the run must be repeated last before handoff' `
      ($r.out -match 'last thing before /handoff') $r.out
Check 'the reminder says a red run refuses handoff' `
      ($r.out -match 'refuses while the last run is red') $r.out

# THE FEEDBACK DEMAND LEFT THIS HOOK ON 2026-08-29 AND THE CASE INVERTED WITH IT. It was written out
# here in full and again in `remind-the-feedback.ps1`, and one requirement in two texts is one
# repair landing on one of them. This half now asserts the ABSENCE, and the presence is asserted
# against the hook that owns it, three cases below. Asserting only the new home would leave a copy
# quietly re-appearing here, which is how the duplication arrived the first time.
Check 'the smoke reminder no longer carries the feedback demand' `
      ($r.out -notmatch 'VAULT-FEEDBACK') $r.out

# AND IT DEMANDS THE FOREGROUND, which is the half that was wrong when this hook was written: it
# said "start it now and carry on talking", and a backgrounded run is recorded by nothing.
Check 'the reminder says to run smoke in the foreground' `
      ($r.out -match 'FOREGROUND') $r.out

$r = RunSmokeHook (SkillPayload 'superpowers:retro' 'K1' '') $remindHook
Check 'the reminder fires on a plugin-scoped retro' ($r.out -match 'make smoke') $r.out

$r = RunSmokeHook (SkillPayload 'ingest' 'K1' '') $remindHook
Check 'the reminder is silent on a skill that is not the retro' `
      ($r.code -eq 0 -and $r.out -notmatch 'make smoke') $r.out

$r = RunSmokeHook (SkillPayload 'retro' 'K1' 'Bash') $remindHook
Check 'the reminder is silent when the tool is not Skill' `
      ($r.code -eq 0 -and $r.out -notmatch 'make smoke') $r.out

$r = RunSmokeHook 'this is not json at all' $remindHook
Check 'the reminder exits 0 on a malformed payload' ($r.code -eq 0) $r.out

# --- the feedback reminder ------------------------------------------------------------------
#
# THIS IS THE ONLY HOOK HERE THAT DECIDES WHETHER TO SPEAK, so the cases are about the counter and
# not about the text. The failure it addresses is a channel that goes quiet mid-conversation, and
# the two defences built before it fire unconditionally - which is why the interesting assertions
# below are the SILENT ones. A reminder that speaks on every prompt would pass a text-only suite and
# be furniture within three turns.
#
# WHAT IS NOT TESTED HERE AND CANNOT BE. No case can assert that a session ACTS on the message. The
# reading that would tell us whether this works is how often the hook speaks in a real session, and
# it is taken by running one.
Copy-Item (Join-Path $repo '.claude/hooks/remind-the-feedback.ps1') (Join-Path $sandbox '.claude/hooks')
$feedbackHook = Join-Path $sandbox '.claude/hooks/remind-the-feedback.ps1'
$silenceState = Join-Path $catchSdd '.feedback-silence'

function PromptPayload([string] $session) {
    return (@{
        session_id      = $session
        hook_event_name = 'UserPromptSubmit'
        prompt          = 'a prompt whose text this hook must not read'
    } | ConvertTo-Json -Compress)
}
function RunPrompt([string] $session) {
    $out = (PromptPayload $session) |
        & powershell -NoProfile -ExecutionPolicy Bypass -File $feedbackHook 2>&1 | Out-String
    return @{ out = $out; code = $LASTEXITCODE; spoke = ($out -match 'VAULT-FEEDBACK') }
}
function FreshSilence {
    FreshFeedback
    Remove-Item -LiteralPath $silenceState -Force -ErrorAction SilentlyContinue
}
function RunFeedbackSkill([string] $skill, [string] $tool) {
    $out = (SkillPayload $skill 'K9' $tool) |
        & powershell -NoProfile -ExecutionPolicy Bypass -File $feedbackHook 2>&1 | Out-String
    return @{ out = $out; code = $LASTEXITCODE; spoke = ($out -match 'VAULT-FEEDBACK') }
}

# THE RITUAL HALF, WHICH THIS HOOK TOOK OVER ON 2026-08-29. The demand used to live in prose at the
# head of `remind-the-smoke.ps1`; one requirement in two texts drifts, and the repair lands on one
# copy. The absence there is asserted above, beside that hook's own cases, and the presence here.
#
# IT IS NOT COUNTER-GATED AND THE CASE SAYS SO. The counter is about a session that has been
# drifting; a ritual that has just opened has no silence to count, so the very first invocation
# speaks. A case that only checked the text would pass on a hook that had inherited the counter here
# too and would then say nothing until the retro's third turn.
$rt = RunFeedbackSkill 'retro' ''
Check 'the feedback hook demands a block every turn of the retro' `
      ($rt.code -eq 0 -and $rt.spoke -and $rt.out -match 'every turn') $rt.out
Check 'the ritual half speaks on its first invocation and is not counter-gated' `
      ($rt.out -match 'EVERY TURN OF THIS RETRO') $rt.out
Check 'the ritual half answers the tool event and names it' `
      ($rt.out -match 'PostToolUse') $rt.out

$rt = RunFeedbackSkill 'superpowers:retro' ''
Check 'the ritual half fires on a plugin-scoped retro' ($rt.spoke) $rt.out

$rt = RunFeedbackSkill 'ingest' ''
Check 'the ritual half is silent on a skill that is not the retro' `
      ($rt.code -eq 0 -and -not $rt.spoke) $rt.out

$rt = RunFeedbackSkill 'retro' 'Bash'
Check 'the ritual half is silent when the tool is not Skill' `
      ($rt.code -eq 0 -and -not $rt.spoke) $rt.out

# THE THREE-PROMPT RHYTHM. Two silent, the third speaks. If the first prompt spoke, every session
# would open with a reminder about nothing.
FreshSilence
$p1 = RunPrompt 'S1'; $p2 = RunPrompt 'S1'; $p3 = RunPrompt 'S1'
Check 'the feedback reminder is silent on the first quiet prompt' (-not $p1.spoke) $p1.out
Check 'the feedback reminder is silent on the second quiet prompt' (-not $p2.spoke) $p2.out
Check 'the feedback reminder speaks on the third quiet prompt'    ($p3.spoke)      $p3.out

# AND IT RESETS AFTER SPEAKING, rather than speaking on every prompt from then on. The second shape
# is the furniture this design exists to avoid, and the two are one assignment apart in the writing.
$p4 = RunPrompt 'S1'; $p5 = RunPrompt 'S1'; $p6 = RunPrompt 'S1'
Check 'the feedback reminder goes quiet again after it has spoken' `
      ((-not $p4.spoke) -and (-not $p5.spoke)) ($p4.out + $p5.out)
Check 'the feedback reminder returns after three more quiet prompts' ($p6.spoke) $p6.out

# A FILED BLOCK IS THE SIGNAL, and it arrives as the feedback file's write time. This is the case
# that makes the hook conditional rather than a timer: a session that is using the channel must
# never hear from it.
FreshSilence
$null = RunPrompt 'S2'; $null = RunPrompt 'S2'
Start-Sleep -Milliseconds 20
WriteUtf8 $catchFile "# header`n`n- decision: a block was filed`n`n---`n"
$after = RunPrompt 'S2'
Check 'a filed block resets the count before the reminder speaks' (-not $after.spoke) $after.out

# A NEW SESSION DOES NOT INHERIT A QUIET RUN. Without this the first prompt of a fresh session
# speaks about a conversation that ended yesterday.
FreshSilence
$null = RunPrompt 'S3'; $null = RunPrompt 'S3'
$other = RunPrompt 'A-DIFFERENT-SESSION'
Check 'a new session does not inherit the previous quiet count' (-not $other.spoke) $other.out

# THE MESSAGE SAYS WHAT THE CONDITION WAS. A reminder that reads as a judgement on what the session
# just wrote invites arguing with it instead of acting on it.
FreshSilence
$null = RunPrompt 'S4'; $null = RunPrompt 'S4'; $spoke = RunPrompt 'S4'
Check 'the reminder says the channel was quiet and claims nothing more' `
      ($spoke.out -match 'QUIET FOR THREE' -and $spoke.out -match 'means nothing else') $spoke.out

# THE KIND IS THE POINT AND NOT THE CHANNEL. The measured failure was not silence - it was `measure:`
# and `miss:` lines filed freely while every ruling went unrecorded. A reminder saying only "file
# feedback" would have been obeyed on the day it failed.
Check 'the reminder names decision as the kind that goes missing' `
      ($spoke.out -match 'decision:') $spoke.out
Check 'the reminder names the three shapes a ruling takes' `
      ($spoke.out -match 'SAID' -and $spoke.out -match 'SELECTED' -and $spoke.out -match 'UNDERSTOOD') `
      $spoke.out
Check 'the reminder licenses a turn that genuinely recorded nothing' `
      ($spoke.out -match 'legitimate answer') $spoke.out

# IT NAMES ITS OWN EVENT IN THE OUTPUT. A hook that returns the wrong `hookEventName` is dropped
# silently by the harness, which looks exactly like a hook with nothing to say.
Check 'the reminder returns its own event name in the payload' `
      ($spoke.out -match 'UserPromptSubmit') $spoke.out

# WITH NO `.superpowers/sdd` THERE IS NO CHANNEL TO BE QUIET ABOUT. Speaking there would be a
# reminder about a file the repository does not have.
Remove-Item -Recurse -Force $catchSdd -ErrorAction SilentlyContinue
$noSdd = RunPrompt 'S5'
Check 'the reminder is silent when there is no feedback directory' `
      ($noSdd.code -eq 0 -and -not $noSdd.spoke) $noSdd.out

FreshSilence
$bad = 'this is not json at all' |
    & powershell -NoProfile -ExecutionPolicy Bypass -File $feedbackHook 2>&1 | Out-String
Check 'the feedback reminder exits 0 on a malformed payload' ($LASTEXITCODE -eq 0) $bad

# --- the reply-silence counter, which is two hooks and one number ------------------------------
#
# THE COUNTER LIVES IN THE CATCHER AND THE SENTENCE IN THE REMINDER, because a probe on 2026-08-29
# established that a `MessageDisplay` hook cannot return `additionalContext` to a session at all: it
# fired three times, confirmed by its own marker, and nothing reached the session. So the only party
# that can see the session's replies cannot speak, and the only one that can speak cannot see them.
#
# EACH HOOK WRITES ONLY ITS OWN FILE, and the cases are split the same way: the three below ask the
# catcher what it counted, and the four after them ask the reminder what it said about it.
$replyState = Join-Path $catchSdd '.reply-silence'
function ReplyCount {
    if (-not (Test-Path -LiteralPath $replyState)) { return -1 }
    $v = -1
    [void][int]::TryParse((Get-Content -Raw -LiteralPath $replyState).Trim(), [ref] $v)
    return $v
}
function SetReplies([int] $n) {
    [System.IO.File]::WriteAllText($replyState, ([string]$n + "`n"),
        (New-Object System.Text.UTF8Encoding($false)))
}

FreshFeedback
Remove-Item -LiteralPath $replyState -Force -ErrorAction SilentlyContinue
$null = RunCatch (CatchPayload 'tR1' 'mR1' 'a reply carrying no block at all' $true)
Check 'the catcher counts a reply that filed nothing' ((ReplyCount) -eq 1) ("count=" + (ReplyCount))

$null = RunCatch (CatchPayload 'tR2' 'mR2' 'a second reply carrying no block' $true)
Check 'the catcher keeps counting consecutive silent replies' ((ReplyCount) -eq 2) ("count=" + (ReplyCount))

# THE RESET IS THE FILED BLOCK AND NOT A TIMER. A session using the channel must never hear from
# this, which is the same property the prompt counter has and the reason either is bearable.
$null = RunCatch (CatchPayload 'tR3' 'mR3' "$fence`VAULT-FEEDBACK`nmiss: something worth filing`n$fence" $true)
Check 'a filed block puts the reply count back to zero' ((ReplyCount) -eq 0) ("count=" + (ReplyCount))

# AND THE REMINDER SIDE. The first prompt of a session only establishes where the count stood, so
# the speaking case is the second - otherwise a fresh session would open by reporting replies
# somebody else wrote, which is the case after these three.
FreshSilence
SetReplies 0
$null = RunPrompt 'R1'
SetReplies 5
$rr1 = RunPrompt 'R1'
Check 'the reminder speaks when five replies filed nothing' ($rr1.out -match 'REPLIES SINCE') $rr1.out

$rr2 = RunPrompt 'R1'
Check 'the reply half does not repeat while the count has not moved' `
      ($rr2.out -notmatch 'REPLIES SINCE') $rr2.out

SetReplies 10
$rr3 = RunPrompt 'R1'
Check 'the reply half returns after five more silent replies' ($rr3.out -match 'REPLIES SINCE') $rr3.out

FreshSilence
SetReplies 99
$rr4 = RunPrompt 'R2'
Check 'a new session does not speak about replies it did not write' `
      ($rr4.out -notmatch 'REPLIES SINCE') $rr4.out

# --- the recorder ---------------------------------------------------------------------------
#
# THE ROW MUST CARRY THE CODE AND NOT THE FACT OF A RUN. A row saying only that smoke happened
# cannot enforce the owner's rule that a RED run refuses /handoff, and the two are one keystroke
# apart in the writing.
FreshLedger 'smoke-green' | Out-Null
$null = RunSmokeHook (BashPayload 'make smoke' "== gate`nSMOKE-EXIT: 0 (ok)" 'K2') $recordHook
#    THE FUNCTION CALL IS PARENTHESISED AND THAT IS NOT STYLE. `LedgerText -match "x"` parses as
#    CALLING `LedgerText` with the arguments `-match` and `"x"`, so it returns a string, `Check`
#    refuses to bind a string to a boolean, and the case NEVER RUNS. Five cases here were written
#    that way and the suite reported `caught 169, missed 0` with all five absent from the count -
#    the total is not asserted anywhere, so a case that does not run is indistinguishable from one
#    that passed. Found by reading the raw output of `make smoke` rather than a grep of it.
Check 'the recorder files a green run as smoke:0' ((LedgerText) -match "`tsmoke:0`t") (LedgerText)

FreshLedger 'smoke-red' | Out-Null
$null = RunSmokeHook (BashPayload 'make smoke' "SMOKE-EXIT: 2 (FAILED)" 'K2') $recordHook
Check 'the recorder files a red run with its own code' ((LedgerText) -match "`tsmoke:2`t") (LedgerText)

FreshLedger 'smoke-suite' | Out-Null
$null = RunSmokeHook (BashPayload 'make suite' "SMOKE-EXIT: 0 (ok)`nSUITE-EXIT: 0 (ok)" 'K2') $recordHook
Check 'a suite run files a smoke row, because suite contains smoke' `
      ((LedgerText) -match "`tsmoke:0`t") (LedgerText)

# A run that was interrupted or killed prints no marker. Recording that as a pass would open the
# gate on a run that never finished, so nothing is recorded and the gate asks for one.
FreshLedger 'smoke-nomarker' | Out-Null
$null = RunSmokeHook (BashPayload 'make smoke' "== gate`n== style" 'K2') $recordHook
Check 'a run that printed no marker files no row' ((LedgerText) -notmatch 'smoke:') (LedgerText)

FreshLedger 'smoke-notmake' | Out-Null
$null = RunSmokeHook (BashPayload 'cat Makefile' "SMOKE-EXIT: 0 (ok)" 'K2') $recordHook
Check 'a command that is not a make run files no row' ((LedgerText) -notmatch 'smoke:') (LedgerText)

# THE CASE THAT WOULD HAVE CAUGHT THE THREE FALSE GREEN ROWS OF 2026-08-29, and it fails against the
# hook as it stood that day. The command test was `\bmake\b`, and a word boundary sits between
# `make` and a hyphen - so the SLUG of any vault page whose filename begins `make-` satisfied it,
# while the page's own prose supplied the marker. Two live pages document `SMOKE-EXIT:`, so reading
# either one wrote a green row for a run nobody made. Two of the three rows were written by a
# subagent holding no write tool, while it counted how often this fires.
#
# The case above does not reach it: `Makefile` is one word, so `\bmake\b` never matched it and that
# case passed before the change as well as after. A case that passes before the change tests
# nothing, and this one is here because that one does not.
FreshLedger 'smoke-page-named-make' | Out-Null
$null = RunSmokeHook (BashPayload `
    'cat job_hunt_ai_vault/wiki/concepts/make-is-the-entry-point-and-every-check-has-a-target-a-trigger-and-an-obligation.md' `
    "the target prints ``SMOKE-EXIT: 0`` at the end of a green run" 'K2') $recordHook
Check 'reading a page whose slug begins make- files no row' ((LedgerText) -notmatch 'smoke:') (LedgerText)

# A BACKGROUNDED RUN IS THE TRAP THE REMINDER USED TO SET. The call reports only that it started, so
# the marker cannot be there and no row is written - and left silent, the session finds that out
# when /handoff refuses, with no clue why. Prose in the reminder is not enough on its own: this
# repository moved the title rule out of the vault and into the gate on exactly that argument.
FreshLedger 'smoke-background' | Out-Null
$bg = (@{
    tool_name       = 'Bash'
    session_id      = 'K2'
    permission_mode = 'default'
    tool_input      = @{ command = 'make smoke'; run_in_background = $true }
    tool_response   = @{ task_id = 'abc123'; output_file = 'C:\tmp\abc123.output' }
} | ConvertTo-Json -Compress)
$r = RunSmokeHook $bg $recordHook
Check 'a backgrounded make smoke files no row' ((LedgerText) -notmatch 'smoke:') (LedgerText)
Check 'and the recorder says so instead of going quiet' `
      ($r.out -match 'BACKGROUND' -and $r.out -match 'foreground') $r.out
Check 'and it never refuses, because PostToolUse cannot' ($r.code -eq 0) $r.out

# --- the refusal ----------------------------------------------------------------------------
FreshLedger 'handoff-none' | Out-Null
AppendRow '2026-01-01T00:00:00' 'K3' 'session-start:startup' ''
$r = RunSmokeHook (SkillPayload 'handoff' 'K3' '') $handoffHook
Check 'handoff is refused when no smoke has run' `
      ($r.out -match '"permissionDecision":\s*"deny"') $r.out
Check 'that refusal names the command the caller must run' ($r.out -match 'make smoke') $r.out
Check 'that refusal says which of the three states this is' ($r.out -match 'No .make smoke. has run') $r.out

FreshLedger 'handoff-red' | Out-Null
AppendRow '2026-01-01T00:00:01' 'K3' 'smoke:2' 'make smoke'
$r = RunSmokeHook (SkillPayload 'handoff' 'K3' '') $handoffHook
Check 'handoff is refused on a red run' ($r.out -match '"permissionDecision":\s*"deny"') $r.out
Check 'a red refusal says what it returned and where to fix it' `
      ($r.out -match 'returned 2' -and $r.out -match 'retro') $r.out

FreshLedger 'handoff-green' | Out-Null
AppendRow '2026-01-01T00:00:02' 'K3' 'smoke:0' 'make smoke'
$r = RunSmokeHook (SkillPayload 'handoff' 'K3' '') $handoffHook
Check 'handoff opens on a green run with nothing written after it' `
      ($r.code -eq 0 -and $r.out -notmatch 'deny') $r.out

# THE LAST ROW DECIDES, NOT ANY ROW. The fix loop the owner described produces several runs in one
# session - red, fix, green - and a reader that took any green row would open the path on the first
# success of a session that ended red.
FreshLedger 'handoff-lastwins' | Out-Null
AppendRow '2026-01-01T00:00:03' 'K3' 'smoke:0' 'make smoke'
AppendRow '2026-01-01T00:00:04' 'K3' 'smoke:1' 'make smoke'
$r = RunSmokeHook (SkillPayload 'handoff' 'K3' '') $handoffHook
Check 'a later red run overrides an earlier green one' `
      ($r.out -match '"permissionDecision":\s*"deny"' -and $r.out -match 'returned 1') $r.out

FreshLedger 'handoff-reopened' | Out-Null
AppendRow '2026-01-01T00:00:05' 'K3' 'smoke:1' 'make smoke'
AppendRow '2026-01-01T00:00:06' 'K3' 'write'   'scripts/vault-check.sh'
AppendRow '2026-01-01T00:00:07' 'K3' 'smoke:0' 'make smoke'
$r = RunSmokeHook (SkillPayload 'handoff' 'K3' '') $handoffHook
Check 'a green run after a fix clears the writes that preceded it' `
      ($r.code -eq 0 -and $r.out -notmatch 'deny') $r.out

# THE STALE STATE IS THE ONE THE OWNER ADDED AFTER SEEING THE FIRST DESIGN. A green run says the
# tree was sound at that instant and nothing after it, and a librarian's writes count too.
FreshLedger 'handoff-stale' | Out-Null
AppendRow '2026-01-01T00:00:08' 'K3' 'smoke:0' 'make smoke'
AppendRow '2026-01-01T00:00:09' 'K3' 'write'   'scripts/vault-check.sh'
$r = RunSmokeHook (SkillPayload 'handoff' 'K3' '') $handoffHook
Check 'handoff is refused when a file was written after a green run' `
      ($r.out -match '"permissionDecision":\s*"deny"') $r.out
Check 'a stale refusal names the file and says to run it again' `
      ($r.out -match 'vault-check\.sh' -and $r.out -match 'make smoke') $r.out

# WHERE GIT CANNOT ANSWER, EVERY WRITE COUNTS. The sandbox is not a repository, so `check-ignore`
# fails here and the fallback is what this case pins: a gate that fails towards refusing costs a
# three-minute run, and one that fails towards opening costs the thing it guards.
FreshLedger 'handoff-nogit' | Out-Null
AppendRow '2026-01-01T00:00:10' 'K3' 'smoke:0' 'make smoke'
AppendRow '2026-01-01T00:00:11' 'K3' 'write'   '.superpowers/sdd/retro.md'
$r = RunSmokeHook (SkillPayload 'handoff' 'K3' '') $handoffHook
Check 'with no git to ask, an ignored-looking path still counts' `
      ($r.out -match '"permissionDecision":\s*"deny"') $r.out

# AND WHERE GIT CAN ANSWER, AN IGNORED PATH DOES NOT. Without this case the rule the owner ratified
# - a write counts only if git tracks it - is asserted by nothing, and /retro writing its own
# transit file would close the gate on every session for ever.
$gitOk = $false
try {
    & git -C $sandbox init --quiet 2>&1 | Out-Null
    WriteUtf8 (Join-Path $sandbox '.gitignore') ".superpowers/`n"
    $gitOk = (Test-Path -LiteralPath (Join-Path $sandbox '.git'))
} catch { }
if ($gitOk) {
    FreshLedger 'handoff-ignored' | Out-Null
    AppendRow '2026-01-01T00:00:12' 'K3' 'smoke:0' 'make smoke'
    AppendRow '2026-01-01T00:00:13' 'K3' 'write'   '.superpowers/sdd/retro.md'
    $r = RunSmokeHook (SkillPayload 'handoff' 'K3' '') $handoffHook
    Check 'a write to a git-ignored path leaves the path open' `
          ($r.code -eq 0 -and $r.out -notmatch 'deny') $r.out

    FreshLedger 'handoff-mixed' | Out-Null
    AppendRow '2026-01-01T00:00:14' 'K3' 'smoke:0' 'make smoke'
    AppendRow '2026-01-01T00:00:15' 'K3' 'write'   '.superpowers/sdd/retro.md'
    AppendRow '2026-01-01T00:00:16' 'K3' 'write'   'Makefile'
    $r = RunSmokeHook (SkillPayload 'handoff' 'K3' '') $handoffHook
    Check 'one tracked write among ignored ones still refuses' `
          ($r.out -match '"permissionDecision":\s*"deny"' -and $r.out -match 'Makefile') $r.out
} else {
    Check 'a write to a git-ignored path leaves the path open' $false `
          'git could not initialise a repository in the sandbox, so the ignore branch was not exercised'
}

$r = RunSmokeHook (SkillPayload 'ingest' 'K3' '') $handoffHook
Check 'the refusal is silent on a skill that is not the handoff' `
      ($r.code -eq 0 -and $r.out -notmatch 'deny') $r.out

$r = RunSmokeHook (SkillPayload 'handoff' '' '') $handoffHook
Check 'with no session identifier the gate speaks instead of refusing' `
      ($r.code -eq 0 -and $r.out -notmatch 'deny' -and $r.out -match 'DID NOT RUN') $r.out

Remove-Item -Recurse -Force (Join-Path $sandbox '.git') -ErrorAction SilentlyContinue

# ---------------------------------------------------- which hook refuses, and which only speaks
#
# THE LIST LIVES HERE AND NOT IN PROSE, on the owner's ruling of 2026-08-21. A `decisions/` page
# and `entities/session-hooks.md` both carried the sentence "no hook in this repository blocks",
# and it went false the day `lock-the-librarian.ps1` landed and stood for a further day. Nothing
# could contradict it: the claim ranges over every registration, and checking it meant opening
# seven scripts by hand. A list that is also a test cannot drift from what it describes.
#
# THE TEST A REFUSAL IS DECIDED BY, ratified the same day, replacing a rule the corpus attributed
# to the owner and he had never given: a hook may refuse when the condition is MEASURED rather than
# judged, when that measurement is RELIABLE AT THE POINT THE HOOK STANDS, and when the refusal SAYS
# HOW TO CLEAR IT. Where it cannot measure, it allows and says so aloud. Only the first of the
# three is mechanical, which is why this block asserts the disposition and not the reasoning.
#
# EVENT BEFORE JUDGEMENT. `PostToolUse` fires after the act and `SessionStart` injects context;
# neither has a way to deny, so neither is a candidate however good its case. That is asserted
# below rather than left as a thing everyone knows, because it is the half that bounds the
# question: three registrations can refuse, not five.
# ---------------------------------------------------------------- the rule server
#
# WHAT IS UNDER TEST IS THE MATCH AND THE SILENCES, not the wording of the note. The hook looks up
# every `current` page in `wiki/rules/` whose `governs:` names the file being written and hands it
# over; it says nothing for a file nothing governs, nothing for a write inside the vault, and
# nothing the second time in one session.
#
# THE SILENCE INSIDE `wiki/` IS THE CASE THAT MATTERS. It is what keeps the librarian from being
# handed a rule on every page of an ingest, and it is scoped by path because there is no documented
# way to exclude one subagent from a hook declared in `settings.json`. A regression there is
# invisible in use - it looks like a chatty hook, not like a broken guard - so it is asserted here.
$serveHook = Join-Path $sandbox '.claude/hooks/serve-the-rule.ps1'
$serveLedger = Join-Path $sandbox 'serve-ledger.tsv'
New-Item -ItemType Directory -Force -Path (Join-Path $vault 'wiki/rules') | Out-Null
$serveTarget = Join-Path $sandbox '.claude/templates/handoff.md'
WriteUtf8 (Join-Path $vault 'wiki/rules/a-rule-the-server-must-find.md') @"
---
title: "A rule the server must find"
type: rule
status: current
governs: .claude/templates/handoff.md
render: region
basis: human
sprint: S3
created: 2026-08-30
sources: ["scripts/hook-selftest.ps1"]
tags: [harness, vault]
---

# A rule the server must find

Planted by the selftest.
"@
WriteUtf8 (Join-Path $vault 'wiki/rules/a-retired-rule-the-server-must-skip.md') @"
---
title: "A retired rule the server must skip"
type: rule
status: deprecated
governs: .claude/templates/handoff.md
render: region
basis: human
sprint: S3
created: 2026-08-30
sources: ["scripts/hook-selftest.ps1"]
tags: [harness, vault]
---

# A retired rule the server must skip

Planted by the selftest. It is not current, so its text is what WAS true and must not be handed
over as though it still were.
"@

# THE LOOKUP HALF, ADDED 2026-08-31. A `render: authority` page carries a slug and no destination,
# so nothing about it can be tested through the `governs:` fixture above: it is found by the
# `authority:` of the file being READ, and the write path is silent exactly where such a slug
# exists. Both a rule and a page to touch are needed, and they have to be real files, because this
# half opens the touched file to read its head.
New-Item -ItemType Directory -Force -Path (Join-Path $vault 'wiki/concepts') | Out-Null
WriteUtf8 (Join-Path $vault 'wiki/rules/a-lookup-rule-the-server-must-find.md') @"
---
title: "A lookup rule the server must find"
type: rule
status: current
authority: selftest-served-slug
render: authority
basis: human
sprint: S3
created: 2026-08-31
sources: ["scripts/hook-selftest.ps1"]
tags: [harness, vault]
---

# A lookup rule the server must find

Planted by the selftest. It carries no ``governs:`` and no marked slice, which is what the mode is.
"@
WriteUtf8 (Join-Path $vault 'wiki/rules/a-retired-lookup-rule-the-server-must-skip.md') @"
---
title: "A retired lookup rule the server must skip"
type: rule
status: deprecated
authority: selftest-served-slug
render: authority
basis: human
sprint: S3
created: 2026-08-31
sources: ["scripts/hook-selftest.ps1"]
tags: [harness, vault]
---

# A retired lookup rule the server must skip

Planted by the selftest. Two rules of one type may share a slug while only one of them is current.
"@
WriteUtf8 (Join-Path $vault 'wiki/concepts/a-page-the-lookup-must-match.md') @"
---
title: "A page the lookup must match"
type: concept
status: current
authority: selftest-served-slug
basis: human
sprint: S3
created: 2026-08-31
sources: ["scripts/hook-selftest.ps1"]
tags: [harness, vault]
---

# A page the lookup must match
"@
WriteUtf8 (Join-Path $vault 'wiki/concepts/a-page-no-rule-answers-for.md') @"
---
title: "A page no rule answers for"
type: concept
status: current
authority: selftest-unanswered-slug
basis: human
sprint: S3
created: 2026-08-31
sources: ["scripts/hook-selftest.ps1"]
tags: [harness, vault]
---

# A page no rule answers for
"@
$serveMatched   = Join-Path $vault 'wiki/concepts/a-page-the-lookup-must-match.md'
$serveUnmatched = Join-Path $vault 'wiki/concepts/a-page-no-rule-answers-for.md'

# `tool_name` DEFAULTS TO Edit so that every case written before the mode-aware silence keeps
# meaning what it meant. The hook reads the field to tell a read from a write, and an absent field
# has to land on the stricter side - a payload that lost its tool name must not start speaking
# inside the vault.
function RunServe([string] $path, [string] $session, [string] $tool = 'Edit') {
    $json = @{ session_id = $session; tool_name = $tool; tool_input = @{ file_path = $path } } |
        ConvertTo-Json -Depth 4
    $env:JOBHUNT_PRETASK_LEDGER = $serveLedger
    $out = $json | & powershell -NoProfile -ExecutionPolicy Bypass -File $serveHook 2>&1 | Out-String
    $code = $LASTEXITCODE
    Remove-Item Env:\JOBHUNT_PRETASK_LEDGER -ErrorAction SilentlyContinue
    return @{ out = $out; code = $code }
}

if (Test-Path -LiteralPath $serveLedger) { Remove-Item -LiteralPath $serveLedger -Force }
$r = RunServe $serveTarget 'serve-1'
Check "the rule server finds the governing rule" `
      ($r.code -eq 0 -and $r.out -match 'A rule the server must find') $r.out
Check "the rule server skips a retired rule" `
      ($r.out -notmatch 'A retired rule the server must skip') $r.out

$r = RunServe $serveTarget 'serve-1'
Check "the rule server says it once per session" `
      ($r.code -eq 0 -and $r.out -notmatch 'A rule the server must find') $r.out

$r = RunServe $serveTarget 'serve-2'
Check "a new session hears it again" `
      ($r.out -match 'A rule the server must find') $r.out

$r = RunServe (Join-Path $vault 'wiki/decisions/anything.md') 'serve-3'
Check "the rule server is silent inside the vault" ($r.out.Trim() -eq '') $r.out

$r = RunServe (Join-Path $sandbox 'scripts/vault-check.sh') 'serve-4'
Check "the rule server is silent on an ungoverned file" ($r.out.Trim() -eq '') $r.out

$r = RunServe $serveMatched 'serve-5' 'Read'
Check "the rule server serves a lookup rule on a read of the page carrying its slug" `
      ($r.code -eq 0 -and $r.out -match 'A lookup rule the server must find') $r.out
Check "a retired lookup rule is not served" `
      ($r.out -notmatch 'A retired lookup rule the server must skip') $r.out
# THE WORDING IS PART OF THE CONTRACT AND NOT DECORATION. The `governs:` note tells a reader the
# text is rendered here and that editing the region alone reads as drift; both halves of that are
# FALSE of a rule written into no file, and one wording for both delivery modes would have the
# hook assert something untrue about the rule it just handed over.
Check "a lookup rule is not described as a rendered region" `
      ($r.out -notmatch 'rendered here from the vault') $r.out

$r = RunServe $serveMatched 'serve-6'
Check "a write to the same page stays silent" ($r.out.Trim() -eq '') $r.out

$r = RunServe $serveUnmatched 'serve-7' 'Read'
Check "a read of a page no rule answers for is silent" ($r.out.Trim() -eq '') $r.out

$expectedHooks = @(
    @{ Event = 'SessionStart'; Matcher = 'startup|resume|clear|compact'; Script = 'session-brief.ps1';      Refuses = $false },
    @{ Event = 'PreToolUse';   Matcher = 'Edit|Write';                   Script = 'ask-the-vault.ps1';      Refuses = $false },
    #   ADDED 2026-08-30. It hands over the rule that governs the file being written, looked up in
    #   `wiki/rules/` at the moment of the write. It speaks and never refuses: an edit is
    #   reversible, and a rule merely governing a file is not a reason to stop it.
    @{ Event = 'PreToolUse';   Matcher = 'Edit|Write';                   Script = 'serve-the-rule.ps1';     Refuses = $false },
    #   REGISTERED ON `Read` AS WELL, 2026-08-31, and this is the registration the `authority:`
    #   half needs to fire at all: the write path is silent inside `wiki/`, which is exactly where
    #   a slug exists. The measurement its deferral demanded was taken first, across every
    #   transcript this project has - Bash 5088, Edit 1102, Read 490, Write 392 - so `Read` is a
    #   third of the write path here and not the multiplier the deferral feared.
    @{ Event = 'PreToolUse';   Matcher = 'Read';                         Script = 'serve-the-rule.ps1';     Refuses = $false },
    @{ Event = 'PreToolUse';   Matcher = 'Agent|Task';                   Script = 'lock-the-librarian.ps1'; Refuses = $true  },
    @{ Event = 'PreToolUse';   Matcher = 'ExitPlanMode';                 Script = 'check-the-plan.ps1';     Refuses = $false },
    @{ Event = 'PostToolUse';  Matcher = 'ExitPlanMode';                 Script = 'check-the-plan.ps1';     Refuses = $false },
    @{ Event = 'PostToolUse';  Matcher = 'Write|Edit';                   Script = 'check-the-journal.ps1';  Refuses = $false },
    #   ADDED 2026-08-22. It records and cannot refuse: `PostToolUse` fires after the act, so the
    #   disposition is fixed by the event and is not a policy choice about this script.
    @{ Event = 'PostToolUse';  Matcher = 'Agent|Task';                   Script = 'record-the-dispatch.ps1'; Refuses = $false },
    #   ADDED 2026-08-24, and it is the instrument for the one rule among the six that had none:
    #   plan mode disarms the party obliged to write a feedback line, so the line is spoken in the
    #   reply and this hook files it. THE MATCHER IS EMPTY BECAUSE THE EVENT TAKES NONE - the
    #   census reads `$m.matcher` and formats a missing one as the empty string, so the expected
    #   key must be empty too rather than absent. It speaks: `MessageDisplay` is display-only and
    #   a refusal is possible on `PreToolUse` alone, so the disposition is fixed by the event.
    @{ Event = 'MessageDisplay'; Matcher = '';                           Script = 'catch-the-feedback.ps1'; Refuses = $false },
    #   ADDED 2026-08-26, the two halves of the smoke gate that cannot refuse. The reminder fires
    #   when /retro starts and asks for a run; the recorder turns a returned `make smoke` into the
    #   row the refusal later reads. Both are `PostToolUse`, so neither could deny if it wanted to.
    #
    @{ Event = 'PostToolUse';  Matcher = 'Skill';                       Script = 'remind-the-smoke.ps1';   Refuses = $false },
    @{ Event = 'PostToolUse';  Matcher = 'Bash';                        Script = 'record-the-smoke.ps1';   Refuses = $false },
    #   ADDED 2026-08-28. It was built first on `PostToolUse` with a `Skill` matcher, firing once
    #   when /grill-me opened, and the owner replaced it the same day: what must not be lost is the
    #   ruling HE writes, so the reminder belongs on HIS prompt. `UserPromptSubmit` TAKES NO
    #   MATCHER, so the expected key here carries the empty string for the same reason the
    #   `MessageDisplay` row above does - the census formats a missing matcher as empty.
    #
    #   IT IS THE FIRST HOOK IN THIS REPOSITORY THAT DECIDES WHETHER TO SPEAK. Every other one
    #   either always speaks or speaks on a condition in the payload; this one carries a counter and
    #   stays silent while the channel is being used, because the two defences built before it fire
    #   unconditionally and were read three times each before becoming furniture.
    @{ Event = 'UserPromptSubmit'; Matcher = '';                        Script = 'remind-the-feedback.ps1'; Refuses = $false },
    #   AND A SECOND REGISTRATION OF THE SAME FILE, 2026-08-29. It took over the `VAULT-FEEDBACK`
    #   demand that `remind-the-smoke.ps1` carried in prose, so one requirement stopped being two
    #   texts that drift. The precedent for one file on two events is `check-the-plan.ps1` above.
    #
    #   IT IS THE SHAPE THE OWNER WITHDREW ON 2026-08-28, RESTORED FOR A DIFFERENT PURPOSE AND WITH
    #   HIS RULING. What he corrected then was the reminder about HIS rulings firing on a skill
    #   instead of on his prompt, and that half is untouched: the prompt registration above still
    #   owns the counter. This arm speaks only the ritual's own obligation, at the ritual's door.
    #
    #   THE HOOK REGISTER KEYS ON THE FILE, so one script with two registrations still produces one
    #   row there and its disposition is asked once. Both events are `PostToolUse` or later, so
    #   neither could deny even if the file wanted to.
    @{ Event = 'PostToolUse';  Matcher = 'Skill';                       Script = 'remind-the-feedback.ps1'; Refuses = $false },
    #   THE SECOND REFUSER, AND IT ARRIVED AS THIS BLOCK INTENDED IT TO. The plan that built it said
    #   to leave it unregistered until a restart had shown the reminder fire on a live /retro. The
    #   case below that reads every hook script and asks whether it is registered or dot-sourced
    #   refused that state, and it refused it BY DESIGN: it is a property rather than an exemption
    #   list, argued in its own comment as the thing that cannot go stale, so there was nowhere to
    #   write the exception down. A hook left on disk and wired to nothing is inert and looks
    #   exactly like one with nothing to say - which is the whole class it exists to catch.
    #
    #   IT WAS ARMED THE MOMENT IT WAS REGISTERED, AND THE SENTENCE THAT STOOD HERE SAID OTHERWISE.
    #   "Hooks are read at session start, so registering does not arm it this session" was written
    #   here, in the gate's own header, and in a commit message. On the same day the sibling
    #   reminder - registered under a `Skill` matcher minutes earlier - fired on that session's own
    #   `/retro`. So a settings change takes effect without a restart here, the acceptance the plan
    #   was waiting for passed live, and the exposure the plan tried to postpone by one session was
    #   never postponable. The cases below are what the gate's logic actually rests on.
    @{ Event = 'PreToolUse';   Matcher = 'Skill';                       Script = 'gate-the-handoff.ps1';   Refuses = $true  }
)

$actualHooks = @()
try {
    $cfg = (Get-Content $settings -Raw) | ConvertFrom-Json
    foreach ($ev in $cfg.hooks.PSObject.Properties) {
        foreach ($m in $ev.Value) {
            foreach ($h in $m.hooks) {
                #    NO REGEX FOR THE SEPARATOR. A character class holding a backslash is one
                #    escaping mistake away from an invalid pattern, and PowerShell reports that
                #    as a caught exception rather than a bad match - so the census read `could
                #    not read` and every registration looked absent. The platform already has
                #    a parser for this and it takes both separators.
                $cmd  = $h.command -replace '"', ''
                $leaf = [System.IO.Path]::GetFileName($cmd.Trim())
                $actualHooks += ("{0}|{1}|{2}" -f $ev.Name, $m.matcher, $leaf)
            }
        }
    }
} catch { $actualHooks += "could not read: $_" }

$expectedKeys = $expectedHooks | ForEach-Object { "{0}|{1}|{2}" -f $_.Event, $_.Matcher, $_.Script }
$missing = $expectedKeys | Where-Object { $actualHooks -notcontains $_ }
$extra   = $actualHooks  | Where-Object { $expectedKeys -notcontains $_ }

# BOTH DIRECTIONS. A registration removed and a registration added are different failures and this
# repository has met the first: the `InstructionsLoaded` block was deleted and its script stayed on
# disk. Listing only what is expected would go green on a hook nobody declared.
Check 'the registered hook set is exactly the one this list names' `
      ($missing.Count -eq 0 -and $extra.Count -eq 0) `
      ("not registered: " + ($missing -join ', ') + "; not listed: " + ($extra -join ', '))

# A REFUSAL IS A `permissionDecision` OF `deny` AND NOTHING ELSE, so the disposition is read off
# the script rather than asserted about it. The matcher is deliberately literal: a hook that
# merely mentions the word in a comment has not got a branch that denies.
$wrongDisposition = @()
foreach ($e in $expectedHooks) {
    $path = Join-Path $repo (".claude/hooks/" + $e.Script)
    if (-not (Test-Path -LiteralPath $path)) { $wrongDisposition += ($e.Script + " is registered and absent"); continue }
    $text = Get-Content $path -Raw
    $denies = $text -match "permissionDecision\s*=\s*'deny'"
    if ($denies -ne $e.Refuses) {
        if ($denies) { $wrongDisposition += ($e.Script + " denies and is listed as speaking") }
        else         { $wrongDisposition += ($e.Script + " is listed as refusing and has no deny branch") }
    }
}
Check 'every hook refuses or speaks exactly as this list says' ($wrongDisposition.Count -eq 0) `
      ($wrongDisposition -join '; ')

# THE ONE REFUSER, named rather than counted. `bash scripts/vault-check.sh | grep -c` would answer
# the same question and answer it about whatever the corpus happens to hold; this asks about the
# tree in front of it and says which file, so a second refuser arriving is a failure with a name.
#    WRAPPED IN @() BECAUSE ONE RESULT IS NOT A LIST. `Sort-Object -Unique` returns the bare
#    string when it has one item, and `$refusers[0]` on a string is its first CHARACTER - so
#    this case failed while reporting the right answer beside itself, which is the worst
#    shape a test can take.
$refusers = @($expectedHooks | Where-Object { $_.Refuses } | ForEach-Object { $_.Script } | Sort-Object -Unique)
$expectedRefusers = @('gate-the-handoff.ps1', 'lock-the-librarian.ps1')
# THE SET IS NAMED, NOT COUNTED, and it grew on 2026-08-26 from one to two. This case read "exactly
# one hook refuses" until then, which is what made the second one arrive as a failure with a name
# rather than as a silent widening. Both guard something that cannot be undone once it has happened:
# the lock guards an ingest over a broken corpus, and the handoff gate guards a journal already in
# the librarian's hands. A third arriving is a conversation with the owner, and this line is what
# starts it.
Check 'exactly the named hooks refuse, and no others' `
      (-not (Compare-Object $refusers $expectedRefusers)) `
      ("refusers: " + ($refusers -join ', '))

# THE EVENT BOUNDS THE QUESTION. `PostToolUse` runs after the tool has run and `SessionStart`
# injects context into a session that has already begun - an exit code from either changes nothing
# that has not already happened. A refusal listed on one of them would be a design error rather
# than a policy disagreement, and it is caught here before anybody argues the policy.
$deniesOnADeafEvent = $expectedHooks | Where-Object { $_.Refuses -and $_.Event -ne 'PreToolUse' } |
                      ForEach-Object { $_.Event + " -> " + $_.Script }
Check 'no refusal is listed on an event that cannot deny' ($deniesOnADeafEvent.Count -eq 0) `
      ("listed on a deaf event: " + ($deniesOnADeafEvent -join ', '))

Remove-Item -Recurse -Force $sandbox -ErrorAction SilentlyContinue

# --- the suite's own argument contract ---
#
# THESE CASES LIVE HERE BECAUSE `vault-check-selftest.sh` CANNOT TEST ITSELF WITHOUT RUNNING ITSELF,
# and a whole run of it is thirty-four minutes against this file's one. The flag they pin is the one
# `make smoke ONLY=<pattern>` depends on, so it is checked by a suite that smoke actually runs.
#
# NOTHING BELOW REACHES THE WORKING VAULT except the last case. `--list` and the refusal both answer
# from a sweep of the suite's own source and return before it builds a sandbox or opens a page, so
# the rule that a selftest works in its own fixture is untouched by them. The last case lets a run
# proceed and pays for that suite's own throwaway copy, which is that suite's normal behaviour and
# not this one reaching into the corpus.
#
# BASH IS DERIVED FROM GIT AND NEVER TAKEN FROM PATH. On this machine `bash` on PATH is the WSL shim
# in WindowsApps, which would run the suite under a different operating system entirely. `Find-Bash`
# is the one implementation two hooks already share, and this is its third caller.
. (Join-Path $repo '.claude/hooks/vault-path.ps1')
$suiteBash = Find-Bash
$suitePath = (Join-Path $repo 'scripts/vault-check-selftest.sh') -replace '\\', '/'

function RunSuite([string[]] $suiteArgs) {
    $all = @($suitePath) + $suiteArgs
    $text = (& $suiteBash @all | Out-String)
    return @{ out = $text; code = $LASTEXITCODE }
}

if ($null -eq $suiteBash) {
    Check 'a bash was found to run the suite with' $false `
          'Find-Bash returned nothing - git is absent from PATH, or is not a Git-for-Windows install'
} else {
    $list = RunSuite @('--list')
    Check 'the suite lists both its cases and its sections' `
          ($list.code -eq 0 -and $list.out -match 'case\(s\)' -and $list.out -match 'section\(s\)') `
          $list.out

    # THE SWEEP USED TO COUNT THE PARAGRAPH THAT EXPLAINS IT. `--list` finds an inline case by the
    # literal `report "..."`, and the comment above that sweep quotes exactly that to say what it
    # looks for - so a case named `...` was in every listing from the day it was written, and the
    # count was one too high with nothing to compare it against.
    Check 'the case list does not count the comment that explains it' `
          ($list.out -notmatch '\(inline\) \.\.\.') $list.out

    Check 'the section list names a section the cases are grouped under' `
          ($list.out -match '\(section\) --- the archive script ---') $list.out

    # THE DEFECT THIS PAIR EXISTS FOR. Until 2026-08-28 an `--only` matching nothing printed
    # `caught 1, missed 0` and exited 0 - the one being the baseline copy, which no filter ever
    # saw - so `make smoke ONLY=<typo>` read as a clean slice that had run nothing at all.
    $miss = RunSuite @('--only', 'archive|units')
    Check 'a substring matching no case is refused with the usage code' `
          ($miss.code -eq 2) ("exit=" + $miss.code + "`n" + $miss.out)
    Check 'the refusal says the substring selected no case' `
          ($miss.out -match 'selects no case') $miss.out
    Check 'the refusal says the matcher is a substring and not a pattern' `
          ($miss.out -match 'SUBSTRING') $miss.out

    $noValue = RunSuite @('--only')
    Check 'an --only with no substring after it is refused' `
          ($noValue.code -eq 2 -and $noValue.out -match 'needs a substring') `
          ("exit=" + $noValue.code + "`n" + $noValue.out)

    $unknown = RunSuite @('--nonsense')
    Check 'an unknown argument to the suite is refused' `
          ($unknown.code -eq 2 -and $unknown.out -match 'unknown argument') `
          ("exit=" + $unknown.code + "`n" + $unknown.out)

    # THE OTHER HALF OF THE PAIR, AND IT IS WHAT COSTS. Without it "refuses everything" passes every
    # case above. The name is taken from the listing rather than written here, so renaming a case
    # cannot leave this asserting about a case that no longer exists.
    $firstCase = ($list.out -split "`r?`n" |
                  Where-Object { $_ -match '^  [^ (]' } |
                  Select-Object -First 1)
    if ($null -eq $firstCase) {
        Check 'a listed case name was available to select with' $false $list.out
    } else {
        $one = RunSuite @('--only', $firstCase.Trim())
        Check 'a listed case name is selected rather than refused' `
              ($one.code -eq 0 -and $one.out -match 'FILTERED by' -and $one.out -notmatch 'selects no case') `
              ("selected: " + $firstCase.Trim() + "`nexit=" + $one.code + "`n" + $one.out)
        Check 'the baseline copy is not counted as a case that passed' `
              ($one.out -match 'BASELINE' -and $one.out -match 'caught 1,') $one.out
    }
}

# A CASE THAT DID NOT RUN IS NOT A CASE THAT PASSED, AND NOTHING HERE COULD TELL THE TWO APART.
# `Check` takes a [bool]; hand it a string and PowerShell refuses to bind, the case never executes,
# and neither `$pass` nor `$fail` moves. The line at the bottom then reports a smaller number with
# perfect confidence. It happened on 2026-08-26: five cases written as `LedgerText -match "x"` -
# which parses as CALLING that function with two arguments rather than comparing its result -
# vanished from a run that said `caught 169, missed 0`, and were found only by reading the raw
# output instead of grepping it.
#
# THE GUARD IS NOT A COUNT. Asserting an expected total would be a number in the file that every
# new case has to update, which is the drifting-list shape this project repairs by deletion. This
# asks the platform instead: did any argument fail to bind. Errors swallowed by the `try/catch`
# blocks above carry different identifiers and do not reach it.
$bindingFailures = @($Error | Where-Object { $_.FullyQualifiedErrorId -like 'ParameterArgumentTransformationError*' })
Check 'every Check call bound its arguments and therefore ran' ($bindingFailures.Count -eq 0) `
      (($bindingFailures | ForEach-Object { $_.InvocationInfo.Line.Trim() }) -join "`n")

""
"HOOK-SELFTEST: caught $pass, missed $fail"
if ($fail -gt 0) { exit 1 } else { exit 0 }
