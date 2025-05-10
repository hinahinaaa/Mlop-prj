from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
from geopy.geocoders import ArcGIS
import requests
import pytz
import threading

from map_input import open_map, get_selected_location
from voice_input import voice_command
from welcome import init_assistance, speak, get_time, welcome

def update_clock():
    current_time = datetime.now().strftime("%I:%M %p")
    clock.config(text=current_time)
    root.after(1000, update_clock)

def on_window_open():
    update_clock()
    welcome(assistance)

def open_map_and_get_weather():
    # Mở cửa sổ bản đồ
    selected_location = open_map()

    # Nếu người dùng đã chọn một vị trí trên bản đồ
    if selected_location:
        city_name = selected_location.address.split(",")[-3]
        textfield.delete(0, tk.END)
        textfield.insert(0, city_name)
        speak(assistance, f"Confirm location selected: {city_name}")
        getWeather()


def getWeather():
    try:
        city = textfield.get()

        geolocator = ArcGIS()
        location = geolocator.geocode(city)
        print(location)

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        print(result)
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # Weather
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=7a2cf28ff543bc7246652ebe4ecc767b&units=metric"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'])
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp, "°C"))
        c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°C"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry")

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False) 

#VA xin chào
assistance = init_assistance()
get_time()

#nhận diện giọng nói
def voice_query():
    thread = threading.Thread(target=activate_microphone)
    thread.start()

# Mở mic và bắt đầu thu âm
def activate_microphone():
    speak(assistance, 'Please speak the name of the city you want to check the weather for.')
    query = voice_command(assistance, textfield)
    if query:
        # Đặt giá trị của textfield thành tên thành phố từ giọng nói
        textfield.delete(0, tk.END)
        textfield.insert(0, query)
        speak(assistance, f"I will check the weather for {query}. Please wait.")
        getWeather()

#search box
Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root, justify="center", width=17, font=("poppins",25,"bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon1=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=Search_icon1,borderwidth=0, cursor="hand2", bg="#404040",command=getWeather)
myimage_icon.place(x=400, y=34)

Search_icon2=PhotoImage(file="microphone.png")
myimage_icon=Button(image=Search_icon2,borderwidth=0, cursor="hand2", bg="#404040",command=voice_query)
myimage_icon.place(x=350, y=40)

Search_icon3=PhotoImage(file="marking.png")
myimage_icon=Button(image=Search_icon3,borderwidth=0, cursor="hand2", bg="#404040",command=open_map_and_get_weather)
myimage_icon.place(x=50, y=40)

#logo
Logo_image=PhotoImage(file="logo.png")
logo=Label(image=Logo_image)
logo.place(x=300, y=100)

#bottom box
Frame_image=PhotoImage(file="box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5,side=BOTTOM)


#label
label1=Label(root,text="WIND", font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY", font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)

label3=Label(root,text="DESCRIPTION", font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4=Label(root,text="PRESSURE", font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)



w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)
d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=430,y=430)
p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)

# Time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=50, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=50, y=130)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=600, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=600, y=250)

def open_window():
    root.deiconify()
    on_window_open()

root.withdraw()
root.after(100, open_window)

root.mainloop()