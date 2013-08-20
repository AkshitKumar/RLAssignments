""" This Module contains the Class to Simulate any Algorithm.
    Other classes can inherit from this template and override
    the methods to implement specific Algorithm"""
import random
import const
import header
from arm import Arm
import numpy as np

"""
@param q_val[i][j] : Actual values of ith arm in jth Bandit Game
@param Q_val[i][j] : The average reward of ith arm in jth Bandit Game at any step
@param optimal_rewards[i] : Optimal arm of the ith Bandit Game
@param avg_reward[i] : Average reward over all Bandit Games in ith Step
@param avg_optimality[i] : Number of optimal actions chosen in all Bandit Games in ith step
@param num_steps[i] : Number of steps completed in ith Bandit Game at any instant
"""
class SimulatorTemplate:
  def __init__(self):
    self.q_val = [
      [random.gauss(const.MU, const.SIGMA) for i in range(const.NUM_ARMS)]
      for j in range(const.NUM_GAMES)
    ]
    self.Q_val = [[Arm() for i in range(const.NUM_ARMS)] for j in range(const.NUM_GAMES)]
    self.optimal_rewards = [np.argmax(i) for i in self.q_val]
    self.avg_reward = list()
    self.avg_optimality = list()
    self.num_steps = [0 for i in range(const.NUM_GAMES)] 

  # Override this method in the subclass
  def getBestArm(self, j):
      return 0

  # Default simulator of all the Algorithms
  def SimulateMethod(self):
    for i in range(const.NUM_STEPS):
      if i%100 == 99:
        print str(i+1)+' steps done'
      tmp_avg_reward = 0.0
      tmp_avg_optimality = 0
      for j in range(const.NUM_GAMES):
        self.num_steps[j] += 1
        arm_to_play = self.getBestArm(j)

        actual_reward = self.q_val[j][arm_to_play]
        noise_in_reward = random.gauss(const.MU, const.SIGMA);
        net_reward = actual_reward + noise_in_reward

        tmp_avg_reward += net_reward
        if arm_to_play == self.optimal_rewards[j]:
          tmp_avg_optimality += 1

        if self.Q_val[j][arm_to_play].num_played == 0:
          self.Q_val[j][arm_to_play].value = net_reward
        else:
          self.Q_val[j][arm_to_play].value = \
              self.Q_val[j][arm_to_play].value + \
              (net_reward - self.Q_val[j][arm_to_play].value)/self.Q_val[j][arm_to_play].num_played

        self.Q_val[j][arm_to_play].num_played += 1

      self.avg_reward.append(tmp_avg_reward/const.NUM_GAMES)
      self.avg_optimality.append(tmp_avg_optimality*100.0/const.NUM_GAMES)
