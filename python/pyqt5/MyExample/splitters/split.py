#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
#from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame,
#    QSplitter, QStyleFactory, QApplication, QTabWidget, QLabel)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class Examp(QWidget):

    def __init__(self):
        super().__init__()

        hbox = QHBoxLayout()


        left = QTabWidget()
        left.addTab(QLabel(u'Содержимое вкладки 1'), u'Вккладка 1')
        left.addTab(QLabel(u'Содержимое вкладки2'), u'Вкладка 2')
        left.setTabPosition(QTabWidget.West)
        #left.setFrameShape(QFrame.StyledPanel)

        right = QFrame()
        right.setFrameShape(QFrame.StyledPanel)

        bottom = QTabWidget()
        bottom.addTab(QLabel(u'Содержимое вкладки 1 НИЗ'), u'Вкладка 1')
        bottom.addTab(QLabel(u'Содержимое вкладки 2 НИЗ'), u'Вкладка 2')
        bottom.setTabPosition(QTabWidget.South)
        #bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(left)
        splitter1.addWidget(right)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)

        self.setLayout(hbox)

        self.setGeometry(300, 300, 900, 700)
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Examp()
    sys.exit(app.exec_())