import header
import const
from epsilonsimulator import EpsilonSimulator
import plotterclasses as pc
import cPickle

def main():
  rewards, optimality = list(), list()

  rewFile = open('EpsRew'+str(const.NUM_ARMS)+'.p', 'wb')
  optFile = open('EpsOpt'+str(const.NUM_ARMS)+'.p', 'wb')
  for i in const.EPSILON_LIST:
    simulatorObj = EpsilonSimulator(i)
    simulatorObj.SimulateMethod()
    cPickle.dump(simulatorObj.avg_reward, rewFile)
    cPickle.dump(simulatorObj.avg_optimality, optFile)
    rewards.append(simulatorObj.avg_reward)
    optimality.append(simulatorObj.avg_optimality)

  rewFile.close()
  optFile.close()
  pc.EpsilonRewardPlotter(rewards).plotMethod()
  pc.EpsilonOptimalityPlotter(optimality).plotMethod()

if __name__ == "__main__":
  main()
