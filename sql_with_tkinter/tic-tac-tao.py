import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [" " for _ in range(9)]

        # Create and style buttons with colors
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(master, font=("Arial", 20), width=6, height=3,
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(button)
                button.config(bg="#ffffff", fg="#000000", activebackground="#90ee90", activeforeground="#000000")

        # Add background color
        master.configure(bg="#d3d3d3")

    def on_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
                winning_line = self.find_winning_line()
                for index in winning_line:
                    self.buttons[index].config(bg="#FFFF00")  # Highlight winning line
                self.disable_buttons()
            elif " " not in self.board:
                messagebox.showinfo("Draw", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != " ":
                return True
        return False

    def find_winning_line(self):
        lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != " ":
                return line
        return []

    def reset_board(self):
        for i in range(9):
            self.board[i] = " "
            self.buttons[i].config(text=" ", bg="#ffffff")  # Reset button colors
            self.buttons[i].config(state=tk.NORMAL)  # Enable buttons
        self.current_player = "X"

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state=tk.DISABLED)  # Disable buttons

if __name__ == "__main__":
    root = tk.Tk()

    # Set window size and center it on screen
    window_width = 300
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create game instance
    game = TicTacToe(root)
    root.mainloop()
