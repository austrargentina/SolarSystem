__author__ = 'Daniel'

from abc import abstractmethod, ABCMeta

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

    def drawObject(self):
        pass

class Planet(ICenterObject):
    """
    Planet ist Objekt, dass sich um eigen Achse dreht und um Sonne dreht
    """

    def drawObject(self):
        pass

class Moon(ICenterObject):
    """
    Mond ist Objekt, dass sich um eigene Achse dreht, um einen Planeten und um die Sonne
    """
        
    def drawObject(self):
        pass