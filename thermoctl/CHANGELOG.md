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
