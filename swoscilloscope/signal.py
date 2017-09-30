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


_nsamples = 32


def set_nsamples(n):
    _nsamples = n

def get_nsamples(n):
    return _nsamples


class Signal:
    def __init__(self):
        self._samples = np.zeros((0, 2), dtype=np.float64)
        self._vline = scene.Line()

    def get_samples(self):
        return self._samples

    def append(self, samples):
        #TODO time -= (first sample time)
        self._samples = np.append(self._samples, samples, axis=0)
        #TODO check nsamples strict

    def plot(self, scene):
        self._vline.parent = scene
        self._vline.set_data(pos=self._samples)
