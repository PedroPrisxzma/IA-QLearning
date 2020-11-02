import random
from modules.action import Actions

class State:
    def __init__(self, posX: int, posY: int, char: str, steps: int):
        self.posX = posX
        self.posY = posY
        self.steps = steps
        self.is_terminal = False if char == "." or char == "#" else True
        self.char = char
        self.qvalues = {Actions.UP: 1.0, Actions.RIGHT: 1.0, Actions.DOWN: 1.0, Actions.LEFT: 1.0}
    
    #falta terminar
    def update_qvalue(learning_rate, discount_factor, next_state, action):
        max_next_state_qvalue = max(next_state.qvalues.values())
        next_state.reward

