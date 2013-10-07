""" Generic Plotter Module for plotting a list of curves"""
from matplotlib import pyplot

"""
@param curves: List of y-values representing curves
"""
class Plotter:
  def __init__(self, curves):
    self.curves = curves
    self.XMAX = 455
  # Override in subclass
  def getTitle(self): pass
  def getXlabel(self):
    return 'State Number in base 13'
  # Override in subclass
  def getYlabel(self): pass
  # Override in Subclass
  def getFigureName(self):
    return 'Graph.png'
  # Override in Subclass
  def getLegendLabels(self):
    return list()
  def plotMethod(self):
    xaxis = [169*i+13*j+k for i in range(13) for j in range(13-i) for k in range(13-i-j)]
    pyplot.title(self.getTitle())
    pyplot.legend([pyplot.plot(xaxis, i)[0] for i in self.curves], self.getLegendLabels(), loc=4)
    pyplot.xlabel(self.getXlabel())
    pyplot.ylabel(self.getYlabel())
    pyplot.grid(True)
    pyplot.savefig(self.getFigureName())
    pyplot.show()
