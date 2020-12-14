---
title: "Minimax"
date: 2020-12-02
layout: "Layout"
---

# Minimax

*Go [home](/).*

The Minimax Search Algorithm is a graph decision algorithm used, in this case, to offer move candidates for our Connect Four bot. Its name comes from its goal to *minimize* the score of its opponent while *maximizing* the bot score at every move made. In contrast to the MCTS algorithm, it doesn't play out the game tree entirely to a terminal state. Instead, we utilize both a variable depth and a heuristic that doesn't depend on whether a given branch results in a win.

## Variability

Since we don't explore game to their conclusion, we need to make a decision as designers about how deep the algorithm should search. As we increase the number of layers forward in the tree that the bot should search, it becomes more proficient. However, because each node (a game state) has seven children, the decision of how deep to evaluate the tree becomes extremely performance dependent.

## Heuristics

Because we don't know the outcome of each game branch, we have to use a variable heuristic to rank the value of particular branches. One option is to count how many less-than-four length piece streaks exist, ranking them by their length. For instance, we would rank a streak of three pieces very highly, while simultaneously ranking the opponent having a long streak negatively.

A simple heuristic might look like:

$$\text{rating} = \text{four streaks} \times 10000 + \text{three streaks} \times 1000 + \text{two streaks} \times 100 - \\ \text{opp two streaks} \times 10$$
