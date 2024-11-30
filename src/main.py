import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5.uic import loadUi
class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)

def fun():
    app=QApplication(sys.argv)
    login=Login()
    login.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    fun()


