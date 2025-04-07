import math


class TakeStones:
    def __init__(self, n):
        # set stones and moves
        self.available_stones= set(range(1, n + 1))
        self.last_move= -1
        self.current_player= 1  # first player is 1

    def clone(self):
        # clone the game state
        clone_state= TakeStones(0)
        clone_state.available_stones= set(self.available_stones)
        clone_state.last_move= self.last_move
        clone_state.current_player= self.current_player
        return clone_state

    def apply_move(self, move):
        # remove stone and change turn
        self.available_stones.remove(move)
        self.last_move=move
        self.current_player= 2 if self.current_player== 1 else 1


def is_terminal(state):
    # check if game over (no legal moves)
    return len(get_legal_moves(state))== 0


def get_legal_moves(state: TakeStones):
    # return all valid moves
    legal_moves = []
    n = len(state.available_stones)* 2
    for stone in state.available_stones:
        if state.last_move== -1:
            if stone%2 !=0 and stone< n/2:
                legal_moves.append(stone)
        else:
            if stone%state.last_move== 0 or state.last_move% stone== 0:
                legal_moves.append(stone)
    return legal_moves


def evaluate(state):
    # return score if game over
    if is_terminal(state):
        return -1 if state.current_player== 1 else 1
    return 0


# track node evaluations
nodes_evaluated_with_pruning= 1  # start counting from 1
nodes_evaluated_without_pruning= 1  # start counting from 1
total_branches= 1  # start counting branches


def max_value(state, alpha, beta):
    # max function for minimax with pruning
    global nodes_evaluated_with_pruning, total_branches
    if is_terminal(state):
        return evaluate(state)

    v= -math.inf
    legal_moves= get_legal_moves(state)
    total_branches+= len(legal_moves)

    for move in legal_moves:
        next_state= state.clone()
        next_state.apply_move(move)
        v= max(v, min_value(next_state, alpha, beta))
        if v>=beta:
            nodes_evaluated_with_pruning +=1  # count pruned node
            return v  # prune the tree
        alpha = max(alpha, v)
        nodes_evaluated_with_pruning +=1  # count node
    return v


def min_value(state, alpha, beta):
    # min function for minimax with pruning
    global nodes_evaluated_with_pruning, nodes_evaluated_without_pruning, total_branches
    if is_terminal(state):
        return evaluate(state)

    v= math.inf
    legal_moves= get_legal_moves(state)
    total_branches +=len(legal_moves)

    for move in legal_moves:
        next_state= state.clone()
        next_state.apply_move(move)

        nodes_evaluated_without_pruning +=1  # count node without pruning
        value= max_value(next_state, alpha, beta)

        if value<=alpha:
            nodes_evaluated_with_pruning += 1  # count pruned node
            return value  # prune the tree

        v= min(v, value)
        beta= min(beta, v)

    return v


def find_best_move(state):
    # find the best move for max player
    best_move= None
    best_value= -math.inf
    alpha= -math.inf
    beta= math.inf

    for move in sorted(get_legal_moves(state)):
        next_state= state.clone()
        next_state.apply_move(move)
        move_value= min_value(next_state, alpha, beta)

        if move_value>best_value:
            best_value= move_value
            best_move= move

    return best_move, best_value


def calculate_average_branching_factor(total_branches, total_nodes):
    # calculate average branching factor and round down
    return math.floor(total_branches/ total_nodes *10) /10 if total_nodes > 0 else 0


def main():
    n= int(input("Enter the number of stones: "))
    initial_state= TakeStones(n)

    global nodes_evaluated_with_pruning, nodes_evaluated_without_pruning, total_branches
    nodes_evaluated_with_pruning= 1  # start from 1
    nodes_evaluated_without_pruning= 1  # start from 1
    total_branches= 1  # start from 1

    # Find the best move for the Max player
    best_move, best_value= find_best_move(initial_state)

    # Calculate the average branching factor based on branches and nodes evaluated without pruning
    average_branching_factor= calculate_average_branching_factor(total_branches, nodes_evaluated_without_pruning)

    # Print results
    print(f"average Branching Factor: {average_branching_factor:.1f}")
    print(f"best Move: {best_move}")
    print(f"score: {best_value}")
    print(f"nodes evaluated without pruning: {nodes_evaluated_without_pruning}")
    print(f"nodes evaluated with pruning: {nodes_evaluated_with_pruning}")


if __name__ == "__main__":
    main()