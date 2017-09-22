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


def close():
    print('Closing')
    server.close()


atexit.register(close)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', SERVER_PORT))
server.listen(1)

while True:
    client, addr = server.accept()
    print('Connected ', addr)

    while True:
        client.sendall(b'0.1 0.3 0.4')
        time.sleep(0.5)
