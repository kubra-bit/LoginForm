import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import  loadUi

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.loginButton.clicked.connect(self.loginFunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createButton.clicked.connect(self.gotoFunction)
    def loginFunction(self):
        email=self.email.text()
        password=self.password.text()
        print("başarili bir şekilde giriş yapildi email:",email,"şifre: ",password)
    def gotoFunction(self):
        created=Create()
        widget.addWidget(created)
        widget.setCurrentIndex(widget.currentIndex()+1)
class Create(QDialog):
    def __init__(self):
        super(Create,self).__init__()
        loadUi("create.ui",self)
        self.signButton.clicked.connect(self.signFunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

    def signFunction(self):
        password=self.password.text()
        if password==self.confirim.text():
            email=self.email.text()
            print("başarili bir şekilde hesap oluşturuldu email: ",email," şifre :",password)
        else:
            print("şifreler eşlemiyor...")

app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(490)
widget.setFixedHeight(620)
widget.show()
app.exec_()
