from builtins import staticmethod

__author__ = 'Daniel'

#Import der Interfaces
from MVC.AbstractMVC import *
#Import aller konkreten Strategien fuer Movement, Appearence, Lighting und Camera
from Strategies.ConcreteStrategies import *
#Import der Planeten
from Planets.Planets import *

#Import der relevanten Klassen fuer Pygame und PyOpenGL
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


class ComputeEventsPlanets(IComputeEvents):

    screen = None
    screenContent = None

    def __init__(self):

        #Pygame initialisieren
        pygame.init()
        #Fenster offnen
        self.screenContent = ScreenPlanets()
        self.screen = DrawScreenPlanets(self.screenContent)
        #Ursprung drehen
        glRotatef(20,1,0,0)

        while True:
            #Events abfragen
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.computeKeyboardEvents(event)
                else:
                    self.computeMouseEvents(event)

            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #clear frame !IMPORTANT!

            self.doStrategies()         #Strategien anwenden
            self.screen.drawContent()   #Objekte zeichnen

            pygame.display.flip()
            pygame.time.wait(10)

    def computeKeyboardEvents(self, event):
        """
        Verarbeitet die Keyboard-Events

        :return: Nichts
        """
        #if event.key == pygame.K_LEFT:


    def computeMouseEvents(self, event):
        """
        Verarbeitet die Mouse-Events

        :return: Nichts
        """
        if event.type == pygame.QUIT: #Falls das Fenster geschlossen werden soll
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:    #Falls etwas mit der Maus gedrückt wurde
            if event.button == 1:   #Falls linke Maustaste gedrückt wurde
                self.screenContent.changeMovement() #Movement-Strategie aendern
            elif event.button == 3:   #Falls rechts Maustaste gedrückt wurde
                self.screenContent.changeLighting()
            elif event.button == 4: #Falls Maus-Rad nach vorne gescrollt wird
                glTranslatef(0.0,0.0,1)
            elif event.button == 5: #Falls Maus-Rad nach hinten gescrollt wird
                glTranslatef(0.0,0.0,-1)

    def doStrategies(self):
        """
        Wendet die verschiedenen Strategien an
        """
        self.screenContent.lighting.implementLighting()
        self.screenContent.movement.implementMovement()
        self.screenContent.appearence.implementAppearence()
        self.screenContent.camera.implementCamera()

class DrawScreenPlanets(IDrawScreen):
    """
    Ist die View-Klasse des PlanetenScreens und beinhaltet die Infos ueber das Display
    """

    #Model des MVCs, beinhaltet alle Objekte
    screenContent = None

    def __init__(self, screenContent):
        #Zuweisen des uebermittelten Models
        self.screenContent = screenContent

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
        #Fuer jedes Objekt in der Model-Klasse
        for object in self.screenContent.getObjects():
            #Zeichne Objekt
            object.drawObject()

class ScreenPlanets(IScreen):
    """
    Beinhaltet die Objekte des Planeten-Screens (die Planeten) und die verschiedenen Strategien
    """

    lighting = None     #Lightin-Strategie
    movement = None     #Movement-Strategie
    appearence = None   #Appearence-Strategie
    camera = None       #Camera-Strategie

    objects = []        #Liste, die alle Objekte enthält

    def __init__(self):
        """
        Es werden die Standard-Strategien implemntiert (keine Animation, kein Licht, keine Texturen, Kamera von oben)
        :return: Nichts
        """

        #Definieren der Standard-Strategien
        self.lighting = NoLight()
        self.movement = NoAnimation()
        self.appearence =  NoTexture()
        self.camera = CamOben()

        self.objects.append(Sun(1)) #hinzufuegen der Sonne
        self.objects.append(Cube())

    def getObjects(self):
        """
        Liefert die Liste mit allen Objekten zurueck
        :return: objects[]; Liste mit allen Objekten
        """
        return self.objects

    def changeLighting(self):
        pass

    def changeMovement(self):
        #Falls Movement derzeit NoAnimation-Strategie implementiert
        if isinstance(self. movement, NoAnimation):
            #Auf WithAnimation-Strategie aendern
            self.movement = WithAnimation()
        #Falls WithAnimation-Strategie implementiert
        elif isinstance(self.movement, WithAnimation):
            #Auf NoAnimation-Strategie aendern
            self.movement = NoAnimation()

    def changeAppearence(self):
        pass

    def changeCamera(self):
        pass

app = ComputeEventsPlanets()