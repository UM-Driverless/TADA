# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1119, 854)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 60, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(30, 30, 211, 20))
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName("status")
        self.speed = QtWidgets.QLCDNumber(self.centralwidget)
        self.speed.setGeometry(QtCore.QRect(240, 60, 64, 23))
        self.speed.setObjectName("speed")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 66, 55, 20))
        self.label.setObjectName("label")
        self.lcdRpm = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdRpm.setGeometry(QtCore.QRect(640, 40, 64, 23))
        self.lcdRpm.setObjectName("lcdRpm")
        self.lcdEct = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdEct.setGeometry(QtCore.QRect(640, 70, 64, 23))
        self.lcdEct.setObjectName("lcdEct")
        self.lcdOilP = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdOilP.setGeometry(QtCore.QRect(640, 100, 64, 23))
        self.lcdOilP.setObjectName("lcdOilP")
        self.lcdTps = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdTps.setGeometry(QtCore.QRect(780, 40, 64, 23))
        self.lcdTps.setObjectName("lcdTps")
        self.lcdApps = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdApps.setGeometry(QtCore.QRect(780, 70, 64, 23))
        self.lcdApps.setObjectName("lcdApps")
        self.lcdBreakHdr = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdBreakHdr.setGeometry(QtCore.QRect(780, 100, 64, 23))
        self.lcdBreakHdr.setObjectName("lcdBreakHdr")
        self.lRpm = QtWidgets.QLabel(self.centralwidget)
        self.lRpm.setGeometry(QtCore.QRect(710, 46, 55, 20))
        self.lRpm.setObjectName("lRpm")
        self.lEct = QtWidgets.QLabel(self.centralwidget)
        self.lEct.setGeometry(QtCore.QRect(710, 76, 55, 20))
        self.lEct.setObjectName("lEct")
        self.lOilP = QtWidgets.QLabel(self.centralwidget)
        self.lOilP.setGeometry(QtCore.QRect(710, 106, 55, 20))
        self.lOilP.setObjectName("lOilP")
        self.lTps = QtWidgets.QLabel(self.centralwidget)
        self.lTps.setGeometry(QtCore.QRect(850, 46, 55, 20))
        self.lTps.setObjectName("lTps")
        self.lApps = QtWidgets.QLabel(self.centralwidget)
        self.lApps.setGeometry(QtCore.QRect(850, 76, 55, 20))
        self.lApps.setObjectName("lApps")
        self.lBreakHdr = QtWidgets.QLabel(self.centralwidget)
        self.lBreakHdr.setGeometry(QtCore.QRect(850, 106, 55, 20))
        self.lBreakHdr.setObjectName("lBreakHdr")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1119, 26))
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
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.status.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "Km/h"))
        self.lRpm.setText(_translate("MainWindow", "rpm"))
        self.lEct.setText(_translate("MainWindow", "ect"))
        self.lOilP.setText(_translate("MainWindow", "oilP"))
        self.lTps.setText(_translate("MainWindow", "tps"))
        self.lApps.setText(_translate("MainWindow", "apps"))
        self.lBreakHdr.setText(_translate("MainWindow", "breakHdr"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

