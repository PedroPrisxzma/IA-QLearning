import random
from modules.action import Actions


class State:
    def __init__(self, posX: int, posY: int, char: str, steps: int):
        self.posX = posX
        self.posY = posY
        self.steps = steps
        self.is_terminal = False if char == "." or char == "#" else True
        self.char = char
        self.qvalues = {
            Actions.UP: 0.0,
            Actions.RIGHT: 0.0,
            Actions.DOWN: 0.0,
            Actions.LEFT: 0.0,
        }

    def update_qvalue(self, learning_rate, reward, discount_factor, next_state, action):
        max_next_state_qvalue = max(next_state.qvalues.values())

        self.qvalues[action] = self.qvalues[action] + learning_rate * (
            reward + discount_factor * max_next_state_qvalue - self.qvalues[action]
        )

    def __str__(self):
        print("State:")
        print(" posX:    ", self.posX)
        print(" posY:    ", self.posY)
        print(" steps:   ", self.steps)
        print(" terminal:", self.is_terminal)
        print(" char:    ", self.char)
        print(" Qvalues: ", self.qvalues)
        return ""