import random
import const
import header
import math
from arm import Arm
from simulatorTemplate import SimulatorTemplate
import numpy as np

class UCBSimulator(SimulatorTemplate):
  def __init__(self):
    SimulatorTemplate.__init__(self)
  def getBestArm(self, j):
    tmp_val = [
      v.value + math.sqrt(2.0*math.log(v.num_played)/self.num_steps[str(j)])
      for k, v in sorted(self.Q_val[str(j)].iteritems())
    ]
    return str(np.argmax(tmp_val))

  def InitialPlay(self):
    for i in range(const.NUM_ARMS):
      for j in range(const.NUM_GAMES):
        self.num_steps[str(j)] += 1
        arm_to_play = str(i)

        actual_reward = self.q_val[str(j)][arm_to_play]
        noise_in_reward = random.gauss(const.MU, const.SIGMA);
        net_reward = actual_reward + noise_in_reward

        if self.Q_val[str(j)][arm_to_play].num_played == 0:
          self.Q_val[str(j)][arm_to_play].value = net_reward
        else:
          self.Q_val[str(j)][arm_to_play].value = \
              self.Q_val[str(j)][arm_to_play].value + \
              (net_reward - self.Q_val[str(j)][arm_to_play].value)/self.Q_val[str(j)][arm_to_play].num_played

        self.Q_val[str(j)][arm_to_play].num_played += 1

  def SimulateMethod(self):
    print 'Running UCB Algorithm'
    self.InitialPlay()
    SimulatorTemplate.SimulateMethod(self)
