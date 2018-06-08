# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AMUDIS_camera_control.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(734, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loadCamera = QtWidgets.QPushButton(self.centralwidget)
        self.loadCamera.setGeometry(QtCore.QRect(10, 20, 81, 21))
        self.loadCamera.setObjectName("loadCamera")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 89, 181, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.begin_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.begin_label.setObjectName("begin_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.begin_label)
        self.dateTimeEdit_begin = QtWidgets.QDateTimeEdit(self.formLayoutWidget)
        self.dateTimeEdit_begin.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 5, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit_begin.setDate(QtCore.QDate(2018, 5, 1))
        self.dateTimeEdit_begin.setTime(QtCore.QTime(0, 0, 0))
        self.dateTimeEdit_begin.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit_begin.setCalendarPopup(True)
        self.dateTimeEdit_begin.setObjectName("dateTimeEdit_begin")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateTimeEdit_begin)
        self.dateTimeEdit_end = QtWidgets.QDateTimeEdit(self.formLayoutWidget)
        self.dateTimeEdit_end.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 5, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit_end.setDate(QtCore.QDate(2018, 5, 1))
        self.dateTimeEdit_end.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit_end.setCalendarPopup(True)
        self.dateTimeEdit_end.setObjectName("dateTimeEdit_end")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dateTimeEdit_end)
        self.end_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.end_label.setObjectName("end_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.end_label)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 231, 16))
        self.label_3.setObjectName("label_3")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(10, 170, 81, 21))
        self.startButton.setObjectName("startButton")
        self.takePictureButton = QtWidgets.QPushButton(self.centralwidget)
        self.takePictureButton.setGeometry(QtCore.QRect(130, 20, 75, 23))
        self.takePictureButton.setObjectName("takePictureButton")
        self.objectSettings = QtWidgets.QStackedWidget(self.centralwidget)
        self.objectSettings.setGeometry(QtCore.QRect(370, 0, 191, 281))
        self.objectSettings.setObjectName("objectSettings")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.page)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(0, 40, 160, 80))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.ExposureValue = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.ExposureValue.setObjectName("ExposureValue")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ExposureValue)
        self.labelExposure = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.labelExposure.setObjectName("labelExposure")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelExposure)
        self.tempsensorlabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.tempsensorlabel.setObjectName("tempsensorlabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.tempsensorlabel)
        self.TempSensorValue = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.TempSensorValue.setObjectName("TempSensorValue")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.TempSensorValue)
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(40, 10, 91, 20))
        self.label.setObjectName("label")
        self.pushButtonLoadSettings = QtWidgets.QPushButton(self.page)
        self.pushButtonLoadSettings.setGeometry(QtCore.QRect(0, 240, 75, 23))
        self.pushButtonLoadSettings.setObjectName("pushButtonLoadSettings")
        self.objectSettings.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.objectSettings.addWidget(self.page_2)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 220, 81, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.MeasurementNo = QtWidgets.QLabel(self.centralwidget)
        self.MeasurementNo.setGeometry(QtCore.QRect(10, 200, 91, 20))
        self.MeasurementNo.setObjectName("MeasurementNo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 734, 21))
        self.menubar.setObjectName("menubar")
        self.menuProgram = QtWidgets.QMenu(self.menubar)
        self.menuProgram.setObjectName("menuProgram")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionInitialize_system = QtWidgets.QAction(MainWindow)
        self.actionInitialize_system.setObjectName("actionInitialize_system")
        self.menuProgram.addAction(self.actionInitialize_system)
        self.menuProgram.addSeparator()
        self.menuProgram.addAction(self.actionQuit)
        self.menubar.addAction(self.menuProgram.menuAction())

        self.retranslateUi(MainWindow)
        self.objectSettings.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AMUDIS Control"))
        self.loadCamera.setText(_translate("MainWindow", "Load Camera"))
        self.begin_label.setText(_translate("MainWindow", "Begin"))
        self.end_label.setText(_translate("MainWindow", "End"))
        self.label_3.setText(_translate("MainWindow", "Measurement Setting"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.takePictureButton.setText(_translate("MainWindow", "Take Picture"))
        self.ExposureValue.setText(_translate("MainWindow", "200"))
        self.labelExposure.setText(_translate("MainWindow", "Exposure(ms)"))
        self.tempsensorlabel.setText(_translate("MainWindow", "Temperature Sensor"))
        self.TempSensorValue.setText(_translate("MainWindow", "-65"))
        self.label.setText(_translate("MainWindow", "Settings Sensor"))
        self.pushButtonLoadSettings.setText(_translate("MainWindow", "Load Settings"))
        self.MeasurementNo.setText(_translate("MainWindow", "Measurement No:"))
        self.menuProgram.setTitle(_translate("MainWindow", "Program"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionInitialize_system.setText(_translate("MainWindow", "Initialize system"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
