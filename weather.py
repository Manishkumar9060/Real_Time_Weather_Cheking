import tkinter as tk
from tkinter import ttk, messagebox
import requests
from datetime import datetime

# Function to get weather
def get_weather():
    city = city_combo.get()
    api_key = "6d165c50ffdbc97******************"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            messagebox.showerror("Error", data.get("message", "Unknown error"))
            return

        city_name = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        weather_desc = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        result_label.config(
            text=(
                f"🌍 {city_name}, {country}\n"
                f"🌡 Temp: {temp}°C (Feels like {feels_like}°C)\n"
                f"☁ Weather: {weather_desc.capitalize()}\n"
                f"💧 Humidity: {humidity}%\n"
                f"💨 Wind Speed: {wind_speed} m/s\n"
                f"🕒 Last Updated: {last_updated}"
            )
        )

    except Exception as e:
        messagebox.showerror("Error", f"Failed to retrieve data: {e}")

# GUI Setup
root = tk.Tk()
root.title("Real-Time Weather Application 🌦")
root.geometry("600x600")
root.resizable(False, False)
root.configure(bg="#e6f2ff")

# Dropdown for popular cities
tk.Label(root, text="Select City:", font=("Arial", 12, "bold"), bg="#e6f2ff").pack(pady=10)
cities = ["London", "New York", "Delhi", "Mumbai", "Paris", "Tokyo", "Sydney", "Berlin", "Dubai", "Sitamarhi", "Patna", "Bihar"]
city_combo = ttk.Combobox(root, values=cities, font=("Arial", 12))
city_combo.pack(pady=5)
city_combo.set("Enter/Select City")  # Default city

# Button
tk.Button(root, text="Check Weather", command=get_weather, bg="#1ee145", fg="white",
          font=("Arial", 12, "bold"), relief="raised").pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#EAEEF1", justify="left", fg="#e11e1e")
result_label.pack(pady=10)

root.mainloop()
