import connect4
from monteCarloPlayer import Node, MCTS

import time

# Globals

Players = (connect4.PIECE_ONE, connect4.PIECE_TWO)
Board   = connect4.Board()
Radius  = 40
Tries   = 0
player_type = ["Human", "Random", "MCTS"]

#TODO Increase itermax
#TODO Store game tree to continually train AI
itermax = 200

def start_game(board, player1, player2):
    Winner  = None
    node = Node(board=board)
    while not Winner:
        print(board)
        turn = len(board.history)
        node.turn = turn % 2
        node.piece = node.pieces[node.turn]

        if turn % 2 == 0:
            if player1 == player_type[0]:
                move = connect4.HumanPlayer(board, Players)  # Human Player
            elif player1 == player_type[1]:
                move = connect4.RandomPlayer(board, Players)  # Random Player
            else:
                node, move = MCTS(board, itermax, node)   # MCTS Player
            # print("player move is ", move, "history is ", board.history)

        else:
            if player2 == player_type[0]:
                move = connect4.HumanPlayer(board, Players)  # Human Player
            elif player2 == player_type[1]:
                move = connect4.RandomPlayer(board, Players)  # Random Player
            else:
                node, move = MCTS(board, itermax, node)   # Player One

        if board.drop_piece(move, node.piece):
            Tries = 0
            board.history.append(move)

        if Tries > 3:
            # print("Player", (turn % 2) + 1," is stuck!")
            break

        if node.child_nodes:
            for child_node in node.child_nodes:
                if move == child_node.move:
                    node = child_node
                    break
        else:
            node = Node(board=board)
        # time.sleep(1)

        Winner = Board.find_winner()

        if Winner is not None:
            print(connect4.PIECE_COLOR_MAP[Winner])

    # print("The Winner is the", connect4.PIECE_COLOR_MAP[Winner], "piece")

    return Players.index(Winner)

# TODO: Run multiple simulations and see how many times MCTS wins against other
# players
if __name__ == "__main__":
    winner = start_game(Board, "MCTS", "Human")
    print(winner)

    ### Uncomment to play several games against MCTS
    # games = 10
    # wins = 0
    # for game in range(games):
    #     Board = connect4.Board()
    #     winner = start_game(Board)
    #     print(winner)
    #     if winner == 1: # first player is 0, second is 1
    #         wins += 1
    #     percent_win = wins/300
    #     if game % 2 == 0:
    #         print("MCTS win rate against random player: {}%".format(percent_win))
