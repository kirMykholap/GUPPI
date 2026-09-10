---
type: lesson
kind: error
root_cause: a hook's stdin on Windows is a cp1252 text wrapper with `surrogateescape`; a UTF-8 payload becomes lone surrogates, `write_text(encoding="utf-8")` raises after creating the file; fixed by reading `stdin.buffer` and decoding UTF-8 (`read_text` in `guppi/event.py`), stderr reconfigured to UTF-8 in `cli.py`, covered by tests
status: new
estimates: [estimate-hooks-windows-stdin-encoding]
origin: raw/2026-09-09/ledger.md#L31
sprint: migration
created: 2026-09-09
---

## Trigger

`probe-Stop-1.json` and `-2.json` were 0 bytes although the `Stop` hook had fired, and `event_log.md` carried mojibake (`â€”`) in tool details

## Root cause

a hook's stdin on Windows is a cp1252 text wrapper with `surrogateescape`; a UTF-8 payload becomes lone surrogates, `write_text(encoding="utf-8")` raises after creating the file; fixed by reading `stdin.buffer` and decoding UTF-8 (`read_text` in `guppi/event.py`), stderr reconfigured to UTF-8 in `cli.py`, covered by tests

## Estimates

- [[estimate-hooks-windows-stdin-encoding]]

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#L31
