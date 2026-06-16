# Brief — Génération du CV d'Élodie SIGUENZA (HTML/CSS → PDF, format A4)

## Objectif

Créer un CV pour **Élodie SIGUENZA** en réutilisant la **mise en forme / le gabarit visuel** du CV de Sébastien SIGUENZA (profil « Leader Webmastering », CV à deux colonnes avec timeline), mais avec le **contenu d'Élodie** (parcours administratif et financier) et une **palette de couleurs imposée**.

Le livrable est un CV au **format A4, prêt pour l'impression**, généré en **HTML + CSS**, puis converti en **PDF via un script**.

---

## Contraintes techniques

- Page unique **A4 portrait** (210 × 297 mm), marges maîtrisées pour impression.
- **HTML + CSS** autonomes (un seul fichier `cv_elodie.html`, CSS interne ou fichier `.css` séparé — au choix).
- Polices : utiliser une police web propre et sobre (ex. *Marianne* si dispo, sinon *Inter*, *Source Sans*, *Roboto* ou équivalent système). Pas de dépendance externe bloquante pour l'impression.
- Couleurs et mise en page fidèles à l'impression (`@media print`, `-webkit-print-color-adjust: exact;` / `print-color-adjust: exact;` pour conserver les aplats de couleur).
- **Script de conversion en PDF** : fournir un script (ex. Python avec Playwright/Chromium, ou `wkhtmltopdf`, ou `weasyprint`) qui transforme le HTML en `cv_elodie.pdf` au format A4 sans marges parasites.
- Le rendu PDF doit tenir sur **une seule page**.

---

## Palette de couleurs (imposée)

- **Primaire : `#000091`** (bleu France) → bandeaux, titres de sections, pastilles de timeline, nom.
- **Secondaire : `#c9191e`** (rouge Marianne) → accents, icônes, filets, puces ou détails.
- Fonds neutres : blanc + un gris/crème très clair pour la colonne de gauche (ex. `#f5f5f7` ou `#f6f6f6`) afin de séparer visuellement les deux colonnes.
- Texte courant : gris foncé/noir (`#1a1a1a` ou `#222`).

> Cette palette est la charte de l'État français, cohérente avec le profil d'attachée d'administration.

---

## Gabarit / mise en forme à reproduire (d'après le CV de Sébastien)

Structure **en deux colonnes** :

### Colonne de gauche (étroite, fond clair)
1. **Photo** d'identité en haut (placeholder si non fournie — prévoir un emplacement carré/arrondi).
2. **Bandeau nom + intitulé de poste** : « Élodie SIGUENZA » + sous-titre « Attachée d'administration de l'État » / « Responsable administrative et financière ».
3. **Bloc compétences clés** : liste de compétences. *Ne pas reprendre le système d'étoiles* du CV de Sébastien (profil cadre administratif → présentation plus sobre : tags, ou liste à puces colorées). Voir contenu plus bas.
4. **Bloc « Informatique / Outils »** : type tags (Word, Excel, PowerPoint, Chorus Pro, GFC, DEMACT…).
5. **Langues** : anglais courant.
6. **Infos personnelles** : date de naissance, adresse, téléphone, e-mail.

> ⚠️ **Pas de section « Centres d'intérêt / Loisirs »** (absente du CV d'Élodie — ne rien inventer).

### Colonne de droite (large)
1. **PROFIL** : court paragraphe d'accroche (brouillon fourni plus bas, à faire valider/ajuster par Élodie).
2. **EXPÉRIENCES PROFESSIONNELLES** sur une **timeline verticale** : années (début/fin) à gauche, pastille colorée, intitulé du poste en gras, employeur/lieu, puis missions en puces.
3. **FORMATIONS** sur la même logique de timeline.

Reprendre les codes visuels du modèle : titres de sections avec petite icône/pastille, filet vertical de timeline, dates en gris à gauche des pastilles, hiérarchie typographique nette (poste en gras + ligne employeur en couleur/italique + puces).

---

## CONTENU À INTÉGRER (CV d'Élodie)

### En-tête / identité
- **Nom** : Élodie SIGUENZA
- **Née le** : 05/10/1985
- **Adresse** : 33 impasse de l'Autan, 32600 Ségoufielle
- **Téléphone** : 06.71.47.95.28
- **E-mail** : elodie.siguenza@gmail.com
- **Titre / poste visé** : Responsable administrative et financière — Attachée d'administration de l'État

### Profil (BROUILLON — à valider par Élodie)
> Attachée d'administration de l'État, je dispose d'une solide expérience en gestion administrative et financière au sein d'établissements publics. Spécialisée dans la gestion des marchés publics, le suivi budgétaire, l'exécution des dépenses et le pilotage d'équipe, j'interviens sur l'ensemble du cycle administratif et comptable. Rigoureuse et organisée, je veille à la conformité des procédures et au conseil juridique auprès des ordonnateurs.

### Expériences professionnelles (de la plus récente à la plus ancienne)

**1. Chargée d'affaires administratives et financières** — *Depuis janvier 2026*
Ministère de la Transition Écologique — Agence de l'eau Adour-Garonne, Toulouse (31) — *Établissement public*
- Gestion administrative et financière des marchés publics
- Suivi budgétaire et contrôle de l'exécution des dépenses
- Gestion des engagements juridiques et comptables
- Suivi des factures, acomptes, avances et paiements
- Contrôle de la conformité des actes et procédures
- Utilisation de Chorus Pro et des outils de gestion financière
- Relations avec les fournisseurs et partenaires institutionnels

**2. Secrétaire Générale** — *Septembre 2022 – Décembre 2025*
Ministère de l'Éducation nationale, de l'Enseignement supérieur et de la Recherche
Collège Albert Camus, Villemur-sur-Tarn (31) — *Établissement de catégorie 3 – 510 élèves – SEGPA – UPE2A – restauration autonome*
et Lycée des métiers Eugène Montel, Colomiers (31) — *Lycée professionnel – GRETA – ERASMUS – restauration autonome*
- Élaboration et suivi d'exécution du budget en dépenses et recettes (GFC)
- Participation à la rédaction de marché public (MAPA)
- Rédaction des actes administratifs (DEMACT)
- Rédaction et présentation du compte financier pour la partie ordonnateur
- Mise en place des plans de mise en sûreté
- Gestion administrative de l'établissement (suivi des contrats)
- Conseils juridiques à l'ordonnateur
- Encadrement d'équipe (16 agents Région – 1B – 2C)

**3. Professeur des écoles** — *2014 – 2022*
Ministère de l'Éducation nationale, de l'Enseignement supérieur et de la Recherche
- Différents postes occupés dans les académies de Reims et Toulouse

### Formations
- **2022** — Formation Attachée d'Administration de l'État — IRA de Bastia (2A)
- **2008** — Master Management et Ingénierie Économique — Université de Paris-Est, Marne-la-Vallée (77)
- **2003** — Baccalauréat Général « Économique et Social » — Lycée Jean Jaurès, Reims (51)

### Compétences clés (dérivées des expériences — SANS étoiles)
- Gestion administrative et financière
- Marchés publics (MAPA)
- Suivi et exécution budgétaire (GFC)
- Engagements juridiques et comptables
- Conformité des actes et procédures
- Conseil juridique à l'ordonnateur
- Encadrement et management d'équipe

### Outils / Informatique
- Bureautique : Word, Excel, PowerPoint
- Outils métiers : Chorus Pro, GFC, DEMACT
- Outils de gestion administrative et financière

### Langues
- Anglais courant (séjours longs en Australie, Canada, Nouvelle-Zélande)

---

## Livrables attendus
1. `cv_elodie.html` — le CV en HTML/CSS, format A4, une page.
2. (optionnel) `style.css` si CSS séparé.
3. `convert_to_pdf.py` (ou équivalent) — script de conversion HTML → PDF A4.
4. `cv_elodie.pdf` — le rendu final imprimable.

## Points de vigilance
- Tenir sur **une seule page A4**.
- Conserver les **aplats de couleur à l'impression** (`print-color-adjust: exact`).
- **Aucune section loisirs**, **pas d'étoiles** de compétences.
- Le **profil** est un brouillon à faire valider.
- Prévoir un **emplacement photo** (placeholder si la photo n'est pas fournie au moment de la génération).

---

## Révisions / décisions de version

### v2 — Outils métiers (mise à jour de cohérence)
Décision : **conserver les outils métiers** (valorisés dans la fonction publique), mais **mettre à jour selon le poste réel** d'Élodie. GFC était l'outil de l'Éducation nationale (poste passé) ; l'outil actuel à l'Agence de l'eau (Transition Écologique) est **Qualiac**.

- **Bloc compétences / outils métiers (colonne gauche)** :
  - Bureautique : Word, Excel, PowerPoint *(inchangé)*
  - Gestion financière publique : **Chorus Pro, Qualiac**
  - Dématérialisation des actes : DEMACT
  - → **Retirer GFC du bloc compétences** (outil quitté), le remplacer par **Qualiac**.
- **Expérience actuelle** « Chargée d'affaires administratives et financières – Agence de l'eau Adour-Garonne » : mentionner **Qualiac** au niveau du suivi budgétaire / exécution des dépenses.
- **Expérience passée** « Secrétaire Générale – Éducation nationale » : **conserver GFC** (outil de l'époque, à sa juste place).

Logique : GFC = passé (Éducation nationale), Qualiac = poste actuel (Agence de l'eau). Cohérence du récit professionnel.
