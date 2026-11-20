import random
import os


# ANSI Colors
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_rules():
    print("=" * 40)
    print("🎮 CODE BREAKER")
    print("=" * 40)

    print("\nRULES")
    print("- Guess the secret code.")
    print("- Digits = correct digits in the code.")
    print("- Positions = correct digits in the correct position.")
    print("- Type 'hint' to use a hint.")
    print("- Type 'q' during a game to quit the round.")
    print()

    print("DIFFICULTY")
    print("1. Easy   (3 digits, 0 hints)")
    print("2. Normal (4 digits, 1 hint)")
    print("3. Hard   (6 digits, 2 hints)")
    print()

    print("Type 'q' to quit.")
    print()


def choose_difficulty():
    while True:
        clear_screen()
        show_rules()

        choice = input("Choice: ").strip().lower()

        if choice == "1":
            return 3, 0

        if choice == "2":
            return 4, 1

        if choice == "3":
            return 6, 2

        if choice == "q":
            return None

        input("❌ Invalid choice. Press Enter...")


def analyze_guess(guess, secret):
    positions = 0

    for i in range(len(secret)):
        if guess[i] == secret[i]:
            positions += 1

    digits = 0
    temp_secret = list(secret)

    for digit in guess:
        if digit in temp_secret:
            digits += 1
            temp_secret.remove(digit)

    return digits, positions


def display_history(history):
    print("📜 Guess History\n")

    if not history:
        print("No guesses yet.")
        return

    print(
        f"{'No.':<5}"
        f"{'Guess':<10}"
        f"{'Digits':<10}"
        f"{'Positions'}"
    )

    print("-" * 35)

    for i, item in enumerate(history, start=1):
        print(
            f"{i:<5}"
            f"{item['guess']:<10}"
            f"{item['digits']:<10}"
            f"{item['positions']}"
        )


def display_game(
    code_length,
    tries,
    hints_left,
    hint_messages,
    history,
):
    print("🎮 CODE BREAKER\n")

    print(f"Digits     : {code_length}")
    print(f"Tries      : {tries}")
    print(f"Hints Left : {hints_left}")

    print()

    if hint_messages:
        print("💡 Hints")

        for message in hint_messages:
            print(message)

        print()

    display_history(history)

    print()


def color_guess(guess, secret):
    """
    Used ONLY on final results screen.
    Handles duplicate numbers correctly.
    """
    colors = [""] * len(guess)

    secret_remaining = []
    guess_remaining = []

    # Pass 1 - exact matches
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            colors[i] = GREEN
        else:
            secret_remaining.append(secret[i])
            guess_remaining.append((i, guess[i]))

    # Pass 2 - wrong position matches
    for index, digit in guess_remaining:
        if digit in secret_remaining:
            colors[index] = YELLOW
            secret_remaining.remove(digit)
        else:
            colors[index] = RED

    result = ""

    for i in range(len(guess)):
        result += colors[i] + guess[i] + RESET

    return result


def show_final_history(history, secret):
    clear_screen()

    print("📜 FINAL GUESS HISTORY\n")

    print("Legend:")
    print(f"{GREEN}■{RESET} Correct digit and position")
    print(f"{YELLOW}■{RESET} Correct digit, wrong position")
    print(f"{RED}■{RESET} Not in code")

    print()

    print(
        f"{'No.':<5}"
        f"{'Guess':<12}"
        f"{'Digits':<10}"
        f"{'Positions'}"
    )

    print("-" * 40)

    for i, item in enumerate(history, start=1):
        coloured_guess = color_guess(
            item["guess"],
            secret,
        )

        # ANSI colours break width calculation,
        # so manually add spacing.
        spacing = max(
            1,
            12 - len(item["guess"]),
        )

        print(
            f"{i:<5}"
            f"{coloured_guess}"
            f"{' ' * spacing}"
            f"{item['digits']:<10}"
            f"{item['positions']}"
        )

    print()

    while True:
        print("\nWhat would you like to do?")
        print("[1] Play Code Breaker again")
        print("[2] Return to Menu")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            return True

        if choice == "2":
            return False

        print("❌ Invalid choice. Please enter 1 or 2.")


def play_round():
    difficulty = choose_difficulty()

    if difficulty is None:
        return False

    code_length, max_hints = difficulty

    secret_code = "".join(
        str(random.randint(0, 9))
        for _ in range(code_length)
    )

    tries = 0
    hints_left = max_hints

    history = []
    hint_messages = []

    while True:
        clear_screen()

        display_game(
            code_length,
            tries,
            hints_left,
            hint_messages,
            history,
        )

        guess = input(
            "Enter guess ('hint' or 'q'): "
        ).strip().lower()

        # Quit current round
        if guess == "q":
            return True

        # Hint
        if guess == "hint":
            if hints_left <= 0:
                clear_screen()
                print("❌ No hints remaining.")

                input(
                    "\nPress Enter to continue..."
                )

                continue

            position = random.randint(
                0,
                code_length - 1,
            )

            hint_message = (
                f"Digit #{position + 1} "
                f"is {secret_code[position]}"
            )

            hint_messages.append(hint_message)
            hints_left -= 1

            continue

        # Input validation
        if (
            len(guess) != code_length
            or not guess.isdigit()
        ):
            clear_screen()

            print(
                f"❌ Please enter exactly "
                f"{code_length} digits."
            )

            input(
                "\nPress Enter to continue..."
            )

            continue

        tries += 1

        digits, positions = analyze_guess(
            guess,
            secret_code,
        )

        history.append(
            {
                "guess": guess,
                "digits": digits,
                "positions": positions,
            }
        )

        # Win
        if guess == secret_code:
            clear_screen()

            print("🎉 CONGRATULATIONS!\n")
            print(f"✅ Secret Code : {secret_code}")
            print(f"🔢 Total Tries : {tries}")

            input(
                "\nPress Enter to view results..."
            )

            return show_final_history(
                history,
                secret_code,
            )


def play():
    while True:
        result = play_round()

        if result is False:
            break

    clear_screen()
    print("Returning to game menu...")


if __name__ == "__main__":
    play()
