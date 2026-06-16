#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Conversion du CV HTML d'Élodie SIGUENZA en PDF A4 (une page, prêt à imprimer).

Privilégie Playwright/Chromium (rendu fidèle des aplats de couleur et des
masques SVG). Bascule automatiquement sur WeasyPrint si Playwright n'est pas
disponible.

Pré-requis (au choix) :
    pip install playwright && playwright install chromium
    # ou
    pip install weasyprint

Usage :
    python convert_to_pdf.py
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent
HTML = HERE / "cv_elodie.html"
PDF = HERE / "cv_elodie.pdf"


def with_playwright() -> bool:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return False

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(HTML.as_uri(), wait_until="networkidle")
        page.emulate_media(media="print")
        page.pdf(
            path=str(PDF),
            format="A4",
            print_background=True,          # conserve les aplats de couleur
            prefer_css_page_size=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )
        browser.close()
    return True


def with_weasyprint() -> bool:
    try:
        from weasyprint import HTML as WeasyHTML
    except ImportError:
        return False

    WeasyHTML(filename=str(HTML)).write_pdf(str(PDF))
    return True


def main() -> None:
    if not HTML.exists():
        raise SystemExit(f"Fichier introuvable : {HTML}")

    if with_playwright():
        print(f"[OK] PDF généré via Playwright/Chromium : {PDF}")
    elif with_weasyprint():
        print(f"[OK] PDF généré via WeasyPrint : {PDF}")
    else:
        raise SystemExit(
            "Aucun moteur de rendu disponible.\n"
            "  pip install playwright && playwright install chromium\n"
            "  ou : pip install weasyprint"
        )


if __name__ == "__main__":
    main()
