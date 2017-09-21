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
import wx

import gui.main_frame_base as gui


class MainFrame(gui.MainFrameBase):
    def __init__(self):
        gui.MainFrameBase.__init__(self, None)
        self._init_scope()
        self._bind_events()
        # Frame auto-size
        self.SetInitialSize()

    def _init_scope(self):
        self.scope.figure = plt.figure()
        self.scope.canvas = FigureCanvas(self, -1, self.scope.figure)
        self.scope.ax = self.scope.figure.add_subplot(111)

    def _bind_events(self):
        self.Bind(wx.EVT_SHOW, self._on_show)
        self.Bind(wx.EVT_CLOSE, self._on_close)
        self.Bind(wx.EVT_BUTTON, self._plot_frame)

    def _on_show(self, evt):
        evt.Skip()

    def _on_close(self, evt):
        plt.close()
        evt.Skip()

    def _plot_frame(self, *_):
        import random
        data = [random.random() for i in range(25)]
        self.scope.ax.hold(False)
        self.scope.ax.plot(data, '*-')
        self.scope.canvas.draw()
