#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Aimer Neige
# Mail: aimer.neige@aimerneige.com
# LICENSE: AGPLv3 (https://www.gnu.org/licenses/agpl-3.0.txt)

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        self.setGeometry(100, 100, 300, 200)
