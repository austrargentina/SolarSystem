__author__ = 'Daniel'

from MVC.AbstractMVC import *

class ComputeEventsStart(IComputeEvents):

    def __init__(self):
        pass

    def computeKeyboardEvents(self):
        pass

    def computeMouseEvents(self):
        pass

class DrawScreenStart(IDrawScreen):

    def __init__(self):
        pass

    def drawButtons(self):
        pass

    def drawContent(self):
        pass

class ScreenStart(IScreen):

    def __init__(self):
        pass

    def getObjects(self):
        pass