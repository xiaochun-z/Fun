#!/usr/bin/env python
# --coding:utf-8--

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QCheckBox, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from os import path
from ctypes import *


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        dll_path = path.realpath(path.join(path.dirname(path.realpath(__file__)), "ieproxy"))
        self.lib = cdll.LoadLibrary(dll_path)
        self.editProxy = QLineEdit("127.0.0.1:8118")
        self.chkProxy = QCheckBox("Enable")
        self.chkProxy.setChecked(self.lib.proxyEnabled() == 1)
        self.btnSave = QPushButton("Save")
        self.btnSave.clicked.connect(self.Save)
        self.btnSave.setMaximumWidth(80)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.initUI()

    def initUI(self):
        icon = QIcon("icon.png")
        self.setWindowIcon(icon)
        self.resize(320, 50)
        self.setWindowTitle("Internet explorer proxy")

        layout = QGridLayout()
        layout.setSpacing(10)
        layout.addWidget(QLabel("Proxy Address"), 0, 0)
        layout.addWidget(self.editProxy, 0, 1)
        layout.addWidget(self.chkProxy, 1, 1)

        layout.addWidget(self.btnSave, 2, 1)

        self.setLayout(layout)
        self.show()

    def Save(self):
        proxyaddress = self.editProxy.text()
        if 1 == self.lib.setproxy(proxyaddress, self.chkProxy.isChecked()):
            QMessageBox.information(self, "Proxy Setting", "Save the setting successfully!",
                                    QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MainWindow()

    sys.exit(app.exec())
