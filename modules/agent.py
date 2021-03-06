import random
from modules.state import State
from modules.action import Actions


class Agent:
    def __init__(self, learning_rate, discount_factor, reward_map, state_grid, steps):
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.reward_map = reward_map
        self.state_grid = state_grid
        self.maxSteps = steps

    @staticmethod
    def choose_start(reward_map, state_grid, max_steps):
        x = random.randrange(0, len(reward_map))
        y = random.randrange(0, len(reward_map[x]))
        if reward_map[x][y] == -10:
            return Agent.choose_start(reward_map, state_grid, max_steps)
        else:
            return State(x, y, state_grid[x][y], max_steps)
    
    @staticmethod
    def epsilon_greedy_policy(epsilon, state):
        greedChance = random.random()
        if(greedChance < epsilon):
            return random.choice([Actions.LEFT, Actions.UP, Actions.RIGHT, Actions.DOWN])
        else:
            max_action = max(state.qvalues, key=state.qvalues.get)
            return max_action

    def take_action(self, state, action, stateDic):
        if action == Actions.UP and state.posX - 1 < 0:
            return (State(None, None, None, None), -10)
        if action == Actions.DOWN and state.posX + 1 >= len(self.reward_map):
            return (State(None, None, None, None), -10)
        if action == Actions.LEFT and state.posY - 1 < 0:
            return (State(None, None, None, None), -10)
        if action == Actions.RIGHT and state.posY + 1 >= len(
            self.reward_map[state.posX]
        ):
            return (State(None, None, None, None), -10)

        if action == Actions.UP:
            nextX = state.posX-1
            nextY = state.posY

        elif action == Actions.DOWN:
            nextX = state.posX+1
            nextY = state.posY 

        elif action == Actions.LEFT:
            nextX = state.posX
            nextY = state.posY-1 

        elif action == Actions.RIGHT:
            nextX = state.posX
            nextY = state.posY+1

        else:
            print("WARNING NO ACTION TAKEN!!")
            return (State(None, None, None, None), -10)


        next_char = self.state_grid[nextX][nextY]
        next_steps = self.maxSteps if next_char == '#' else state.steps-1

        if((nextX, nextY, next_steps) in stateDic.keys()):
            state = stateDic[(nextX, nextY, next_steps)] 
        else:
            state = State(nextX, nextY, next_char, next_steps)

        if(next_steps < 0):
            return (State(None, None, None, None), -10)
        return (state, self.reward_map[nextX][nextY])

        