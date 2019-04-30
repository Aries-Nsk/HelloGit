#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QBoxLayout,\
    QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()


        butA = QPushButton('A')
        butB = QPushButton('B')
        butC = QPushButton('C')

        pbxLayout = QBoxLayout()
        pbxLayout.addWidget(butA)
        pbxLayout.addWidget(butB)
        pbxLayout.addWidget(butC)
        self.setLayout(pbxLayout)

        pass

if __name__ == "__main__":

    import sys
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())