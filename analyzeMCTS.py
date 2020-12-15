'''
Scripts to generate related graphs for MCTS
'''

import timeit
import numpy as np
import connect4
from monteCarloPlayer import Node, MCTS
import matplotlib.pyplot as plt
from playWithMCTS import start_game

def get_MCTS_runtime(start, stop, increment):
    '''
    Returns plot of runtime for different itermax sizes.
    '''
    runtimes = []

    for itermax in range(start, stop, increment):
        board = connect4.Board()
        node = Node(board=board)
        turn = len(board.history)
        node.turn = turn % 2
        node.piece = node.pieces[node.turn]

        # node, move = MCTS(board, itermax, node)
        t = timeit.Timer('MCTS(board, itermax, node)', setup='from __main__ import MCTS', globals=locals())

        runtime = t.timeit(1)
        print("Runtime added")
        runtimes.append(runtime)

    #plot results
    plt.plot(range(start, stop, increment), runtimes, '.')
    plt.xlabel("Itermax Size")
    plt.ylabel("Runtime (seconds)")
    plt.title("MCTS Move Time by Itermax Value")
    fig = plt.gcf()
    fig.savefig("turn_MCTS_runtimes.png")
    plt.show()


def get_MCTS_winrate():
    '''
    Returns plot of winning percentage for different itermax sizes against a
    random player.
    '''
    winrate = []
    # number of games played in total=
    num_games = 50
    for itermax in range(start, stop, increment):
        wins = 0
        for game in range(num_games):
            Board = connect4.Board()

            winner = start_game(Board, ["MCTS", "Random"], itermax=itermax, print_winner=False)
            if winner == 0:
                wins += 1
        winrate.append(wins/num_games * 100)
    #plot results
    plt.plot(range(start, stop, increment), winrate, '.')
    plt.xlabel("Itermax Size")
    plt.ylabel("Win Percentage (%)")
    plt.title("MCTS Win Rate Against Random by Itermax Value")
    fig = plt.gcf()
    fig.savefig("MCTS_winrate.png")
    plt.show()

def train_MCTS(games_to_play, itermax):
    games = []
    winrate = []
    node = Node(board=connect4.Board())
    wins = 0
    for game in range(games_to_play):
        Board = connect4.Board()
        winner = start_game(Board, ["MCTS", "Random"], node=node, itermax=itermax, timeout=3600, print_winner=False)
        if winner == 0:
            wins += 1
        if game % 100 == 0:
            games.append(game+1)
            winrate.append(wins/(game+1))

    plt.plot(games, winrate, '.')
    plt.xlabel("Games Played")
    plt.ylabel("Win Percentage (%)")
    plt.title("MCTS Win Rate (Itermax {})".format(itermax))
    fig = plt.gcf()
    fig.savefig("MCTS_winrate_build.png")
    plt.show()

if __name__ == "__main__":
    # Uncomment functions to run analysis
    # get_MCTS_runtime(100, 1001, 100)
    # get_MCTS_winrate(25, 501, 25)
    train_MCTS(100000,100)
