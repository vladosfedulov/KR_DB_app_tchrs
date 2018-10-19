# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

from query import query_in


DB_REQUEST_IN = "select distinct FIO_prep from zanyatie"
DB_REQUEST_IN1 = """Select N_Auditirii from auditiria;"""
DB_REQUEST_IN2 = """Select distinct Nazvanie_discipl from zanyatie;"""
DAY_OF_WEEK = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 614)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 911, 611))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(400, 70, 91, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab)
        self.comboBox_3.setGeometry(QtCore.QRect(500, 70, 31, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab)
        self.comboBox_4.setGeometry(QtCore.QRect(600, 70, 81, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_5 = QtWidgets.QComboBox(self.tab)
        self.comboBox_5.setGeometry(QtCore.QRect(690, 70, 241, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_6 = QtWidgets.QComboBox(self.tab)
        self.comboBox_6.setGeometry(QtCore.QRect(400, 150, 91, 22))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_7 = QtWidgets.QComboBox(self.tab)
        self.comboBox_7.setGeometry(QtCore.QRect(500, 150, 31, 22))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_8 = QtWidgets.QComboBox(self.tab)
        self.comboBox_8.setGeometry(QtCore.QRect(600, 150, 81, 22))
        self.comboBox_8.setObjectName("comboBox_8")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(400, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 361, 531))
        self.textEdit.setMouseTracking(False)
        self.textEdit.setObjectName("textEdit")
        self.comboBox_10 = QtWidgets.QComboBox(self.tab)
        self.comboBox_10.setGeometry(QtCore.QRect(540, 70, 51, 22))
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_11 = QtWidgets.QComboBox(self.tab)
        self.comboBox_11.setGeometry(QtCore.QRect(540, 150, 51, 22))
        self.comboBox_11.setObjectName("comboBox_11")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.comboBox_9 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_9.setGeometry(QtCore.QRect(10, 250, 141, 22))
        self.comboBox_9.setObjectName("comboBox_9")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 290, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab_2)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 30, 296, 183))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(self.tab_2)
        self.calendarWidget_2.setGeometry(QtCore.QRect(340, 30, 296, 183))
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "УЧИТЕЛЪ"))
        self.pushButton.setText(_translate("MainWindow", "Заменить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Занятия"))
        self.pushButton_2.setText(_translate("MainWindow", "Оповестить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Оповещение"))

        position_cb = 0

        self.comboBox_9.addItem("")
        self.comboBox_9.setItemText(position_cb, _translate("MainWindow", '-'))

        for fio in query_in(DB_REQUEST_IN):
            self.comboBox.addItem("")
            self.comboBox.setItemText(position_cb, _translate("MainWindow", fio[0]))
            self.comboBox_9.addItem("")
            self.comboBox_9.setItemText(position_cb+1, _translate("MainWindow", fio[0]))
            position_cb += 1

        position_cb = 0

        for chosen_day in DAY_OF_WEEK:
            self.comboBox_2.addItem("")
            self.comboBox_2.setItemText(position_cb, _translate("MainWindow", chosen_day))
            self.comboBox_6.addItem("")
            self.comboBox_6.setItemText(position_cb, _translate("MainWindow", chosen_day))
            position_cb += 1

        position_cb = 0

        for x in range(1,9):
            self.comboBox_3.addItem("")
            self.comboBox_3.setItemText(position_cb, _translate("MainWindow", str(x)))
            self.comboBox_7.addItem("")
            self.comboBox_7.setItemText(position_cb, _translate("MainWindow", str(x)))
            position_cb += 1

        query = query_in(DB_REQUEST_IN1)
        position_cb = 0

        for cortege in query:
            self.comboBox_4.addItem("")
            self.comboBox_4.setItemText(position_cb, _translate("MainWindow", cortege[0]))
            self.comboBox_8.addItem("")
            self.comboBox_8.setItemText(position_cb, _translate("MainWindow", cortege[0]))
            position_cb += 1

        query = query_in(DB_REQUEST_IN2)
        position_cb = 0

        for cortege in query:
            self.comboBox_5.addItem("")
            self.comboBox_5.setItemText(position_cb, _translate("MainWindow", cortege[0]))
            position_cb += 1

        self.comboBox_10.addItem("")
        self.comboBox_10.setItemText(0, _translate("MainWindow", "Верх"))
        self.comboBox_11.addItem("")
        self.comboBox_11.setItemText(0, _translate("MainWindow", "Верх"))

        self.comboBox_10.addItem("")
        self.comboBox_10.setItemText(1, _translate("MainWindow", "Низ"))
        self.comboBox_11.addItem("")
        self.comboBox_11.setItemText(1, _translate("MainWindow", "Низ"))

        self.comboBox_10.addItem("")
        self.comboBox_10.setItemText(2, _translate("MainWindow", "-"))
        self.comboBox_11.addItem("")
        self.comboBox_11.setItemText(2, _translate("MainWindow", "-"))