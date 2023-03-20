# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\admin\Desktop\weather_proje\weather.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.la_guncel = QtWidgets.QLabel(self.centralwidget)
        self.la_guncel.setGeometry(QtCore.QRect(80, 50, 651, 61))
        self.la_guncel.setStyleSheet("\n"
"color: rgb(85, 0, 127);\n"
"background-color: rgb(255, 167, 140);\n"
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.la_guncel.setObjectName("la_guncel")
        self.but_nl = QtWidgets.QPushButton(self.centralwidget)
        self.but_nl.setGeometry(QtCore.QRect(60, 240, 90, 50))
        self.but_nl.setStyleSheet("color: rgb(85, 0, 127);\n"
"background-color: rgb(255, 167, 140);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"")
        self.but_nl.setObjectName("but_nl")
        self.but_tr = QtWidgets.QPushButton(self.centralwidget)
        self.but_tr.setGeometry(QtCore.QRect(160, 240, 90, 50))
        self.but_tr.setStyleSheet("color: rgb(85, 0, 127);\n"
"background-color: rgb(255, 167, 140);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.but_tr.setObjectName("but_tr")
        self.but_gr = QtWidgets.QPushButton(self.centralwidget)
        self.but_gr.setGeometry(QtCore.QRect(260, 240, 90, 50))
        self.but_gr.setStyleSheet("color: rgb(85, 0, 127);\n"
"background-color: rgb(255, 167, 140);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.but_gr.setObjectName("but_gr")
        self.table_city_info = QtWidgets.QTableWidget(self.centralwidget)
        self.table_city_info.setGeometry(QtCore.QRect(60, 300, 291, 500))
        self.table_city_info.setStyleSheet("alternate-background-color: rgb(255, 182, 57);")
        self.table_city_info.setObjectName("table_city_info")
        self.table_city_info.setColumnCount(3)
        self.table_city_info.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_city_info.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_city_info.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_city_info.setHorizontalHeaderItem(2, item)
        self.li_city = QtWidgets.QLineEdit(self.centralwidget)
        self.li_city.setGeometry(QtCore.QRect(510, 290, 221, 20))
        self.li_city.setStyleSheet("color: rgb(85, 0, 127);\n"
"background-color: rgb(255, 167, 140);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.li_city.setObjectName("li_city")
        self.but_search = QtWidgets.QPushButton(self.centralwidget)
        self.but_search.setGeometry(QtCore.QRect(510, 330, 221, 20))
        self.but_search.setStyleSheet("color: rgb(85, 0, 127);\n"
"background-color: rgb(255, 167, 140);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.but_search.setObjectName("but_search")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 250, 221, 20))
        self.label.setStyleSheet("color: rgb(85, 0, 127);\n"
"background-color: rgb(255, 167, 140);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.la_weather = QtWidgets.QLabel(self.centralwidget)
        self.la_weather.setGeometry(QtCore.QRect(520, 400, 211, 161))
        self.la_weather.setStyleSheet("color: rgb(85, 0, 127);\n"
"background-color: rgb(255, 167, 140);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.la_weather.setText("")
        self.la_weather.setObjectName("la_weather")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.la_guncel.setText(_translate("MainWindow", "WELCOME TO ::::::WEATER APLLICATION?????"))
        self.but_nl.setText(_translate("MainWindow", "NEDERLAND"))
        self.but_tr.setText(_translate("MainWindow", "TURKEY"))
        self.but_gr.setText(_translate("MainWindow", "GERMANY"))
        item = self.table_city_info.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "CITY"))
        item = self.table_city_info.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "POPULATION"))
        item = self.table_city_info.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "REGION"))
        self.but_search.setText(_translate("MainWindow", "SEARCH WEATHER"))
        self.label.setText(_translate("MainWindow", "      PLEASE ENTER CITY NAME"))
        
        
        
if __name__ == "__main__":
        
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
