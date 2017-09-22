# Copyright (C) 2017  Eldar Khayrullin <eldar.khayrullin@mail.ru>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import numpy as np
import matplotlib
matplotlib.use("WxAgg")
from matplotlib.lines import Line2D
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
import matplotlib.pyplot as plt


class Oscilloscope:
    def __init__(self, widget):
        self._widget = widget
        self._widget.figure = plt.figure()
        self._widget.canvas = FigureCanvas(self._widget, -1,
                                           self._widget.figure)
        self._widget.ax = self._widget.figure.add_subplot(111)

    def close(self):
        plt.close()

    def plot(self):
        import random
        data = [random.random() for i in range(25)]
        self._widget.ax.hold(False)
        self._widget.ax.plot(data, '*-')
        self._widget.canvas.draw()
