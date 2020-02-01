import time
import requests
import json
from datetime import datetime,timedelta

first_bus_time=datetime.now()
then=datetime(2020,1,18,17,17,00)
delta=first_bus_time-then
x=delta.total_seconds()
print(x)

url='https://map.kakao.com/bus/info.json?output=json&busline=B7672'
response=requests.get(url)
responseJson=json.loads(response.text)
y=len(responseJson['busStops'])
bus_time=[]
for i in range(y):
    bus_time.append([])
print(bus_time)
while True:
    time.sleep(15)
    before_resJson=responseJson
    url='https://map.kakao.com/bus/info.json?output=json&busline=B7672'
    response=requests.get(url)
    responseJson=json.loads(response.text)
    len_busloc_after=len(responseJson['busLocations'])
    len_busloc_before=len(before_resJson['busLocations'])
    for i in range(len_busloc_after):
        for j in range(len_busloc_before):
            if responseJson['busLocations'][i]['vehicleNumber']==before_resJson['busLocations'][j]['vehicleNumber']:
                if int(responseJson['busLocations'][i]["sectionOrder"])==before_resJson['busLocations'][j]["sectionOrder"]+1:
                    bus_time[responseJson['busLocations'][i]["sectionOrder"]-1].append(datetime.now())
    print(bus_time)
