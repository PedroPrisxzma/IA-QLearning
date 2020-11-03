import random
from modules.agent import Agent
import matplotlib.pyplot as plt

def qLearning(
    learning_rate, discount_factor, epsilon, reward_map, state_grid, max_steps, epochs
):

    agent = Agent(learning_rate, discount_factor, reward_map, state_grid, max_steps)

    stateDic = {}
    # all_epochs = []
    # epoch_rewards = []
    # every_5 = []
    # mean_every_5 = []
    # epochs_mean = []

    for e in range(epochs):

        current_state = Agent.choose_start(reward_map, state_grid, max_steps)

        # epoch_reward = 0
        # all_epochs.append(e)
        # current_epoch_rewards = []

        for _ in range(0, len(reward_map) * len(reward_map[0]) * 2):

            action = Agent.epsilon_greedy_policy(epsilon, current_state)

            next_state, reward = agent.take_action(current_state, action, stateDic)

            # update
            current_state.update_qvalue(
                learning_rate, reward, discount_factor, next_state, action
            )

            stateDic[(current_state.posX, current_state.posY, current_state.steps)] = current_state

            # epoch_reward += reward
            # current_epoch_rewards.append(reward)

            if next_state.is_terminal:
                # epoch_rewards.append(epoch_reward)
                # every_5.append(epoch_reward)
                break

            current_state = next_state
        
        # epochs_mean.append(sum(current_epoch_rewards) / len(current_epoch_rewards))

        # if(e % 5 == 0):
        #     mean_every_5.append(sum(every_5) / len(every_5))
        #     every_5 = [] 

    # plt.style.use(['dark_background'])   
    # plt.figure(figsize=(18,12))
    # plt.plot(epochs_mean)
    # plt.xlabel("Episodios")
    # plt.ylabel("Reward médio por episodio", size=10)
    # plt.title("Reward médio por episodio 0.9 Lambda")
    # plt.savefig('epochs_mean.png')
    # plt.show()


    # plt.style.use(['dark_background'])
    # plt.figure(figsize=(20,10))
    # plt.plot(epoch_rewards)
    # plt.xlabel("Episodios")
    # plt.ylabel("Reward axumulativa", size=10)
    # plt.title("Reward acumulativa por episodio")
    # plt.savefig('reward_cumulative.png')
    # plt.show()

    # plt.figure(figsize=(20,10))
    # plt.plot(mean_every_5)
    # plt.xlabel("Episodios")
    # plt.ylabel("Média Móvel a cada 5 episodios", size=10)
    # plt.title("Média Móvel")
    # plt.savefig('mean_every5.png')
    # plt.show()

    # plt.figure(figsize=(20,10))
    # plt.plot(epochs_mean)
    # plt.xlabel("Episodios")
    # plt.ylabel("Reward médio por episodio", size=10)
    # plt.title("Reward médio por episodio")
    # plt.savefig('epochs_mean.png')
    # plt.show()
    
    return stateDic
