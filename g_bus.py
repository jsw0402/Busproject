import requests
import json

url='http://www.gbis.go.kr/gbis2014/schBusAPI.action'
data={'cmd':'searchRouteJson','routeId':'223000032'}
response=requests.post(url,data=data)
responseJson=json.loads(response.text)
stationId=[]
for i in range (len(responseJson['result']['gg']['up']['list'])):
    stationId.append(responseJson['result']['gg']['up']['list'][i]['stationId'])
for i in range (len(responseJson['result']['gg']['down']['list'])):
    stationId.append(responseJson['result']['gg']['down']['list'][i]['stationId'])

buslo=responseJson['result']['realTime']['list']

#
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

