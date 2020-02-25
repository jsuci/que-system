# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'usermainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserMainWindow(object):
    def setupUi(self, UserMainWindow):
        UserMainWindow.setObjectName("UserMainWindow")
        UserMainWindow.resize(320, 480)
        UserMainWindow.setMinimumSize(QtCore.QSize(320, 480))
        UserMainWindow.setMaximumSize(QtCore.QSize(320, 480))
        UserMainWindow.setAcceptDrops(False)
        UserMainWindow.setAutoFillBackground(False)
        UserMainWindow.setStyleSheet("QWidget {\n"
"    background:rgb(0, 0, 72);\n"
"    font-family: Arial, Helvetica, sans-serif;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background:rgb(211, 141, 0);\n"
"    border-radius: 8px;\n"
"    font-size: 20px;\n"
"    font-weight: normal;\n"
"    letter-spacing: 5px;\n"
"    color: rgb(0, 0, 0)\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: rgb(255, 227, 15);\n"
"}\n"
"\n"
"QTextEdit {\n"
"    font-size: 35px;\n"
"    font-weight: 500;\n"
"    border: 0px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(UserMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 310, 281, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 60))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(-20, 60, 361, 51))
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 160, 301, 81))
        self.textEdit_2.setObjectName("textEdit_2")
        UserMainWindow.setCentralWidget(self.centralwidget)
        self.actionOpen = QtWidgets.QAction(UserMainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(UserMainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionUndo = QtWidgets.QAction(UserMainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(UserMainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCut = QtWidgets.QAction(UserMainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(UserMainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionCopy = QtWidgets.QAction(UserMainWindow)
        self.actionCopy.setObjectName("actionCopy")

        self.retranslateUi(UserMainWindow)
        QtCore.QMetaObject.connectSlotsByName(UserMainWindow)

    def retranslateUi(self, UserMainWindow):
        _translate = QtCore.QCoreApplication.translate
        UserMainWindow.setWindowTitle(_translate("UserMainWindow", "MainWindow"))
        self.pushButton.setText(_translate("UserMainWindow", "Get Priority Ticket Here"))
        self.textEdit.setHtml(_translate("UserMainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\',\'Helvetica\',\'sans-serif\'; font-size:35px; font-weight:496; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600;\">W E L C O M E</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("UserMainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\',\'Helvetica\',\'sans-serif\'; font-size:35px; font-weight:496; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:400;\">Press Button Below to</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:400;\">Generate Priority Ticket</span></p></body></html>"))
        self.actionOpen.setText(_translate("UserMainWindow", "Open"))
        self.actionClose.setText(_translate("UserMainWindow", "Close"))
        self.actionUndo.setText(_translate("UserMainWindow", "Undo"))
        self.actionRedo.setText(_translate("UserMainWindow", "Redo"))
        self.actionCut.setText(_translate("UserMainWindow", "Cut"))
        self.actionPaste.setText(_translate("UserMainWindow", "Paste"))
        self.actionCopy.setText(_translate("UserMainWindow", "Copy"))
