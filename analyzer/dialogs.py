from PyQt5 import uic

from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel

from analyzer import consts
from analyzer.consts import ABOUT_PATH


class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(ABOUT_PATH, self)
        self.setWindowTitle(consts.ABOUT_US_TITLE)
        self.setupUi()
        self.show()

    def setupUi(self):
        self.confirm.clicked.connect(self.close)
