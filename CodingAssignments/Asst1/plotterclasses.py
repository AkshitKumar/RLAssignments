from plotter import Plotter
import const
import header

class EpsilonPlotter(Plotter):
  def getTitle(self):
    return r'$\epsilon-greedy\ Action-Value\ Method$'
  def getLegendLabels(self):
    return [r'$\epsilon='+str(i)+'$' for i in const.EPSILON_LIST]

class SoftMaxPlotter(Plotter):
  def getTitle(self):
    return 'Softmax Action Selection'
  def getLegendLabels(self):
    return [r'$T='+str(i)+'$' for i in const.TEMPERATURE_LIST]

class UCBPlotter(Plotter):
  def getTitle(self):
    return 'UCB Algorithm'
  def getLegendLabels(self):
    return ['Greedy']

class EpsilonRewardPlotter(EpsilonPlotter): 
  def getYlabel(self):
    return 'Average Reward'
  def getFigureName(self):
    return 'Graph1.png'

class EpsilonOptimalityPlotter(EpsilonPlotter):
  def getYlabel(self):
    return '% Optimal Action'
  def getFigureName(self):
    return 'Graph2.png'

class SoftMaxRewardPlotter(SoftMaxPlotter):
  def getYlabel(self):
    return 'Average Reward'
  def getFigureName(self):
    return 'Graph3.png'

class SoftMaxOptimalityPlotter(SoftMaxPlotter):
  def getYlabel(self):
    return '% Optimal Action'
  def getFigureName(self):
    return 'Graph4.png'

class UCBRewardPlotter(UCBPlotter):
  def getYlabel(self):
    return 'Average Reward'
  def getFigureName(self):
    return 'Graph5.png'

class UCBOptimalityPlotter(UCBPlotter):
  def getYlabel(self):
    return '% Optimal Action'
  def getFigureName(self):
    return 'Graph6.png'
