#!/bin/sh
# Prepare new runtime with color commands still disabled. Never sends a PUT.
set -eu
: "${HUE_PUBLIC_URL:?Set HUE_PUBLIC_URL to this installation HTTPS URL}"
[ "$(id -u)" = 0 ] || { echo 'Run as root'; exit 1; }
src=/opt/loxberry/hue2lox-white-staging
dst=/opt/loxberry/hue2lox-prototype
backup=/opt/loxberry/hue2lox-backups/white-$(date +%Y%m%d-%H%M%S)
umask 077
mkdir -p "$backup"
for f in app.py hue_client.py color.py compose.yaml .dockerignore Dockerfile.status compose.override.yaml; do
    if [ -f "$dst/$f" ]; then cp -p "$dst/$f" "$backup/$f"; fi
done
printf 'Rollback files: %s\n' "$backup"
for f in app.py hue_client.py color.py compose.yaml .dockerignore Dockerfile.status; do
    install -m 644 "$src/$f" "$dst/$f"
done
# Preserve existing on/off/dimming activation and token. Do not change override.
cd "$dst"
docker compose config --format json | python3 -c 'import json,sys; d=json.load(sys.stdin); assert str(d["services"]["hue2lox"]["environment"].get("HUE_WHITE_ENABLED")) == "0", "White must stay disabled"'
docker compose build
docker compose run --rm --no-deps hue2lox python hue_client.py
docker compose up -d --no-build
i=0
until curl --fail --silent --show-error --max-time 8 --cacert health-test.crt "${HUE_PUBLIC_URL}/health"; do
    i=$((i + 1)); [ "$i" -lt 8 ] || exit 1
    sleep 2
done
printf '\n'
curl --fail --silent --show-error --max-time 8 --cacert health-test.crt "${HUE_PUBLIC_URL}/hue-go/status"
printf '\n'
docker compose ps
printf 'Prepared white code installed; white control remains disabled. No Hue PUT sent by this script.\n'
