# Security / Sicherheit

Hue2Lox is currently a development project; there is no released version with a security support commitment yet. It is intended for a trusted local network. Do not expose the admin interface directly to the Internet.

Fresh installations generate their own control token and TLS key. The initial login is `admin` / `admin`; change it in the web interface before wider use. Keep private backups protected. Use a verified certificate or trust setup; do not permanently disable TLS verification.

Do not report credentials, unredacted HTTP headers, private keys or exploitable vulnerability details in a public issue. Use GitHub private vulnerability reporting if enabled for this repository; otherwise contact the maintainer through an existing private channel before sharing details. No response-time guarantee is offered.

If a token or key was exposed, remove the exposure and replace the affected credential. Deleting the current file alone does not remove it from Git history. Review history separately before publication.

Deutsch: Sicherheitsprobleme vertraulich melden. Keine Tokens, Passwörter oder privaten Schlüssel in Issues, Screenshots oder Logs veröffentlichen. Das Standardpasswort nach der Einrichtung ändern; die Oberfläche nicht direkt ins Internet stellen.
