#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *

class FindFileDialog(QWidget):


    def __init__(self):
        super().__init__()

        namedLabel = QLabel('Named:')
        namedLineEdit = QLineEdit('myfile.txt')

        lookInLabel = QLabel('Look in:')
        lookInLineEdit = QLineEdit('/var/log')

        subfoldersCheckBox = QCheckBox('include subfolders')

        table = QTableWidget()

        messageLabel = QLabel('Готово')

        findBottom = QPushButton('Искать')
        stopBottom = QPushButton('&Стоп')
        stopBottom.clicked.connect(self.stopButtomClicked)

        closeButtom = QPushButton('&Закрыть')
        closeButtom.clicked.connect(self.closeButtomClicked)
        helpBottom = QPushButton('Помощь')

        # Компановка
        leftLayout = QGridLayout()
        leftLayout.addWidget(namedLabel, 0, 0)
        leftLayout.addWidget(namedLineEdit, 0, 1)
        leftLayout.addWidget(lookInLabel, 1, 0)
        leftLayout.addWidget(lookInLineEdit, 1, 1)
        leftLayout.addWidget(subfoldersCheckBox, 2, 0, 1, 2)
        leftLayout.addWidget(table, 3, 0, 1, 2)
        leftLayout.addWidget(messageLabel, 4, 0, 1, 2)

        rightLayout = QVBoxLayout()
        rightLayout.addWidget(findBottom)
        rightLayout.addWidget(stopBottom)
        rightLayout.addWidget(closeButtom)
        rightLayout.addStretch()
        rightLayout.addWidget(helpBottom)

        mainLayout = QHBoxLayout()
        mainLayout.addLayout(leftLayout)
        mainLayout.addLayout(rightLayout)

        self.setLayout(mainLayout)
        self.setWindowTitle('Искать файлы или папки')
        self.resize(500, 300)
        self.moveToCenter()
        self.show()

    def closeButtomClicked(self):
        print('Clicked on close Button')
        self.close()

    def stopButtomClicked(self):
        print('Clicked on stop Buttom')

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height) / 2)

    def moveToCenter(self):
        qr = self.frameGeometry()   # получаем прямоугольник, точно определяющий форму главного окна
        cp = QDesktopWidget().availableGeometry().center()  # выясняем разрешение экрана нашего монитора. Из этого разрешения, мы получаем центральную точку.
        qr.moveCenter(cp)
        '''
            перемещаем верхнюю левую точку окна приложения в верхнюю левую точку прямоугольника qr,
            таким образом центрируя окно на нашем экране
        '''
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = FindFileDialog()
    sys.exit(app.exec_())