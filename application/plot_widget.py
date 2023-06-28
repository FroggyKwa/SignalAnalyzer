from __future__ import annotations

import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QMenu
from pyqtgraph import PlotWidget, InfiniteLine

from consts import SIGNAL_FRAGMENT_ACTION_TEXT
from utils import show_fragment_dialog


class MyPlotWidget(PlotWidget):
    def __init__(self, mainwindow, plot_data=None, frequency=None, **kwargs):
        super().__init__(**kwargs)
        self.mainwindow = mainwindow
        self.scene().sigMouseClicked.connect(self.mouse_clicked)
        self.border_left = None
        self.border_right = None
        self.line_1 = None
        self.line_2 = None
        self.plot_data = plot_data
        self.frequency = frequency
    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)
        fragment_action = contextMenu.addAction(SIGNAL_FRAGMENT_ACTION_TEXT)
        action = contextMenu.exec_(self.mapToGlobal(event.pos()))
        if action == fragment_action:
            show_fragment_dialog(self)

    def mouse_clicked(self, event):
        vb = self.plotItem.vb
        scene_coords = event.scenePos()
        if self.sceneBoundingRect().contains(scene_coords):
            mouse_point = vb.mapSceneToView(scene_coords)
            line = InfiniteLine(angle=90, movable=False, pen='r')
            line.setValue(mouse_point.x())
            if not self.border_left:
                self.border_left = mouse_point.x()
                self.line_1 = line
            elif not self.border_right:
                if self.border_left > mouse_point.x():
                    self.border_right = self.border_left
                    self.border_left = mouse_point.x()
                else:
                    self.border_right = mouse_point.x()
                self.line_2 = line
                self.open_scaled_plot()
            elif self.line_1 and self.line_2:
                # delete borders from plot
                self.removeItem(self.line_1)
                self.removeItem(self.line_2)

                self.border_left = mouse_point.x()
                self.line_1 = line
                self.line_2 = None
                self.border_right = None

            self.addItem(line)
            return mouse_point.x(), mouse_point.y()

    def open_scaled_plot(self, border_left=-1, border_right=-1):
        if border_left != -1 and border_right != -1:
            self.border_left = border_left
            self.border_right = border_right

        data = self.plot_data[1][int(self.border_left * self.frequency):int(self.border_right * self.frequency)]
        times = np.linspace(self.border_left,
                            self.border_right,
                            num=len(data))
        d = pg.plot(times, data, pen='r')
