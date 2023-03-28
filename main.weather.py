from PyQt5 import QtWidgets
import requests,pymongo
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Ui_weather import *
import pytz     # pip install pytz
from datetime import datetime
from geopy.geocoders import Nominatim  # pip install geopy
from timezonefinder import TimezoneFinder #pip install timezonefinder

# initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")

class Main_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        
        super(Main_Window,self).__init__()
        self.weatherform=Ui_MainWindow()
        self.weatherform.setupUi(self)

        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, self.width(), self.height())

        self.set_background('BackgroundImages\Telefon Duvar Kağıdı, Background Tasarımı.jpg')
        self.background_label.lower()
    
        self.client=pymongo.MongoClient('mongodb+srv://yunus:1234@cluster0.lytui3m.mongodb.net/?retryWrites=true&w=majority')
        self.db=self.client["WeatherApp"]
        self.city_germany=self.db["Germany"]
        self.city_holland=self.db["Netherland"]
        self.city_usa=self.db["USA"]
        self.show_weather_data_3()
        self.weatherform.table_cities.cellClicked.connect(self.show_weather_data)
        self.weatherform.but_search.clicked.connect(self.show_weather_data_2)
        
 
        self.get_nl_citys()             #Default Country
        self.weatherform.but_usa.clicked.connect(self.get_usa_citys)
        self.weatherform.but_gr.clicked.connect(self.get_gr_citys)
        self.weatherform.but_nl.clicked.connect(self.get_nl_citys)
    
    def set_background(self, path):
        self.background_label.setPixmap(QPixmap(path))
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        
    def show_weather_data(self):
        try:
            row_current= self.weatherform.table_cities.currentRow()
            column_current=self.weatherform.table_cities.currentColumn()
            self.city_name=self.weatherform.table_cities.item(row_current,column_current).text()
            self.population = self.weatherform.table_cities.item(row_current,column_current+1).text()
            self.region = self.weatherform.table_cities.item(row_current,column_current+2).text()
            
        
            #you need an api key to get data.take an api key from website
            self.API="fb3328815f2ebd7034f6b56edaaffcda"
            
            self.BASE_URL="https://api.openweathermap.org/data/2.5/weather?"
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
                if description == "clear sky":
                    self.set_background('BackgroundImages\Deniz Kenarı Gökyüzü Martılar Günaydın Temalı Instagram Hikayesi.jpg')
                elif description == "mist":
                    self.set_background('BackgroundImages\Gray Minimalist Nature Mindset Inspirational Quote Instagram Reel.jpg')
                pressure=get_data_JSON["main"]["pressure"]
                country=get_data_JSON["sys"]["country"]
                icon=get_data_JSON["weather"][0]["icon"]
                
                location = geolocator.geocode(self.city_name)
                obj = TimezoneFinder()
                result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
                timezone = pytz.timezone(result)  # replace with the timezone of the city
                local_time = datetime.now(timezone)
                self.weatherform.label.setText(local_time.strftime('%H:%M:%S'))
                
                self.weatherform.la_temperature.setText(str(int(float(temp)-273.15))+"C°")
                self.weatherform.la_description.setText(description)
                self.weatherform.la_pressure.setText(str(pressure))
                self.weatherform.la_country.setText(country)
                self.weatherform.la_city.setText(self.city_name)
                self.weatherform.la_population.setText(self.population)
                self.weatherform.la_region.setText(self.region)
                
            else:
                print("This country can not find, please enter correctly") 
        except :
            return

    def show_weather_data_2(self):


        self.city_name=self.weatherform.li_city.text()
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
            if description == "clear sky":
                self.set_background('BackgroundImages\Deniz Kenarı Gökyüzü Martılar Günaydın Temalı Instagram Hikayesi.jpg')
            elif description == "mist":
                self.set_background('BackgroundImages\Gray Minimalist Nature Mindset Inspirational Quote Instagram Reel.jpg')
            pressure=get_data_JSON["main"]["pressure"]
            country=get_data_JSON["sys"]["country"]
            icon=get_data_JSON["weather"][0]["icon"]
            
            location = geolocator.geocode(self.city_name)
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
            timezone = pytz.timezone(result)  # replace with the timezone of the city
            local_time = datetime.now(timezone)
            self.weatherform.label.setText(local_time.strftime('%H:%M:%S'))
            
            self.weatherform.la_temperature.setText(str(int(float(temp)-273.15))+"C°")
            self.weatherform.la_description.setText(description)
            self.weatherform.la_pressure.setText(str(pressure))
            self.weatherform.la_country.setText(country)
            self.weatherform.la_city.setText(self.city_name)
            try:
                self.weatherform.la_population.setText(str(self.db.Germany.find_one({"city":f"{self.city_name}"})['population']))
            except:
                pass
            try:
                self.weatherform.la_population.setText(str(self.db.Netherland.find_one({"city":f"{self.city_name}"})['population']))
            except:
                pass
            try:
                self.weatherform.la_population.setText(str(self.db.USA.find_one({"city":f"{self.city_name}"})['population']))
            except:
                pass
            try:
                self.weatherform.la_region.setText(str(self.db.Germany.find_one({"city":f"{self.city_name}"})['region']))
            except:
                pass
            try:
                self.weatherform.la_region.setText(str(self.db.Netherland.find_one({"city":f"{self.city_name}"})['region']))
            except:
                pass
            try:
                self.weatherform.la_region.setText(str(self.db.USA.find_one({"city":f"{self.city_name}"})['region']))
            except:
                pass
    def show_weather_data_3(self):

        '''
        Default city at the opening
        '''
        self.city_name='Amsterdam'
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
            if description == "clear sky":
                self.set_background('BackgroundImages\Deniz Kenarı Gökyüzü Martılar Günaydın Temalı Instagram Hikayesi.jpg')
            elif description == "mist":
                self.set_background('BackgroundImages\Gray Minimalist Nature Mindset Inspirational Quote Instagram Reel.jpg')
            pressure=get_data_JSON["main"]["pressure"]
            country=get_data_JSON["sys"]["country"]
            icon=get_data_JSON["weather"][0]["icon"]

            location = geolocator.geocode(self.city_name)
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
            timezone = pytz.timezone(result)  # replace with the timezone of the city
            local_time = datetime.now(timezone)
            self.weatherform.label.setText(local_time.strftime('%H:%M:%S'))
            # print(f"Current time in {self.city_name}: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")
            
            self.weatherform.la_temperature.setText(str(int(float(temp)-273.15))+"C°")
            self.weatherform.la_description.setText(description)
            self.weatherform.la_pressure.setText(str(pressure))
            self.weatherform.la_country.setText(country)
            self.weatherform.la_city.setText(self.city_name)
            try:
                self.weatherform.la_population.setText(str(self.db.Germany.find_one({"city":f"{self.city_name}"})['population']))
            except:
                pass
            try:
                self.weatherform.la_population.setText(str(self.db.Netherland.find_one({"city":f"{self.city_name}"})['population']))
            except:
                pass
            try:
                self.weatherform.la_population.setText(str(self.db.USA.find_one({"city":f"{self.city_name}"})['population']))
            except:
                pass
            try:
                self.weatherform.la_region.setText(str(self.db.Germany.find_one({"city":f"{self.city_name}"})['region']))
            except:
                pass
            try:
                self.weatherform.la_region.setText(str(self.db.Netherland.find_one({"city":f"{self.city_name}"})['region']))
            except:
                pass
            try:
                self.weatherform.la_region.setText(str(self.db.USA.find_one({"city":f"{self.city_name}"})['region']))
            except:
                pass
    
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
            self.weatherform.table_cities.setItem(row, 1, QtWidgets.QTableWidgetItem(str(i["population"])))
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