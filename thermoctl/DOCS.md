# thermoctl

Sensorbasierte Raumregelung mit Zeitplänen, konfigurierbar über eine eigene
Weboberfläche — dazu ansprechbar über REST-API und MCP-Server. Der Quelltext steht
unter der [AGPL-3.0](https://www.gnu.org/licenses/agpl-3.0.html) und liegt vollständig
unter <https://github.com/MagicalWig34653/thermoctl>.

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
Das erste Konto legen Sie beim ersten Öffnen der Oberfläche an.

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

## Grenzen dieser Fassung

- Passkeys/WebAuthn sind über dieses Add-on nicht einstellbar.
- Der MCP-Server läuft nicht als Teil dieses Add-ons.

Beides ist bewusst nicht Teil dieser ersten Add-on-Fassung — siehe das begleitende
`CHANGELOG.md` und der Bericht zur Aufgabe, die dieses Repository angelegt hat.

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
