# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\yunus\OneDrive\Desktop\ATM-PROJECKT-2-TEAM-2-main\Class_3_team_3_project_3\weather.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 900)
        MainWindow.setMinimumSize(QtCore.QSize(800, 900))
        MainWindow.setMaximumSize(QtCore.QSize(800, 900))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.but_nl = QtWidgets.QPushButton(self.centralwidget)
        self.but_nl.setGeometry(QtCore.QRect(29, 470, 121, 91))
        self.but_nl.setStyleSheet("color: rgb(0, 0, 138);\n"
"background-color: rgb(255, 255, 255, 128);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;\n"
"\n"
"")
        self.but_nl.setObjectName("but_nl")
        self.but_usa = QtWidgets.QPushButton(self.centralwidget)
        self.but_usa.setGeometry(QtCore.QRect(30, 690, 121, 91))
        self.but_usa.setStyleSheet("color: rgb(0, 0, 138);\n"
"background-color: rgb(255, 255, 255, 128);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;\n"
"")
        self.but_usa.setObjectName("but_usa")
        self.but_gr = QtWidgets.QPushButton(self.centralwidget)
        self.but_gr.setGeometry(QtCore.QRect(30, 580, 121, 91))
        self.but_gr.setStyleSheet("color: rgb(0, 0, 138);\n"
"background-color: rgb(255, 255, 255, 128);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;\n"
"")
        self.but_gr.setObjectName("but_gr")
        self.table_cities = QtWidgets.QTableWidget(self.centralwidget)
        self.table_cities.setGeometry(QtCore.QRect(180, 470, 381, 311))
        self.table_cities.setStyleSheet("background-color: transparent;\n"
"")
        self.table_cities.setShowGrid(False)
        self.table_cities.setGridStyle(QtCore.Qt.SolidLine)
        self.table_cities.setObjectName("table_cities")
        self.table_cities.setColumnCount(3)
        self.table_cities.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_cities.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_cities.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_cities.setHorizontalHeaderItem(2, item)
        self.li_city = QtWidgets.QLineEdit(self.centralwidget)
        self.li_city.setGeometry(QtCore.QRect(550, 300, 221, 61))
        self.li_city.setStyleSheet("color: rgb(0, 0, 138);\n"
"background-color: rgb(255, 255, 255, 128);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;\n"
"")
        self.li_city.setText("")
        self.li_city.setFrame(False)
        self.li_city.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.li_city.setAlignment(QtCore.Qt.AlignCenter)
        self.li_city.setObjectName("li_city")
        self.but_search = QtWidgets.QPushButton(self.centralwidget)
        self.but_search.setGeometry(QtCore.QRect(550, 380, 221, 51))
        self.but_search.setStyleSheet("color: rgb(0, 0, 138);\n"
"background-color: rgb(255, 255, 255, 128);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;\n"
"")
        self.but_search.setObjectName("but_search")
        self.la_description = QtWidgets.QLabel(self.centralwidget)
        self.la_description.setGeometry(QtCore.QRect(290, 260, 241, 71))
        self.la_description.setStyleSheet("color: rgb(0, 0, 138);\n"
"background-color: rgb(255, 255, 255, 10);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.la_description.setText("")
        self.la_description.setAlignment(QtCore.Qt.AlignCenter)
        self.la_description.setObjectName("la_description")
        self.la_temperature = QtWidgets.QLabel(self.centralwidget)
        self.la_temperature.setGeometry(QtCore.QRect(260, 80, 301, 211))
        self.la_temperature.setStyleSheet("color: rgb(0, 0, 138);\n"
"background-color: rgb(255, 255, 255, 10);\n"
"font: 75 66pt \"MS Shell Dlg 2\";")
        self.la_temperature.setFrameShadow(QtWidgets.QFrame.Plain)
        self.la_temperature.setText("")
        self.la_temperature.setScaledContents(False)
        self.la_temperature.setAlignment(QtCore.Qt.AlignCenter)
        self.la_temperature.setObjectName("la_temperature")
        self.la_city = QtWidgets.QLabel(self.centralwidget)
        self.la_city.setGeometry(QtCore.QRect(140, 50, 541, 61))
        self.la_city.setStyleSheet("color: rgb(0, 0, 138);\n"
"background-color: rgb(255, 255, 255, 10);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.la_city.setText("")
        self.la_city.setAlignment(QtCore.Qt.AlignCenter)
        self.la_city.setObjectName("la_city")
        self.la_country = QtWidgets.QLabel(self.centralwidget)
        self.la_country.setGeometry(QtCore.QRect(60, 40, 81, 91))
        self.la_country.setStyleSheet("color: rgb(0, 0, 138);\n"
"background-color: rgb(255, 255, 255, 10);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.la_country.setText("")
        self.la_country.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.la_country.setObjectName("la_country")
        self.la_region = QtWidgets.QLabel(self.centralwidget)
        self.la_region.setGeometry(QtCore.QRect(40, 180, 141, 121))
        self.la_region.setMaximumSize(QtCore.QSize(141, 121))
        self.la_region.setStyleSheet("color: rgb(0, 0, 138);\n"
"background-color: rgb(255, 255, 255, 10);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.la_region.setText("")
        self.la_region.setTextFormat(QtCore.Qt.AutoText)
        self.la_region.setScaledContents(False)
        self.la_region.setObjectName("la_region")
        self.la_population = QtWidgets.QLabel(self.centralwidget)
        self.la_population.setGeometry(QtCore.QRect(360, 390, 171, 61))
        self.la_population.setStyleSheet("color: rgb(0, 0, 138);\n"
"background-color: rgb(255, 255, 255, 10);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.la_population.setText("")
        self.la_population.setObjectName("la_population")
        self.la_pressure = QtWidgets.QLabel(self.centralwidget)
        self.la_pressure.setGeometry(QtCore.QRect(320, 320, 171, 71))
        self.la_pressure.setStyleSheet("color: rgb(0, 0, 138);\n"
"background-color: rgb(255, 255, 255, 10);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.la_pressure.setText("")
        self.la_pressure.setAlignment(QtCore.Qt.AlignCenter)
        self.la_pressure.setObjectName("la_pressure")
        self.la_pressure_lbl = QtWidgets.QLabel(self.centralwidget)
        self.la_pressure_lbl.setGeometry(QtCore.QRect(220, 320, 151, 71))
        self.la_pressure_lbl.setStyleSheet("background-color: rgb(255, 255, 255, 10);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 138);\n"
"\n"
"")
        self.la_pressure_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.la_pressure_lbl.setObjectName("la_pressure_lbl")
        self.la_population_lbl = QtWidgets.QLabel(self.centralwidget)
        self.la_population_lbl.setGeometry(QtCore.QRect(220, 380, 131, 71))
        self.la_population_lbl.setStyleSheet("background-color: rgb(255, 255, 255, 10);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 138);\n"
"")
        self.la_population_lbl.setObjectName("la_population_lbl")
        self.la_time = QtWidgets.QLabel(self.centralwidget)
        self.la_time.setGeometry(QtCore.QRect(590, 10, 71, 21))
        self.la_time.setStyleSheet("background-color: rgb(255, 255, 255, 10);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 138);")
        self.la_time.setObjectName("la_time")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(670, 10, 111, 21))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255, 10);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 138);")
        self.label.setText("")
        self.label.setObjectName("label")
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
        self.but_nl.setText(_translate("MainWindow", "NEDERLAND"))
        self.but_usa.setText(_translate("MainWindow", "USA"))
        self.but_gr.setText(_translate("MainWindow", "GERMANY"))
        item = self.table_cities.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "CITY"))
        item = self.table_cities.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "POPULATION"))
        item = self.table_cities.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "REGION"))
        self.li_city.setPlaceholderText(_translate("MainWindow", "Please Enter City Name"))
        self.but_search.setText(_translate("MainWindow", "SEARCH WEATHER"))
        self.la_pressure_lbl.setText(_translate("MainWindow", "Pressure(N/m2):"))
        self.la_population_lbl.setText(_translate("MainWindow", "Population:"))
        self.la_time.setText(_translate("MainWindow", "Local Time :"))
