import header
import const
from ucbsimulator import UCBSimulator 
import plotterclasses as pc
import cPickle

def main():
  simulatorObj = UCBSimulator()
  simulatorObj.SimulateMethod()

  cPickle.dump([simulatorObj.avg_reward], open('UCBRew'+str(const.NUM_ARMS)+'.p', 'wb'))
  cPickle.dump([simulatorObj.avg_optimality], open('UCBOpt'+str(const.NUM_ARMS)+'.p', 'wb'))
  try:
    pc.UCBRewardPlotter([simulatorObj.avg_reward]).plotMethod()
    pc.UCBOptimalityPlotter([simulatorObj.avg_optimality]).plotMethod()
  except:
    print 'Couldn\'t print'

if __name__ == "__main__":
  main()
