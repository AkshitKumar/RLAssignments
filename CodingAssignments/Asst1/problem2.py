import const
import header 
from softmaxsimulator import SoftMaxSimulator
from matplotlib import pyplot

def plotRewardGraph(lst):
  xaxis = [i for i in range(1, const.NUM_PLAYS+1)]
  
  legend_labels = [r'$T='+str(i)+'$' for i in const.TEMPERATURE_LIST]
  pyplot.title('Softmax Action Selection')
  pyplot.legend([ pyplot.plot(xaxis, i)[0] for i in lst], legend_labels, loc=4)
  pyplot.xlabel("Number of Steps")
  pyplot.ylabel("Average Reward")
  pyplot.grid(True)
  pyplot.savefig('Graph5.png')
  pyplot.show()

def plotOptimalityGraph(lst):
  xaxis = [i for i in range(1, const.NUM_PLAYS+1)]
  
  legend_labels = [r'$T='+str(i)+'$' for i in const.TEMPERATURE_LIST]
  pyplot.title('Softmax Action Selection')
  pyplot.legend([ pyplot.plot(xaxis, i)[0] for i in lst], legend_labels, loc=4)
  pyplot.xlabel("Number of Steps")
  pyplot.ylabel("% Optimal Action")
  pyplot.grid(True)
  pyplot.savefig('Graph6.png')
  pyplot.show()

def main():
  rewards, optimality = list(), list()

  for i in const.TEMPERATURE_LIST:
    simulatorObj = SoftMaxSimulator(i)
    simulatorObj.SimulateMethod()
    rewards.append(simulatorObj.avg_reward)
    optimality.append(simulatorObj.avg_optimality)

  plotRewardGraph(rewards)
  plotOptimalityGraph(optimality)

if __name__ == "__main__":
  main()
