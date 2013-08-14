import const
import header
from matplotlib import pyplot

class Plotter:
  def __init__(self, curves):
    self.curves = curves
  def getTitle(self): pass
  def getXlabel(self):
    return 'Number of Steps'
  def getYlabel(self):
    return 'ylabel'
  def getFigureName(self):
    return 'Graph.png'
  def getLegendLabels(self):
    return list()
  def plotMethod(self):
    xaxis = [i for i in range(1, const.NUM_PLAYS+1)]
    pyplot.title(self.getTitle())
    pyplot.legend([pyplot.plot(xaxis, i)[0] for i in self.curves], self.getLegendLabels(), loc=4)
    pyplot.xlabel(self.getXlabel())
    pyplot.ylabel(self.getYlabel())
    pyplot.grid(True)
    pyplot.savefig(self.getFigureName())
    pyplot.show()
