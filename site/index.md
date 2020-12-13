---
title: "Home"
date: 2020-12-02
layout: "Layout"
---

# Monte Carlo Connect Four
Hi There!  

<SidePhoto>
We implemented and tested a Monte Carlo Tree Search algorithm that can successfully play Connect Four against a human player or another simulation. In the process,  we trained our algorithm, built an alternative minimax simulated player, and compared their performance. In this website, we included our findings, research, and conclusions. Take a dive in the world of board game bots and connect four!

<img src="./run.png" style="min-width: 50%;">

</SidePhoto>

### [Connect Four](connect-four/index.md)
 The Monte Carlo Tree Search algorithm determines the best move possible for our player given the results of many game situations. Each node in the tree represents a unique game state. For each potential move, the game plays multiple games, choosing random moves until a win/loss/draw is reached. The algorithm then backpropagates up the tree, updating values at each node depending on the outcome. The move to take on that turn is the one with the best win rate based on simulations.

<HeroButton to="/connect-four">Connect Four</HeroButton>

### [MCTS](mcts/index.md)
The Monte Carlo Tree Search algorithm determines the vest move possible for our player given the results of many game situations. Each node in the tree represents a unique game state. For each potential move, the game plays multiple games, choosing random moves until a win/loss/draw is reached. The algorithm then backpropagates up the tree, updating values at each node depending on the outcome. The move to take on that turn is the one with the best win rate based on simulations.

<HeroButton to="/mcts">MCTS</HeroButton>

### [Minimax](minimax/index.md)
The Minimax Search Algorithm is a graph decision algorithm used, in this case, to offer move candidates for our connect four bot. Its name comes from its goal to minimize the score of its opponent while maximizing the bot score at every move made. In contrast to the MCTS, it doesn't play out the game tree entirely. 

<HeroButton to="/minimax">Minimax</HeroButton>

### Heuristics
#### MCTS

#### Minimax
In the minimax technique, game trees aren't typically played out in their entirety. As such, we only explore a few layers, the amount of which we can adjust according to how proficient we want the bot to be. Because we don't know the outcome of each game branch, we have to use a variable heuristic to rank the value of particular branches. One option is to count how many less-than-four length piece streaks exist, ranking them by their length.

### [performance](performance/index.md)

<HeroButton to="/performance">Performance</HeroButton>

### [discussion](discussion/index.md)

<HeroButton to="/discussion">Discussion</HeroButton>

### [bibliography](bibliography/index.md)

---
Made with ❤️ at Olin College. [source code](https://github.com/sdaitzman/MonteCarloConnoctFour)
