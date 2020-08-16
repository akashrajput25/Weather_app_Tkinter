from tkinter import *
from PIL import Image, ImageTk
import requests
import json

root = Tk()
root.title('Weather App Tkinter')
root.geometry('600x100')

#create functn for looking zip codes
def ziplookup():
    #ziplabel = Label(root, text = zip.get())
    #ziplabel.grid(row=2 , column =0 ,columnspan =2)

    try:
        api_req = requests.get("http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode="+zip.get()+"&date=2020-08-16&distance=25&API_KEY=B6922580-F44C-490D-A578-34EF214744A6")
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
        myLabel.grid(row=1 , column =0 ,columnspan=2)

        root.config(background = weather_color)

    except Exception as e:
        api='error'

zip = Entry(root)
zip.grid(row=0,column=0 ,stick =W+E+N+S)

zipbtn = Button(root, text ="Lookup ZipCode", command=ziplookup )
zipbtn.grid(row=0,column=1 ,pady=10,stick =W+E+N+S)

root.mainloop()
