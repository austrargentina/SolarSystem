__author__ = 'Daniel'

from abc import abstractmethod, ABCMeta

class IComputeEvents(metaclass = ABCMeta):
    """
    Ist das Interface fuer die Controller-Klasse
    """

    @abstractmethod
    def computeMouseEvents(self):
        """
        Verarbeitet die Mouse-Events
        :return: Nichts
        """
        pass

    @abstractmethod
    def computeKeyboardEvents(self):
        """
        Verarbeitet die Keyboard-Events
        :return: Nichts
        """

class IDrawScreen(object, metaclass = ABCMeta):
    """
    Ist das Interface fuer die View-Klasse
    """

    @abstractmethod
    def drawContent(self):
        """
        Der Inhalt wird gezeichnet (Hintergrundbild, Planeten, etc.)
        :return: Nichts
        """
        pass

    @abstractmethod
    def drawButtons(self):
        """
        Falls vorhanden, sollen hier die Buttons gezeichnet werden
        :return: Nichts
        """

class IScreen(object, metaclass = ABCMeta):
    """
    Ist das Interface fuer die Model-Klasse
    """

    @abstractmethod
    def getObjects(self):
        """
        Liefert alle Planeten, die der derzeitige Screen beinhaltet, zurueck
        :return: objects[]
        """
        pass