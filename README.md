Rock Paper Scissors Arcade
created by Jamie Pascual
A neon‑arcade styled Rock–Paper–Scissors game built in Python (Tkinter) with animated buttons, a persistent leaderboard, and multiple‑player support.
This project is designed to be fun, visually engaging, and beginner‑friendly to understand.

🎮 Features

Dark neon arcade themed UI
Animated hover buttons
Score tracking (player & computer)
Player name popup when starting the game
Top‑5 leaderboard saved in a JSON file
Reset button for scores
Vertical flowchart diagram included (rps_flowchart.png)
Simple, readable, fully commented Python code


📁 Project Structure
project_folder/
│
├── rps_arcade.py          # Main game code (Tkinter GUI)
├── leaderboard.json       # Saved leaderboard (auto-created)
└── rps_flowchart.png      # Architecture diagram


🚀 How to Run
1. Install Python
   Make sure you have Python 3 installed.
2. Run the game
   In terminal or IntelliJ:
   python rps_arcade.py

The arcade game window will appear.
Click Set Player Name to begin.

📊 Leaderboard System
The leaderboard automatically stores:

Player name
High score

Leaderboard data is saved in:
leaderboard.json

Even after closing the game, your scores are preserved.

🧩 Flowchart Diagram
A vertical flowchart showing the function flow is included:
rps_flowchart.png

This diagram illustrates:

Program startup
GUI initialization
Name entry
Game loop (Rock/Paper/Scissors)
Score updates
Leaderboard updates


💻 Technologies Used

Python 3
Tkinter (GUI)
Pillow (only for generating diagrams)


🛠 Future Enhancements

Neon animations
Arcade sound effects
Pixel icons for Rock/Paper/Scissors
Difficulty modes
Full‑screen arcade mode
PyInstaller EXE packaging


📜 License
This project is open for personal or learning use.