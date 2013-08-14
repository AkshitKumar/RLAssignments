import header
import const
from epsilonsimulator import EpsilonSimulator
import plotterclasses as pc

def main():
  rewards, optimality = list(), list()

  for i in const.EPSILON_LIST:
    simulatorObj = EpsilonSimulator(i)
    simulatorObj.SimulateMethod()
    rewards.append(simulatorObj.avg_reward)
    optimality.append(simulatorObj.avg_optimality)

  pc.EpsilonRewardPlotter(rewards).plotMethod()
  pc.EpsilonOptimalityPlotter(optimality).plotMethod()

if __name__ == "__main__":
  main()
