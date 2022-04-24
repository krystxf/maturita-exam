#!/usr/bin/python


from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy
from game import Game
from player import Player
from user_inputs import get_user_inputs


# sign variable to decide the turn of which player
turn_number = 2

gameboard_size, player1_sign, player1_name, player2_name = get_user_inputs()

game = Game(gameboard_size)
# setup window
window = Tk()   # init a window
window.geometry("400x400")  # size of the window
window.title("Piškvorky")  # title


# init player 1
if player1_sign != "X":
    player1_sign = "O"
player1 = Player(player1_sign, Button(
    window), player1_name)

# init player 2
player2 = Player("O" if player1.sign == "X" else "X", Button(
    window), player2_name)

# init player Buttons
player1.button.grid(row=1, column=1)
player2.button.grid(row=1, column=2)


def get_text(x, y, window):
    global turn_number
    # if selected field is empty fill it
    if game.board[x][y] == ' ':
        is_even: bool = turn_number % 2 == 0
        is_player1_turn: bool = is_even and player1.sign == "X" or not is_even and player1.sign == "O"
        player1.button.config(state=DISABLED if is_player1_turn else ACTIVE)
        player2.button.config(
            state=ACTIVE if is_player1_turn else DISABLED)
        game.sign_to_place('X' if is_even else "O", x, y)

        turn_number += 1  # move to next turn
        button[x][y].config(text=game.board[x][y])  # update button label
    # X wins
    if game.check_win("X"):
        window.destroy()
        messagebox.showinfo("Vítěz", "Hráč %s vyhrál" % player1.name)
    # O wins
    elif game.check_win("O"):
        window.destroy()
        messagebox.showinfo("Vítěz", "Hráč %s vyhrál" % player2.name)
    # Tie
    elif(game.check_full()):
        window.destroy()
        messagebox.showinfo("Remíza", "Remíza")


# Print the board
def print_gameboard(game_board):
    global button
    button = []
    for x in range(len(game.board)):
        row = 7+x
        button.append(x)
        button[x] = []
        for y in range(len(game.board)):
            column = y
            button[x].append(y)
            get_t = partial(get_text, x, y, game_board)
            button[x][y] = Button(
                game_board, bd=5, command=get_t, height=4, width=8)
            button[x][y].grid(row=row, column=column)


print_gameboard(window)

window.mainloop()
