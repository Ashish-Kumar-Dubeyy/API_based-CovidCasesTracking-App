import requests
import tkinter as tk

import datetime

def getcoviddata():
    api="https://disease.sh/v3/covid-19/all"
    json_data = requests.get(api).json()
    total_cases =str(json_data['cases'])
    total_deaths=str(json_data['deaths'])
    today_cases=str(json-data['todaycases'])
    today_recovered=str(json_data['todayrecovered'])
    updated_at=json_data('updated')
    dat=datetime.datetime.fromtimestamp(updatedat/le3)
    label.config(text='total cases'+total_cases
    +'\ntotaldeaths'+total_deaths+
    '\ntoday recovered'+today_recovred+
    '\ntoday cases'+today_cases+
    '\ntoday deaths'+ today_deaths)

    label2.config(text=date)
    print(total_cases)
    
canvas = tk.Tk()

canvas.geometry("400x400")
canvas.title("corona tracking app ")
f=("poppins",15,"bold")

button =tk.Button(canvas,fant=f,text="load",command=getcoviddata)
button.pack(pady=20)

label =tk.Label(canvas,font=f)
label.pack(pady=20)

label2=tk.Label(canvas,font =8)
label2.pack()
print('hell')
getcoviddata()
canvas.mainloop