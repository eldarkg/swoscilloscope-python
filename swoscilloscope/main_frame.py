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


import matplotlib
matplotlib.use("WxAgg")
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
import wx

import gui.main_frame_base as gui


_UPD_INTERVAL = 16

class MainFrame(gui.MainFrameBase):
    def __init__(self):
        gui.MainFrameBase.__init__(self, None)

        self._init_scope()
        # Frame auto-size
        self.SetInitialSize()

        self._bind_events()

    def _init_scope(self):
        self.scope.figure = plt.figure()
        self.scope.canvas = FigureCanvas(self, -1, self.scope.figure)
        ani = animation.FuncAnimation(self.scope.figure, self._upd_plot,
                                      self._pre_plot, interval=_UPD_INTERVAL,
                                      blit=True)

    def _bind_events(self):
        self.Bind(wx.EVT_SHOW, self._on_show)
        self.Bind(wx.EVT_CLOSE, self._on_close)

    def _on_show(self, evt):
        evt.Skip()

    def _on_close(self, evt):
        plt.close()
        evt.Skip()

    def _pre_plot(self):
        import random
        data = [random.random() for i in range(25)]
        return data

    def _upd_plot(self, data):
        ax = self.scope.figure.add_subplot(111)
        ax.hold(False)
        ax.plot(data, '*-')
        self.scope.canvas.draw()
