# Where the vault is - one implementation, dot-sourced by both hooks.
#
# It was two, and they could disagree: one used Get-ChildItem, which skips hidden directories
# and returns them sorted, the other `find | head -1`, which does neither. With two candidate
# directories present they picked different vaults, and the hook would have printed a brief
# from one while every script in the repository read the other. One reader, one answer.
#
# The vault is the top-level directory holding a `wiki/`. Its name is what Obsidian displays,
# so it is the owner's to change - it has changed four times - and nothing may hard-code it.
# Dot-directories are excluded and the rest are sorted, so the answer is the same on every
# machine and matches `scripts/vault-check.sh`.

function Find-Vault {
    param([string] $Root)

    Get-ChildItem -LiteralPath $Root -Directory -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -notlike '.*' } |
        Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName 'wiki') } |
        Sort-Object Name |
        Select-Object -First 1
}

# A usable bash is DERIVED from where git is, never hard-coded. `git` resolves to
# ...\Git\mingw64\bin\git.exe on this machine and to ...\Git\cmd\git.exe on a default install, and
# bash sits at ...\Git\bin\bash.exe in both - so walk up until a `bin\bash.exe` appears rather
# than counting levels, which is the difference between the two layouts.
#
# IT LIVES HERE BECAUSE IT HAS TWO CALLERS NOW (2026-08-20). It was written inside
# check-the-journal.ps1, and the librarian lock needed the same answer. Copying it would have made
# a second definition of one discovery rule - the exact shape this repository already carries four
# copies of for the VAULT path, and the reason that is recorded as a defect rather than a style.
# Two rules that can disagree are worse than either of them.
function Find-Bash {
    $git = Get-Command git -ErrorAction SilentlyContinue
    if ($null -eq $git) { return $null }
    $dir = Split-Path $git.Source
    for ($i = 0; $i -lt 5 -and $dir; $i++) {
        $candidate = Join-Path $dir 'bin\bash.exe'
        if (Test-Path -LiteralPath $candidate) { return $candidate }
        $dir = Split-Path $dir
    }
    return $null
}
