#!/usr/bin/env bash
# Progress before Python exists. Only called for package-manager commands.
set -uo pipefail
label=$1; shift
umask 077
work=$(mktemp -d "${TMPDIR:-/tmp}/hue2lox-bootstrap-XXXXXXXX") || exit 1
log=$work/install.log
: > "$log"
mkfifo "$work/output" || exit 1
exec 3<>"$work/output"
exec 4<&0
animated=0; drawn=0; frame=0; live=0; private=0
[[ -t 1 && "${TERM:-dumb}" != dumb ]] && animated=1
clear_dance() {
  if (( drawn )); then
    printf '\033[4A\033[J'
    drawn=0
  fi
}
dance() {
  (( animated && ! live )) || return 0
  clear_dance
  printf '       .----.\n      ( o  o )\n'
  case $((frame % 4)) in
    0) printf '    _/ / || \\ \\_\n';;
    1) printf '   \\_\\ \\||/ /_/\n';;
    2) printf '    / / /||\\ \\ \\\n';;
    3) printf '   _\\ \\ || / /_\n';;
  esac
  printf '  %s …\n' "$label"
  frame=$((frame+1)); drawn=1
}
record() {
  local text=$1 partial=${2:-0}
  if [[ "$text" == *BEGIN*PRIVATE* ]]; then private=1; fi
  if (( private )) || printf '%s' "$text" | grep -Eiq 'password|passwort|token|secret|authorization|api.?key|private.?key|https?://[^ /]+@|[0-9a-f]{32,}'; then
    [[ "$text" != *END*PRIVATE* ]] || private=0
    text='[sensitive output omitted]'
  else
    # Never forward terminal control sequences from package output.
    if [[ "$text" == *$'\033'* ]]; then text='[terminal control output omitted]'; fi
    text=$(printf '%s' "$text" | tr -d '\000-\010\013-\037\177')
  fi
  printf '%s\n' "$text" >> "$log"
  if (( partial )) || [[ "$text" == *\?* || "$text" == *configuration\ file* || "$text" == *Konfigurationsdatei* ]]; then
    if (( ! live )); then clear_dance; tail -n 18 "$log"; live=1; return; fi
  fi
  (( ! live )) || printf '%s\n' "$text"
}
cleanup() { exec 3>&-; exec 4<&-; rm -f "$work/output"; }
trap cleanup EXIT
printf '%s …\n' "$label"
"$@" <&4 > "$work/output" 2>&1 &
child=$!
trap 'kill -INT "$child" 2>/dev/null || true; clear_dance; wait "$child"; exit 130' INT
trap 'kill -TERM "$child" 2>/dev/null || true; clear_dance; wait "$child"; exit 143' TERM
dance
buffer=; idle=0; tick=0.15; prompt_ticks=4
if (( BASH_VERSINFO[0] < 4 )); then tick=1; prompt_ticks=1; fi
while true; do
  chunk=
  if IFS= read -r -n 1 -t "$tick" chunk <&3; then
    if [[ -z "$chunk" ]]; then
      record "$buffer"
      buffer=
    else
      buffer=$buffer$chunk
    fi
    idle=0
  else
    buffer=$buffer$chunk
    idle=$((idle+1))
    if ! kill -0 "$child" 2>/dev/null; then
      [[ -z "$buffer" ]] || record "$buffer"
      break
    fi
    if [[ -n "$buffer" ]] && (( idle >= prompt_ticks )); then
      record "$buffer" 1
      buffer=; idle=0
    fi
    dance
  fi
done
code=0
wait "$child" || code=$?
clear_dance
if (( code )); then
  printf '\n[ERROR] %s\n' "$label"
  (( live )) || tail -n 18 "$log"
else
  printf '\n[OK] %s\n' "$label"
fi
printf 'Log: %s\n' "$log"
exit "$code"
