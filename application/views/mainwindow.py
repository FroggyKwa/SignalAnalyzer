import pyqtgraph
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QAction, QMessageBox

from application.consts import MAINWINDOW_PATH, OPEN_ACTION_TEXT, SIGNAL_INFORMATION_ACTION_TEXT
from application.dialogs import AboutDialog
from application.utils import open_file_dialog, show_signal_information, open_warning_messagebox
from signal.signal import Signal


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(MAINWINDOW_PATH, self)
        self.setMinimumHeight(800)
        self.plots = []
        self.signal = Signal()
        self.setupUi()
        self.show()

    def setupUi(self):
        # About us menu trigger
        self.menu_6.aboutToShow.connect(self.open_about_us_dialog)

        # Open file menu action
        self.open_file_action = QAction(OPEN_ACTION_TEXT, self)
        self.menu.addAction(self.open_file_action)
        self.open_file_action.triggered.connect(lambda: open_file_dialog(self))

        # Analyzing menu action

        self.signal_information_action = QAction(SIGNAL_INFORMATION_ACTION_TEXT, self)
        self.menu_3.addAction(self.signal_information_action)
        self.signal_information_action.triggered.connect(lambda: show_signal_information(
            n_channels=self.signal.n_channels,
            n_signals=self.signal.n_signals,
            frequency=self.signal.frequency,
            start_datetime=self.signal.start_datetime,
        ))

    def setup_signal_from_file(self, filename):
        try:
            self.add_data_to_plots(self.signal.load_file(filename))
        except ValueError:
            open_warning_messagebox(title='Ошибка!',
                                    text='Произошла ошибка при чтении файла! \nНеверный формат!')

    def add_data_to_plots(self, plots):
        for name, plot in plots.items():
            self.plots.append(pyqtgraph.PlotWidget())
            self.graphs_layout.addWidget(self.plots[-1])
            self.plots[-1].plot(*plot, pen='b')
            self.plots[-1].setLabel(axis='bottom', text=name)
            self.plots[-1].setFixedSize(self.size().width() - 50, (self.size().height() - 70) / len(plots) - 10)

    def resizeEvent(self, event):
        for plot in self.plots:
            plot.setFixedSize(self.size().width() - 50, (self.size().height() - 70) / len(self.plots) - 10)

    @staticmethod
    def open_about_us_dialog():
        AboutDialog().exec()
