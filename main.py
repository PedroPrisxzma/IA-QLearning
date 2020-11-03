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

printStates(finalStateDic, reward_map, state_grid, steps)
