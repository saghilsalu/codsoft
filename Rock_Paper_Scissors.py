import tkinter as tk
from tkinter import *
import random
from datetime import datetime

player_score = 0
computer_score = 0
history = []
root = tk.Tk()
root.geometry("600x700")
root.title("Rock Paper Scissors Game")
root.configure(bg="#1E1E1E")
title_label = tk.Label(root, text="Rock Paper Scissors Game", font=("Helvetica", 26, "bold"), fg="#FFD700", bg="#1E1E1E")
title_label.pack(pady=20)
user_frame = tk.Frame(root, bg="#1E1E1E")
user_frame.pack(pady=20)
user_label = tk.Label(user_frame, text="Select your choice:", font=("Helvetica", 18), fg="#E5E5E5", bg="#1E1E1E")
user_label.pack(side="left", padx=10)
user_choice = StringVar()
user_choice.set("Select")
radio_rock = tk.Radiobutton(user_frame, text="Rock", variable=user_choice, value="rock", font=("Helvetica", 16), bg="#1E1E1E", fg="#E5E5E5", selectcolor="#4A4A4A")
radio_rock.pack(side="left", padx=5)
radio_paper = tk.Radiobutton(user_frame, text="Paper", variable=user_choice, value="paper", font=("Helvetica", 16), bg="#1E1E1E", fg="#E5E5E5", selectcolor="#4A4A4A")
radio_paper.pack(side="left", padx=5)
radio_scissors = tk.Radiobutton(user_frame, text="Scissors", variable=user_choice, value="scissors", font=("Helvetica", 16), bg="#1E1E1E", fg="#E5E5E5", selectcolor="#4A4A4A")
radio_scissors.pack(side="left", padx=5)
play_button = tk.Button(root, text="Play", font=("Helvetica", 18), fg="#FFFFFF", bg="#FF8C00", bd=2, relief="raised", command=lambda: play_game())
play_button.pack(pady=10)
reset_button = tk.Button(root, text="Reset", font=("Helvetica", 18), fg="#FFFFFF", bg="#FF4500", bd=2, relief="raised", command=lambda: reset_game())
reset_button.pack(pady=10)
result_frame = tk.Frame(root, bg="#1E1E1E")
result_frame.pack(pady=20)
result_label = tk.Label(result_frame, text="Game Result:", font=("Helvetica", 18), fg="#E5E5E5", bg="#1E1E1E")
result_label.pack(side="left", padx=10)
result_textbox = Text(result_frame, height=6, width=40, font=("Helvetica", 16), bg="#2D2D2D", fg="#FFFFFF", borderwidth=2, relief="solid")
result_textbox.pack(padx=10, pady=10)
score_frame = tk.Frame(root, bg="#1E1E1E")
score_frame.pack(pady=10)
score_label = tk.Label(score_frame, text="Score", font=("Helvetica", 18), fg="#E5E5E5", bg="#1E1E1E")
score_label.pack(pady=5)
player_score_label = tk.Label(score_frame, text="Player: 0", font=("Helvetica", 16), fg="#E5E5E5", bg="#1E1E1E")
player_score_label.pack()
computer_score_label = tk.Label(score_frame, text="Computer: 0", font=("Helvetica", 16), fg="#E5E5E5", bg="#1E1E1E")
computer_score_label.pack()
def update_score(winner):
    global player_score, computer_score
    if winner == "player":
        player_score += 1
    elif winner == "computer":
        computer_score += 1
    player_score_label.config(text=f"Player: {player_score}")
    computer_score_label.config(text=f"Computer: {computer_score}")
def update_history(user_choice, computer_choice, result):
    global history
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history.append(f"[{timestamp}] You chose {user_choice}, Computer chose {computer_choice} - {result}")
def reset_game():
    global player_score, computer_score, history
    player_score = 0
    computer_score = 0
    history = []
    player_score_label.config(text="Player: 0")
    computer_score_label.config(text="Computer: 0")
    result_textbox.delete("1.0", END)
def play_game():
    user_choice_value = user_choice.get()
    if user_choice_value not in ["rock", "paper", "scissors"]:
        result_textbox.delete("1.0", END)
        result_textbox.insert(END, "Please select a valid option.")
        return
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result_textbox.delete("1.0", END)
    result_textbox.insert(END, f"Your choice: {user_choice_value}\nComputer's choice: {computer_choice}\n\n")
    if user_choice_value == computer_choice:
        result = "It's a TIE!"
        winner = None
    elif (user_choice_value == "rock" and computer_choice == "scissors") or \
            (user_choice_value == "paper" and computer_choice == "rock") or \
            (user_choice_value == "scissors" and computer_choice == "paper"):
        result = "YOU WIN!"
        winner = "player"
    else:
        result = "YOU LOSE!"
        winner = "computer"

    result_textbox.insert(END, result)
    if winner:
        update_score(winner)
    update_history(user_choice_value, computer_choice, result)
root.mainloop()
