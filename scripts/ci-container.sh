#!/bin/sh
# Disposable Linux CI only: never touches an installed instance or a Hue bridge.
set -eu
[ "${CI:-}" = "true" ] || { echo 'Run only on a disposable CI runner.'; exit 1; }
[ "$(id -u)" = 0 ] || { echo 'Run with sudo on the disposable CI runner.'; exit 1; }
repo=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
# Also exercise the conventional docker build entry point, without device access.
docker build -t hue2lox-default-ci:check -f "$repo/Dockerfile" "$repo"
docker run --rm --entrypoint python hue2lox-default-ci:check -c 'import app,json; assert json.load(open("/app/registry.json")) == {"schema_version":1,"bridges":[]}'
test_root=$(mktemp -d /tmp/hue2lox-ci.XXXXXXXX)
project="hue2lox-ci-$$"
compose() { docker compose --project-directory "$test_root/instance" -p "$project" -f "$test_root/instance/compose.yaml" -f "$test_root/image.yaml" "$@"; }
cleanup() { compose down --remove-orphans >/dev/null 2>&1 || true; rm -rf -- "$test_root"; }
trap cleanup EXIT HUP INT TERM
python3 "$repo/scripts/prepare-install.py" --destination "$test_root/instance" --host 127.0.0.1 --port 18443
printf 'services:\n  hue2lox:\n    image: hue2lox-ci:check\n' > "$test_root/image.yaml"
compose config --quiet
compose up -d --build --wait --wait-timeout 120
[ "$(compose exec -T hue2lox id -u)" = 10001 ]
compose exec -T hue2lox python -c 'import os; assert not os.access("/app", os.W_OK)'
python3 "$repo/scripts/check-ci-http.py" "$test_root/instance"
compose restart
compose up -d --wait --wait-timeout 120
python3 "$repo/scripts/check-ci-http.py" "$test_root/instance"
echo 'PASS: fresh Docker build, health, non-root user, read-only application, HTTPS, login and restart.'
