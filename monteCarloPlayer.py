# Monte Carlo Tree Search trained AI

import random
import numpy as np
import copy
PIECE_ONE  = 'x'
PIECE_TWO  = 'o'

class Node:
    def __init__(self, move=None, board=None, parent_node=None):
        '''
        Node of MCTS Tree
        board: Board object
        turn: player 0 or player 1
        piece: game piece (x or o)
        child_nodes: all possible moves
        new_moves: moves that haven't been explored yet
        parent_node: previous turn
        wins: number of wins that have occurred through this node
        visits: number of times this node has been visited
        '''
        self.pieces = ['x','o']
        self.board = copy.deepcopy(board)
        self.turn = board.turn
        self.piece = self.pieces[self.turn]
        self.move = move
        self.child_nodes = []
        self.new_moves = board.find_moves(self.piece)
        self.parent_node = parent_node
        self.wins = 0
        self.visits = 0

    def make_move(self):
        '''
        Makes a move based on both exploration and exploitation.
        algorithm from https://repl.it/@NameChris96/Connect4AIMCTS#main.property
        Returns the child node with the highest value given the formula
        wins/visits + sqrt(2*log(visits)/(child_node visits))
        '''
        # TODO: Experiment with this
        foo = lambda x: x.wins/x.visits + np.sqrt(2*np.log(self.visits)/x.visits)
        return sorted(self.child_nodes, key=foo)[-1]

    def expand_tree(self, move, board):
        '''
        Given a move not previously explored, create a child node to represent
        that move and return that new node.
        '''
        board = copy.deepcopy(board)
        new_node = Node(move=move, board=board, parent_node=self)
        # switch to opponent's turn to continue the game
        new_node.board.turn ^= 1
        new_node.switch_turns()
        #mark node as visited
        self.new_moves.remove(move)
        # link node to tree
        self.child_nodes.append(new_node)

        return new_node

    def update(self, isWin):
        '''
        Backpropogation after a game has finished
        '''
        if isWin:
            self.wins += 1
        self.visits += 1

    def switch_turns(self, board=None):
        '''
        Changes player turn for game tree
        '''
        if board:
            self.turn = board.turn
        else:
            self.turn = self.board.turn
        self.piece = self.pieces[self.turn]


def MCTS(curr_board, itermax, curr_node=None):
    '''
    Builds the game tree and trains the computer
    '''

    if curr_node != None:
        root = curr_node
        if root.child_nodes == [] and root.new_moves == []:
            root.new_moves = root.board.find_moves(root.piece)
        # root.board = curr_board
        # root.new_moves = root.board.find_moves(root.piece)
    else:
        root = Node(board=curr_board)
        # print(node.piece)
    counter = 0
    for i in range(itermax):

        # Run simulation games itermax times, starting at the current position
        # in the game (root)
        node = root
        board = copy.deepcopy(curr_board)
        # We are at a node that has all paths explored and not a W/L/D state
        while node.new_moves == [] and node.child_nodes != []:
            # print("old node")
            dropped_piece = node.piece
            node = node.make_move()
            board.drop_piece(node.move, dropped_piece)
            board.history.append(node.move)
            node.switch_turns(board)
            # print(board)

        # Explore moves that haven't been explored yet
        if node.new_moves != []:
            # print("new node")
            move = random.choice(node.new_moves)
            board.drop_piece(move, node.piece)
            board.history.append(move)
            node = node.expand_tree(move, board)
            node.switch_turns(board)
            # print(board)
        # continue to explore while there are available moves
        while board.find_moves(node.piece):
            # print("explore")
            move = random.choice(board.find_moves(node.piece))
            board.drop_piece(move, node.piece)
            board.history.append(move)
            node.switch_turns(board)
        print(board)
        # There are no available moves so a terminal state has been reached
        # Backpropogation
        winning_piece = board.find_winner()
        # print("Game over; winner is", winning_piece)
        while node is not None:
            if winning_piece == node.piece:
                isWin = True
            else:
                isWin = False
            node.update(isWin)
            node = node.parent_node

    # Choose best move based on winning percentages
    foo = lambda x: x.wins/x.visits
    # print("Child Nodes:")
    # for child in root.child_nodes:
    #     print(child.move)
    sorted_child_nodes = sorted(root.child_nodes, key=foo)[::-1]

    # print winning percentages of each valid move
    # print("AI\'s computed winning percentages")
    # for node in sorted_child_nodes:
    #     print('Move: %s    Win Rate: %.2f%%' % (node.move+1, 100*node.wins/node.visits))
    # print('Simulations performed: %s\n' % i)

    # return original state of board and best move
    if sorted_child_nodes == []:
        return root, None
    return root, sorted_child_nodes[0].move
