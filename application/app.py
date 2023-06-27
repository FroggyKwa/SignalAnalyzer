import sys

from PyQt5.QtWidgets import QApplication

from application.mainwindow import MainWindow


app = QApplication(sys.argv)
window = MainWindow()
