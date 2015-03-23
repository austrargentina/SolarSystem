__author__ = 'Martin'

#Import der relevanten Klassen fuer Pygame und PyOpenGL
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from MVC.AbstractMVC import *

class ComputeEventsStart(IComputeEvents):
    """
     Ist die Controller-Klasse des StartScreens und beinhaltet die Infos ueber das Display

    """

    screen = None
    screenContent = None

    def __init__(self):
        #Pygame initialisieren
        pygame.init()
        #Fenster offnen
        self.screenContent = ScreenStart()
        self.screen = DrawScreenStart(self.screenContent)


    def computeKeyboardEvents(self):
        pass

    def computeMouseEvents(self):
        pass

class DrawScreenStart(IDrawScreen):

    """
     Ist die View-Klasse des StartScreens und beinhaltet die Infos ueber das Display

    """

    #Model des MVCs, beinhaltet alle Objekte
    screenContent = None

    def __init__(self, screenContent):
        #Zuweisen des uebermittelten Models
        self.screenContent = screenContent

        #Displaygroesse einstellen
        display = (800, 600)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    def drawButtons(self):
        pass

    def drawContent(self):
        pass



class ScreenStart(IScreen):

    def __init__(self):
     pass

    def getObjects(self):
        pass

app = ComputeEventsStart()