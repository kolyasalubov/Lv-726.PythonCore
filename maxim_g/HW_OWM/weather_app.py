from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

from tkinter import *

# ---------- FREE API KEY examples ---------------------
API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()


def get_weather():
    try:
        observation = mgr.weather_at_place(str(input_field.get().title()))
        w = observation.weather
        wd = {
            'wind': w.wind()['speed'],
            'temp': w.temperature('celsius')['temp'],
            'clouds': w.clouds,
            'status': w.detailed_status
        }
        msg = f"Weather info:\nWind is {wd['wind']}\nTemperature is {round(wd['temp'], 2)}\nClouds are {wd['clouds']}"
    except:
        msg = 'Sorry, city didn\'t find, try again with ather city!'
    return msg


def create_weather_report():
    weather_info_from_fiald = get_weather()
    message.config(text=weather_info_from_fiald)


window = Tk()
my_title = window.title('Weather program')
window.minsize(width=400, height=400)
window.config(padx=30, pady=30)

button = Button(text="Get weather info", command=create_weather_report)
button.grid(column=0, row=0)

input_field = Entry(width=30)
input_field.insert(END, string="Enter the city")
input_field.grid(column=1, row=0)

message = Message(window, text="information about city")
message.config(width=400, bg='lightgreen', padx=20, pady=20)
message.grid(columnspan=2, column=0, row=1)

window.mainloop()
