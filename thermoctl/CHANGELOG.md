# Änderungen (Add-on)

Änderungen an der Add-on-Verpackung selbst -- nicht an thermoctl. Für die Anwendung
siehe das `CHANGELOG.md` im Hauptrepository (<https://github.com/MagicalWig34653/thermoctl>).

## Unveröffentlicht

- Erste Fassung des Add-ons: `config.yaml` für `thermoctl:0.6.1`, Architekturen
  `amd64`/`aarch64`, Ingress mit eigener Anmeldung, Optionen für Datenbank
  (SQLite/MariaDB), MQTT, Meross und Störungs-Webhook.

## 0.11.1

- Zeigt jetzt auf `thermoctl:0.11.1`.
- **Wichtig, wenn du unter 0.11.0 Ausgleichswerte für Thermostate gesetzt hast:** Das
  Formular unter Zonen → Regelparameter zeigte sie nicht an, und ein Speichern der Seite
  (Berechtigung `device.manage`) löschte sie still. Das ist behoben: Der gespeicherte Wert
  steht im Feld, ein Speichern ohne Änderung lässt ihn stehen. **Wer die Seite unter 0.11.0
  gespeichert hat, muss die Ausgleichswerte einmal neu eintragen.** Ein leeres Feld entfernt
  den Wert weiterhin (die Zone rechnet dann wie mit 0 K), das steht jetzt als Hinweis am Feld.
- Der Notbetriebs-Hinweis nennt bei Zonen mit Thermostat und Fußbodenkreis beide
  Verhaltensweisen („Thermostat regelt selbst; Fußboden taktet 10/20 min").
- Entscheidungsgründe lesen sich einheitlich (Dezimalkomma, Leerzeichen vor der Einheit); bei
  der PI-Regelung heißt es „Abweichung" statt „Fehler", der Tastgrad steht gerundet in
  Prozent. Nur Text, die Regelung ist unverändert.
- Schaltprotokoll: Lange Ergebnis- und Begründungstexte laufen bei breiten Bildschirmen nicht
  mehr über ihre Spalte hinaus.
- Beim Upgrade nichts zu tun: keine Migration, keine neue Einstellung, keine neuen Optionen.

## 0.11.0

- Zeigt jetzt auf `thermoctl:0.11.0`.

### ⚠ Verhaltensänderung beim Upgrade

**Der Notbetrieb bei Sensorausfall wird für alle bestehenden Zonen automatisch
aktiviert; neu angelegte Zonen starten ebenfalls damit.** Bis 0.10.1 tat `thermoctl`
bei einem Sensorausfall nichts Eigenes, jetzt greift es ein:

- Fällt in einer Zone der Temperatursensor aus — und gibt es keine brauchbare
  Ersatzquelle über die Thermostat-Thermometer der Zone —, **takten Fußbodenkreise**
  (Vorgabe 10 Minuten an, 20 Minuten aus; nach der Außentemperatur-Kennlinie, sobald
  ein Außenwert vorliegt).
- **Heizkörper-Thermostate werden einmal** auf `manual` und den Notsollwert
  (Vorgabe 20 °C) gestellt und danach nicht mehr angesprochen. Sie regeln dann selbst.
- **Bei Rückkehr** des Sensors wird der vorherige `operating_mode` des Thermostats
  einmal zurückgeschrieben.
- **Meldung** bei Beginn und bei Entwarnung (Schalter `notify_sensor_faults`).

**Wer das für eine Zone nicht will:** unter „Parameter" der Zone
(Zonen → Regelparameter) „Notbetrieb für diese Zone aktivieren" ausschalten.

**Ein Downgrade** (Alembic `downgrade` unter `d4a81c6e5b29`) setzt den Notbetrieb für
**alle** Zonen auf aus; wer ihn vorher von Hand für einzelne Zonen eingeschaltet hatte,
muss ihn nach erneutem Upgrade selbst wieder setzen.

### Neu in der Anwendung

- Ersatzquelle mit Echo-Regel: Bei Ausfall des Raumfühlers gilt die kälteste
  Thermostat-Messung der Zone (Ausgleichswert je Thermostat einstellbar). Ein Messwert
  zählt erst 30 Minuten nach dem letzten Sendeversuch an das Thermostat.
- Betriebsseite mit Vergleich Ersatzquelle ↔ Wandfühler und vorgeschlagenem
  Ausgleichswert; Konfiguration über Oberfläche, REST und MCP.
- Eine Störungsmeldung und eine Entwarnung je Episode; nach einem Neustart zwischen
  Markierung und Versand wird einmal wiederholt.

### Korrekturen

- Downgrade-Migrationen vertragen vorhandene Betriebsdaten.
- Das Notbetriebs-Formular speichert ganz oder gar nicht; unvollständige
  Kennlinienzeilen werden abgewiesen.
- Beim Eintritt in den Notbetrieb und bei der Rückkehr zählt die reale
  Mindest-Ein-/Aus-Dauer des Relais.

Migrationen laufen beim Start automatisch (Kopf `e5b92d7f3a18`).

## 0.10.1

- Zeigt jetzt auf `thermoctl:0.10.1`.
- **Zonen → Regelparameter hat nur noch einen Speichern-Knopf.** Der Schalter
  „Fenster aus Temperatursturz erkennen“ stand bisher in einem eigenen Formular;
  wer ihn umlegte und den großen Knopf drückte, verlor die Änderung.
- Die Minus-/Plus-Knöpfe am Sollwert (Übersicht, Wohnungssicht, Kiosk) sitzen jetzt
  unabhängig von der Schrift des Endgeräts mittig; der Knopf auf der Übersicht ist
  auf 44 px Tippfläche gewachsen.
- **PI-Regelung (Beta), nur relevant für Zonen mit eingeschaltetem PI:**
  - Ein veralteter Raumfühler wurde übersehen, solange gleichzeitig die
    Mindestschaltdauer der Hysterese griff — PI regelte dann mit dem alten Messwert
    weiter. Jetzt fällt die Zone in diesem Fall wie jede andere auf die
    Sicherheitsregel zurück.
  - Eine Phase, die unter Hysterese begonnen hat, hält deren Mindestdauer auch dann,
    wenn PI währenddessen übernimmt (etwa nach Sensorrückkehr, Fenster zu, Ende des
    Aus-Modus).
  - Der Entscheidungsgrund nannte die Hysterese-Mindestdauer, obwohl PI schaltete.
- Beim Upgrade nichts zu tun: keine Migration, keine neue Einstellung, keine neuen
  Optionen.

## 0.10.0

- Zeigt jetzt auf `thermoctl:0.10.0`.
- **Neu: eine zweite, kompakte Kiosk-Ansicht für kleine Wandtabletts
  (480×480, z. B. Sonoff NSPanel Pro Gen2).** Neben der bisherigen,
  scrollenden Tafel-Darstellung gibt es jetzt ein festes 2-Spalten-Raster mit
  allen Zonen auf einen Blick und einen flächendeckenden Detailbereich je
  Zone. Umschaltbar über `?ansicht=panel`/`?ansicht=tafel`/`?ansicht=auto`
  (Vorgabe: automatisch nach Bildschirmbreite), gemerkt in einem eigenen
  Cookie (`thermoctl_kiosk_ansicht`) -- ohne Einfluss auf Token, Rechte oder
  Sitzung.
- Ein zweiter, schneller Tipp auf "Sollwert anheben" am Kiosk-Wandtablett
  konnte bisher wirkungslos verschwinden. Der Knopf sperrt sich jetzt
  sichtbar für die Dauer der eigenen Anfrage.
- Auf „Bediengeräte" gingen gespeicherte Kanaleinstellungen (Kanalart,
  Quellgerät, Zone, fester Text/feste Zahl) beim nächsten Laden verloren
  oder zeigten einen falschen Wert an -- behoben. Eine feste Zahl mit
  mehreren Nachkommastellen wird jetzt ungerundet angezeigt.
- `/tokens` und `/kiosk-tokens` stürzten mit Serverfehler ab, wenn die
  Gültigkeitsdauer keine Zahl war -- zeigen jetzt eine Fehlermeldung im
  Formular.
- Die mobile Navigation der Anlagensicht öffnete außerhalb des Sichtbereichs,
  wenn die Seite zuvor gescrollt war. Der Kopfzeilen-Knopf „Navigation" ist
  entfernt; „Mehr" ist jetzt der einzige mobile Zugang und öffnet die
  Seitenleiste als feste Schublade über dem Inhalt, unabhängig von der
  Scrollposition.
- Mehrere behobene Zeilenumbrüche mitten im Wort und zu enge Spalten in
  Tabellen (Schaltprotokoll, Benutzer, Geräte, Zonen, Schnittstellen,
  Einstellungen, Gruppen, Tokens, Kiosk-Tokens, Audit-Protokoll,
  Bediengeräte, Geräte-Zuordnung) bei 1280 px und 390 px.
- Zwei Knöpfe am Kiosk-Wandtablett ("Nächste Schaltung vorziehen",
  "Übersteuerung aufheben") kamen auf 42 statt 44 px Mindestgröße für ein
  Tippziel -- betraf jeden Knopf im Programm, nicht nur diese zwei.
- Die README und zwei neue Anleitungen (`docs/bedienung.md` für den
  Betreiber, `docs/wohnung.md` zum Weitergeben an Bewohner) zeigen jetzt
  Bildschirmfotos der Oberfläche.
- Beim Upgrade nichts zu tun: keine neue Migration, keine neue Einstellung,
  keine Änderung an Rechten oder Gruppen. An der Verpackung selbst ändert
  sich nichts: keine neuen Optionen. Neu ist ein Cookie
  (`thermoctl_kiosk_ansicht`), das ohne Zutun beim ersten Wechsel der
  Kiosk-Ansicht entsteht.

## 0.9.5

- Zeigt jetzt auf `thermoctl:0.9.5`. An der Anwendung ändert sich gegenüber 0.9.4
  nichts — die neue Nummer gibt es nur, weil Home Assistant eine geänderte
  `config.yaml` erst mit einer neuen Version übernimmt.
- **Der Eintrag in der Seitenleiste ist jetzt für alle Home-Assistant-Nutzer
  sichtbar, nicht nur für Administratoren** (`panel_admin: false`). Bisher galt die
  Vorgabe des Supervisors, und wer in Home Assistant kein Administrator war, sah
  thermoctl gar nicht. Wer was darf, entscheidet weiterhin allein thermoctls eigene
  Anmeldung — Home Assistant zeigt nur den Weg dorthin. Wer den Eintrag bewusst nur
  Administratoren zeigen will, kann das in Home Assistant nicht je Nutzer
  einstellen; das Add-on müsste dann `panel_admin: true` tragen.
- Beim Upgrade sonst nichts zu tun: keine neue Migration, keine neue Einstellung, keine
  Änderung an Rechten oder Gruppen. Keine neuen Optionen.

## 0.9.4

- Zeigt jetzt auf `thermoctl:0.9.4`. **Wer Meross-Steckdosen schaltet, sollte
  aktualisieren.**
- Behoben: thermoctl sperrte sich selbst aus der Meross-Cloud aus und kam ohne Zutun
  nicht wieder heraus. Ein gescheiterter Schaltbefehl verwarf die Sitzung, der nächste
  Regelzyklus meldete sich neu an, die Cloud lehnte wegen zu häufiger Anmeldungen ab —
  und von vorn, alle 32 Sekunden. Jetzt wartet eine abgelehnte Anmeldung, verdoppelnd
  von einer Minute bis höchstens dreißig.
- Geräteabgleich und Schaltweg teilen sich jetzt eine Sitzung: von rund 28 auf rund 4
  Anmeldungen am Tag.
- Der Grund einer abgelehnten Anmeldung steht jetzt im Schaltprotokoll, nicht nur im
  Add-on-Protokoll. Er trägt nur, was die Cloud selbst gemeldet hat — nie Konto oder
  Passwort.
- Behoben: im Schaltprotokoll brachen Wörter mitten durch.
- **Steckt die Anlage gerade in der Sperre, löst sich das nach dem Update von selbst.**
  Die Wartezeit lässt die Sperre ablaufen, statt sie weiter zu erneuern.
- Beim Upgrade sonst nichts zu tun: keine neue Migration, keine neue Einstellung, keine
  Änderung an Rechten oder Gruppen. An der Verpackung ändert sich nichts: keine neuen
  Optionen.

## 0.9.3

- Zeigt jetzt auf `thermoctl:0.9.3`. Nachtrag zu 0.9.2: dieselbe Ursache, die zweite
  Stelle. **Wer die Betriebsseite benutzt, sollte aktualisieren.**
- Behoben: Die Betriebsseite las noch immer die gesamte Entscheidungshistorie aller
  Räume, die die Übersicht in 0.9.2 schon losgeworden war. Gemessen an zehn Räumen mit
  dreißig Tagen Historie: 5,1 Sekunden für diese eine Abfrage, jetzt 0,14 Sekunden.
  Die Abfrage steht jetzt nur noch an einer Stelle, damit sich das nicht ein drittes
  Mal wiederholt.
- Die Regelung selbst ist unberührt: schneller abgefragt, nicht anders entschieden.
- Beim Upgrade ist nichts zu tun: keine neue Migration, keine neue Einstellung, keine
  Änderung an Rechten oder Gruppen.
- An der Verpackung selbst ändert sich nichts: keine neuen Optionen.

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
