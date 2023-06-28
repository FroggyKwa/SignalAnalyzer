from PyQt5 import uic

from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel
from pyqtgraph import PlotWidget
import pyqtgraph as pg

from application import consts
from application.consts import ABOUT_PATH, SCALED_PLOT_PATH


class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(ABOUT_PATH, self)
        self.setWindowTitle(consts.ABOUT_US_TITLE)
        self.setupUi()
        self.show()

    def setupUi(self):
        self.confirm.clicked.connect(self.close)