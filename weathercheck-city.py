import requests

url = "https://api.openweathermap.org/data/2.5/weather"

name=input("Enter your city name: ")
args = {
    "q": name ,
    "appid": "0bcd5cd13c62ff00ae2964c040eb25a4",
    "units": "metric"
}

response = requests.get(url,params=args)
data = response.json()

if response.status_code == 200:
    print("temperature" ,data["main"]["temp"],"C")
elif response.status_code == 404:
    print(name, "not found")


