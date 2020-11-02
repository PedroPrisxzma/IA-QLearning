import random
from modules.state import State


def epsilon_greedy_policy(epsilon, state):
    action_probabilities = [1.0, 1.0, 1.0, 1.0] * (epsilon / 4)
    best_action = max(state.qvalues.values())
    action_probabilities[best_action] += (1.0 - epsilon)
    return action_probabilities


def choose_start(state_map):
    x = random.randrange(0, len(state_map))
    y = random.randrange(0, len(state_map[x]))
    if state_map[x][y].is_terminal:
        choose_start(state_map)
    else:
        return state_map[x][y]


def env_from_file(filepath):
    """
    Returns the state action grid from a file.
    """

    state_map = []

    with open(filepath) as inputfile:
        state_grid = [
            [state for state in filter(lambda x: x in ["*", ".", "#", "$"], list(line))]
            for line in inputfile
        ]

    for i in range(len(state_grid)):
        state_line = []
        for j in range(len(state_grid[i])):
            state_line.append(State(i,j,state_grid[i][j]))
        state_map.append(state_line)

    return state_map

