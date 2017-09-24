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
import threading
from vispy import app, scene


class Oscilloscope:
    def __init__(self):
        self._canvas = scene.SceneCanvas(keys='interactive', show=True)
        grid = self._canvas.central_widget.add_grid()
        self._view = grid.add_view(row=0, col=0, camera='panzoom')
        self._view.camera.rect = (-1., -1., 2., 2.)
        scene.GridLines(color=(1, 1, 1, 0.5), parent=self._view.scene)

        self._vispy_thread = threading.Thread(target=self._vispy_thread_func)
        self._vispy_thread.start()

    def _vispy_thread_func(self):
        app.run()

    def close(self):
        app.close()
        self._vispy_thread.join()

    def plot(self):
        self._view.camera.rect = (-1., -1., 2., 2.)
        lines = scene.Line(pos=np.array(((0.,0.),(2.,2.))),
                           parent=self._view.scene)
