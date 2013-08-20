""" Generic Plotter Module for plotting a list of curves"""
import const
import header
from matplotlib import pyplot

"""
@param curves: List of y-values representing curves
"""
class Plotter:
  def __init__(self, curves):
    self.curves = curves
  # Override in subclass
  def getTitle(self): pass
  def getXlabel(self):
    return 'Number of Steps'
  # Override in subclass
  def getYlabel(self): pass
  # Override in Subclass
  def getFigureName(self):
    return 'Graph.png'
  # Override in Subclass
  def getLegendLabels(self):
    return list()
  def plotMethod(self):
    xaxis = [i for i in range(1, const.NUM_STEPS+1)]
    pyplot.title(self.getTitle())
    pyplot.legend([pyplot.plot(xaxis, i)[0] for i in self.curves], self.getLegendLabels(), loc=4)
    pyplot.xlabel(self.getXlabel())
    pyplot.ylabel(self.getYlabel())
    pyplot.grid(True)
    pyplot.savefig(self.getFigureName())
    pyplot.show()
