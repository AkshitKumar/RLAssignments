"""Plotter Subclasses"""
from plotter import Plotter

class value_plotter(Plotter):
  def getTitle(self):
    return r'Value Iteration : V*(s) vs s'
  def getLegendLabels(self):
    return [r'$\gamma='+str(i)+'$' for i in [0.3, 0.5, 0.7, 0.9]]
  def getYlabel(self):
    return r'Value function'
  def getFigureName(self):
    return 'Graph_value.png'

class policy_plotter(Plotter):
  def getTitle(self):
    return r'Policy Iteration : V*(s) vs s'
  def getLegendLabels(self):
    return [r'$\gamma='+str(i)+'$' for i in [0.3, 0.5, 0.7, 0.9]]
  def getYlabel(self):
    return r'Value function'
  def getFigureName(self):
    return 'Graph_policy.png'

class sweep_plotter(Plotter):
  def __init__(self, curves, gamma, name):
    Plotter.__init__(self, curves)
    self.gamma = gamma
    self.name = name
  def getTitle(self):
    return r''+self.name+' Iteration with $\gamma='+str(self.gamma)+'$ : V(s) vs s'
  def getLegendLabels(self):
    return [r'sweep='+str(i) for i in [1, 10, 'INF']]
  def getYlabel(self):
    return r'Value function'
  def getFigureName(self):
    return 'Graph_'+str(self.name)+'_'+str(self.gamma)+'.png'
