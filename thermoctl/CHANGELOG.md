# Änderungen (Add-on)

Änderungen an der Add-on-Verpackung selbst -- nicht an thermoctl. Für die Anwendung
siehe das `CHANGELOG.md` im Hauptrepository (<https://github.com/MagicalWig34653/thermoctl>).

## Unveröffentlicht

- Erste Fassung des Add-ons: `config.yaml` für `thermoctl:0.6.1`, Architekturen
  `amd64`/`aarch64`, Ingress mit eigener Anmeldung, Optionen für Datenbank
  (SQLite/MariaDB), MQTT, Meross und Störungs-Webhook.

## 0.6.2

Die erste Fassung, die als Add-on wirklich läuft. Zuvor las das Abbild die
Konfiguration des Add-ons gar nicht, und der Ingress-Pfad blieb leer.

- Alle Optionen sind jetzt flache Felder statt verschachtelter Gruppen — daran war
  das Speichern der Konfiguration mehrfach gescheitert.
- Neues Feld **`env`**: der Inhalt einer `.env`, eine Zuweisung je Zeile. Damit lässt
  sich jede Einstellung setzen, auch eine ohne eigenes Formularfeld.
- MQTT-**Client-ID** und **CA-Zertifikat** sind einstellbar — nötig an einem Broker,
  dessen Rechteregeln an der Client-ID hängen.
- Das Abbild gibt es jetzt für `amd64` **und** `arm64`, läuft also auch auf einem
  Raspberry Pi.

## 0.6.3

- **Störungsmeldungen lassen sich einzeln abschalten** — Sensorstörung, Brücke oder
  Broker weg, und neu: Schaltbefehl gescheitert. Alle drei sind ab Werk an.
- **Ein Testknopf für den Webhook** in den Einstellungen: Er schickt eine echte, als
  Test gekennzeichnete Meldung und zeigt sofort, was zurückkam. Daneben steht, wann
  zuletzt zugestellt wurde und ob es ankam.
- Das Kiosk-Dashboard nennt jetzt ebenfalls den Quelltext (AGPL-3.0).

## 0.6.4

- **Behoben: Das Add-on startete nicht.** Es kam an die eigene Konfiguration nicht
  heran — der Supervisor legt sie als `root` ab, das Abbild lief als unprivilegierter
  Benutzer. Der Dienst selbst läuft weiterhin unprivilegiert.

## 0.7.0

- **Eine per Boost ausgelöste Übersteuerung lässt sich jetzt aufheben.** Das Kiosk
  hat dafür einen eigenen Knopf, sichtbar solange eine läuft, und Home Assistant
  bekommt einen Knopf samt Anzeige, ob überhaupt eine Übersteuerung aktiv ist.
  **Bereits ausgestellte Kiosk-Token zeigen den Knopf nicht** — sie brauchen dafür
  eine erneute Ausstellung.
- **Störungsmeldungen sind einzeln abschaltbar** und lassen sich mit einem Testknopf
  prüfen, ohne auf einen echten Sensorausfall zu warten.
- **Eine dezente Ladeanzeige** zeigt an, dass eine Anfrage unterwegs ist — spürbar
  hinter dem Ingress-Proxy, der jede Anfrage einen Umweg nehmen lässt.
- Das Kiosk nennt den Quelltext (AGPL-3.0), wie es Paragraf 13 verlangt.

## 0.7.1

- **Ein eigener Reverse Proxy kann jetzt direkt auf thermoctl zeigen**, zusätzlich zum
  Zugang über die Home-Assistant-Seitenleiste. Dafür ist der Container-Port `8000`
  freigegeben; unter *Konfiguration → Netzwerk* lässt er sich ändern oder leersetzen,
  dann bleibt es beim Ingress.
  **Dieser Weg geht an der Anmeldung von Home Assistant vorbei.** Die eigene Anmeldung
  von thermoctl gilt weiterhin, die Verbindung ist aber unverschlüsseltes HTTP, solange
  kein Proxy davor TLS beendet.
- **Passkeys** hängen an einem einzigen Hostnamen: Ist thermoctl über zwei verschiedene
  Namen erreichbar, funktionieren sie nur unter dem konfigurierten. Die Anmeldung mit
  Passwort geht unter beiden.
- Behoben: Die Testmeldung an den Webhook schrieb „Keine Stoerung liegt vor".

## 0.7.2

- **Passkeys und der MCP-Token haben jetzt eigene Felder.** Bisher waren sie nur über
  das freie `env`-Feld erreichbar.
- **Wichtig zu Passkeys hinter der Seitenleiste:** Als *Relying-Party-Id* gehört der
  Hostname hinein, unter dem **Home Assistant** erreichbar ist — nicht der von
  thermoctl. Der Browser sieht die Adresse von Home Assistant, und nur gegen die prüft
  WebAuthn. Ist Home Assistant ausschliesslich über eine blosse IP-Adresse erreichbar,
  können Passkeys dort nicht funktionieren; die Anmeldung mit Passwort bleibt.
- Der MCP-Token ist ein gewöhnliches API-Token. Ihn einzutragen startet **keinen**
  MCP-Server — der läuft als eigener Einstiegspunkt, nicht in diesem Add-on.
