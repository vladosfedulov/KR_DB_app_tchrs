import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

import design
from query import query_in, query_ins

DB_REQUEST_SEl1 = """select * from zanyatie 
                where Den_nedeli = '{}'
                AND Nomer_pari = '{}'
                AND Nedela = '{}' 
                AND N_Auditorii = '{}'"""
DB_REQUEST_INS1 = """insert into zamena values ('{}','{}','{}',{},{},'{}','{}',{},{},'{}') """
DB_REQUEST_INS2 = """insert into rest values ('{}','{}','{}','{}') """
DB_REQUEST_INS3 = """Select X1.Nomer_pari,X2.Nazvanie_discipl,X1.N_Auditorii,X1.N_gruppi,X2.Nedela
                from gruppazanyatie X1 INNER JOIN zanyatie X2 ON (X1.Nomer_pari = X2.Nomer_pari 
                AND X1.Den_nedeli = X2.Den_nedeli AND X1.N_Auditorii = X2.N_Auditorii) 
                where X2.FIO_prep  = '{}' AND X1.Den_nedeli = '{}'
                group by X1.Nomer_pari,X2.Nazvanie_discipl,X1.N_Auditorii,X2.Nedela;"""


class ExampleDialog(QtWidgets.QMainWindow, design.Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


class ExampleDialogErr(QtWidgets.QMainWindow, design.Ui_DialogErr):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dialog = ExampleDialog()
        self.dialog.hide()
        self.dialog_err = ExampleDialogErr()
        self.dialog_err.hide()

        self.comboBox.activated[str].connect(self.combo_activated)
        self.pushButton.clicked.connect(self.btn_clk)
        self.pushButton_2.clicked.connect(self.btn2_clk)

    def btn2_clk(self):
        date1 = self.calendarWidget.selectedDate()
        date2 = self.calendarWidget_2.selectedDate()
        query_ins(DB_REQUEST_INS2.format(self.comboBox.currentText(), date1.toString(Qt.ISODate),
                                         date2.toString(Qt.ISODate), self.comboBox_9.currentText()))

    def btn_clk(self):
        cortege = []
        if self.comboBox_10.currentText() == '-':
            dayoftheweek_cb10 = 0
        if self.comboBox_10.currentText() == 'Верх':
            dayoftheweek_cb10 = 1
        if self.comboBox_10.currentText() == 'Низ':
            dayoftheweek_cb10 = 2
        if self.comboBox_11.currentText() == '-':
            dayoftheweek_cb11 = 0
        if self.comboBox_11.currentText() == 'Верх':
            dayoftheweek_cb11 = 1
        if self.comboBox_11.currentText() == 'Низ':
            dayoftheweek_cb11 = 2

        cortege.append(self.comboBox.currentText())
        cortege.append(self.comboBox_5.currentText())
        cortege.append(self.comboBox_2.currentText())
        cortege.append(self.comboBox_3.currentText())
        cortege.append(self.comboBox_4.currentText())
        cortege.append(self.comboBox_6.currentText())
        cortege.append(self.comboBox_7.currentText())
        cortege.append(self.comboBox_8.currentText())

        query = query_in(DB_REQUEST_SEl1.format(cortege[5], int(cortege[6]), dayoftheweek_cb11, cortege[7]))

        if query:
            query_ins(DB_REQUEST_INS1.format(cortege[0], cortege[1], cortege[2], int(cortege[3]), dayoftheweek_cb10,
                                        cortege[4], cortege[5], int(cortege[6]), dayoftheweek_cb11, cortege[7]))
            self.dialog.show()
        else:
            self.dialog_err.show()

    def combo_activated(self, text):
        day_of_week = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота')
        self.textEdit.clear()

        for chosen_day in day_of_week:
            self.textEdit.append('\t')
            self.textEdit.append('<font size="5"><u>' + chosen_day + '</u></font>')
            try:

                query = query_in(DB_REQUEST_INS3.format(str(text), chosen_day))
                if query:
                    for cortege in query:
                        if cortege[4] == 1:
                            self.textEdit.append(
                                '<font size="4"><span style="color: red;">' + str(cortege[0]) +
                                '</span>' + ' - ' + cortege[1] + ' ' + ' - ' + cortege[2] +'</font>')
                        if cortege[4] == 2:
                            self.textEdit.append(
                                '<font size="4"><span style="color: blue;">' + str(cortege[0]) +
                                '</span>' + ' - ' + cortege[1] + ' ' + ' - ' + cortege[2] + '</font>')
                        if cortege[4] == 0:
                            self.textEdit.append(
                                '<font size="4"><span style="color: black;">' + str(cortege[0]) +
                                '</span>' + ' - ' + cortege[1] + ' ' + ' - ' + cortege[2] + '</font>')

                else:
                    self.textEdit.append("\nВыходной")

            except:
                self.textEdit.append("Error")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()

    window.show()
    app.exec_()

if __name__ == '__main__':
    main()