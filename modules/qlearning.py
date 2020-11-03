import random
from modules.agent import Agent


def qLearning(
    learning_rate, discount_factor, epsilon, reward_map, state_grid, max_steps, epochs
):

    agent = Agent(learning_rate, discount_factor, reward_map, state_grid, max_steps)

    stateDic = {}

    for _ in range(epochs):

        current_state = Agent.choose_start(reward_map, state_grid, max_steps)

        for _ in range(0, len(reward_map) * len(reward_map[0]) * 2):

            action = Agent.epsilon_greedy_policy(epsilon, current_state)

            next_state, reward = agent.take_action(current_state, action, stateDic)
            print(current_state)

            # update
            current_state.update_qvalue(
                learning_rate, reward, discount_factor, next_state, action
            )

            stateDic[(current_state.posX, current_state.posY, current_state.steps)] = current_state

            if next_state.is_terminal:
                break

            current_state = next_state

        return stateDic
