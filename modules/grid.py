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
        return +1
    elif(character == '$'):
        return 10
    else:
        return -10


def printStates(stateDic, rewardMap, stateGrid, steps):
    for x in range(0, len(rewardMap)):

        for y in range(0, len(rewardMap[0])):
        
            for s in range(0, steps+1):
                if ((x,y,s) in stateDic.keys() and stateGrid[x][y] != '$'):
                    printState(stateDic[(x,y,s)])
                
                else:
                    if(stateGrid[x][y] != '#' and stateGrid[x][y] != '*' and stateGrid[x][y] != '$'):
                        print((x, y, s), 'UP', 0)

def printState(state):
    maxValue = max(state.qvalues, key=state.qvalues.get)
    print((state.posX, state.posY, state.steps), stringAction(maxValue), round(state.qvalues[maxValue], 2))

def stringAction(number):
    if(number == 0):
        return "UP"
    elif(number == 1):
        return "RIGHT"
    elif(number == 2):
        return "DOWN"
    elif(number == 3):
        return "LEFT"
    else:
        return "invalid"