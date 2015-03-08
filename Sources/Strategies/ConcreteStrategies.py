__author__ = 'Daniel'

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
        pass



class NoAnimation(IMovementStrategy):
    """
    Implementiert die Klasse IMovementStrategy
    Bewegungsstrategie: Keine Bewegung, nur Stillstand
    """

    def implementMovement(self):
        pass

class WithAnimation(IMovementStrategy):
    """
    Implementiert die Klasse IMovementStrategy
    Bewegungsstrategie: Planeten drehen sich um Sonne, Monde drehen sich um Planeten
    """

    def implementMovement(self):
        pass



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
