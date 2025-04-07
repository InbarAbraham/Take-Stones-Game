# Take-Stones-Game
Job Description:
---
The job is to implement the MiniMax algorithm with alpha-beta pruning for the game "Take-Stones". 
The goal of the algorithm is to calculate the optimal move for the first player (Max), while pruning unnecessary branches in the game tree to optimize the search and reduce the number of nodes calculated.

Implementation of the algorithm:
---
The algorithm is based on the functions max_value and min_value , with each function searching for the maximum or minimum value for the current player.
Each function performs recursion until it reaches a final state, that is, until it reaches a leaf, and then returns the value
of the victory or loss of the node.


The algorithm combines alpha-beta pruning to reduce the number of nodes explored:
• If a value is discovered that leads to a certain quantity being irrelevant, in case the value is already outside the alpha-beta range, the algorithm does not continue exploring this node and performs a "pruning".


Game structure:
---
• TakeStones – This class represents the state of the game including the available stones, the last move made, and the current player.

• Get_legal_moves – A function that returns all possible moves for the current player, according to the following rules:
    o At the beginning of the game, the player can choose odd stones less than n/2.
    o After the first move, a player can choose stones that are a multiple of the previous move or can be divided by it.

• Evaluate – A function that evaluates whether the game is over and if so who won, returning a value according to the final result.

• MaxValue and MinValue – Functions Recursions that calculate the optimal moves for the players Max and Min respectively, and incorporate Alpha-Beta intersection.

• Find_best_move – A function that performs the search for the best move for the first player (Max)

• Calculate_average_branching_factor – A function that calculates the average branching factor according to the number of branches and nodes examined.
