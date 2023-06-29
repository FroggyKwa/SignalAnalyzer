from matplotlib import pyplot as plt
from numpy import linspace, histogram as np_histogram


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
    return min(p[1])


def maximum_value(p):
    return max(p[1])


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
    # return y, x
#
# import random
# print(histogram(([], [random.randint(0, 100) for i in range(100000)])))
#
#

