# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_fgo_about.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(260, 150)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 240, 61))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(85, 110, 90, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "关于"))
        self.label_2.setText(_translate("Dialog", "注意：需要将source文件夹，settings文件夹和执行文件放在一个目录下，并且目录中不能包含中文"))
        self.pushButton.setText(_translate("Dialog", "确定"))
