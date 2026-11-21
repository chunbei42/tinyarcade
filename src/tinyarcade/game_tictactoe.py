import random
import time


class TerminalTicTacToe:

    def __init__(self):
        self.reset_game_state()

    def reset_game_state(self):
        self.current_player = "X"
        self.mode = None
        self.board = [str(i) for i in range(1, 10)]

    def display_board(self):
        print("\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("\n")

    def select_mode(self):
        while True:
            print("=== Welcome to Tic Tac Toe ===")
            print("1. PVE (Single Player)")
            print("2. PVP (Multi-Player)")
            print("3. Exit")
            choice = input("Select Mode (1-3): ").strip()

            if choice == "1":
                self.mode = "PVE"
                return True
            elif choice == "2":
                self.mode = "PVP"
                return True
            elif choice == "3":
                print("Goodbye!")
                return False
            else:
                print("❌ Invalid choice. Please enter 1, 2, or 3.\n")

    def play(self):
        while self.select_mode():
            self.reset_game_state()
            print(f"\n🎮 Game Started! Mode: {self.mode}")

            while True:
                self.display_board()
                print(f"Current Turn: {self.current_player}")

                if self.mode == "PVE" and self.current_player == "O":
                    print("🤖 Computer is thinking...")
                    time.sleep(0.6)
                    move = self.get_computer_move()
                else:
                    move = self.get_player_move()

                self.board[move] = self.current_player

                if self.check_game_over():
                    break

                self.current_player = "O" if self.current_player == "X" else "X"

            print("=" * 30 + "\n")

    def get_player_move(self):
        while True:
            try:
                move_input = input(
                    f"Choose a position (1-9) to place '{self.current_player}': "
                ).strip()
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

    def get_computer_move(self):
        empty_cells = [i for i in range(9) if self.board[i] not in ["X", "O"]]
        return random.choice(empty_cells)

    def check_game_over(self):
        win_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]

        for combo in win_combinations:
            if (
                self.board[combo[0]]
                == self.board[combo[1]]
                == self.board[combo[2]]
            ):
                self.display_board()
                winner = self.board[combo[0]]
                if self.mode == "PVE" and winner == "O":
                    print("🤖 Game Over: Computer (O) wins!")
                else:
                    print(f"🎉 Game Over: Player {winner} wins!")
                return True

        if all(cell in ["X", "O"] for cell in self.board):
            self.display_board()
            print("🤝 Game Over: It's a Draw!")
            return True

        return False


if __name__ == "__main__":
    game = TerminalTicTacToe()
    game.play()
