import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import base64
import pandas as pd
import altair as alt
import random
import requests
import numpy as np
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
    page_title="Seynabou Sougou - Cyber Ninja 🐱‍👤",
    layout="wide",
    page_icon="🛡️",
    initial_sidebar_state="expanded"
)

# CSS personnalisé
st.markdown("""
<style>
    .main {
        background-color: #1e1e1e;
    }
    .st-emotion-cache-1kyxreq {
        justify-content: center;
    }
    .big-font {
        font-size:24px !important;
        font-weight: bold !important;
        color: #333333;
    }
    .fun-fact {
        background-color: #e6f7ff;
        border-radius: 10px;
        padding: 10px;
        margin: 10px 0;
        color: #333333;
        border-left: 4px solid #4b8df8;
    }
    .hack-animation {
        font-family: monospace;
        color: #00aa00;
        background-color: #111111;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .project-card {
        border-left: 5px solid #4b8df8;
        padding: 20px;
        background-color: #ffffff;
        border-radius: 0 10px 10px 0;
        margin: 20px 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        color: #000000;

    }
    .skill-badge {
        display: inline-block;
        padding: 6px 12px;
        margin: 5px;
        background-color: #4b8df8;
        color: white;
        border-radius: 20px;
        font-size: 14px;
        font-weight: 500;
    }
    .header {
        color: #2c3e50;
        border-bottom: 2px solid #4b8df8;
        padding-bottom: 10px;
    }
    .stButton>button {
        background-color: #4b8df8;
        color: white;
        border-radius: 5px;
        padding: 8px 16px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #3a7bd5;
        color: white;
    }
    .sidebar .sidebar-content {
        background-color: #2c3e50;
    }
    #MainMenu, footer, header {
    visibility: hidden;
    }
    .accueil-container {
    color: #ffffff;
    background: linear-gradient(135deg, rgba(30, 30, 45, 0.95), rgba(45, 45, 70, 0.95));
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border-radius: 16px;
    padding: 30px;
    margin: 20px 0;
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.2);
    border: 1px solid rgba(255, 255, 255, 0.15);
    font-family: 'Segoe UI', 'Roboto', sans-serif;
}
.accueil-title {
    color: #4b8df8;
    margin-top: 0;
    border-bottom: 2px solid rgba(75, 141, 248, 0.3);
    padding-bottom: 10px;
}
.accent-text {
    font-weight: bold;
    background: linear-gradient(90deg, #4b8df8, #00c6ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.accent-text2 {
    font-weight: bold;
    background: linear-gradient(90deg, #ff4b4b, #ff8c00);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.accent-text3 {
    font-weight: bold;
    background: linear-gradient(90deg, #8e44ad, #e74c3c);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.specialties-list {
    margin-top: 10px;
    padding-left: 20px;
}
.specialties-list li {
    margin-bottom: 8px;
}
.quote-box {
    margin-top: 25px;
    padding: 12px;
    background: rgba(75, 141, 248, 0.15);
    border-radius: 8px;
    border-left: 4px solid #4b8df8;
}

</style>
""", unsafe_allow_html=True)

# Sidebar (menu)
with st.sidebar:
    st.title("🔍 Navigation")
    st.image("https://media.giphy.com/media/L1R1tvI9svkIWwpVYr/giphy.gif", use_container_width=True)
    page = st.radio("Choisissez votre destination:", 
               ["🏠 Accueil", "🚀 Projets", "🧑‍💼 Expériences", "🛠️ Compétences", "📄 CV", "🗓️ Calendrier", "📱 Contact"])

    st.markdown("---")
    st.markdown("""
    <div class="fun-fact">
    <b>💡 Saviez-vous ?</b><br>
    Le premier virus informatique s'appelait "Creeper" en 1971 et affichait simplement le message "I'm the creeper, catch me if you can!"
    </div>
    """, unsafe_allow_html=True)

# Accueil
if page == "🏠 Accueil":
    st.title("👋 Bienvenue dans mon bunker numérique!")
    
    col1, col2 = st.columns([1, 3])
    with col1:
        img = Image.open("photo_seynabou.jpeg")
        st.image(img, caption="Seynabou Sougou - Cyber Gardienne", width=250)
        st.markdown("""
        <div style="text-align:center">
            <img src="https://media.giphy.com/media/QssGEmpkyEOhBCb7e1/giphy.gif" width="100">
            <p style="color:#ffffff;"><i>"Paranoïaque ? Non, juste prudente"</i></p>
        </div>
        """, unsafe_allow_html=True)

    # Dans votre section Accueil, remplacez le contenu de with col2: par ceci :
    with col2:
        st.markdown("""
            <div style="color: #ffffff;
                        background: linear-gradient(135deg, rgba(30, 30, 45, 0.95) 0%, rgba(45, 45, 70, 0.95) 100%);
                        backdrop-filter: blur(10px);
                        -webkit-backdrop-filter: blur(10px);
                        border-radius: 16px;
                        padding: 30px;
                        margin: 20px 0;
                        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.2);
                        border: 1px solid rgba(255, 255, 255, 0.15);
                        font-family: 'Segoe UI', 'Roboto', sans-serif;">
            
            <h2 style="color: #4b8df8; margin-top: 0; border-bottom: 2px solid rgba(75, 141, 248, 0.3); padding-bottom: 10px;">
                Salut, moi c'est Seynabou SOUGOU!
            </h2>
            
            <div style="font-size: 1.1em; line-height: 1.6; margin: 15px 0;">
                <span style="background: linear-gradient(90deg, #4b8df8, #00c6ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: bold;">
                    Apprentie ingénieure en cybersécurité
                </span> par jour, 
                <span style="background: linear-gradient(90deg, #ff4b4b, #ff8c00); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: bold;">
                    hackeuse éthique
                </span> par passion, et 
                <span style="background: linear-gradient(90deg, #8e44ad, #e74c3c); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: bold;">
                    mangeuse de cookies
                </span> 🍪 (seulement ceux du navigateur).
            </div>
            
            <div style="font-size: 1.05em; line-height: 1.6; margin: 15px 0;">
                Mon quotidien ? Protéger le monde numérique contre les forces obscures du dark web! 
                <span style="font-style: italic;">(Ou au moins essayer)</span>
            </div>
            
            <h3 style="color: #4b8df8; margin-top: 20px; border-bottom: 1px solid rgba(75, 141, 248, 0.3); padding-bottom: 5px;">
                🔥 Spécialités :
            </h3>
            <ul style="margin-top: 10px; padding-left: 20px;">
                <li style="margin-bottom: 8px;">Construire des forteresses numériques 🏰</li>
                <li style="margin-bottom: 8px;">Traquer les intrus comme John Wick 🐶</li>
                <li style="margin-bottom: 8px;">Automatiser tout ce qui bouge (et ce qui ne bouge pas aussi) 🤖</li>
            </ul>

            </div>
        """, unsafe_allow_html=True)


        st.markdown("""
        <div class="fun-fact">
        <b>⚡ Fun fact :</b> Saviez-vous que 95% des cyberattaques sont dues à des erreurs humaines ? 
        C'est pour ça que je passe mon temps à crier "NE CLIQUEZ PAS SUR CE LIEN !" à mes proches.
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📈 Mes Stats de Cyber-Guerrière")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("☕ Tasses de café/jour", "3", "+1 quand il y a un bug")
    with col2:
        st.metric("🚨 Alertes traitées", "42", help="Cette semaine seulement!")
    with col3:
        st.metric("💻 Lignes de code", "∞", "Et toujours un ';' qui manque")

# Projets
elif page == "🚀 Projets":
    st.title("🚀 Mes Missions Secrètes (enfin, pas trop)")

    # Projet 1 : Pentest
    with st.expander("🔐 Projet 1 : Simulateur de Cyberattaques - Le Jeu du Chat et de la Souris", expanded=True):
        st.markdown("""
        <div class="project-card">
        <h3 style="color:#1e1e1e;">🎮 Le Pentest dont vous êtes le héros</h3>
        J'ai créé un <b>lab ultra-réaliste</b> où je joue à la fois le méchant hacker et le gentil admin.
        🔧 <b>Arsenal :</b> Kali Linux, Metasploit, Wireshark, Ettercap
        🎯 <b>Objectif :</b> Comprendre comment pensent les méchants pour mieux les stopper!
        </div>
        """, unsafe_allow_html=True)

        tab1, tab2, tab3 = st.tabs(["📈 Statistiques", "🎥 Scénario", "💡 Leçon"])

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
            **Scénario :** Un attaquant essaie de deviner les mots de passe SSH  
            1. Scan réseau  
            2. Port SSH trouvé  
            3. Brute-force  
            4. Fail2ban active !  
            """)
            if st.button("🚨 Lancer une simulation d'attaque (safe)"):
                st.markdown("""
                <div class="hack-animation">
                > ssh admin@192.168.1.1<br>
                > Password: ********<br>
                > Permission denied<br>
                > Password: ********<br>
                > Connection closed by 192.168.1.1 [FAIL2BAN]
                </div>
                """, unsafe_allow_html=True)
                st.success("✅ Attaque bloquée avec succès !")

        with tab3:
            st.markdown("""
            **💡 Ce que j'ai appris :**
            - Les mots de passe faibles = danger
            - Fail2ban est mon ami
            - Ne jamais activer SSH root
            """)

    # Projet 2 : ELK
    with st.expander("📊 Projet 2 : Chasse aux menaces avec ELK", expanded=True):
        st.markdown("""
        <div class="project-card">
        <h3 style="color:#2c3e50;">🔍 Mon mini-SIEM maison</h3>
        Stack ELK (ElasticSearch, Logstash, Kibana) + logs SSH + alertes
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
            🔎 Mon workflow :
            - Je vois l’alerte
            - Je vérifie
            - Je corrige ou automatise
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
    st.subheader("🔥 NeuralFirewall - Système de détection IA")

    st.markdown("""
    <div style="border-left: 4px solid #e74c3c; padding-left: 15px;">
    <h3 style="color:#e74c3c;">🛡️ Architecture Zero Trust + Machine Learning</h3>
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

    st.markdown("### 📉 Dashboard de Menaces (simulation)")

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
    with st.expander("🌐 SeynaBoss VPN - Infrastructure Zero Trust", expanded=True):
        st.markdown("""
        <div style="border-left: 4px solid #3498db; padding-left: 15px;">
        <h3 style="color:#3498db;">🔒 VPN sécurisé pour entreprise multi-sites</h3>
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
        🔐 Mesures de sécurité :
        - Segmentation réseau
        - Audit quotidien
        - Rotation de certificats
        - Isolation KVM
        - Backups chiffrés
        """)

elif page == "🧑‍💼 Expériences":
    st.title("💼 Mon Parcours Professionnel")
    
    # Style CSS supplémentaire
    st.markdown("""
    <style>
        .timeline {
            position: relative;
            max-width: 1200px;
            margin: 0 auto;
        }
        .timeline::after {
            content: '';
            position: absolute;
            width: 6px;
            background-color: #4b8df8;
            top: 0;
            bottom: 0;
            left: 50%;
            margin-left: -3px;
        }
        .exp-card {
            padding: 10px 40px;
            position: relative;
            background-color: inherit;
            width: 50%;
        }
        .exp-card::after {
            content: '';
            position: absolute;
            width: 25px;
            height: 25px;
            right: -17px;
            background-color: white;
            border: 4px solid #FF9F55;
            top: 15px;
            border-radius: 50%;
            z-index: 1;
        }
        .left {
            left: 0;
        }
        .right {
            left: 50%;
        }
        .left::before {
            content: " ";
            height: 0;
            position: absolute;
            top: 22px;
            width: 0;
            z-index: 1;
            right: 30px;
            border: medium solid white;
            border-width: 10px 0 10px 10px;
            border-color: transparent transparent transparent white;
        }
        .right::before {
            content: " ";
            height: 0;
            position: absolute;
            top: 22px;
            width: 0;
            z-index: 1;
            left: 30px;
            border: medium solid white;
            border-width: 10px 10px 10px 0;
            border-color: transparent white transparent transparent;
        }
        .right::after {
            left: -16px;
        }
        .exp-content {
            padding: 20px 30px;
            background-color: white;
            position: relative;
            border-radius: 6px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .tech-badge {
            display: inline-block;
            padding: 3px 8px;
            margin: 3px;
            background-color: #e6f7ff;
            color: #0066cc;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 500;
        }
        .screenshot {
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 5px;
            margin: 10px 0;
            max-width: 100%;
        }
    </style>
    """, unsafe_allow_html=True)

    # Timeline des expériences
    st.markdown("""
    <div class="timeline">
        <!-- Expérience 1 - SOC Analyst -->
        <div class="exp-card left">
            <div class="exp-content">
                <h3>🔍 Analyste SOC</h3>
                <h4>Orange Cyberdefense | 2024-2024</h4>
                <p>Surveillance proactive des infrastructures critiques et réponse aux incidents de sécurité</p>
                
                <div style="margin: 15px 0;">
                    <img src="https://via.placeholder.com/600x300?text=QRadar+Dashboard" alt="QRadar Dashboard" class="screenshot" style="width:100%">
                    <p><i>Capture de mon dashboard QRadar personnalisé</i></p>
                </div>
                
                <h5>🚀 Réalisations clés :</h5>
                <ul>
                    <li>Analyse de <b>150+ alertes/jour</b> sur QRadar avec triage automatisé</li>
                    <li>Création de <b>12 playbooks XSOAR</b> réduisant le temps de réponse de 40%</li>
                    <li>Intégration réussie Cortex XDR avec enrichissement automatique des alertes</li>
                </ul>
                
                <h5>🛠️ Technologies utilisées :</h5>
                <div style="margin: 10px 0;">
                    <span class="tech-badge">QRadar</span>
                    <span class="tech-badge">Cortex XDR</span>
                    <span class="tech-badge">XSOAR</span>
                    <span class="tech-badge">Ansible</span>
                    <span class="tech-badge">Python</span>
                </div>
                
                <button onclick="alert('Détails techniques disponibles sur demande')" style="background-color: #4b8df8; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">
                    Voir un exemple de playbook
                </button>
            </div>
        </div>
        
        <!-- Expérience 2 - Apprentie Réseaux Sécurité -->
        <div class="exp-card right">
            <div class="exp-content">
                <h3>🛡️ Apprentie Réseaux & Sécurité</h3>
                <h4>Société Générale | 2022-2025</h4>
                <p>Audit et sécurisation des infrastructures réseau du groupe</p>
                
                <div style="margin: 15px 0;">
                    <img src="https://via.placeholder.com/600x300?text=Script+Python+Analyse+Réseau" alt="Script Python" class="screenshot" style="width:100%">
                    <p><i>Extrait de mon script d'analyse réseau automatisée</i></p>
                </div>
                
                <h5>🚀 Réalisations clés :</h5>
                <ul>
                    <li>Développement d'un <b>outil SIG sécurisé</b> pour la cartographie réseau</li>
                    <li>Automatisation des audits avec <b>réduction de 80% du temps d'analyse</b></li>
                    <li>Mise en place d'un <b>système de scoring des vulnérabilités</b></li>
                </ul>
                
                <h5>🛠️ Technologies utilisées :</h5>
                <div style="margin: 10px 0;">
                    <span class="tech-badge">Python</span>
                    <span class="tech-badge">Pandas</span>
                    <span class="tech-badge">Cisco ISE</span>
                    <span class="tech-badge">TACACS+</span>
                    <span class="tech-badge">PowerBI</span>
                </div>
                
                <div style="background-color: #e6f7ff; padding: 10px; border-radius: 5px; margin-top: 10px;">
                    <b>💡 Innovation :</b> Mon script Python a été adopté par 3 autres équipes pour standardiser les audits.
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Section détaillée pour le projet phare
    st.markdown("---")
    st.header("🛠️ Projet Phare: Automatisation des Audits Réseau")
    
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Contexte", "🖥️ Solution", "📈 Résultats", "🧑‍💻 Code Exemple"])
    
    with tab1:
        st.markdown("""
        ### Le Défi
        - **Problème:** Processus manuel fastidieux pour analyser les livrables réseau (Excel)
        - **Volume:** 50+ audits/mois avec 1000+ équipements chacun
        - **Délai:** 2 jours/audit en analyse manuelle
        
        <div style="background-color: #fff5e6; padding: 15px; border-radius: 8px; margin: 15px 0;">
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
    <div style="background-color: #e6f7ff; padding: 15px; border-radius: 8px; margin-top: 20px;">
        <h3 style="color: #0066cc;">💡 Ce que ces expériences m'ont appris</h3>
        <p>La sécurité est un équilibre constant entre <b>automatisation</b> et <b>expertise humaine</b>.
        Mes outils réduisent le bruit mais c'est mon analyse qui fait la différence sur les vrais threats.</p>
    </div>
    """, unsafe_allow_html=True)

# Compétences
elif page == "🛠️ Compétences":
    
    st.title("🛠️ Ma Cyber-Toolbox")
    
    # Section principale avec onglets
    tab1, tab2, tab3, tab4 = st.tabs(["🔧 Techniques", "🛡️ Sécurité", "📚 Apprentissage", "🤝 Soft Skills"])

    with tab1:
        st.markdown("### 💻 Compétences Techniques")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 4px solid #4b8df8; margin-bottom: 20px;">
                <h4 style="color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 8px;">🌐 Réseaux</h4>
                <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px;">
                    <span style="background-color: #4b8df8; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">TCP/IP</span>
                    <span style="background-color: #4b8df8; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">OSPF/BGP</span>
                    <span style="background-color: #4b8df8; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">VLAN</span>
                    <span style="background-color: #4b8df8; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">DNS/DHCP</span>
                    <span style="background-color: #4b8df8; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">VPN</span>
                    <span style="background-color: #4b8df8; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Firewall</span>
                </div>
            </div>
            
            <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 4px solid #4b8df8; margin-bottom: 20px;">
                <h4 style="color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 8px;">🖥️ Systèmes</h4>
                <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px;">
                    <span style="background-color: #4b8df8; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Linux (Debian/Kali)</span>
                    <span style="background-color: #4b8df8; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Windows Server</span>
                    <span style="background-color: #4b8df8; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Docker</span>
                    <span style="background-color: #4b8df8; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Virtualisation</span>
                    <span style="background-color: #4b8df8; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Active Directory</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 4px solid #ff7043; margin-bottom: 20px;">
                <h4 style="color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 8px;">💻 Développement</h4>
                <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px;">
                    <span style="background-color: #ff7043; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Python</span>
                    <span style="background-color: #ff7043; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Bash</span>
                    <span style="background-color: #ff7043; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Java</span>
                    <span style="background-color: #ff7043; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">SQL</span>
                    <span style="background-color: #ff7043; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">PowerShell</span>
                    <span style="background-color: #ff7043; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">HTML/CSS</span>
                </div>
            </div>
            
            <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 4px solid #ff7043; margin-bottom: 20px;">
                <h4 style="color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 8px;">🛠️ Outils</h4>
                <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px;">
                    <span style="background-color: #ff7043; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Git</span>
                    <span style="background-color: #ff7043; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Jira</span>
                    <span style="background-color: #ff7043; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Ansible</span>
                    <span style="background-color: #ff7043; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Terraform</span>
                    <span style="background-color: #ff7043; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">PostgreSQL</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with tab2:
        st.markdown("### 🛡️ Expertise Cybersécurité")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 4px solid #5cb85c; margin-bottom: 20px;">
                <h4 style="color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 8px;">🔍 Analyse & Protection</h4>
                <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px;">
                    <span style="background-color: #5cb85c; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">SIEM (QRadar)</span>
                    <span style="background-color: #5cb85c; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">XDR (Cortex)</span>
                    <span style="background-color: #5cb85c; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">SOAR (XSOAR)</span>
                    <span style="background-color: #5cb85c; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">ELK Stack</span>
                    <span style="background-color: #5cb85c; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Kibana</span>
                </div>
            </div>
            
            <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 4px solid #5cb85c; margin-bottom: 20px;">
                <h4 style="color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 8px;">📜 Normes & Cadres</h4>
                <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px;">
                    <span style="background-color: #5cb85c; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">ISO 27001</span>
                    <span style="background-color: #5cb85c; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">RGPD</span>
                    <span style="background-color: #5cb85c; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">NIST CSF</span>
                    <span style="background-color: #5cb85c; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">OWASP</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 4px solid #f0ad4e; margin-bottom: 20px;">
                <h4 style="color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 8px;">⚔️ Pentest & Red Team</h4>
                <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px;">
                    <span style="background-color: #f0ad4e; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Metasploit</span>
                    <span style="background-color: #f0ad4e; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Burp Suite</span>
                    <span style="background-color: #f0ad4e; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Nmap</span>
                    <span style="background-color: #f0ad4e; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Wireshark</span>
                    <span style="background-color: #f0ad4e; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">John the Ripper</span>
                </div>
            </div>
            
            <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 4px solid #f0ad4e; margin-bottom: 20px;">
                <h4 style="color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 8px;">🔐 Sécurité Offensive</h4>
                <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px;">
                    <span style="background-color: #f0ad4e; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">OSINT</span>
                    <span style="background-color: #f0ad4e; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Social Engineering</span>
                    <span style="background-color: #f0ad4e; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">PrivEsc</span>
                    <span style="background-color: #f0ad4e; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">CTF</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with tab3:
        st.markdown("### 📚 Formation Continue")
        
        st.markdown("""
        
        <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
            <h4 style="color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 8px;">🌐 Ressources</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; margin-top: 12px;">
                <div style="background-color: #e6f7ff; color:  #1e1e1e; padding: 10px; border-radius: 8px;">
                    <b>📖 Lectures</b><br>SANS, Medium, ZDNet
                </div>
                <div style="background-color: #e6f7ff; color:  #1e1e1e;  padding: 10px; border-radius: 8px;">
                    <b>🎧 Podcasts</b><br>NoLimitSecu, CyberUncut
                </div>
                <div style="background-color: #e6f7ff; color:  #1e1e1e;  padding: 10px; border-radius: 8px;">
                    <b>📺 Vidéos</b><br>LiveOverflow, The Cyber Mentor
                </div>
                <div style="background-color: #e6f7ff; padding: 10px; color:  #1e1e1e;  border-radius: 8px;">
                    <b>💬 Événements</b><br>FIC, Root-Me, Meetups
                </div>
            </div>
        </div>
        
        <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px;">
            <h4 style="color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 8px;">🏆 Plateformes</h4>
            <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px;">
                <span style="background-color: #4b8df8; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Youtube</span>
                <span style="background-color: #4b8df8; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">HackTheBox</span>
                <span style="background-color: #4b8df8; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Root-Me</span>
                <span style="background-color: #4b8df8; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">OpenClassrooms</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with tab4:
        st.markdown("### 🤝 Soft Skills & Méthodologie")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div style="background-color: #e6ffe6; padding: 15px; border-radius: 8px; margin-bottom: 20px;">
                <h4 style="color: #2c3e50; margin-top: 0; border-bottom: 1px solid #ddd; padding-bottom: 8px;">🧠 Cognitives</h4>
                <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px;">
                    <span style="background-color: #5cb85c; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Résolution de problèmes</span>
                    <span style="background-color: #5cb85c; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Curiosité</span>
                    <span style="background-color: #5cb85c; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Adaptabilité</span>
                    <span style="background-color: #5cb85c; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Rigueur</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div style="background-color: #fff2e6; padding: 15px; border-radius: 8px; margin-bottom: 20px;">
                <h4 style="color: #2c3e50; margin-top: 0; border-bottom: 1px solid #ddd; padding-bottom: 8px;">👥 Relationnelles</h4>
                <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px;">
                    <span style="background-color: #ff7043; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Pédagogie</span>
                    <span style="background-color: #ff7043; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Travail d'équipe</span>
                    <span style="background-color: #ff7043; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Communication</span>
                    <span style="background-color: #ff7043; color: white; padding: 6px 12px; border-radius: 16px; font-size: 14px;">Écoute active</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Section Méthodologie
        st.markdown("""
        <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin-top: 20px;">
            <h4 style="color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 8px;">⚡ Méthodologie de travail</h4>
            <ul style="margin-top: 12px; color: #333; padding-left: 20px;">
                <li style="margin-bottom: 8px;"><b>Approche itérative :</b> Test → Analyse → Amélioration</li>
                <li style="margin-bottom: 8px;"><b>Documentation systématique</b> des processus</li>
                <li style="margin-bottom: 8px;"><b>Veille technologique</b> hebdomadaire</li>
                <li><b>Retrospective</b> après chaque projet</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        # Citation
        st.markdown("""
        <div style="background-color: #f0f0f0; padding: 15px; border-radius: 8px; margin-top: 20px;">
            <p style="margin: 0; font-style: italic; color: #555; text-align: center;">
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
        Voici mon CV détaillé. Vous pouvez le visualiser ci-dessous ou le télécharger.
        """)
        
        with open("CV_Seynabou_Sougou.pdf", "rb") as file:
            base64_pdf = base64.b64encode(file.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

            st.download_button(
                label="📥 Télécharger le CV complet",
                data=file,
                file_name="CV_Seynabou_Sougou.pdf",
                mime="application/pdf"
            )
    
    with col2:
        st.markdown("""
        ### 🎯 Version Twitter
        (280 caractères max)
        
        **Seynabou Sougou**  
        Apprentie ingénieure cybersécurité  
        🛡️ Passion: protéger le monde numérique  
        🔧 Skills: Python, SIEM, Pentest, Réseaux   
        💼 Exp: SOC Analyste, Audit réseau  
        📚 Form: Auto-formation permanente  
        📍 Paris, Lyon, Toulouse, France  
        #CyberSecurity #WomenInTech
        """)
        
        st.markdown("---")
        st.markdown("""
        ### 📊 Mes Stats Clés
        - 3 ans d'expérience  
        - 15+ projets sécurité  
        - 100+ vulnérabilités trouvées  
        - 1000+ heures de formation  
        - ∞ motivation  
        """)

# Calendrier
elif page == "🗓️ Calendrier":
    st.title("🗓️ Calendrier d'Alternance 2025-2026")

    # Aperçu textuel clair
    st.markdown("""
    ### 🔍 Rythme d'Alternance
    
    Voici mon planning officiel pour l'année 2025-2026 :
    
    - 📚 **3 semaines à l'école**, suivi de  
    - 🏢 **3 semaines en entreprise**, en alternance parfois d'un mois jusqu'à fin janvier  
    - 🧑‍💼 Puis **temps plein en entreprise** à partir de février 2026
    """)

    st.markdown("### 📜 Calendrier Officiel")
    st.write("Visualisez le document original fourni par l'école :")

    with open("calendrier_alternance.pdf", "rb") as file:
        base64_pdf = base64.b64encode(file.read()).decode('utf-8')
        pdf_display = f"""
        <div style="
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 10px;
            margin: 15px 0;
            overflow: auto;
            height: 700px;
        ">
            <embed src="data:application/pdf;base64,{base64_pdf}" 
                   type="application/pdf" 
                   width="100%" 
                   height="100%"
                   style="min-height: 650px;">
        </div>
        """
        st.markdown(pdf_display, unsafe_allow_html=True)

    # Relecture du fichier pour le bouton (important car file.read() a déjà été fait)
    with open("calendrier_alternance.pdf", "rb") as file_download:
        st.download_button(
            label="📥 Télécharger le calendrier complet",
            data=file_download,
            file_name="calendrier_alternance_2025-2026.pdf",
            mime="application/pdf"
        )


# Contact
elif page == "📱 Contact":
    st.title("📱 Contactez-moi (sans virus inclus)")
    
    # Section contacts
    st.markdown("### 💌 Pour les messages sérieux (ou pas)")

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
        *(Certains repos sont privés. Mission Impossible mode activé)*

        **📍 Localisation :**  
        Paris, France  
        *(Zone précise verrouillée par chiffrement AES-256)*

        **🔒 PGP :**  
        *Disponible sur demande*  
        *(Pour les ultra-paranos comme moi)*
        """)

    st.markdown("---")
    
    # Section disponibilités
    st.markdown("### 📅 Mes disponibilités")
    st.markdown("""
    ✅ **Actuellement ouverte à :**
    - Alternances en réseaux et cybersécurité
    - Missions freelance (pentest, audit)
    - Cafés tech (physique ou virtuel)
    - Défis techniques qui chauffent les CPUs

    ❌ **Pas intéressée par :**
    - Offres non sollicitées de "richesse rapide"
    - Formations payantes miracles
    - Arnaques au "virement trop payé"
    """)
    
    st.warning("""
    ⚠️ **Mon filtre anti-spam est activé :**  
    Les emails avec "Cher client", "Vous avez gagné" ou contenant des pièces jointes .exe seront automatiquement détruits.
    """)

    st.markdown("---")
    
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