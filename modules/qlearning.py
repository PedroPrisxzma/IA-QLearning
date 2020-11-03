import random
from modules.agent import Agent
import matplotlib.pyplot as plt

def qLearning(
    learning_rate, discount_factor, epsilon, reward_map, state_grid, max_steps, epochs
):

    agent = Agent(learning_rate, discount_factor, reward_map, state_grid, max_steps)

    stateDic = {}
    all_epochs = []
    epoch_rewards = []
    every_5 = []
    mean_every_5 = []

    for e in range(epochs):

        current_state = Agent.choose_start(reward_map, state_grid, max_steps)

        epoch_reward = 0
        all_epochs.append(e)

        for _ in range(0, len(reward_map) * len(reward_map[0]) * 2):

            action = Agent.epsilon_greedy_policy(epsilon, current_state)

            next_state, reward = agent.take_action(current_state, action, stateDic)

            # update
            current_state.update_qvalue(
                learning_rate, reward, discount_factor, next_state, action
            )

            stateDic[(current_state.posX, current_state.posY, current_state.steps)] = current_state

            epoch_reward += reward

            if next_state.is_terminal:
                epoch_rewards.append(epoch_reward)
                every_5.append(epoch_reward)
                break

            current_state = next_state
        if(e % 5 == 0):
            mean_every_5.append(sum(every_5) / len(every_5))
            every_5 = [] 
        
    plt.plot(epoch_rewards)
    plt.savefig('reward_cumulative.png')
    plt.show()

    plt.plot(mean_every_5)
    plt.savefig('mean_every5.png')
    plt.show()
    
    return stateDic
