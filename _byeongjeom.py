import requests
import json
from api import honbo_time,hanlim

def get_Json_data(api):
    url=api

    response=requests.get(url)

    responseJson=json.loads(response.text)

    return responseJson


class bjtime():
    def __init__(self,responseJson):
        self.responseJson=responseJson
    
    
    def dong_bj(self):
        x=[]
        for i in range(0,len(self.responseJson['result']['path'])):
            x.append(self.responseJson['result']['path'][i]['subPath'][1]['lane'][0]['busNo'])
        for a in enumerate(x):
            if a[1]=='701':
                bus_index=a[0]

        return self.responseJson['result']['path'][bus_index]['subPath'][1]['sectionTime']
        
    def yedang_bj(self):
        x=[]
        for i in range(0,len(self.responseJson['result']['path'])):
            x.append(self.responseJson['result']['path'][i]['subPath'][1]['lane'][0]['busNo'])
        for a in enumerate(x):
            if a[1]=='73':
                bus_index=a[0]
            elif a[1]=='73-1':
                bus_index=a[0]

        return self.responseJson['result']['path'][bus_index]['subPath'][1]['sectionTime']
        




