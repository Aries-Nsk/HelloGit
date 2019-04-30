#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
По примеру
http://doc.qt.io/qt-5/qtwidgets-layouts-basiclayouts-dialog-h.html
'''

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import qApp
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QGridLayout

class Example(QDialog):

#    menuBar = QMenuBar
#    horGroupBox = QGroupBox
#    gridGroupBox = QGroupBox


    def __init__(self):
        super().__init__()

        self.createMenu()
        self.createHorGroupBox()
        self.createGridGroupBox()
        self.initUI()

        mainLayout = QVBoxLayout()
        mainLayout.setMenuBar(self.menuBar)
        mainLayout.addWidget(self.horGroupBox)
        mainLayout.addWidget(self.gridGroupBox)

        self.setLayout(mainLayout)

    def createMenu(self):

        self.menuBar = QMenuBar()
        fileMenu = QMenu(u'&File', self)
        exitAction = fileMenu.addAction('Exit')
        self.menuBar.addMenu(fileMenu)
        exitAction.triggered.connect(qApp.quit)

    def createHorGroupBox(self):

        self.horGroupBox = QGroupBox(u'Горизонтальное размещение')
        layout = QHBoxLayout()

        buttons1 = QPushButton(u'Кнопка1')
        layout.addWidget(buttons1)

        buttons2 = QPushButton(u'Кнопка2')
        layout.addWidget(buttons2)

        buttons3 = QPushButton(u'Кнопка3')
        layout.addWidget(buttons3)

        self.horGroupBox.setLayout(layout)

    def createGridGroupBox(self):

        NumGridRows = 3
        i = 0

        self.gridGroupBox = QGroupBox(u'Сеточное размещение')
        layout = QGridLayout()
#
        labels1 = QLabel(u'Line : 1')
        lineEdits1 = QLineEdit()
        layout.addWidget(labels1, 1, 0)
        layout.addWidget(lineEdits1, 1, 1)

        labels2 = QLabel(u'Line : 2')
        lineEdits2 = QLineEdit()
        layout.addWidget(labels2, 2, 0)
        layout.addWidget(lineEdits2, 2, 1)

        labels3 = QLabel(u'Line : 3')
        lineEdits3 = QLineEdit()
        layout.addWidget(labels3, 3, 0)
        layout.addWidget(lineEdits3, 3, 1)

        smallEditor = QTextEdit()
        smallEditor.setPlainText(u'This widget takes up about two thirds of the')
        layout.addWidget(smallEditor, 0, 2, 4, 1)

        layout.setColumnStretch(1, 10)
        layout.setColumnStretch(2, 20)
        self.gridGroupBox.setLayout(layout)

    def initUI(self):

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())