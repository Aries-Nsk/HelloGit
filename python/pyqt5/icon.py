#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMessageBox
from PyQt5.QtGui import QIcon, QFont

class Icon(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()

    def closeEvent(self, event):

#        reply = QMessageBox.question(self, 'Сообщение', "Приложение будет закрыто. Вы уверены?",
#                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        msg = QMessageBox()
        #msg.setIcon(QMessageBox.Warning)
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle('Сообщение')
        msg.setText('Текст сообщения')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        reply = msg.exec_()

        if reply == QMessageBox.Yes:
            print('Выход')
            event.accept()
        else:
            print('Игнор')
            event.ignore()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Кнопка', self)
        btn.setToolTip('Это <b>QPushButton</b> виджет')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)


        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('./img/at'))
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Icon()
    sys.exit(app.exec_())
