#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic


class BarMain(QToolBar):
    def __init__(self, parent=None):
        super(BarMain, self).__init__(parent)
        self.setFloatable(False)
        self.setMovable(False)


class ToolPanel(QListView):
    def __init__(self, parent=None):
        super(ToolPanel, self).__init__(parent)

    def restoreSettings(self):
        settings = QSettings()
        settings.beginGroup("ToolPanel")
        self.setFixedWidth(settings.value("width", 200))
        settings.endGroup()


class FileManagerPanel(QListView):
    def __init__(self, parent=None):
        super(FileManagerPanel, self).__init__(parent)


class WndMain(QMainWindow):
    def __init__(self, parent=None):
        super(WndMain, self).__init__(parent)
        self.settings = QSettings()
        self.initUi()

    def initUi(self):
        self.restoreSettings()
        self.centralWidget = QWidget(self)
        self.toolbar = BarMain(self.centralWidget)
        self.toolPanel = ToolPanel(self.centralWidget)
        self.fmPanel = FileManagerPanel(self.centralWidget)
        boxMain = QHBoxLayout(self.centralWidget)
        boxMain.addWidget(self.toolPanel)
        boxMain.addWidget(self.fmPanel)
        self.centralWidget.setLayout(boxMain)
        self.setCentralWidget(self.centralWidget)

    def restoreSettings(self):
        settings = QSettings()
        settings.beginGroup("WndMain")
        defaultSize = QSize(600, 400)
        self.resize(settings.value("size", defaultSize))
        settings.endGroup()

    def storeSettings(self):
        settings = QSettings()
        settings.beginGroup("WndMain");
        settings.setValue("size", self.size());
        settings.setValue("fullScreen", self.isFullScreen());
        settings.endGroup();


class AppMain(QApplication):
    def __init__(self, argv):
        super(AppMain, self).__init__(argv)
        QCoreApplication.setOrganizationName("freakish");
        QCoreApplication.setOrganizationDomain("freakish.org");
        QCoreApplication.setApplicationName("MimicFM")


if __name__ == '__main__':
    app = AppMain(sys.argv)
    w = WndMain()
    w.show()
    sys.exit(app.exec_())