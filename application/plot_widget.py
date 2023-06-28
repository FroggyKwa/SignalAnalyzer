from __future__ import annotations

import numpy as np
import pyqtgraph as pg
from pyqtgraph import PlotWidget, InfiniteLine


class MyPlotWidget(PlotWidget):
    def __init__(self, mainwindow, plot_data=None, frequency=None, **kwargs):
        super().__init__(**kwargs)
        self.mainwindow = mainwindow
        self.scene().sigMouseClicked.connect(self.mouse_clicked)
        self.border_left: tuple[None | float, None | float] = (None, None)
        self.border_right: tuple[None | float, None | float] = (None, None)
        self.plot_data = plot_data
        self.frequency = frequency

    def mouse_clicked(self, event):
        vb = self.plotItem.vb
        scene_coords = event.scenePos()
        if self.sceneBoundingRect().contains(scene_coords):
            mouse_point = vb.mapSceneToView(scene_coords)
            line = InfiniteLine(angle=90, movable=False, pen='r')
            line.setValue(mouse_point.x())
            if not self.border_left[1]:
                self.border_left = mouse_point.x(), line
            elif not self.border_right[1]:
                self.border_right = mouse_point.x(), line
                self.open_scaled_plot()
            elif self.border_right[1] and self.border_left[1]:
                # delete borders from plot
                self.removeItem(self.border_left[1])
                self.removeItem(self.border_right[1])

                self.border_left = mouse_point.x(), line
                self.border_right = (None, None)

            self.addItem(line)
            return mouse_point.x(), mouse_point.y()

    def open_scaled_plot(self):
        print(self.border_left[0], self.border_right[0])
        data = self.plot_data[1][int(self.border_left[0]*self.frequency):int(self.border_right[0]*self.frequency)]
        times = np.linspace(self.border_left[0],
                            self.border_right[0],
                            num=len(data))
        d = pg.plot(times, data, pen='r')
