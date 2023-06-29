from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QAction

from application.consts import MAINWINDOW_PATH, OPEN_ACTION_TEXT, SIGNAL_INFORMATION_ACTION_TEXT, ERROR_TITLE, \
    ERROR_TEXT, SINUSOID_NAME, SAW_NAME, MEANDER_NAME, DELAYED_SINGLE_LEAP_NAME, DELAYED_SINGLE_IMPULSE_NAME, \
    DECREASING_EXP
from application.dialogs import open_warning_messagebox
from application.utils import open_file_dialog, show_signal_information, open_about_us_dialog, \
    open_delayed_single_impulse_dialog, add_data_to_plots, open_delayed_single_leap_dialog, open_decreasing_exp_dialog
from application.utils import open_meander_dialog, open_saw_dialog, open_sinusoid_dialog
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
        self.action_list = []
        # About us menu trigger
        self.menu_6.aboutToShow.connect(open_about_us_dialog)

        # Open file menu action
        self.open_file_action = QAction(OPEN_ACTION_TEXT, self)
        self.menu.addAction(self.open_file_action)
        self.open_file_action.triggered.connect(
            lambda: self.clear_layout(layout=self.graphs_layout) and open_file_dialog(self))

        self.sinusoid_action = QAction(SINUSOID_NAME, self)
        self.meander_action = QAction(MEANDER_NAME, self)
        self.saw_action = QAction(SAW_NAME, self)
        self.menu_2.addAction(self.meander_action)
        self.menu_2.addAction(self.sinusoid_action)
        self.menu_2.addAction(self.saw_action)

        self.sinusoid_action.triggered.connect(open_sinusoid_dialog)
        self.meander_action.triggered.connect(open_meander_dialog)
        self.saw_action.triggered.connect(open_saw_dialog)

        self.delayed_single_impulse_action = QAction(DELAYED_SINGLE_IMPULSE_NAME, self)
        self.delayed_single_impulse_action.triggered.connect(
            lambda: open_delayed_single_impulse_dialog(self)
        )
        self.delayed_single_leap_action = QAction(DELAYED_SINGLE_LEAP_NAME, self)
        self.delayed_single_leap_action.triggered.connect(open_delayed_single_leap_dialog)
        self.dicreasing_exp = QAction(DECREASING_EXP, self)
        self.dicreasing_exp.triggered.connect(open_decreasing_exp_dialog)

        self.open_sinusoid = QAction(SINUSOID_NAME, self)
        self.open_meander = QAction(MEANDER_NAME, self)
        self.saw = QAction(SAW_NAME, self)

        self.menu_2.addAction(self.delayed_single_impulse_action)
        self.menu_2.addAction(self.delayed_single_leap_action)
        self.menu_2.addAction(self.dicreasing_exp)


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
            add_data_to_plots(self, self.signal.load_file(filename))
        except ValueError:
            open_warning_messagebox(title=ERROR_TITLE,
                                    text=ERROR_TEXT)

    def resizeEvent(self, event):
        for plot in self.plots:
            plot.setFixedSize(self.size().width() - 50, (self.size().height() - 70) // len(self.plots) - 10)

    @staticmethod
    def clear_layout(layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        return True
