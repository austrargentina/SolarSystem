__author__ = 'Daniel'

from MVC.AbstractMVC import *

class ComputeEventsPlanets(IComputeEvents):

    def __init__(self):
        pass

    def computeKeyboardEvents(self):
        pass

    def computeMouseEvents(self):
        pass

class DrawScreenPlanets(IDrawScreen):

    def __init__(self):
        pass

    def drawButtons(self):
        pass

    def drawContent(self):
        pass

class ScreenPlanets(IScreen):

    def __init__(self):
        pass

    def getObjects(self):
        pass