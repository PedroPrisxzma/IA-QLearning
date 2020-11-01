from modules.wip import State
from modules.action import Actions

class Agent():
    def __init__(self, learning_rate, discount_factor, state_map) -> Agent:
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.state_map = state_map
    
    def take_action(self, state, action):
        if action == Actions.UP and state.posX - 1 < 0:
            return State(None, None, None)
        if action == Actions.DOWN and state.posX + 1 > len(self.state_map):
            return State(None, None, None)
        if action == Actions.LEFT and state.posY - 1 < 0:
            return State(None, None, None)
        if action == Actions.RIGHT and state.posY + 1 > len(self.state_map[state.posX]):
            return State(None, None, None)