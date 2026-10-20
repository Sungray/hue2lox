# Hue model reference snapshot

Retrieved 2026-10-18 from the Philips definitions maintained by
[zigbee-herdsman-converters](https://github.com/Koenkk/zigbee-herdsman-converters/blob/499535e092401a6c21e8c3b5e3aeca8062c11841/src/devices/philips.ts).
949 distinct model IDs, with product identifier, description, on/off, dimming,
color-temperature, RGB and gradient flags. The ZIP download under Lamps contains the CSV, this source notice and the full MIT license.
JSON includes the immutable source URL, commit and SHA-256 of the downloaded upstream file.

Upstream commit: `499535e092401a6c21e8c3b5e3aeca8062c11841`.
Source SHA-256: `96b02d51956f47dab2bf9f0e5ada7f2d56902a27873724d3dd2539af2b59a2c5`.
Copyright (c) 2018 Koen Kanters. Derived catalog data retains the upstream MIT terms; include the accompanying full license when redistributing.

This is a community-maintained reference, not an official complete worldwide Hue
product catalog. Regional SKUs, recently released products, Bluetooth-only products
or entries without a Zigbee model ID may be missing. Capabilities are extracted
from explicit light definitions, not guessed from product names. Gradient denotes
hardware catalog information, not additional multi-zone control in Hue2Lox.

For a connected light, Hue Bridge capability fields take precedence; catalog data
only supplies a product label. Unsupported modes cannot be enabled by a checkbox.
Unknown models remain usable according to their reported Bridge capabilities.
Runtime lookup is local and does not call the internet.

Regenerate from a downloaded `philips.ts` using
`python3 tools/build_hue_catalog.py /path/to/philips.ts`.
Upstream MIT license is included in LICENSE-zigbee-herdsman-converters. The build
script verifies the pinned source hash before writing files and reads data without executing upstream TypeScript.
