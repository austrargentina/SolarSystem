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

            glPushMatrix()              #Speichern der aktuellen mMatrix
            self.doStrategies()         #Strategien anwenden
            self.screen.drawContent()   #Objekte zeichnen
            glPopMatrix()               #Wiederherstellen der aktuellen Matrix

            self.screenContent.zaehler +=  1 * self.screenContent.geschw; #Für Rotation

            pygame.display.flip()
            pygame.time.wait(20)

    def computeKeyboardEvents(self, event):
        """
        Verarbeitet die Keyboard-Events

        :return: Nichts
        """
        if event.key == pygame.K_LEFT:
            self.screenContent.geschw -= 1
            print(self.screenContent.geschw)
        elif event.key == pygame.K_RIGHT:
            self.screenContent.geschw += 1
            print(self.screenContent.geschw)
        elif event.key == pygame.K_c:
            self.screenContent.changeCamera()

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
                if self.screenContent.fov >= 10:
                    self.screenContent.fov -= 5
                    self.screen.setPerspective()
            elif event.button == 5: #Falls Maus-Rad nach hinten gescrollt wird
                if self.screenContent.fov <= 100:
                    self.screenContent.fov += 5
                    self.screen.setPerspective()

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
        self.display = (800, 600)
        pygame.display.set_mode(self.display, DOUBLEBUF|OPENGL)

        self.setPerspective()

    def drawButtons(self):
        pass

    def drawContent(self):
        #Fuer jedes Objekt in der Model-Klasse
        for object in self.screenContent.getObjects():
            #Zeichne Objekt
            object.drawObject()

    def setPerspective(self):
        glLoadIdentity()
        #Perspektive aendern
        gluPerspective(self.screenContent.fov, (self.display[0]/self.display[1]), 0.1, self.screenContent.maxSichtbar)

        #Ursprung verschieben
        glTranslatef(0.0,0,-self.screenContent.kameraEntfernung)

class ScreenPlanets(IScreen):
    """
    Beinhaltet die Objekte des Planeten-Screens (die Planeten) und die verschiedenen Strategien
    """

    lighting = None     #Lightin-Strategie
    movement = None     #Movement-Strategie
    appearence = None   #Appearence-Strategie
    camera = None       #Camera-Strategie

    objects = []        #Liste, die alle Objekte enthält
    zaehler = 0         #Zeahler für die Rotation
    geschw = 1          #Geschwindigkeit der Rotation

    unterteilungen = 50 #Anzal der Unterteilungen (für die Spheres)

    kameraEntfernung = 5000  #Entfrenung der Anfangskamera

    vergr = 1000    #vergrößerung der planeten

    maxSichtbar = 100000 #distanz, die maximal sichtbar ist

    fov = 45    #field of fiev für vergrößerung und verklinerung

    def __init__(self):
        """
        Es werden die Standard-Strategien implemntiert (keine Animation, kein Licht, keine Texturen, Kamera von oben)
        :return: Nichts
        """

        #Definieren der Standard-Strategien
        self.lighting = NoLight()
        self.movement = NoAnimation(self)
        self.appearence =  NoTexture()
        self.camera = CamOben()

        sonne = Sun(self, 1)
        self.objects.append(sonne) #hinzufuegen der Sonne
        merkur = Planet(self,sonne,42,0.0035,0.1) #41; 0.0035
        venus = Planet(self,sonne,78,0.0086, 0.1) #77; 0.0086
        erde = Planet(self,sonne,108,0.0091, 0.1) #107; 0.0091
        mars = Planet(self,sonne,164,0.0049, 0.1) #163; 0.0049
        jupiter = Planet(self,sonne,557,0.102, 0.1) #556; 0.102
        saturn = Planet(self,sonne,1020,0.086, 0.1) #1019; 0.086
        uranus = Planet(self,sonne,2052,0.037, 0.1) #2051; 0.037
        neptun = Planet(self,sonne,3214,0.035, 0.1) #3213; 0.035
        pluto = Planet(self,sonne,4220,0.0016, 0.1) #4219; 0.0016

        #planet1 = Planet(self,sonne,10,1,0.1) #41; 0.0035


        #mond1 = Moon(self,0.5,planet1,1,2)
        #mond2 = Moon(self,0.5, planet2,1,2)

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
            self.movement = WithAnimation(self)
        #Falls WithAnimation-Strategie implementiert
        elif isinstance(self.movement, WithAnimation):
            #Auf NoAnimation-Strategie aendern
            self.movement = NoAnimation(self)

    def changeAppearence(self):
        pass

    def changeCamera(self):
        #Falls Camera derzeit auf Cam-Oben-Strategie
        if isinstance(self.camera, CamOben):
            #Auf WithAnimation-Strategie aendern
            self.camera = CamParallel()
        #Falls Camera derzeit auf Cam-Parallel-Strategie
        elif isinstance(self.camera, CamParallel):
            #Auf NoAnimation-Strategie aendern
            self.camera = CamOben()

app = ComputeEventsPlanets()