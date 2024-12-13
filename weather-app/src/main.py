import tkinter as tk
from tkinter import messagebox
from weather.weather_service import WeatherService

def get_weather():
    city = city_entry.get()
    api_key = "e453df6c2a80ef4b95ec6f6e7a94dfac"
    weather_service = WeatherService(api_key)
    weather_data = weather_service.get_weather(city)

    if weather_data:
        weather_info = weather_service.parse_weather_data(weather_data)
        display_weather(weather_info)
    else:
        messagebox.showerror("Error", "Weather data not available for the specified city.")

def display_weather(weather_info):
    result = (
        f"City: {weather_info['city']}\n"
        f"Temperature: {weather_info['temperature']}°C\n"
        f"Description: {weather_info['description']}\n"
        f"Humidity: {weather_info['humidity']}%\n"
        f"Wind Speed: {weather_info['wind_speed']} m/s"
    )
    result_label.config(text=result)

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create and place the widgets
city_label = tk.Label(root, text="Enter the city name:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.pack()

# Run the application
root.mainloop()