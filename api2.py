import requests

url="http://openapi.gbis.go.kr/ws/rest/busstationservice/searcharound?serviceKey=aT2lgQ3eq4GY4xrspJsvGHjXdJVHZxbGfq5dExmviAtuG9U7rZvEJA7U8BfYg30j%2BZP7wnKAE7XkTSFjOq9EZw%3D%3D&x=127.118991&y=37.195967"

response=requests.get(url)

data=response.text

import xml.etree.ElementTree as ET

root=ET.fromstring(data)

