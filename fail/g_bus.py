import requests
import json
import time
import copy

def get_url(cmd,routeId):
    url='http://www.gbis.go.kr/gbis2014/schBusAPI.action'
    data={'cmd':cmd,'routeId':routeId}
    response=requests.post(url,data=data)
    responseJson=json.loads(response.text)
    return responseJson

responseJson=get_url('searchRouteJson','223000032')

time_data=[
    {
        'routeId':223000032,
        'data':[]
    },
    {
        'routeId':223000058,
        'data':[]
    },
    {
        'routeId':233000130,
        'data':[]
    }
]

for i in range(len(responseJson['result']['gg']['up'])):
    time_data[0]['data'].append({"stationId":responseJson['result']['gg']['up'][i]})
for i in range(len(responseJson['result']['gg']['down'])):
    time_data[0]['data'].append({"stationId":responseJson['result']['gg']['down'][i]})

while True :
    time.sleep(10)
    responseJson=get_url('searchRouteJson','223000032')
    b_responseJson=copy.copy(responseJson)
    responseJson=get_url('searchRouteJson','223000032')
    
    for i in range(len(b_responseJson['result']['realTime']['list'])):
        for z in range(len(responseJson['result']['realTime']['list'])):    
            if b_responseJson['result']['realTime']['list'][i]['busNo']==responseJson['result']['realTime']['list'][j]['busNo']:
                if b_responseJson['result']['realTime']['list'][i]['toStationId']==responseJson['result']['realTime']['list'][j]['fromStationId']:
                    time_data[]


