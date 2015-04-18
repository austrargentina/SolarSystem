from MVC.PlanetenScreen import ComputeEventsPlanets

__author__ = 'Martin'

#Import der relevanten Klassen fuer Pygame und PyOpenGL
import pygame

from MVC.AbstractMVC import *

class ComputeEventsStart(IComputeEvents):
    """
     Ist die Controller-Klasse des StartScreens

    """

    screen = None
    screenContent = None

    def __init__(self):
        """

        Konstruktor

        Erstellt unser Fenster und füllt es mit vorgegebnen Content;
        Überprüft auf Events und ruft dementsprechende Methoden auf.

        """
        #Pygame initialisieren
        pygame.init()
        #Fenster offnen
        self.screenContent = ScreenStart()
        self.screen = DrawScreenStart(self.screenContent)

        self.screen.drawContent()

        while True:
            #Events abfragen
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.computeKeyboardEvents(event)
                else:
                    self.computeMouseEvents(event)
            pygame.display.flip()



    def computeKeyboardEvents(self,event):
        """
        Verarbeitet Tastertur-Knopf Events

        :param event:           Tastertur-Event, welches aufgetreten ist.

        """
        if event.key == pygame.K_SPACE:
            pygame.quit()
            ComputeEventsPlanets()

    def computeMouseEvents(self,event):
        """
        Verarbeitet Maus Events

        :param event:           Maus-Event, welches aufgetreten ist.

        """
        if event.type == pygame.QUIT: #Falls das Fenster geschlossen werden soll
            pygame.quit()
            quit()

class DrawScreenStart(IDrawScreen):

    """
     Ist die View-Klasse des StartScreens und beinhaltet die Infos ueber das Display

    """

    #Model des MVCs, beinhaltet alle Objekte
    screenContent = None
    bgd_image = None
    surface = None

    def __init__(self, screenContent):
        """
        Konstruktor

        Setzt Fenstergröße und Titel;
        Laedt Hintergrundbild (Splashscreen)


        :param screenContent:   Das Objekt des aktuellen Inhaltes des Fensters.
        """
        #Zuweisen des uebermittelten Models
        self.screenContent = screenContent

        #Displaygroesse einstellen
        display = (800, 600)
        pygame.display.set_mode(display)

        #Fenster Titel einstellen
        pygame.display.set_caption("Solarsystem Menü")

        #Hintergrundbild laden
        self.bgd_image = pygame.image.load("../../Images/Splashscreen.jpg").convert()

    def drawButtons(self):
        """
        Methode zum Zeichhen von Buttons.

        """
        pass

    def drawContent(self):
        """
        Methode zum Zeichhen vom Inhalt des Fensters.

        """
        pygame.Surface.blit(pygame.display.get_surface(),self.bgd_image, [0, 0])

class ScreenStart(IScreen):
    """
        Model-Klasse des StartScreen
    """

    def __init__(self):
        """

        Konstruktor

        """
        pass

    def getObjects(self):
        """
        Liefert alle Planeten, die der derzeitige Screen beinhaltet, zurueck

        :return: objects[]
        """
        pass

#Main-Launch
if __name__ == '__main__':
    app = ComputeEventsStart()