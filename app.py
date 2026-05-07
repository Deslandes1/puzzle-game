import streamlit as st
from datetime import datetime
import random

st.set_page_config(
    page_title="Triangle Puzzle | GlobalInternet.py",
    page_icon="🔺",
    layout="wide"
)

# ---------- CUSTOM CSS (colorful, beautiful) ----------
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
        margin: 0.5rem;
        text-align: center;
        border: 2px solid #ffd966;
        min-height: 180px;
        transition: 0.2s;
    }
    .game-square:hover {
        border-color: #e94560;
        transform: scale(1.02);
    }
    .triangle-card {
        background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%);
        border-radius: 15px;
        padding: 1rem;
        margin: 0.5rem;
        text-align: center;
        font-weight: bold;
        cursor: pointer;
        transition: 0.2s;
        border: 1px solid #fff;
    }
    .triangle-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
    .triangle-placed {
        background: #2e7d32;
        opacity: 0.7;
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
    .square-title {
        font-size: 1.2rem;
        font-weight: bold;
        color: #ffd966;
    }
    .triangle-list {
        font-size: 1.1rem;
        margin-top: 0.5rem;
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

# ---------- SPINNING GLOBE ANIMATION (used later) ----------
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
    # triangles: each is {id, placed, square_index}
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

    # Main game area
    st.markdown("<h1 style='text-align:center;'>🔺 Six Triangles → Four Squares 🔲</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="inspiration">
    Puzzles teach us not to give up easily. <br>
    They push us to try again, think differently, and come up with new ideas to solve problems.<br>
    Every puzzle is like a small workout for the brain – helping our mind grow sharper, more creative, and more patient with challenges.
    </div>
    """, unsafe_allow_html=True)

    col_left, col_right = st.columns([2, 1])

    with col_left:
        st.markdown("### 🟦 Squares (Click a square to place the selected triangle)")
        squares = st.columns(2)
        square_index = 0
        for row in range(2):
            cols = st.columns(2)
            for col in cols:
                with col:
                    triangles_in_square = [t for t in st.session_state.game_state["triangles"] if t["square"] == square_index]
                    placed_count = len(triangles_in_square)
                    st.markdown(f"""
                    <div class="game-square" id="square_{square_index}">
                        <div class="square-title">Square {square_index+1}</div>
                        <div class="triangle-list">
                            {''.join([f'🔺 ' for _ in range(placed_count)]) or '⚪ empty'}
                        </div>
                        <p style="font-size:0.8rem;">({placed_count}/6 triangles)</p>
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button(f"Place here → Square {square_index+1}", key=f"place_{square_index}", width="stretch"):
                        if st.session_state.game_state["selected_triangle"] is not None:
                            tri_id = st.session_state.game_state["selected_triangle"]
                            # find that triangle
                            for t in st.session_state.game_state["triangles"]:
                                if t["id"] == tri_id and not t["placed"]:
                                    t["placed"] = True
                                    t["square"] = square_index
                                    st.session_state.game_state["selected_triangle"] = None
                                    break
                            # check win
                            all_placed = all(t["placed"] for t in st.session_state.game_state["triangles"])
                            if all_placed:
                                st.session_state.game_state["win"] = True
                            st.rerun()
                        else:
                            st.warning("First select a triangle from the right panel!")
                    square_index += 1

    with col_right:
        st.markdown("### 🔺 Available Triangles")
        st.markdown("*Click a triangle to select it, then click a square.*")
        # Display triangles that are not placed
        unplaced = [t for t in st.session_state.game_state["triangles"] if not t["placed"]]
        if unplaced:
            cols_tri = st.columns(2)
            for idx, tri in enumerate(unplaced):
                with cols_tri[idx % 2]:
                    is_selected = (st.session_state.game_state["selected_triangle"] == tri["id"])
                    bg_color = "#e94560" if is_selected else "#ff9a9e"
                    st.markdown(f"""
                    <div style="background:{bg_color}; border-radius:15px; padding:0.8rem; margin:0.5rem; text-align:center; cursor:pointer;">
                        <div style="font-size:2rem;">🔺</div>
                        <div>Triangle {tri['id']+1}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button(f"Select 🔺 {tri['id']+1}", key=f"select_{tri['id']}"):
                        st.session_state.game_state["selected_triangle"] = tri["id"]
                        st.rerun()
        else:
            st.success("🎉 All triangles are placed! You win!")

        if st.button("⟳ Reset Game", width="stretch"):
            reset_game()

    # Win detection and celebration
    if st.session_state.game_state["win"]:
        st.markdown('<div class="win-message">🎉 YOU WIN! 🎉</div>', unsafe_allow_html=True)
        st.balloons()
        st.snow()  # just for fun

    # Show selected triangle info
    if st.session_state.game_state["selected_triangle"] is not None:
        st.info(f"Selected: Triangle {st.session_state.game_state['selected_triangle']+1}. Now click on a square to place it.")

    st.markdown("---")
    st.caption("© GlobalInternet.py – Train your brain, one puzzle at a time.")

# ---------- ROUTING ----------
if not st.session_state.game_authenticated:
    login_page()
else:
    game_main()
