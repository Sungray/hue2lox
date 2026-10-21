# Running the container image

For Docker-native hosts (Unraid, Synology, Portainer, plain Docker). Linux hosts that prefer a guided setup can still use `install-assistant.sh` ([INSTALL.en.md](INSTALL.en.md)).

Images are published to `ghcr.io/square-com-de/hue2lox` for `linux/amd64` and `linux/arm64` on every release tag (`latest` for stable releases, `rc` for release candidates, plus the exact version).

## HTTP and HTTPS

The image serves **plain HTTP**. Like most self-hosted apps, it does not manage certificates: if you want HTTPS, terminate TLS in a reverse proxy in front of it and set `HUE_PUBLIC_URL` to the `https://` address. The proxy must forward the original `Host` header: the admin interface rejects requests whose `Host` or `Origin` differs from `HUE_PUBLIC_URL`. Without a proxy, the admin login and control token cross your network unencrypted, so only expose it on a network you trust.

Built-in HTTPS (as used by `install-assistant.sh`) is still available: set `TLS_CERT` and `TLS_KEY` to certificate and key files mounted into the container.

## Volumes

| Mount | Purpose |
| --- | --- |
| `/data` | Bridge registry, admin credentials, control token. Back this up. |

The container runs as UID/GID 10001, so `/data` must be writable by it.

## Docker Compose

Copy [`docker/compose.image.yaml`](../docker/compose.image.yaml), set `PORT` and `HUE_PUBLIC_URL`, then:

```sh
docker compose up -d
```

Host networking is used so bridges can be discovered on the LAN; the service listens on `PORT`, so choose one that is free on the host.

## Unraid (Compose Manager)

Create a stack, paste the contents of `docker/compose.image.yaml`, and replace `./data` with an absolute path such as `/mnt/user/appdata/hue2lox/data`. No source checkout or local build is needed.

## Updating

```sh
docker compose pull && docker compose up -d
```

`/data` is kept across upgrades and existing files are never overwritten by the container. Back up `/data` first: the data format is not yet versioned for compatibility between release candidates.

## Settings

| Variable | Default | Meaning |
| --- | --- | --- |
| `PORT` | `8443` | Listen port |
| `HUE_PUBLIC_URL` | `https://localhost:8443` | Address used in the generated Loxone commands; an `https://` value also marks the login cookie `Secure` |
| `HUE2LOX_ADMIN_PASSWORD` | `admin` | Initial admin password, applied only when no credentials exist yet |
| `TLS_CERT`, `TLS_KEY` | unset | Optional built-in HTTPS |
