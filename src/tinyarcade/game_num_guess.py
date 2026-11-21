import random


def generate_range():
    while True:
        a = random.randint(1, 10000)
        b = random.randint(1, 10000)
        if b - a >= 100:
            return a, b


class TerminalGuessingGame:

    def __init__(self):
        self.min_num, self.max_num = generate_range()
        self.target_number = random.randint(self.min_num, self.max_num)
        self.attempts = 0

    def play(self):
        print("=== Welcome to the Number Guessing Game! ===")
        print(f"I'm thinking of a number between {self.min_num} and {self.max_num}.\n")

        while True:
            try:
                # Prompt the user for input
                user_input = input(
                    f"Enter your guess ({self.min_num}-{self.max_num}): "
                )

                # Allow user to quit early
                if user_input.lower() == "exit":
                    print(
                        f"Game over! The correct number was {self.target_number}."
                    )
                    break

                user_guess = int(user_input)

                # Validate range
                if user_guess < self.min_num or user_guess > self.max_num:
                    print(
                        f"❌ Invalid range! Please stay between {self.min_num} and {self.max_num}.\n"
                    )
                    continue

                self.attempts += 1

                # Check guess
                if user_guess == self.target_number:
                    print(
                        f"\n🎉 Congratulations! You found the number in {self.attempts} attempt(s)!"
                    )
                    break
                elif user_guess < self.target_number:
                    print("📉 Too low! Try again.\n")
                else:
                    print("📈 Too high! Try again.\n")

            except ValueError:
                print("❌ Invalid input! Please enter a valid whole number.\n")


if __name__ == "__main__":
    game = TerminalGuessingGame()
    game.play()
