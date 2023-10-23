import tkinter as tk
import random


def print_board():
    for i in range(3):
        for j in range(3):
            cell = board[i][j]
            button = tk.Button(root, text=cell, width=10, height=4, font=("Helvetica", 24),
                              command=lambda i=i, j=j: make_move(i, j))
            button.grid(row=i, column=j)


def make_move(i, j):
    global game_over
    if board[i][j] == ' ' and not game_over:
        board[i][j] = 'X'
        print_board()
        if check_winner('X'):
            label.config(text="Oyuncu X kazandı!")
            game_over = True
        elif all(board[i][j] != ' ' for i in range(3) for j in range(3)):
            label.config(text="Oyun berabere bitti.")
            game_over = True
        else:
            play_computer()
            if check_winner('O'):
                label.config(text="Bilgisayar kazandı!")
                game_over = True
            elif all(board[i][j] != ' ' for i in range(3) for j in range(3)):
                label.config(text="Oyun berabere bitti.")
                game_over = True


def check_winner(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def play_computer():
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 'O'
        print_board()


def minimax(board, player):
    if check_winner('X'):
        return -1
    elif check_winner('O'):
        return 1
    elif not any(' ' in row for row in board):
        return 0

    if player == 'O':
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, 'X')
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, 'O')
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score


if __name__ == "__main__":
    root = tk.Tk()
    root.title("XOX")

    board = [[' ' for _ in range(3)] for _ in range(3)]
    game_over = False
    current_player = 'X'

    label = tk.Label(root, text="Sıra: Oyuncu X", font=("Helvetica", 16))
    label.grid(row=3, column=0, columnspan=3)

    print_board()

    root.mainloop()
