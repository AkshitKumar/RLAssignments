""" This Module inherits the default simulator template
    and overrides the methods to implement Soft-Max 
    Action value method"""
import random
import const
import header
import math
from arm import Arm
from simulatorTemplate import SimulatorTemplate

"""
@param temperature: Temperature Parameter to generate probability of the samples
"""
class SoftMaxSimulator(SimulatorTemplate):
  def __init__(self, temperature=1.0):
    SimulatorTemplate.__init__(self)
    self.temperature = temperature

  # Returns the best arm based on the temperature and the Bandit Game
  def getBestArm(self, game_num):
    expo_val = [math.exp(v.value/self.temperature) for v in self.Q_val[game_num]]
    expo_sum = sum(expo_val)
    expo_lst = [i/expo_sum for i in expo_val]

    # Weighted Random Sampling
    rnd = random.random()
    for i, w in enumerate(expo_lst):
        rnd -= w
        if rnd < 0:
            return i
    return 0

  def SimulateMethod(self):
    print 'For temperature '+str(self.temperature)
    SimulatorTemplate.SimulateMethod(self)
