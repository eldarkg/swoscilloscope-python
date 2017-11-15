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


from vispy import app, scene


class Oscilloscope:
    def __init__(self, widget):
        self._canvas = scene.SceneCanvas(show=True,
                                         size=widget.GetSize(),
                                         keys='interactive', parent=widget)
        grid = self._canvas.central_widget.add_grid()
        self._view = grid.add_view(row=0, col=0, camera='panzoom')
        self._view.camera.rect = (0., -0.5, 1., 1.)
        scene.GridLines(color=(1, 1, 1, 0.5), parent=self._view.scene)

    def close(self):
        ...

    def plot(self, signals):
        for sig in signals:
            sig.plot(self._view.scene)
