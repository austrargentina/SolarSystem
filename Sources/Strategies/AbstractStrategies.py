__author__ = 'Daniel'

from abc import ABCMeta, abstractmethod

class IMovementStrategy(object,metaclass = ABCMeta):

    @abstractmethod
    def implementMovement(self):
        pass

class ILightingStrategy(object,metaclass = ABCMeta):

    @abstractmethod
    def implementLighting(self):
        pass

class IAppearenceStrategy(object,metaclass = ABCMeta):

    @abstractmethod
    def implementAppearence(self):
        pass

class ICameraStrategy(object,metaclass = ABCMeta):

    @abstractmethod
    def implementCamera(self):
        pass