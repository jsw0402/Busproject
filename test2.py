import requests
import json
from api import honbo_time

url=honbo_time

response=requests.get(url)

responseJson=json.loads(response.text)


print(responseJson['result']['path'][1]['subPath'][1]['lane'][0]['busNo'])