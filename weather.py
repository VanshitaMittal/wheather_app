import tkinter as tk
from tkinter import font
import PIL.Image
import PIL.ImageTk
import requests

API_KEY = '6a681cac28a4a5b1626f6986f7727b06' 

def test_function(entry):
    print("button clicked", entry)

def format_response(weather):
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temperature = weather['main']['temp']
        final_str = 'City: %s \nConditions: %s \nTemperature (C): %s' % (name, description, (temperature-32)*5//9)
    except:
        final_str = 'There was a problem retrieving that information.'

    return final_str

def get_weather(city):
    weather_key = API_KEY
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params)
    weather = response.json()
    format_response(weather)

    label['text'] = format_response(weather)


HEIGHT = 500
WIDTH = 600

root = tk.Tk()
root.title('Weather App')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)

im = PIL.Image.open("aws.jpg")
photo = PIL.ImageTk.PhotoImage(im)
background_label = tk.Label(root, image=photo)
background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

canvas.pack()

frame = tk.Frame(root, bg="steel blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 18))
entry.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Report", bg="light cyan", fg="black", font=('Courier', 12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='steel blue', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 18))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()