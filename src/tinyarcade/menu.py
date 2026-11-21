import os

from tinyarcade import game_num_guess
from tinyarcade import game_mastermind
from tinyarcade import game_tictactoe
from tinyarcade import game_colour_memorizing
from tinyarcade import game_rock_paper_scissors
from tinyarcade import game_hangman


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


GAMES = {
    "1": ("Number Guess", game_num_guess.play),
    "2": ("Mastermind", game_mastermind.play),
    "3": ("Tic Tac Toe", game_tictactoe.play),
    "4": ("Colour Memorizing", game_colour_memorizing.play),
    "5": ("Rock, Paper, Scissors", game_rock_paper_scissors.play),
    "6": ("Hangman", game_hangman.play),
}


def show_menu():
    print("=" * 50)
    print("🎮 TINYARCADE 🎮".center(50))
    print("Select a Game".center(50))
    print("=" * 50)
    print()

    for key, (name, _) in GAMES.items():
        print(f" [{key}] {name}")

    print(" [Q] Quit")

    print()
    print("=" * 50)


def show_goodbye():
    clear_screen()

    print("=" * 50)
    print("THANK YOU FOR PLAYING".center(50))
    print("TINYARCADE".center(50))
    print("=" * 50)
    print()
    print("🎮 Hope you had fun!".center(50))
    print("🏆 Keep practicing and challenge yourself!".center(50))
    print("🕹️ Thanks for supporting TinyArcade!".center(50))
    print()
    print("=" * 50)

    input("\nPress Enter to exit...")


def run():
    while True:
        clear_screen()
        show_menu()

        choice = input("👉 Enter your choice: ").strip().lower()

        if choice == "q":
            show_goodbye()
            break

        if choice in GAMES:
            _, game_function = GAMES[choice]

            clear_screen()
            game_function()

        else:
            print("\n❌ Invalid choice. Please try again.")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    run()
