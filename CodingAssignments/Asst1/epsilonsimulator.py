import random
import const
import header
from arm import Arm
from simulatorTemplate import SimulatorTemplate

class EpsilonSimulator(SimulatorTemplate):
  def __init__(self, epsilon=0.0):
    SimulatorTemplate.__init__(self)
    self.epsilon = epsilon

  def getBestArm(self, j):
    arm_to_play = str(random.randint(0, const.NUM_ARMS-1))
    if random.random() > self.epsilon:
      arm_to_play = max(self.Q_val[str(j)].iterkeys(), key=(lambda key: self.Q_val[str(j)][key]))
    return arm_to_play

  def SimulateMethod(self):
    print "Simulating Algorithm with epsilon = "+str(self.epsilon)
    SimulatorTemplate.SimulateMethod(self)
