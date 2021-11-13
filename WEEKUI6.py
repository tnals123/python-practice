from PyQt5 import QtCore, QtGui, QtWidgets
import sys
class Ui_MainWindow(object):
    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi()
        self.MainWindow.show()
    def setupUi(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(260, 157)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 210, 21))
        self.lineEdit.setStyleSheet("border: 1px solid green;\n"
"border-radius:5px;\n"
"padding-left:50px")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 60, 210, 21))
        self.lineEdit_2.setStyleSheet("border: 1px solid green;\n"
"border-radius:5px;\n"
"padding-left:10px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 90, 210, 28))
        self.pushButton.setStyleSheet("background-color: Lightgreen;\n"
"color:white;\n"
"border:1px soild green;\n"
"border-radius:5px;\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("Mainwindow", "Mainwindow"))
        self.pushButton.setText(_translate("Mainwindow", "login"))


if __name__ == "__main__":
        
        app = QtWidgets.QApplication(sys.argv)
        ui = Ui_MainWindow()
        sys.exit(app.exec_())

