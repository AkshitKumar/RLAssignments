import random
import const
import header
import math
from arm import Arm
from simulatorTemplate import SimulatorTemplate
import numpy as np

class SoftMaxSimulator(SimulatorTemplate):
  def __init__(self, temperature=1.0):
    SimulatorTemplate.__init__(self)
    self.temperature = temperature

  def getBestArm(self, j):
    expo_val = [math.exp(v.value/self.temperature) for k, v in sorted(self.Q_val[str(j)].iteritems())]
    expo_sum = sum(expo_val)
    expo_prob = [i/expo_sum for i in expo_val]
    
    arm_to_play = str(np.random.multinomial(100, expo_prob).argmax())
    return arm_to_play

  def SimulateMethod(self):
    print 'For temperature '+str(self.temperature)
    SimulatorTemplate.SimulateMethod(self)
