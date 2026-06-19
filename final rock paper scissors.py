import tkinter as tk
from tkinter import messagebox
import random

# Scores
user_score = 0
computer_score = 0

# Game function
def play(user_choice):
    global user_score, computer_score

    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    result_text = f"You: {user_choice}\nComputer: {computer_choice}\n\n"

    if user_choice == computer_choice:
        result_text += "🤝 It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result_text += "🎉 You Win!"
        user_score += 1
    else:
        result_text += "😢 Computer Wins!"
        computer_score += 1

    result_label.config(text=result_text)
    score_label.config(
        text=f"Your Score: {user_score}   |   Computer Score: {computer_score}"
    )

# Reset game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Choose Rock, Paper, or Scissors")
    score_label.config(text="Your Score: 0 | Computer Score: 0")

# Main Window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("500x400")
root.resizable(False, False)

# Heading
title = tk.Label(
    root,
    text="🎮 Rock Paper Scissors 🎮",
    font=("Arial", 20, "bold")
)
title.pack(pady=15)

# Buttons
frame = tk.Frame(root)
frame.pack(pady=20)

rock_btn = tk.Button(
    frame, text="🪨 Rock", font=("Arial", 12),
    width=12, command=lambda: play("Rock")
)
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(
    frame, text="📄 Paper", font=("Arial", 12),
    width=12, command=lambda: play("Paper")
)
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(
    frame, text="✂️ Scissors", font=("Arial", 12),
    width=12, command=lambda: play("Scissors")
)
scissors_btn.grid(row=0, column=2, padx=10)

# Result Area
result_label = tk.Label(
    root,
    text="Choose Rock, Paper, or Scissors",
    font=("Arial", 14),
    justify="center"
)
result_label.pack(pady=20)

# Scoreboard
score_label = tk.Label(
    root,
    text="Your Score: 0 | Computer Score: 0",
    font=("Arial", 12, "bold")
)
score_label.pack(pady=10)

# Reset Button
reset_btn = tk.Button(
    root,
    text="🔄 Reset Game",
    font=("Arial", 12),
    command=reset_game
)
reset_btn.pack(pady=15)

# Exit Button
exit_btn = tk.Button(
    root,
    text="❌ Exit",
    font=("Arial", 12),
    command=root.destroy
)
exit_btn.pack()

root.mainloop()
