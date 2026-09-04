# thermoctl — Home-Assistant-Add-on

Dieses Repository ist ein **Add-on-Repository für Home Assistant**. Es enthält keinen
Anwendungscode — der liegt unter
<https://github.com/MagicalWig34653/thermoctl> und steht unter der AGPL-3.0.

## Installieren

1. In Home Assistant: **Einstellungen → Add-ons → Add-on-Store**
2. Oben rechts **⋮ → Repositories**
3. Diese Adresse eintragen:
   ```
   https://github.com/MagicalWig34653/thermoctl-addon
   ```
4. Nach dem Neuladen erscheint **thermoctl** im Store.

Was das Add-on tut, was es voraussetzt und was **vor dem Scharfschalten** zu beachten
ist, steht in [`thermoctl/DOCS.md`](thermoctl/DOCS.md) — dieselbe Seite, die Home
Assistant im Store anzeigt.

## Warum ein eigenes Repository

Der Add-on-Store fragt dieses Repository regelmäßig ab. Hier liegen nur die paar
Dateien, die Home Assistant dafür braucht; das Anwendungsprojekt bleibt davon
unberührt. Die Versionsnummer in `thermoctl/config.yaml` zeigt auf ein Abbild unter
`ghcr.io`, das im Anwendungsprojekt gebaut wird.

## Voraussetzung

Home Assistant **OS** oder **Supervised**. Wer Home Assistant Container oder Core
betreibt, hat keinen Add-on-Store und startet thermoctl direkt als Container — die
Anleitung dafür steht im Anwendungsprojekt.
