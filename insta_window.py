# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insta_login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow")
        MainWindow2.resize(841, 619)
        MainWindow2.setMinimumSize(QtCore.QSize(841, 619))
        MainWindow2.setMaximumSize(QtCore.QSize(841, 619))
        MainWindow2.setStyleSheet("*{\n"
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
"background:url(C:/Users/User/Downloads/bg.jpg);\n"
"}\n"
"QPushButton\n"
"{\n"
"background:red;\n"
"border-radius:60px;\n"
"}\n"
"QToolButton\n"
"{\n"
"background:transparent;\n"
"border-radius:60px;\n"
"border:4px solid white; \n"
"}\n"
"QLabel\n"
"{\n"
"color:white;\n"
"background:transparent;\n"
"}\n"
"#lineEdit_3\n"
"{\n"
"color:red;\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid #717072;\n"
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
"")
        self.Form = QtWidgets.QWidget(MainWindow2)
        self.Form.setObjectName("Form")
        self.frame = QtWidgets.QFrame(self.Form)
        self.frame.setGeometry(QtCore.QRect(40, 60, 761, 511))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(320, 10, 141, 51))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(30, 90, 111, 111))
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(128, 128))
        self.toolButton.setObjectName("toolButton")
        MainWindow2.setCentralWidget(self.Form)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "INSTAEASY"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow2 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow2)
    MainWindow2.show()
    sys.exit(app.exec_())

