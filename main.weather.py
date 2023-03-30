from PyQt5 import QtWidgets
import requests,pymongo
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Ui_weather import *
import pytz     # pip install pytz
import datetime
from geopy.geocoders import Nominatim  # pip install geopy
from timezonefinder import TimezoneFinder #pip install timezonefinder
import urllib

# initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")

class Main_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        
        super(Main_Window,self).__init__()
        self.weatherform=Ui_MainWindow()
        self.weatherform.setupUi(self)
        #To arrange background image for first opening
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        self.set_background("BackgroundImages\cristofer-maximilian-3_gzeydxuhc-unsplash.jpg")
        self.background_label.lower()
    
        self.client=pymongo.MongoClient('mongodb+srv://yunus:1234@cluster0.lytui3m.mongodb.net/?retryWrites=true&w=majority')
        self.db=self.client["WeatherApp"]
        self.city_germany=self.db["Germany"]
        self.city_holland=self.db["Netherland"]
        self.city_usa=self.db["USA"]
        self.show_weather_data_3()
        self.weatherform.table_cities.cellClicked.connect(self.show_weather_data)  #to click cell(cities) on QTableWidget 
        self.weatherform.but_search.clicked.connect(self.show_weather_data_2)    
        
 
        self.get_nl_citys()             #Default Country
        self.weatherform.but_usa.clicked.connect(self.get_usa_citys)  
        self.weatherform.but_gr.clicked.connect(self.get_gr_citys)
        self.weatherform.but_nl.clicked.connect(self.get_nl_citys)
    
    def set_background(self, path):
        self.background_label.setPixmap(QPixmap(path))
        pixmap = QPixmap(path)
        pixmap = pixmap.scaled(self.width(), self.height())
        self.background_label.setPixmap(pixmap)
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        self.background_label.lower()
             
        
    def show_weather_data(self): # Show weather condition of the city thats selected from table
        
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
                
                pressure=get_data_JSON["main"]["pressure"]
                country=get_data_JSON["sys"]["country"]
                icon=get_data_JSON["weather"][0]["icon"]
                icon_url = f"http://openweathermap.org/img/w/{icon}.png"
                icon_data = urllib.request.urlopen(icon_url).read()
                icon_pixmap = QPixmap()
                icon_pixmap.loadFromData(icon_data)
                self.weatherform.la_icon.setPixmap(icon_pixmap)
                
                location = geolocator.geocode(self.city_name)
                obj = TimezoneFinder()
                result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
                timezone = pytz.timezone(result)  # replace with the timezone of the city
                self.local_time = datetime.datetime.now(timezone)
                specific_time = datetime.datetime(self.local_time.year, self.local_time.month, self.local_time.day, hour=19, minute=0, second=0).time()
                self.weatherform.label.setText(self.local_time.strftime('%H:%M:%S'))

                if self.local_time.time() >= specific_time: #Setting a dynamic background images depending on both local time and description of weather
                    if description == "clear sky":
                        self.set_background('BackgroundImages\walkator-ZzdcWsmKMuU-unsplash.jpg')
                    elif description == "mist":
                        self.set_background('BackgroundImages\\aron-visuals-6sMGdkj3Ywg-unsplash.jpg')
                    elif description == "overcast clouds":
                        self.set_background('BackgroundImages\\richard-felix-V05SI4UtPBs-unsplash.jpg')
                    elif description == "rain" or description == "light rain":
                        self.set_background('BackgroundImages\severin-stalder-pe8ETR2u9h0-unsplash.jpg')
                
                    elif description == "broken clouds" or description =="scattered clouds" or description =="few clouds":
                        self.set_background("BackgroundImages\\nitish-meena-RbbdzZBKRDY-unsplash.jpg")
                        
                    elif description == "shower rain" or description == "intensity shower" or description == "moderate rain":
                        self.set_background("BackgroundImages\heavyrain_day.jpg")
                        
                    elif description == "thunderstorm":
                        self.set_background("BackgroundImages\\thunder_night.jpg")
                        
                    elif description == "snow":
                        self.set_background("BackgroundImages\snow_day2.jpg")
                        
                else:
                    if description == "clear sky":
                        self.set_background('BackgroundImages\cristofer-maximilian-3_gzeydxuhc-unsplash.jpg')
                    elif description == "mist":
                        self.set_background('BackgroundImages\mist_day.jpg')
                    elif description == "overcast clouds":
                        self.set_background('BackgroundImages\overcast_day3.jpg')
                    elif description == "rain" or description == "light rain":
                        self.set_background('BackgroundImages\\rain_day2.jpg')
                
                    elif description =="scattered clouds" or description =="few clouds":
                        self.set_background("BackgroundImages\overcast_day3.jpg")
                    elif description == "broken clouds":
                        self.set_background("BackgroundImages\\1e3b26afc18a3693832ef07890e841b9.jpg")
                    elif description == "shower rain" or description == "intensity shower" or description == "moderate rain":
                        self.set_background("BackgroundImages\heavyrain_day.jpg")
                        
                    elif description == "thunderstorm":
                        self.set_background("BackgroundImages\\thunder_day.jpg")
                        
                    elif description == "snow":
                        self.set_background("BackgroundImages\snowy_day.jpg")
                
                self.weatherform.la_temperature.setText(str(int(float(temp)-273.15))+"C°") #write the informations to the labels
                self.weatherform.la_description.setText(description)
                self.weatherform.la_pressure.setText(str(pressure))
                self.weatherform.la_country.setText(country)
                self.weatherform.la_city.setText(self.city_name)
                self.weatherform.la_population.setText(self.population)
                self.weatherform.la_region.setText(self.region)
                
            else:
                print("This country can not find, please enter correctly") 
            self.weatherform.la_hata.clear()            
        except :
            return

    def show_weather_data_2(self): #Show weather condition of the city in the line edit
        
        if not self.weatherform.li_city.text():
            self.weatherform.la_hata.setText("Please enter a valid city name") # show error message for invalid city name    
        
            return
        city_name = self.weatherform.li_city.text()
        query_result = self.city_germany.find_one({"city": city_name}) or \
                       self.city_holland.find_one({"city": city_name}) or \
                       self.city_usa.find_one({"city": city_name}) #check if the cities exist or not
    
        if not query_result:
            self.weatherform.la_hata.setText("City not found.")#If the city is not found, the label will display "City not found."
            self.weatherform.li_city.clear()
            return
        
       
        
       
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
            
            pressure=get_data_JSON["main"]["pressure"]
            country=get_data_JSON["sys"]["country"]
            icon=get_data_JSON["weather"][0]["icon"]
            icon_url = f"http://openweathermap.org/img/w/{icon}.png"
            icon_data = urllib.request.urlopen(icon_url).read()
            icon_pixmap = QPixmap()
            icon_pixmap.loadFromData(icon_data)
            self.weatherform.la_icon.setPixmap(icon_pixmap)
            
            location = geolocator.geocode(self.city_name)
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
            timezone = pytz.timezone(result)  # replace with the timezone of the city
            self.local_time = datetime.datetime.now(timezone)
            specific_time = datetime.datetime(self.local_time.year, self.local_time.month, self.local_time.day, hour=19, minute=0, second=0).time()
            self.weatherform.label.setText(self.local_time.strftime('%H:%M:%S'))

            if self.local_time.time() >= specific_time: #Setting a dynamic background images depending on both local time and description of weather
                if description == "clear sky":
                    self.set_background('BackgroundImages\walkator-ZzdcWsmKMuU-unsplash.jpg')
                elif description == "mist":
                    self.set_background('BackgroundImages\\aron-visuals-6sMGdkj3Ywg-unsplash.jpg')
                elif description == "overcast clouds":
                    self.set_background('BackgroundImages\\richard-felix-V05SI4UtPBs-unsplash.jpg')
                elif description == "rain" or description == "light rain":
                    self.set_background('BackgroundImages\severin-stalder-pe8ETR2u9h0-unsplash.jpg')
            
                elif description == "broken clouds" or description =="scattered clouds" or description =="few clouds":
                    self.set_background("BackgroundImages\\nitish-meena-RbbdzZBKRDY-unsplash.jpg")
                    
                elif description == "shower rain" or description == "intensity shower" or description == "moderate rain":
                    self.set_background("BackgroundImages\heavyrain_day.jpg")
                    
                elif description == "thunderstorm":
                    self.set_background("BackgroundImages\\thunder_night.jpg")
                    
                elif description == "snow":
                    self.set_background("BackgroundImages\snow_day2.jpg")
                    
            else:
                if description == "clear sky":
                    self.set_background('BackgroundImages\cristofer-maximilian-3_gzeydxuhc-unsplash.jpg')
                elif description == "mist":
                    self.set_background('BackgroundImages\mist_day.jpg')
                elif description == "overcast clouds":
                    self.set_background('BackgroundImages\overcast_day3.jpg')
                elif description == "rain" or description == "light rain":
                    self.set_background('BackgroundImages\\rain_day2.jpg')
            
                elif description =="scattered clouds" or description =="few clouds":
                        self.set_background("BackgroundImages\overcast_day3.jpg")
                elif description == "broken clouds":
                    self.set_background("BackgroundImages\\1e3b26afc18a3693832ef07890e841b9.jpg")
                
                elif description == "shower rain" or description == "intensity shower" or description == "moderate rain":
                    self.set_background("BackgroundImages\heavyrain_day.jpg")
                    
                elif description == "thunderstorm":
                    self.set_background("BackgroundImages\\thunder_day.jpg")
                    
                elif description == "snow":
                    self.set_background("BackgroundImages\snowy_day.jpg")
            
            self.weatherform.la_temperature.setText(str(int(float(temp)-273.15))+"C°")
            self.weatherform.la_description.setText(description)
            self.weatherform.la_pressure.setText(str(pressure))
            self.weatherform.la_country.setText(country)
            self.weatherform.la_city.setText(self.city_name)
            self.weatherform.la_hata.setText("") # clear error message if it was set previously
           #################### self.weatherform.la_region.setText(str(a))
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
        
        else:
           # if not result: # if the city is not found in one of the collections
              self.weatherform.la_hata.setText("Unknown City") 
              #print("hata")
              return
        self.weatherform.la_hata.clear()
        self.weatherform.li_city.setText("")
      
             #self.weatherform.la_hata.setText("Please enter a valid city name") # show error message for invalid city name 
        #self.weatherform.la_hata.clear()
           
    def show_weather_data_3(self):  #Show weather condition of the default city at the opening

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

            pressure=get_data_JSON["main"]["pressure"]
            country=get_data_JSON["sys"]["country"]
            icon=get_data_JSON["weather"][0]["icon"]
            icon_url = f"http://openweathermap.org/img/w/{icon}.png"
            icon_data = urllib.request.urlopen(icon_url).read()
            icon_pixmap = QPixmap()
            icon_pixmap.loadFromData(icon_data)
            self.weatherform.la_icon.setPixmap(icon_pixmap)

            location = geolocator.geocode(self.city_name)
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
            timezone = pytz.timezone(result)  # replace with the timezone of the city
            self.local_time = datetime.datetime.now(timezone)
            specific_time = datetime.datetime(self.local_time.year, self.local_time.month, self.local_time.day, hour=19, minute=0, second=0).time()
            self.weatherform.label.setText(self.local_time.strftime('%H:%M:%S'))
            # print(f"Current time in {self.city_name}: {self.local_time.strftime('%Y-%m-%d %H:%M:%S')}")
        
            if self.local_time.time() >= specific_time: #Setting a dynamic background images depending on both local time and description of weather
                if description == "clear sky":
                    self.set_background('BackgroundImages\walkator-ZzdcWsmKMuU-unsplash.jpg')
                elif description == "mist":
                    self.set_background('BackgroundImages\\aron-visuals-6sMGdkj3Ywg-unsplash.jpg')
                elif description == "overcast clouds":
                    self.set_background('BackgroundImages\\richard-felix-V05SI4UtPBs-unsplash.jpg')
                elif description == "rain" or description == "light rain":
                    self.set_background('BackgroundImages\severin-stalder-pe8ETR2u9h0-unsplash.jpg')
            
                elif description == "broken clouds" or description == "scattered clouds" or description =="few clouds":
                    self.set_background("BackgroundImages\\nitish-meena-RbbdzZBKRDY-unsplash.jpg")
                    
                elif description == "shower rain" or description == "intensity shower" or description == "moderate rain":
                    self.set_background("BackgroundImages\heavyrain_day.jpg")
                    
                elif description == "thunderstorm":
                    self.set_background("BackgroundImages\\thunder_night.jpg")
                    
                elif description == "snow":
                    self.set_background("BackgroundImages\snow_day2.jpg")
                    
            else:
                if description == "clear sky":
                    self.set_background('BackgroundImages\cristofer-maximilian-3_gzeydxuhc-unsplash.jpg')
                elif description == "mist":
                    self.set_background('BackgroundImages\mist_day.jpg')
                elif description == "overcast clouds":
                    self.set_background('BackgroundImages\overcast_day3.jpg')
                elif description == "rain" or description == "light rain":
                    self.set_background('BackgroundImages\\rain_day2.jpg')
            
                elif description =="scattered clouds" or description =="few clouds":
                        self.set_background("BackgroundImages\overcast_day3.jpg")
                elif description == "broken clouds":
                    self.set_background("BackgroundImages\\1e3b26afc18a3693832ef07890e841b9.jpg")
                    
                elif description == "shower rain" or description == "intensity shower" or description == "moderate rain":
                    self.set_background("BackgroundImages\heavyrain_day.jpg")
                    
                elif description == "thunderstorm":
                    self.set_background("BackgroundImages\\thunder_day.jpg")
                    
                elif description == "snow":
                    self.set_background("BackgroundImages\snowy_day.jpg")
            
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
    
    def get_usa_citys(self):   # to get the usa cities, region of the cities and the population to the tablewidget
        
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
        total_cities = self.weatherform.table_cities.rowCount()
        self.weatherform.la_total.setText("TOTAL CITIES:"+str(total_cities))
    def get_gr_citys(self): # to get the Germany cities, region of the cities and the population to the tablewidget 
        
        
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
        total_cities = self.weatherform.table_cities.rowCount()#count of the cities
        self.weatherform.la_total.setText("TOTAL CITIES:"+str(total_cities))  
    def get_nl_citys(self):       # to get the NL cities, region of the cities and the population to the tablewidget
        
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
        total_cities = self.weatherform.table_cities.rowCount()
        self.weatherform.la_total.setText("TOTAL CITIES:"+str(total_cities))
   
        

if __name__ == "__main__":
        app = QApplication(sys.argv)
        Main_Window = Main_Window()
        widget = QtWidgets.QStackedWidget()
        widget.addWidget(Main_Window)
        widget.setFixedHeight(900)
        widget.setFixedWidth(800)
        
        widget.show()
        
        try:
            sys.exit(app.exec_())
        
        except:
            print("Exit App")    