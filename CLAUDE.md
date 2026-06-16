# CLAUDE.md — Projet CV Élodie SIGUENZA

## Objectif du projet
Générer un **CV pour Élodie SIGUENZA** au **format A4, prêt à imprimer**, en réutilisant le **gabarit visuel** d'un CV existant (modèle « Leader Webmastering » à deux colonnes avec timeline) mais avec **le contenu d'Élodie** et une **palette de couleurs imposée**.

Le brief détaillé (contenu complet, mise en forme, livrables) se trouve dans **`brief_cv_elodie.md`** à la racine. **Lis ce fichier en premier** avant toute génération.

## Stack technique
- CV en **HTML + CSS** (un fichier `cv_elodie.html`, CSS interne ou `style.css` séparé).
- Conversion en **PDF** via un script (`convert_to_pdf.py`) — privilégier **Playwright/Chromium** ou **WeasyPrint** pour un rendu A4 fidèle.
- Cible : **page unique A4 portrait** (210 × 297 mm).

## Palette de couleurs (NE PAS modifier)
- Primaire : `#000091` (bleu France) — bandeaux, titres de sections, pastilles, nom.
- Secondaire : `#c9191e` (rouge Marianne) — accents, icônes, filets, détails.
- Fond colonne gauche : gris/crème clair (`#f5f5f7`).
- Texte : `#222`.

## Règles de mise en forme
- Mise en page **deux colonnes** : gauche étroite (photo, identité, compétences, outils, langues, infos perso) / droite large (profil, expériences et formations en **timeline verticale**).
- **PAS de section « Centres d'intérêt / Loisirs ».**
- **PAS de système d'étoiles** pour les compétences (présentation sobre : tags ou puces colorées).
- Le **profil d'accroche** est un brouillon : ne pas inventer d'informations supplémentaires sur le parcours.
- Conserver les aplats de couleur à l'impression : `print-color-adjust: exact;` (+ préfixe `-webkit-`).

## Contraintes impératives
- **Une seule page A4** au rendu PDF (vérifier le débordement).
- **Ne jamais inventer** d'expérience, de date, de diplôme ou de loisir absent du brief.
- Prévoir un **emplacement photo** (placeholder si l'image n'est pas fournie).
- Police sobre (Marianne si disponible, sinon Inter / Source Sans / Roboto).

## Livrables attendus
1. `cv_elodie.html`
2. `style.css` (si CSS séparé)
3. `convert_to_pdf.py`
4. `cv_elodie.pdf` (rendu final, une page A4)

## Workflow conseillé
1. Lire `brief_cv_elodie.md`.
2. Construire le HTML/CSS.
3. Générer le PDF avec le script.
4. **Vérifier que le PDF tient sur une page** et que les couleurs sont conservées ; corriger si besoin.
