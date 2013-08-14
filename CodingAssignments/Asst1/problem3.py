import header
import const
from ucbsimulator import UCBSimulator 
import plotterclasses as pc

def main():
  simulatorObj = UCBSimulator()
  simulatorObj.SimulateMethod()

  pc.UCBRewardPlotter([simulatorObj.avg_reward]).plotMethod()
  pc.UCBOptimalityPlotter([simulatorObj.avg_optimality]).plotMethod()

if __name__ == "__main__":
  main()
