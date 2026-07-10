# WeatherHub-Application

# EverWeather

EverWeather is a modern Python desktop weather application built with **Tkinter** and **ttkbootstrap**.  
It allows users to search for a city, view live weather details, open the location in Google Maps, and get a polished, user-friendly weather dashboard experience.

---

## Features

- Search weather by city name.
- Auto-suggest cities from a predefined list.
- Live weather details from OpenWeather API.
- Displays:
  - Weather condition
  - Description
  - Temperature
  - Pressure
  - Humidity
  - Wind speed
- Weather-based visit suggestion:
  - Shows whether the weather is good for visiting or not.
- Open location in Google Maps.
- Clean and responsive desktop UI.
- Modern ttkbootstrap styling.
- Error handling for empty input, invalid city names, and network issues.

---

## Tech Stack

- **Python**
- **Tkinter**
- **ttkbootstrap**
- **Requests**
- **OpenWeather API**
- **Webbrowser**
- **urllib.parse**

---

## Requirements

Install the required packages before running the project:

```bash
pip install requests ttkbootstrap
```

If you are using only standard Tkinter styling, ttkbootstrap is optional, but this project is designed to look better with it.

---

## API Used

This project uses the **OpenWeather Current Weather API**.

### API Endpoint
```text
https://api.openweathermap.org/data/2.5/weather
```

### Parameters Used
- `q` = city name
- `appid` = your OpenWeather API key
- `units` = metric or imperial

### Temperature Unit
- `metric` returns temperature in **Celsius**
- `imperial` returns temperature in **Fahrenheit**
- Without units, OpenWeather returns **Kelvin** by default [web:79][web:80].

---

## Project Structure

```text
EverWeather/
│
├── weafor.py
├── README.md
├── screenshots/
│   └── home.png
└── requirements.txt
```

---

## How to Run

1. Clone or download the project.
2. Open the project folder in terminal or PowerShell.
3. Install dependencies:

```bash
pip install requests ttkbootstrap
```

4. Run the application:

```bash
python weafor.py
```

If you are using `py` launcher:

```bash
py weafor.py
```

---

## How It Works

### 1. City Selection
The user can type a city name or select one from the dropdown list.

### 2. Weather Fetching
When the Search button is clicked, the app sends a request to the OpenWeather API and receives real-time weather data.

### 3. Data Display
The app extracts:
- weather condition,
- description,
- temperature,
- pressure,
- humidity,
- and wind speed,

then displays them on the interface.

### 4. Visit Recommendation
The app checks the weather conditions and gives a simple recommendation:
- “Good weather for visiting”
- or
- “Weather may not be ideal for visiting”

### 5. Google Maps
The Show Map button opens the searched city in Google Maps.

---

## UI Design

The interface is designed to be:
- clean,
- modern,
- easy to read,
- and suitable for a college project or portfolio demo.

It uses:
- light background colors,
- card-style layout,
- bold headings,
- modern fonts,
- and nicely spaced widgets.

---

## Error Handling

The app handles common issues such as:
- empty city input,
- invalid city names,
- no internet connection,
- unexpected API responses.

This prevents the app from crashing and improves usability.

---

## Future Improvements

You can extend this project by adding:
- weather icons,
- 5-day forecast,
- hourly forecast,
- dark mode,
- voice search,
- recent searches,
- favorite cities,
- sunrise/sunset time,
- AQI,
- humidity gauge,
- temperature charts,
- PDF export,
- and live clock.

---

## Notes

- Make sure your OpenWeather API key is valid.
- If the API returns temperature in Kelvin, convert it to Celsius using:

```python
temp_c = temp_k - 273.15
```

- Better option: use `units=metric` in the API request to directly receive Celsius [web:80][web:83].

---

## License

This project is created for educational and personal use.

---

## Author

Developed as a Python desktop weather project using Tkinter and OpenWeather API.
