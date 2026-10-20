# Mit KI installieren

[Startseite](README.md) · [English](AI-INSTALL.en.md) · [Installationsanleitung](INSTALL.md)

Öffne einen **neuen Chat** in ChatGPT, Claude oder einem anderen KI-Assistenten und kopiere den folgenden Prompt hinein. Die KI hilft bis zum Start des Installers; danach übernimmt dessen Menü.

Du brauchst einen Linux-Zielserver, dessen IP und Benutzernamen, SSH-Zugang und Root-/sudo-Rechte sowie Zugriff auf [Hue2Lox auf GitHub](https://github.com/square-com-de/hue2lox). Der Download ist ohne GitHub-Konto möglich. Passwörter nur im Terminal eingeben. Unterstützte Systeme und Hilfe bei fehlendem SSH oder sudo stehen in der [Installationsanleitung](INSTALL.md).

## Prompt zum Kopieren

```text
Hilf mir, den Hue2Lox-Installer zu starten. Halte es einfach und führe mich
Schritt für Schritt durch genau diesen Ablauf:

1. Frage zuerst, auf welchem Linux-Gerät Hue2Lox laufen soll: Betriebssystem,
   IP/Hostname und Benutzername. Frage auch, ob mein Arbeitsgerät ein Mac
   oder Windows-PC ist. Warte auf die fehlenden Antworten. Mein Arbeitsgerät
   ist nicht automatisch das Installationsziel.
2. Lass mich auf dem Arbeitsgerät https://github.com/square-com-de/hue2lox öffnen
   und über Code → Download ZIP das aktuelle hue2lox-main.zip herunterladen.
   Wenn die Datei schon vorhanden ist, verwende sie ohne Umbenennung.
3. Gib mir den passenden scp-Befehl, um das ZIP vom Arbeitsgerät in den
   persönlichen Ordner auf dem Zielserver zu kopieren, und den SSH-Befehl
   zum Anmelden. Setze meine tatsächlichen Angaben ein.
4. Auf dem Zielserver: Falls unzip oder sudo fehlt beziehungsweise die
   Berechtigung fehlt, hilf nur bei dieser Voraussetzung anhand von
   https://github.com/square-com-de/hue2lox/blob/main/INSTALL.md.
   Entpacke das ZIP nach ~/hue2lox-installer. Bei vorhandenem Ordner oder
   Fehler erst klären, nichts überschreiben und nicht einfach fortfahren.
5. Starte auf dem Zielserver:
   sudo bash "$HOME/hue2lox-installer/hue2lox-main/install-assistant.sh"
   Falls ich als Root arbeite, verwende ohne sudo den tatsächlichen Pfad
   im Benutzerordner, nicht /root. Danach übernimmt das Installer-Menü.

Beschrifte jeden Befehlsblock mit ARBEITSGERÄT oder ZIELSERVER.
Gib jeweils nur den nächsten Schritt und warte auf mein Ergebnis.
Keine Git-Befehle, Versionsauswahl oder Quellcodeprüfung. Keine eigene
Docker-Installation durch die KI: Das erledigt der Installer.
Fordere keine Passwörter, Tokens oder privaten Schlüssel im Chat an.
Antworte auf Deutsch.
```

**Teststatus:** Der vereinfachte KI-Ablauf muss noch in einem neuen Chat getestet werden. Die bereits bestätigten Systemtests stehen in [INSTALL.md](INSTALL.md).
