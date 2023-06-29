import matplotlib
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QDialog, QMainWindow
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from consts import HISTOGRAM_PATH

matplotlib.use('Qt5Agg')


def average(p):
    return sum(p[1]) / len(p[1])


def dispersion(p):
    return sum([(i - average(([], p))) ** 2 / len(p[1]) for i in p[1]])


def standard_deviation(p):  # среднеквадратичное отклонение
    return dispersion(p) ** 0.5


def coef_of_variation(p):
    return standard_deviation(p) / average(p)


def skewness(p):  # коэффициент ассиметрии
    return sum([(i - average(([], p))) ** 3 / len(p[1]) for i in p[1]]) / standard_deviation(p) ** 3


def excess_kurtosis(p):
    return sum([(i - average(([], p))) ** 4 / len(p[1]) for i in p[1]]) / standard_deviation(p) ** 4 - 3


def minimal_value(p):
    return min(p)


def maximum_value(p):
    return max(p)


def _quantile(p, a):
    values = sorted(p[1])
    k = int(a * (len(values) - 1))
    if k + 1 < a * len(values):
        return values[k + 1]
    elif k + 1 == a * len(values):
        return (values[k] + values[k + 1]) / 2
    else:
        return values[k]


def quantile_005(p):
    return _quantile(p, 0.05)


def quantile_095(p):
    return _quantile(p, 0.95)


def median(p):
    return _quantile(p, 0.5)


def histogram(p, h: float = 0.1):
    start, end = int(minimal_value(p)), int(maximum_value(p))
    c = 0  # counter
    intervals = []
    while start + c * h < end:
        intervals.append(start + c * h)
        c += 1
    c += 1
    intervals.append(start + c * h)
    # y, x = np_histogram(p[1], bins=intervals)
    plt.hist(p[1], bins=intervals)
    plt.show()


matplotlib.use('QT5Agg')

# Matplotlib canvas class to create figure
import matplotlib

matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class HistoWidget(QDialog):

    def __init__(self, plot, h=0.1, *args, **kwargs):
        super(QWidget, self).__init__(*args, **kwargs)
        self.plot = plot
        uic.loadUi(HISTOGRAM_PATH, self)

        sc = MplCanvas(self, width=5, height=4, dpi=100)
        start, end = int(minimal_value(plot)), int(maximum_value(plot))
        c = 0  # counter
        intervals = []
        while start + c * h < end:
            intervals.append(start + c * h)
            c += 1
        c += 1
        intervals.append(start + c * h)
        # y, x = np_histogram(p[1], bins=intervals)
        sc.axes.hist(plot, bins=intervals)
        self.base_layout.addWidget(sc)

        self.show()
