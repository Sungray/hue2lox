<p align="center"><a href="README.md">Deutsch</a> | <a href="README.en.md">English</a></p>

<p align="center">
  <img src="web/hue2lox-logo.png" width="360" alt="Hue2Lox – our octopus holding the wordmark">
</p>
<h1 align="center">Get a grip on Hue. With Hue2Lox.</h1>
<p align="center">Connect Philips Hue to Loxone – locally, clearly, with eight helping arms.</p>
<p align="center"><a href="docs/MANUAL.en.md">Manual</a> · <a href="docs/INSTALL.en.md">Installation</a> · <a href="RELEASE.md">Release status</a></p>

**Release Candidate 1.** German and English are available. A fresh Debian 13 installation, bridge pairing, light display and restart have passed a user-run test. Full acceptance of all Loxone functions on this release remains pending. Original project code is licensed under Apache 2.0.

The public download contains **source code, the installer and Dockerfile**. The installer builds the Hue2Lox image on your Linux machine; we do not offer prebuilt Hue2Lox images at this stage.

## Start here

**[Installation](docs/INSTALL.en.md) · [Download RC1 ZIP](https://github.com/square-com-de/hue2lox/releases/download/v1.0.0-rc.1/hue2lox-main.zip) · [Release notes](https://github.com/square-com-de/hue2lox/releases/tag/v1.0.0-rc.1)**

RC1 is an immutable version. Verify its [commit and checksum](docs/DOWNLOADS.md); do not follow the outdated main-download instructions inside the RC1 ZIP. `main` is the separate development version.

Fresh Ubuntu, Debian, Raspberry Pi OS 64-bit or DietPi setup: prerequisites, ZIP download, transfer from your Mac/PC to the server, and first login. Each step states where to run it.

## Features

- Pair multiple Hue Bridges and discover lights and Hue scenes.
- Use switching, dimming, RGB and white temperature according to light capabilities.
- Filter by bridge and room; ignore and restore lights or scenes.
- Copy Loxone HTTP commands or export a selection as XML.
- Inspect incoming requests in a temporary, sanitized HTTP monitor.
- Manage locally over HTTPS without a cloud account for normal operation.

Create and edit scenes in the Hue app; recall them through Loxone. Synchronizing actual Hue light state back into the Loxone Lighting Controller is not part of this project.

## Preview

![Loxone command fields in Hue2Lox](web/tutorial-commands.png)

*Example with test data and German labels; the current layout is more compact. More illustrations are in the [Loxone guide](docs/TUTORIAL.en.md).*

## Get started

You need a Linux machine with Docker Compose, Python and OpenSSL, a supported Hue Bridge and a Loxone Miniserver for control. See [docs/TEST-RESULTS.md](docs/TEST-RESULTS.md) for the documented test scope.

1. Follow [the English installation guide](docs/INSTALL.en.md), using a separate test directory and free port.
2. Generate a fresh installation with individual control tokens and TLS keys and an empty bridge list.
3. Open the web interface, verify its certificate, and sign in with `admin` / `admin`. Change the password in the interface.
4. Pair a bridge, inspect discovered lights and follow the [Loxone guide](docs/TUTORIAL.en.md).

**Existing development installations:** use the established staged update path, not fresh setup. Preserve credentials and device state. A general release updater is not yet approved.

The [interactive installer](docs/INSTALL.en.md) offers English and German menus for system checks, SSH, packages, Docker and setup. Changes require confirmation.

## Install with ChatGPT or Claude

[AI installation prompt and prerequisites](docs/AI-INSTALL.en.md): copy the prompt, check your target system and set up an isolated test instance step by step. With terminal access the assistant can act; otherwise it guides you. The assistant guides you to the same interactive installer.

## Documentation

| Topic | Start here |
| --- | --- |
| Usage, troubleshooting and backup | [Manual](docs/MANUAL.en.md) |
| Fresh test installation | [Installation](docs/INSTALL.en.md) |
| Loxone HTTP outputs and XML | [Illustrated guide](docs/TUTORIAL.en.md) |
| Architecture and container | [Technical reference (German)](docs/CONTAINER.md) |
| Quality checks and contributing | [Development](CONTRIBUTING.md) |
| Joint hardware tests | [Acceptance plan](docs/ACCEPTANCE.md) |
| Sources, icons and licensing | [Third-party notices](THIRD-PARTY-NOTICES.md) |
| Release status and limits | [Release notes](RELEASE.md) |

## Quality and security

[GitHub checks](https://github.com/square-com-de/hue2lox/actions/workflows/quality.yml) cover source, translations, local HTTPS startup and an isolated container. Passing checks do not prove compatibility with every light or Miniserver.

Do not submit tokens, private keys, private backups or token-bearing XML in issues or pull requests. See [security reporting](SECURITY.md).

## License status

Hue2Lox uses the [Apache License 2.0](LICENSE), which permits commercial use and redistribution under its terms. Original code, documentation and project artwork are included to the extent applicable rights exist. Third-party materials retain their own terms: [notices](THIRD-PARTY-NOTICES.md) · [NOTICE](NOTICE).

Independent project; not officially affiliated with Philips Hue or Loxone.

<p align="center"><strong>by <a href="https://square-com.de/">square | com</a></strong> · <a href="https://square-com.de/impressum/">Impressum / Legal notice</a></p>
