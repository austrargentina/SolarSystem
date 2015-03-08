__author__ = 'Daniel'

from MVC.AbstractMVC import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

import sys

class ComputeEventsPlanets(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.myForm = Ui_SolarSystem()
        self.myForm.setupUi(self)

    def computeKeyboardEvents(self):
        pass

    def computeMouseEvents(self):
        pass

class DrawScreenPlanets(IDrawScreen):

    def __init__(self):
        pass

    def drawButtons(self):
        pass

    def drawContent(self):
        pass

class Ui_SolarSystem(object):
    def setupUi(self, SolarSystem):
        SolarSystem.setObjectName("SolarSystem")
        SolarSystem.resize(800, 600)
        SolarSystem.setMinimumSize(QtCore.QSize(800, 600))
        SolarSystem.setMaximumSize(QtCore.QSize(800, 600))
        SolarSystem.setAutoFillBackground(False)
        self.gridLayoutWidget = QtWidgets.QWidget(SolarSystem)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.Content = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.Content.setContentsMargins(0, 0, 0, 0)
        self.Content.setObjectName("Content")

        self.retranslateUi(SolarSystem)
        QtCore.QMetaObject.connectSlotsByName(SolarSystem)

    def retranslateUi(self, SolarSystem):
        _translate = QtCore.QCoreApplication.translate
        SolarSystem.setWindowTitle(_translate("SolarSystem", "SolarSystem"))


class ScreenPlanets(IScreen):

    def __init__(self):
        pass

    def getObjects(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = ComputeEventsPlanets()
    c.show()
    sys.exit(app.exec_())