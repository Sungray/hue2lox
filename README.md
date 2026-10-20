<p align="center">
  <img src="web/hue2lox-logo.png" width="360" alt="Hue2Lox – unser Oktopus hält den Schriftzug">
</p>
<h1 align="center">Hue im Griff. Mit Hue2Lox.</h1>
<p align="center">Philips Hue mit Loxone verbinden – lokal, übersichtlich und mit acht helfenden Armen.</p>
<p align="center"><a href="README.en.md">English</a> · <a href="MANUAL.md">Handbuch</a> · <a href="INSTALL.md">Installation</a> · <a href="RELEASE.md">Release-Status</a></p>

**Public Beta.** Deutsch und Englisch sind verfügbar. Eine frische Debian-13-Installation mit Bridge-Kopplung, Lampenanzeige und Neustart wurde erfolgreich getestet. Die vollständige Abnahme aller Loxone-Funktionen auf dem Veröffentlichungsstand bleibt offen. Der eigene Projektcode steht unter Apache 2.0.

Der öffentliche Download enthält den **Quellcode samt Installer und Dockerfile**. Der Installer baut das Hue2Lox-Image auf deinem Linux-Rechner; ein fertiges Hue2Lox-Image bieten wir vorerst nicht an.

## Hier starten

**[Hue2Lox installieren – Schritt für Schritt](INSTALL.md)**

Für eine frische Linux-Installation (Ubuntu, Debian, Raspberry Pi OS 64 Bit oder DietPi): Voraussetzungen, ZIP-Download, Übertragung vom Mac/PC auf den Server und erster Login. Jeder Schritt zeigt, wo du ihn ausführst.

## Was Hue2Lox kann

- Mehrere Hue Bridges koppeln und Lampen sowie Hue-Szenen einlesen.
- Ein/Aus, Dimmen, RGB und Weißtemperatur passend zu den Lampenfähigkeiten anbieten.
- Lampen und Szenen nach Bridge und Raum filtern, ignorieren und wieder einblenden.
- Loxone-HTTP-Befehle kopieren oder eine Auswahl als XML exportieren.
- Loxone-Anfragen mit einem zeitlich begrenzten, bereinigten HTTP-Monitor prüfen.
- Lokal über HTTPS verwalten – ohne Cloudkonto für den laufenden Betrieb.

Szenen erstellst du weiterhin in der Hue-App. Hue2Lox ruft sie über Loxone ab. Eine Synchronisierung des tatsächlichen Lampenzustands zurück in den Loxone-Lichtsteuerungsbaustein ist nicht vorgesehen.

## So sieht es aus

![Befehle für Loxone im Hue2Lox-Webinterface](web/tutorial-commands.png)

*Beispielansicht mit Testdaten; die aktuelle Oberfläche ist kompakter. Weitere Abbildungen stehen in der [Loxone-Anleitung](TUTORIAL.md).*

## Starten

Du brauchst einen Linux-Rechner mit Docker Compose, Python und OpenSSL, eine unterstützte Hue Bridge sowie für die Steuerung einen Loxone Miniserver. Den dokumentierten Testumfang findest du in [TEST-RESULTS.md](TEST-RESULTS.md).

1. Folge der [Linux-Installation mit Installer oder Schritt für Schritt](INSTALL.md): Voraussetzungen installieren, ZIP herunterladen, vom Mac/PC auf den Server kopieren und starten.
2. Erzeuge eine frische Installation mit eigenen Schlüsseln und leerer Bridge-Liste.
3. Öffne das Webinterface, prüfe das Zertifikat und melde dich mit `admin` / `admin` an. Das Passwort lässt sich dort ändern.
4. Kopple eine Bridge, prüfe die gefundenen Lampen und richte Loxone nach der [Anleitung](TUTORIAL.md) ein.

**Für bestehende Entwicklungsinstallationen:** Nicht neu installieren. Den bisherigen vorbereiteten Update-Weg nutzen; Zugangsdaten und gespeicherte Geräte erhalten. Ein allgemeiner Release-Updater ist noch nicht freigegeben.

Der [Installer – einfach und komfortabel](INSTALL.md#option-1-einfach-und-komfortabel--der-installer) bietet ein Menü für Systemprüfung, SSH, Grundpakete, Docker und Einrichtung. Änderungen erfolgen erst nach Bestätigung.

## Mit ChatGPT oder Claude installieren

[KI-Installationsprompt und Voraussetzungen](AI-INSTALL.md): kopieren, Zielsystem prüfen lassen und Schritt für Schritt eine getrennte Testinstallation einrichten. Mit Terminalzugriff kann die KI ausführen; ohne Zugriff begleitet sie dich. Die KI begleitet dich bis zum Start desselben interaktiven Installers.

## Dokumentation

| Thema | Einstieg |
| --- | --- |
| Bedienung, Fehlerbehebung, Backup | [Handbuch](MANUAL.md) |
| Neue Testinstallation | [Installation](INSTALL.md) |
| HTTP-Ausgänge und XML in Loxone | [Bebilderte Anleitung](TUTORIAL.md) |
| Architektur und Container | [Technik](CONTAINER.md) |
| Qualitätsprüfungen und Mitarbeit | [Entwicklung](CONTRIBUTING.md) |
| Was wir gemeinsam testen | [Abnahmeplan](docs/ACCEPTANCE.md) |
| Quellen, Icons und Lizenzstatus | [Drittanbieterhinweise](THIRD-PARTY-NOTICES.md) |
| Release-Stand und Grenzen | [Release-Hinweise](RELEASE.md) |

## Tests und Sicherheit

[Automatische Prüfungen auf GitHub](https://github.com/square-com-de/hue2lox/actions/workflows/quality.yml) prüfen Quellcode, Übersetzungen, lokale HTTPS-Installation und einen isolierten Container. Ein grüner Lauf bestätigt nur diese Prüfungen, nicht den Betrieb mit jeder Hue-Lampe oder jedem Miniserver.

Keine Tokens, privaten Schlüssel, Zertifikats-Backups oder XML-Dateien mit echtem Token in Issues oder Pull Requests hochladen. Siehe [Sicherheit](SECURITY.md).

## Lizenzstatus

Hue2Lox steht unter der [Apache License 2.0](LICENSE). Sie erlaubt auch kommerzielle Nutzung und Weitergabe unter ihren Bedingungen. Eigener Code, Dokumentation und eigene Projektgrafiken sind einbezogen, soweit entsprechende Rechte bestehen. Drittanbieterbestandteile behalten ihre eigenen Bedingungen: [Lizenzen und Quellen](THIRD-PARTY-NOTICES.md) · [NOTICE](NOTICE).

Unabhängiges Projekt; keine offizielle Verbindung zu Philips Hue oder Loxone.

<p align="center"><strong>by <a href="https://square-com.de/">square | com</a></strong> · <a href="https://square-com.de/impressum/">Impressum / Legal notice</a></p>
