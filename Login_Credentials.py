# -*- coding: utf-8 -*-
import os
import subprocess
from tkinter import messagebox

# Form implementation generated from reading ui file 'Login_Credentials.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginCredential(object):
    def setupUi(self, LoginCredential):
        LoginCredential.setObjectName("LoginCredential")
        LoginCredential.resize(500, 500)
        LoginCredential.setMinimumSize(QtCore.QSize(498, 500))
        LoginCredential.setMaximumSize(QtCore.QSize(500, 500))
        self.label = QtWidgets.QLabel(LoginCredential)
        self.label.setGeometry(QtCore.QRect(0, 0, 501, 511))
        self.label.setStyleSheet("background-image: url(image/Display.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(LoginCredential)
        self.frame.setGeometry(QtCore.QRect(50, 70, 400, 400))
        self.frame.setMinimumSize(QtCore.QSize(400, 400))
        self.frame.setStyleSheet("background-color: rgba(0, 36, 66,0.9);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 381, 41))
        self.label_3.setStyleSheet("background-color: rgba(0, 36, 66,0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Tahoma\";\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.username = QtWidgets.QLineEdit(self.frame)
        self.username.setGeometry(QtCore.QRect(20, 100, 361, 31))
        self.username.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Tahoma\";")
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.setObjectName("username")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 381, 41))
        self.label_4.setStyleSheet("background-color: rgba(0, 36, 66,0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Tahoma\";\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(20, 230, 361, 31))
        self.password.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Tahoma\";")
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(150, 320, 101, 41))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Tahoma\";\n"
"background-color: rgb(51, 51, 51);")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(LoginCredential)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 461, 41))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 24pt \"Perpetua Titling MT\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(LoginCredential)
        QtCore.QMetaObject.connectSlotsByName(LoginCredential)

        self.pushButton.clicked.connect(self.login)

    def retranslateUi(self, LoginCredential):
        _translate = QtCore.QCoreApplication.translate
        LoginCredential.setWindowTitle(_translate("LoginCredential", "Log In Credential"))
        self.label_3.setText(_translate("LoginCredential", "Username:"))
        self.label_4.setText(_translate("LoginCredential", "Password:"))
        self.pushButton.setText(_translate("LoginCredential", "Login"))
        self.label_2.setText(_translate("LoginCredential", "Log-in Credentials"))

    USER = "admin"
    PASS = "admin"

    def login(self):
        if self.username.text() == "" or self.password.text() == "":
            messagebox.showwarning("Missing Data", "Please fill up all needed data.")
            return

        elif self.username.text() == self.USER and self.password.text() == self.PASS:
            self.GoToMain()

        else:
            messagebox.showerror("Invalid Data", "Username or Pass is invalid.")

    def GoToMain(self):
        LoginCredential.destroy()
        current_directory = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(current_directory, "main.py")
        subprocess.run(["python", script_path])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginCredential = QtWidgets.QFrame()
    ui = Ui_LoginCredential()
    ui.setupUi(LoginCredential)
    LoginCredential.show()
    sys.exit(app.exec_())
