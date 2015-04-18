__author__ = 'Daniel'

from OpenGL.GL import *

from Strategies.AbstractStrategies import *

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
        """
        Erestellen eines Point-Lights

        :return: Nichts
        """
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
        """
        Initialisieren aller Attribute

        :param model: Model-Objekt des MVCs
        """
        self.model = model

    def implementMovement(self):
        """
        Deaktivieren der Animation

        :return: Nichts
        """
        self.model.geschw = 0 #Geschwinddigkeit auf 0 setzen

class WithAnimation(IMovementStrategy):
    """
    Implementiert die Klasse IMovementStrategy
    Bewegungsstrategie: Planeten drehen sich um Sonne, Monde drehen sich um Planeten
    """
    model = None
    aufgerufen = None

    def __init__(self, model):
        """
        Initialisieren aller Attribute

        :param model: Model-Objekt des MVCs
        """
        self.model = model
        self.aufgerufen = False #ob schon einmal aufgerufen

    def implementMovement(self):
        """
        Aktivieren der Animation

        :return: Nichts
        """
        if self.aufgerufen is False:
            self.model.geschw = 1
            self.aufgerufen = True

class NoTexture(IAppearenceStrategy):
    """
    Implementiert die Klasse IAppearenceStrategy
    Bewegungsstrategie: Keine Texturen
    """

    def implementAppearence(self):
        """
        Deaktivieren der Texturen

        :return: Nichts
        """
        glDisable(GL_TEXTURE_2D) #Deaktivieren der Texturen

class WithTexture(IAppearenceStrategy):
    """
    Implementiert die Klasse IAppearenceStrategy
    Bewegungsstrategie: Realistische Texturen
    """

    def implementAppearence(self):
        """
        Aktivieren der Texturen

        :return: Nichts
        """
        glEnable(GL_TEXTURE_2D) #Deaktivieren der Texturen

class CamOben(ICameraStrategy):
    """
    Implementiert die Klasse ICameraStrategy
    Bewegungsstrategie: Kamera befindet sich in der Vogelperspektive
    """

    def implementCamera(self):
        """
        Kamera schaut von oben auf Planeten

        :return: Nichts
        """
        glRotatef(90,1,0,0) #drehen des urpsrungs

class CamParallel(ICameraStrategy):
    """
    Implementiert die Klasse ICameraStrategy
    Bewegungsstrategie: Kamera befindet sich parallel zu den Planetenbahnen
    """

    def implementCamera(self):
        """
        Kamera schaut parallel zu Planetenbahnen auf Planeten

        :return: Nichts
        """
        glRotatef(0,1,0,0) #drehen des urpsrungs

class CamSeitlich(ICameraStrategy):
    """
    Implementiert die Klasse ICameraStrategy
    Bewegungsstrategie: Kamera befindet sich schräg zu den Planetenbahnen
    """

    def implementCamera(self):
        """
        Kamera schaut schräg auf Planeten

        :return: Nichts
        """
        glRotatef(15,1,0,0) #drehen des urpsrungs
