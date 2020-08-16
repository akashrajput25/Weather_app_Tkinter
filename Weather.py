from tkinter import *
from PIL import Image, ImageTk
import requests
import json

root = Tk()
root.title('Weather App Tkinter')
root.geometry('600x50')

#http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=89129&date=2020-08-16&distance=5&API_KEY=B6922580-F44C-490D-A578-34EF214744A6

try:
    api_req = requests.get("http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=93552&date=2020-08-16&distance=25&API_KEY=B6922580-F44C-490D-A578-34EF214744A6")
    api = json.loads(api_req.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']
    if category =="Good":
        weather_color ="#00e400"
    elif category =="Moderate":
        weather_color ="#ffff00"
    elif category =="Unhealthy for Sensitive Groups":
        weather_color ="#ff7e00"
    elif category =="Unhealthy":
        weather_color ="#ff0000"
    elif category =="Very Unhealthy":
        weather_color ="#8f3f97"
    elif category =="Hazardous":
        weather_color ="#7e0023"
    myLabel = Label(root , text = city +" Air Quality :" +str(quality) +"   "+category, font =("Helvetica",13),background = weather_color,fg='#fff')
    myLabel.pack()

    root.config(background = weather_color)

except Exception as e:
    api='error'

root.mainloop()
