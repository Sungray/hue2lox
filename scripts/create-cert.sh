#!/bin/sh
set -eu
: "${HUE2LOX_BIND_IP:?Set HUE2LOX_BIND_IP to the local server IPv4 address}"
python3 -c 'import ipaddress,os; ipaddress.IPv4Address(os.environ["HUE2LOX_BIND_IP"])'
cd "$(dirname "$0")/.."
if [ -e certs/server.key ] || [ -e certs/server.crt ]; then
    echo 'Certificate/key already exists; refusing overwrite.' >&2
    exit 1
fi
umask 077
mkdir -p certs
chmod 700 certs
work=$(mktemp -d certs/.generate.XXXXXX)
trap 'rm -rf "$work"' EXIT HUP INT TERM
openssl req -x509 -newkey rsa:2048 -sha256 -nodes -days 365 \
    -keyout "$work/server.key" -out "$work/server.crt" \
    -subj '/CN=hue2lox.local' \
    -addext "subjectAltName=IP:${HUE2LOX_BIND_IP},IP:127.0.0.1,DNS:localhost,DNS:hue2lox.local" \
    -addext 'extendedKeyUsage=serverAuth'
chmod 600 "$work/server.key"
chmod 644 "$work/server.crt"
if [ "$(id -u)" = 0 ]; then
    chown 10001:10001 "$work/server.key" "$work/server.crt" certs
fi
mv "$work/server.key" certs/server.key
mv "$work/server.crt" certs/server.crt
chmod 700 certs
# When generated without sudo, chown certs to UID/GID 10001 before container use.
echo "Created certificate for ${HUE2LOX_BIND_IP} and localhost; valid for 365 days."
