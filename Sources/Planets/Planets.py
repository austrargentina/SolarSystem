__author__ = 'Daniel'

from abc import abstractmethod, ABCMeta

from OpenGL.GL import *
from OpenGL.GLU import *

class ICenterObject(object, metaclass=ABCMeta):
    """
    Ist das Interaface fuer alle Objekte im Weltraum
    """

    @abstractmethod
    def drawObject(self):
        """
        Zeichnet das Objekt und alle Unterobjekte
        """
        pass

    @abstractmethod
    def addDependentObject(self):
        """
        Hinzufügen eines abhängigen Objekts (Sonne -> Planet; Planet -> Mond)
        """
        pass

class Sun(ICenterObject):
    """
    Objekt ist Fixpunkt und dreht sich nur um eigene Achse
    """
    model = None
    radius = 0  #Radius der Kugel
    dependentObjects = []

    def __init__(self, model, radius):
        self.model = model
        self.radius = radius #zuweisen des übergebenen radius

    def drawObject(self):
         sphere = gluNewQuadric()
         #gluQuadricDrawStyle(self.sphere,GLU_LINE)
         gluSphere(sphere,self.radius,self.model.unterteilungen,self.model.unterteilungen)
         #glutWireSphere(2,100,20)

         #Fuer jeden abhängigen Planeten
         for object in self.dependentObjects:
             glPushMatrix()
             object.drawObject()
             glPopMatrix()

    def addDependentObject(self, object):
        self.dependentObjects.append(object) #hinzufügen eines abhängigen Objekts

class Planet(ICenterObject):
    """
    Planet ist Objekt, dass sich um eigen Achse dreht und um Sonne dreht
    """
    model = None
    radius = 0
    rotation = 0
    distanceToSun = 0

    def __init__(self, model, radius, sun, rotation, distanceToSun):
        self.model = model
        sun.addDependentObject(self) #hinzufügen des Plaentens zur aktuellen Sonne
        self.radius = radius
        self.rotation = rotation
        self.distanceToSun = distanceToSun

    def drawObject(self):
        glRotatef(self.rotation*self.model.zaehler,0,1,0) #drehen des urpsrungs
        glTranslatef(self.distanceToSun,0.0,0.0) #Verschieben des ursprungs
        sphere = gluNewQuadric()
        gluSphere(sphere,self.radius,self.model.unterteilungen,self.model.unterteilungen)

    def addDependentObject(self, object):
        pass


class Moon(ICenterObject):
    """
    Mond ist Objekt, dass sich um eigene Achse dreht, um einen Planeten und um die Sonne
    """

    def __init__(self, planet):
        pass
        
    def drawObject(self):
        pass

class Cube(ICenterObject):
    """
    Cube ist ein Testobjekt, dass nur aus Gitterlinien besteht
    """
    def addDependentObject(self):
        pass

    def drawObject(self):
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