__author__ = 'Daniel'

from abc import abstractmethod, ABCMeta

from OpenGL.GL import *
from OpenGL.GLU import *
from pyglet.gl import *

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
    name = None

    def __init__(self,model, name, radius):
        self.dependentObjects = []
        self.name = name
        self.model = model
        self.radius = radius * model.vergr/5 #zuweisen des übergebenen radius

    def drawObject(self):
        texture = self.model.textures[self.name]
        glBindTexture(texture.target, texture.id)

        sphere = gluNewQuadric()

        gluQuadricNormals(sphere,GLU_SMOOTH)
        gluQuadricTexture(sphere,GL_TRUE)

        gluSphere(sphere,self.radius,self.model.unterteilungen,self.model.unterteilungen)

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
    dependentObjects = []

    name = None
    model = None
    radius = 0
    rotation = 0
    distanceToSun = 0

    def __init__(self, model, name, sun, distanceToSun, radius, rotation):
        self.name = name
        self.model = model
        sun.addDependentObject(self) #hinzufügen des Plaentens zur aktuellen Sonne
        self.radius = radius * model.vergr
        self.rotation = 1/(rotation)
        self.distanceToSun = sun.radius + distanceToSun #* model.vergr

    def drawObject(self):
        glRotatef(self.rotation*self.model.zaehler,0,1,0) #drehen des urpsrungs
        glTranslatef(self.distanceToSun,0.0,0.0) #Verschieben des ursprungs

        sphere = gluNewQuadric()

        gluSphere(sphere,self.radius,self.model.unterteilungen,self.model.unterteilungen)

        #Fuer jeden abhängigen Planeten
        for object in self.dependentObjects:
             glPushMatrix()
             object.drawObject()
             glPopMatrix()

    def addDependentObject(self, object):
        self.dependentObjects.append(object) #hinzufügen eines abhängigen Objekts


class Moon(ICenterObject):
    """
    Mond ist Objekt, dass sich um eigene Achse dreht, um einen Planeten und um die Sonne
    """

    name = None
    model = None
    radius = 0
    rotation = 0
    distanceToPlanet = 0

    def __init__(self, model, name, planet, distanceToPlanet, radius, rotation):
        self.name = name
        self.model = model
        planet.addDependentObject(self) #hinzufügen des Mondes zum aktuellen Planeten
        self.radius = radius
        self.rotation = rotation
        self.distanceToPlanet = distanceToPlanet
        
    def drawObject(self):
        glRotatef(self.rotation*self.model.zaehler,0,1,0) #drehen des urpsrungs
        glTranslatef(self.distanceToPlanet,0.0,0.0) #Verschieben des ursprungs
        sphere = gluNewQuadric()
        gluSphere(sphere,self.radius,self.model.unterteilungen,self.model.unterteilungen)

    def addDependentObject(self):
        pass
