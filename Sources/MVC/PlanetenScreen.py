__author__ = 'Daniel'

#Import der Interfaces
from MVC.AbstractMVC import *

#Import der relevanten Klassen fuer Pygame und PyOpenGL
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


class ComputeEventsPlanets(IComputeEvents):

    screen = None

    def __init__(self):

        #Pygame initialisieren
        pygame.init()
        #Fenster offnen
        screen = DrawScreenPlanets()

        while True:
            #Keyboard-Events abfragen
            self.computeKeyboardEvents()
            glRotatef(1,1,0,0)
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #clear frame !IMPORTANT!
            Cube()
            pygame.display.flip()
            pygame.time.wait(10)

    def computeKeyboardEvents(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def computeMouseEvents(self):
        pass

class DrawScreenPlanets(IDrawScreen):

    def __init__(self):
        #Displaygroesse einstellen
        display = (800, 600)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

        #Perspektive aendern
        gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

        #Ursprung verschieben
        glTranslatef(0.0,0.0,-5)

    def drawButtons(self):
        pass

    def drawContent(self):
        pass

class ScreenPlanets(IScreen):

    def __init__(self):
        pass

    def getObjects(self):
        pass
