import requests
from bs4 import BeautifulSoup as BS

url='https://m.map.naver.com/bus/lane.nhn?busID=16019#/text/88372'
root=requests.get(url)
soup=BS(root.content,'html.parser')
station_data=soup.select('li._station')
data=[]
for i in range(len(station_data)):
    if station_data[i].select('div.bus_pst _icon') in station_data[i]:
        data.append(station_data[i])
print(station_data[10])