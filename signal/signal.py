import datetime

import numpy as np
from plot_modelling import PlotType


class Signal:
    def __init__(self, file=None, n_channels=None, n_signals=None, frequency=None):
        self.file = file
        self.n_channels = n_channels
        self.n_signals = n_signals
        self.frequency = frequency
        self.channels = None
        self.start_datetime = None
        self.names = None
        self.duration = None
        self.models = {data.name: 0 for data in PlotType}

    def load_file(self, filename):
        """
        Load file and pass data to signal
        :param filename: name of file to scan
        :return: None
        """
        with open(filename, 'r') as file:

            # next(file) - for skipping line comments. I think it is faster than reading line from file
            next(file)
            self.n_channels = int(file.readline().strip())
            next(file)
            self.n_signals = int(file.readline().strip())
            next(file)
            self.frequency = float(file.readline().strip())
            next(file)
            start_date = file.readline().strip()
            next(file)
            start_time = file.readline().strip()
            self.start_datetime = datetime.datetime.strptime(' '.join([start_date, start_time]),
                                                             '%d-%m-%Y %H:%M:%S.%f')
            next(file)
            self.names = file.readline().strip().split(';')

            self.channels = [[] for _ in range(self.n_channels)]

            self.duration = self.n_signals / self.frequency

            for line in file:
                for index, data in enumerate(line.strip().split(' ')):
                    self.channels[index % len(self.channels)].append(float(data))

            times = np.linspace(0, self.n_signals / self.frequency, num=self.n_signals)
            plots = {
                self.names[i]: (times, self.channels[i])
                for i in range(len(self.channels))
            }
            return plots
