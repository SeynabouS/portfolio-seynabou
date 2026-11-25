# Portfolio de Seynabou Sougou

Portfolio professionnel Streamlit : réseaux, cybersécurité, automatisation et projets IT.

## Lancement local

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Structure

- `app.py` : page, navigation, filtre des projets et téléchargement du CV.
- `portfolio_content.py` : descriptions des projets et compétences.
- `styles.css` : présentation responsive et styles accessibles.
- `.streamlit/config.toml` : thème Streamlit.
- `CV_Seynabou_Sougou.pdf` : CV officiel, conservé sans modification.
- `assets/cv_preview.png` : rendu de la page du même PDF pour l’aperçu.

## Mise à jour des contenus

Les expériences, dates et chiffres reprennent le CV officiel fourni le 25 novembre 2026.
Les projets professionnels, académiques et personnels sont explicitement distingués.
Les évaluations de laboratoire ne sont pas présentées comme des mesures de performance en production.
Pour remplacer le CV, copier le nouveau PDF au même emplacement et régénérer l’aperçu depuis ce PDF.

## Vérification

```bash
python -m unittest discover -s tests -v
```

L’application reste compatible avec le point d’entrée `app.py` de Streamlit Community Cloud.
