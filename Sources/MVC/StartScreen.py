from MVC.PlanetenScreen import ComputeEventsPlanets

__author__ = 'Martin'

#Import der relevanten Klassen fuer Pygame und PyOpenGL
import pygame


from MVC.AbstractMVC import *

class ComputeEventsStart(IComputeEvents):
    """
     Ist die Controller-Klasse des StartScreens und beinhaltet die Infos ueber das Display

    """

    screen = None
    screenContent = None

    def __init__(self):

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
        if event.key == pygame.K_SPACE:
            pygame.quit()
            ComputeEventsPlanets()

    def computeMouseEvents(self,event):

         #Falls das Fenster geschlossen werden soll
        if event.type == pygame.QUIT:
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
        #Zuweisen des uebermittelten Models
        self.screenContent = screenContent

        #Displaygroesse einstellen
        display = (800, 600)
        pygame.display.set_mode(display)

        #Fenster Titel einstellen
        pygame.display.set_caption("Solarsystem Menü")

        #Hintergrundbild laden
        self.bgd_image = pygame.image.load("../../Images/Sunrise-Earth-In-Space.jpg").convert()

    def drawButtons(self):
        pass

    def drawContent(self):

        #Hintergrundbild setzen
        pygame.Surface.blit(pygame.display.get_surface(),self.bgd_image, [0, 0])





class ScreenStart(IScreen):

    def __init__(self):
     pass

    def getObjects(self):
        pass

app = ComputeEventsStart()