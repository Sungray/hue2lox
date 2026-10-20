<p align="center"><a href="README.md">Deutsch</a> | <a href="README.en.md">English</a></p>

<p align="center">
  <img src="web/hue2lox-logo.png" width="360" alt="Hue2Lox – our octopus holding the wordmark">
</p>
<h1 align="center">Get a grip on Hue. With Hue2Lox.</h1>
<p align="center">Connect Philips Hue to Loxone – locally, clearly, with eight helping arms.</p>
<p align="center"><a href="docs/MANUAL.en.md">Manual</a> · <a href="docs/INSTALL.en.md">Installation</a></p>

**Your Hue lights. Your Loxone controls. One place to connect them.**

Want to use your Philips Hue lights in Loxone without putting together every HTTP command by hand? Hue2Lox discovers lights and scenes from your bridges, offers controls that match each light and generates commands you can copy or export as XML for Loxone Config.

Keep multiple bridges in one view, choose the devices you want to use and inspect incoming Loxone requests when troubleshooting. Everything runs on your own Linux server, with a German or English web interface and no cloud account needed for normal operation.

## Features

- Pair multiple Hue Bridges and discover lights and Hue scenes.
- Use switching, dimming, RGB and white temperature according to light capabilities.
- Filter by bridge and room; ignore and restore lights or scenes.
- Copy Loxone HTTP commands or export a selection as XML.
- Inspect incoming requests in a temporary, sanitized HTTP monitor.
- Manage locally over HTTPS without a cloud account for normal operation.

## Preview

![Loxone command fields in Hue2Lox](web/tutorial-commands.png)

*Example with test data and German labels; the current layout is more compact. More illustrations are in the [Loxone guide](docs/TUTORIAL.en.md).*

## Install and get started

You need a Linux server, VM or Raspberry Pi with a supported 64-bit OS, a Hue Bridge and a Loxone Miniserver for control. Use your Mac or Windows PC to follow the setup guide.

1. **Start the installer:** the [English installation guide](docs/INSTALL.en.md) takes you through prerequisites, downloading the RC1 ZIP, copying it to the server and starting the installer.
2. **Set up Hue2Lox:** the installer checks your system and can install missing packages and Docker. Existing working Docker installations are reused.
3. **Pair your bridge:** open the displayed HTTPS address, verify the certificate and sign in with `admin` / `admin`. You can change the password in the interface.
4. **Connect to Loxone:** choose lights or scenes and follow the [illustrated guide](docs/TUTORIAL.en.md) to copy commands or import XML into Loxone Config.

**[Open the installation guide](docs/INSTALL.en.md) · [Download RC1 ZIP](https://github.com/square-com-de/hue2lox/releases/download/v1.0.0-rc.1/hue2lox-main.zip) · [Verify the download](docs/DOWNLOADS.md)**

Prefer guidance from an AI assistant? Use the [ChatGPT or Claude installation prompt](docs/AI-INSTALL.en.md). It guides you to the same interactive installer.

## Release status and technical notes

**Release Candidate 1.** German and English are available. A fresh Debian 13 installation, bridge pairing, light display and restart have passed a user-run test. End-to-end testing with a Loxone Miniserver is still in progress. Original project code is licensed under Apache 2.0.

The public download contains **source code, the installer and Dockerfile**. The installer builds the Hue2Lox image on your Linux machine; we do not offer prebuilt Hue2Lox images at this stage.

RC1 is an immutable version. Verify its [commit and checksum](docs/DOWNLOADS.md); do not follow the outdated main-download instructions inside the RC1 ZIP. `main` is the separate development version.

Create and edit scenes in the Hue app; recall them through Loxone. Synchronizing actual Hue light state back into the Loxone Lighting Controller is not part of this project.

**Existing installations:** a general release updater is not yet available. Preserve credentials and device state; do not overwrite an existing installation with fresh setup.

See [release notes](RELEASE.md) and [documented test results](docs/TEST-RESULTS.md) for details.

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
