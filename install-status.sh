#!/bin/sh
# Run as root; updates only the existing Hue2Lox prototype.
set -eu
: "${HUE_PUBLIC_URL:?Set HUE_PUBLIC_URL to this installation HTTPS URL}"
[ "$(id -u)" = 0 ] || { echo 'Run as root'; exit 1; }
src=/opt/loxberry/hue2lox-status-staging
dst=/opt/loxberry/hue2lox-prototype
backup=/opt/loxberry/hue2lox-backups/$(date +%Y%m%d-%H%M%S)
umask 077
mkdir -p "$backup"
cp -p "$dst/app.py" "$dst/compose.yaml" "$dst/.dockerignore" "$backup/"
printf 'Rollback files: %s\n' "$backup"
install -m 644 "$src/app.py" "$dst/app.py"
install -m 644 "$src/hue_client.py" "$dst/hue_client.py"
buildfile="$src/Dockerfile.status"
[ -f "$buildfile" ] || buildfile="$src/Dockerfile"
install -m 644 "$buildfile" "$dst/Dockerfile.status"
install -m 644 "$src/.dockerignore" "$dst/.dockerignore"
install -m 644 "$src/compose.yaml" "$dst/compose.yaml"
install -d -m 755 "$dst/trust"
install -m 644 "$src/trust/huebridge-ca.pem" "$dst/trust/huebridge-ca.pem"
install -d -m 700 -o 10001 -g 10001 "$dst/secrets"
install -m 400 -o 10001 -g 10001 "$src/secrets/hue_key" "$dst/secrets/hue_key"
cd "$dst"
docker compose config --quiet
docker compose build
# Validate actual container runtime, TLS and key before replacing running service.
docker compose run --rm --no-deps hue2lox python hue_client.py
docker compose up -d --no-build
# Allow startup, then check both HTTPS endpoints using existing trusted cert.
i=0
until curl --fail --silent --show-error --max-time 8 --cacert health-test.crt "${HUE_PUBLIC_URL}/hue-go/status"; do
    i=$((i + 1)); [ "$i" -lt 5 ] || exit 1
    sleep 2
done
printf '\n'
curl --fail --silent --show-error --max-time 8 --cacert health-test.crt "${HUE_PUBLIC_URL}/health"
printf '\n'
docker compose ps
docker compose logs --tail=20 hue2lox
