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


def create_board(rows=ROWS, columns=COLUMNS):
    """ Creates empty Connect 4 board """
    board = []

    for row in range(rows):
        board_row = []
        for column in range(columns):
            board_row.append(PIECE_NONE)
        board.append(board_row)

    return board


def copy_board(board):
    """ Return a copy of the board """
    rows    = len(board)
    columns = len(board[0])
    copied  = create_board(rows, columns)

    for row in range(rows):
        for column in range(columns):
            copied[row][column] = board[row][column]
    return copied


def print_board(board):
    """ Prints Connect 4 board """
    for row in board:
        print('|' + '|'.join(row) + '|')


def drop_piece(board, column, piece):
    """ Attempts to drop specified piece into the board at the
    specified column

    If this succeeds, return True, otherwise return False.
    """

    for row in reversed(board):
        if row[column] == PIECE_NONE:
            row[column] = piece
            return True

    return False


def find_winner(board, length=4):
    ''' Return whether or not the board has a winner '''

    rows    = len(board)
    columns = len(board[0])

    for row in range(rows):
        for column in range(columns):
            if board[row][column] == PIECE_NONE:
                continue

            if check_piece(board, row, column, length):
                return board[row][column]

    return None


def check_piece(board, row, column, length):
    """ Return whether or not there is a winning sequence starting from
    this piece
    """
    rows    = len(board)
    columns = len(board[0])

    for dr, dc in DIRECTIONS:
        found_winner = True

        for i in range(1, length):
            r = row + dr*i
            c = column + dc*i

            if r not in range(rows) or c not in range(columns):
                found_winner = False
                break

            if board[r][c] != board[row][column]:
                found_winner = False
                break

        if found_winner:
            return True

    return False


def HumanPlayer(board, history, players):
    """ Read move from human player """
    columns = len(board[0])
    column  = -1

    while column not in range(0, columns):
        column = int(input('Which column? '))
        print("you input ", column)
    return column


def RandomPlayer(board, history, players):
    """ Randomly select a column """
    columns = len(board[0])
    return random.randint(0, columns - 1)
