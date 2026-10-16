# thermoctl

Sensorbasierte Raumregelung mit Zeitplänen, konfigurierbar über eine eigene
Weboberfläche — dazu ansprechbar über REST-API und MCP-Server. Der Quelltext steht
unter der [AGPL-3.0](https://www.gnu.org/licenses/agpl-3.0.html) und liegt vollständig
unter <https://github.com/MagicalWig34653/thermoctl>.

## So sieht es aus

Eine gemeinsame Oberfläche für Bewohner und Verwaltung: Welche Bereiche und Aktionen
sichtbar sind, folgt den Rechten der Person. Die Übersicht am Rechner, mit Navigation links —

![Übersicht der neuen Oberfläche am Rechner mit Navigation links, Statuskarten, Kennzahlen und Anlagenstatus](https://raw.githubusercontent.com/MagicalWig34653/thermoctl/main/docs/bilder/anlage-startseite.png)

— und dieselbe Übersicht auf dem Telefon:

![Übersicht auf dem Handy mit Hinweis zum Notbetrieb und Kennzahlen zu Räumen, Heizanforderung und Auffälligkeiten](https://raw.githubusercontent.com/MagicalWig34653/thermoctl/main/docs/bilder/wohnung-startseite-mobil.png)

Dazu eine Kioskansicht für ein Wandtablet, hinter einem eigenen, widerrufbaren Token:

![Kioskansicht mit Raumkacheln, je mit Ist-Temperatur, Sollwert und Plus-/Minus-Tasten sowie Umschaltern für Ansicht](https://raw.githubusercontent.com/MagicalWig34653/thermoctl/main/docs/bilder/kiosk-dashboard.png)

Für kleine Wandtablets (480×480, z. B. Sonoff NSPanel Pro Gen2) gibt es zusätzlich eine
kompakte Panel-Ansicht: alle Zonen als Raster, ein Antippen öffnet die Zone im Detail.
Umschaltbar über `?ansicht=panel`, `?ansicht=tafel` oder `?ansicht=auto` (Vorgabe).

Eine ausführliche Bedienungsanleitung mit weiteren Bildern steht
in [`docs/bedienung.md`](https://github.com/MagicalWig34653/thermoctl/blob/main/docs/bedienung.md)
des Hauptrepositories.

## Wichtig, bevor Sie anfangen

**thermoctl steuert eine echte Heizung.** Es ist keine Simulation und kein Spielzeug —
Fehler in der Konfiguration können dazu führen, dass Räume nicht beheizt werden oder
Ventile falsch schalten. Lesen Sie diese Seite vollständig, bevor Sie das Add-on
scharf schalten.

**Trockenlauf ist die Vorgabe.** Nach der Installation entscheidet thermoctl zunächst,
ohne tatsächlich zu schalten — es protokolliert nur, was es täte. Das gibt Ihnen
Gelegenheit, die Regelentscheidungen gegen Ihr bisheriges System zu vergleichen, bevor
irgendetwas an einem echten Ventil oder einer echten Steckdose passiert. **Das
Scharfschalten braucht einen Neustart des Add-ons**, nachdem Sie die entsprechende
Einstellung in der Weboberfläche geändert haben — es genügt nicht, den Schalter in der
Oberfläche umzulegen und weiterzumachen.

**thermoctl hat eine eigene Anmeldung, unabhängig von Ihrer Home-Assistant-Anmeldung.**
Auch mit eingeschaltetem Ingress ersetzt Ingress diese Anmeldung nicht — Sie melden
sich also zweimal an: einmal bei Home Assistant, um über die Seitenleiste ins Add-on zu
gelangen, und ein zweites Mal bei thermoctl selbst, mit einem eigenen Benutzerkonto.
Das erste Konto legen Sie beim ersten Öffnen der Oberfläche an. Der Eintrag in der
Seitenleiste erscheint seit 0.9.5 jedem Home-Assistant-Nutzer, nicht nur
Administratoren — ohne thermoctl-Konto kommt aber niemand über die Anmeldeseite hinaus.

![Anmeldeseite von thermoctl mit den Feldern Benutzername und Passwort und der Schaltfläche Anmelden](https://raw.githubusercontent.com/MagicalWig34653/thermoctl/main/docs/bilder/oeffentlich-anmeldung.png)

Es gibt eine gemeinsame Oberfläche; Bereiche und Aktionen folgen den Rechten der
Person. Das Gruppenfeld „UI-Profil“ (Anlage oder Wohnung) gibt es weiterhin: Eine Person
gilt als Mieter, wenn sie mindestens einer Gruppe angehört und alle ihre Gruppen das
Wohnungsprofil haben; das Profil trennt weiterhin die Verwaltungsbereiche (Geräte, Betrieb und Einstellungen, Personen und Gruppen, Berichte, Urlaub, Modi) vom Wohnbereich: Ein Konto mit Wohnungsprofil sieht sie auch mit passendem Recht nicht. Was jemand
darf, bestimmen weiterhin die Rechte. Beim Upgrade behalten alle bestehenden Gruppen das
Anlagenprofil, auch eine Gruppe namens „Mieter“. Für eine Mietergruppe setzen Sie das
UI-Profil in der Gruppenverwaltung von thermoctl ausdrücklich auf Wohnung. Das Recht
`report.create` für Problemmeldungen müssen Sie ebenfalls ausdrücklich vergeben — keine
bestehende Gruppe erhält es beim Upgrade automatisch.

## Installation

1. Fügen Sie dieses Repository unter *Einstellungen → Add-ons → Add-on-Store → ⋮ →
   Repositories* hinzu.
2. Installieren Sie das Add-on **thermoctl** aus der Liste.
3. Öffnen Sie den Reiter *Konfiguration* und tragen Sie mindestens einen
   Sicherheitsschlüssel (`secret_key`, mindestens 32 Zeichen — erzeugen lässt sich
   einer z. B. mit `python3 -c "import secrets; print(secrets.token_urlsafe(48))"` in
   einem beliebigen Terminal) ein.
4. Starten Sie das Add-on und öffnen Sie es über die Seitenleiste. Legen Sie beim
   ersten Aufruf das erste thermoctl-Benutzerkonto an.
5. Richten Sie Räume, Geräte und Zeitpläne in der thermoctl-Oberfläche ein, während das
   Add-on noch im Trockenlauf arbeitet.
6. Vergleichen Sie die protokollierten Regelentscheidungen mit Ihrem bisherigen System.
   Erst wenn Sie zufrieden sind: Trockenlauf in der Konfiguration abschalten und das
   Add-on **neu starten** — erst der Neustart schaltet scharf.

## Konfiguration

### Datenbank

Vorgabe ist SQLite in einer Datei unter `/data` — dem Datenverzeichnis des Add-ons, das
Neustarts und Updates übersteht. Für die meisten Haushalte reicht das vollständig.

Wer ohnehin einen MariaDB-Server betreibt (z. B. ein eigenes MariaDB-Add-on oder einen
externen Server), kann `database_type` auf `mariadb` stellen und Host, Port, Benutzer,
Passwort und Datenbankname eintragen. Die Datenbank muss vorher existieren.

### MQTT (Zigbee2MQTT)

Optional, und standardmäßig abgeschaltet. Sobald `mqtt_enabled` an ist, nimmt thermoctl
über den angegebenen Broker nicht nur Sensordaten entgegen, sondern auch Befehle für
alle Zonen — tragen Sie deshalb einen eigenen Broker-Zugang mit eng begrenzten Rechten
für thermoctl ein, nicht Ihren allgemeinen Home-Assistant-Zugang.

Dieses Add-on übernimmt die Zugangsdaten eines im selben Home Assistant laufenden
MQTT-Broker-Add-ons derzeit **nicht automatisch** — tragen Sie Host, Port, Benutzername
und Passwort selbst ein, auch wenn Sie bereits ein MQTT-Add-on installiert haben.

### Meross (Steckdosen als Ventile)

Optional. Ohne E-Mail-Adresse und Passwort bleibt der Meross-Adapter unkonfiguriert und
tut nichts.

### Störungsbenachrichtigung

Optional. Ohne eingetragene Webhook-Adresse geht eine Störungsmeldung nur ins
Add-on-Protokoll, nicht nach außen.

### Notbetrieb bei Sensorausfall

Seit 0.11.0 ist der Notbetrieb für jede Zone automatisch aktiv: Fällt der Raumfühler aus
und gibt es keine brauchbare Ersatzquelle, takten Fußbodenkreise, und Heizkörper-Thermostate
werden einmal auf `manual` mit Notsollwert gestellt. Einstellbar unter „Regelvorgaben“
(anlagenweit) und „Zonen → Regelparameter“ (je Zone, dort auch abschaltbar). Meldungen
laufen über den Störungs-Webhook, abschaltbar mit `notify_sensor_faults`.

### MCP-Server über HTTP

Optional, standardmäßig **aus** (`mcp_mode` steht auf `off`) — ohne Einstellung ändert
sich nichts. Werkzeuge und Rechte sind dieselben wie im stdio-Betrieb; die Anmeldung
erfolgt per Bearer-Token (unter `/tokens`) oder per OAuth. Die Felder:

| Feld | Bedeutung |
|---|---|
| `mcp_mode` | `off` (Vorgabe), `path` oder `port` |
| `mcp_path` | nur `path`: Pfad des Endpunkts unter der Weboberfläche; leer heißt `/mcp` |
| `mcp_port` | nur `port`: Port des zweiten Prozesses; Vorgabe `8001` |
| `public_url` | öffentliche Adresse der Weboberfläche, Pflicht bei `path` und `port` |
| `mcp_public_url` | öffentliche Adresse des MCP-Ports, Pflicht bei `port`; bei `path` optional |

**Wichtig: Ingress taugt dafür nicht.** Ingress verlangt eine Home-Assistant-Anmeldung, die
ein externer MCP-Client nicht leisten kann. Der Zugang geht über die direkt
veröffentlichten Ports, mit einem eigenen Reverse Proxy, der TLS beendet. Die
eingetragenen Adressen müssen die **öffentlichen** (`https`) sein, unter denen der Proxy
antwortet; `http` ist nur für `localhost` zulässig. Der Proxy muss den `Host`-Header
unverändert weitergeben und die Pfade unter `/.well-known/` durchlassen.

**Betriebsart `path`:** MCP liegt unter einem Pfad der Weboberfläche und nutzt den
vorhandenen Port 8000. Eintragen:

- `mcp_mode`: `path`
- `public_url`: `https://<adresse-unter-der-die-weboberfläche-öffentlich-erreichbar-ist>`
- `mcp_path`: nur nötig, wenn nicht `/mcp` gelten soll, z. B. `/<eigener-pfad>`

Der MCP-Endpunkt ist dann `<public_url><mcp_path>`.

**Betriebsart `port`:** MCP läuft als zweiter Prozess auf eigenem Port. Eintragen:

- `mcp_mode`: `port`
- `mcp_port`: `8001`
- `public_url`: `https://<adresse-unter-der-die-weboberfläche-öffentlich-erreichbar-ist>`
- `mcp_public_url`: `https://<öffentliche-adresse-des-mcp-ports>`

Zusätzlich den Port `8001` unter „Add-on → Konfiguration → Netzwerk“ freigeben; er ist
standardmäßig nicht veröffentlicht. **Der Container-Port dort muss zu `mcp_port`
passen:** Wer einen anderen Wert in `mcp_port` einträgt, braucht auch eine andere
Port-Zuordnung, sonst erreicht niemand den Dienst. Die Zustimmungsseite von OAuth bleibt
in der Weboberfläche (`public_url`).

Eine unvollständige oder unzulässige Angabe verhindert den Start des Add-ons mit einer
Meldung im Protokoll, die das betroffene Feld nennt. Die Einstellungen im Einzelnen:
`docs/mcp.md` und `docs/self-hosting.md` (Abschnitt 8c) im
[Anwendungsprojekt](https://github.com/MagicalWig34653/thermoctl).

## Grenzen dieser Fassung

- Passkeys/WebAuthn lassen sich über `passkey_rp_id`, `passkey_rp_name` und
  `passkey_origin` einstellen; hinter Ingress ist der Hostname von Home Assistant
  maßgeblich, weil der Browser dessen Adresse sieht.
- Der MCP-Server im **stdio**-Betrieb läuft nicht als Teil dieses Add-ons, sondern
  außerhalb (dafür das Feld `mcp_token`). Der **HTTP**-Betrieb ist im Add-on möglich,
  siehe „MCP-Server über HTTP“.

## Support

Fehler und Fragen bitte als Issue im Quelltext-Repository:
<https://github.com/MagicalWig34653/thermoctl/issues>.

## Wenn ein Feld fehlt

Nicht jede Einstellung von thermoctl hat ein eigenes Feld in dieser Oberfläche. Für
alles Übrige gibt es **`env`**: Dort hinein kommt der Inhalt einer `.env`, so wie man
sie auch neben `docker compose` legen würde — eine Zuweisung je Zeile:

```
THERMOCTL_MEROSS_EMAIL=ich@example.org
THERMOCTL_NOTIFY_WEBHOOK=https://beispiel.invalid/haken
# Zeilen mit Rautenzeichen werden übersprungen
```

Diese Zuweisungen gelten **nach** den Feldern darüber und dürfen sie überschreiben.
Welche Namen es gibt, steht in der `.env.example` des
[Anwendungsprojekts](https://github.com/MagicalWig34653/thermoctl).

**Achtung:** Was Sie hier eintragen, steht im Klartext in der Add-on-Konfiguration —
genau wie die übrigen Felder auch. Ein Passwort gehört trotzdem lieber in das dafür
vorgesehene Feld, wo der Supervisor es wenigstens in der Anzeige verdeckt.
