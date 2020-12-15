"""
Implementation of the Minimax algorithm for connect four. Works interlocked with
the playWithMiniMax.py and connect4.py
"""

import random
import numpy as np
import copy
import math
from node import Node

# the two character representations
PIECE_ONE  = 'x'
PIECE_TWO  = 'o'

def MiniMax(current_board, current_node=None):
    '''
    builds a game tree and picks moves with the minimax algorithm from the current point
    in the connect four game.

    current_board: the board object, at the current point in the game
    current_node: move to work from.
    '''

    # how far the minimax alg will search down the game tree
    search_depth = 4

    # if we're given a game in progress
    if current_node != None:
        root = current_node
        root.board = current_board
        root.new_moves = root.board.find_moves(root.piece)
    else:
        # if the game board is brand new and we want to make a decision
        # from scatch
        # TODO: when does this case actually happen?)
        root = Node(board=current_board)

    # evaluate possible next moves, making sure to only think
    # about the valid ones (not resulting in overfull board, etc)
    ratedMoves = {} # move to val map

    for move in root.new_moves:
        # make a new node with the given move
        # and flip the turn toggle
        temp_node = root.expand_tree_mm(move, root.board)
        # evaluate moves with the recursive game tree explorer
        ratedMoves[move] = -mini_max_search(search_depth - 1, temp_node)

    # make a "lowest possible" value
    best_rating = -math.inf

    best_move = None
    moves = ratedMoves.items()
    for move, rating in moves:
        if rating >= best_rating:
            best_rating = rating
            best_move = move

    # print(moves)
    # print(best_move, best_rating)

    return best_move


def mini_max_search(depth_target, current_node):
    '''
    recursive algorithm to build game tree for a given depth limit.

    depth_target: int, how far to search from the current node in the game tree
    current_node: object representing the current board state
    '''

    # get all the valid moves
    # (children of current board state)
    potential_moves = current_node.new_moves

    # create children of the point node (given board state)
    for move in potential_moves:
        # make a new node with the given move
        # and flip the turn toggle
        current_node.expand_tree_silent(move, current_node.board)

        print(current_node.board)

    # if depth_target == 3:
    #     print(current_node.child_nodes[0].piece, current_node.child_nodes[0].turn, current_node.child_nodes[0].parent_node.turn)

    # check if it's a terminal (root or full board or game over) state
    # if terminal, evaluate heuristic at point
    # todo check for win/draw/loss at this point
    if depth_target == 0 or len(potential_moves) == 0 or current_node.board.find_winner():
        # do the heuristic here at the recursive base
        return rating_eval(current_node)

    rating = -math.inf

    # recurse on all children, reducing target depth
    # return best rating of the child
    for child in current_node.child_nodes:
        if child == None:
            print("Looks like we reached terminal state, no children game states left!")

        rating = max(rating, -mini_max_search(depth_target - 1, child))

    return rating

def rating_eval(current_node):
    '''
    the heuristic function.

    current_node: Node object
    '''

    # alias for the character of the opponent ('x' or 'o')
    opponent_piece = current_node.pieces[current_node.turn ^ 1]

    # how many 4's in a row there are in the board for the good piece
    pos_fours = current_node.board.find_winner_multiple(current_node.piece, 4)

    # how many 3's in a row there are in the board for the good piece
    pos_threes = current_node.board.find_winner_multiple(current_node.piece, 3)

    # good 2's in a row
    pos_twos = current_node.board.find_winner_multiple(current_node.piece, 2)

    # opponent 4's (super bad!)
    neg_fours = current_node.board.find_winner_multiple(opponent_piece, 4)

    # opponent 3's (still not good)
    neg_threes = current_node.board.find_winner_multiple(opponent_piece, 3)

    # opponent 2's (moderately bad)
    neg_twos = current_node.board.find_winner_multiple(opponent_piece, 2)

    if neg_fours >= 1:
        # dont make a move in which the opponent wins!
        rating =  -99999
    else:
        # assemble the ratings into a single quantity
        rating =  pos_fours*-99999 + pos_threes * 999 + pos_twos * 9 - neg_threes * 99 - neg_twos * 9

    return rating
