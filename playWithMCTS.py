import connect4
from monteCarloPlayer import Node, MCTS

import time

# Globals

Players = (connect4.PIECE_ONE, connect4.PIECE_TWO)
Board   = connect4.Board()
Radius  = 40
Tries   = 0

#TODO Increase itermax
#TODO Store game tree to continually train AI
itermax = 100

def start_game(board):
    Winner  = None
    node = Node(board=board)
    while not Winner:
        print(board)
        turn = len(board.history)
        node.turn = turn % 2
        node.piece = node.pieces[node.turn]

        if turn % 2 == 0:
            print("player 1 move")
            # move = connect4.HumanPlayer(board, Players)  # Player Two
            node, move = MCTS(board, itermax, node)   # Player One
            print("player move is ", move, "history is ", board.history)

        else:
            print("player 2 move")
            # move = connect4.RandomPlayer(board, Players)  # Player Two
            node, move = MCTS(board, itermax, node)
            print("bot move is ", move, "history is ", board.history)

        if board.drop_piece(move, node.piece):
            Tries = 0
            board.history.append(move)

        if Tries > 3:
            print("Player", (turn % 2) + 1," is stuck!")
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

    print("The Winner is the", connect4.PIECE_COLOR_MAP[Winner], "piece")

# TODO: Run multiple simulations and see how many times MCTS wins against other
# players
if __name__ == "__main__":
    start_game(Board)
