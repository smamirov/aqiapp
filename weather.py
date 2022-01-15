from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("Checkboxes")
root.geometry('600x150')

'''
https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=94597&distance=5&API_KEY=572C51D3-7A22-4133-BEEC-A84CC463323C
'''

def zipLookUp():
    try:
        apiRequest = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode.get() + "&distance=5&API_KEY=572C51D3-7A22-4133-BEEC-A84CC463323C")
        api = json.loads(apiRequest.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weatherColor = "#00e400"
        elif category == "Moderate":
            weatherColor = "#ffff00"
        elif category == "Unhealthy for Sensitive Groups":
            weatherColor = "#ff7e00"
        elif category == "Unhealthy":
            weatherColor = "#ff0000"
        elif category == "Very Unhealthy":
            weatherColor = "#8f3f97"
        elif category == "Hazardous":
            weatherColor = "#7e0023"
        
        root.configure(background=weatherColor)

        myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20), background=weatherColor)
        myLabel.grid(row=3, column=0)
        #myLabel.forget()
    except Exception as e:
        api = "Error...."


zipcode = Entry(root, justify=LEFT)
zipcode.grid(row=1, column=0, padx=10, pady=10, sticky=W)

zipcodeButton = Button(root, text="Lookup Zipcode", command=zipLookUp, justify=LEFT)
zipcodeButton.grid(row=2, column=0, padx=10, sticky=W)

root.mainloop()