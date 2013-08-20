import const
import header 
from softmaxsimulator import SoftMaxSimulator
import plotterclasses as pc
import cPickle

def main():
  rewards, optimality = list(), list()

  rewFile = open('SoftRew'+str(const.NUM_ARMS)+'.p', 'wb')
  optFile = open('SoftOpt'+str(const.NUM_ARMS)+'.p', 'wb')
  for i in const.TEMPERATURE_LIST:
    simulatorObj = SoftMaxSimulator(i)
    simulatorObj.SimulateMethod()
    cPickle.dump(simulatorObj.avg_reward, rewFile)
    cPickle.dump(simulatorObj.avg_optimality, optFile)
    rewards.append(simulatorObj.avg_reward)
    optimality.append(simulatorObj.avg_optimality)

  rewFile.close()
  optFile.close()
  pc.SoftMaxRewardPlotter(rewards).plotMethod()
  pc.SoftMaxOptimalityPlotter(optimality).plotMethod()

if __name__ == "__main__":
  main()
