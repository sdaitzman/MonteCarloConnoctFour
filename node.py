import random
import numpy as np
import copy
import math

PIECE_ONE  = 'x'
PIECE_TWO  = 'o'


class Node:
    def __init__(self, move=None, board=None, parent_node=None):
        '''
        Node of MiniMax Tree
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
        Makes a move.

        Returns the child node with the highest value given the formula

        Function used most likely in MCTS scenario
        '''
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
        new_node.switch_turns(board)
        #mark node as visited
        self.new_moves.remove(move)
        # link node to tree
        self.child_nodes.append(new_node)

        return new_node

    def expand_tree_mm(self, move, board):
        '''
        Given a move not previously explored, create a child node to represent
        that move and return that new node. Also actually adjust the board for the minimax
        algorithm
        '''
        new_node = Node(move=move, board=board, parent_node=self)

        # adjust board history for move
        #if new_node.board.drop_piece_test(move, new_node.piece):
        new_node.board.drop_piece(move, new_node.piece)

        # switch to opponent's turn to continue the game
        new_node.board.turn ^= 1
        # new_node.switch_turns(new_node.board)
        new_node.turn = new_node.board.turn

        if new_node.piece == 'x':
            new_node.piece = 'o'
        else:
            new_node.piece = 'x'

        # link node to tree
        self.child_nodes.append(new_node)

        return new_node

    def expand_tree_silent(self, move, board):
        '''
        Given a move not previously explored, create a child node to represent
        that move and return that new node. Also actually adjust the board for the minimax
        algorithm
        '''
        
        new_node = Node(move=move, board=board, parent_node=self)

        new_node.turn = new_node.board.turn

        if new_node.piece == 'x':
            new_node.piece = 'o'
        else:
            new_node.piece = 'x'

        # adjust board history for move
        new_node.board.drop_piece(move, new_node.piece)

        # link node to tree
        self.child_nodes.append(new_node)

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

