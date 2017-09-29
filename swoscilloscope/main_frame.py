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


import wx

import client
import gui.main_frame_base as gui
from oscilloscope import *
from signal import *


class MainFrame(gui.MainFrameBase):
    def __init__(self):
        gui.MainFrameBase.__init__(self, None)
        self._bind_events()
        # Frame auto-size
        self.SetInitialSize()
        self._connect()
        self._signals = []

    def _connect(self):
        self._client = client.Client('localhost', 2000, self._rcv_handler)

    def _rcv_handler(self, msg):
        entries = msg.decode().split(sep='\n')
        for entry in entries:
            if entry == '':
                break

            fields = entry.split()
            if fields[0] == '#':
                self._signals = []
                for fname in fields[1:]:
                    #TODO change header
                    self._signals.append(Signal())
            else:
                t = float(fields[0])
                for i in range(len(fields) - 1):
                    print(fields[i+1])
                    self._signals[i].append([(t, float(fields[i+1]))])

    def _bind_events(self):
        self.Bind(wx.EVT_SHOW, self._on_show)
        self.Bind(wx.EVT_CLOSE, self._on_close)
        self.Bind(wx.EVT_BUTTON, self._plot_frame)

    def _on_show(self, evt):
        self._osc = Oscilloscope(self.scope)
        evt.Skip()

    def _on_close(self, evt):
        self._client.close()
        self._osc.close()
        evt.Skip()

    def _plot_frame(self, *_):
        self._osc.plot(self._signals)
