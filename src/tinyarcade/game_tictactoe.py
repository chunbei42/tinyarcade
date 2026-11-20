import random
import tkinter as tk
from tkinter import messagebox


class TicTacToe:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("400x480")

        self.current_player = "X"
        self.mode = None  
        self.buttons = []

        self.menu_frame = tk.Frame(self.window)
        self.menu_frame.pack(pady=100)

        self.mode_label = tk.Label(
            self.menu_frame, text="Select Mode:", font=("Arial", 18, "bold")
        )
        self.mode_label.pack(pady=15)

        self.pve_mode_button = tk.Button(
            self.menu_frame,
            text="PVE (Single Player)",
            font=("Arial", 12),
            width=20,
            command=lambda: self.start_game("PVE"),
        )
        self.pve_mode_button.pack(pady=5)

        self.pvp_mode_button = tk.Button(
            self.menu_frame,
            text="PVP (Multi-Player)",
            font=("Arial", 12),
            width=20,
            command=lambda: self.start_game("PVP"),
        )
        self.pvp_mode_button.pack(pady=5)

    def start_game(self, mode):
        self.mode = mode
        self.current_player = "X"
        self.menu_frame.pack_forget()  

        self.status_label = tk.Label(
            self.window,
            text=f"Mode: {self.mode} | Turn: X",
            font=("Arial", 14),
        )
        self.status_label.pack(pady=10)

        self.board_frame = tk.Frame(self.window)
        self.board_frame.pack()

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(
                    self.board_frame,
                    text="",
                    font=("Arial", 20, "bold"),
                    height=2,
                    width=5,
                    command=lambda r=i, c=j: self.click(r, c),
                )
                button.grid(row=i, column=j, padx=2, pady=2)
                row.append(button)
            self.buttons.append(row)

        self.reset_button = tk.Button(
            self.window,
            text="Back to Menu",
            font=("Arial", 12),
            command=self.reset_to_menu,
        )
        self.reset_button.pack(pady=15)

    def click(self, row, column):
        if self.buttons[row][column].cget("text") != "":
            return
        self.buttons[row][column].config(text=self.current_player)
        if self.check_game_over():
            return
        self.current_player = "O" if self.current_player == "X" else "X"
        self.status_label.config(
            text=f"Mode: {self.mode} | Turn: {self.current_player}"
        )
        if self.mode == "PVE" and self.current_player == "O":
            self.window.after(300, self.computer_move)  

    def computer_move(self):
        empty_cells = [
            (r, c)
            for r in range(3)
            for c in range(3)
            if self.buttons[r][c].cget("text") == ""
        ]
        if empty_cells:
            r, c = random.choice(empty_cells)
            self.click(r, c)

    def check_game_over(self):
        board = [
            [self.buttons[r][c].cget("text") for c in range(3)]
            for r in range(3)
        ]
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != "":
                self.announce_winner(board[i][0])
                return True
            if board[0][i] == board[1][i] == board[2][i] != "":
                self.announce_winner(board[0][i])
                return True
        if board[0][0] == board[1][1] == board[2][2] != "":
            self.announce_winner(board[0][0])
            return True
        if board[0][2] == board[1][1] == board[2][0] != "":
            self.announce_winner(board[0][2])
            return True
        if all(board[r][c] != "" for r in range(3) for c in range(3)):
            messagebox.showinfo("Game Over", "It's a Draw!")
            self.reset_to_menu()
            return True

        return False

    def announce_winner(self, winner):
        if self.mode == "PVE" and winner == "O":
            msg = "Computer (O) wins!"
        else:
            msg = f"Player {winner} wins!"
        messagebox.showinfo("Game Over", msg)
        self.reset_to_menu()

    def reset_to_menu(self):
        self.status_label.destroy()
        self.board_frame.destroy()
        self.reset_button.destroy()
        self.menu_frame.pack(pady=100)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    game = TicTacToe()
    game.run()
