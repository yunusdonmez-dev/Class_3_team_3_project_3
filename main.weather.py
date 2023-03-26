from PyQt5 import QtWidgets
import requests,pymongo
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Ui_weather import *

class Main_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        
        super(Main_Window,self).__init__()
        self.weatherform=Ui_MainWindow()
        self.weatherform.setupUi(self)
    
        self.client=pymongo.MongoClient('mongodb+srv://yunus:1234@cluster0.lytui3m.mongodb.net/?retryWrites=true&w=majority')
        self.db=self.client["WeatherApp"]
        self.collection=self.db["WeatherInfos"]
        self.city_germany=self.db["Germany"]
        self.city_holland=self.db["Netherland"]
        self.city_usa=self.db["USA"]
        self.weatherform.table_cities.cellClicked.connect(self.show_weather_data)
        self.weatherform.but_search.clicked.connect(self.show_weather_data)
        self.weatherform.table_cities.itemSelectionChanged.connect(self.city_info_gr)
        self.weatherform.table_cities.itemSelectionChanged.connect(self.city_info_nl)
        self.weatherform.table_cities.itemSelectionChanged.connect(self.city_info_usa)
        
        self.weatherform.but_usa.clicked.connect(self.get_usa_citys)
        self.weatherform.but_gr.clicked.connect(self.get_gr_citys)
        self.weatherform.but_nl.clicked.connect(self.get_nl_citys)
        
    def show_weather_data(self,row,column):
        row_current= self.weatherform.table_cities.currentRow()
        column_current=self.weatherform.table_cities.currentColumn()
        self.city_name=self.weatherform.table_cities.item(row_current,column_current).text()
        #you need an api key to get data.take an api key from website
        self.API="fb3328815f2ebd7034f6b56edaaffcda"
        
        self.BASE_URL="https://api.openweathermap.org/data/2.5/weather?"
        #self.CITY_NAME=self.combo_city.currentText( )
        #create url with your choice
        self.URL=self.BASE_URL + "appid=" + self.API + "&q=" +self.city_name
         #get data with requests
        get_data=requests.get(self.URL)
         #get jason format
        get_data_JSON=get_data.json()
       
        
        if (get_data_JSON["cod"] !="404"):
            #if you get 404,you can't get data
            temp=get_data_JSON["main"]["temp"]
            description=get_data_JSON["weather"][0]["description"]
            pressure=get_data_JSON["main"]["pressure"]
            country=get_data_JSON["sys"]["country"]
            icon=get_data_JSON["weather"][0]["icon"]
            
            self.weatherform.la_temperature.setText(str(int(float(temp)-273.15))+"C°")
            self.weatherform.la_description.setText(description)
            self.weatherform.la_pressure.setText(str(pressure))
            self.weatherform.la_country.setText(country)
            self.weatherform.la_city.setText(self.city_name)
          
            #insert mongodb
            item={"country":self.weatherform.la_country.text(),
                  "city_name":self.city_name,
                  "temperature":temp,
                  "description":description,
                  "pressure":pressure,
                  
                
            }
            try:
                self.collection.insert_one(item)
            except  pymongo.errors.WriteError as ERROR:
                print("Error:",ERROR)    
                 
            #convert celcius
            print("temp : " , str(int(float(temp)-273.15)))
           
            print("description : " , description)
            
            print("pressure : " , pressure)
            print("country : " , country)
            print("city : " , self.city_name)
            print("icon:",icon)
            
        else:
            print("This country can not find, please enter correctly") 

    
    
    def get_usa_citys(self):
        info_cities=self.city_usa.find({"country":"USA"},{"city":1,"population":1,"region":1})
        rows_info=[]
        for i in info_cities:
            rows_info.append(i)
            
            
        row=0
        self.weatherform.table_cities.setRowCount(len(rows_info))
        for i in rows_info:
            self.weatherform.table_cities.setItem(row, 0, QtWidgets.QTableWidgetItem(i["city"]))
            self.weatherform.table_cities.setItem(row, 1, QtWidgets.QTableWidgetItem(str(i["population"])))
            self.weatherform.table_cities.setItem(row, 2, QtWidgets.QTableWidgetItem(i["region"]))
            row +=1   
    def get_gr_citys(self):
        info_cities=self.city_germany.find({"country":"Germany"},{"city":1,"population":1,"region":1})
        rows_info=[]
        for i in info_cities:
            rows_info.append(i)
            
            
        row=0
        self.weatherform.table_cities.setRowCount(len(rows_info))
        for i in rows_info:
            self.weatherform.table_cities.setItem(row, 0, QtWidgets.QTableWidgetItem(i["city"]))
            self.weatherform.table_cities.setItem(row, 1, QtWidgets.QTableWidgetItem(i["population"]))
            self.weatherform.table_cities.setItem(row, 2, QtWidgets.QTableWidgetItem(i["region"]))
            row +=1   
            
            
    def get_nl_citys(self):
        info_cities=self.city_holland.find({"country":"Holland"},{"city":1,"population":1,"region":1})
        rows_info=[]
        for i in info_cities:
            rows_info.append(i)
            
            
        row=0
        self.weatherform.table_cities.setRowCount(len(rows_info))
        for i in rows_info:
            self.weatherform.table_cities.setItem(row, 0, QtWidgets.QTableWidgetItem(i["city"]))
            self.weatherform.table_cities.setItem(row, 1, QtWidgets.QTableWidgetItem(str(i["population"])))
            self.weatherform.table_cities.setItem(row, 2, QtWidgets.QTableWidgetItem(i["region"]))
            row +=1 
    def city_info_nl(self):
        selected_nl=self.weatherform.table_cities.selectedItems()
        if len (selected_nl)==0:
            return
        selected_city=selected_nl[0].text()
        x={"country":"Netherland","city":selected_city}
        nl_info=self.city_holland.find_one(x)
        if not nl_info:
            return
        self.weatherform.la_country.setText("Netherland")
        self.weatherform.la_population.settext(str(nl_info["population"]))
        self.weatherform.la_region.setText(nl_info["region"])
        
    def city_info_gr(self):
        selected_gr=self.weatherform.table_cities.selectedItems()
        if len (selected_gr)==0:
            return
        selected_city=selected_gr[0].text()
        x={"country":"Germany","city":selected_city}
        gr_info=self.city_germany.find_one(x)
        if not gr_info:
            return
        self.weatherform.la_country.setText("Germany")
        self.weatherform.la_population.setText(str(gr_info["population"]))
        self.weatherform.la_region.setText(gr_info["region"])
        
    def city_info_usa(self):
        selected_usa=self.weatherform.table_cities.selectedItems()
        if len (selected_usa)==0:
            return
        selected_city=selected_usa[0].text()
        x={"country":"Usa","city":selected_city}
        usa_info=self.city_usa.find_one(x)
        if not usa_info:
            return
        self.weatherform.la_country.setText("Usa")
        self.weatherform.la_population.settext(str(usa_info["population"]))
        self.weatherform.la_region.setText(usa_info["region"])
        

    
if __name__ == "__main__":
        app = QApplication(sys.argv)
        Main_Window = Main_Window()
        widget = QtWidgets.QStackedWidget()
        widget.addWidget(Main_Window)
        
        widget.show()
        
        try:
            sys.exit(app.exec_())
        
        except:
            print("Exit App")    
