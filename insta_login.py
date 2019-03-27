import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Insta_Easy")
        MainWindow.resize(578, 641)
        MainWindow.setMinimumSize(QtCore.QSize(578, 641))
        MainWindow.setMaximumSize(QtCore.QSize(578, 641))
        MainWindow.setStyleSheet("*{\n"
"    font-family:century gothic;\n"
"    font-size:24px;\n"
"}\n"
"QFrame\n"
"{\n"
"background:rgba(0,0,0,0.8);\n"
"border-radius:15px\n"
"}\n"
"#Form\n"
"{\n"
"background:url(bg.jpg);\n"
"}\n"
"QPushButton\n"
"{\n"
"background:red;\n"
"border-radius:60px;\n"
"}\n"
"QToolButton\n"
"{\n"
"background:red;\n"
"border-radius:60px;\n"
"}\n"
"QLabel\n"
"{\n"
"color:white;\n"
"background:transparent;\n"
"}\n"
"QPushButton\n"
"{\n"
"background:red;\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"color:#333;\n"
"background:#49ebff;\n"
"border-radius:15px;\n"
"}\n"
"QLineEdit\n"
"{\n"
"color:#717072;\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid #717072;\n"
"}\n" 
"#lineEdit_3\n"
"{\n"
"color:red;\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:0px solid #717072;\n"
"}\n"                                 
"QLineEdit\n"
"{\n"
"font-family:century gothic;\n"
"font-size:16px;\n"
"}\n"                            
"")
        self.Form = QtWidgets.QWidget(MainWindow)
        self.Form.setObjectName("Form")
        self.frame = QtWidgets.QFrame(self.Form)
        self.frame.setGeometry(QtCore.QRect(90, 90, 401, 511))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(138, 70, 141, 51))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 433, 341, 51))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(40, 210, 321, 41))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 320, 321, 41))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 380, 321, 41))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 270, 141, 51))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 160, 131, 51))
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.toolButton = QtWidgets.QToolButton(self.Form)
        self.toolButton.setGeometry(QtCore.QRect(230, 30, 121, 121))
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("login-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(68, 68))
        self.toolButton.setObjectName("toolButton")
        MainWindow.setCentralWidget(self.Form)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Insta_Easy", "Insta_Easy"))
        self.label.setText(_translate("Insta_Easy", "INSTAEASY"))
        self.pushButton.setText(_translate("Insta_Easy", "Войти"))
        self.lineEdit.setPlaceholderText(_translate("Insta_Easy", "Введите Логин"))
        self.lineEdit_2.setPlaceholderText(_translate("Insta_Easy", "Введите Пароль"))
        self.label_2.setText(_translate("Insta_Easy", "Password"))
        self.label_3.setText(_translate("Insta_Easy", "Username"))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

