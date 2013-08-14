import random
import const
import header
from arm import Arm

class SimulatorTemplate:
  def __init__(self):
    self.q_val = {
      str(j) : {str(i) : random.gauss(const.MU, const.SIGMA) for i in range(const.NUM_ARMS)} 
      for j in range(const.NUM_GAMES)
    }
    self.Q_val = {
      str(j) : {str(i) : Arm() for i in range(const.NUM_ARMS)} for j in range(const.NUM_GAMES)
    }
    self.optimal_rewards = {
      str(i) : max(self.q_val[str(i)].iterkeys(), key=(lambda key: self.q_val[str(i)][key])) 
      for i in self.q_val.keys()
    }
    self.avg_reward = list()
    self.avg_optimality = list()

  def getBestArm(self, j):
    try:
      return Q_val.keys()[0]
    except:
      return 0

  def SimulateMethod(self):
    for i in range(const.NUM_PLAYS):
      tmp_avg_reward = 0.0
      tmp_avg_optimality = 0
      for j in range(const.NUM_GAMES):
        arm_to_play = self.getBestArm(str(j))

        actual_reward = self.q_val[str(j)][arm_to_play]
        noise_in_reward = random.gauss(const.MU, const.SIGMA);
        net_reward = actual_reward + noise_in_reward

        tmp_avg_reward += net_reward
        if str(arm_to_play) == str(self.optimal_rewards[str(j)]):
          tmp_avg_optimality += 1

        if self.Q_val[str(j)][arm_to_play].num_played == 0:
          self.Q_val[str(j)][arm_to_play].value = net_reward
        else:
          self.Q_val[str(j)][arm_to_play].value = \
              self.Q_val[str(j)][arm_to_play].value + \
              (net_reward - self.Q_val[str(j)][arm_to_play].value)/self.Q_val[str(j)][arm_to_play].num_played

        self.Q_val[str(j)][arm_to_play].num_played += 1

      self.avg_reward.append(tmp_avg_reward/const.NUM_GAMES)
      self.avg_optimality.append(tmp_avg_optimality*100.0/const.NUM_GAMES)
