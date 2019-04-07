#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
import sys
#from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
#    newAct = QAction
#    closeAct = QAction
#    exitAct = QAction

    def __init__(self):
        super().__init__()


        topFiller = QWidget()
        topFiller.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.createActions()
        self.createMenu()

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')
        self.show()

    def createActions(self):

        self.newAct = QAction(u'&Новый...', self)
        self.newAct.setShortcut(u'Ctrl+N')
        self.newAct.setStatusTip(u'Создать новый документ')
        self.newAct.triggered.connect(self.newFile)

        self.closeAct = QAction(QIcon('img/close.png'), u'&Закрыть', self)
        self.closeAct.setShortcut('Ctrl+W')
        self.closeAct.setStatusTip(u'Закрыть документ')
        self.closeAct.triggered.connect(self.closeFile)

        self.exitAct = QAction(QIcon('img/exit.png'), u'В&ыход', self)
        self.exitAct.setShortcut('Ctrl+Q')
        self.exitAct.setStatusTip(u'Закончить работу с программой и выйти')
        self.exitAct.triggered.connect(qApp.quit)

#        self.statusBar()


    def createMenu(self):

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu(u'&Файл')
        fileMenu.addAction(self.newAct)
        fileMenu.addAction(self.closeAct)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAct)

        '''
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(self.exitAct)
        toolbar.addSeparator()
        toolbar.addAction(self.closeAct)
        '''


    def newFile(self):
        print(u'Меню - новый')
        pass

    def closeFile(self):
        print(u'Меню - закрыть')
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
