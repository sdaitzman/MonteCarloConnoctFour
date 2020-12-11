"""
Connect4 implementation code adapted from University of Notre Dame

https://www3.nd.edu/~pbui/teaching/cdt.30010.fa16/project01.html

"""

import random
import copy

# Game Constants

# default board size
ROWS       = 6
COLUMNS    = 7

# piece types for showing on the board
PIECE_NONE = ' '
PIECE_ONE  = 'x'
PIECE_TWO  = 'o'

# piece types for declaring who won
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

class Board:
    def __init__(self, rows=ROWS, columns=COLUMNS):
        '''
        Creates empty Connect 4 board

        rows: the 0-indexed number of rows to play with
        columns: the 0-indexed number of columns to play with
        '''
        self.board = []
        self.columns = columns
        self.rows = rows
        self.history = []
        self.turn = 0

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

        # print the column index to help guide player
        board_str += " 0 1 2 3 4 5 6\n"

        # print board, including the pieces which have been placed
        for row in self.board:
            board_str += str('|' + '|'.join(row) + '|' + '\n')
        return board_str


    def drop_piece(self, column, piece):
        ''' Attempts to drop specified piece into the board at the
        specified column

        If this succeeds, return True, otherwise return False.

        column: int index of column to place piece in
        piece: o or x, representing which player to place for
        '''

        for row in reversed(self.board):
            if row[column] == PIECE_NONE:
                row[column] = piece
                self.turn ^= 1
                return True

        return False

    def drop_piece_test(self, column, piece):
        ''' Check if it possible to place a piece in a given column.

        If is a valid move, return True, otherwise return False.

        column: int index of column to place piece in
        piece: o or x, representing which player to place for
        '''

        for row in reversed(self.board):
            if row[column] == PIECE_NONE:
                return True

        return False

    def find_moves(self, piece):
        '''
        Make a list of valid column indices for a piece given the
        current game state

        returns: list of columns, which are int indices of column to place piece in
        piece: o or x, representing which player to place for
        '''

        if self.find_winner():
            return []
        moves = []
        for column in range(self.columns):
            test_board = copy.deepcopy(self)
            if test_board.drop_piece(column, piece):
                moves.append(column)
        return moves

    def find_winner(self, length=4):
        '''
        Return whether or not the board has a winner for a given
        streak length

        length: how long of a streak of pieces to look for (default 4)
        '''

        rows    = self.rows
        columns = self.columns

        for row in range(rows):
            for column in range(columns):
                if self.board[row][column] == PIECE_NONE:
                    continue

                if self.check_piece(row, column, length):
                    return self.board[row][column]

        return None

    def find_winner_multiple(self, piece, length):
        '''
        Return how many wins of a given lenth a given piece has.

        length: how long of a streak of pieces to look for (default 4)
        piece: which player, x or o

        returns: list of placed piece coordinates which are associated with
                 a win of the given length. There can be multiple wins in this
                 abstraction :P
        '''
        wins = []

        rows    = len(self.board)
        columns = len(self.board[0])

        for row in range(rows):
            for column in range(columns):
                if self.board[row][column] == PIECE_NONE:
                    continue

                # if self.check_piece(row, column, length):
                #     # TODO remove duplicates
                #     # i.e if a piece has been involved in a piece do not consider it again
                #     # in the count.
                #     if self.board[row][column] == piece:
                #         wins.append(self.board[row][column])

                # if there are any streaks of the chosen length
                if self.check_piece_multiple(row, column, length, piece) > 0:
                    wins.append[self.board[row][column]]
        return wins

    def check_piece_multiple(self, row, column, length, piece):
        '''
        Return whether or not there is a winning sequence starting from this
        piece.

        row: index of row to check
        column: index of column to check
        length: how long of a streak to look for

        returns:
        '''
        rows = len(self.board)
        columns = len(self.board[0])
        count = 0

        # check all directions from given piece coordinate
        for dr, dc in DIRECTIONS:
            found_winner = True
            # check for streaks of given length
            for i in range(1, length):
                r = row + dr*i
                c = column + dc*i

                if r not in range(rows) or c not in range(columns):
                    # no streak of length
                    found_winner = False
                    break

                if self.board[r][c] != self.board[row][column]:
                    # no streak of length
                    found_winner = False
                    break

                if self.board[row][column] != piece:
                    found_winner = False
                    break

            if found_winner:
                count += 1

    def check_piece(self, row, column, length):
        '''
        Return whether or not there is a winning sequence starting from
        this piece.

        column: index of column to check
        row: index of row to check
        length: how long of a streak to look for
        '''

        rows    = self.rows
        columns = self.columns

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


def HumanPlayer(board, players):
    '''
    Read move from human player

    board: Board object
    players: tuple of player characters, i.e. (x, o)
    '''

    columns = len(board.board[0])
    column  = -1

    while column not in range(0, columns):
        column = int(input('Which column? '))
        print("you input ", column)
    return column


def RandomPlayer(board, players):
    '''
    Randomly select a column

    board: Board object
    players: tuple of player characters, i.e. (x, o)
    '''

    columns = len(board.board[0])
    return random.randint(0, columns - 1)
