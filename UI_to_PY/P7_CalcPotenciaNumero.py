# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P7_PotenciaNumero.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(781, 449)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_calcular = QtWidgets.QPushButton(self.centralwidget)
        self.btn_calcular.setGeometry(QtCore.QRect(220, 120, 401, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.btn_calcular.setFont(font)
        self.btn_calcular.setObjectName("btn_calcular")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txt_numero = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_numero.setGeometry(QtCore.QRect(170, 20, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.txt_numero.setFont(font)
        self.txt_numero.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_numero.setObjectName("txt_numero")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 30, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txt_exponente = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_exponente.setGeometry(QtCore.QRect(570, 20, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.txt_exponente.setFont(font)
        self.txt_exponente.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_exponente.setObjectName("txt_exponente")

        #######################################################################

        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        self.labelResult.setGeometry(QtCore.QRect(180, 260, 125, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelResult.setFont(font)
        self.labelResult.setObjectName("label")

        self.txt_resultado = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_resultado.setGeometry(QtCore.QRect(320, 250, 171, 71))
        self.txt_resultado.setObjectName("txt_resultado")

        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.txt_resultado.setFont(font)
        self.txt_resultado.setAlignment(QtCore.Qt.AlignCenter)

        ########################################################################


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 781, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_calcular.setText(_translate("MainWindow", "CALCULAR"))
        self.label.setText(_translate("MainWindow", "Número:"))
        self.label_2.setText(_translate("MainWindow", "Exponente:"))
