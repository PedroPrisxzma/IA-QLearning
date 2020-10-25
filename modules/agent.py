
class Agent:

  def __init__(
    self,
    n_states,
    n_actions,
    decay_rate=0.0001,
    learning_rate=0.7,
    gamma=0.618
  ):
    pass

  def choose_action(self, explore=True):
    pass

  def learn(
    self,
    state,
    action,
    reward,
    next_state,
    done,
    episode
  ):
    pass
