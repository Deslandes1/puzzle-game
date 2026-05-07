import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Triangle Puzzle | GlobalInternet.py",
    page_icon="🔺",
    layout="wide"
)

# ---------- CUSTOM CSS for overall app (sidebar, login, etc.) ----------
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
    h1, h2, h3 {
        color: #ffd966 !important;
    }
    .footer {
        text-align: center;
        margin-top: 2rem;
        padding: 1rem;
        border-top: 1px solid #e94560;
    }
</style>
""", unsafe_allow_html=True)

# ---------- SPINNING GLOBE SIDEBAR FUNCTION ----------
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
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def logout():
    st.session_state.authenticated = False
    st.rerun()

def login_page():
    st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; min-height: 80vh;">
        <div class="login-card">
            <div style="font-size:80px; animation:spin 4s linear infinite; display:inline-block;">🌍</div>
            <div class="login-title">Triangle Puzzle</div>
            <p style="color:white;">Enter password to start the game</p>
    """, unsafe_allow_html=True)
    password = st.text_input("Password", type="password", key="login_pass")
    if st.button("🔐 Login", use_container_width=True):
        if password == "20082010":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Incorrect password.")
    st.markdown("</div></div>", unsafe_allow_html=True)

# ---------- SIDEBAR (visible only after login) ----------
def show_sidebar():
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
    if st.sidebar.button("🔓 Logout", use_container_width=True):
        logout()

# ---------- HTML/JS DRAG-AND-DROP GAME ----------
def drag_drop_game():
    game_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
        <style>
            * {
                user-select: none;
                -webkit-tap-highlight-color: transparent;
            }
            body {
                background: transparent;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                padding: 1rem;
            }
            .game-container {
                background: rgba(0,0,0,0.3);
                border-radius: 30px;
                padding: 1.5rem;
            }
            .game-title {
                text-align: center;
                margin-bottom: 1.5rem;
            }
            .game-title h2 {
                color: #ffd966;
                margin: 0;
            }
            .game-title p {
                color: #ddd;
                font-size: 1rem;
            }
            .grid {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 20px;
                margin: 20px 0;
            }
            .square {
                width: 100px;
                height: 100px;
                background: rgba(255, 217, 102, 0.2);
                border: 3px solid #ffd966;
                border-radius: 15px;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                transition: all 0.2s;
                position: relative;
            }
            .square.filled {
                background: rgba(46, 125, 50, 0.6);
                border-color: #4caf50;
                box-shadow: 0 0 12px #4caf50;
            }
            .square .square-label {
                position: absolute;
                top: 5px;
                left: 8px;
                font-size: 12px;
                color: #ffd966;
                font-weight: bold;
            }
            .square .triangle-placed {
                font-size: 50px;
                cursor: default;
            }
            .square.empty .triangle-placed {
                display: none;
            }
            .triangle {
                width: 80px;
                height: 80px;
                background: linear-gradient(135deg, #ff9a9e, #fad0c4);
                border-radius: 15px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 45px;
                cursor: grab;
                transition: all 0.2s;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                margin: 0 auto;
            }
            .triangle.dragging {
                opacity: 0.5;
                cursor: grabbing;
            }
            .triangle:hover {
                transform: scale(1.05);
                background: #ff6b6b;
            }
            .triangle-container {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 20px;
                margin: 20px 0;
            }
            .info-panel {
                display: flex;
                justify-content: space-between;
                align-items: center;
                flex-wrap: wrap;
                gap: 10px;
                margin-bottom: 20px;
                background: rgba(0,0,0,0.5);
                padding: 10px 20px;
                border-radius: 40px;
            }
            .remaining {
                color: white;
                font-weight: bold;
            }
            .reset-btn {
                background-color: #e94560;
                color: white;
                border: none;
                border-radius: 40px;
                padding: 8px 24px;
                font-weight: bold;
                cursor: pointer;
                transition: 0.2s;
            }
            .reset-btn:hover {
                background-color: #ff6b6b;
                transform: scale(1.02);
            }
            .win-message {
                text-align: center;
                font-size: 2rem;
                font-weight: bold;
                color: #ffd966;
                animation: pulse 0.8s infinite;
                margin-top: 20px;
            }
            @keyframes pulse {
                0% { transform: scale(1); opacity: 1; }
                50% { transform: scale(1.05); opacity: 0.8; }
                100% { transform: scale(1); opacity: 1; }
            }
            @media (max-width: 700px) {
                .square { width: 70px; height: 70px; }
                .triangle { width: 60px; height: 60px; font-size: 35px; }
                .triangle-placed { font-size: 35px; }
            }
        </style>
    </head>
    <body>
    <div class="game-container">
        <div class="game-title">
            <h2>🔺 Drag each triangle into a square 🔲</h2>
            <p>Drop a triangle onto a square – it will stick. Each square fits exactly one triangle.</p>
        </div>

        <!-- Squares (10 positions) -->
        <div id="squaresContainer" class="grid"></div>

        <!-- Triangles (10 draggable) -->
        <div id="trianglesContainer" class="triangle-container"></div>

        <div class="info-panel">
            <span class="remaining">🔺 Remaining triangles: <span id="remainingCount">10</span></span>
            <button class="reset-btn" id="resetBtn">⟳ Reset Game</button>
        </div>
        <div id="winMessage" style="display: none;" class="win-message">🎉 YOU WIN! 🎉</div>
    </div>

    <script>
        // Configuration: 10 triangles, 10 squares (indexed 0-9)
        let squaresOccupied = new Array(10).fill(false);  // true if a triangle is placed
        let trianglePlaced = new Array(10).fill(false);   // which triangle ID is placed, but we track by draggable elements
        let dragSrcElement = null;

        // Create squares
        const squaresContainer = document.getElementById('squaresContainer');
        for (let i = 0; i < 10; i++) {
            const square = document.createElement('div');
            square.className = 'square empty';
            square.setAttribute('data-square-id', i);
            square.innerHTML = `<div class="square-label">S${i+1}</div><div class="triangle-placed"></div>`;
            square.addEventListener('dragover', (e) => {
                e.preventDefault();
            });
            square.addEventListener('drop', (e) => {
                e.preventDefault();
                const squareId = parseInt(e.currentTarget.getAttribute('data-square-id'));
                if (squaresOccupied[squareId]) return; // already filled
                const triangleId = e.dataTransfer.getData('text/plain');
                if (triangleId === null) return;
                const triangleElement = document.getElementById(`triangle-${triangleId}`);
                if (triangleElement && triangleElement.parentNode) {
                    // Remove triangle from its container
                    triangleElement.remove();
                    // Mark square as filled
                    squaresOccupied[squareId] = true;
                    // Update square display
                    e.currentTarget.classList.remove('empty');
                    e.currentTarget.classList.add('filled');
                    const placedDiv = e.currentTarget.querySelector('.triangle-placed');
                    placedDiv.innerHTML = '🔺';
                    // Update remaining count
                    updateRemaining();
                    // Check win
                    if (squaresOccupied.every(v => v === true)) {
                        document.getElementById('winMessage').style.display = 'block';
                        // optional: disable further drops
                        alert('Congratulations! You placed all triangles!');
                    }
                }
            });
            squaresContainer.appendChild(square);
        }

        // Create triangles
        const trianglesContainer = document.getElementById('trianglesContainer');
        for (let i = 0; i < 10; i++) {
            const triangle = document.createElement('div');
            triangle.id = `triangle-${i}`;
            triangle.className = 'triangle';
            triangle.setAttribute('draggable', 'true');
            triangle.setAttribute('data-triangle-id', i);
            triangle.innerHTML = '🔺';
            triangle.addEventListener('dragstart', (e) => {
                e.dataTransfer.setData('text/plain', e.target.getAttribute('data-triangle-id'));
                e.dataTransfer.effectAllowed = 'move';
                e.target.classList.add('dragging');
            });
            triangle.addEventListener('dragend', (e) => {
                e.target.classList.remove('dragging');
            });
            // For touch devices: we need to handle touch events (simpler: use HTML5 drag and drop works on most desktops, but touch requires additional handling)
            // We'll add a fallback: on touch, use a simple "tap" + "tap square" mechanism? But for simplicity, we rely on drag/drop.
            // However, modern touch devices support drag/drop partially. To ensure full mobile, we add a touch polyfill using simple button mode? Not needed for now.
            trianglesContainer.appendChild(triangle);
        }

        function updateRemaining() {
            const remaining = squaresOccupied.filter(v => !v).length;
            document.getElementById('remainingCount').innerText = remaining;
        }

        // Reset function
        function resetGame() {
            // Reset arrays
            squaresOccupied.fill(false);
            // Clear squares and rebuild content
            const squares = document.querySelectorAll('.square');
            squares.forEach((square, idx) => {
                square.classList.remove('filled');
                square.classList.add('empty');
                const placedDiv = square.querySelector('.triangle-placed');
                placedDiv.innerHTML = '';
                // Reset data attribute? no need.
            });
            // Rebuild triangles container (remove all and recreate)
            trianglesContainer.innerHTML = '';
            for (let i = 0; i < 10; i++) {
                const triangle = document.createElement('div');
                triangle.id = `triangle-${i}`;
                triangle.className = 'triangle';
                triangle.setAttribute('draggable', 'true');
                triangle.setAttribute('data-triangle-id', i);
                triangle.innerHTML = '🔺';
                triangle.addEventListener('dragstart', (e) => {
                    e.dataTransfer.setData('text/plain', e.target.getAttribute('data-triangle-id'));
                    e.dataTransfer.effectAllowed = 'move';
                    e.target.classList.add('dragging');
                });
                triangle.addEventListener('dragend', (e) => {
                    e.target.classList.remove('dragging');
                });
                trianglesContainer.appendChild(triangle);
            }
            document.getElementById('winMessage').style.display = 'none';
            updateRemaining();
        }

        document.getElementById('resetBtn').addEventListener('click', resetGame);
        updateRemaining();
    </script>
    </body>
    </html>
    """
    components.html(game_html, height=700, scrolling=False)

# ---------- MAIN APP AFTER LOGIN ----------
def main_app():
    show_sidebar()
    st.markdown("<h1 style='text-align:center;'>🔺 Drag & Drop Puzzle</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Drag each triangle into a square – each square can hold exactly one triangle.</p>", unsafe_allow_html=True)
    drag_drop_game()
    st.markdown('<div class="footer">© GlobalInternet.py – Train your brain, one puzzle at a time.</div>', unsafe_allow_html=True)

# ---------- ROUTING ----------
if not st.session_state.authenticated:
    login_page()
else:
    main_app()
