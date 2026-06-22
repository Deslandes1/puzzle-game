Triangle Memory Puzzle

An interactive brain training game designed to boost memory and cognitive skills through fun drag-and-drop puzzles. Perfect for both adults and kids who want to improve their memory and learning abilities.

---

About the Project

The Triangle Memory Puzzle is a web-based memory training game that challenges players to remember the position of hidden numbers. Each square hides a random number, and the player must drag the triangle with the matching number to the correct square. By remembering where each number is hidden, the player trains their brain to retain and recall information more effectively.

Key Features

Three difficulty levels: 10, 20, and 100 squares
Audio feedback for correct and incorrect moves
Celebration animations when you win
AI female voice description of the app
Multilingual support: English, Spanish, French, Haitian Creole
Fully responsive design for mobile and desktop
Dark theme with a professional look
Simple login system

Why Play This Game?

Improves short-term memory and recall
Enhances concentration and focus
Develops better learning habits
Fun and engaging for all ages
Perfect for students, professionals, and parents

---

How It Works

The game presents a grid of squares, each hiding a random number. A set of triangles with matching numbers is displayed below. The player must drag each triangle to the square that contains its matching number. If correct, the triangle stays and the square turns green. If wrong, an error sound plays and the triangle returns to its original position.

The challenge is to remember where each number is hidden while matching all triangles correctly.

Difficulty Levels

Level 1: 10 squares - Perfect for beginners and kids
Level 2: 20 squares - Good for intermediate players
Level 3: 100 squares - Ultimate challenge for memory experts

---

Getting Started

Prerequisites

Python 3.8 or higher
pip (Python package manager)

Installation

First, clone the repository.

git clone https://github.com/yourusername/triangle-memory-puzzle.git
cd triangle-memory-puzzle

Next, install the required dependencies.

pip install -r requirements.txt

Then, run the application.

streamlit run app.py

Finally, open your browser and navigate to http://localhost:8501. Login with the password 20082010.

---

Deployment

Deploy on Streamlit Cloud

Push your code to a GitHub repository.
Go to Streamlit Cloud.
Click New app and select your repository.
Deploy and get your public URL.

Deploy on Arm-Powered Devices

This app is optimized to run on Arm-powered devices including Raspberry Pi, Android phones and tablets, Apple Silicon Macs, and Arm64 cloud instances.

To run on an Arm device, install Python 3.8 or higher for your Arm platform, clone the repository, install dependencies, and run streamlit run app.py. Access the app via the device's IP address on port 8501.

---

Arm AI Optimization Challenge

This project is submitted to the Arm AI Optimization Challenge 2026 - Mobile AI Track.

Optimizations Implemented

Client-side processing: All game logic runs in the browser using HTML, CSS, and JavaScript, reducing server load.
Lightweight design: Minimal dependencies for fast startup and low memory usage.
Mobile responsive: Optimized for touch input on phones and tablets.
Efficient rendering: Uses CSS animations instead of heavy JavaScript libraries.
Audio optimization: Web Audio API for efficient sound playback.

Measurable Improvements

Memory usage is minimal because everything runs in the browser.
Startup time is fast because the game uses pure HTML, CSS, and JavaScript.
Response time is instant for drag and drop interactions.
Battery efficiency is optimized for mobile devices.

---

Technologies Used

Python for backend logic and the Streamlit framework.
Streamlit for the web application framework.
HTML, CSS, and JavaScript for frontend game logic.
gTTS for text-to-speech AI voice feature.
Streamlit Cloud for deployment.
MIT License for open source.

---

Project Structure

triangle-memory-puzzle/
├── app.py                  Main application file
├── requirements.txt        Python dependencies
├── README.md              This file
└── .streamlit/
    └── secrets.toml       Configuration if needed

---

Future Enhancements

User accounts and progress tracking
Daily challenges and leaderboards
Additional difficulty levels
Sound effects library
Multiplayer mode
Statistics dashboard

---

About the Creator

This project was built by Gesner Deslandes, Engineer in Chief at GlobalInternet.py.

We are a software company based in Haiti that builds tailor-made solutions connecting the global market with our local expertise. We believe in using technology to educate and empower.

Contact

Phone: (509) 4738-5663
Email: deslandes78@gmail.com
Website: https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/

---

License

This project is open source and available under the MIT License.

---

Acknowledgments

Built with Streamlit.
Powered by Python.
Inspired by memory training games.
Special thanks to the Arm AI Optimization Challenge team.

---

Support

If you find this project helpful, please consider starring the repository, sharing with others, providing feedback, or contributing to the project.

We are proud to say: We are the best!

Enjoy the game and train your brain every day.
