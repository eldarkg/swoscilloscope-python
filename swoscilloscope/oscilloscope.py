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

        for p in np.linspace(0., ratio, num=nx+1):
            scene.InfiniteLine(pos=p, color=(1., 1., 1., 0.2), vertical=True, parent=self._view.scene)
        for p in np.linspace(0., 1., num=ny+1):
            scene.InfiniteLine(pos=p-0.5, color=(1., 1., 1., 0.2), vertical=False, parent=self._view.scene)

        '''
        scene.Line(pos=np.array([[0., 0.], [1., 0.]]), color=(1., 1., 1., 0.5), width=1, parent=self._view.scene)
        scene.Line(pos=np.array([[0.5, -0.5], [0.5, 0.5]]), color=(1., 1., 1., 0.5), width=1, parent=self._view.scene)

        c_x = np.linspace(0., 1., num=11)
        c_y = np.linspace(-0.5, 0.5, num=11)
        grid = np.array(np.meshgrid(c_x, c_y, indexing='ij')).T
        grid = grid.reshape(11 * 11, 2)
        scene.Markers(pos=grid, symbol='disc', size=5, face_color=(1., 1., 1., 0.2), parent=self._view.scene)
        '''

        #scene.Markers(pos=np.array([[0., 0.], [0., 0.02]]), symbol='disc', size=3, parent=self._view.scene)
        #scene.GridLines(color=(1., 1., 1., 1.), parent=self._view.scene)
        #scene.GridLines(scale=(0.3, 0.3), color=(1., 1., 1., 1.), parent=self._view.scene)

    def close(self):
        ...

    def reset(self, signals):
        for sig in signals:
            sig.reset()

    def plot(self, signals):
        for sig in signals:
            sig.plot(self._view.scene)
