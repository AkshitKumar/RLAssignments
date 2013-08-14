import header
import const
from epsilonsimulator import EpsilonSimulator
from matplotlib import pyplot

def plotRewardGraph(lst):
  xaxis = [i for i in range(1, const.NUM_PLAYS+1)]
  
  legend_labels = [r'$\epsilon='+str(i)+'$' for i in const.EPSILON_LIST]
  pyplot.title(r'$\epsilon-greedy\ Action-Value\ Method$')
  pyplot.legend([ pyplot.plot(xaxis, i)[0] for i in lst], legend_labels, loc=4)
  pyplot.xlabel("Number of Steps")
  pyplot.ylabel("Average Reward")
  pyplot.grid(True)
  pyplot.savefig('Graph3.png')
  pyplot.show()

def plotOptimalityGraph(lst):
  xaxis = [i for i in range(1, const.NUM_PLAYS+1)]
  
  legend_labels = [r'$\epsilon='+str(i)+'$' for i in const.EPSILON_LIST]
  pyplot.title(r'$\epsilon-greedy\ Action-Value\ Method$')
  pyplot.legend([ pyplot.plot(xaxis, i)[0] for i in lst], legend_labels, loc=4)
  pyplot.xlabel("Number of Steps")
  pyplot.ylabel("% Optimal Action")
  pyplot.grid(True)
  pyplot.savefig('Graph4.png')
  pyplot.show()

def main():
  rewards, optimality = list(), list()

  for i in const.EPSILON_LIST:
    simulatorObj = EpsilonSimulator(i)
    simulatorObj.SimulateMethod()
    rewards.append(simulatorObj.avg_reward)
    optimality.append(simulatorObj.avg_optimality)

  plotRewardGraph(rewards)
  plotOptimalityGraph(optimality)

if __name__ == "__main__":
  main()
