import streamlit as st
from datetime import datetime
import random

st.set_page_config(
    page_title="Triangle Puzzle | GlobalInternet.py",
    page_icon="🔺",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f3460 0%, #1a1a2e 100%);
        border-right: 2px solid #e94560;
    }
    [data-testid="stSidebar"] .stMarkdown, 
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] .stCaption {
        color: #ffffff !important;
    }
    .stButton button {
        background-color: #e94560 !important;
        color: white !important;
        border-radius: 30px !important;
        font-weight: bold !important;
        width: 100%;
        transition: 0.2s;
    }
    .stButton button:hover {
        background-color: #ff6b6b !important;
        transform: scale(1.02);
    }
    .game-square {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 1rem;
        text-align: center;
        border: 2px solid #ffd966;
        margin-bottom: 1rem;
        min-height: 180px;
    }
    .triangle-card {
        background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%);
        border-radius: 15px;
        padding: 0.8rem;
        margin: 0.5rem 0;
        text-align: center;
        font-weight: bold;
        transition: 0.2s;
    }
    .triangle-selected {
        background: #e94560 !important;
        color: white;
        transform: scale(1.02);
    }
    .win-message {
        text-align: center;
        font-size: 2rem;
        font-weight: bold;
        color: #ffd966;
        animation: pulse 0.8s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.05); opacity: 0.8; }
        100% { transform: scale(1); opacity: 1; }
    }
    h1, h2, h3 {
        color: #ffd966 !important;
    }
    p, li {
        color: #ffffff !important;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
        border-top: 1px solid #e94560;
    }
    .inspiration {
        background: rgba(233,69,96,0.2);
        border-left: 5px solid #e94560;
        padding: 0.5rem 1rem;
        border-radius: 12px;
        margin: 1rem 0;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# ---------- SPINNING GLOBE ----------
def spinning_globe():
    st.sidebar.markdown("""
    <div style="text-align: center;">
        <div style="font-size:80px; animation:spin 4s linear infinite; display:inline-block;">🌍</div>
    </div>
    <style>
        @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    </style>
    """, unsafe_allow_html=True)

# ---------- LOGIN / LOGOUT ----------
if "game_authenticated" not in st.session_state:
    st.session_state.game_authenticated = False
if "game_state" not in st.session_state:
    st.session_state.game_state = {
        "triangles": [{"id": i, "placed": False, "square": None} for i in range(6)],
        "selected_triangle": None,
        "win": False
    }

def logout():
    st.session_state.game_authenticated = False
    st.rerun()

def reset_game():
    st.session_state.game_state = {
        "triangles": [{"id": i, "placed": False, "square": None} for i in range(6)],
        "selected_triangle": None,
        "win": False
    }
    st.rerun()

def login_page():
    st.markdown("""
    <style>
    .login-container { display: flex; justify-content: center; align-items: center; min-height: 80vh; }
    .login-card {
        background: rgba(15,52,96,0.8);
        backdrop-filter: blur(12px);
        border-radius: 30px;
        padding: 2rem;
        text-align: center;
        border: 1px solid #e94560;
        width: 100%;
        max-width: 450px;
        margin: auto;
    }
    .login-title { color: #ffd966; font-size: 2rem; margin-bottom: 1rem; }
    </style>
    <div class="login-container">
        <div class="login-card">
            <div style="font-size:80px; animation:spin 4s linear infinite; display:inline-block;">🌍</div>
            <div class="login-title">Triangle Puzzle</div>
            <p style="color:white;">Enter password to start the game</p>
    """, unsafe_allow_html=True)
    password = st.text_input("Password", type="password", key="game_pass")
    if st.button("🔐 Login", width="stretch"):
        if password == "20082010":
            st.session_state.game_authenticated = True
            st.rerun()
        else:
            st.error("Incorrect password.")
    st.markdown("</div></div>", unsafe_allow_html=True)

# ---------- MAIN GAME UI ----------
def game_main():
    spinning_globe()
    st.sidebar.markdown("## **GlobalInternet.py**")
    st.sidebar.markdown("### Triangle Puzzle")
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Built by Gesner Deslandes** – Coder in Chief")
    st.sidebar.markdown("📞 (509)-47385663")
    st.sidebar.markdown("✉️ deslandes78@gmail.com")
    st.sidebar.markdown("---")
    st.sidebar.markdown("**🌐 Website:**")
    st.sidebar.markdown("[https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 💰 Pricing")
    st.sidebar.markdown("""
    | Puzzle Game | Price |
    |-------------|-------|
    | **Single‑User** | $5 |
    | **Source Code** | $49 |
    """)
    if st.sidebar.button("🔓 Logout", width="stretch"):
        logout()

    # Main content
    st.markdown("<h1 style='text-align:center;'>🔺 Six Triangles → Four Squares 🔲</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="inspiration">
    Puzzles teach us not to give up easily.<br>
    They push us to try again, think differently, and come up with new ideas to solve problems.<br>
    Every puzzle is like a small workout for the brain – helping our mind grow sharper, more creative, and more patient with challenges.
    </div>
    """, unsafe_allow_html=True)

    # Layout: squares on left, triangles on right
    col_squares, col_triangles = st.columns([2, 1])

    # ----- SQUARES (2x2 grid) -----
    with col_squares:
        st.markdown("### 🟦 Squares (click button to place selected triangle)")
        # Create 2 rows of 2 squares each
        for row in range(2):
            row_cols = st.columns(2)
            for col_idx in range(2):
                square_index = row * 2 + col_idx
                # Count triangles already placed in this square
                triangles_in_square = [t for t in st.session_state.game_state["triangles"] if t["square"] == square_index]
                placed_count = len(triangles_in_square)
                with row_cols[col_idx]:
                    st.markdown(f"""
                    <div class="game-square">
                        <h3>Square {square_index+1}</h3>
                        <div style="font-size:1.5rem;">🔲</div>
                        <div>{'🔺 ' * placed_count}</div>
                        <div>({placed_count}/6 triangles)</div>
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button(f"Place here → Square {square_index+1}", key=f"place_{square_index}"):
                        if st.session_state.game_state["selected_triangle"] is not None:
                            tri_id = st.session_state.game_state["selected_triangle"]
                            for t in st.session_state.game_state["triangles"]:
                                if t["id"] == tri_id and not t["placed"]:
                                    t["placed"] = True
                                    t["square"] = square_index
                                    st.session_state.game_state["selected_triangle"] = None
                                    break
                            # check win
                            if all(t["placed"] for t in st.session_state.game_state["triangles"]):
                                st.session_state.game_state["win"] = True
                            st.rerun()
                        else:
                            st.warning("First select a triangle from the right panel!")

    # ----- TRIANGLES -----
    with col_triangles:
        st.markdown("### 🔺 Available Triangles")
        st.markdown("*Click a triangle to select it, then click a square.*")
        unplaced = [t for t in st.session_state.game_state["triangles"] if not t["placed"]]
        if unplaced:
            for tri in unplaced:
                is_selected = (st.session_state.game_state["selected_triangle"] == tri["id"])
                label = f"🔺 Triangle {tri['id']+1}"
                if st.button(label, key=f"tri_{tri['id']}"):
                    st.session_state.game_state["selected_triangle"] = tri["id"]
                    st.rerun()
                if is_selected:
                    st.markdown(f"<p style='color:#e94560; font-weight:bold;'>✓ Selected: Triangle {tri['id']+1}</p>", unsafe_allow_html=True)
        else:
            st.success("🎉 All triangles placed! You win!")

        if st.button("⟳ Reset Game", width="stretch"):
            reset_game()

    # Win celebration
    if st.session_state.game_state["win"]:
        st.markdown('<div class="win-message">🎉 YOU WIN! 🎉</div>', unsafe_allow_html=True)
        st.balloons()
        st.snow()

    st.markdown("---")
    st.caption("© GlobalInternet.py – Train your brain, one puzzle at a time.")

# ---------- ROUTING ----------
if not st.session_state.game_authenticated:
    login_page()
else:
    game_main()
