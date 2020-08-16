from tkinter import *
from PIL import Image, ImageTk
import requests
import json

root = Tk()
root.title('Weather App Tkinter')
root.geometry('400x50')
root.config(background = 'green')

#http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=89129&date=2020-08-16&distance=5&API_KEY=B6922580-F44C-490D-A578-34EF214744A6

try:
    api_req = requests.get("http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=89129&date=2020-08-16&distance=5&API_KEY=B6922580-F44C-490D-A578-34EF214744A6")
    api = json.loads(api_req.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']

except Exception as e:
    api='error'

myLabel = Label(root , text = city +" Air Quality :" +str(quality) +"   "+category, font =("Helvetica",15),background = 'green',fg='#fff')
myLabel.pack()
root.mainloop()
