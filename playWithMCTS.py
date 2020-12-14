#!/usr/bin/env python3
"""
Connect4 implementation code adapted from University of Notre Dame

https://www3.nd.edu/~pbui/teaching/cdt.30010.fa16/project01.html

"""
import connect4
from monteCarloPlayer import Node, MCTS

import time
import copy
import pickle

# Globals
Players = (connect4.PIECE_ONE, connect4.PIECE_TWO)
player_type = ["Human", "Random", "MCTS"]

# Next Steps:
# Increase itermax
# Store game tree to continually train AI

def start_game(board, player1, player2, node=None, itermax=100, print_winner=True, timeout=3600):
    '''
    Plays a game of Connect Four.
    Board: Board object
    player1, player2: "Human", "Random", or "MCTS" (defaults to MCTS)
    node: starting node
    itermax: number of simulations to run per turn
    print_winner: turn off if training or running multiple games, turn on to
                  see winner after every game
    timeout: parameter to cutoff iterations if too long. Defaults to 1 hour per
             turn.
    '''
    Winner = None
    # If playing multiple games, initialize the same starting node to build
    # upon the existing tree.
    if node == None:
        node = Node(board=board)
    while not Winner:
        # Determine player
        turn = len(board.history)
        node.turn = turn % 2
        node.piece = node.pieces[node.turn]

        # Handle different player types
        if turn % 2 == 0:
            if player1 == player_type[0]:
                print(board)
                move = connect4.HumanPlayer(board, Players)  # Human Player
            elif player1 == player_type[1]:
                move = connect4.RandomPlayer(board, Players)  # Random Player
            else:
                node, move = MCTS(board, itermax, node, timeout=timeout)   # MCTS Player

        else:
            if player2 == player_type[0]:
                print(board)
                move = connect4.HumanPlayer(board, Players)  # Human Player
            elif player2 == player_type[1]:
                move = connect4.RandomPlayer(board, Players)  # Random Player
            else:
                node, move = MCTS(board, itermax, node, timeout=timeout)   # Player One

        # If a valid move is returned, play it
        if move != None:
            if board.drop_piece(move, node.piece):
                board.history.append(move)

            if node.child_nodes:
                for child_node in node.child_nodes:
                    if move == child_node.move:
                        node = child_node
                        break
            else:
                node = Node(board=board)

        # Check for terminal state
        Winner = board.find_winner()

    # Print winner
    if print_winner:
        print("The Winner is the", Winner, "piece")
        print(node.board)
    return Players.index(Winner)


if __name__ == "__main__":
    Board   = connect4.Board()
    ## Play against MCTS
    print("Play game --------------")
    timeout = 600
    itermax = 500
    winner = start_game(Board, "MCTS", "Human", itermax=itermax, timeout=timeout)
