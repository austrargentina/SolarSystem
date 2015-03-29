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
        Zeichnet das Objekt und ruft die drawObject()-Methode aller Unterobjekte auf
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
    Objekt ist Fixpunkt und dreht sich nicht
    """
    model = None
    radius = 0  #Radius der Kugel
    name = None

    def __init__(self,model, name, radius):
        """
        Initialisieren aller Attribute

        :param model: Model-Objekt des MVCs
        :param name: Name der Sonne
        :param radius: Radius der Sonne

        :return: Nichts
        """
        self.dependentObjects = [] #Liste, in der alle abhängigen Planeten gespeichert werden
        self.name = name
        self.model = model
        self.radius = radius * model.vergr/5 #zuweisen des übergebenen radius und skalieren, so dass gut sichtbar

    def drawObject(self):
        """
        Zeichnet die Sonne und ruft die drawObject aller abhängigen Planeten auf

        :return: Nichts
        """

        texture = self.model.textures[self.name].get_texture()  #Textur holen

        #glEnable(texture.target)    #Texturen aktivieren
        glBindTexture(texture.target, texture.id)   #Textur verwenden

        #Sonne zeichnen
        sphere = gluNewQuadric()
        gluQuadricTexture(sphere,GL_TRUE)
        gluSphere(sphere,self.radius,self.model.unterteilungen,self.model.unterteilungen)

        #Fuer jeden abhängigen Planeten
        for planet in self.dependentObjects:
            glPushMatrix()
            planet.drawObject()
            glPopMatrix()

    def addDependentObject(self, planet):
        """
        Hinzufügen eines Planeten als abhängiges Objekt

        :param planet: Planet, der hinzugefügt werden soll

        :return: Nichts
        """
        self.dependentObjects.append(planet) #hinzufügen eines abhängigen Planten

class Planet(ICenterObject):
    """
    Planet ist Objekt, dass sich um eigen Achse dreht und um Sonne dreht
    """

    name = None
    model = None
    radius = 0          #Radius des Planetn
    rotation = 0        #Drehung um Sonne
    distanceToSun = 0  #Abstand zur Sonne

    def __init__(self, model, name, sun, distanceToSun, radius, rotation):
        """
        Initialisieren aller Attribute

        :param model: Model-Objekt des MVCs
        :param name: Name des Planeten
        :param sun: Sonne, um die sich der Planet dreht
        :param distanceToSun: Entfernung zur Sonne
        :param radius: Radius des Planeten
        :param rotation: Drehung um Sonne

        :return: Nichts
        """
        self.dependentObjects = []
        self.name = name
        self.model = model
        sun.addDependentObject(self) #hinzufügen des Plaentens zur aktuellen Sonne
        self.radius = radius * model.vergr  #Skalieren, so dass gut sichtbar
        self.rotation = 1/(rotation)
        self.distanceToSun = sun.radius + distanceToSun #Skalieren, so dass gut sichtbar

    def drawObject(self):
        """
        Zeichnet den Planeten und ruft die drawObject aller abhängigen Monde auf

        :return: Nichts
        """

        glRotatef(self.rotation*self.model.zaehler,0,1,0)   #drehen des urpsrungs
        glTranslatef(self.distanceToSun,0.0,0.0)    #Verschieben des ursprungs

        texture = self.model.textures[self.name].get_texture()  #Textur holen

        #glEnable(texture.target)    #Texturen aktivieren
        glBindTexture(texture.target, texture.id)   #Textur verwenden

        #Planet zeichnen
        sphere = gluNewQuadric()
        gluQuadricTexture(sphere,GL_TRUE)
        gluSphere(sphere,self.radius,self.model.unterteilungen,self.model.unterteilungen)

        #Fuer jeden abhängigen Mond
        for moon in self.dependentObjects:
            glPushMatrix()
            moon.drawObject()
            glPopMatrix()

    def addDependentObject(self, moon):
        """
        Hinzufügen eines Mondes als abhängiges Objekt

        :param moon: Mond, der hinzugefügt werden soll

        :return: Nichts
        """
        self.dependentObjects.append(moon) #hinzufügen eines abhängigen Mondes

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
        """
        Initialisieren aller Attribute

        :param model: Model-Objekt des MVCs
        :param name: Name des Planeten
        :param planet: Planet, um den sich der Mond dreht
        :param distanceToPlanet: Entfernung zum Planeten
        :param radius: Radius des Mondes
        :param rotation: Drehung um Planeten

        :return: Nichts
        """
        self.name = name
        self.model = model
        planet.addDependentObject(self) #hinzufügen des Mondes zum aktuellen Planeten
        self.radius = radius * model.vergr
        self.rotation = 1/(rotation)
        self.distanceToPlanet = planet.radius + distanceToPlanet #* model.vergr
        
    def drawObject(self):
        """
        Zeichnet den Mond

        :return: Nichts
        """
        glRotatef(self.rotation*self.model.zaehler,0,1,0) #drehen des urpsrungs
        glTranslatef(self.distanceToPlanet,0.0,0.0) #Verschieben des ursprungs

        texture = self.model.textures[self.name].get_texture()  #Textur holen

        #glEnable(texture.target)    #Texturen aktivieren
        glBindTexture(texture.target, texture.id)   #Textur verwenden

        #Mond zeichnen
        sphere = gluNewQuadric()
        gluQuadricTexture(sphere,GL_TRUE)
        gluSphere(sphere,self.radius,self.model.unterteilungen,self.model.unterteilungen)

    def addDependentObject(self):
        pass
