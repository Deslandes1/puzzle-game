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
            <div class="login-title">Triangle Match Puzzle</div>
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
    st.sidebar.markdown("### Triangle Match Puzzle")
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

# ---------- HTML/JS DRAG-AND-DROP MATCH GAME (20 triangles, specific squares) ----------
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
                gap: 15px;
                margin: 20px 0;
            }
            .square {
                width: 80px;
                height: 80px;
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
            .square.correct {
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
                font-size: 40px;
                cursor: default;
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
                gap: 15px;
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
            .error-toast {
                position: fixed;
                bottom: 20px;
                left: 50%;
                transform: translateX(-50%);
                background: #e94560;
                color: white;
                padding: 8px 16px;
                border-radius: 30px;
                font-weight: bold;
                pointer-events: none;
                z-index: 1000;
                opacity: 0;
                transition: opacity 0.2s;
            }
            @media (max-width: 700px) {
                .square { width: 65px; height: 65px; }
                .triangle { width: 65px; height: 65px; font-size: 35px; }
                .triangle-placed { font-size: 35px; }
            }
        </style>
    </head>
    <body>
    <div class="game-container">
        <div class="game-title">
            <h2>🔺 Match Each Triangle to Its Correct Square 🔲</h2>
            <p>Drag a triangle to the square with the same number. Wrong placement = error sound, no placement.</p>
        </div>

        <!-- Squares (20 squares) -->
        <div id="squaresContainer" class="grid"></div>

        <!-- Triangles (20 draggable) -->
        <div id="trianglesContainer" class="triangle-container"></div>

        <div class="info-panel">
            <span class="remaining">🔺 Remaining triangles: <span id="remainingCount">20</span></span>
            <button class="reset-btn" id="resetBtn">⟳ Reset Game</button>
        </div>
        <div id="winMessage" style="display: none;" class="win-message">🎉 YOU WIN! 🎉</div>
    </div>
    <div id="errorToast" class="error-toast">❌ Wrong square! Try again.</div>

    <script>
        // Audio context for sounds (success: high beep, error: low buzz)
        let audioCtx = null;
        function playSound(type) {
            if (!audioCtx) {
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            }
            audioCtx.resume().then(() => {
                const oscillator = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                oscillator.connect(gain);
                gain.connect(audioCtx.destination);
                if (type === 'success') {
                    oscillator.frequency.value = 880;
                    gain.gain.value = 0.3;
                    oscillator.type = 'sine';
                    gain.gain.exponentialRampToValueAtTime(0.00001, audioCtx.currentTime + 0.8);
                    oscillator.start();
                    oscillator.stop(audioCtx.currentTime + 0.8);
                } else {
                    oscillator.frequency.value = 220;
                    gain.gain.value = 0.2;
                    oscillator.type = 'square';
                    gain.gain.exponentialRampToValueAtTime(0.00001, audioCtx.currentTime + 0.5);
                    oscillator.start();
                    oscillator.stop(audioCtx.currentTime + 0.5);
                }
            }).catch(e => console.log("Audio error", e));
        }

        // State: 20 squares, each matched to a triangle id (0-indexed)
        let squareFilled = new Array(20).fill(false);   // true if correct triangle placed
        let triangleUsed = new Array(20).fill(false);   // true if that triangle already placed
        let remaining = 20;

        const squaresContainer = document.getElementById('squaresContainer');
        const trianglesContainer = document.getElementById('trianglesContainer');
        const remainingSpan = document.getElementById('remainingCount');
        const winDiv = document.getElementById('winMessage');
        const errorToast = document.getElementById('errorToast');

        function showErrorToast() {
            errorToast.style.opacity = '1';
            setTimeout(() => { errorToast.style.opacity = '0'; }, 1500);
        }

        function updateRemaining() {
            remainingSpan.innerText = remaining;
        }

        function checkWin() {
            if (remaining === 0) {
                winDiv.style.display = 'block';
                // Trigger balloons via Streamlit? We'll use JS balloons (canvas or simply alert)
                // For simplicity, we'll create floating balloons using canvas.
                createBalloons();
            }
        }

        function createBalloons() {
            const balloonDiv = document.createElement('div');
            balloonDiv.style.position = 'fixed';
            balloonDiv.style.top = '0';
            balloonDiv.style.left = '0';
            balloonDiv.style.width = '100%';
            balloonDiv.style.height = '100%';
            balloonDiv.style.pointerEvents = 'none';
            balloonDiv.style.zIndex = '10000';
            document.body.appendChild(balloonDiv);
            for (let i = 0; i < 100; i++) {
                const balloon = document.createElement('div');
                balloon.style.position = 'absolute';
                balloon.style.bottom = '-50px';
                balloon.style.left = Math.random() * 100 + '%';
                balloon.style.width = '40px';
                balloon.style.height = '50px';
                balloon.style.backgroundColor = `hsl(${Math.random() * 360}, 80%, 60%)`;
                balloon.style.borderRadius = '50%';
                balloon.style.animation = `floatUp ${4 + Math.random() * 2}s linear forwards`;
                balloon.style.fontSize = '24px';
                balloon.style.textAlign = 'center';
                balloon.innerHTML = '🎈';
                balloonDiv.appendChild(balloon);
            }
            const style = document.createElement('style');
            style.textContent = `
                @keyframes floatUp {
                    0% { transform: translateY(0) rotate(0deg); opacity: 1; }
                    100% { transform: translateY(-120vh) rotate(20deg); opacity: 0; }
                }
            `;
            document.head.appendChild(style);
            setTimeout(() => { balloonDiv.remove(); }, 7000);
        }

        // Build squares
        for (let i = 0; i < 20; i++) {
            const square = document.createElement('div');
            square.className = 'square';
            if (squareFilled[i]) square.classList.add('correct');
            square.setAttribute('data-square-id', i);
            square.innerHTML = `<div class="square-label">${i+1}</div><div class="triangle-placed">${squareFilled[i] ? '🔺' : ''}</div>`;
            square.addEventListener('dragover', (e) => {
                e.preventDefault();
            });
            square.addEventListener('drop', (e) => {
                e.preventDefault();
                const squareId = parseInt(e.currentTarget.getAttribute('data-square-id'));
                if (squareFilled[squareId]) return; // already filled
                const triangleId = e.dataTransfer.getData('text/plain');
                if (triangleId === null) return;
                const tid = parseInt(triangleId);
                if (triangleUsed[tid]) return; // already placed (should not happen)
                // Check if triangle matches square (triangle number == square number)
                if (tid === squareId) {
                    // Correct match
                    playSound('success');
                    squareFilled[squareId] = true;
                    triangleUsed[tid] = true;
                    remaining--;
                    updateRemaining();
                    // Update square appearance
                    e.currentTarget.classList.add('correct');
                    e.currentTarget.querySelector('.triangle-placed').innerHTML = '🔺';
                    // Remove triangle from draggable area
                    const triangleElem = document.getElementById(`triangle-${tid}`);
                    if (triangleElem) triangleElem.remove();
                    checkWin();
                } else {
                    // Wrong match
                    playSound('error');
                    showErrorToast();
                }
            });
            squaresContainer.appendChild(square);
        }

        // Build triangles
        for (let i = 0; i < 20; i++) {
            const triangle = document.createElement('div');
            triangle.id = `triangle-${i}`;
            triangle.className = 'triangle';
            triangle.setAttribute('draggable', 'true');
            triangle.setAttribute('data-triangle-id', i);
            triangle.innerHTML = `🔺<span style="font-size:12px; display:block;">${i+1}</span>`;
            triangle.addEventListener('dragstart', (e) => {
                if (triangleUsed[i]) {
                    e.preventDefault();
                    return false;
                }
                e.dataTransfer.setData('text/plain', i);
                e.dataTransfer.effectAllowed = 'move';
                e.target.classList.add('dragging');
            });
            triangle.addEventListener('dragend', (e) => {
                e.target.classList.remove('dragging');
            });
            trianglesContainer.appendChild(triangle);
        }

        function resetGame() {
            // Reset arrays
            squareFilled.fill(false);
            triangleUsed.fill(false);
            remaining = 20;
            updateRemaining();
            winDiv.style.display = 'none';
            // Clear squares and rebuild content
            const squares = document.querySelectorAll('.square');
            squares.forEach((square, idx) => {
                square.classList.remove('correct');
                const placedDiv = square.querySelector('.triangle-placed');
                placedDiv.innerHTML = '';
            });
            // Rebuild triangles container
            trianglesContainer.innerHTML = '';
            for (let i = 0; i < 20; i++) {
                const triangle = document.createElement('div');
                triangle.id = `triangle-${i}`;
                triangle.className = 'triangle';
                triangle.setAttribute('draggable', 'true');
                triangle.setAttribute('data-triangle-id', i);
                triangle.innerHTML = `🔺<span style="font-size:12px; display:block;">${i+1}</span>`;
                triangle.addEventListener('dragstart', (e) => {
                    if (triangleUsed[i]) {
                        e.preventDefault();
                        return false;
                    }
                    e.dataTransfer.setData('text/plain', i);
                    e.dataTransfer.effectAllowed = 'move';
                    e.target.classList.add('dragging');
                });
                triangle.addEventListener('dragend', (e) => {
                    e.target.classList.remove('dragging');
                });
                trianglesContainer.appendChild(triangle);
            }
        }

        document.getElementById('resetBtn').addEventListener('click', resetGame);
        updateRemaining();
    </script>
    </body>
    </html>
    """
    components.html(game_html, height=800, scrolling=False)

# ---------- MAIN APP AFTER LOGIN ----------
def main_app():
    show_sidebar()
    st.markdown("<h1 style='text-align:center;'>🔺 Match the Triangle to Its Square 🔲</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Each triangle has a number. Drag it to the square with the same number. Wrong placement = error sound, correct = success sound and the triangle disappears. Fit all 20 to win!</p>", unsafe_allow_html=True)
    drag_drop_game()
    st.markdown('<div class="footer">© GlobalInternet.py – Train your brain, one puzzle at a time.</div>', unsafe_allow_html=True)

# ---------- ROUTING ----------
if not st.session_state.authenticated:
    login_page()
else:
    main_app()
