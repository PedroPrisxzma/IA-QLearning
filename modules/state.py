import random
from modules.action import Actions

class State:
    def __init__(self, posX: int, posY: int, char: str, steps: int):
        self.posX = posX
        self.posY = posY
        self.steps = steps
        self.is_terminal = False if char == "." or char == "#" else True
        self.char = char
        self.reward = self.define_reward(char)
        self.qvalues = {Actions.UP: 0, Actions.RIGHT: 0, Actions.DOWN: 0, Actions.LEFT: 0}

    def define_reward(char):
        if(char == '.'):
            return -1
        elif(char == '#'):
            return 1
        elif(char == '$'):
            return 10
        else:
            return -10
    
    #falta terminar
    def update_qvalue(learning_rate, discount_factor, next_state, action):
        max_next_state_qvalue = max(next_state.qvalues.values())
        next_state.reward

