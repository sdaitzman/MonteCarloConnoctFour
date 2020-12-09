import connect4
from minimaxPlayer import Node, MiniMax

import time

# Globals

Players = (connect4.PIECE_ONE, connect4.PIECE_TWO)
Board   = connect4.Board()
Radius  = 40
Tries   = 0
player_type = ["Human", "Random", "MiniMax"]

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
                 move = MiniMax(board, node)   # MiniMax Player
        else:
            if player2 == player_type[0]:
                move = connect4.HumanPlayer(board, Players)  # Human Player
            elif player2 == player_type[1]:
                move = connect4.RandomPlayer(board, Players)  # Random Player
            else:
                move = MiniMax(board, node)   # Player One

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

    return Players.index(Winner)


if __name__ == "__main__":
    winner = start_game(Board, "Human", "MiniMax")
    print(winner)
