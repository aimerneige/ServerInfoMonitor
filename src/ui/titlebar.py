#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Aimer Neige
# Mail: aimer.neige@aimerneige.com
# LICENSE: AGPLv3 (https://www.gnu.org/licenses/agpl-3.0.txt)

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class TitleBar(QWidget):
    def __init__(self, parent: QWidget, title: str) -> None:
        super().__init__(parent)
        self.title = title
        self.initUI()

    def initUI(self) -> None:
        """
        Init UI widgets and layout.
        """
        self.setFixedHeight(20)
        self.setStyleSheet("color: #ffffff;")

        self.initTitleLabel()
        self.initCloseButton()

        hbox = QHBoxLayout(self)
        hbox.setSpacing(0)
        hbox.setContentsMargins(1, 1, 1, 1)
        hbox.addWidget(self.label)
        hbox.addStretch(1)
        hbox.addWidget(self.closeButton)

        self.setLayout(hbox)

    def initTitleLabel(self) -> None:
        self.label = QLabel(self.title, self)
        self.label.setAlignment(Qt.AlignCenter)

    def initCloseButton(self) -> None:
        self.closeButton = QPushButton("X", self)
        self.closeButton.setFixedSize(20, 20)
        self.closeButton.clicked.connect(self.closeButtonClicked)

    @pyqtSlot()
    def closeButtonClicked(self) -> None:
        """
        Close button clicked.
        """
        self.parent().close()
