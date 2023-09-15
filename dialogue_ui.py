import os
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, QSize, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QFrame


class CustomDialog(QDialog):
    def __init__(self, text):
        super(CustomDialog, self).__init__()
        # uic.loadUi('.doNotDelete\\CustomDialog.ui', self)
        self.label = None
        self.setupUi(self, text)

    def setupUi(self, Dialog, text):
        Dialog.setWindowTitle("Info")
        Dialog.setObjectName("Dialog")
        Dialog.resize(359, 184)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(-90, 0, 451, 301))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(os.path.abspath("files\\Background.jpg")))
        self.label.setObjectName("label")
        self.Export = QPushButton(Dialog)
        self.Export.setGeometry(QRect(220, 110, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Export.setFont(font)
        self.Export.setStyleSheet("color: rgb(243, 243, 243);\n"
                                  "border-color: rgb(243, 243, 243);\n"
                                  "background-color: rgb(2, 5, 3);\n"
                                  "border-left-radius:10px;\n"
                                  "background-color: rgb(63, 122, 138);\n"
                                  "hover {\n"
                                  "                background-color: rgb(0, 0, 138);\n"
                                  "                border-style: inset;\n"
                                  "            }")
        self.Export.setFlat(False)
        self.Export.setObjectName("Export")
        self.Cancel = QPushButton(Dialog)
        self.Cancel.setGeometry(QRect(140, 110, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Cancel.setFont(font)
        self.Cancel.setStyleSheet("color: rgb(243, 243, 243);\n"
                                  "border-color: rgb(243, 243, 243);\n"
                                  "background-color: rgb(2, 5, 3);\n"
                                  "border-left-radius:10px;\n"
                                  "background-color: rgb(63, 122, 138);\n"
                                  "hover {\n"
                                  "                background-color: rgb(0, 0, 138);\n"
                                  "                border-style: inset;\n"
                                  "            }")
        self.Cancel.setObjectName("Cancel")
        self.label_4 = QLabel(Dialog)
        self.label_4.setGeometry(QRect(10, 30, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(243, 243, 243);\n"
                                   "background-color: rgb(2, 5, 3);\n"
                                   "border-radius:10px;\n"
                                   "background-color: rgb(63, 122, 138);\n"
                                   "color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_6 = QLabel(Dialog)
        self.label_6.setGeometry(QRect(200, 110, 20, 41))
        self.label_6.setMinimumSize(QSize(10, 0))
        self.label_6.setMaximumSize(QSize(20, 16777215))
        self.label_6.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label_6.setFrameShape(QFrame.StyledPanel)
        self.label_6.setFrameShadow(QFrame.Raised)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label.raise_()
        self.label_4.raise_()
        self.label_6.raise_()
        self.Cancel.raise_()
        self.Export.raise_()
        self.label_4.setText('   ' + str(text))
        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Message"))
        self.Export.setText(_translate("Dialog", "Export"))
        self.Cancel.setText(_translate("Dialog", "Cancel"))
        self.label_4.setText(_translate("Dialog", "    File Successfully Created !"))
