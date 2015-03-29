__author__ = 'Daniel'

from abc import ABCMeta, abstractmethod

class IMovementStrategy(object,metaclass = ABCMeta):
    """
    Ist das Interface für die Movement-Strategie
    """

    @abstractmethod
    def implementMovement(self):
        """
        Implementieren der Movement-Strategie

        :return: Nichts
        """
        pass

class ILightingStrategy(object,metaclass = ABCMeta):
    """
    Ist das Interface für die Lighting-Strategie
    """

    @abstractmethod
    def implementLighting(self):
        """
        Implementieren der Lighting-Strategie

        :return: Nichts
        """
        pass

class IAppearenceStrategy(object,metaclass = ABCMeta):
    """
    Ist das Interface für die Appearence-Strategie
    """

    @abstractmethod
    def implementAppearence(self):
        """
        Implementieren der Appearence-Strategie

        :return: Nichts
        """
        pass

class ICameraStrategy(object,metaclass = ABCMeta):
    """
    Ist das Interface für die Kamera-Strategie
    """

    @abstractmethod
    def implementCamera(self):
        """
        Implementieren der Camera-Strategie

        :return: Nichts
        """
        pass