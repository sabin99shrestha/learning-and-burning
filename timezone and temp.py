# import requests
# url1="https://api.api-ninjas.com/v1/worldtime"

# city=input("Enter city name: ")
# paras={
#     "q":city,
#     "appid":"bJYtEVMAlYlaT5mKnRiADnZuYwxP6DWGeYAxbz1s"


# }
# response = requests.get(url1,params=paras)
# data = response.json()

# print(data)
import requests

url = "https://api.timezonedb.com/v2.1/get-time-zone"

timezone=input("Enter timezone: ")

params = {
    "key": "bJYtEVMAlYlaT5mKnRiADnZuYwxP6DWGeYAxbz1s",
    "format": "json",
    "by": "zone",
    "timezone":timezone,
   
}

response = requests.get(url, params=params)
print(response.json())