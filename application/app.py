import sys

import settings
from PyQt5.QtWidgets import QApplication

from views.mainwindow import MainWindow


app = QApplication(sys.argv)
window = MainWindow()
