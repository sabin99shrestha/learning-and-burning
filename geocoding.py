from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()  # Load environment variables from .env file
url="https://api.api-ninjas.com/v1/geocoding"

city=input("Enter city name: ")
country=input("Enter country name: ")

api_key=os.getenv("GEOCODE_API_KEY")
params={
    "city":city,
    "country":country,

}
headers={
    "X-Api-Key":api_key
}
response = requests.get(url,params=params,headers=headers)
data=response.json()

if response.status_code == 200:
 print(json.dumps(data,indent=4)) # Pretty print the JSON response
elif response.status_code == 404:
    print(city, "not found")
