"""
Connect4 implementation code adapted from University of Notre Dame

https://www3.nd.edu/~pbui/teaching/cdt.30010.fa16/project01.html

"""

import random

# Game Constants

ROWS       = 6
COLUMNS    = 7

PIECE_NONE = ' '
PIECE_ONE  = 'x'
PIECE_TWO  = 'o'

PIECE_COLOR_MAP = {
    PIECE_NONE : "white",
    PIECE_ONE  : "black",
    PIECE_TWO  : "red",
}

DIRECTIONS = (
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
)

# Board Functions

class Board:
    def __init__(self, rows=ROWS, columns=COLUMNS):
        ''' Creates empty Connect 4 board '''
        self.board = []
        self.columns = columns
        self.rows = rows

        for row in range(self.rows):
            board_row = []
            for column in range(self.columns):
                board_row.append(PIECE_NONE)
            self.board.append(board_row)

    # Copy board
    def copy(self):
        ''' Return a copy of the board '''
        rows    = len(self.board)
        columns = len(self.board[0])
        copied  = self.deepcopy()

        return copied


    def __str__(self):
        ''' Prints Connect 4 board '''
        board_str = ""
        for row in self.board:
            board_str += str('|' + '|'.join(row) + '|' + '\n')
        return board_str


    def drop_piece(self, column, piece):
        ''' Attempts to drop specified piece into the board at the
        specified column

        If this succeeds, return True, otherwise return False.
        '''

        for row in reversed(self.board):
            if row[column] == PIECE_NONE:
                row[column] = piece
                return True

        return False

    def find_moves(self, piece):
        if self.find_winner():
            return []
        moves = []
        for column in self.columns:
            if self.drop_piece(column, piece):
                moves.append(column)
        return moves

    def find_winner(self, length=4):
        ''' Return whether or not the board has a winner '''

        rows    = len(self.board)
        columns = len(self.board[0])

        for row in range(rows):
            for column in range(columns):
                if self.board[row][column] == PIECE_NONE:
                    continue

                if self.check_piece(row, column, length):
                    return self.board[row][column]

        return None


    def check_piece(self, row, column, length):
        ''' Return whether or not there is a winning sequence starting from
        this piece
        '''
        rows    = len(self.board)
        columns = len(self.board[0])

        for dr, dc in DIRECTIONS:
            found_winner = True

            for i in range(1, length):
                r = row + dr*i
                c = column + dc*i

                if r not in range(rows) or c not in range(columns):
                    found_winner = False
                    break

                if self.board[r][c] != self.board[row][column]:
                    found_winner = False
                    break

            if found_winner:
                return True

        return False


def HumanPlayer(board, history, players):
    ''' Read move from human player '''
    columns = len(board.board[0])
    column  = -1

    while column not in range(0, columns):
        column = int(input('Which column? '))
        print("you input ", column)
    return column


def RandomPlayer(board, history, players):
    ''' Randomly select a column '''
    columns = len(board.board[0])
    return random.randint(0, columns - 1)
