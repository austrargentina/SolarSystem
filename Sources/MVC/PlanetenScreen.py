__author__ = 'Daniel'

#Import der Interfaces
from MVC.AbstractMVC import *
#Import aller konkreten Strategien fuer Movement, Appearence, Lighting und Camera
from Strategies.ConcreteStrategies import *

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
        #Ursprung drehen
        glRotatef(20,1,0,0)

        while True:
            #Keyboard-Events abfragen
            self.computeKeyboardEvents()
            #glRotatef(1,1,0,0)
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #clear frame !IMPORTANT!
            #Objekte zeichnen
            ScreenPlanets()
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
    """
    Beinhaltet die Objekte des Planeten-Screens (die Planeten) und die verschiedenen Strategien
    """

    lighting = None
    movement = None
    appearence = None
    camera = None

    def __init__(self):
        """
        Es werden die Standard-Strategien implemntiert (keine Animation, kein Licht, keine Texturen, Kamera von oben)
        :return: Nichts
        """

        #Definieren der Standard-Strategien
        lighting = NoLight()
        movement = NoAnimation()
        appearence =  NoTexture()
        camera = CamOben()

    def getObjects(self):
        """
        Liefert 
        :return:
        """
        pass

    def changeLighting(self):
        pass

    def changeMovement(self):
        pass

    def changeAppearence(self):
        pass

    def changeCamera(self):
        pass

    def Cube(self):
        vertices= (
            (1, -1, -1),
            (1, 1, -1),
            (-1, 1, -1),
            (-1, -1, -1),
            (1, -1, 1),
            (1, 1, 1),
            (-1, -1, 1),
            (-1, 1, 1)
            )

        edges = (
            (0,1),
            (0,3),
            (0,4),
            (2,1),
            (2,3),
            (2,7),
            (6,3),
            (6,4),
            (6,7),
            (5,1),
            (5,4),
            (5,7)
            )

        glBegin(GL_LINES)

        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])

        glEnd()

app = ComputeEventsPlanets()