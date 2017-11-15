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
from signal import *
from oscilloscope import Oscilloscope


_PLOT_PERIOD = 0.03
_PLOT_N_DIV = 10
_PLOT_SAMPLES_PER_DIV = 10


class MainFrame(gui.MainFrameBase):
    def __init__(self):
        gui.MainFrameBase.__init__(self, None)
        self._signals = []
        self._t = 0.
        self._on_change_time_div(None)
        self._on_change_setup_mul(None)
        self._plot_frame_tmr = wx.Timer(self)
        self._bind_events()
        # Frame auto-size
        self.SetInitialSize()
        self._connect()

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
                dt = float(fields[0])
                self._t += dt
                if self._t >= self._sample_time:
                    step = self._t * self._scale_per_sec
                    self._t = 0.
                    for i in range(len(fields) - 1):
                        self._signals[i].append([(step,
                            float(fields[i+1]) * self._vert_scale)])

    def _bind_events(self):
        self.Bind(wx.EVT_SHOW, self._on_show)
        self.Bind(wx.EVT_CLOSE, self._on_close)
        self.Bind(wx.EVT_TIMER, self._plot_frame, self._plot_frame_tmr)
        self.time_div_val.Bind(wx.EVT_CHOICE, self._on_change_time_div)
        self.time_div_unit.Bind(wx.EVT_CHOICE, self._on_change_time_div)
        self.setup_mul_op.Bind(wx.EVT_CHOICE, self._on_change_setup_mul)
        self.setup_mul_val.Bind(wx.EVT_CHOICE, self._on_change_setup_mul)

    def _on_show(self, evt):
        self._osc = Oscilloscope(self.scope)
        self._plot_frame_tmr.Start(_PLOT_PERIOD * 1000) # to ms
        evt.Skip()

    def _on_close(self, evt):
        self._plot_frame_tmr.Stop()
        self._client.close()
        self._osc.close()
        evt.Skip()

    def _on_change_time_div(self, evt):
        val = int(self._get_choice(self.time_div_val))
        mul = self._unit_to_mul(self._get_choice(self.time_div_unit))
        self._sec_per_div = val * mul

        self._sample_time = self._sec_per_div / _PLOT_SAMPLES_PER_DIV
        self._scale_per_sec = 1. / (_PLOT_N_DIV * self._sec_per_div)

    def _on_change_setup_mul(self, evt):
        isdiv = (self._get_choice(self.setup_mul_op) == "div")
        val = int(self._get_choice(self.setup_mul_val))
        if isdiv:
            val = 1. / val

        self._vert_scale = val

    def _plot_frame(self, *_):
        self._osc.plot(self._signals)

    def _get_choice(self, choice):
        return choice.GetString(choice.GetSelection())

    def _unit_to_mul(self, unit):
        if unit == "ns":
            return 1.E-9
        elif unit == "us":
            return 1.E-6
        elif unit == "ms":
            return 1.E-3
        elif unit == "s":
            return 1.
