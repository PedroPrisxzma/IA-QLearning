import modules 

def env_from_file(filepath):
    """
    Returns the state action grid from a file.
    """

    reward_map = []

    with open(filepath) as inputfile:
        inputfile.readline()
        state_grid = [
            [state for state in filter(lambda x: x in ["*", ".", "#", "$"], list(line))]
            for line in inputfile
        ]

    for i in range(len(state_grid)):
        reward_line = []
        for j in range(len(state_grid[i])):
            char = state_grid[i][j]
            reward_line.append(getReward(char))
        reward_map.append(reward_line)

    return reward_map, state_grid

def steps_from_file(filepath):
    with open(filepath) as inputfile:
        first_line = list(inputfile.readline().split(" "))
    return int(first_line[2])

def getReward(character):
    if(character == '.'):
        return -1
    elif(character == '#'):
        return 1
    elif(character == '$'):
        return 10
    else:
        return -10
        