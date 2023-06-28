import pyqtgraph
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
        self.plots = []
        self.analyzer = Analyzer()
        self.setupUi()
        self.show()

    def setupUi(self):
        self.menu_6.aboutToShow.connect(self.open_about_us_dialog)
        self.open_file_action = QAction("Открыть", self)
        self.menu.addAction(self.open_file_action)
        self.open_file_action.triggered.connect(lambda: open_file_dialog(self))

    def setup_signal_from_file(self, filename):
        self.add_data_to_plots(self.analyzer.load_file(filename))

    def add_data_to_plots(self, plots):
        for name, plot in plots.items():
            self.plots.append(pyqtgraph.PlotWidget())
            self.graphs_layout.addWidget(self.plots[-1])
            self.plots[-1].plot(*plot, pen='b')
            self.plots[-1].setLabel(axis='bottom', text=name)

    @staticmethod
    def open_about_us_dialog():
        AboutDialog().exec()
