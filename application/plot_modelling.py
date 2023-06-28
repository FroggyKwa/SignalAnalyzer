from math import pi, sin, radians, exp, cos
from enum import Enum

import numpy as np


class PlotType(Enum):
    delayed_single_impulse = 0
    delayed_single_leap = 1
    decreasing_exp = 2
    sinusoid = 3
    meander = 4
    saw = 5
    exp_envelope = 6
    balance_envelope = 7
    tonal_envelope = 8
    linear_frequency_modulation = 9


def model_plot(plottype: PlotType, start: int = 0, end: int = 60, frequency: float = 1, n0: int = 0, a: float = 1,
               fi: float = 0, L: float = 1, t: float = 1,
               fn: float = 0, fo: float = 0, m: float = 0, fk: float = 0, w: float = 0):
    n = int((end - start) * frequency)
    times = np.linspace(start, end, num=n)
    match plottype:
        case PlotType.delayed_single_impulse:
            return times, [1 if i == n0 else 0 for i in range(n)]
        case PlotType.delayed_single_leap:
            return times, [1 if i >= n0 else 0 for i in range(n)]
        case PlotType.decreasing_exp:
            return times, [a ** i for i in range(n)]
        case PlotType.sinusoid:
            return times, [a * sin(radians(i*w + fi)) for i in range(n)]
        case PlotType.meander:
            return times, [1 if i % L < L/2 else -1 for i in range(n)]
        case PlotType.saw:
            return times, [(i % L) / L for i in range(n)]
        case PlotType.exp_envelope:
            return times, [a * exp(-times[i] / t) * cos(radians(2 * pi * fn * times[i] + fi)) for i in range(n)]
        case PlotType.balance_envelope:
            return times, [a * cos(radians(2 * pi * fo * times[i])) * cos(radians(2 * pi * fn * times[i] + fi)) for i in range(n)]
        case PlotType.tonal_envelope:
            return times, [a * (1 + m * cos(radians(2 * pi * fo * times[i]))) * cos(radians(2 * pi * fn * times[i] + fi)) for i in range(n)]
        case PlotType.linear_frequency_modulation:
            return times, [a * cos(radians(2 * pi * (fo + (fk - fo) * times[i] / (start - end)) * times[i] + fi)) for i in range(n)]