""" This Module inherits the default simulator template
    and overrides the methods to implement UCB Algorithm"""
import random
from random import choice
import const
import header
import math
from arm import Arm
from simulatorTemplate import SimulatorTemplate
import numpy as np

class UCBSimulator(SimulatorTemplate):
  def __init__(self):
    SimulatorTemplate.__init__(self)

  """ Formula : choose ith arm such that it maximizes
              q_val[i] + sqrt(2*log(n_i)/n_total) """
  def getBestArm(self, game_num):
    tmp_val = [
      v.value + math.sqrt(2.0*math.log(self.num_steps[game_num])/v.num_played) 
      for v in self.Q_val[game_num]
    ]
    max_val = max(tmp_val)
    return choice([i for i, j in enumerate(tmp_val) if j == max_val])
  
  # Initialization - simulate each arm once in all the Bandit games
  def InitialPlay(self):
    for i in range(const.NUM_ARMS):
      for j in range(const.NUM_GAMES):
        self.num_steps[j] += 1
        arm_to_play = i

        actual_reward = self.q_val[j][arm_to_play]
        noise_in_reward = random.gauss(const.MU, const.SIGMA);
        net_reward = actual_reward + noise_in_reward

        if self.Q_val[j][arm_to_play].num_played == 0:
          self.Q_val[j][arm_to_play].value = net_reward
        else:
          self.Q_val[j][arm_to_play].value = \
              self.Q_val[j][arm_to_play].value + \
              (net_reward - self.Q_val[j][arm_to_play].value)/self.Q_val[j][arm_to_play].num_played

        self.Q_val[j][arm_to_play].num_played += 1

  def SimulateMethod(self):
    print 'Running UCB Algorithm'
    self.InitialPlay()
    SimulatorTemplate.SimulateMethod(self)
