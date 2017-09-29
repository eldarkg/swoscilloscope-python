#!/usr/bin/env python3
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


import atexit
import socket
import time


SERVER_PORT = 2000
PERIOD = 0.5


def close():
    print('Closing')
    server.close()


atexit.register(close)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', SERVER_PORT))
server.listen(1)

while True:
    client, addr = server.accept()
    t = 0.0
    print('Connected ', addr)

    client.sendall(b'# sig0 sig1\n')
    while True:
        b = bytes('{0} 0.1 0.2\n'.format(t), encoding='ascii')
        client.sendall(b)
        time.sleep(PERIOD)
        t += PERIOD
