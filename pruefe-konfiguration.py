#!/usr/bin/env python3
"""Prueft config.yaml gegen die Regeln, an denen der Supervisor das Speichern ablehnt.

Zweimal ist die Add-on-Konfiguration beim ersten echten Ausfuellen gescheitert --
einmal an einem leeren Vorgabewert fuer ein URL-Feld ("expected a URL"), einmal an
einer im Schema genannten Gruppe ohne Vorgabe ("Missing option 'notify' in root").
Beide Male war der Fehler in dieser Datei mit blossem Auge nicht zu sehen.

Aufruf: python3 pruefe-konfiguration.py
Rueckgabe 0, wenn nichts zu beanstanden ist.
"""
import sys
from pathlib import Path

import yaml

KONFIGURATION = Path(__file__).parent / "thermoctl" / "config.yaml"


def pruefe(schema: dict, optionen: dict, pfad: str = "") -> list[str]:
    probleme: list[str] = []
    for schluessel, typ in schema.items():
        wo = f"{pfad}{schluessel}"
        if isinstance(typ, dict):
            # Eine Gruppe ist immer Pflicht. Das Fragezeichen macht einzelne Felder
            # optional, nie die Gruppe -- eine leere Gruppe in den Vorgaben ist der
            # Weg, sie vorhanden und trotzdem unausgefuellt zu lassen.
            if schluessel not in optionen:
                probleme.append(f"Gruppe '{wo}' fehlt in den Vorgaben")
            else:
                probleme += pruefe(typ, optionen[schluessel] or {}, wo + ".")
            continue
        if not str(typ).rstrip(")").endswith("?") and schluessel not in optionen:
            probleme.append(f"Pflichtfeld '{wo}' ({typ}) fehlt in den Vorgaben")
        if optionen.get(schluessel) == "" and str(typ).startswith(("url", "port", "int", "float")):
            probleme.append(f"'{wo}' hat den leeren Vorgabewert \"\", Typ {typ} laesst das nicht zu")
    return probleme


def main() -> int:
    geladen = yaml.safe_load(KONFIGURATION.read_text(encoding="utf-8"))
    probleme = pruefe(geladen["schema"], geladen["options"])
    for zeile in probleme:
        print(zeile)
    if not probleme:
        print("Keine Verstoesse gegen die Supervisor-Regeln gefunden.")
    return 1 if probleme else 0


if __name__ == "__main__":
    sys.exit(main())
