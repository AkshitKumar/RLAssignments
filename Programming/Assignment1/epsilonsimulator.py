""" This Module inherits the default simulator template
    and overrides the methods to implement epsilon-greedy
    Action value method"""
import random
from random import choice
import const
import header
from arm import Arm
from simulatorTemplate import SimulatorTemplate
import numpy as np

"""
@param epsilon: Percentage of exploratory moves
"""
class EpsilonSimulator(SimulatorTemplate):
  def __init__(self, epsilon=0.0):
    SimulatorTemplate.__init__(self)
    self.epsilon = epsilon

  # Returns the best arm based on epsilon and the Bandit Game
  def getBestArm(self, game_num):
    arm_to_play = random.randint(0, const.NUM_ARMS-1)
    if random.random() > self.epsilon:
      max_elem = max(self.Q_val[game_num])
      arm_to_play = choice([i for i, j in enumerate(self.Q_val[game_num]) if j == max_elem])
    return arm_to_play

  def SimulateMethod(self):
    print "Simulating Algorithm with epsilon = "+str(self.epsilon)
    SimulatorTemplate.SimulateMethod(self)
