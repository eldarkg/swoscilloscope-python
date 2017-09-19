#!/usr/bin/env python3
#
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


import sys
import wx

import main_frame


NDEBUG = True


if __name__ == '__main__':
    if '-d' in sys.argv:
        NDEBUG = False

    app = wx.App(False)

    if not NDEBUG:
        import wx.lib.inspection
        wx.lib.inspection.InspectionTool().Show()
        main_frame.NDEBUG = NDEBUG

    main_frame.MainFrame().Show()

    app.MainLoop()
