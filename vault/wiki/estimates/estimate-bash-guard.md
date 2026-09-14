---
type: estimate
kind: QA
status: passed
target: rule-bash-guard
origin: raw/2026-09-14/1029/ledger.md#case-127
sprint: migration
created: 2026-09-14
tags: [hooks, harness]
---

## Context

A lesson the agent has to remember is not a rule. A `PreToolUse Bash` hook that refuses a command whose heredoc body carries a backslash escape — or refuses a heredoc that writes a file at all, pointing at Write and Edit — makes the trap impossible instead of remembered. (Case 120 as it stands.)

## Criterion

### case 127

When:
The agent calls the `Bash` tool and the hook `uv run guppi bashguard` runs on `PreToolUse`.

Then:
The hook reads `tool_input.command`, finds every heredoc (`<<` or `<<-`, the marker quoted or not) and its body up to the closing line. A body with a backslash, or a marker line that redirects into a file (`>` / `>>` not to `/dev/null`, `tee`) — exit 2, the reason on stderr: `bashguard: heredoc refused — <a backslash in its body | it writes <path>>. Write the script with the Write tool into the scratchpad and run it by path; change a file with Edit.`
**＋** Before the refusal one line `- HH:MM:SS <stamp> bashguard: <reason>` goes to `raw/<date>/event_log.md` (case 91).
**＋** Any other tool, a command without a heredoc, a heredoc without a backslash and without a file write, an unreadable payload — exit 0, the last with a line on stderr; the hook never raises.
**＋** `rule-bash-guard` is a `Leaf`, `enforcement: hook`, `implementation_ref: [guppi/bashguard.py, tests/test_bashguard.py, .claude/settings.json]`, `parent: rule-harness`, `tags: [hooks, harness]`; `estimate-bash-guard` (`QA`), `pending`: the test on `python - <<'EOF'` with `\n` in the body → 2; `cat > f <<EOF` → 2; a heredoc with a clean body into a pipe → 0; a command without a heredoc → 0; an unreadable payload → 0; the live reading is the first refusal in Work Mode or, without one, the test.
**＋** `rule-hook-registry`: in `PreToolUse` after the matcher `Edit|Write|MultiEdit` — `{ "matcher": "Bash", "hooks": [ { "type": "command", "command": "uv run guppi bashguard", "timeout": 30 } ] }`; `contract: same`; `rule-harness` gets `rule-bash-guard` as its seventh child through the `ref`.
**－** `{supersedes:case 120}`: `decision-case-120` is superseded, `rule-bash-guard` loses `deferred_by`.

## Method

pytest in `tests/test_bashguard.py` with piped payloads — a `python - <<'EOF'` body with `\n` → 2, `cat > f <<EOF` → 2, a clean heredoc into a pipe → 0, no heredoc → 0, an unreadable payload → 0; the live reading is the first refusal of a Work Mode, written into the estimate line, or the test alone when none occurs

## Result

live 2026-09-14 session O, block 127: the first heredoc with a backslash in its body (`cat <<'EOF' | head -1`) was refused, exit 2, the reason naming Write and Edit and the scratchpad; the event log carries `12:34:26 07a95bd2 bashguard refused: a backslash in its body` before the refusal

## History

- 2026-09-14 created · [[decision-case-127]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1029/ledger.md#L35
- 2026-09-14 status: passed → passed · raw/2026-09-14/1229/ledger.md#L3
