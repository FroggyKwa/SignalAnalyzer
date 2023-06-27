from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from analyzer.consts import MAINWINDOW_PATH
from analyzer.dialogs import AboutDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(MAINWINDOW_PATH, self)
        self.setupUi()
        self.show()

    def setupUi(self):
        self.menu_6.aboutToShow.connect(self.openDialog)

    def openDialog(self):
        AboutDialog().exec()
