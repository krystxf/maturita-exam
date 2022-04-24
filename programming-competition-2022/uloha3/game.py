#!/usr/bin/python

class Game:
    number_to_win: int = 5

    def __init__(self, board_size: int):
        if board_size < 3:
            print("Velikost hracího pole automaticky nastavena na 3")
            board_size = 3
        self.board = [[" " for x in range(board_size)]
                      for y in range(board_size)]

    def check_full(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == " ":
                    return False
        return True

    def sign_to_place(self, sign, x, y):
        self.board[x][y] = sign

    def check_win(self, sign):
        # check rows
        for i in range(len(self.board)):
            for j in range(4):
                if self.board[i][j] == sign and self.board[i][j + 1] == sign and self.board[i][j + 2] == sign and self.board[i][j + 3] == sign:
                    return True

        # check columns
        for i in range(4):
            for j in range(len(self.board)):
                if self.board[i][j] == sign and self.board[i + 1][j] == sign and self.board[i + 2][j] == sign and self.board[i + 3][j] == sign:
                    return True

        # check diagonals
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == sign and self.board[i + 1][j + 1] == sign and self.board[i + 2][j + 2] == sign and self.board[i + 3][j + 3] == sign:
                    return True

        for i in range(self.number_to_win):
            for j in range(3, len(self.board)):
                if self.board[i][j] == sign and self.board[i + 1][j - 1] == sign and self.board[i + 2][j - 2] == sign and self.board[i + 3][j - 3] == sign:
                    return True
