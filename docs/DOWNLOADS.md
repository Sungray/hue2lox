# Versionierter Download / Versioned download

Der aktuelle veröffentlichte Kandidat ist **RC1**, kein Stable. / The published candidate is **RC1**, not stable.

| Merkmal / Field | Wert / Value |
| --- | --- |
| Version | `v1.0.0-rc.1` |
| Commit | `1d631cd1231d7cf004c6452c1fad0c262ff92bfd` |
| Paket / Package | [hue2lox-main.zip](https://github.com/square-com-de/hue2lox/releases/download/v1.0.0-rc.1/hue2lox-main.zip) |
| SHA-256 | `a630235b27d3f2bde5419d146050013c21907ec8862c3d88ef4ed8bc2c2a1f09` |
| Archivordner / Archive root | `hue2lox-main/` |
| Prüfsummendatei / Checksums | [SHA256SUMS.txt](https://github.com/square-com-de/hue2lox/releases/download/v1.0.0-rc.1/SHA256SUMS.txt) |

Der Name allein identifiziert die Version nicht. Das gleichnamige Branch-ZIP ist ein anderer Download. Verwende das obige Asset. / The filename alone does not identify the version. The branch ZIP has the same name but different contents. Use the asset above.

## Prüfen / Verify

**Mac**, im Downloadordner / in Downloads:

```sh
cd ~/Downloads
shasum -a 256 hue2lox-main.zip
```

**Windows PowerShell**:

```powershell
Get-FileHash "$env:USERPROFILE\Downloads\hue2lox-main.zip" -Algorithm SHA256
```

**Linux**, im Ordner der ZIP / in the ZIP directory:

```sh
printf '%s  %s\n' 'a630235b27d3f2bde5419d146050013c21907ec8862c3d88ef4ed8bc2c2a1f09' hue2lox-main.zip | sha256sum --check
```

Nur bei passender Prüfsumme fortfahren. / Continue only if the checksum matches.

Für RC1 führt [Installation](../INSTALL.md) (Option 1) bzw. die [englische Anleitung](INSTALL.en.md) zum unveränderten interaktiven Einstieg. Die manuelle Option 2 beschreibt dagegen den neueren main-Quellbaum. Die alten Hinweise im unveränderten RC1-ZIP auf main-Downloads nicht verwenden; die obige Paketbindung hat Vorrang. / For RC1, use option 1 of the German guide or the English interactive guide. Manual option 2 targets the newer main layout. Ignore the old main-download instructions inside the immutable RC1 archive; use this package mapping instead.

## Entwicklung / Development

[main.zip](https://github.com/square-com-de/hue2lox/archive/refs/heads/main.zip) ist ausschließlich der bewegliche Entwicklungsstand. Er ist kein RC1- oder Stable-Paket. / This is a moving development snapshot, not RC1 or stable. Record the tested commit separately.

## Stable-Vorbereitung / Stable preparation

Noch kein Stable-Paket vorhanden. Vor der Freigabe genau einen Commit prüfen, ein daraus erzeugtes Paket mit Archivordner und SHA-256 abgleichen und dann alle DE/EN/KI-Einstiege gemeinsam aktualisieren. Release-Assets erst nach dieser Abnahme veröffentlichen. RC1 wird nicht ersetzt. / No stable package exists yet. Verify one candidate commit, match its archive contents and SHA-256, then update all DE/EN/AI entry points together. Publish only after acceptance; do not replace RC1.
