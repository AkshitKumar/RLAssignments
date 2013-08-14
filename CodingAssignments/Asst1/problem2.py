import const
import header 
from softmaxsimulator import SoftMaxSimulator
import plotterclasses as pc

def main():
  rewards, optimality = list(), list()

  for i in const.TEMPERATURE_LIST:
    simulatorObj = SoftMaxSimulator(i)
    simulatorObj.SimulateMethod()
    rewards.append(simulatorObj.avg_reward)
    optimality.append(simulatorObj.avg_optimality)

  pc.SoftMaxRewardPlotter(rewards).plotMethod()
  pc.SoftMaxOptimalityPlotter(optimality).plotMethod()

if __name__ == "__main__":
  main()
