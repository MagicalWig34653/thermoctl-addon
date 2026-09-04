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
