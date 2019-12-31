import requests

url="http://openapi.gbis.go.kr/ws/rest/busarrivalservice/station?serviceKey=aT2lgQ3eq4GY4xrspJsvGHjXdJVHZxbGfq5dExmviAtuG9U7rZvEJA7U8BfYg30j%2BZP7wnKAE7XkTSFjOq9EZw%3D%3D&stationId=233002421"

response=requests.get(url)

data=response.text

import xml.etree.ElementTree as ET

root=ET.fromstring(data)
for busArr in range(0,6):
    print([root[2][busArr][0].text]
