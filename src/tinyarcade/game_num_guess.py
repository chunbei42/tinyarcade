import random
import tkinter as tk
from tkinter import messagebox


def generate_range():
    while True:
        a = random.randint(1, 10000)
        b = random.randint(1, 10000)
        if b - a >= 100:
            return a, b


class NumberGuessingGame:
    def __init__(self):
        self.min_num, self.max_num = generate_range()
        self.target_number = random.randint(self.min_num, self.max_num)
        self.attempts = 0

        self.window = tk.Tk()
        self.window.title("Number Guessing Game")
        self.window.geometry("350x220")

        self.guess_label = tk.Label(
            self.window,
            text=f"Guess a number between {self.min_num} and {self.max_num}",
            font=("Arial", 16),
        )
        self.guess_label.pack(pady=10)

        self.guess_entry = tk.Entry(self.window, width=10, font=("Arial", 14))
        self.guess_entry.pack(pady=5)
        self.guess_entry.focus()

        self.check_button = tk.Button(
            self.window, text="Check", command=self.check_guess, font=("Arial", 12)
        )
        self.check_button.pack(pady=5)

        self.result_label = tk.Label(
            self.window, text="", font=("Arial", 14), wraplength=320
        )
        self.result_label.pack(pady=10)

        self.window.bind("<Return>", lambda event: self.check_guess())

    def check_guess(self):
        try:
            user_guess = int(self.guess_entry.get())
            if user_guess < self.min_num or user_guess > self.max_num:
                messagebox.showerror(
                    "Invalid input",
                    f"Please enter a number between {self.min_num} and {self.max_num}.",
                )
                return

            self.attempts += 1

            if user_guess == self.target_number:
                result_text = f"Congratulations! You found the number in {self.attempts} attempt(s)."
                text_color = "green"
                self.check_button.config(state="disabled")
            elif user_guess < self.target_number:
                result_text = "Too low!"
                text_color = "red"
            else:
                result_text = "Too high!"
                text_color = "red"

            self.result_label.config(text=result_text, fg=text_color)
            self.guess_entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    game = NumberGuessingGame()
    game.run()
