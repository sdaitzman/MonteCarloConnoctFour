---
title: "Home"
date: 2020-12-02
layout: "Layout"
---

# Monte Carlo Connect Four
Hi There!  

<SidePhoto>
<p>We implemented and tested a Monte Carlo Tree Search algorithm that can successfully play Connect Four against a human player or another simulation. <br> <br><br>In the process,  we trained our algorithm, built an alternative minimax simulated player, and compared their performance. In this website, we included our findings, research, and conclusions. Take a dive in the world of board game bots and connect four!</p>

<img src="./run.png" style="min-width: 50%;">

</SidePhoto>

### [Connect Four](connect-four/index.md)
Connect Four is a game in which two players take turns dropping colored pieces into a vertical grid.

The objective of the game is to create a sequence of four pieces in a row horizontally, vertically, or diagonally.

<HeroButton to="/connect-four">Connect Four Gameplay</HeroButton>

### [Monte Carlo Tree Search](mcts/index.md)
The Monte Carlo Tree Search algorithm determines the best move possible for our player given the results of many game situations.

Each node in the tree represents a unique game state.

For each potential move, the computer plays multiple simulation games, choosing random moves as necessary until a win/loss/draw is reached.

The algorithm then backpropagates up the tree, updating values at each node depending on the outcome.

The move with the best win rate is the move taken by the player.

<HeroButton to="/mcts">MCTS in Detail</HeroButton>

### [Minimax](minimax/index.md)
The Minimax Search Algorithm is a graph decision algorithm used, in this case, to offer move candidates for our connect four bot.

Its name comes from its goal to minimize the score of its opponent while maximizing the bot score at every move made.

In contrast to the MCTS, it doesn't play out the game tree entirely.

<HeroButton to="/minimax">Minimax in Detail</HeroButton>

### [performance](performance/index.md)
While our MCTS-based computer player will not be going pro anytime soon, we looked into analyzing what it would take to make our implementation a tough competitor.

<HeroButton to="/performance">More Performance Stats</HeroButton>

<!-- ### [discussion](discussion/index.md) -->

<!-- <HeroButton to="/discussion">Discussion in Depth</HeroButton> -->

### [bibliography](bibliography/index.md)

---
Made with ❤️ at Olin College. [source code](https://github.com/sdaitzman/MonteCarloConnoctFour)
