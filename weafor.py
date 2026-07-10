from tkinter import *
from tkinter import ttk, messagebox
import requests
import webbrowser
import urllib.parse

API_KEY = "39a75d5b40369ce3d9ef2702e1228d4b"

CITY_LIST = [
    "Ajmer", "Jaipur", "Jodhpur", "Udaipur", "Kota", "Bikaner", "Alwar", "Bharatpur",
    "Delhi", "Mumbai", "Pune", "Nagpur", "Nashik", "Bengaluru", "Mysuru", "Chennai",
    "Hyderabad", "Kolkata", "Ahmedabad", "Surat", "Vadodara", "Indore", "Bhopal",
    "Lucknow", "Kanpur", "Varanasi", "Patna", "Ranchi", "Guwahati", "Thiruvananthapuram"
]

def data_get():
    city = city_name.get().strip()

    if not city:
        messagebox.showwarning("Input Required", "Please select or type a city name.")
        return

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={urllib.parse.quote(city)}&appid={API_KEY}"
        response = requests.get(url, timeout=10)
        data = response.json()

        if data.get("cod") != 200:
            messagebox.showerror("Error", data.get("message", "City not found."))
            clear_fields()
            return

        weather_main = data["weather"][0]["main"]
        weather_desc = data["weather"][0]["description"].title()
        temp_c = round(data["main"]["temp"] - 273.15, 1)
        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        city_result.config(text=city.title())
        w_value.config(text=weather_main)
        desc_value.config(text=weather_desc)
        temp_value.config(text=f"{temp_c} °C")
        pressure_value.config(text=f"{pressure} hPa")
        humidity_value.config(text=f"{humidity} %")
        wind_value.config(text=f"{wind_speed} m/s")

        if weather_main in ["Clear", "Clouds"] and 10 < temp_c < 30 and humidity < 70:
            visit_status.config(text="Good weather for visiting", style="Good.TLabel")
        else:
            visit_status.config(text="Weather may not be ideal for visiting", style="Bad.TLabel")

    except requests.exceptions.RequestException:
        messagebox.showerror("Network Error", "Could not connect to the weather service.")
    except KeyError:
        messagebox.showerror("Data Error", "Unexpected response from weather service.")

def clear_fields():
    city_result.config(text="")
    w_value.config(text="-")
    desc_value.config(text="-")
    temp_value.config(text="-")
    pressure_value.config(text="-")
    humidity_value.config(text="-")
    wind_value.config(text="-")
    visit_status.config(text="", style="Good.TLabel")

def show_map():
    city = city_name.get().strip()
    if not city:
        messagebox.showwarning("Input Required", "Please select or type a city name.")
        return
    map_url = f"https://www.google.com/maps/search/{urllib.parse.quote(city)}"
    webbrowser.open(map_url)

def filter_cities(event=None):
    typed = city_name.get().strip().lower()
    if typed == "":
        city_box["values"] = CITY_LIST
    else:
        filtered = [city for city in CITY_LIST if typed in city.lower()]
        city_box["values"] = filtered

def on_city_select(event=None):
    city_name.set(city_box.get())

win = Tk()
win.title("EverWeather")
win.geometry("900x650")
win.state("zoomed")
win.minsize(900, 650)
win.configure(bg="#eaf3ff")

style = ttk.Style()
style.theme_use("clam")

style.configure("TFrame", background="#eaf3ff")
style.configure("Card.TFrame", background="white")
style.configure("Title.TLabel", background="#eaf3ff", foreground="#1f3c88",
                font=("Segoe UI", 28, "bold"))
style.configure("Sub.TLabel", background="#eaf3ff", foreground="#5c6f91",
                font=("Segoe UI", 11))
style.configure("CardTitle.TLabel", background="white", foreground="#1f3c88",
                font=("Segoe UI", 16, "bold"))
style.configure("Label.TLabel", background="white", foreground="#334155",
                font=("Segoe UI", 11))
style.configure("Value.TLabel", background="white", foreground="#0f172a",
                font=("Segoe UI", 12, "bold"))
style.configure("Good.TLabel", background="white", foreground="#15803d",
                font=("Segoe UI", 11, "bold"))
style.configure("Bad.TLabel", background="white", foreground="#b91c1c",
                font=("Segoe UI", 11, "bold"))
style.configure("TButton", font=("Segoe UI", 11, "bold"), padding=8)

main_frame = ttk.Frame(win, padding=25, style="TFrame")
main_frame.pack(fill="both", expand=True)

ttk.Label(main_frame, text="EverWeather", style="Title.TLabel").pack(pady=(10, 4))
ttk.Label(main_frame, text="Select a city or type your own to check live weather", style="Sub.TLabel").pack(pady=(0, 20))

card = ttk.Frame(main_frame, style="Card.TFrame", padding=25)
card.pack(fill="both", expand=True)
card.columnconfigure(0, weight=1)
card.columnconfigure(1, weight=1)

ttk.Label(card, text="Search City", style="CardTitle.TLabel").grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

city_name = StringVar()
city_box = ttk.Combobox(card, textvariable=city_name, values=CITY_LIST, font=("Segoe UI", 12))
city_box.grid(row=1, column=0, sticky="ew", padx=(0, 10), pady=(0, 15))
city_box.bind("<KeyRelease>", filter_cities)
city_box.bind("<<ComboboxSelected>>", on_city_select)
city_box.bind("<Return>", lambda e: data_get())

search_btn = ttk.Button(card, text="Search Weather", command=data_get)
search_btn.grid(row=1, column=1, sticky="ew", pady=(0, 15))

map_btn = ttk.Button(card, text="Show Map", command=show_map)
map_btn.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 20))

ttk.Label(card, text="Weather Details", style="CardTitle.TLabel").grid(row=3, column=0, columnspan=2, sticky="w", pady=(0, 10))

city_result = ttk.Label(card, text="", style="CardTitle.TLabel")
city_result.grid(row=4, column=0, columnspan=2, sticky="w", pady=(0, 12))

def add_row(r, label_text):
    ttk.Label(card, text=label_text, style="Label.TLabel").grid(row=r, column=0, sticky="w", pady=7)

add_row(5, "Weather")
w_value = ttk.Label(card, text="-", style="Value.TLabel")
w_value.grid(row=5, column=1, sticky="e", pady=7)

add_row(6, "Description")
desc_value = ttk.Label(card, text="-", style="Value.TLabel")
desc_value.grid(row=6, column=1, sticky="e", pady=7)

add_row(7, "Temperature")
temp_value = ttk.Label(card, text="-", style="Value.TLabel")
temp_value.grid(row=7, column=1, sticky="e", pady=7)

add_row(8, "Pressure")
pressure_value = ttk.Label(card, text="-", style="Value.TLabel")
pressure_value.grid(row=8, column=1, sticky="e", pady=7)

add_row(9, "Humidity")
humidity_value = ttk.Label(card, text="-", style="Value.TLabel")
humidity_value.grid(row=9, column=1, sticky="e", pady=7)

add_row(10, "Wind Speed")
wind_value = ttk.Label(card, text="-", style="Value.TLabel")
wind_value.grid(row=10, column=1, sticky="e", pady=7)

visit_status = ttk.Label(card, text="", style="Good.TLabel", wraplength=550, justify="center")
visit_status.grid(row=11, column=0, columnspan=2, sticky="ew", pady=(20, 0))

win.mainloop()