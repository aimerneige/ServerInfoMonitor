#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Aimer Neige
# Mail: aimer.neige@aimerneige.com
# LICENSE: AGPLv3 (https://www.gnu.org/licenses/agpl-3.0.txt)

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

_title = "Server Info Monitor"
_width = 300
_height = 200
_opacity = 0.3

class Window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initWindow()
        self.initUI()
        self.center()

    def initWindow(self) -> None:
        """
        Init window properties.
        """
        self.setWindowTitle(_title)
        self.setFixedWidth(_width)
        self.setFixedHeight(_height)
        self.setWindowOpacity(_opacity)
        self.setWindowFlag(Qt.FramelessWindowHint)

    def initUI(self) -> None:
        """
        Init UI widgets and layout.
        """
        self.initHelloWorldLabel()

    def initHelloWorldLabel(self) -> None:
        """
        Init the Hello World label.
        """
        self.label = QLabel("Hello World", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(0, 0, 300, 200)
        self.label.setStyleSheet("background-color: #000000; color: #ffffff;")

    def center(self) -> None:
        """
        Center the window on the screen.
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # override keyboard events for exiting the application
    def keyPressEvent(self, event: QKeyEvent) -> None:
        """
        Handle key press events.
        """
        if event.key() == Qt.Key_Escape:
            self.close()

    # override mouse events for moving the window
    def mousePressEvent(self, event: QMouseEvent) -> None:
        """
        Handle mouse press events.
        """
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        """
        Handle mouse move events.
        """
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
