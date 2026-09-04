# Symbol und Logo

`icon.png` (128 × 128) und `logo.png` (250 × 100) liegen neben dieser Datei und sind
mit `../werkzeuge-bilder.py` erzeugt — dem Chromium, das im Anwendungsprojekt ohnehin
für die Browsertests da ist. Wer sie ändern will, ändert das Skript und lässt es neu
laufen, statt die PNG von Hand zu bearbeiten.

## Was dargestellt ist

Ein Thermostat-Zifferblatt: eine Skala von kühl nach warm, der Zeiger im warmen
Drittel. Die Farben stammen aus dem Stylesheet der Anwendung (`thermoctl.css`) —
warm `#e8834f`, kühl `#79aecd`, Schiefer `#2b343b`.

## Warum sie unterschiedlich aufgebaut sind

- **`icon.png` hat einen transparenten Rand und eine gefüllte Scheibe.** Home Assistant
  beschneidet das Symbol in der Seitenleiste auf einen Kreis; ein randloses Motiv würde
  dabei angeschnitten.
- **`logo.png` bringt seine eigene Fläche mit**, statt transparent zu sein. Es erscheint
  im Add-on-Store je nach Design auf hellem oder dunklem Hintergrund — eine
  schiefergraue Schrift auf transparentem Grund wäre im dunklen Design unsichtbar.

Beides ist ein tragfähiger Anfang, kein Ergebnis eines Gestaltungsprozesses. Wer ein
richtiges Zeichen entwirft, ersetzt beide Dateien.
