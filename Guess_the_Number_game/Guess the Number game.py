# -*- coding: utf-8 -*-
import tkinter as tk
import random

class GuessTheNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")
        self.root.geometry("400x400")

        self.secret_number = random.randint(1, 100)
        self.attempts_remaining = 10

        # Custom fonts and colors
        self.title_font = ("Helvetica", 24, "bold")
        self.label_font = ("Arial", 14)
        self.result_font = ("Arial", 16, "bold")
        self.button_font = ("Arial", 12, "bold")
        self.bg_color = "#F0F0F0"
        self.button_color = "#BA9E60"  # Gold
        self.error_color = "#FF0000"   # Red
        self.result_color = "#0000FF"  # Blue

        self.root.configure(bg=self.bg_color)

        # Create widgets for the GUI
        self.title_label = tk.Label(root, text="Guess the Number", font=self.title_font, bg=self.bg_color)
        self.title_label.pack(pady=20)

        self.guess_label = tk.Label(root, text="Enter your guess (1-100):", font=self.label_font, bg=self.bg_color)
        self.guess_label.pack(pady=10)

        self.guess_entry = tk.Entry(root, width=10, font=self.label_font)
        self.guess_entry.pack(pady=5)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_guess, font=self.button_font, bg=self.button_color, fg="white")
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=self.result_font, fg=self.result_color, bg=self.bg_color)
        self.result_label.pack(pady=20)

        self.restart_button = tk.Button(root, text="Restart", command=self.restart_game, font=self.button_font, bg=self.button_color, fg="white")
        self.restart_button.pack()

    def restart_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts_remaining = 10
        self.result_label.config(text="")
        self.submit_button.config(state=tk.NORMAL)
        self.guess_entry.delete(0, tk.END)

    def check_guess(self):
        guess = self.guess_entry.get()
        if not guess.isdigit():
            self.result_label.config(text="Please enter a valid number.", fg=self.error_color)
            return

        guess = int(guess)
        self.attempts_remaining -= 1

        if guess == self.secret_number:
            self.result_label.config(text=f"Congratulations!\nYou guessed the number {self.secret_number}.", fg=self.result_color)
            self.submit_button.config(state=tk.DISABLED)
        elif self.attempts_remaining == 0:
            self.result_label.config(text=f"Game Over!\nThe secret number was {self.secret_number}.", fg=self.error_color)
            self.submit_button.config(state=tk.DISABLED)
        elif guess < self.secret_number:
            self.result_label.config(text=f"Try a higher number.\nAttempts left: {self.attempts_remaining}", fg=self.result_color)
        else:
            self.result_label.config(text=f"Try a lower number.\nAttempts left: {self.attempts_remaining}", fg=self.result_color)

def main():
    root = tk.Tk()
    guess_the_number_game = GuessTheNumberGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
