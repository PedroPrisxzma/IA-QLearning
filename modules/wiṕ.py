from abc import ABC

class Actions(ABC):
    """
    Enum holding the possible actions the Agent can take at any state.
    """
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


def env_from_file(filepath):
    """
    Returns the state action grid from a file. 
    """
    action_state_map = []
    state_dict = {}
    
    with open(filepath) as inputfile:
        state_grid = [[state for state in filter(lambda x: x not in ["\n", " "], list(line))] for line in inputfile]
    
    # These for loops build the action state map, the order in witch the condition are verified matter,
    # keep that in mind.
    for i in range(len(state_grid)):
        for j in range(len(state_grid[i])):
                state = []
                # UP
                if i-1 > 0 and state_grid[i-1][j] == ".":
                    state.append(-1)
                elif i-1 > 0 and state_grid[i-1][j] == "#":
                    state.append(1)
                elif i-1 > 0 and state_grid[i-1][j] == "$":
                    state.append(10)
                else:
                    state.append(-10)
                #RIGHT
                if j+1 > len(state_grid[i]) and state_grid[i][j+1] == ".":
                    state.append(-1)
                elif j+1 > len(state_grid[i]) and state_grid[i][j+1] == "#":
                    state.append(1)
                elif j+1 > len(state_grid[i]) and state_grid[i][j+1] == "$":
                    state.append(10)
                else:
                    state.append(-10)
                #DOWN
                if i+1 > len(state_grid) and state_grid[i+1][j] == ".":
                    state.append(-1)
                elif i+1 > len(state_grid) and state_grid[i+1][j] == "#":
                    state.append(1)
                elif i+1 > len(state_grid) and state_grid[i+1][j] == "$":
                    state.append(10)
                else:
                    state.append(-10)
                #LEFT
                if j-1 > 0 and state_grid[i][j-1] == ".":
                    state.append(-1)
                elif j-1 > 0 and state_grid[i][j-1] == "#":
                    state.append(1)
                elif j-1 > 0 and state_grid[i][j-1] == "$":
                    state.append(10)
                else:
                    state.append(-10)
                
                state_dict[len(action_state_map)] = (i ,j, state_grid[i][j])
                action_state_map.append(state)
    
    return action_state_map, state_dict

