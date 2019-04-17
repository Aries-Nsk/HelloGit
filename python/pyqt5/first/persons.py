#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Person(QDialog):

    def __init__(self):
        super(Person, self).__init__()

        self.initUI()
        self.setWindowTitle('Ларионов Игорь Анатольевич (0024565). Системный администратор')
        self.show()

    def initUI(self):

        topHBox = QHBoxLayout()
        tabNoLbl = QLabel('Таб. №: ')
        tabNoLbl.setToolTip('Табельный номер')
        tabNoEdit = QLineEdit('0024565')
        tabNoEdit.setAlignment(Qt.AlignRight)
        tabNoEdit.setEnabled(False)
        fioLbl = QLabel('<h1>Ларионов Игорь Анатольевич</h1>')

        topHBox.addWidget(tabNoLbl)
        topHBox.addWidget(tabNoEdit)
        topHBox.addStretch(1)
        topHBox.addWidget(fioLbl)


        ###############################################
        bottomHBox = QHBoxLayout()
        saveBtn = QPushButton('ОK')
        saveBtn.clicked.connect(self.saveBtnClicked)

        applyBtn = QPushButton('Применить')
        applyBtn.clicked.connect(self.applyBtnClicked)

        cancelBtn = QPushButton('Отменить')
        cancelBtn.clicked.connect(self.cancelBtnClicked)

        bottomHBox.addStretch(1)
        bottomHBox.addWidget(saveBtn)
        #self.bplPush.clicked.connect(self.bplPushClicked)

        bottomHBox.addWidget(applyBtn)
        bottomHBox.addWidget(cancelBtn)

        ################################################
        tabWidget = QTabWidget()
        tabWidget.addTab(PrimaryTab(), 'Сведения')
        tabWidget.addTab(PersonalTab(), 'Личные данные')
        tabWidget.addTab(TrainingTab(), 'Обучение и развитие')


        formLayout = QVBoxLayout()
        formLayout.addLayout(topHBox)
        formLayout.addWidget(tabWidget)
        #formLayout.addStretch(1)
        formLayout.addLayout(bottomHBox)
        self.setLayout(formLayout)

    def saveBtnClicked(self):
        # Нажата кнопка Сохранить (Ok)
        print("Ok clicked")
        self.close()

    def applyBtnClicked(self):
        print("apply clicked")

    def cancelBtnClicked(self):
        print("cancel clicked")
        self.close()

class PrimaryTab(QWidget):

    def __init__(self):
        super(PrimaryTab, self).__init__()

        dob = QDate(1970, 3, 27)
        dobLbl = QLabel('Дата рождения:')
        dobDateEdit = QDateEdit(dob)

        sexLbl = QLabel('Пол:')
        sexComboBox = QComboBox()
        sexComboBox.addItem('Мужской')
        sexComboBox.addItem('Женский')
        bplLbl = QLabel('Место рождения:')

        self.bplPush = QPushButton('Заполнить')
        self.bplPush.clicked.connect(self.bplPushClicked)

        # self.bplLbl1 = QLabel('630001 г. Новосибирск, улица Ельцовкая, д. 4, кв. 101')

        self.birthGrid = QGridLayout()
        self.birthGrid.addWidget(dobLbl, 0,0, Qt.AlignRight)
        self.birthGrid.addWidget(dobDateEdit, 0, 1)
        self.birthGrid.addWidget(sexLbl, 0, 2, Qt.AlignRight)
        self.birthGrid.addWidget(sexComboBox, 0, 3)
        self.birthGrid.addWidget(bplLbl, 1, 0, Qt.AlignRight)
        self.birthGrid.addWidget(self.bplPush, 1, 1, Qt.AlignLeft)
        #birthGrid.removeWidget(bplPush)
        #birthGrid.addWidget(bplLbl1, 1, 1, 1, 3)

        birthGroupBox = QGroupBox()
        birthGroupBox.setLayout(self.birthGrid)

        ## Codes
        innLbl = QLabel('ИНН:')
        innLineEdit = QLineEdit()
        snilsLbl = QLabel('СНИЛС:')
        snilsLineEdit = QLineEdit()

        codeGrid = QGridLayout()
        codeGrid.addWidget(innLbl, 0, 0, Qt.AlignRight)
        codeGrid.addWidget(innLineEdit, 0, 1)
        codeGrid.addWidget(snilsLbl, 0, 2, Qt.AlignRight)
        codeGrid.addWidget(snilsLineEdit, 0, 3)

        codeGroupBox = QGroupBox()
        codeGroupBox.setLayout(codeGrid)

        ## Макет
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(birthGroupBox)
        mainLayout.addWidget(codeGroupBox)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)

    def bplPushClicked(self):
        print('Clicked button Заполнить')
        self.birthGrid.removeWidget(self.bplPush)
        self.bplPush.setVisible(False)
        self.bplLbl1 = QLabel('630001 г. Новосибирск, улица Ельцовкая, д. 4, кв. 101')
        self.birthGrid.addWidget(self.bplLbl1, 1, 1, 1, 3)



class PersonalTab(QWidget):
    def __init__(self):
        super(PersonalTab, self).__init__()
        pass

class TrainingTab(QWidget):
    def __init__(self):
        super(TrainingTab, self).__init__()
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Person()
    sys.exit(app.exec_())