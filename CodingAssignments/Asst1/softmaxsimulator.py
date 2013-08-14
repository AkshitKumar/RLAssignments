import random
import const
import header
import math
from arm import Arm
from simulatorTemplate import SimulatorTemplate
import numpy as np

class SoftMaxSimulator(SimulatorTemplate):
  def __init__(self, temperature=100.0):
    SimulatorTemplate.__init__(self)
    self.temperature = temperature

  def getBestArm(self, j):
    expo_val = [math.exp(v.value/self.temperature) for k, v in sorted(self.Q_val[str(j)].iteritems())]
    expo_sum = sum(expo_val)
    expo_prob = [i/expo_sum for i in expo_val]
    
    arm_to_play = str(np.random.multinomial(100, expo_prob).argmax())
    #print arm_to_play
    #rand_num = random.random()
    #arm_to_play = str(0);
    #sum_prob = 0.0
    #for k in expo_prob:
    #  sum_prob += expo_prob[str(k)]
    #  if rand_num <= sum_prob:
    #    arm_to_play = str(k)
    #    break
    return arm_to_play

  def SimulateMethod(self):
    print 'For temperature '+str(self.temperature)
    SimulatorTemplate.SimulateMethod(self)
