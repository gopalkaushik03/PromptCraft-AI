import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        /* IMPORT GOOGLE FONTS */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

        /* GLOBAL THEME */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            color: #e2e8f0; 
        }

        /* MAIN BACKGROUND */
        .stApp {
            background-color: #020617; /* Very dark blue */
            background-image: 
                radial-gradient(at 0% 0%, rgba(56, 189, 248, 0.15) 0px, transparent 50%),
                radial-gradient(at 100% 100%, rgba(99, 102, 241, 0.15) 0px, transparent 50%);
            background-attachment: fixed;
        }

        /* ----------------------------------------------------
           🔥🔥 NEW SIDEBAR STYLING 🔥🔥
        ---------------------------------------------------- */
        section[data-testid="stSidebar"] {
            /* Deep gradient background */
            background: linear-gradient(180deg, #0f172a 0%, #1e1b4b 100%);
            border-right: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 10px 0 30px rgba(0,0,0,0.5);
        }
        
        /* Sidebar Headers */
        section[data-testid="stSidebar"] h2 {
            color: #818cf8 !important; /* Indigo accent */
            text-transform: uppercase;
            font-size: 0.9rem;
            letter-spacing: 2px;
            margin-bottom: 20px;
        }

        /* Custom "Profile Card" in Sidebar */
        .sidebar-card {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 15px;
            margin-bottom: 20px;
            text-align: center;
        }
        
        .sidebar-card h3 {
            margin: 0;
            color: white;
            font-size: 1.1rem;
        }
        
        .sidebar-card p {
            margin: 5px 0 0 0;
            color: #94a3b8;
            font-size: 0.8rem;
        }

        /* Style the Dropdowns and Inputs in Sidebar */
        div[data-testid="stSidebar"] .stSelectbox > div > div {
            background-color: rgba(0, 0, 0, 0.3);
            border: 1px solid #475569;
            color: white;
        }
        
        div[data-testid="stSidebar"] .stTextArea textarea {
            background-color: rgba(0, 0, 0, 0.3);
            border: 1px solid #475569;
        }

        /* Expanders (Settings Menu) */
        div[data-testid="stSidebar"] .streamlit-expanderHeader {
            background-color: rgba(255, 255, 255, 0.05);
            border-radius: 8px;
            color: white;
        }

        /* ----------------------------------------------------
           MAIN CONTENT STYLES
        ---------------------------------------------------- */
        
        /* Hero Header */
        .hero-header {
            text-align: center;
            padding: 40px 0 20px 0;
            background: linear-gradient(180deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0) 100%);
            border-radius: 16px;
            margin-bottom: 30px;
            border: 1px solid rgba(255,255,255,0.05);
            animation: slideUp 0.8s ease-out;
        }

        .gradient-text {
            background: linear-gradient(90deg, #818cf8 0%, #38bdf8 50%, #818cf8 100%);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
            font-size: 3rem;
            letter-spacing: -1px;
            animation: shimmer 3s linear infinite;
        }

        .subtitle { color: #94a3b8; font-size: 1.1rem; }

        /* Floating Robot */
        .floating-robot {
            text-align: center;
            animation: float 6s ease-in-out infinite;
        }

        /* Chat Bubbles */
        div[data-testid="stChatMessage"] {
            background-color: rgba(30, 41, 59, 0.7); /* Slightly more opaque */
            border: 1px solid #334155;
            border-radius: 12px;
            animation: fadeIn 0.5s ease-in;
        }
        
        /* Animations */
        @keyframes float { 0% { transform: translateY(0px); } 50% { transform: translateY(-15px); } 100% { transform: translateY(0px); } }
        @keyframes shimmer { to { background-position: 200% center; } }
        @keyframes slideUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

        /* Buttons */
        .stButton button {
            background: linear-gradient(90deg, #6366f1 0%, #3b82f6 100%);
            color: white; border: none; font-weight: 600;
        }
        </style>
    """, unsafe_allow_html=True)