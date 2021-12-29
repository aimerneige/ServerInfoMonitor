#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Aimer Neige
# Mail: aimer.neige@aimerneige.com
# LICENSE: AGPLv3 (https://www.gnu.org/licenses/agpl-3.0.txt)

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

widget_height = 20

margin_left = 1
margin_right = 1
margin_top = 1
margin_button = 1

close_button_width = 20
close_button_height = 20

class TitleBar(QWidget):
    def __init__(self, parent: QWidget, title: str) -> None:
        super().__init__(parent)
        self.title = title
        self.initUI()

    def initUI(self) -> None:
        """
        Init UI widgets and layout.
        """
        self.setFixedHeight(widget_height)
        self.setStyleSheet("color: #ffffff;")

        self.initTitleLabel()
        self.initCloseButton()

        hbox = QHBoxLayout(self)
        hbox.setSpacing(0)
        hbox.setContentsMargins(margin_left, margin_top, margin_right, margin_button)
        hbox.addWidget(self.label)
        hbox.addStretch(1)
        hbox.addWidget(self.closeButton)

        self.setLayout(hbox)

    def initTitleLabel(self) -> None:
        self.label = QLabel(self.title, self)
        self.label.setAlignment(Qt.AlignCenter)

    def initCloseButton(self) -> None:
        self.closeButton = QPushButton("X", self)
        self.closeButton.setFixedSize(close_button_width, close_button_height)
        self.closeButton.clicked.connect(self.closeButtonClicked)

    @pyqtSlot()
    def closeButtonClicked(self) -> None:
        """
        Close button clicked.
        """
        self.parent().close()
