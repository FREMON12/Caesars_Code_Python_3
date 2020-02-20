from PySide2 import QtCore, QtGui, QtWidgets
from Hack_interface_design import Ui_Dialog
from Hack import hack_en
from Hack import hack_fr
from Hack import encript_hack_en
from Hack import encript_hack_fr
import sys


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Dialog()
        self.text = ""
        self.key = ""
        self.ui.setupUi(self)
        self.ui.label.setFont(
            QtGui.QFont('SansSerif', 30)

        )
        self.ui.pushButton.clicked.connect(self.Fun_hack_en)
        self.ui.pushButton.clicked.connect(self.Fun_hack_fr)
        self.ui.pushButton.clicked.connect(self.Fun_hack_encript_en)
        self.ui.pushButton.clicked.connect(self.Fun_hack_encript_fr)

    def Fun_hack_en(self):
        self.ui.textEdit_2.setText(hack_en())

    def Fun_hack_fr(self):
        self.ui.textEdit.setText(hack_fr())

    def Fun_hack_encript_en(self):
        self.ui.textEdit_3.setText(encript_hack_en())

    def Fun_hack_encript_fr(self):
        self.ui.textEdit_4.setText(encript_hack_fr())


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec_())
