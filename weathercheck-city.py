from dotenv import load_dotenv
import requests
import os

load_dotenv("api.env")
url = "https://api.openweathermap.org/data/2.5/weather"
api_key=os.getenv("API_KEY")
print(api_key)
name=input("Enter your city name: ")
args = {
    "q": name ,
    "units": "metric",
    "appid": api_key
}

response = requests.get(url,params=args)
data = response.json()

if response.status_code == 200:
    print("temperature" ,data["main"]["temp"],"C")
elif response.status_code == 404:
    print(name, "not found")


