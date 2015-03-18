__author__ = 'Daniel'

from Strategies.AbstractStrategies import *

from OpenGL.GL import *
from OpenGL.GLU import *

class NoLight(ILightingStrategy):
    """
    Implementiert die Klasse ILightingStrategy
    Beleuchtungsstrategie: Keine Beleuchtung
    """

    def implementLighting(self):
        pass

class PointLight(ILightingStrategy):
    """
    Implementiert die Klasse ILightingStrategy
    Beleuchtungsstrategie: Ein PointLight
    """

    def implementLighting(self):
        zeros = (0.15, 0.15, 0.15, 0.3)
        ones = (1.0, 1.0, 1.0, 0.3)
        half = (0.5, 0.5, 0.5, 0.5)

        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, zeros)
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, half)
        glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 15)
        glLightfv(GL_LIGHT0, GL_AMBIENT, zeros)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, ones)
        glLightfv(GL_LIGHT0, GL_SPECULAR, half)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)
        glColorMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE)

        glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
        glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
        glEnable(GL_TEXTURE_GEN_S)
        glEnable(GL_TEXTURE_GEN_T)

        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_NORMALIZE)
        glShadeModel(GL_SMOOTH)

class NoAnimation(IMovementStrategy):
    """
    Implementiert die Klasse IMovementStrategy
    Bewegungsstrategie: Keine Bewegung, nur Stillstand
    """
    model = None

    def __init__(self, model):
        self.model = model

    def implementMovement(self):
        self.model.geschw = 0

class WithAnimation(IMovementStrategy):
    """
    Implementiert die Klasse IMovementStrategy
    Bewegungsstrategie: Planeten drehen sich um Sonne, Monde drehen sich um Planeten
    """
    model = None
    aufgerufen = None

    def __init__(self, model):
        self.model = model
        self.aufgerufen = False

    def implementMovement(self):
        if self.aufgerufen is False:
            self.model.geschw = 1
            self.aufgerufen = True

class NoTexture(IAppearenceStrategy):
    """
    Implementiert die Klasse IAppearenceStrategy
    Bewegungsstrategie: Keine Texturen
    """

    def implementAppearence(self):
        pass

class WithTexture(IAppearenceStrategy):
    """
    Implementiert die Klasse IAppearenceStrategy
    Bewegungsstrategie: Realistische Texturen
    """

    def implementAppearence(self):
        pass



class CamOben(ICameraStrategy):
    """
    Implementiert die Klasse ICameraStrategy
    Bewegungsstrategie: Kamera befindet sich in der Vogelperspektive
    """

    def implementCamera(self):
        pass

class CamParallel(ICameraStrategy):
    """
    Implementiert die Klasse ICameraStrategy
    Bewegungsstrategie: Kamera befindet sich parallel zu den Planetenbahnen
    """

    def implementCamera(self):
        pass
