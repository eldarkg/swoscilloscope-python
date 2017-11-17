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
from vispy import app, scene


_nsamples = 240


def set_nsamples(n):
    _nsamples = n

def get_nsamples(n):
    return _nsamples


class Signal:
    def __init__(self):
        self.reset()
        self.isenable = False
        self._vline = scene.Line()

    def get_samples(self):
        return self._samples

    def append(self, sample):
        def offset_time(a, base):
            return (a[0] - base, a[1])

        if self._samples.size != 0:
            sample[0] = (self._samples[-1][0] + sample[0][0], sample[0][1])
        else:
            sample[0] = (0.0, sample[0][1])

        self._samples = np.append(self._samples, sample, axis=0)

        #TODO time control > 1.0
        if self._samples.shape[0] > _nsamples:
            self._samples = self._samples[1:]
            base = self._samples[0][0]
            self._samples = np.apply_along_axis(offset_time, 1, self._samples,
                                                base)

    def reset(self):
        self._samples = np.zeros((0, 2), dtype=np.float64)

    def enable(self):
        self.isenable = True

    def disable(self):
        self.isenable = False
        self.reset()
        self._vline.set_data(pos=self._samples)

    def plot(self, scene):
        if self.isenable:
            self._vline.parent = scene
            self._vline.set_data(pos=self._samples)
