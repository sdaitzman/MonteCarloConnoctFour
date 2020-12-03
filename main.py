"""
connect 4 interface example

adapted from https://www3.nd.edu/~pbui/teaching/cdt.30010.fa16/project01.html

"""

import connect4
import time

# Globals

Players = (connect4.PIECE_ONE, connect4.PIECE_TWO)
History = []
Board   = connect4.Board()
Radius  = 40
Winner  = None
Tries   = 0

# Game Loop

while not Winner:
    print(Board)
    turn = len(History)

    if turn % 2 == 0:
        print("player move")
        move = connect4.HumanPlayer(Board, History, Players)   # Player One
        print("player move is ", move, "history is ", History)
    else:
        move = connect4.RandomPlayer(Board, History, Players)  # Player Two
        print("bot move is ", move, "history is ", History)

    if Board.drop_piece(move, Players[turn % 2]):
        Tries = 0
        History.append(move)

    if Tries > 3:
        print('Player {} is stuck!').format((turn % 2) + 1)
        break

    # time.sleep(1)

    Winner = Board.find_winner()

    if Winner is not None:
        print(connect4.PIECE_COLOR_MAP[Winner])

print("The Winner is the", connect4.PIECE_COLOR_MAP[Winner], "piece")
