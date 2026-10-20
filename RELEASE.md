# Hue2Lox — Release Candidate 1

[RC1 release notes and ZIP](https://github.com/square-com-de/hue2lox/releases/tag/v1.0.0-rc.1) · [English installation](docs/INSTALL.en.md) · [Deutsche Installation](INSTALL.md)

Published RC1 (`v1.0.0-rc.1`) remains unchanged. The `main` branch includes subsequent repository and documentation cleanup. Test the exact candidate commit before publishing stable; a passing older release test is not automatic acceptance of newer changes.

Publisher: **square | com** · [Impressum](https://square-com.de/impressum/)
License: Apache 2.0 for original project material; see LICENSE, NOTICE and THIRD-PARTY-NOTICES.md.

## Delivery

This repository starts with a clean source snapshot, without private development history.
Download the source ZIP or clone this repository and follow [INSTALL.md](INSTALL.md).
Docker images are built locally from these sources. No prebuilt Hue2Lox images or VM appliances are distributed.

## Validation and limits

On 20 October 2026, a user-run fresh Debian 13 VM installation passed installation, login, bridge discovery/pairing, inventory display and a full VM reboot with the configuration retained. See [docs/TEST-RESULTS.md](docs/TEST-RESULTS.md).
Automated source, HTTPS and container checks are defined in GitHub Actions; consult the run for the specific commit.
Full Loxone acceptance on this release, backup/restore and certificate renewal remain additional acceptance work. Existing historical live-control tests do not imply every device or distribution is covered.

## Operating notes

- Intended for a trusted local network; do not expose the interface directly to the Internet.
- Initial login: `admin` / `admin`. Change the password after installation.
- New installations generate individual control tokens and TLS keys.
- The installer refuses to overwrite an existing destination. It is not a general upgrade tool. Back up existing configuration and secrets before any manual update; preserve `.env` and the installation name.
- See [SECURITY.md](SECURITY.md) for reporting vulnerabilities, and GitHub Issues for ordinary bugs (without private data).

## Future prebuilt image release gate

Before changing the delivery model, complete and review the following for the
exact image to be distributed:

- Record the release/source commit, build recipes and patches, base index and
  platform digests, resulting image digests and every offered CPU architecture.
- Inventory the final image, including OS packages, Python, pip, vendored
  libraries and transitive dependencies; produce a versioned SBOM per platform.
- Collect applicable complete license texts, copyrights and notices per
  component, with a mapping to the inventory. A generic Python/Alpine notice
  or a list of SPDX identifiers alone is not the complete license package.
- Determine and fulfill source-delivery obligations under each applicable
  GPL/LGPL or other license: retain matching sources, build scripts and patches,
  and provide a compliant delivery method or offer where permitted. Do not
  assume a link to an upstream homepage or SBOM satisfies these obligations.
- Retain copies and an availability/retention plan for any required source
  delivery or offers; document where recipients obtain the materials.
- Package notices and accompanying materials with the release, and verify the
  recipient-facing download path. Resolve the Hue certificate redistribution
  question for images as well as source archives.
- Run image security checks and acceptance tests on the exact release digests.
  Record license review and release approval separately from test results.

Until these checks are complete, continue source-only distribution. A local
user who later redistributes their built image must assess that distribution's
obligations separately; the local-build workflow is not a blanket exemption.
