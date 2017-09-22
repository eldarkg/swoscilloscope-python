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


import asyncore
import socket
import threading


_MAX_RECV = 8192


class Client(asyncore.dispatcher):
    def __init__(self, host, port, handler):
        asyncore.dispatcher.__init__(self)
        self._handler = handler
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))

        self._thread = threading.Thread(target=self._work_loop)
        self._thread.start()

    def _work_loop(self):
        asyncore.loop()

    def handle_connect(self):
        pass

    def handle_close(self):
        if self._thread:
            self._thread.join()
        self.close()

    def handle_read(self):
        msg = self.recv(_MAX_RECV)
        self._handler(msg)
