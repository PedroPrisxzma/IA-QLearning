import random
from modules.agent import Agent


def qLearning(
    learning_rate, discount_factor, epsilon, reward_map, state_grid, max_steps, epochs
):

    agent = Agent(learning_rate, discount_factor, reward_map, max_steps)

    stateDic = {}

    for _ in range(epochs):

        current_state = Agent.choose_start(reward_map, state_grid, max_steps)

        for _ in len(reward_map) * len(reward_map[0]) * 2:

            action_probabilities = Agent.epsilon_greedy_policy(epsilon, current_state)

            action = random.choices([0, 1, 2, 3], weights=action_probabilities)

            next_state, done = agent.take_action(current_state, action)

            # update
            current_state.update_qvalue(
                learning_rate, discount_factor, next_state, action
            )

            if done:
                break
            
            stateDic[(current_state.posX, current_state.posY, current_state.steps)] = current_state

            current_state = next_state

        # ver como vai ser a saida no final
        return False
