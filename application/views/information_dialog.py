import datetime

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QHeaderView

from consts import INFORMATION_PATH


class InformationDialog(QDialog):
    def __init__(self,
                 n_channels=None,
                 n_signals=None,
                 frequency=None,
                 start_datetime=None,
                 ):
        super(QDialog, self).__init__()
        uic.loadUi(INFORMATION_PATH, self)
        self.n_channels = n_channels
        self.n_signals = n_signals
        self.frequency = frequency
        self.start_datetime = start_datetime
        self.duration = self.n_signals / frequency
        self.end_datetime = datetime.timedelta(seconds=self.duration) + self.start_datetime
        self.setupUi()

    def setupUi(self):
        COLUMNS = 2
        ROWS = 6
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setColumnCount(COLUMNS)
        self.table.setRowCount(ROWS)
        self.table.setHorizontalHeaderLabels(['Информация', 'Значение'])

        info = [
            {'Общее число каналов': self.n_channels},
            {'Общее количество отсчетов': self.n_signals},
            {'Частота дискретизации': self.frequency},
            {'Дата и время начала записи': self.start_datetime},
            {'Дата и время окончания записи': self.end_datetime},
            {'Длительность': self.duration}
        ]
        cnt = 0
        for i in info:
            for name, value in i.items():
                self.table.setItem(cnt, 0, QTableWidgetItem(str(name)))
                self.table.setItem(cnt, 1, QTableWidgetItem(str(value)))
            cnt += 1
