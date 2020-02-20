# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\MY_PROJECT_PC\Python\Caesar_Project\venv\file35.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Caesar(object):
    def setupUi(self, Caesar):
        Caesar.setObjectName("Caesar")
        Caesar.resize(750, 573)
        self.label = QtWidgets.QLabel(Caesar)
        self.label.setGeometry(QtCore.QRect(150, 110, 141, 51))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Caesar)
        self.label_2.setGeometry(QtCore.QRect(430, 0, 241, 71))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Caesar)
        self.label_3.setGeometry(QtCore.QRect(110, 20, 151, 31))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Caesar)
        self.label_5.setGeometry(QtCore.QRect(110, 120, 181, 31))
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(Caesar)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 170, 351, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(Caesar)
        self.label_6.setGeometry(QtCore.QRect(480, 120, 181, 31))
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(Caesar)
        self.lineEdit_6.setGeometry(QtCore.QRect(390, 170, 351, 41))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.textEdit = QtWidgets.QTextEdit(Caesar)
        self.textEdit.setGeometry(QtCore.QRect(10, 330, 351, 241))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Caesar)
        self.textEdit_2.setGeometry(QtCore.QRect(390, 330, 351, 241))
        self.textEdit_2.setObjectName("textEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(Caesar)
        self.lineEdit.setGeometry(QtCore.QRect(10, 70, 351, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(Caesar)
        self.label_4.setGeometry(QtCore.QRect(110, 230, 151, 31))
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(Caesar)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 280, 101, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Caesar)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 280, 111, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Caesar)
        self.pushButton_5.setGeometry(QtCore.QRect(260, 280, 101, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Caesar)
        self.pushButton_6.setGeometry(QtCore.QRect(390, 280, 101, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Caesar)
        self.pushButton_7.setGeometry(QtCore.QRect(640, 280, 101, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Caesar)
        self.pushButton_8.setGeometry(QtCore.QRect(510, 280, 111, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_7 = QtWidgets.QLabel(Caesar)
        self.label_7.setGeometry(QtCore.QRect(490, 230, 161, 31))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Caesar)
        QtCore.QMetaObject.connectSlotsByName(Caesar)

    def retranslateUi(self, Caesar):
        _translate = QtCore.QCoreApplication.translate
        Caesar.setWindowTitle(_translate("Caesar", "Dialog"))
        self.label_2.setText(_translate("Caesar", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Шифр Цезаря </span></p></body></html>"))
        self.label_3.setText(_translate("Caesar", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Введите текст </span></p></body></html>"))
        self.label_5.setText(_translate("Caesar", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Введите ключ</span></p></body></html>"))
        self.label_6.setText(_translate("Caesar", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Ведите алфавит</span></p></body></html>"))
        self.label_4.setText(_translate("Caesar", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Зашифровать </span></p></body></html>"))
        self.pushButton_3.setText(_translate("Caesar", "английский"))
        self.pushButton_4.setText(_translate("Caesar", "русский"))
        self.pushButton_5.setText(_translate("Caesar", "произвольный"))
        self.pushButton_6.setText(_translate("Caesar", "английский"))
        self.pushButton_7.setText(_translate("Caesar", "произвольный"))
        self.pushButton_8.setText(_translate("Caesar", "русский"))
        self.label_7.setText(_translate("Caesar", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Расшифровать </span></p></body></html>"))
