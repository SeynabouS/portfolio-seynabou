"""Portfolio professionnel de Seynabou Sougou — application Streamlit."""

from base64 import b64encode
from html import escape
from pathlib import Path

import streamlit as st

from portfolio_content import PROJECTS, SKILLS


ROOT = Path(__file__).resolve().parent
CV_PATH = ROOT / "CV_Seynabou_Sougou.pdf"
EMAIL = "seynabousougou21@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/seynabousougou/"
GITHUB = "https://github.com/SeynabouS"

st.set_page_config(
    page_title="Seynabou Sougou | Réseaux, cybersécurité & projets IT",
    page_icon="◈", layout="wide", initial_sidebar_state="collapsed",
)


def html(content: str) -> None:
    """Render static markup in the main document, without a nested iframe."""
    st.html(content)


@st.cache_data(show_spinner=False)
def read_asset(path: str) -> bytes:
    return (ROOT / path).read_bytes()


def tags(values: list[str]) -> str:
    return '<div class="tag-list">' + "".join(
        f'<span class="tag">{escape(value)}</span>' for value in values
    ) + "</div>"


def project_card(project: dict) -> str:
    bullets = "".join(f"<li>{escape(item)}</li>" for item in project["contributions"])
    source = ""
    if project.get("url"):
        source = (
            f'<a class="text-link" href="{escape(project["url"], quote=True)}" '
            'target="_blank" rel="noopener noreferrer">Consulter le projet sur GitHub</a>'
        )
    return f"""
    <article class="project-card" id="{escape(project['id'])}">
      <div class="project-meta"><span>{escape(project['context'])}</span>
        <span class="project-number">{escape(project['number'])}</span></div>
      <p class="project-domain">{escape(project['domain'])}</p>
      <h3>{escape(project['title'])}</h3>
      <p class="project-subtitle">{escape(project['subtitle'])}</p>
      <p class="project-description">{escape(project['description'])}</p>
      <div class="project-result"><span>RÉSULTAT</span><p>{escape(project['result'])}</p></div>
      {tags(project['stack'])}
      <details class="project-details">
        <summary>Explorer le projet <span aria-hidden="true">＋</span></summary>
        <div class="detail-body">
          <h4>Le besoin</h4><p>{escape(project['need'])}</p>
          <h4>Mon rôle</h4><p>{escape(project['role'])}</p>
          <h4>Mes contributions</h4><ul>{bullets}</ul>
          <h4>Les livrables</h4><p>{escape(project['deliverables'])}</p>{source}
        </div>
      </details>
    </article>
    """


html(f"<style>{(ROOT / 'styles.css').read_text(encoding='utf-8')}</style>")
html("""
<a class="skip-link" href="#projets" target="_self">Aller aux projets</a>
<header class="site-header" id="accueil">
  <a href="#accueil" class="brand" target="_self" aria-label="Seynabou Sougou — accueil">
    <span class="monogram" aria-hidden="true">SS<span>·</span></span>
    <span>Seynabou Sougou<small>Réseaux & cybersécurité</small></span>
  </a>
  <nav aria-label="Navigation principale">
    <a href="#projets" target="_self">Projets</a>
    <a href="#parcours" target="_self">Parcours</a>
    <a href="#competences" target="_self">Compétences</a>
    <a href="#cv" target="_self">Mon CV</a>
    <a href="#contact" class="nav-contact" target="_self">Échangeons <span class="arrow-icon" aria-hidden="true"></span></a>
  </nav>
</header>
""")

portrait = b64encode(read_asset("photo_seynabou.jpeg")).decode("ascii")
html(f"""
<section class="hero" aria-labelledby="hero-title">
  <div class="hero-copy">
    <span class="availability"><span aria-hidden="true"></span>À l’écoute d’opportunités · CDI / CDD</span>
    <p class="eyebrow">RÉSEAUX · CYBERSÉCURITÉ · PROJETS IT</p>
    <h1 id="hero-title">Seynabou<br>Sougou<span class="accent">.</span></h1>
    <p class="hero-headline">Comprendre les enjeux.<br>Construire les solutions.</p>
    <p class="hero-intro">Je conçois des outils qui fiabilisent les données,
      automatisent les contrôles et aident à protéger les infrastructures.
      Une approche technique, avec le sens du besoin métier.</p>
    <div class="hero-actions">
      <a class="button button-accent" href="#projets" target="_self">Découvrir mes projets <span class="arrow-icon" aria-hidden="true"></span></a>
      <a class="button button-outline" href="#cv" target="_self">Consulter mon CV</a>
    </div>
    <p class="hero-location">Île-de-France & Toulouse</p>
  </div>
  <div class="hero-visual">
    <img class="portrait" src="data:image/jpeg;base64,{portrait}"
      alt="Portrait de Seynabou Sougou" width="688" height="1298">
    <div class="portrait-note"><span class="note-symbol arrow-icon" aria-hidden="true"></span>
      <span>Du besoin métier<br><strong>à la solution opérationnelle.</strong></span></div>
  </div>
</section>
<section class="metrics" aria-label="Quelques repères sur mon expérience au SIPPEREC">
  <div><strong>4 ans</strong><span>d’alternance en réseaux & sécurité</span></div>
  <div><strong>6 projets</strong><span>d’automatisation des audits réseau</span></div>
  <div><strong>−80 %</strong><span>de temps d’audit des livrables réseau</span></div>
</section>
<section class="intro-section" aria-labelledby="approche-title">
  <p class="eyebrow section-kicker">MON APPROCHE</p>
  <div class="intro-grid">
    <h2 id="approche-title">La technique au service<br>d’un besoin concret.</h2>
    <div><p>Au SIPPEREC, j’ai mené des projets d’applications métiers de bout en bout :
      comprendre les attentes, structurer les données, développer, tester et documenter.
      Mon expérience en SOC chez Orange et mon projet d’audit RGPD avec EY
      complètent cette pratique par une vision opérationnelle de la cybersécurité.</p>
    <p class="intro-emphasis">Ce qui m’anime : transformer un problème complexe en un outil utile,
      compréhensible et exploitable par les équipes.</p></div>
  </div>
</section>
<section class="section-heading" id="projets" aria-labelledby="projets-title">
  <p class="eyebrow section-kicker">01 / RÉALISATIONS</p>
  <h2 id="projets-title">Des projets, du terrain au code.</h2>
  <p>Une sélection de réalisations professionnelles, académiques et personnelles.</p>
</section>
""")

category = st.segmented_control(
    "Filtrer les projets par domaine",
    ["Tous les projets", "Réseaux & SIG", "Cybersécurité & IA", "Développement"],
    default="Tous les projets", key="project_filter", label_visibility="collapsed",
)
selected_projects = [
    p for p in PROJECTS if category in (None, "Tous les projets") or p["category"] == category
]
html('<div class="project-grid">' + "".join(project_card(p) for p in selected_projects) + "</div>")

html("""
<section class="section-heading" id="parcours" aria-labelledby="parcours-title">
  <p class="eyebrow section-kicker">02 / PARCOURS</p>
  <h2 id="parcours-title">Une expérience ancrée dans le concret.</h2>
  <p>Des réseaux télécoms à la réponse aux incidents, avec un fil conducteur : rendre les systèmes plus fiables.</p>
</section>
<div class="timeline">
  <article class="experience">
    <div class="experience-date"><span>2022 — 2026</span><small>Alternance · 4 ans</small></div>
    <div class="experience-content">
      <p class="company">SIPPEREC</p><h3>Réseaux & sécurité</h3>
      <p>Suivi de réseaux télécoms délégués et développement d’outils pour fiabiliser les données,
        les audits et les analyses d’infrastructure.</p>
      <ul><li>Pilotage technique et fonctionnel d’applications métiers, du recueil du besoin à la livraison.</li>
        <li>Automatisation en Python des contrôles de livrables réseau et de l’identification des anomalies.</li>
        <li>Conception d’outils SIG et d’analyse de résilience avec PostgreSQL/PostGIS et des interfaces web.</li>
        <li>Suivi du référentiel réseau, échanges avec les délégataires et rédaction de documentation technique.</li></ul>
      <div class="experience-highlight">6 projets d’automatisation · Réduction de 80 % du temps d’audit des livrables réseau</div>
    </div>
  </article>
  <article class="experience">
    <div class="experience-date"><span>Avr. — juin 2024</span><small>Stage · SOC</small></div>
    <div class="experience-content">
      <p class="company">ORANGE</p><h3>Analyste SOC</h3>
      <p>Participation à l’analyse des alertes et à l’automatisation de la réponse aux incidents de sécurité.</p>
      <ul><li>Analyse d’alertes avec IBM QRadar et enrichissement des investigations avec Cortex XDR.</li>
        <li>Création et documentation de playbooks Cortex XSOAR pour les scénarios malware et phishing.</li>
        <li>Intégration de XSOAR avec Ansible Tower pour automatiser les actions de réponse.</li>
        <li>Configuration d’accès sécurisés aux serveurs Linux via Cisco ISE et TACACS+.</li></ul>
    </div>
  </article>
</div>
<section class="formation" aria-labelledby="formation-title">
  <h3 id="formation-title">Formation technique</h3>
  <div class="formation-grid">
    <div><span class="formation-date">2023 — 2026</span><h4>ECE Paris</h4>
      <p>Cursus ingénieur · Systèmes d’information, réseaux et cybersécurité.</p></div>
    <div><span class="formation-date">2021 — 2023</span><h4>IUT de Créteil-Vitry · UPEC</h4>
      <p>Réseaux & télécommunications · Parcours cybersécurité.</p></div>
  </div>
</section>
<section class="section-heading" id="competences" aria-labelledby="competences-title">
  <p class="eyebrow section-kicker">03 / SAVOIR-FAIRE</p>
  <h2 id="competences-title">Un profil à l’interface de plusieurs métiers.</h2>
  <p>Des compétences mobilisées dans les projets, les missions et les environnements de laboratoire.</p>
</section>
""")

html('<div class="skills-grid">' + "".join(
    f'<article class="skill-card"><span class="skill-index">{i:02}</span>'
    f'<h3>{escape(skill["title"])}</h3><p>{escape(skill["description"])}</p>'
    f'{tags(skill["items"])}</article>' for i, skill in enumerate(SKILLS, 1)
) + '</div><p class="language-note">Langues : français · anglais B2 · espagnol A1</p>')

html("""
<section class="cv-section" id="cv" aria-labelledby="cv-title">
  <div><p class="eyebrow section-kicker">04 / CURRICULUM VITÆ</p>
    <h2 id="cv-title">Mon parcours, en une page.</h2>
    <p>Retrouvez mes expériences, mes projets et mes compétences dans mon CV officiel.</p></div>
  <span class="document-label">PDF · 1 PAGE</span>
</section>
""")
st.download_button(
    "Télécharger mon CV officiel", data=read_asset(CV_PATH.name),
    file_name="CV_Seynabou_Sougou.pdf", mime="application/pdf",
    key="download_official_cv", type="primary", on_click="ignore", icon=":material/download:",
)
with st.expander("Aperçu du CV officiel"):
    st.image(str(ROOT / "assets" / "cv_preview.png"), use_container_width=True)

html(f"""
<section class="contact-section" id="contact" aria-labelledby="contact-title">
  <div class="contact-copy">
    <p class="eyebrow">05 / CONTACT</p>
    <h2 id="contact-title">Un projet.<br>Une opportunité.<br><span>Échangeons.</span></h2>
    <p>Je recherche un poste en réseaux, cybersécurité ou gestion de projets IT,
      en Île-de-France ou à Toulouse.</p>
  </div>
  <div class="contact-links">
    <a href="mailto:{EMAIL}"><span><small>PAR EMAIL</small>{EMAIL}</span><span class="arrow-icon" aria-hidden="true"></span></a>
    <a href="{LINKEDIN}" target="_blank" rel="noopener noreferrer"><span><small>RÉSEAU PROFESSIONNEL</small>LinkedIn</span><span class="arrow-icon" aria-hidden="true"></span></a>
    <a href="{GITHUB}" target="_blank" rel="noopener noreferrer"><span><small>CODE & PROJETS PUBLICS</small>GitHub</span><span class="arrow-icon" aria-hidden="true"></span></a>
    <a href="tel:+33667047341"><span><small>PAR TÉLÉPHONE</small>+33 6 67 04 73 41</span><span class="arrow-icon" aria-hidden="true"></span></a>
  </div>
</section>
<footer class="site-footer"><span>© 2026 Seynabou Sougou</span>
  <span>Mise à jour · novembre 2026</span><a href="#accueil" target="_self">Retour en haut ↑</a></footer>
""")
