# Änderungen (Add-on)

Änderungen an der Add-on-Verpackung selbst -- nicht an thermoctl. Für die Anwendung
siehe das `CHANGELOG.md` im Hauptrepository (<https://github.com/MagicalWig34653/thermoctl>).

## Unveröffentlicht

- Erste Fassung des Add-ons: `config.yaml` für `thermoctl:0.6.1`, Architekturen
  `amd64`/`aarch64`, Ingress mit eigener Anmeldung, Optionen für Datenbank
  (SQLite/MariaDB), MQTT, Meross und Störungs-Webhook.

## 0.9.2

- Zeigt jetzt auf `thermoctl:0.9.2`. Nachtrag zu 0.9.1: dieselbe Beschwerde über die
  träge Oberfläche, aber die zweite und größere Hälfte der Ursache. **Wer die Anlage
  länger als ein paar Wochen betreibt, sollte aktualisieren** — der Fehler wurde mit
  jedem Betriebstag schlimmer.
- Behoben: Die Übersicht las bei jedem Aufruf die gesamte Entscheidungshistorie aller
  Räume, nur um je Raum den neuesten Eintrag zu behalten. Die Aufbewahrung steht
  vorgabemäßig auf 365 Tage, und die Regelung schreibt je Raum und Zyklus einen
  Eintrag — nach Monaten Betrieb sind das Hunderttausende. Gemessen an zehn Räumen mit
  dreißig Tagen Historie: 5,1 Sekunden vorher, 0,14 Sekunden nachher.
- Die Regelung selbst ist unberührt: schneller abgefragt, nicht anders entschieden.
- Beim Upgrade ist nichts zu tun: keine neue Migration, keine neue Einstellung, keine
  Änderung an Rechten oder Gruppen.
- An der Verpackung selbst ändert sich nichts: keine neuen Optionen.

## 0.9.1

- Zeigt jetzt auf `thermoctl:0.9.1`. Reine Fehlerbehebung, am selben Tag wie 0.9.0.
  **Wer 0.9.0 einsetzt oder im Browser offen hatte, sollte aktualisieren:** veraltetes
  CSS aus dem Browser-Zwischenspeicher traf genau diese Fassung, weil `StaticFiles`
  bislang ohne `Cache-Control` auslieferte und Browser heuristisch cachten.
- Behoben: veraltetes CSS nach einem Update (jede Asset-URL trägt jetzt eine aus
  Versionsnummer und Dateiinhalt gebildete Kennung, `/static` liefert dazu passende
  Cache-Vorgaben, und ein Tab mit noch offener Seite erzwingt bei veralteter Kennung
  eine echte Navigation statt eines Teil-Updates); zähes Laden der Oberfläche
  (Seitenskripte laden nur noch, wenn die jeweilige Seite sie wirklich braucht);
  404-Fehler auf fehlende Source-Maps der mitgelieferten Bibliotheken; eine
  Geräteliste, die wie Zonenkacheln vom Dashboard aussah, dazu eine Seitenleiste und
  eine Kopfleiste, die nicht sauber mitwuchsen.
- Beim Upgrade ist nichts zu tun: keine neue Migration, keine neue Einstellung, keine
  Änderung an Rechten oder Gruppen. Der erste Aufruf nach dem Update lädt die
  Oberfläche einmal vollständig neu, weil sich mit der Versionsnummer auch die
  Kennung aller Asset-URLs ändert — das ist gewollt und genau die Behebung.
- An der Verpackung selbst ändert sich nichts: keine neuen Optionen.

## 0.9.0

- Zeigt jetzt auf `thermoctl:0.9.0`.
- Neu darin: zwei getrennte Weboberflächen für Anlage und Wohnung, gewählt über das
  UI-Profil der Gruppe, mit Zuhause, Zeitplan und Heizzeit in der Wohnungssicht.
- Zur nächsten Schaltzeit springen zieht die nächste Zeitplanphase vor, ohne den
  Wochenplan zu ändern.
- Abwesenheit senkt die eigenen Räume für einen gewählten Zeitraum ab.
- Problemmeldungen nutzen den bereits vorhandenen Störungs-Webhook.
- Ein persönlicher Bereich bündelt Passwort, Passkeys und Sitzungen für beide
  Oberflächen.
- **Beim Upgrade wird keine bestehende Gruppe umklassifiziert:** Jede behält die
  Anlagenoberfläche, auch eine, die „Mieter“ heißt, denn ein Gruppenname bestimmt
  weder Oberfläche noch Rechte. Wer eine Mietergruppe will, setzt das UI-Profil
  ausdrücklich in der Gruppenverwaltung von thermoctl. Auch das neue Recht
  `report.create` bekommt keine bestehende Gruppe automatisch, weil eine Meldung
  nach außen nicht allein aus einem Leserecht folgen darf.
- An der Verpackung selbst hat sich nichts geändert: keine neuen Optionen. Die neuen
  Einstellungen werden in der Weboberfläche gepflegt, nicht in der Add-on-Konfiguration.

## 0.8.2

- Zeigt jetzt auf `thermoctl:0.8.2`. Fehlerbehebung: In 0.8.1 blieb der beim Start
  gesetzte Riegel dauerhaft zu, die Anlage schaltete deshalb nichts und die Oberfläche
  meldete unverändert „Scharf, Neustart fehlt". **Wer 0.8.1 einsetzt, sollte
  aktualisieren.**
- An der Verpackung selbst hat sich nichts geändert: keine neuen Optionen.

## 0.8.1

- Zeigt jetzt auf `thermoctl:0.8.1`. Neu darin: Urlaubsbetrieb, Frostschutz schlägt ein
  offenes Fenster, Zonen an EIN/AUS-Ventilen schalten beim Lüften nicht mehr ab,
  Außentemperatur als wählbare Gerätequelle mit Alarm für ein vergessenes Fenster, und
  eine Fenstererkennung über den Temperatursturz (Vorgabe aus).
- An der Verpackung selbst hat sich nichts geändert: keine neuen Optionen. Die neuen
  Einstellungen werden in der Weboberfläche gepflegt, nicht in der Add-on-Konfiguration.

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

## 0.7.3

- **Die Schnittstellen-Seite liefert die Homebridge-Konfiguration je Zone**, fertig zum
  Kopieren — mit den echten Topics und dem konfigurierten MQTT-Präfix. Zugangsdaten
  stehen nie darin: Homebridge braucht einen eigenen Broker-Zugang mit engen Rechten.

## 0.7.4

- **Behoben: Homebridge nahm die Betriebsart nicht an.** Ein Wechsel von Aus auf Auto
  bewirkte nichts, und ein fehlender Messwert kam als 0 °C an. Beides lag an der
  Konfiguration, die thermoctl ausgibt — **wer sie schon eingerichtet hat, holt sich den
  Block auf der Schnittstellen-Seite neu und ersetzt den alten.**
- An thermoctls eigenen Topics ändert sich nichts; Home Assistant ist nicht betroffen.
