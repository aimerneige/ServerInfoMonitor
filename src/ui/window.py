#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Aimer Neige
# Mail: aimer.neige@aimerneige.com
# LICENSE: AGPLv3 (https://www.gnu.org/licenses/agpl-3.0.txt)

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from .titlebar import TitleBar

window_title = "Server Info Monitor"
window_width = 300
window_height = 200
window_opacity = 0.3

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
        self.setWindowTitle(window_title)
        self.setFixedWidth(window_width)
        self.setFixedHeight(window_height)
        self.setWindowOpacity(window_opacity)
        self.setStyleSheet("background-color: #000000;")
        self.setWindowFlag(Qt.FramelessWindowHint)

    def initUI(self) -> None:
        """
        Init UI widgets and layout.
        """
        self.initTitleBar()

    def initTitleBar(self) -> None:
        """
        Init the title bar.
        """
        self.titlebar = TitleBar(self, window_title)
        self.titlebar.setGeometry(0, 0, window_width, 20)

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
