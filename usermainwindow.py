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
        UserMainWindow.resize(320, 470)
        UserMainWindow.setMinimumSize(QtCore.QSize(320, 470))
        UserMainWindow.setMaximumSize(QtCore.QSize(320, 470))
        UserMainWindow.setAcceptDrops(False)
        UserMainWindow.setAutoFillBackground(False)
        UserMainWindow.setStyleSheet("QWidget {\n"
"    background:rgb(0, 0, 72);\n"
"    font-family: Arial, Helvetica, sans-serif;\n"
"}\n"
"\n"
"QTextEdit {\n"
"    border: 0px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(UserMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 170, 261, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 60))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background: rgb(211, 141, 0);\n"
"    border-radius: 8px;\n"
"    font-size: 20px;\n"
"    font-weight: normal;\n"
"    color: rgb(0, 0, 0)\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: rgb(255, 227, 15);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 20, 321, 51))
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textEdit.setMouseTracking(True)
        self.textEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setReadOnly(True)
        self.textEdit.setAcceptRichText(True)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 90, 321, 61))
        self.textEdit_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setAcceptRichText(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 240, 261, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background:rgb(211, 141, 0);\n"
"    border-radius: 8px;\n"
"    font-size: 20px;\n"
"    font-weight: normal;\n"
"    color: rgb(0, 0, 0)\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: rgb(255, 227, 15);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 310, 261, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background:rgb(211, 141, 0);\n"
"    border-radius: 8px;\n"
"    font-size: 20px;\n"
"    font-weight: normal;\n"
"    color: rgb(0, 0, 0)\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: rgb(255, 227, 15);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 380, 261, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMaximumSize(QtCore.QSize(16777215, 60))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background:rgb(211, 141, 0);\n"
"    border-radius: 8px;\n"
"    font-size: 20px;\n"
"    font-weight: normal;\n"
"    color: rgb(0, 0, 0)\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background: rgb(255, 227, 15);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        UserMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(UserMainWindow)
        QtCore.QMetaObject.connectSlotsByName(UserMainWindow)

    def retranslateUi(self, UserMainWindow):
        _translate = QtCore.QCoreApplication.translate
        UserMainWindow.setWindowTitle(_translate("UserMainWindow", "MainWindow"))
        self.pushButton.setText(_translate("UserMainWindow", "Clearance"))
        self.textEdit.setHtml(_translate("UserMainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\',\'Helvetica\',\'sans-serif\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">W E L C O M E</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("UserMainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\',\'Helvetica\',\'sans-serif\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#ffffff;\">Please select any</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#ffffff;\">option below</span></p></body></html>"))
        self.pushButton_2.setText(_translate("UserMainWindow", "Evaluation"))
        self.pushButton_3.setText(_translate("UserMainWindow", "Adding / Droppping"))
        self.pushButton_4.setText(_translate("UserMainWindow", "Others"))
