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
        pass

class Sun(ICenterObject):
    """
    Objekt ist Fixpunkt und dreht sich nur um eigene Achse
    """
    radius = 0  #Radius der Kugel

    def __init__(self, radius):
        self.radius = radius #zuweisen des übergebenen radius

    def drawObject(self):
         sphere = gluNewQuadric()
         #gluQuadricDrawStyle(self.sphere,GLU_LINE)
         gluSphere(sphere,self.radius,20,20)
         #glutWireSphere(2,100,20)

class Planet(ICenterObject):
    """
    Planet ist Objekt, dass sich um eigen Achse dreht und um Sonne dreht
    """

    def __init__(self, sun):
        pass

    def drawObject(self):
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