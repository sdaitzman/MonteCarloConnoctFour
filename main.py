"""
connect 4 interface example

adapted from https://www3.nd.edu/~pbui/teaching/cdt.30010.fa16/project01.html

"""

import connect4
import time

# Globals

Players = (connect4.PIECE_ONE, connect4.PIECE_TWO)
Board   = connect4.Board()
Radius  = 40
Tries   = 0

# Game Loop
def start_game(board, player1, player2):
    Winner  = None
    while not Winner:
        turn = len(board.history)

        if turn % 2 == 0:
            print(board)
            print("player move")
            move = player1(board, Players)   # Player One
            print("player move is ", move, "history is ", board.history)
        else:
            move = player2(board, Players)  # Player Two
            print("bot move is ", move, "history is ", board.history)

        if board.drop_piece(move, Players[turn % 2]):
            Tries = 0
            board.history.append(move)

        if Tries > 3:
            print("Player", (turn % 2) + 1," is stuck!")
            break

        time.sleep(1)

        Winner = Board.find_winner()

        if Winner is not None:
            print(connect4.PIECE_COLOR_MAP[Winner])

    print("The Winner is the", connect4.PIECE_COLOR_MAP[Winner], "piece")

start_game(Board, connect4.HumanPlayer, connect4.RandomPlayer)
