import random
from shutil import move
import time
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# ANSI colours
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"


WINNING_COMBINATIONS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


class TerminalTicTacToe:

    def __init__(self):
        self.reset_game_state()

    def reset_game_state(self):
        self.current_player = "X"
        self.mode = None
        self.difficulty = None
        self.board = [str(i) for i in range(1, 10)]

        self.last_move = None
        self.winning_line = None

    def format_cell(self, index):
        value = self.board[index]

        if self.winning_line and index in self.winning_line:
            return f"{GREEN}{value}{RESET}"

        if index == self.last_move:
            return f"{YELLOW}{value}{RESET}"

        return value
    

    def display_board(self):

        print("=" * 35)

        if self.mode == "PVE":
            print(
                f"🎮 Mode: {CYAN}PVE{RESET}    "
                f"🎯 Difficulty: {YELLOW}{self.difficulty}{RESET}"
            )
        elif self.mode == "PVP":
            print(f"🎮 Mode: {CYAN}PVP{RESET}")

        print("=" * 35)

        print()

        print(
            f" {self.format_cell(0)} | "
            f"{self.format_cell(1)} | "
            f"{self.format_cell(2)} "
        )

        print("---+---+---")

        print(
            f" {self.format_cell(3)} | "
            f"{self.format_cell(4)} | "
            f"{self.format_cell(5)} "
        )

        print("---+---+---")

        print(
            f" {self.format_cell(6)} | "
            f"{self.format_cell(7)} | "
            f"{self.format_cell(8)} "
        )

        print()

    def post_game_menu(self):
        while True:
            print("\n[1] 🔄 Play Again")
            print("[2] 🎮 Game Selection")
            print("[q] 🚪 Exit")

            choice = input("\nChoose: ").strip().lower()

            if choice == "1":
                return "again"

            if choice == "2":
                return "menu"

            if choice == "q":
                return "quit"

            print("❌ Invalid choice.")

    def select_mode(self):
        while True:
            clear_screen()
            print("🎮 === TIC TAC TOE === 🎮")
            print("Choose a game mode:")

            print("\n[1] 🧑🤖 PVE - Single Player")
            print("[2] 🧑🧑 PVP - Multi-Player")
            print("[q] 🚪 Return to TinyArcade menu")

            choice = input("\n🎯 Choose a mode: ").strip().lower()

            if choice == "1":
                self.mode = "PVE"

                if not self.select_difficulty():
                    return False

                return True

            if choice == "2":
                self.mode = "PVP"
                return True

            if choice == "q":
                print("\n🚪 Returning to TinyArcade menu...")
                return False

            print("❌ Invalid choice. Please enter 1, 2, or q.")

    def select_difficulty(self):
        while True:
            clear_screen()
            print("🎯 Choose the computer difficulty:")

            print("\n[1] 🟢 Easy   - Random moves")
            print("[2] 🟡 Normal - Blocks and wins when possible")
            print("[3] 🔴 Hard   - Plays the best possible move")
            print("[q] 🚪 Return to TinyArcade menu")

            choice = input("\n🎯 Choose a difficulty: ").strip().lower()

            if choice == "1":
                self.difficulty = "Easy"
                clear_screen()
                return True

            if choice == "2":
                self.difficulty = "Normal"
                clear_screen()
                return True

            if choice == "3":
                self.difficulty = "Hard"
                clear_screen()
                return True

            if choice == "q":
                print("\n🚪 Returning to TinyArcade menu...")
                return False

            print("❌ Invalid choice. Please enter 1, 2, 3, or q.")

    def play(self):
        if not self.select_mode():
            return

        clear_screen()

        print(f"\n🎮 Game Started! Mode: {self.mode}")

        if self.mode == "PVE":
            print(f"🤖 Computer difficulty: {self.difficulty}")

        time.sleep(1.5)

        while True:
            clear_screen()

            self.display_board()
            print(f"Current Turn: {self.current_player}")

            if self.mode == "PVE" and self.current_player == "O":
                print("🤖 Computer is thinking...")
                time.sleep(0.6)
                move = self.get_computer_move()

                self.board[move] = "O"
                self.last_move = move

                clear_screen()
                self.display_board()

                print(
                    f"{MAGENTA}🤖 Computer played "
                    f"position {move + 1}{RESET}"
                )

                time.sleep(1.2)
                if self.check_game_over():
                    break

                self.current_player = "X"
                continue

            else:
                move = self.get_player_move()

                if move == "quit":
                    print("\n🚪 Returning to TinyArcade menu...")
                    return

            self.board[move] = self.current_player
            self.last_move = move

            if self.check_game_over():
                break

            self.current_player = "O" if self.current_player == "X" else "X"

        print("=" * 30)

        action = self.post_game_menu()

        if action == "again":

            mode = self.mode
            difficulty = self.difficulty

            self.reset_game_state()

            self.mode = mode
            self.difficulty = difficulty

            self.play()

        elif action == "menu":

            self.reset_game_state()

            self.play()

        return

    def get_player_move(self):
        while True:
            try:
                move_input = input(
                    f"Choose a position (1-9) to place "
                    f"'{self.current_player}' or [q] to quit: "
                ).strip().lower()

                if move_input == "q":
                    return "quit"

                move = int(move_input) - 1

                if move < 0 or move > 8:
                    print("❌ Please enter a number between 1 and 9.")
                    continue

                if self.board[move] in ["X", "O"]:
                    print("❌ That position is already taken! Try again.")
                    continue

                return move

            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")

    def get_empty_cells(self):
        return [
            i for i in range(9)
            if self.board[i] not in ["X", "O"]
        ]

    def get_computer_move(self):
        if self.difficulty == "Easy":
            return self.get_random_move()

        if self.difficulty == "Normal":
            return self.get_normal_move()

        return self.get_best_move()

    def get_random_move(self):
        empty_cells = self.get_empty_cells()
        return random.choice(empty_cells)

    def find_winning_move(self, player):
        empty_cells = self.get_empty_cells()

        for cell in empty_cells:
            test_board = self.board[:]
            test_board[cell] = player

            if self.check_winner(test_board, player):
                return cell

        return None

    def get_normal_move(self):
        winning_move = self.find_winning_move("O")

        if winning_move is not None:
            return winning_move

        blocking_move = self.find_winning_move("X")

        if blocking_move is not None:
            return blocking_move

        return self.get_random_move()

    def get_best_move(self):
        best_score = -2
        best_move = None
        empty_cells = self.get_empty_cells()

        for cell in empty_cells:
            self.board[cell] = "O"
            score = self.minimax(False)
            self.board[cell] = str(cell + 1)

            if score > best_score:
                best_score = score
                best_move = cell

        return best_move

    def minimax(self, is_computer_turn):
        if self.check_winner(self.board, "O"):
            return 1

        if self.check_winner(self.board, "X"):
            return -1

        empty_cells = self.get_empty_cells()

        if not empty_cells:
            return 0

        if is_computer_turn:
            best_score = -2

            for cell in empty_cells:
                self.board[cell] = "O"
                score = self.minimax(False)
                self.board[cell] = str(cell + 1)
                best_score = max(best_score, score)

            return best_score

        best_score = 2

        for cell in empty_cells:
            self.board[cell] = "X"
            score = self.minimax(True)
            self.board[cell] = str(cell + 1)
            best_score = min(best_score, score)

        return best_score

    def check_winner(self, board, player):
        for combo in WINNING_COMBINATIONS:
            if (
                board[combo[0]] == player
                and board[combo[1]] == player
                and board[combo[2]] == player
            ):
                return True

        return False

    def check_game_over(self):
        for combo in WINNING_COMBINATIONS:
            if (
                self.board[combo[0]]
                == self.board[combo[1]]
                == self.board[combo[2]]
            ):

                self.winning_line = combo

                clear_screen()
                self.display_board()

                winner = self.board[combo[0]]

                if self.mode == "PVE" and winner == "O":
                    print(f"{RED}🤖 Game Over: Computer (O) wins!{RESET}")
                else:
                    print(
                        f"{GREEN}🎉 Game Over: Player {winner} wins!{RESET}"
                    )

                return True

        if all(cell in ["X", "O"] for cell in self.board):
            clear_screen()
            self.display_board()
            print(f"{YELLOW}🤝 Game Over: It's a Draw!{RESET}")
            return True

        return False


def play():
    game = TerminalTicTacToe()
    game.play()


if __name__ == "__main__":
    play()
