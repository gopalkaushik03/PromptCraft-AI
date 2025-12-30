import streamlit as st
import os
from gemini_client import refine_prompt, generate_response_stream

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="PromptCraft AI", 
    page_icon="⚡", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. ADVANCED CYBER-GLASS CSS (TRANSPARENT SIDEBAR)
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&family=JetBrains+Mono:wght@400;700&display=swap');

    /* 🌌 DEEP SPACE BACKGROUND */
    .stApp {
        background-color: #030712;
        background-image: 
            radial-gradient(at 10% 10%, rgba(79, 70, 229, 0.2) 0px, transparent 50%),
            radial-gradient(at 90% 90%, rgba(236, 72, 153, 0.2) 0px, transparent 50%),
            radial-gradient(at 50% 50%, rgba(0, 0, 0, 0) 0px, transparent 50%);
        font-family: 'Outfit', sans-serif;
        color: #f3f4f6;
    }

    /* 🟣 SMOOTH NEON BREATHE ANIMATION */
    @keyframes neon-breathe {
        0% { text-shadow: 0 0 15px rgba(129, 140, 248, 0.3); }
        50% { text-shadow: 0 0 35px rgba(168, 85, 247, 0.6), 0 0 10px rgba(129, 140, 248, 0.8); }
        100% { text-shadow: 0 0 15px rgba(129, 140, 248, 0.3); }
    }

    /* 🪄 TITLE STYLING */
    .title-glow {
        font-weight: 800;
        font-size: 3.5rem;
        background: linear-gradient(to right, #818cf8, #c084fc, #818cf8);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradient-move 5s linear infinite, neon-breathe 3s ease-in-out infinite;
        margin-bottom: 0px;
    }

    @keyframes gradient-move {
        0% { background-position: 0% 50%; }
        100% { background-position: 200% 50%; }
    }

    /* 🥛 ULTRA-GLASS SIDEBAR (NEW & IMPROVED) */
    section[data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0.2) !important; /* Very transparent */
        backdrop-filter: blur(15px) saturate(150%); /* The "Frost" Effect */
        border-right: 1px solid rgba(255, 255, 255, 0.08); /* Subtle edge */
        box-shadow: 5px 0 20px rgba(0,0,0,0.2);
    }
    
    /* Fix for the internal container of sidebar to be transparent */
    section[data-testid="stSidebar"] > div {
        background-color: transparent;
    }

    /* ✨ MODERN CARDS */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 20px;
        transition: transform 0.2s, border-color 0.2s;
    }
    .glass-card:hover {
        transform: translateY(-2px);
        border-color: rgba(99, 102, 241, 0.5);
    }

    /* 🟢 NEON BUTTONS */
    .stButton button {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
        color: white;
        border: none;
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        box-shadow: 0 0 20px rgba(124, 58, 237, 0.5);
        transform: scale(1.02);
    }
    
    /* 💬 CHAT BUBBLES */
    div[data-testid="stChatMessage"] {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
    }

    /* 🖊️ CUSTOM TEXT AREA */
    .stTextArea textarea {
        background-color: rgba(0, 0, 0, 0.3) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: #e0e7ff !important;
        font-family: 'JetBrains Mono', monospace;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. AVATAR CONFIG (STABLE 3D ROBOTS)
# ==========================================
AVATARS = {
    "default": "https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Robot.png",
    "coder": "https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/People/Technologist.png",
    "creative": "https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Artist%20Palette.png",
    "user": "https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/People/Student.png" 
}

def get_smart_avatar(text):
    text = text.lower()
    if any(x in text for x in ["code", "python", "bug", "api", "html", "css", "java", "script", "function", "react", "node"]): 
        return AVATARS["coder"]
    if any(x in text for x in ["design", "story", "write", "poem", "essay", "paint", "draw"]): 
        return AVATARS["creative"]
    return AVATARS["default"]

# ==========================================
# 4. SIDEBAR DASHBOARD
# ==========================================
with st.sidebar:
    st.markdown("### ⚡ System Status")
    c1, c2 = st.columns(2)
    with c1: st.metric("Latency", "24ms", "⚡")
    with c2: st.metric("Model", "Gemini 1.5", "🟢")
    
    st.markdown("---")
    
    # 🧠 BRAIN PARAMETERS (Simplified)
    with st.expander("🛠️ Advanced Settings", expanded=True):
        temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
        max_tokens = st.slider("Max Length", 100, 8000, 4000)
        
    st.markdown("---")
    if st.button("🗑️ New Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.current_refined_prompt = ""
        st.rerun()

# ==========================================
# 5. MAIN APP LOGIC
# ==========================================
if "messages" not in st.session_state: st.session_state.messages = []
if "current_refined_prompt" not in st.session_state: st.session_state.current_refined_prompt = ""

# --- HEADER ---
c1, c2 = st.columns([1, 8])
with c1:
    st.image(AVATARS["default"], width=85)
with c2:
    st.markdown('<div class="title-glow">PromptCraft AI</div>', unsafe_allow_html=True)
    st.caption("🚀 Next-Gen Human-in-the-Loop Prompt Engineering")

st.markdown("---")

# --- EMPTY STATE: SUGGESTION CARDS ---
if not st.session_state.messages and not st.session_state.current_refined_prompt:
    st.markdown("### 👋 Ready to craft? Pick a starter:")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="glass-card">
            <h4>🐍 Python Game</h4>
            <p style="color:#aaa; font-size:0.9rem;">Create a Snake game with Pygame...</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Try 'Snake Game'", key="btn1"):
            raw_input = "code for snake game"
            with st.spinner("✨ Polishing your idea..."):
                st.session_state.current_refined_prompt = refine_prompt(raw_input) 
                st.rerun()

    with col2:
        st.markdown("""
        <div class="glass-card">
            <h4>⚛️ React Component</h4>
            <p style="color:#aaa; font-size:0.9rem;">Build a responsive Navbar with Tailwind...</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Try 'React Navbar'", key="btn2"):
            raw_input = "react navbar component"
            with st.spinner("✨ Polishing your idea..."):
                st.session_state.current_refined_prompt = refine_prompt(raw_input)
                st.rerun()

    with col3:
        st.markdown("""
        <div class="glass-card">
            <h4>📝 Essay Writer</h4>
            <p style="color:#aaa; font-size:0.9rem;">Explain Quantum Physics simply...</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Try 'Explain Physics'", key="btn3"):
            raw_input = "explain quantum physics"
            with st.spinner("✨ Polishing your idea..."):
                st.session_state.current_refined_prompt = refine_prompt(raw_input)
                st.rerun()

# --- CHAT HISTORY ---
for msg in st.session_state.messages:
    if msg["role"] == "user":
        avatar_url = AVATARS["user"]
    else:
        avatar_url = get_smart_avatar(msg["content"])
    
    with st.chat_message(msg["role"], avatar=avatar_url):
        st.markdown(msg["content"])

# --- INPUT & REFINEMENT ---
if not st.session_state.current_refined_prompt:
    user_input = st.chat_input("💡 Type a raw idea (e.g. 'function to sort list')...")
    if user_input:
        with st.spinner("🔮 AI is refining your prompt..."):
            refined = refine_prompt(user_input)
            st.session_state.current_refined_prompt = refined
            st.rerun()
else:
    # --- MISSION CONTROL DASHBOARD ---
    st.markdown(f"""
    <div style="background: rgba(79, 70, 229, 0.1); border: 1px solid rgba(79, 70, 229, 0.3); border-radius: 12px; padding: 15px; margin-bottom: 20px;">
        <h4 style="margin:0; color: #818cf8;">✨ Optimization Complete</h4>
        <p style="margin:0; font-size: 0.9rem; color: #ccc;">AI has auto-detected optimal settings.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        final_prompt = st.text_area("Review Prompt", value=st.session_state.current_refined_prompt, height=200, label_visibility="collapsed")
    
    run_pressed = False
    with col2:
        st.markdown("<br>", unsafe_allow_html=True) # Spacer
        if st.button("🚀 EXECUTE", type="primary", use_container_width=True):
            run_pressed = True
        
        if st.button("🔄 Edit Raw", use_container_width=True):
            st.session_state.current_refined_prompt = ""
            st.rerun()

    if run_pressed:
        st.session_state.messages.append({"role": "user", "content": final_prompt})
        stream_avatar = get_smart_avatar(final_prompt)
        
        with st.chat_message("assistant", avatar=stream_avatar):
            response_stream = generate_response_stream(
                final_prompt, 
                "You are a helpful AI.",
                temperature, 
                max_tokens, 
                0.9
            )
            full_response = st.write_stream(response_stream)
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})
        st.session_state.current_refined_prompt = ""
        st.rerun()