import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import base64
import pandas as pd
import altair as alt
import random
import requests
import numpy as np
from textwrap import dedent
def generate_attack_data():
    base = np.random.poisson(50, 24)
    attacks = np.concatenate([np.zeros(18), np.random.poisson([1, 3, 5, 8, 3, 2])])
    return pd.DataFrame({
        "Heure": [f"{h}:00" for h in range(24)],
        "Trafic": base + attacks * 10,
        "Alertes": attacks
    })


# Configuration de la page
st.set_page_config(
    page_title="Seynabou Sougou - Portfolio Cybersécurité",
    layout="wide",
    page_icon="🛡️",
    initial_sidebar_state="expanded",
)

# CSS personnalisé - Thème Adaptable "Cyber-Minimaliste"
st.markdown("""
<style>
    /* Import de la police Inter */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    /* Configuration globale */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    :root {
        --primary-accent: #0ea5e9;
        --secondary-accent: #10b981;
        --bg-dark: #0f172a;
        --bg-card: #1e293b;
        --text-light: #f8fafc;
        --text-muted: #94a3b8;
        --text-dark: #0f172a;
        --border-color: rgba(148, 163, 184, 0.1);
        --border-color-dark: rgba(30, 41, 59, 0.5);
        --bg-subtle: rgba(30, 41, 59, 0.5);
        --bg-overlay: rgba(0, 0, 0, 0.2);
        --shadow-glow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        --border-radius: 12px;
        --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    /* ========== MODE CLAIR ========== */
    @media (prefers-color-scheme: light) {
        :root {
            --bg-dark: #f8fafc;
            --bg-card: #ffffff;
            --text-light: #0f172a;
            --text-muted: #475569;
            --text-dark: #0f172a;
            --border-color: rgba(100, 116, 139, 0.15);
            --border-color-dark: rgba(226, 232, 240, 0.8);
            --bg-subtle: rgba(226, 232, 240, 0.5);
            --bg-overlay: rgba(0, 0, 0, 0.05);
        }
    }
    
    /* Body et main */
    .main {
        background-color: var(--bg-dark);
        color: var(--text-light);
        font-family: 'Inter', sans-serif;
    }
    
    /* Typo - Headers */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        letter-spacing: -0.5px;
        color: var(--text-light);
    }
    
    h1 {
        font-size: 2.8em;
        margin-bottom: 1.5rem;
        background: linear-gradient(90deg, var(--text-light), var(--primary-accent));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    h2 {
        font-size: 1.9em;
        margin-bottom: 1.5rem;
        padding-bottom: 0.8rem;
        border-bottom: 1px solid var(--border-color);
        color: var(--text-light);
    }
    
    h3 {
        font-size: 1.4em;
        color: var(--text-light);
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    h4 {
        color: var(--secondary-accent);
        font-weight: 600;
    }
    
    /* Spacing global */
    p {
        line-height: 1.8;
        font-size: 1.05em;
        color: var(--text-muted);
    }
    
    /* Containers principaux (ex: fun-fact) */
    .fun-fact {
        background: var(--border-color-dark);
        border-radius: var(--border-radius);
        padding: 20px;
        margin: 15px 0;
        color: var(--text-light);
        border: 1px solid var(--border-color);
        border-left: 4px solid var(--secondary-accent);
        box-shadow: var(--shadow-glow);
        transition: var(--transition);
    }
    
    .fun-fact:hover {
        border-color: var(--secondary-accent);
        transform: translateY(-2px);
        background: var(--bg-card);
    }
    
    .fun-fact b {
        color: var(--primary-accent);
        font-weight: 600;
    }
    
    /* Code animé */
    .hack-animation {
        font-family: 'Courier New', monospace;
        color: #10b981;
        background-color: var(--bg-card);
        padding: 20px;
        border-radius: var(--border-radius);
        margin: 15px 0;
        border: 1px solid var(--border-color);
        box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.1);
        overflow-x: auto;
        letter-spacing: 0.05em;
    }
    
    /* Project cards améliorées */
    .project-card {
        border-left: none;
        padding: 30px;
        background: var(--bg-card);
        border-radius: var(--border-radius);
        margin: 25px 0;
        box-shadow: var(--shadow-glow);
        color: var(--text-light);
        transition: var(--transition);
        border: 1px solid var(--border-color);
    }
    
    .project-card:hover {
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        transform: translateY(-2px);
        border-color: var(--primary-accent);
    }
    
    .project-card h3 {
        color: var(--primary-accent);
    }
    
    .project-card b {
        color: var(--secondary-accent);
        font-weight: 600;
    }
    
    /* Skill badges avec animation */
    .skill-badge {
        display: inline-block;
        padding: 6px 14px;
        margin: 4px;
        background: rgba(14, 165, 233, 0.1);
        color: var(--text-light);
        border-radius: 6px;
        font-size: 13px;
        font-weight: 500;
        transition: var(--transition);
        cursor: default;
        border: 1px solid rgba(14, 165, 233, 0.2);
    }
    
    .skill-badge:hover {
        background: rgba(14, 165, 233, 0.2);
        color: var(--text-dark);
        border-color: var(--primary-accent);
    }
    
    /* Boutons améliorés */
    .stButton > button {
        background: var(--primary-accent);
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        border: none;
        font-weight: 700;
        font-size: 15px;
        transition: var(--transition);
        box-shadow: 0 0 20px rgba(14, 165, 233, 0.3);
        text-transform: uppercase;
        letter-spacing: 0.5px; 
    }
    
    .stButton > button:hover {
        background: #0284c7;
        box-shadow: 0 0 30px rgba(14, 165, 233, 0.5);
        transform: translateY(-2px);
    }
    
    /* Sidebar amélioré */
    .sidebar .sidebar-content {
        background: var(--bg-dark);
        border-right: 1px solid var(--border-color);
    }
    
    /* Accueil container */
    .accueil-container {
        color: var(--text-light);
        background: var(--bg-card);
        border-radius: var(--border-radius);
        padding: 40px;
        margin: 20px 0;
        box-shadow: var(--shadow-glow);
        border: 1px solid var(--border-color);
    }
    
    /* Textes accentués */
    .accent-text, .accent-text2, .accent-text3 {
        font-weight: 700;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .accent-text { background: linear-gradient(120deg, var(--primary-accent), var(--secondary-accent)); }
    .accent-text2 { background: linear-gradient(120deg, var(--secondary-accent), #ff7eb9); }
    .accent-text3 { background: linear-gradient(120deg, #ff7eb9, var(--primary-accent)); }
    
    /* Keep header visible so sidebar reopen control remains available */
    #MainMenu, footer { visibility: hidden; }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] button {
        background-color: transparent;
        color: var(--text-muted);
        border-bottom: 2px solid transparent;
        transition: var(--transition);
        padding: 10px 0;
        margin: 0 12px;
    }
    
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        color: var(--primary-accent);
        border-bottom-color: var(--primary-accent);
    }
    
    /* Expanders */
    .stExpander {
        background-color: transparent;
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        transition: var(--transition);
    }
    
    .stExpander:hover {
        border-color: rgba(0, 245, 195, 0.4);
        background-color: var(--bg-card);
    }
    
    /* Metrics cards */
    .stMetric {
        background-color: var(--bg-card);
        border: 1px solid var(--border-color);
        border-radius: var(--border-radius);
        padding: 20px;
        transition: var(--transition);
    }
    
    .stMetric:hover {
        border-color: rgba(14, 165, 233, 0.4);
    }
    
    /* Status Badge */
    .status-badge {
        background: linear-gradient(90deg, #0ea5e9, #10b981);
        color: white;
        padding: 8px 16px;
        border-radius: 50px;
        font-weight: 600;
        font-size: 0.9em;
        display: inline-block;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(14, 165, 233, 0.3);
    }

</style>
""", unsafe_allow_html=True)

# Sidebar (menu)
with st.sidebar:
    st.title("Navigation")
    
    # Photo de profil ronde si disponible, sinon placeholder pro
    try:
        img_sidebar = Image.open("photo_seynabou.jpeg")
        st.image(img_sidebar, width=150)
    except:
        st.write("Seynabou Sougou")
        
    st.markdown("---")
    
    page = st.radio("Aller vers :", 
               ["🏠 Accueil", "🚀 Projets", "🧑‍💼 Expériences", "🛠️ Compétences", "📄 CV", "📱 Contact"])

    st.markdown("---")
    st.markdown("""
    <div style="padding: 10px; background: rgba(255,255,255,0.05); border-radius: 8px;">
        <p style="font-size: 0.85em; margin: 0; color: #94a3b8;">
            <b>Statut actuel :</b><br>
            En poste (Alternance)<br>
            <span style="color: #10b981;">●</span> Recherche CDI pour Sept. 2026
        </p>
    </div>
    """, unsafe_allow_html=True)

# Accueil
if page == "🏠 Accueil":
    # En-tête professionnel
    st.markdown('<div class="status-badge">🎓 Fin d\'études : Août 2026 | 💼 Disponible pour CDI : Septembre 2026</div>', unsafe_allow_html=True)
    st.title("Seynabou Sougou")
    st.markdown("### Future Ingénieure en Audit & Sécurité des Infrastructures")
    
    col1, col2 = st.columns([1, 3])
    with col1:
        try:
            img = Image.open("photo_seynabou.jpeg")
            st.image(img, caption="Seynabou Sougou", width=250)
        except:
            st.info("Photo de profil")

    with col2:
        st.markdown("""
            <div style="color: var(--text-light);
                        background: var(--bg-card);
                        border-radius: 12px;
                        padding: 30px;
                        border: 1px solid var(--border-color);
                        font-family: 'Inter', sans-serif;">
            
            <h2 style="color: var(--primary-accent); margin-top: 0; border-bottom: 1px solid var(--border-color); padding-bottom: 15px; font-size: 1.5em;">
                À propos de moi
            </h2>
            
            <div style="font-size: 1.1em; line-height: 1.6; margin: 15px 0;">
                Apprentie ingénieure en cybersécurité, je me spécialise dans l'<b>audit technique</b> et la <b>sécurité des infrastructures</b> (réseau, système). Mon expérience principale chez SIPPEREC m'a permis de développer une expertise en analyse de conformité et en durcissement des systèmes.
            </div>
            
            <div style="font-size: 1.05em; line-height: 1.6; margin: 15px 0;">
                Passionnée par l'efficacité, j'utilise <b>Python pour automatiser et industrialiser les contrôles de sécurité</b>, transformant des processus d'audit manuels en solutions fiables et rapides. Une expérience complémentaire en <b>SOC</b> chez Orange Cyberdefense m'a apporté une vision opérationnelle de la détection et de la réponse aux menaces (SIEM/SOAR).
                <br><br>
                <b>Objectif :</b> Un CDI dès <b>septembre 2026</b> en audit, sécurité des infrastructures, ou GRC technique (mobile sur toute la France).
            </div>
            
            <h3 style="color: var(--text-light); margin-top: 20px; font-size: 1.2em;">
                Domaines de compétences clés :
            </h3>
            <ul style="margin-top: 10px; padding-left: 20px; color: var(--text-muted);">
                <li style="margin-bottom: 8px;">Audit de Sécurité & Analyse de Conformité (ISO 27001, RGPD)</li>
                <li style="margin-bottom: 8px;">Sécurité des Infrastructures (Réseau, Système Linux) & Durcissement</li>
                <li style="margin-bottom: 8px;">Automatisation des Contrôles et Scripting (Python)</li>
                <li style="margin-bottom: 8px;">Gestion des Accès et des Identités (IAM, TACACS+)</li>
                <li style="margin-bottom: 8px;">Analyse de Données de Sécurité (SIEM, EDR)</li>
            </ul>

            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📊 Indicateurs Clés")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Expérience en Audit & Infra", "4 ans", "Apprentissage")
    with col2:
        st.metric("Projets d'Automatisation", "10+", "Python")
    with col3:
        st.metric("Disponibilité CDI", "Sept. 2026", "Mobile France")

# Projets
elif page == "🚀 Projets":
    st.title("Portfolio de Projets")
    st.markdown("Sélection de réalisations techniques démontrant mes compétences en défense et développement.")

    # Projet JuriTech
    with st.expander("⚖️ JuriTech – Solution d’Audit RGPD Automatisée", expanded=True):
        st.markdown("""
        <div class="project-card">
        <h3 style="color:var(--primary-accent);">Projet de fin d’études pour EY</h3>
        Solution innovante pour l'automatisation des audits de conformité RGPD, alliant expertise juridique et intelligence artificielle.
        <br><br>
        🔧 <b>Stack Technique :</b> Backend Modulaire, Base de données relationnelle, IA Locale sécurisée
        🎯 <b>Objectif :</b> Standardiser, accélérer et fiabiliser les audits RGPD pour les organisations.
        </div>
        """, unsafe_allow_html=True)

        # Create tabs for more details
        tab1, tab2, tab3, tab4 = st.tabs(["Contexte & Rôle", "Architecture", "IA & Sécurité", "Résultats"])

        with tab1:
            st.markdown("#### Contexte du Projet")
            st.markdown("""
            Dans le cadre du RGPD, les organisations doivent prouver la conformité de leurs traitements de données personnelles. Les audits sont souvent manuels, chronophages, et difficiles à industrialiser. JuriTech a été conçu pour répondre à ce défi.
            """)
            st.markdown("#### Mon Rôle : Architecte Technique")
            st.markdown("""
            En tant qu'architecte technique, j'ai été responsable de :
            - **Conception de l’architecture backend** (modulaire, sécurisée).
            - **Modélisation de la base de données** pour traduire les exigences RGPD.
            - **Traduction des règles RGPD** en logique algorithmique pour le moteur d’évaluation.
            - **Intégration d’une IA locale sécurisée** pour un chatbot d'assistance.
            """)

        with tab2:
            st.markdown("#### Architecture Technique")
            st.markdown("""
            - **Backend structuré et modulaire :** Séparation claire des couches (API, logique métier, moteur de recommandations).
            - **Base de données relationnelle :** Conception des entités (audits, contrôles, non-conformités) pour une traçabilité et historisation complètes.
            - **Dashboard interactif :** Pour la visualisation des résultats d'audit.
            - **Génération automatisée de livrables :** Rapports de conformité et plans de remédiation.
            """)
            st.code("""
# Exemple de logique du moteur d'évaluation
def evaluate_compliance(data_processing_activity):
    rules = load_rgpd_rules()
    non_conformities = []
    for rule in rules:
        if not rule.check(data_processing_activity):
            non_conformities.append(rule.get_non_conformity())
    
    score = calculate_score(len(non_conformities))
    return {"score": score, "details": non_conformities}
            """, language="python")

        with tab3:
            st.markdown("#### IA Locale & Cybersécurité")
            st.markdown("""
            **🤖 Intégration d’une IA locale sécurisée**
            - Développement d’un chatbot d’assistance RGPD.
            - Utilisation d'un modèle IA exécuté en environnement contrôlé, sans exposition de données sensibles à des APIs externes.
            - Conception d’un système d’aide contextuelle basé sur les résultats d’audit.
            
            **🔐 Dimension Cybersécurité ("Privacy by Design")**
            - **Sécurisation des données d’audit :** Chiffrement et contrôles d'accès stricts.
            - **Cloisonnement des traitements :** Isolation des différents modules de l'application.
            - **Protection des données sensibles :** Anonymisation et pseudonymisation des données lorsque possible.
            """)
           


        with tab4:
            st.markdown("#### Résultats & Collaboration")
            st.markdown("""
            - **Standardisation** des audits RGPD.
            - **Réduction significative** du temps d’analyse.
            - **Génération automatique** de plans de remédiation.
            - **Amélioration de la traçabilité** pour les DPO et auditeurs.
            - Outil exploitable dans un contexte de cabinet de conseil comme **EY**.
            """)
            st.markdown("---")
            st.markdown("#### Travail en Équipe")
            st.markdown("""
            Projet réalisé en collaboration avec Chef de projet, Analyste fonctionnel RGPD, et Développeurs Front-end, en suivant une méthodologie structurée avec des livrables professionnels et des interactions régulières avec le commanditaire EY.
            """)

    # Projet 1 : Pentest
    with st.expander("Projet 1 : Lab de Simulation d'Attaques & Défense", expanded=True):
        st.markdown("""
        <div class="project-card">
        <h3 style="color:var(--primary-accent);">Purple Teaming Lab</h3>
        Mise en place d'un environnement de test pour simuler des attaques (Red Team) et configurer les défenses appropriées (Blue Team).
        <br><br>
        🔧 <b>Stack Technique :</b> Kali Linux, Metasploit, Wireshark, Fail2Ban
        🎯 <b>Objectif :</b> Analyser les signatures d'attaques pour affiner les règles de détection.
        </div>
        """, unsafe_allow_html=True)

        tab1, tab2, tab3 = st.tabs(["Analyse Brute Force", "Scénario", "Retours"])

        with tab1:
            brute_force_data = {
                "Jour": ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"],
                "Tentatives": [20, 45, 10, 35, 5],
                "Bloquées": [20, 45, 10, 35, 5]
            }
            df1 = pd.DataFrame(brute_force_data)
            chart1 = alt.Chart(df1).mark_bar().encode(
                x='Jour',
                y='Tentatives',
                color=alt.value('#ff4b4b')
            ).properties(height=300)
            st.altair_chart(chart1, use_container_width=True)

            st.code("""
            [sshd]
            enabled = true
            maxretry = 3
            bantime = 1h
            """, language='ini')

        with tab2:
            st.write("""
            **Scénario d'attaque SSH :**
            1. Reconnaissance (Nmap)
            2. Identification du service SSH
            3. Attaque par dictionnaire (Hydra)
            4. Détection et bannissement IP (Fail2Ban)
            """)
            if st.button("▶️ Lancer la simulation (Logs)"):
                st.markdown("""
                <div class="hack-animation">
                > ssh admin@192.168.1.1<br>
                > Password: ********<br>
                > Permission denied<br>
                > Password: ********<br>
                > Connection closed by 192.168.1.1 [FAIL2BAN]
                </div>
                """, unsafe_allow_html=True)
                st.success("✅ IP attaquante bannie automatiquement.")

        with tab3:
            st.markdown("""
            **💡 Compétences validées :**
            - Hardening de serveurs Linux
            - Configuration de règles IPS/IDS
            - Analyse de flux chiffrés
            """)

    # Projet 2 : ELK
    with st.expander("Projet 2 : SIEM & Visualisation de Logs (ELK)", expanded=True):
        st.markdown("""
        <div class="project-card">
        <h3 style="color:var(--primary-accent);">Déploiement Stack ELK</h3>
        Centralisation et visualisation des logs systèmes pour la détection d'anomalies.
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            alertes_df = pd.DataFrame({
                "Type d'alerte": ["Brute force", "Port scan", "Web Exploit", "Phishing"],
                "Nombre": [35, 25, 15, 5]
            })
            chart2 = alt.Chart(alertes_df).mark_arc().encode(
                theta="Nombre",
                color=alt.Color("Type d'alerte"),
                tooltip=["Type d'alerte", "Nombre"]
            )
            st.altair_chart(chart2, use_container_width=True)

        with col2:
            st.markdown("""
            🔎 **Workflow de traitement :**
            1. Ingestion des logs (Logstash)
            2. Parsing et enrichissement (GeoIP)
            3. Visualisation (Kibana)
            """)

        st.code("""
        filter {
            grok {
                match => {
                    "message" => "%{SYSLOGTIMESTAMP:timestamp} %{SYSLOGHOST:hostname} sshd\\[%{POSINT:pid}\\]: %{WORD:event} %{WORD:method} for %{WORD:auth_method} user %{USER:user} from %{IP:src_ip} port %{INT:src_port} %{WORD:proto}"
                }
            }
            if [event] == "Failed" {
                mutate { add_tag => ["ssh_failed"] }
            }
        }
        """, language="python")

    # NeuralFirewall (séparé car pas imbriqué)
    st.markdown("---")
    st.subheader("🤖 NeuralFirewall - Détection par IA")

    st.markdown("""
    <div style="border-left: 4px solid var(--primary-accent); padding-left: 15px;">
    <h3 style="color:var(--text-light);">🛡️ Architecture Zero Trust + Machine Learning</h3>
    <b>But :</b> détecter les attaques discrètes (DDoS lent, exfiltration...) non captées par des règles fixes.
    </div>
    """, unsafe_allow_html=True)
    img1 = Image.open("neuralfirewall_diagram_correct.png")
    st.image(img1, caption="Architecture du NeuralFirewall")

    col1, col2 = st.columns(2)
    with col1:
        st.code("""
        from sklearn.ensemble import IsolationForest
        model = IsolationForest(n_estimators=100, contamination=0.01)
        model.fit(X_train)
        """, language='python')
        st.metric("Précision", "92.4%", "±1.2%")
    with col2:
        st.markdown("""
        📊 Features analysées :
        - Intervalle paquets
        - Ratio up/down
        - Payload entropy
        - IP géo
        - Heure d’activité
        """)
        st.metric("Temps d’analyse", "8.3ms")

    st.markdown("### 📉 Simulation de Trafic")

    attack_data = generate_attack_data()
    chart = alt.Chart(attack_data).mark_area().encode(
        x="Heure",
        y="Trafic",
        color=alt.condition(
            alt.datum.Alertes > 0,
            alt.value("#e74c3c"),
            alt.value("#4b8df8")
        )
    ).properties(height=300)
    st.altair_chart(chart, use_container_width=True)

    # VPN Project
    with st.expander("Infrastructure VPN Sécurisée", expanded=True):
        st.markdown("""
        <div style="border-left: 4px solid var(--secondary-accent); padding-left: 15px;">
        <h3 style="color:var(--text-light);">🔒 VPN Site-à-Site & Accès Distant</h3>
        - OpenVPN + LDAP + MFA  
        - Grafana + HAProxy  
        - VM dédiées pour chaque composant
        </div>
        """, unsafe_allow_html=True)

        img2 = Image.open("architecture_vpn_correct.png")
        st.image(img2, caption="Architecture du NeuralFirewall")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Latence Moyenne", "23ms")
        with col2:
            st.metric("Débit Garanti", "50Mbps")
        with col3:
            st.metric("Uptime", "99.98%")

        st.markdown("#### 📜 Extrait de configuration (Ansible)")
        st.code("""
        - name: Install OpenVPN
          apt:
            name: openvpn
            state: latest

        - name: Configure TLS
          template:
            src: tls.conf.j2
            dest: /etc/openvpn/server/tls.conf
            mode: '0600'

        - name: Enable MFA
          shell: ./google-authenticator --time-based --disallow-reuse --force --qr-mode=utf8
        """, language='yaml')

        st.markdown("""
        **🔐 Mesures de sécurité implémentées :**
        - Segmentation réseau
        - Audit quotidien
        - Rotation de certificats
        - Isolation KVM
        - Backups chiffrés
        """)

elif page == "🧑‍💼 Expériences":
    st.title("Parcours Professionnel")
    
    # HTML content for the experiences page, including CSS and the two experience cards.
    experiences_html = """
    <style>
        :root {
            --exp-bg-dark: rgba(30, 41, 59, 0.5);
            --exp-bg-hover: rgba(30, 41, 59, 0.7);
            --exp-text-title: #f8fafc;
            --exp-text-desc: #cbd5e1;
            --exp-text-date: #94a3b8;
            --exp-text-duration: #64748b;
            --exp-bg-desc: rgba(0, 0, 0, 0.2);
            --exp-text-tech: #38bdf8;
            --exp-text-highlight: #d1fae5;
            --exp-border: rgba(148, 163, 184, 0.15);
        }
        
        @media (prefers-color-scheme: light) {
            :root {
                --exp-bg-dark: rgba(226, 232, 240, 0.6);
                --exp-bg-hover: rgba(203, 213, 225, 0.4);
                --exp-text-title: #0f172a;
                --exp-text-desc: #334155;
                --exp-text-date: #64748b;
                --exp-text-duration: #475569;
                --exp-bg-desc: rgba(0, 0, 0, 0.05);
                --exp-text-tech: #0ea5e9;
                --exp-text-highlight: #047857;
                --exp-border: rgba(100, 116, 139, 0.2);
            }
        }
        
        .exp-container {
            display: flex;
            flex-direction: column;
            gap: 24px;
        }
        .exp-card-modern {
            background: linear-gradient(135deg, var(--exp-bg-dark) 0%, rgba(30, 41, 59, 0.3) 100%);
            border: 1px solid var(--exp-border);
            border-left: 4px solid #0ea5e9;
            border-radius: 12px;
            padding: 32px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }
        .exp-card-modern:hover {
            border-left-color: #10b981;
            box-shadow: 0 8px 24px rgba(14, 165, 233, 0.15);
            transform: translateX(4px);
            background: linear-gradient(135deg, var(--exp-bg-hover) 0%, rgba(30, 41, 59, 0.5) 100%);
        }
        .exp-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 16px;
            gap: 20px;
        }
        .exp-left {
            flex: 1;
        }
        .exp-right {
            flex-shrink: 0;
            text-align: right;
        }
        .exp-title {
            font-size: 1.4em;
            font-weight: 700;
            color: var(--exp-text-title);
            margin: 0 0 4px 0;
            line-height: 1.2;
        }
        .exp-company {
            font-size: 1.05em;
            color: #0ea5e9;
            font-weight: 600;
            margin: 0;
        }
        .exp-date {
            font-size: 0.95em;
            color: var(--exp-text-date);
            font-weight: 500;
            margin: 0;
        }
        .exp-duration {
            font-size: 0.85em;
            color: var(--exp-text-duration);
            background: rgba(14, 165, 233, 0.08);
            padding: 4px 10px;
            border-radius: 4px;
            display: inline-block;
            margin-top: 4px;
        }
        .exp-description {
            font-size: 1.05em;
            color: var(--exp-text-desc);
            margin: 16px 0;
            padding: 16px;
            background: var(--exp-bg-desc);
            border-radius: 8px;
            border-left: 3px solid #0ea5e9;
            line-height: 1.6;
        }
        .exp-section-label {
            font-size: 0.85em;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            color: #0ea5e9;
            font-weight: 700;
            margin: 20px 0 12px 0;
        }
        .exp-achievements {
            margin: 16px 0;
        }
        .exp-achievement {
            padding: 12px 0;
            padding-left: 24px;
            position: relative;
            color: var(--exp-text-desc);
            font-size: 1em;
            line-height: 1.5;
        }
        .exp-achievement::before {
            content: '→';
            position: absolute;
            left: 0;
            color: #10b981;
            font-weight: 700;
        }
        .exp-tech-stack {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin: 16px 0;
        }
        .exp-tech-badge {
            display: inline-block;
            padding: 6px 12px;
            background: rgba(14, 165, 233, 0.12);
            color: var(--exp-text-tech);
            border: 1px solid rgba(14, 165, 233, 0.25);
            border-radius: 6px;
            font-size: 0.9em;
            font-weight: 500;
            transition: all 0.2s ease;
        }
        .exp-tech-badge:hover {
            background: rgba(14, 165, 233, 0.2);
            border-color: rgba(14, 165, 233, 0.5);
            transform: translateY(-2px);
        }
        .exp-highlight {
            background: rgba(16, 185, 129, 0.08);
            border-left: 3px solid #10b981;
            padding: 12px 16px;
            border-radius: 6px;
            margin: 16px 0;
            color: var(--exp-text-highlight);
            font-size: 0.95em;
        }
    </style>
    <div class="exp-container">
        <div class="exp-card-modern">
            <div class="exp-header">
                <div class="exp-left">
                    <h3 class="exp-title">Analyste SOC (Stage)</h3>
                    <p class="exp-company">Orange Cyberdefense</p>
                </div>
                <div class="exp-right">
                    <p class="exp-date">Avril 2024 – Juin 2024</p>
                    <div class="exp-duration">3 mois</div>
                </div>
            </div>
            <div class="exp-description">
                Intégrée à l'équipe SOC, j'ai participé à la surveillance et à la protection d'infrastructures critiques en analysant les alertes de sécurité et en contribuant à la réponse sur incident.
            </div>
            <div class="exp-section-label">Réalisations Clés</div>
            <div class="exp-achievements">
                <div class="exp-achievement">Traitement et triage de centaines d'alertes de sécurité par jour via le SIEM <strong>QRadar</strong>.</div>
                <div class="exp-achievement">Investigation d'incidents (malware, phishing) en utilisant l'EDR <strong>Cortex XDR</strong> pour l'analyse de cause racine.</div>
                <div class="exp-achievement">Développement et automatisation de <strong>playbooks de réponse sur incident</strong> avec le SOAR <strong>Palo Alto XSOAR</strong>.</div>
                <div class="exp-achievement">Contribution à l'administration des accès (RBAC) sur serveurs Linux via <strong>Cisco ISE (TACACS+)</strong>.</div>
            </div>
            <div class="exp-section-label">Technologies</div>
            <div class="exp-tech-stack">
                <span class="exp-tech-badge">QRadar (SIEM)</span>
                <span class="exp-tech-badge">Cortex XDR</span>
                <span class="exp-tech-badge">Palo Alto XSOAR</span>
                <span class="exp-tech-badge">Ansible Tower</span>
                <span class="exp-tech-badge">Cisco ISE</span>
                <span class="exp-tech-badge">Linux</span>
            </div>
            <div class="exp-highlight">
                <strong>Point fort :</strong> Première expérience opérationnelle en détection et réponse, confirmant mon objectif de m'orienter vers une carrière en Blue Team.
            </div>
        </div>
        <div class="exp-card-modern">
            <div class="exp-header">
                <div class="exp-left">
                    <h3 class="exp-title">Apprentie Ingénieure Réseaux & Cybersécurité</h3>
                    <p class="exp-company">SIPPEREC</p>
                </div>
                <div class="exp-right">
                    <p class="exp-date">Septembre 2022 – Septembre 2026</p>
                    <div class="exp-duration">4 ans</div>
                </div>
            </div>
            <div class="exp-description">
                En charge de l'amélioration continue de la sécurité des infrastructures réseau à travers l'audit, l'analyse de conformité et le développement d'outils d'automatisation.
            </div>
            <div class="exp-section-label">Réalisations Clés</div>
            <div class="exp-achievements">
                <div class="exp-achievement"><strong>Développement d'un outil d'audit en Python</strong> pour analyser et valider automatiquement les configurations réseau, réduisant le temps d'analyse de plusieurs jours à quelques heures.</div>
                <div class="exp-achievement">Conception et mise en place d'une <strong>base de données PostgreSQL</strong> pour historiser les audits et suivre les indicateurs de conformité.</div>
                <div class="exp-achievement"><strong>Automatisation de la détection d'anomalies</strong> (écarts de configuration, vulnérabilités) dans les architectures des délégataires.</div>
                <div class="exp-achievement">Rédaction de <strong>rapports d'audit de sécurité</strong> et présentation des recommandations aux équipes techniques.</div>
            </div>
            <div class="exp-section-label">Technologies</div>
            <div class="exp-tech-stack">
                <span class="exp-tech-badge">Python (Pandas, Scapy)</span>
                <span class="exp-tech-badge">PostgreSQL</span>
                <span class="exp-tech-badge">GIT</span>
                <span class="exp-tech-badge">Sécurité Réseau (Firewalls, VPN, 802.1X)</span>
                <span class="exp-tech-badge">Audit Technique</span>
            </div>
            <div class="exp-highlight">
                <strong>Point fort :</strong> Forte montée en compétence sur l'automatisation de la sécurité ("Security as Code") et l'analyse de données pour la cyberdéfense.
            </div>
        </div>
    </div>
    """
    components.html(experiences_html, height=1400)
    
    # Synthèse du parcours
    st.markdown("""
    <style>
        .synthesis-container {
            margin: 40px 0;
            padding: 32px;
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.08) 0%, rgba(14, 165, 233, 0.08) 100%);
            border: 1px solid rgba(14, 165, 233, 0.2);
            border-radius: 12px;
        }
        .synthesis-title {
            color: var(--text-muted);
            margin-top: 0;
            font-size: 1.3em;
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .synthesis-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        .synthesis-card {
            padding: 16px;
            background: var(--bg-overlay);
            border-radius: 8px;
        }
        .synthesis-number {
            font-weight: 700;
            font-size: 1.8em;
            margin-bottom: 4px;
        }
        .synthesis-text {
            color: var(--text-muted);
            font-size: 0.95em;
        }
    </style>
    <div class="synthesis-container">
        <h3 class="synthesis-title">
            Synthèse du Parcours
        </h3>
        <div class="synthesis-grid">
            <div class="synthesis-card">
                <div class="synthesis-number" style="color: #10b981;">4 ans</div>
                <div class="synthesis-text">d'expérience en cybersécurité<br/>(apprentissage + stage)</div>
            </div>
            <div class="synthesis-card">
                <div class="synthesis-number" style="color: #0ea5e9;">2 expériences clés</div>
                <div class="synthesis-text">Orange Cyberdefense (SOC)<br/>SIPPEREC (Réseau & Audit)</div>
            </div>
            <div class="synthesis-card">
                <div class="synthesis-number" style="color: #f59e0b;">100 %</div>
                <div class="synthesis-text">Projets avec impact<br/>métier mesurable</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Section détaillée pour le projet phare
    st.markdown("---")
    st.header("🛠️ Projet Phare: Automatisation des Audits Réseau")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Contexte", "Solution", "Résultats", "Code Exemple"])
    
    with tab1:
        st.markdown("""
        ### Le Défi
        - **Problème:** Processus manuel fastidieux pour analyser les livrables réseau (Excel)
        - **Volume:** 50+ audits/mois avec 1000+ équipements chacun
        - **Délai:** 2 jours/audit en analyse manuelle
        
        <div style="background-color: rgba(255, 255, 255, 0.05); padding: 15px; border-radius: 8px; margin: 15px 0;">
            <b>🕵️‍♀️ Constat :</b> 80% du temps passé sur des tâches répétitives (vérification de cohérence, recherche d'anomalies)
        </div>
        """, unsafe_allow_html=True)
        
        st.image("https://via.placeholder.com/800x400?text=Processus+Manuel+vs+Automatisé", use_column_width=True)
    
    with tab2:
        st.markdown("""
        ### Architecture de la Solution
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **📦 Composants :**
            1. Module d'import Excel → DataFrame
            2. Moteur de règles (200+ checks)
            3. Génération de rapports (PDF/Excel)
            4. Dashboard PowerBI
            
            **⚙️ Fonctionnalités :**
            - Détection automatique des anomalies
            - Scoring de vulnérabilités
            - Alertes prioritaires
            """)
        with col2:
            st.image("https://via.placeholder.com/400x300?text=Architecture+Solution", use_column_width=True)
        
        st.markdown("""
        ```python
        def analyze_network_data(df):
            # 1. Vérification des doublons
            dup_analysis = check_duplicates(df)
            
            # 2. Validation des configurations
            config_errors = validate_configs(df)
            
            # 3. Calcul du score de sécurité
            security_score = calculate_score(dup_analysis, config_errors)
            
            return generate_report(security_score)
        ```
        """)
    
    with tab3:
        st.markdown("""
        ### Impact Mesurable
        """)
        
        metrics = {
            "Temps d'analyse": ("⏱️", "2 jours → 2 heures", "-92%"),
            "Précision": ("🎯", "85% → 99%", "+14%"),
            "Couverture": ("🔍", "50 checks → 200+", "+300%")
        }
        
        cols = st.columns(3)
        for i, (name, (icon, value, delta)) in enumerate(metrics.items()):
            cols[i].metric(f"{icon} {name}", value, delta)
        
        st.image("https://via.placeholder.com/800x400?text=Dashboard+PowerBI+Résultats", use_column_width=True)
    
    with tab4:
        st.markdown("""
        ### Extrait Significatif
        """)
        
        code = """# Fonction principale d'analyse
def process_audit(file_path):
    try:
        # Chargement des données
        df = pd.read_excel(file_path)
        
        # Nettoyage initial
        df = clean_data(df)
        
        # Analyse des vulnérabilités
        results = {
            'weak_passwords': detect_weak_passwords(df),
            'config_errors': find_config_errors(df),
            'compliance': check_compliance(df)
        }
        
        # Génération du rapport
        report = generate_report(results)
        return report
        
    except Exception as e:
        log_error(e)
        raise AuditException(f"Erreur traitement: {str(e)}")
        """
        st.code(code, language='python')
        
        st.download_button(
            label="📥 Télécharger un exemple de sortie",
            data=pd.DataFrame({
                'Équipement': ['SW-001', 'RT-002', 'FW-003'],
                'Vulnérabilités': [2, 5, 1],
                'Score': [85, 60, 95]
            }).to_csv(index=False).encode('utf-8'),
            file_name="exemple_rapport_audit.csv",
            mime='text/csv'
        )

    # Section compétences acquises
    st.markdown("---")
    st.header("📈 Compétences Développées")
    
    skills = {
        "Analytique": ["Analyse de logs", "Corrélation d'événements", "Tri des alertes"],
        "Technique": ["QRadar", "Python", "XSOAR", "Cortex XDR"],
        "Gestion": ["Documentation", "Priorisation", "Reporting"]
    }
    
    cols = st.columns(3)
    for i, (category, items) in enumerate(skills.items()):
        with cols[i]:
            st.markdown(f"### {category}")
            for item in items:
                st.markdown(f"- {item}")
    
    st.markdown("""
    <div style="background-color: rgba(14, 165, 233, 0.1); padding: 15px; border-radius: 8px; margin-top: 20px;">
        <h3 style="color: #38bdf8;">Synthèse</h3>
        <p style="color: #cbd5e1;">La sécurité est un équilibre constant entre <b>automatisation</b> et <b>expertise humaine</b>.
        Mes outils réduisent le bruit mais c'est mon analyse qui fait la différence sur les vrais threats.</p>
    </div>
    """, unsafe_allow_html=True)

# Compétences
elif page == "🛠️ Compétences":
    
    st.title("Compétences Techniques")
    
    # Section principale avec onglets
    tab1, tab2, tab3, tab4 = st.tabs(["Techniques", "Sécurité", "Apprentissage", "Soft Skills"])

    with tab1:
        st.markdown("### Compétences Techniques")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div style="background-color: var(--bg-card); padding: 20px; border-radius: 10px; border-left: 4px solid #0ea5e9; margin-bottom: 20px;">
                <h4 style="color: var(--text-light); border-bottom: 1px solid var(--border-color); padding-bottom: 8px;">Réseaux</h4>
                <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px;">
                    <span style="background-color: #0ea5e9; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">TCP/IP</span>
                    <span style="background-color: #0ea5e9; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">OSPF/BGP</span>
                    <span style="background-color: #0ea5e9; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">VLAN</span>
                    <span style="background-color: #0ea5e9; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">DNS/DHCP</span>
                    <span style="background-color: #0ea5e9; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">VPN</span>
                    <span style="background-color: #0ea5e9; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Firewall</span>
                </div>
            </div>
            
            <div style="background-color: var(--bg-card); padding: 20px; border-radius: 10px; border-left: 4px solid #0ea5e9; margin-bottom: 20px;">
                <h4 style="color: var(--text-light); border-bottom: 1px solid var(--border-color); padding-bottom: 8px;">Systèmes</h4>
                <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px;">
                    <span style="background-color: #0ea5e9; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Linux (Debian/Kali)</span>
                    <span style="background-color: #0ea5e9; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Windows Server</span>
                    <span style="background-color: #0ea5e9; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Docker</span>
                    <span style="background-color: #0ea5e9; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Virtualisation</span>
                    <span style="background-color: #0ea5e9; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Active Directory</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div style="background-color: var(--bg-card); padding: 20px; border-radius: 10px; border-left: 4px solid #10b981; margin-bottom: 20px;">
                <h4 style="color: var(--text-light); border-bottom: 1px solid var(--border-color); padding-bottom: 8px;">Développement</h4>
                <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px;">
                    <span style="background-color: #10b981; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Python</span>
                    <span style="background-color: #10b981; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Bash</span>
                    <span style="background-color: #10b981; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Java</span>
                    <span style="background-color: #10b981; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">SQL</span>
                    <span style="background-color: #10b981; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">PowerShell</span>
                    <span style="background-color: #10b981; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">HTML/CSS</span>
                </div>
            </div>
            
            <div style="background-color: var(--bg-card); padding: 20px; border-radius: 10px; border-left: 4px solid #10b981; margin-bottom: 20px;">
                <h4 style="color: var(--text-light); border-bottom: 1px solid var(--border-color); padding-bottom: 8px;">Outils</h4>
                <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px;">
                    <span style="background-color: #10b981; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Git</span>
                    <span style="background-color: #10b981; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Jira</span>
                    <span style="background-color: #10b981; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Ansible</span>
                    <span style="background-color: #10b981; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Terraform</span>
                    <span style="background-color: #10b981; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">PostgreSQL</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with tab2:
        st.markdown("### 🛡️ Expertise Cybersécurité")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div style="background-color: var(--bg-card); padding: 20px; border-radius: 10px; border-left: 4px solid #8b5cf6; margin-bottom: 20px;">
                <h4 style="color: var(--text-light); border-bottom: 1px solid var(--border-color); padding-bottom: 8px;">Analyse & Protection</h4>
                <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px;">
                    <span style="background-color: #8b5cf6; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">SIEM (QRadar)</span>
                    <span style="background-color: #8b5cf6; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">XDR (Cortex)</span>
                    <span style="background-color: #8b5cf6; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">SOAR (XSOAR)</span>
                    <span style="background-color: #8b5cf6; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">ELK Stack</span>
                    <span style="background-color: #8b5cf6; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Kibana</span>
                </div>
            </div>
            
            <div style="background-color: var(--bg-card); padding: 20px; border-radius: 10px; border-left: 4px solid #8b5cf6; margin-bottom: 20px;">
                <h4 style="color: var(--text-light); border-bottom: 1px solid var(--border-color); padding-bottom: 8px;">Normes & Cadres</h4>
                <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px;">
                    <span style="background-color: #8b5cf6; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">ISO 27001</span>
                    <span style="background-color: #8b5cf6; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">RGPD</span>
                    <span style="background-color: #8b5cf6; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">NIST CSF</span>
                    <span style="background-color: #8b5cf6; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">OWASP</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div style="background-color: var(--bg-card); padding: 20px; border-radius: 10px; border-left: 4px solid #f59e0b; margin-bottom: 20px;">
                <h4 style="color: var(--text-light); border-bottom: 1px solid var(--border-color); padding-bottom: 8px;">Pentest & Red Team</h4>
                <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px;">
                    <span style="background-color: #f59e0b; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Metasploit</span>
                    <span style="background-color: #f59e0b; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Burp Suite</span>
                    <span style="background-color: #f59e0b; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Nmap</span>
                    <span style="background-color: #f59e0b; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Wireshark</span>
                    <span style="background-color: #f59e0b; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">John the Ripper</span>
                </div>
            </div>
            
            <div style="background-color: var(--bg-card); padding: 20px; border-radius: 10px; border-left: 4px solid #f59e0b; margin-bottom: 20px;">
                <h4 style="color: var(--text-light); border-bottom: 1px solid var(--border-color); padding-bottom: 8px;">Sécurité Offensive</h4>
                <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px;">
                    <span style="background-color: #f59e0b; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">OSINT</span>
                    <span style="background-color: #f59e0b; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Social Engineering</span>
                    <span style="background-color: #f59e0b; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">PrivEsc</span>
                    <span style="background-color: #f59e0b; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">CTF</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with tab3:
        st.markdown("### 📚 Formation Continue")
        
        st.markdown("""
        
        <div style="background-color: var(--bg-card); padding: 20px; border-radius: 10px; margin-bottom: 20px;">
            <h4 style="color: var(--text-light); border-bottom: 1px solid var(--border-color); padding-bottom: 8px;">Ressources</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; margin-top: 12px;">
                <div style="background-color: var(--bg-subtle); color: var(--text-light); padding: 10px; border-radius: 8px;">
                    <b>📖 Lectures</b><br>SANS, Medium, ZDNet
                </div>
                <div style="background-color: var(--bg-subtle); color: var(--text-light);  padding: 10px; border-radius: 8px;">
                    <b>🎧 Podcasts</b><br>NoLimitSecu, CyberUncut
                </div>
                <div style="background-color: var(--bg-subtle); color: var(--text-light);  padding: 10px; border-radius: 8px;">
                    <b>📺 Vidéos</b><br>LiveOverflow, The Cyber Mentor
                </div>
                <div style="background-color: var(--bg-subtle); padding: 10px; color: var(--text-light);  border-radius: 8px;">
                    <b>💬 Événements</b><br>FIC, Root-Me, Meetups
                </div>
            </div>
        </div>
        
        <div style="background-color: var(--bg-card); padding: 20px; border-radius: 10px;">
            <h4 style="color: var(--text-light); border-bottom: 1px solid var(--border-color); padding-bottom: 8px;">Plateformes</h4>
            <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px;">
                <span style="background-color: #0ea5e9; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Youtube</span>
                <span style="background-color: #0ea5e9; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">HackTheBox</span>
                <span style="background-color: #0ea5e9; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Root-Me</span>
                <span style="background-color: #0ea5e9; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">OpenClassrooms</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with tab4:
        st.markdown("### 🤝 Soft Skills & Méthodologie")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div style="background-color: rgba(16, 185, 129, 0.1); padding: 15px; border-radius: 8px; margin-bottom: 20px;">
                <h4 style="color: #10b981; margin-top: 0; border-bottom: 1px solid rgba(16, 185, 129, 0.2); padding-bottom: 8px;">Cognitives</h4>
                <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px;">
                    <span style="background-color: #10b981; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Résolution de problèmes</span>
                    <span style="background-color: #10b981; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Curiosité</span>
                    <span style="background-color: #10b981; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Adaptabilité</span>
                    <span style="background-color: #10b981; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Rigueur</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div style="background-color: rgba(245, 158, 11, 0.1); padding: 15px; border-radius: 8px; margin-bottom: 20px;">
                <h4 style="color: #f59e0b; margin-top: 0; border-bottom: 1px solid rgba(245, 158, 11, 0.2); padding-bottom: 8px;">Relationnelles</h4>
                <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px;">
                    <span style="background-color: #f59e0b; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Pédagogie</span>
                    <span style="background-color: #f59e0b; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Travail d'équipe</span>
                    <span style="background-color: #f59e0b; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Communication</span>
                    <span style="background-color: #f59e0b; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Écoute active</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Section Méthodologie
        st.markdown("""
        <div style="background-color: var(--bg-card); padding: 20px; border-radius: 10px; margin-top: 20px;">
            <h4 style="color: var(--text-light); border-bottom: 1px solid var(--border-color); padding-bottom: 8px;">Méthodologie de travail</h4>
            <ul style="margin-top: 12px; color: var(--text-muted); padding-left: 20px;">
                <li style="margin-bottom: 8px;"><b>Approche itérative :</b> Test → Analyse → Amélioration</li>
                <li style="margin-bottom: 8px;"><b>Documentation systématique</b> des processus</li>
                <li style="margin-bottom: 8px;"><b>Veille technologique</b> hebdomadaire</li>
                <li><b>Retrospective</b> après chaque projet</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        # Citation
        st.markdown("""
        <div style="background-color: var(--bg-subtle); padding: 15px; border-radius: 8px; margin-top: 20px;">
            <p style="margin: 0; font-style: italic; color: var(--text-muted); text-align: center;">
                "La sécurité est un état d'esprit avant d'être une compétence technique.<br>
                La vigilance permanente et la remise en question sont mes mantras."
            </p>
        </div>
        """, unsafe_allow_html=True)

# CV
elif page == "📄 CV":
    st.title("📄 Mon CV Interactif")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("""
        ### 📌 Version PDF
        Voici mon CV détaillé au format PDF. Vous pouvez le visualiser directement ici ou le télécharger.
        """)
        
        try:
            with open("CV_Seynabou_Sougou.pdf", "rb") as file:
                pdf_bytes = file.read()
                base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
                pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
                st.markdown(pdf_display, unsafe_allow_html=True)
                
                st.download_button(
                    label="📥 Télécharger le CV",
                    data=pdf_bytes,
                    file_name="CV_Seynabou_Sougou_2026.pdf",
                    mime="application/pdf"
                )
        except FileNotFoundError:
            st.error("Le fichier CV.pdf est introuvable. Veuillez me contacter pour l'obtenir.")

    
    with col2:
        st.markdown("""
        ### 🎯 Profil Rapide
        **Seynabou Sougou**  
        *Future Ingénieure en Cybersécurité (2026)*
        
        ---
        
        🛡️ **Spécialité**  
        Audit, Sécurité Infrastructure & Automatisation
        
        🔧 **Compétences Clés**  
        Python, Audit de sécurité, Réseau, Linux, Conformité (RGPD, ISO 27001)
        
        💼 **Expériences**  
        SIPPEREC (Audit & Automatisation), Orange Cyberdefense (SOC)
        
        📍 **Mobilité**  
        Paris, Toulouse, France
        """)
        
        st.markdown("---")

        st.markdown("""
        ### 📊 Indicateurs
        - Automatisation de **+10 processus d'audit** via Python
        - **+100 analyses** de données de sécurité
        - Rédaction de **+20 documents** techniques (rapports, référentiels)
        - Maintenance d'un **lab de sécurité personnel** (Active Directory, SIEM)
        """)
        
        st.markdown("---")

        st.markdown("""
        ### 🔎 Ce que je recherche
        Un CDI en **audit cybersécurité**, **sécurité des infrastructures** ou **GRC technique**, dans une équipe de type SecOps (hors 24/7).
        """)

# Contact
elif page == "📱 Contact":
    st.title("Contact Professionnel")
    
    # Section contacts
    st.markdown("### 🤝 Discutons de votre sécurité")
    st.info("À la recherche d'un poste en CDI à partir de Septembre 2026.")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **📧 Email pro :**  
        [seynabousougou21@gmail.com](mailto:seynabousougou21@gmail.com)  
        *(Réponse garantie sous 48h)*

        **📱 Téléphone :**  
        [+33 6 67 04 73 41](tel:+33667047341)  
        

        **💼 LinkedIn :**  
        [Seynabou Sougou](https://www.linkedin.com/in/seynabousougou/)  
        
        """)

    with col2:
        st.markdown("""
        **🐱‍💻 GitHub :**  
        [github.com/seynabou-s](https://github.com/seynabou-s)  
        *(Projets publics et contributions)*

        **📍 Localisation :**  
        Paris, France  
        *(Mobile sur toute la France)*
        """)

    st.markdown("---")
    
    # Section disponibilités
    st.markdown("### 📅 Mes disponibilités")
    st.markdown("""
    ✅ **Ouverte aux opportunités pour :**
    - CDI (Ingénieur Cybersécurité / SOC / Pentest) - **Dès Septembre 2026**
    - Échanges techniques et retours d'expérience
    """)
    
    
    # Formulaire de contact
    with st.form("contact_form", clear_on_submit=True):
        st.markdown("### ✉️ Formulaire de contact direct")
        
        name = st.text_input("Nom complet*", placeholder="Votre nom")
        email = st.text_input("Email*", placeholder="email@exemple.com")
        message = st.text_area("Message*", placeholder="Votre message...", height=150)
        
        submitted = st.form_submit_button("Envoyer le message 🔒")
        
        if submitted:
            if not all([name, email, message]):
                st.error("Veuillez remplir tous les champs obligatoires (*)")
            else:
                try:
                    import smtplib
                    from email.message import EmailMessage

                    msg = EmailMessage()
                    msg.set_content(f"""
Nom: {name}
Email: {email}
Message:
{message}
""")
                    msg['Subject'] = f"Nouveau message de {name}"
                    msg['From'] = "seynabousougou21@gmail.com"
                    msg['To'] = "seynabousougou21@gmail.com"

                    with smtplib.SMTP('smtp.gmail.com', 587) as server:
                        server.starttls()
                        server.login("seynabousougou21@gmail.com", "fugmyyfhtuoxsfda")
                        server.send_message(msg)

                    st.success("✅ Message envoyé avec succès !")
                    st.balloons()
                except Exception as e:
                    st.error(f"❌ Erreur : {e}. Contactez-moi directement par email.")
