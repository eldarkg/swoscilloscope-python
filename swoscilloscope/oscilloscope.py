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


class Oscilloscope:
    def __init__(self, nx, ny, widget):
        ratio = nx / ny
        self._canvas = scene.SceneCanvas(show=True,
                                         size=widget.GetSize(),
                                         keys='interactive',
                                         parent=widget)
        grid = self._canvas.central_widget.add_grid()
        self._view = grid.add_view(row=0, col=0, camera='panzoom')
        self._view.camera.rect = (0., -0.5, ratio, 1.)

        for p in np.linspace(0., ratio, num=5*nx+1):
            scene.InfiniteLine(pos=p, color=(0.3, 0.3, 0.3, 1.), vertical=True, parent=self._view.scene)
        for p in np.linspace(-0.5, 0.5, num=5*ny+1):
            if p == 0.:
                scene.InfiniteLine(pos=p, color=(0.5, 0.5, 0.5, 1.), vertical=False, parent=self._view.scene)
            else:
                scene.InfiniteLine(pos=p, color=(0.3, 0.3, 0.3, 1.), vertical=False, parent=self._view.scene)

        c_x = np.linspace(0., ratio, num=nx+1)
        c_y = np.linspace(-0.5, 0.5, num=ny+1)
        grid = np.array(np.meshgrid(c_x, c_y, indexing='ij')).T
        grid = grid.reshape((nx+1)*(ny+1), 2)
        scene.Markers(pos=grid, symbol='square', size=4, face_color=(0.6, 0.6, 0.6, 1.), parent=self._view.scene)

        #scene.Line(pos=np.array([[0., 0.], [ratio, 0.]]), color=(0.5, 0.5, 0.5, 1.), width=1, parent=self._view.scene)
        #scene.Line(pos=np.array([[0.75, -0.5], [0.75, 0.5]]), color=(0.5, 0.5, 0.5, 1.), width=1, parent=self._view.scene)

        #scene.GridLines(scale=(1.25, 1.25), color=(0.5, 0.5, 0.5, 1.), parent=self._view.scene)
        #scene.GridLines(scale=(0.3, 0.3), color=(0.5, 0.5, 0.5, 0.5), parent=self._view.scene)

    def close(self):
        ...

    def reset(self, signals):
        for sig in signals:
            sig.reset()

    def plot(self, signals):
        for sig in signals:
            sig.plot(self._view.scene)
