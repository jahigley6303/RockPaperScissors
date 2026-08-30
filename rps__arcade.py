import tkinter as tk
import random
import json
import os

# ------------------------------------------------------------
# SECTION 1 — Leaderboard Storage and File Handling
# ------------------------------------------------------------

# JSON file that saves top 5 scores so they persist after exit
LEADERBOARD_FILE = "leaderboard.json"

def load_leaderboard():
    """
    Load leaderboard data from JSON file.
    If the file doesn't exist yet, return an empty list.
    """
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as f:
            return json.load(f)
    return []

def save_leaderboard(data):
    """
    Save leaderboard back to the JSON file.
    Called every time scores update.
    """
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(data, f) 

# Load leaderboard into memory at startup
leaderboard = load_leaderboard()

# ------------------------------------------------------------
# SECTION 2 — Styling / Color Theme for GUI
# ------------------------------------------------------------

# Dark neon arcade color theme
BG_COLOR = "#0b0f1a"
FG_COLOR = "#39e1ff"
BUTTON_COLOR = "#1a2333"
BUTTON_HOVER = "#2c3f5c"
WIN_COLOR = "#41ff74"
LOSE_COLOR = "#ff4141"
TIE_COLOR = "#ffd541"

# ------------------------------------------------------------
# SECTION 3 — Popup Window to Ask Player Name
# ------------------------------------------------------------

def ask_player_name():
    """
    Opens a popup to ask the user for their player name.
    This name is used for score display and leaderboard storage.
    """
    popup = tk.Toplevel(root)
    popup.title("Enter Player Name")
    popup.configure(bg=BG_COLOR)

    tk.Label(popup, text="Enter your name:", fg=FG_COLOR, bg=BG_COLOR,
             font=("Consolas", 14)).pack(pady=10)

    name_entry = tk.Entry(popup, font=("Consolas", 14))
    name_entry.pack(pady=10)

    def save_name():
        """
        Saves entered name and updates main game window.
        """
        global player_name
        player_name = name_entry.get().strip()
        if player_name:
            popup.destroy()
            welcome_label.config(text=f"Player: {player_name}")

    tk.Button(
        popup, text="Start", command=save_name,
        bg=BUTTON_COLOR, fg=FG_COLOR, font=("Consolas", 12)
    ).pack(pady=15)

# ------------------------------------------------------------
# SECTION 4 — Core Game Logic (Rock Paper Scissors)
# ------------------------------------------------------------

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    """
    Main gameplay function.
    - Computer picks a random choice
    - Compare choices to determine winner
    - Update scores and labels
    - Update leaderboard data
    """
    global user_score, computer_score

    computer_choice = random.choice(choices) 

    # Determine result
    if user_choice == computer_choice:
        result = "Tie!"
        color = TIE_COLOR

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        color = WIN_COLOR
        user_score += 1
    else:
        result = "You Lose!"
        color = LOSE_COLOR
        computer_score += 1

    # Update result display
    result_label.config(
        text=f"Computer chose: {computer_choice}\n{result}",
        fg=color
    )

    # Update scores display
    score_label.config(
        text=f"Score — {player_name}: {user_score} | Computer: {computer_score}"
    )

    # Update leaderboard after every play
    update_leaderboard()

# ------------------------------------------------------------
# SECTION 5 — Leaderboard System (Top 5 Scores)
# ------------------------------------------------------------

def update_leaderboard():
    """
    Adds current player score to leaderboard, sorts it,
    saves only top 5 entries, then refreshes display.
    """
    global leaderboard

    leaderboard.append({"name": player_name, "score": user_score})

    # Sort highest scores first
    leaderboard = sorted(leaderboard, key=lambda x: x["score"], reverse=True)[:5] 

    # Save updated leaderboard
    save_leaderboard(leaderboard)

    # Refresh leaderboard text display
    display_leaderboard()

def display_leaderboard():
    """
    Formats leaderboard text and updates label in GUI.
    """
    text = "🏆 Leaderboard (Top 5)\n"
    text += "----------------------\n" 

    for i, entry in enumerate(leaderboard, start=1):
        text += f"{i}. {entry['name']} — {entry['score']}\n"

    leaderboard_label.config(text=text)

# ------------------------------------------------------------
# SECTION 6 — Reset Button (Reset Scores Only)
# ------------------------------------------------------------

def reset_scores():
    """
    Resets only current session scores.
    Leaderboard remains unchanged.
    """
    global user_score, computer_score

    user_score = 0
    computer_score = 0

    score_label.config(
        text=f"Score — {player_name}: {user_score} | Computer: {computer_score}"
    )
    result_label.config(text="", fg=FG_COLOR)

# ------------------------------------------------------------
# SECTION 7 — Hover Animation for Buttons
# ------------------------------------------------------------
 
def on_enter(event):
    """
    Called when mouse enters a button.
    Changes background color for a neon 'hover' effect.
    """
    event.widget["bg"] = BUTTON_HOVER

def on_leave(event):

    """
    Called when mouse leaves a button.
    Restores normal button color.
    """
    event.widget["bg"] = BUTTON_COLOR

# ------------------------------------------------------------
# SECTION 8 — GUI Setup and Layout
# ------------------------------------------------------------

root = tk.Tk()
root.title("Dark Arcade Rock Paper Scissors")
root.configure(bg=BG_COLOR)
root.geometry("600x550")
 
# Initial game state variables
player_name = ""
user_score = 0
computer_score = 0 

# Player name display
welcome_label = tk.Label(root, text="Player: Not Set", fg=FG_COLOR, bg=BG_COLOR,
                         font=("Consolas", 18))
welcome_label.pack(pady=10)

# Button to open name entry popup
tk.Button(
    root, text="Set Player Name", command=ask_player_name,
    bg=BUTTON_COLOR, fg=FG_COLOR, font=("Consolas", 12)
).pack(pady=10)

# Frame that contains R/P/S buttons
button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(pady=20)
 
# Create Rock, Paper, Scissors buttons
for choice in choices:
    btn = tk.Button(
        button_frame, text=choice, width=12,
        bg=BUTTON_COLOR, fg=FG_COLOR, font=("Consolas", 16),
        command=lambda c=choice: play(c)
    )
    btn.pack(side="left", padx=10)

    # Hover animations
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# Result text label
result_label = tk.Label(root, text="", fg=FG_COLOR, bg=BG_COLOR, font=("Consolas", 20))
result_label.pack(pady=10) 

# Score label
score_label = tk.Label(root, text="Score — Player: 0 | Computer: 0",
                       fg=FG_COLOR, bg=BG_COLOR, font=("Consolas", 16))
score_label.pack(pady=10)
 
# Reset scores button
reset_button = tk.Button(
    root, text="Reset Scores", command=reset_scores,
    bg=BUTTON_COLOR, fg=FG_COLOR, font=("Consolas", 14)
)
reset_button.pack(pady=10)


# Leaderboard display label
leaderboard_label = tk.Label(root, text="", fg=FG_COLOR, bg=BG_COLOR, font=("Consolas", 14))
leaderboard_label.pack(pady=20)


# Initial leaderboard load
display_leaderboard()


# Start Tkinter event loop
root.mainloop()

 
 

