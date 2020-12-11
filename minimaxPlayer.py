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
        new_node.switch_turns()

        # mark node as visited
        self.new_moves.remove(move)

        # link node to tree
        self.child_nodes.append(new_node)

        return new_node

    def expand_tree_silent(self, move, board):
        '''
        Given a move not previously explored, create a child node to represent
        that move and DONT return that new node. It only exists in the child link.
        '''

        board = copy.deepcopy(board)
        new_node = Node(move=move, board=board, parent_node=self)

        # switch to opponent's turn to continue the game
        new_node.board.turn ^= 1
        new_node.switch_turns()

        # mark node as visited
        # TODO will this be a bug in the Minimax alg?
        self.new_moves.remove(move)

        # link node to tree
        self.child_nodes.append(new_node)

    def update(self, isWin):
        '''
        Backpropogation after a game has finished
        '''
        if isWin:
            self.wins += 1
        self.visits += 1

    def switch_turns(self):
        '''
        Changes player turn for game tree
        '''
        self.turn = self.board.turn
        self.piece = self.pieces[self.turn]


def MiniMax(current_board, current_node=None):
    '''
    builds a game tree and picks moves with the minimax algorithm from the current point
    in the connect four game.

    current_board: the board object, at the current point in the game
    '''

    # how far the minimax alg will search down the game tree
    search_depth = 3

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
        temp_node = root.expand_tree(move, root.board)

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

    # return best_move, best_rating
    return best_move


def mini_max_search(depth_target, current_node):
    '''
    recursive algorithm to build game tree for a given depth limit.

    depth_target: int, how far to search from the current node in the game tree
    board: board object
    current_player: string, x or o, determining who's turn it is
    '''


    # get all the valid moves
    # (children of current board state)
    potential_moves = current_node.new_moves

    # create children of the point node (given board state)
    for move in potential_moves:
        # make a new node with the given move
        # and flip the turn toggle
        current_node.expand_tree_silent(move, current_node.board)

    # check if it's a terminal (root or full board or game over) state
    # if terminal, evaluate heuristic at point
    # todo check for win/draw/loss at this point
    if depth_target == 0 or len(potential_moves) == 0:
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

    board: the board state
    opponent: the piece to consider
    '''

    opponent_piece = current_node.pieces[current_node.turn ^ 1]

    # how many 4's in a row there are in the board for the good piece
    pos_fours = current_node.board.find_winner_multiple(current_node.piece, 4)

    # how many 3's in a row there are in the board for the good piece
    pos_threes = current_node.board.find_winner_multiple(current_node.piece, 3)

    # good 2's in a row
    pos_twos = current_node.board.find_winner_multiple(current_node.piece, 2)

    # opponent 4's (super bad!)
    neg_fours = current_node.board.find_winner_multiple(opponent_piece, 2)

    # opponent 3's?
    neg_threes = current_node.board.find_winner_multiple(opponent_piece, 2)


    if len(neg_fours) >= 1:
        # dont make a move in which the opponent wins!
        rating =  -100000
    else:
        rating =  len(pos_fours)*100000 + len(pos_threes) * 100 + len(pos_twos) * 10 - len(neg_threes) * 10

    return rating
