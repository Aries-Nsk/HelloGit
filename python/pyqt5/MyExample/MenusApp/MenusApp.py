#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):

    infoLabel = QLabel  # Информационная строка. Показывает выбранное действие.

    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        #topFiller = QWidget()
        #topFiller.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.infoLabel = QLabel(u'Инфо панель', alignment=Qt.AlignCenter)
        '''
        self.infoLabel = QLabel(u'<i>Choose a menu option, or right-click toinvoke a context menu</i>')
        self.infoLabel.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.infoLabel.setAlignment(Qt.AlignCenter) # Требует PyQt5.QtCore
        '''

        self.tabs = QTabWidget()
        self.tabs.addTab(self.infoLabel, u'Вкладка')

        #bottomFiler = QWidget()
        #bottomFiler.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        layout = QVBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        #ayout.addWidget(topFiller)
        #layout.addWidget(self.infoLabel)
        layout.addWidget(self.tabs)
        # ayout.addWidget(bottomFiler)

        widget.setLayout(layout)

        self.createActions()
        self.createMenu()
        self.createToolBars()
        self.createStatusBar()

        self.setWindowTitle(u'Меню')
        self.setMinimumSize(160, 160)
        self.resize(480, 320)
        self.resize(650, 450)
        self.moveToCenter()
        #self.center()

    def newFile(self):
        self.infoLabel.setText('Invoked <b>File|New</b>')
        self.statusBar().showMessage(u'Выбранно - Файл -> Новый')

        #fileName = QFileDialog.getOpenFileName(self, 'Открыть файл', '/home/isa')
        #fname = QFileInfo(fileName)

        fname, _ = QFileDialog.getOpenFileName(self)
        #fname.open(QFile.ReadOnly)

        #f = QFile(fname)

        #print(fileName)
        print(fname)

    def about(self):
        self.infoLabel.setText(u'Invoked <b>Help|About</b>')
        QMessageBox.about(self, u'About Menu', u'The <b>Menu</b> example\
         shows how to create menu-bar menus and context menus.')

    def aboutQt(self):
        str = QT_VERSION_STR    # PyQt5.QtCore
        self.infoLabel.setText('Invoked <b>Help|About Qt  </b>' + str)
        qApp.aboutQt()

    def initUi(self):
        pass

    def createActions(self):

        self.newAction = QAction(QIcon('./img/home.png'), u'&New', self)
        self.newAction.setShortcuts(QKeySequence.New)    # Требует PyQt5.QtGui
        self.newAction.setStatusTip(u'Create a new file')
        self.newAction.triggered.connect(self.newFile)

        self.exitAction = QAction(u'В&ыход', self)
        self.exitAction.setShortcuts(QKeySequence.Quit)
        self.exitAction.setStatusTip(u'Закончить работу с программой')
        self.exitAction.triggered.connect(self.close)

        self.aboutAction = QAction(QIcon('./img/info.png'), u'&About', self)
        self.aboutAction.setStatusTip(u'Show the application`s About box')
        self.aboutAction.triggered.connect(self.about)

        self.aboutQtAction = QAction(QIcon('./img/comment-speech.png'), u'About &Qt', self)
        self.aboutQtAction.setStatusTip(u'Show the Qt library`s About box')
        self.aboutQtAction.triggered.connect(self.aboutQt)

    def createMenu(self):

        #menuBar = self.menuBar()
        #fileMenu = menuBar.addMenu(u'&File')
        # Это работать будет одинаково
        fileMenu = self.menuBar().addMenu(u'&File')

        fileMenu.addAction(self.newAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)


        #helpMenu = menuBar.addMenu(u'&Help')

        helpMenu = self.menuBar().addMenu(u'&Help')
        helpMenu.addAction(self.aboutAction)
        helpMenu.addAction(self.aboutQtAction)

    def createToolBars(self):

        fileToolBar = self.addToolBar(u'File')
        fileToolBar.addAction(self.newAction)
        fileToolBar.addAction(self.exitAction)

        qle = QLineEdit('редактор')
        qle.setToolTip(u'Это редактор ToolTip')
        qle.setStatusTip(u'Редактор statusBar')
        qle.textChanged[str].connect(self.qleOnChanged)
        fileToolBar.addWidget(qle)

        cb = QComboBox()
        cb.setStatusTip('Cjmbo box')
        cb.setToolTip('Это моя крутая подсказка')
        cb.addItem('Первый элемент списка')
        cb.addItem(QIcon('./img/email.png'), 'Второй элемент')
        cb.insertSeparator(2)
        cb.addItem(QIcon('./img/search.png'), 'Третьий эллемент')
        cb.addItem('Четвертый элемент')

        fileToolBar.addWidget(cb)

        helpToolBar = self.addToolBar(u'Help')
        helpToolBar.addAction(self.aboutAction)
        helpToolBar.addAction(self.aboutQtAction)

    def qleOnChanged(self):
        self.infoLabel.setText(u'Линейный редактор')

    def createStatusBar(self):

        #self.statusBar().showMessage(u'Готово')
        self.statusBar()
        btn = QPushButton(u'Выход', self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        self.statusBar().addWidget(btn)

    def writeSetting(self):

        setting = QSettings(u'QtProject', u'Application Example')
        setting.setValue('pos', self.pos())
        setting.setValue('size', self.size())

    def moveToCenter(self):
        qr = self.frameGeometry()   # получаем прямоугольник, точно определяющий форму главного окна
        cp = QDesktopWidget().availableGeometry().center()  # выясняем разрешение экрана нашего монитора. Из этого разрешения, мы получаем центральную точку.
        qr.moveCenter(cp)
        '''
            перемещаем верхнюю левую точку окна приложения в верхнюю левую точку прямоугольника qr,
            таким образом центрируя окно на нашем экране
        '''
        self.move(qr.topLeft())

    def center(self):

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height()-size.height) /2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
