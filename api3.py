import requests

url="http://openapi.gbis.go.kr/ws/rest/busstationservice/route?serviceKey=aT2lgQ3eq4GY4xrspJsvGHjXdJVHZxbGfq5dExmviAtuG9U7rZvEJA7U8BfYg30j%2BZP7wnKAE7XkTSFjOq9EZw%3D%3D&stationId=233002421"
response=requests.get(url)

data=response.text

import xml.etree.ElementTree as ET

root=ET.fromstring(data)

route_id=[]
route_name=[]
for routeId in root.iter("routeId"):
    route_id.append(routeId.text)

for routeName in root.iter("routeName"):
    route_name.append(routeName.text)

print(route_id)
print(route_name)