import random
import time
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

CHOICES = ["rock", "paper", "scissors"]

CHOICE_EMOJI = {
    "rock": "✊ Rock",
    "paper": "✋ Paper",
    "scissors": "✌️ Scissors",
}

WINNING_MOVES = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}

DIFFICULTIES = {
    "1": ("Easy", 1),
    "2": ("Normal", 3),
    "3": ("Hard", 3),
}

# ANSI colours
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"


def choose_difficulty():
    while True:
        clear_screen()
        print("🎮 === ROCK, PAPER, SCISSORS === 🎮")
        print("Choose your difficulty:")

        print("\n[1] 🟢 Easy   - Win 1 round")
        print("[2] 🟡 Normal - First to 3 points")
        print("[3] 🔴 Hard   - Win 3 rounds in a row")
        print("[q] 🚪 Return to TinyArcade menu")

        choice = input("\n🎯 Choose a difficulty: ").strip().lower()

        if choice == "q":
            return None

        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]

        print("❌ Invalid choice. Please enter 1, 2, 3, or q.")


def get_computer_choice():
    return random.choice(CHOICES)


def get_player_choice():
    while True:
        print("Choose your move:")
        print("[1] ✊ Rock")
        print("[2] ✋ Paper")
        print("[3] ✌️ Scissors")
        print("[q] 🚪 Quit and return to Menu")

        choice = input("Enter 1, 2, 3, or q: ").strip().lower()

        if choice == "q":
            return "quit"

        if choice == "1":
            return "rock"

        if choice == "2":
            return "paper"

        if choice == "3":
            return "scissors"

        clear_screen()
        print("❌ Invalid choice. Please enter 1, 2, 3, or q.")


def decide_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"

    if WINNING_MOVES[player_choice] == computer_choice:
        return "player"

    return "computer"


def show_scoreboard(player_score, computer_score, difficulty_name):
    print(f"\n📊 SCOREBOARD - {difficulty_name.upper()}")

    if difficulty_name == "Hard":
        player_display = "🟩" * player_score + "⬜" * (3 - player_score)
        computer_display = "🟥" * computer_score + "⬜" * (3 - computer_score)

        print("🧑 You      :", player_display)
        print("🤖 Computer :", computer_display)

    else:
        player_display = "🟩" * player_score + "⬜" * (3 - player_score)
        computer_display = "🟥" * computer_score + "⬜" * (3 - computer_score)

        print("🧑 You      :", player_display)
        print("🤖 Computer :", computer_display)


def show_round_result(player_choice, computer_choice, result):
    print("🎮 ROUND RESULT")
    print(f"🧑 You      chose: {CHOICE_EMOJI[player_choice]}")
    print(f"🤖 Computer chose: {CHOICE_EMOJI[computer_choice]}")
    print("-" * 30)

    if result == "player":
        print(f"{GREEN}🎉 You win this round!{RESET}")
    elif result == "computer":
        print(f"{RED}🤖 Computer wins this round!{RESET}")
    else:
        print(f"{YELLOW}🤝 It's a tie!{RESET}")


def play_match(difficulty_name, target_score):
    player_score = 0
    computer_score = 0

    print(f"🎮 === ROCK, PAPER, SCISSORS: {difficulty_name.upper()} === 🎮")

    if difficulty_name == "Easy":
        print("🏆 Win 1 round against the computer!")

    elif difficulty_name == "Normal":
        print("🏆 First to 3 points wins!")

    else:
        print("🏆 Win 3 rounds in a row!")
        print("⚠️ A tie or loss resets both winning streaks.")

    while True:
        player_choice = get_player_choice()

        if player_choice == "quit":
            print("\n🚪 Returning to Menu...")
            return "quit"

        clear_screen()

        computer_choice = get_computer_choice()

        print("\n✊ ✋ ✌️")
        print("Revealing choices...")
        time.sleep(1)

        clear_screen()

        result = decide_winner(player_choice, computer_choice)

        show_round_result(player_choice, computer_choice, result)

        if difficulty_name == "Hard":

            if result == "player":
                player_score += 1
                computer_score = 0

            elif result == "computer":
                computer_score += 1
                player_score = 0

            else:
                player_score = 0
                computer_score = 0
        else:

            if result == "player":
                player_score += 1

            elif result == "computer":
                computer_score += 1

        show_scoreboard(
            player_score,
            computer_score,
            difficulty_name,
        )

        # Easy: player needs only one win
        if difficulty_name == "Easy" and player_score >= 1:
            print(f"\n{GREEN}🎉 CONGRATULATIONS! You won the Easy match!{RESET}")

            input("\nPress ENTER to continue...")
            clear_screen()

            return "player"

        # Normal: first to 3 points
        if difficulty_name == "Normal":
            if player_score >= 3:
                print(f"\n{GREEN}🎉 CONGRATULATIONS! You won the match!{RESET}")
                input("\nPress ENTER to continue...")
                clear_screen()
                return "player"

            if computer_score >= 3:
                print(f"\n{RED}🤖 The computer won the match. Try again!{RESET}")
                input("\nPress ENTER to continue...")
                clear_screen()
                return "computer"

        # Hard: three consecutive wins by either player or computer
        if difficulty_name == "Hard":
            if player_score >= 3:
                print(f"\n{GREEN}🎉 AMAZING! You won 3 rounds in a row!{RESET}")
                input("\nPress ENTER to continue...")
                clear_screen()
                return "player"

            if computer_score >= 3:
                print(f"\n{RED}🤖 The computer won 3 rounds in a row. Try again!{RESET}")
                input("\nPress ENTER to continue...")
                clear_screen()
                return "computer"

        input("\nPress ENTER for the next round...")
        clear_screen()


def ask_play_again():
    while True:
        print("What would you like to do?")
        print("[1] Play Rock, Paper, Scissors again")
        print("[2] Return to Menu")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            return True

        if choice == "2":
            return False

        print("❌ Invalid choice. Please enter 1 or 2.")


def play():
    while True:
        difficulty = choose_difficulty()

        if difficulty is None:
            break

        difficulty_name, target_score = difficulty

        clear_screen()

        result = play_match(difficulty_name, target_score)

        if result == "quit":
            break

        if not ask_play_again():
            break


if __name__ == "__main__":
    play()
