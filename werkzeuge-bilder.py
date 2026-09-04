"""Erzeugt icon.png und logo.png fuer das Home-Assistant-Add-on.

Gerendert mit dem Chromium, das ohnehin fuer die Browsertests da ist -- kein
neues Werkzeug, keine neue Abhaengigkeit. Farben stammen aus thermoctl.css:
warm #b4562f, kuehl #3a6a89, Schiefer #2f3941.
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

WARM, KUEHL, SCHIEFER, HELL = "#e8834f", "#79aecd", "#2b343b", "#ffffff"

def zifferblatt(groesse: int, mitte: float, radius_scheibe: float) -> str:
    """Ein Thermostat-Zifferblatt: Skala von kuehl nach warm, Zeiger im warmen Drittel."""
    m = mitte
    r = radius_scheibe * 0.66          # Radius der Skala
    breite = radius_scheibe * 0.155     # Strichstaerke der Skala
    # 270-Grad-Bogen, offen nach unten: von 135 Grad ueber oben bis 405 Grad.
    import math
    def punkt(grad, faktor=1.0):
        b = math.radians(grad)
        return m + r * faktor * math.cos(b), m + r * faktor * math.sin(b)
    x1, y1 = punkt(135)
    x2, y2 = punkt(45)
    zeiger_x, zeiger_y = punkt(-52, 0.74)    # zeigt nach rechts oben, ins warme Drittel
    return f'''
      <defs>
        <linearGradient id="skala" x1="0" y1="1" x2="1" y2="0">
          <stop offset="0%" stop-color="{KUEHL}"/>
          <stop offset="50%" stop-color="#b9a08f"/>
          <stop offset="100%" stop-color="{WARM}"/>
        </linearGradient>
      </defs>
      <circle cx="{m}" cy="{m}" r="{radius_scheibe}" fill="{SCHIEFER}"/>
      <path d="M {x1:.2f} {y1:.2f} A {r:.2f} {r:.2f} 0 1 1 {x2:.2f} {y2:.2f}"
            fill="none" stroke="url(#skala)" stroke-width="{breite:.2f}"
            stroke-linecap="round"/>
      <line x1="{m}" y1="{m}" x2="{zeiger_x:.2f}" y2="{zeiger_y:.2f}"
            stroke="{HELL}" stroke-width="{breite * 0.52:.2f}" stroke-linecap="round"/>
      <circle cx="{m}" cy="{m}" r="{radius_scheibe * 0.13:.2f}" fill="{HELL}"/>
    '''

ICON = f'''<svg xmlns="http://www.w3.org/2000/svg" width="128" height="128" viewBox="0 0 128 128">
  {zifferblatt(128, 64, 62)}
</svg>'''

LOGO = f'''<svg xmlns="http://www.w3.org/2000/svg" width="250" height="100" viewBox="0 0 250 100">
  <!-- Eigene Flaeche statt transparentem Grund: Das Logo erscheint im Add-on-Store
       je nach Design auf hellem oder dunklem Hintergrund. Schiefergraue Schrift auf
       transparent waere im dunklen Design unsichtbar. -->
  <rect x="0" y="0" width="250" height="100" rx="16" fill="{SCHIEFER}"/>
  <g transform="translate(14,18)">{zifferblatt(64, 32, 31).replace(f'fill="{SCHIEFER}"', 'fill="none"')}</g>
  <text x="92" y="60" font-family="-apple-system, Helvetica Neue, Helvetica, Arial, sans-serif"
        font-size="32" font-weight="600" letter-spacing="-0.4" textLength="146"
        lengthAdjust="spacingAndGlyphs" fill="#eef1f4">thermo<tspan fill="{WARM}">ctl</tspan></text>
</svg>'''

ziel = Path("/Users/linolaske/Documents/Code Projekte/PycharmProjects/thermoctl-addon/thermoctl")
with sync_playwright() as p:
    browser = p.chromium.launch()
    for name, svg, (b, h) in (("icon.png", ICON, (128, 128)), ("logo.png", LOGO, (250, 100))):
        seite = browser.new_page(viewport={"width": b, "height": h}, device_scale_factor=1)
        seite.set_content(f'<body style="margin:0;background:transparent">{svg}</body>')
        seite.screenshot(path=str(ziel / name), omit_background=True)
        seite.close()
        print(name, "geschrieben")
    browser.close()
