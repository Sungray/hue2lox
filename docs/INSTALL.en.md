# Install Hue2Lox on Linux

[Deutsch](../INSTALL.md) · [RC1 release and ZIP](https://github.com/square-com-de/hue2lox/releases/tag/v1.0.0-rc.1) · [English manual](MANUAL.en.md)

This guide installs published RC1 via its unchanged interactive installer. Verify the [version, commit, ZIP and SHA-256 mapping](DOWNLOADS.md) first. Do not follow old main-download instructions inside the RC1 archive. The manual German development guide targets a different layout.

## Requirements and supported systems

You need a Linux server or VM, its address and user account, root or sudo access, Internet access for packages and the Docker base image, and access to your Hue Bridge on the local network. Install the OS and SSH first; the installer cannot establish an SSH connection to a server without SSH. macOS and Windows are clients, not installation targets.

| 64-bit system | Automatic package setup | Observed test scope |
| --- | --- | --- |
| Ubuntu 22.04 / 24.04 / 26.04 LTS | amd64, arm64 | Ubuntu 26.04 amd64 through HTTPS health check; other variants pending |
| Debian 12 / 13 | amd64, arm64 | Debian 13 VM: installation, login, pairing, inventory and reboot confirmed by user on 20 October 2026; Debian 12/ARM pending |
| Raspberry Pi OS based on Debian 12 / 13 | arm64 | Detection tested automatically; physical Pi acceptance pending |
| DietPi based on Debian 12 / 13 | amd64, arm64 | Detection tested automatically; full platform acceptance pending |
| Other Linux distributions | Install prerequisites manually; existing Docker and Compose can be reused | No general compatibility claim |

A 64-bit processor with a 32-bit OS is not sufficient. Existing working Docker Engine and Compose are reused. The installer does not automatically remove conflicting Docker packages or overwrite existing installation directories. Images are built locally from source; no prebuilt Hue2Lox image is distributed.

## 1. Download on your Mac or Windows PC

For the published candidate, download **hue2lox-main.zip** from [RC1 assets](https://github.com/square-com-de/hue2lox/releases/tag/v1.0.0-rc.1). Verify the checksum using [these commands](DOWNLOADS.md#prüfen--verify). Do not use Code → Download ZIP for a release installation. Development downloads are listed separately in that document. Keep the archive zipped in Downloads. GitHub's automatically generated “Source code” archive may use a different folder name; commands below use our named asset or the main-branch ZIP.

Downloads are public; no GitHub login is required. If Safari automatically extracts the ZIP, disable that option and download it again.

## 2. Copy to the server and connect

Replace `anna` and `192.0.2.50` with your Linux user and server address. In the server's local console, `whoami` shows the user and `hostname -I` shows addresses.

**Mac Terminal:**

```sh
scp ~/Downloads/hue2lox-main.zip anna@192.0.2.50:~/hue2lox-main.zip
ssh anna@192.0.2.50
```

**Windows PowerShell with OpenSSH:**

```powershell
scp "$env:USERPROFILE\Downloads\hue2lox-main.zip" anna@192.0.2.50:~/hue2lox-main.zip
ssh anna@192.0.2.50
```

Verify the SSH host fingerprint through the server console on first connection. Password entry shows no characters. If SSH is missing, run `apt update && apt install openssh-server` as root in the Linux console, then `systemctl enable --now ssh` and retry.

## 3. Check sudo on the server

As your normal Linux user:

```sh
sudo whoami
```

If it prints `root`, continue. On minimal Debian, sudo may be missing or your user may lack permission. Run `whoami` and remember your normal username, then:

```sh
su -
```

Enter the **root password** chosen during Debian installation. If you have no root access, ask the server administrator to perform this setup. As root:

```sh
apt update && apt install -y sudo
read -r -p 'Normal Linux username: ' HUE2LOX_USER
if [ -n "$HUE2LOX_USER" ] && [ "$HUE2LOX_USER" != root ] && id "$HUE2LOX_USER" >/dev/null 2>&1; then
  usermod -aG sudo "$HUE2LOX_USER"
else
  printf 'User not found. Check the name and repeat this block.\n'
fi
```

Stop on errors. Exit root, then exit SSH:

```sh
exit
exit
```

Reconnect from your Mac/PC with `ssh anna@192.0.2.50` and check `sudo whoami` again. A new login is necessary for group permissions to apply. Alternatively, an administrator may run the installer as root without sudo, using absolute paths under the user's home directory.

## 4. Extract and start — on the server

```sh
sudo apt update && sudo apt install -y --no-install-recommends unzip
unzip -tq ~/hue2lox-main.zip &&
mkdir ~/hue2lox-installer &&
unzip -q ~/hue2lox-main.zip -d ~/hue2lox-installer
```

Stop if a command fails. If the destination already exists, choose a new extraction directory and adjust the following path; do not overwrite an existing installation.

```sh
sudo bash "$HOME/hue2lox-installer/hue2lox-main/install-assistant.sh"
```

Select English when prompted. The menu offers:

1. Check the system and prerequisites without changes.
2. Check/configure SSH (optional; skip if already active).
3. Install base packages: Python, OpenSSL, curl, CA certificates and unzip.
4. Check/configure Docker and Compose. Existing working installations are reused.
5. Prepare Hue2Lox: choose the reachable server IPv4 address and an unused port; review and confirm them.
6. Start Hue2Lox and run its health check.
7. Choose another installation directory.

Use a separate installation directory (for example `/opt/hue2lox-test`). The installer refuses to overwrite an existing destination. Required dependencies are installed without optional package recommendations. An animated octopus shows progress; detailed output goes into protected logs whose location is displayed. Use `--verbose` for full terminal output.

The installation stores its generated container/project name in `.env`; preserve it for maintenance. Other Docker projects should remain running: do not stop Docker globally or run a system-wide prune.

## 5. Open and pair

Open the HTTPS address printed by the installer, for example `https://192.0.2.50:18443`. The certificate is locally generated. Compare its SHA-256 fingerprint with the server output before adding a browser exception:

```sh
sudo openssl x509 -in /opt/hue2lox-test/certs/server.crt -noout -fingerprint -sha256
```

Initial login is **admin / admin**. You can change the password in the interface. Pair a bridge via **Bridges**, pressing its physical button when instructed. Check the inventory, then follow the [English Loxone tutorial](TUTORIAL.en.md). Scenes are created in the Hue app. Actual Hue state is not synchronized back into the Loxone Lighting Controller.

For persistent browser trust, import only the public server certificate after checking its fingerprint; never share `server.key`. Certificates last 365 days and require renewal. Trust and HTTPS compatibility with the Miniserver are separate checks.

## Troubleshooting and maintenance

- **Incorrect time / “Not live until”:** check `date -u` and `timedatectl status` on the server; correct clock synchronization before retrying package installation.
- **Port already in use:** choose another free port. Do not stop unrelated containers.
- **Wrong IP or existing destination:** stop and inspect the installation before retrying. A changed IP can require a new certificate. Do not erase a paired installation to retry setup.
- **Bridge not found:** check the VM's LAN connectivity and firewall; manual bridge entry may be needed when multicast discovery cannot cross networks.
- **Start failed:** inspect the installation's own Compose project, replacing paths if you chose another directory:

```sh
sudo docker compose --project-directory /opt/hue2lox-test --env-file /opt/hue2lox-test/.env -f /opt/hue2lox-test/compose.yaml ps
sudo docker compose --project-directory /opt/hue2lox-test --env-file /opt/hue2lox-test/.env -f /opt/hue2lox-test/compose.yaml logs --tail=60
```

Read logs locally and remove credentials and personal details before sharing. Report the source version, OS/architecture, failing step and sanitized error in [Issues](https://github.com/square-com-de/hue2lox/issues).

The installer is for fresh installations, not a general updater. Preserve the whole installation including `.env`, data, secrets and certificates; follow [backup and recovery guidance](MANUAL.en.md). Do not copy individual newer files into RC1. The [German extended guide](../INSTALL.md) also documents manual setup and specific network migration procedures; those sections are not yet translated.
