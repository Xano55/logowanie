# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import hashlib
from PyQt5.QtGui import QPixmap
from db_conn import dbConnection

class Ui_FormLogin(object):
    def setupUi(self, FormLogin):
        FormLogin.setObjectName("FormLogin")
        FormLogin.resize(550, 200)
        FormLogin.setMinimumSize(QtCore.QSize(150, 200))
        FormLogin.setMaximumSize(QtCore.QSize(550, 200))
        self.horizontalLayout = QtWidgets.QHBoxLayout(FormLogin)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelimage = QtWidgets.QLabel(FormLogin)
        self.labelimage.setMinimumSize(QtCore.QSize(200, 120))
        self.labelimage.setText("")
        self.labelimage.setObjectName("labelimage")
        self.horizontalLayout.addWidget(self.labelimage)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(FormLogin)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(FormLogin)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_3 = QtWidgets.QLabel(FormLogin)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(FormLogin)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(FormLogin)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(FormLogin)
        QtCore.QMetaObject.connectSlotsByName(FormLogin)
        
        self.pushButton.clicked.connect(self.loguj)
        
    def loguj(self):
        email = self.lineEdit.text()
        password = hashlib.md5(self.lineEdit_2.text().encode('utf-8')).hexdigest()
        #print(password)
        db = dbConnection()
        

    def retranslateUi(self, FormLogin):
        _translate = QtCore.QCoreApplication.translate
        FormLogin.setWindowTitle(_translate("FormLogin", "Logowanie"))
        self.label_2.setText(_translate("FormLogin", "E-mail"))
        self.label_3.setText(_translate("FormLogin", "Password"))
        self.pushButton.setText(_translate("FormLogin", "Login"))
        pixmap = QPixmap("lock.png")
        self.labelimage.setPixmap(pixmap)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormLogin = QtWidgets.QWidget()
    ui = Ui_FormLogin()
    ui.setupUi(FormLogin)
    FormLogin.show()
    sys.exit(app.exec_())