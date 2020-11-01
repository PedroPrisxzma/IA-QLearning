def qLearning():

    for e in epochs:

        currentState = choose_start(state_map)

        for t in state_map_size * 2:

            action_probabilities = epsilon_greedy_policy(epsilon, currentState)

            action = random.choices([0,1,2,3], weights=action_probabilities)

            nextState, done = Agent.takeaction(currentState, action)

            #update
            currentState.update_qvalue(learning_rate, discount_factor, next_state, action)

            if done:
                break

        # ver como vai ser a saida no final
        return(False)