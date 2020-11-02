import random
from modules.state import State


def env_from_file(filepath):
    """
    Returns the state action grid from a file.
    """

    reward_map = []

    with open(filepath) as inputfile:
        state_grid = [
            [state for state in filter(lambda x: x in ["*", ".", "#", "$"], list(line))]
            for line in inputfile
        ]

    for i in range(len(state_grid)):
        reward_line = []
        for j in range(len(state_grid[i])):
            char = state_grid[i][j]
            if(char == '.'):
                reward_line.append(-1)
            elif(char == '#'):
                reward_line.append(1)
            elif(char == '$'):
                reward_line.append(10)
            else:
                reward_line.append(-10)
        reward_map.append(reward_line)

    return reward_map, state_grid

