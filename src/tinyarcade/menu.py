from tinyarcade import game_num_guess
from tinyarcade import game_mastermind
from tinyarcade import game_tictactoe
from tinyarcade import game_colour_memorizing

GAMES = {
    "1": ("Number Guess", game_num_guess.play),
    "2": ("Mastermind", game_mastermind.play),
    "3": ("Tic Tac Toe", game_tictactoe.play),
    "4": ("Colour Memorizing", game_colour_memorizing.play),
}


def show_menu():
    print("\n=== TinyArcade ===")
    for key, (name, _) in GAMES.items():
        print(f"{key}. {name}")
    print("q. Quit")


def run():
    while True:
        show_menu()
        choice = input("Choose a game: ").strip().lower()

        if choice == "q":
            print("Thanks for playing TinyArcade!")
            break

        if choice in GAMES:
            _, game_function = GAMES[choice]
            game_function()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    run()