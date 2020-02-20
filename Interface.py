from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QHBoxLayout, QComboBox

from Interface_Function import Ui_Caesar
from Caesar import Encryption
from Caesar import Descryption
from tkinter import ttk
import sys


alphabet_en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u',
               'v', 'w', 'x', 'y', 'z']

alphabet_ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
               'у',
               'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Caesar()
        self.text = ""
        self.key = ""
        self.alf = ""
        self.ui.setupUi(self)
        self.ui.label.setFont(
            QtGui.QFont('SansSerif', 30)
        )
        self.ui.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.pushButton_3.clicked.connect(self.Fun_Ecryption_en)
        self.ui.pushButton_6.clicked.connect(self.Fun_Decryption_en)
        self.ui.pushButton_4.clicked.connect(self.Fun_Ecryption_ru)
        self.ui.pushButton_8.clicked.connect(self.Fun_Decryption_ru)
        self.ui.pushButton_5.clicked.connect(self.Fun_Ecryption_oll)
        self.ui.pushButton_7.clicked.connect(self.Fun_Decryption_oll)

    def Fun_Ecryption_en(self):
        texts = self.text = self.ui.lineEdit.text()
        keys = self.key = int(self.ui.lineEdit_2.text())
        cryptions = Encryption(keys, texts, alphabet_en)
        self.ui.textEdit.setText(cryptions)

    def Fun_Decryption_en(self):
        texts = self.text = self.ui.lineEdit.text()
        keys = self.key = int(self.ui.lineEdit_2.text())
        Decryptions = Descryption(keys, Encryption(keys, texts, alphabet_en), alphabet_en)
        self.ui.textEdit_2.setText(Decryptions)

    def Fun_Ecryption_ru(self):
        texts = self.text = self.ui.lineEdit.text()
        keys = self.key = int(self.ui.lineEdit_2.text())
        cryptions = Encryption(keys, texts, alphabet_ru)
        self.ui.textEdit.setText(cryptions)

    def Fun_Decryption_ru(self):
        texts = self.text = self.ui.lineEdit.text()
        keys = self.key = int(self.ui.lineEdit_2.text())
        Decryptions = Descryption(keys, Encryption(keys, texts, alphabet_ru), alphabet_ru)
        self.ui.textEdit_2.setText(Decryptions)

    def Fun_Ecryption_oll(self):
        texts = self.text = self.ui.lineEdit.text()
        keys = self.key = int(self.ui.lineEdit_2.text())
        alphabet_ol = self.alf = self.ui.lineEdit_6.text()
        alphabet_ols =list(alphabet_ol)
        cryptions = Encryption(keys, texts, alphabet_ols)
        self.ui.textEdit.setText(cryptions)

    def Fun_Decryption_oll(self):
        texts = self.text = self.ui.lineEdit.text()
        keys = self.key = int(self.ui.lineEdit_2.text())
        alphabet_ol = self.alf = self.ui.lineEdit_6.text()
        alphabet_ols = list(alphabet_ol)
        Decryptions = Descryption(keys, Encryption(keys, texts, alphabet_ols), alphabet_ols)
        self.ui.textEdit_2.setText(Decryptions)


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec_())
