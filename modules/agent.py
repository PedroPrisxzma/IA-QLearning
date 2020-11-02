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
            Agent.choose_start(reward_map)
        else:
            return State(x, y, state_grid[x][y], max_steps)
    
    @staticmethod
    def epsilon_greedy_policy(epsilon, state):
        action_probabilities = [1.0, 1.0, 1.0, 1.0] * (epsilon / 4)
        best_action = max(state.qvalues, key=state.qvalues.get)
        action_probabilities[best_action] += (1.0 - epsilon)
        return action_probabilities

    def take_action(self, state, action):
        if action == Actions.UP and state.posX - 1 < 0:
            return (State(None, None, None, None), -10, True)
        if action == Actions.DOWN and state.posX + 1 > len(self.reward_map):
            return (State(None, None, None, None), -10, True)
        if action == Actions.LEFT and state.posY - 1 < 0:
            return (State(None, None, None, None), -10, True)
        if action == Actions.RIGHT and state.posY + 1 > len(
            self.reward_map[state.posX]
        ):
            return (State(None, None, None, None), -10, True)

        if action == Actions.UP:
            nextX = state.posX-1
            nextY = state.posY
            next_char = self.state_grid[nextX][nextY]
            next_steps = self.maxSteps if self.state_grid[nextX][nextY] == '#' else state.steps-1 
            state = State(nextX, nextY, next_char, next_steps)
            if(next_steps < 0 and next_char != '#'):
                return (State(None, None, None, None), -10, True)
            return (state, self.reward_map[nextX][nextY], state.is_terminal())

        if action == Actions.DOWN:
            nextX = state.posX+1
            nextY = state.posY
            next_char = self.state_grid[nextX][nextY]
            next_steps = self.maxSteps if self.state_grid[nextX][nextY] == '#' else state.steps-1 
            state = State(nextX, nextY, next_char, next_steps)
            if(next_steps < 0 and next_char != '#'):
                return (State(None, None, None, None), -10, True)
            return (state, self.reward_map[nextX][nextY], state.is_terminal())

        if action == Actions.LEFT:
            nextX = state.posX
            nextY = state.posY-1
            next_char = self.state_grid[nextX][nextY]
            next_steps = self.maxSteps if self.state_grid[nextX][nextY] == '#' else state.steps-1 
            state = State(nextX, nextY, next_char, next_steps)
            if(next_steps < 0 and next_char != '#'):
                return (State(None, None, None, None), -10, True)
            return (state, self.reward_map[nextX][nextY], state.is_terminal())

        if action == Actions.RIGHT:
            nextX = state.posX
            nextY = state.posY+1
            next_char = self.state_grid[nextX][nextY]
            next_steps = self.maxSteps if self.state_grid[nextX][nextY] == '#' else state.steps-1 
            state = State(nextX, nextY, next_char, next_steps)
            if(next_steps < 0 and next_char != '#'):
                return (State(None, None, None, None), -10, True)
            return (state, self.reward_map[nextX][nextY], state.is_terminal())


        