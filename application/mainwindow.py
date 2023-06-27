from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QAction

from analyzer.analyzer import Analyzer
from application.consts import MAINWINDOW_PATH
from application.dialogs import AboutDialog
from application.utils import open_file_dialog


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(MAINWINDOW_PATH, self)
        self.analyzer = Analyzer()
        self.setupUi()
        self.show()

    def setupUi(self):
        self.menu_6.aboutToShow.connect(self.open_about_us_dialog)
        self.open_file_action = QAction("Открыть", self)
        self.menu.addAction(self.open_file_action)
        self.open_file_action.triggered.connect(lambda: open_file_dialog(self))

    def setup_signal_from_file(self, filename):
        self.analyzer.load_file(filename)

    @staticmethod
    def open_about_us_dialog():
        AboutDialog().exec()
