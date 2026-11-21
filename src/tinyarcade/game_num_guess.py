import random
import os

def clr():
    os.system("cls" if os.name == "nt" else "clear")

# ANSI colours
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"


def generate_range():
    return 1, 1000


def get_guess(min_num, max_num):
    user_input = input(
        f"\n🎯 Enter your guess ({min_num}-{max_num}) "
        f"or [q] to quit: "
    ).strip().lower()

    if user_input == "q":
        return "quit", None

    try:
        guess = int(user_input)
    except ValueError:
        return None, (
            user_input,
            "❌ Invalid input! Please enter a whole number."
        )

    if guess < min_num or guess > max_num:
        return None, (
            str(guess),
            f"❌ Invalid range! Please stay between "
            f"{min_num} and {max_num}."
        )

    return guess, None


def update_range(guess, target_number, min_num, max_num):
    if guess < target_number:
        print(f"{CYAN}📉 Too low! The number is higher than {guess}.{RESET}")
        return guess + 1, max_num

    if guess > target_number:
        print(f"{YELLOW}📈 Too high! The number is lower than {guess}.{RESET}")
        return min_num, guess - 1

    return min_num, max_num


def show_result(guess, target_number, attempts):
    print("🎮 GUESS RESULT")
    print(f"🎯 Your guess  : {guess}")

    if guess == target_number:
        print(f"🤫 Secret number: {target_number}")
    else:
        print("🤫 Secret number: ???")

    print("-" * 30)

    if guess == target_number:
        print(
            f"{GREEN}🎉 Congratulations! You found the number "
            f"in {attempts} attempt(s)!{RESET}"
        )
        return True

    return False


def ask_play_again():
    while True:
        print("\nWhat would you like to do?")
        print("[1] Play Number Guess again")
        print("[2] Return to Menu")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            return True

        if choice == "2":
            return False

        print("❌ Invalid choice. Please enter 1 or 2.")


def play():
    while True:
        clr()

        min_num, max_num = generate_range()
        target_number = random.randint(min_num, max_num)
        attempts = 0

        print("🔢 === NUMBER GUESSING GAME === 🔢")
        print(
            f"I'm thinking of a number between "
            f"{min_num} and {max_num}."
        )
        print("🏆 Guess the secret number!")

        while True:
            guess, error = get_guess(min_num, max_num)

            if guess == "quit":
                print("\n🚪 Returning to TinyArcade menu...")
                return

            if error:
                entered_value, error_msg = error

                clr()

                print("🎮 GUESS RESULT")
                print(f"🎯 Your guess  : {entered_value}")
                print("🤫 Secret number: ???")
                print("-" * 30)
                print(f"{RED}{error_msg}{RESET}")

                continue

            attempts += 1

            clr()

            won = show_result(guess, target_number, attempts)

            if won:
                break

            min_num, max_num = update_range(
                guess,
                target_number,
                min_num,
                max_num,
            )

        if not ask_play_again():
            break


if __name__ == "__main__":
    play()
