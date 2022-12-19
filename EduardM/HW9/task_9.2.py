import tkinter as tk
from tkinter import font
from pyowm import OWM
import datetime


# ---------- FREE API KEY examples ---------------------
API_KEY = 'ef2206ff5da67de63306d0b143e20872'


def weather_response(city):
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()

    # Search for current weather in city and get details
    observation = mgr.weather_at_place(city)
    w = observation.weather
    cur_time = datetime.datetime.now().strftime("%d %B %Y %H:%M")
    return (f"Time: {cur_time}\n"
            f"City: {city.title()}\n\n"
            f"Conditions: {w.detailed_status }\n"
            f"Temperature: {round(w.temperature('celsius')['temp'], 2)} C \n"
            f"Wind speed: {w.wind()['speed']} km/hours\n"
            f"Humidity of the air: {w.humidity}")


def get_weather(city: str):
    label['text'] = weather_response(city)


HEIGHT = 350
WIDTH = 450

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="lightgoldenrod", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75,
            relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="steel blue", fg="snow",
                   font=('Courier', 10),
                   command=lambda: get_weather(entry_field.get()),
                   cursor='hand2')
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='royal blue', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75,
                  relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 12))
label.place(relx=0, rely=0, relwidth=1, relheight=1)
root.mainloop()
