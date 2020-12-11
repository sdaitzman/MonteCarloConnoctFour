#!/usr/bin/env python3
import connect4
from monteCarloPlayer import Node, MCTS

import time
import copy
import pickle
# Globals

Players = (connect4.PIECE_ONE, connect4.PIECE_TWO)
Board   = connect4.Board()
Radius  = 40
Tries   = 0
player_type = ["Human", "Random", "MCTS"]

#TODO Increase itermax
#TODO Store game tree to continually train AI
itermax = 200

def start_game(board, player1, player2, itermax=100, build_tree=False, db=None):
    Tries   = 0
    Winner = None
    node = Node(board=board)
    if db:
        if len(db) >= 2:
            node = db[1]
    elif build_tree and db != None and node not in db:
        db.append(node)
        print("Added board")
        print(db[1].board)
    while not Winner:
        turn = len(board.history)
        node.turn = turn % 2
        node.piece = node.pieces[node.turn]

        if turn % 2 == 0:
            if player1 == player_type[0]:
                print(board)
                move = connect4.HumanPlayer(board, Players)  # Human Player
            elif player1 == player_type[1]:
                move = connect4.RandomPlayer(board, Players)  # Random Player
            else:
                node, move = MCTS(board, itermax, node, build_tree=build_tree, db=db)   # MCTS Player
            # print("player move is ", move, "history is ", board.history)

        else:
            if player2 == player_type[0]:
                print(board)
                move = connect4.HumanPlayer(board, Players)  # Human Player
            elif player2 == player_type[1]:
                move = connect4.RandomPlayer(board, Players)  # Random Player
            else:
                node, move = MCTS(board, itermax, node, build_tree=build_tree, db=db)   # Player One

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

            if build_tree and db != [] and node not in db:
                db.append(node)

        Winner = board.find_winner()

        # if Winner is not None:
        #     print(connect4.PIECE_COLOR_MAP[Winner])

    if not build_tree:
        print("The Winner is the", Winner, "piece")

    return Players.index(Winner)

# TODO: Run multiple simulations and see how many times MCTS wins against other
# players
if __name__ == "__main__":
    # winner = start_game(Board, "MCTS", "Human", itermax=1000)
    # print(winner)

    ## Uncomment to play several games against MCTS
    # games = 100
    # wins = 0
    # for game in range(games):
    #     Board = connect4.Board()
    #     winner = start_game(Board, "Random", "MCTS", itermax=100)
    #     #print("Winner is player", winner + 1)
    #     if winner == 1: # first player is 0, second is 1
    #         wins += 1
    #     percent_win = wins/(game+1) * 100
    #     if game % 2 == 1:
    #         print("MCTS win rate against random player: {}%".format(percent_win))

    ## Play against MCTS
    dbfile = open('tree_MCTS','rb')
    db = pickle.load(dbfile)
    print(db[1].board)
    print("Play game --------------")
    winner = start_game(Board, "Human", "MCTS", itermax=100, db=None)
