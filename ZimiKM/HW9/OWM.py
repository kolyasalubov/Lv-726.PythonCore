from pyowm import OWM
import tkinter as tk

API_KEY = '5ce05306f258c7f4d0c42269582019d6'
HEIGHT = 350
WIDTH = 450

def weather_response():
  try:
    owm = OWM('5ce05306f258c7f4d0c42269582019d6')
    mgr = owm.weather_manager()
    user_city = entry_field.get()
    observation = mgr.weather_at_place(user_city)
    w = observation.weather
      
    w.detailed_status         
    w.wind()                  
    w.humidity                
    w.temperature('celsius')  
    w.rain                    
    w.heat_index              
    w.clouds                  
      
    label.config ( text = f"City: {user_city}\nConditions: {w.detailed_status }\nTemperature is {round(w.temperature('celsius')['temp'], 2)} C\nWind speed is {w.wind()['speed']} km/hours\nHumidity of the air is {w.humidity}" )
      
  except:
    label.config ( text = 'Smooth went wrong :{')


def get_weather():

  label['text'] = weather_response()



root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()



frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()