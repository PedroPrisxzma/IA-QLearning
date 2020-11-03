import sys
import random
from modules import *

entry_file = sys.argv[1]
learning_rate = float(sys.argv[2])
epsilon = float(sys.argv[3])
discount_factor = float(sys.argv[4])
epochs = int(sys.argv[5])


reward_map, state_grid = env_from_file(entry_file)
steps = steps_from_file(entry_file)

finalStateDic = qLearning(learning_rate, discount_factor, epsilon, reward_map, state_grid, 
                            steps, epochs)

print('Done')
# Print saida

# def printStates(stateDic, rewardMap, steps):
#     for(x in rows of rewardMap):
#         for(y in cols of rewardMap):
#             for(s in range(0, steps)):
#                 if((x,y,s) in stateDic.keys())
#                     printState(stateDic[(x,y,s)])

#                 else
#                     print((x, y, s), 'LEFT', 1)

# def printState(state):
#     maxValue = max(state.qvalues, key=state.qvalues.get())

#     print((state.posX, state.posY, state.steps), maxValue, maxValue)
