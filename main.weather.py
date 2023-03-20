from PyQt5 import QtWidgets
import requests
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class WeatherApp(QtWidgets.QWidget):
    def __init__(self):
        super(WeatherApp,self).__init__()
        loadUi("weather.ui", self)
        
        self.combo_country = QtWidgets.QComboBox()
        self.combo_city = QtWidgets.QComboBox()
        self.search_button = QtWidgets.QPushButton('Search')
        self.la_result = QtWidgets.QLabel('')
        self.la_city_info=QtWidgets.QLabel('')
        self.search_button.clicked.connect(self.show_weather_data)
        
    def get_weather_data(self):
        #you need an api key to get data.take an api key from website
        self.API="fb3328815f2ebd7034f6b56edaaffcda"
        
        self.BASE_URL="https://api.openweathermap.org/data/2.5/weather?"
        self.CITY_NAME=self.combo_city.currentText( )
        #create url with your choice
        self.URL=self.BASE_URL + "appid=" + self.API + "&q=" +self.CITY_NAME
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
            
            print("temp : " , str(int(float(temp)-273.15)))
            #convert celcius
            print("description : " , description)
            print("pressure : " , pressure)
            print("country : " , country)
            print("city : " , self.CITY_NAME)
            
        else:
            print("This country can not find, please enter correctly") 

    def show_weather_data(self):
        pass

    
    if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = WeatherApp()
        widget = QStackedWidget()
        widget.addWidget(window)
      
        widget.show()
        
    
