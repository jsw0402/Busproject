import requests
import json
from datetime import datetime,timedelta

url='https://map.kakao.com/bus/info.json?output=json&busline=B7672'
response=requests.get(url)
responseJson=json.loads(response.text)
x=len(responseJson['busLocations'])
y=len(responseJson['busStops'])
bus_time=[]
for i in range(y):
    bus_time.append([])
first_bus_time=datetime.now()
then=datetime(2020,1,17,16,23,00)
delta=first_bus_time-then

print(first_bus_time)
print(delta)
print(type(delta.total_seconds()))
for i in range(x):
    pass
    

        