#url 불러오기
import requests

url="http://openapi.gbis.go.kr/ws/rest/busarrivalservice/station?serviceKey=aT2lgQ3eq4GY4xrspJsvGHjXdJVHZxbGfq5dExmviAtuG9U7rZvEJA7U8BfYg30j%2BZP7wnKAE7XkTSFjOq9EZw%3D%3D&stationId=233002421"

response=requests.get(url)

data=response.text

import xml.etree.ElementTree as ET

root=ET.fromstring(data)
#정보추출해서 카테코리별로 정리
loNo1=[]
loNo2=[]
predic_time=[]
route_id=[]
plate_no=[]
for locationNo1 in root.iter("locationNo1") :
    loNo1.append(locationNo1.text)

for locationNo2 in root.iter("locationNo2") :
    loNo2.append(locationNo2.text)

for predictTime1 in root.iter("predictTime1") :
    predic_time.append(predictTime1.text)

for routeId in root.iter("routeId") :
    route_id.append(routeId.text)

for plateNo1 in root.iter("plateNo1") :
    plate_no.append(plateNo1.text)
#701 상행하행구분:카카오버스로 실제 버스와비교결과 뒤에있는 701번이 병점역행
#필요한 노선별 index값 찾기
bus_701=[]
bus_73=[]
bus_73_1=[]
for i,name in enumerate(route_id):
    if name=='223000032':
        bus_701.append(i)
    
for i,name in enumerate(route_id):
    if name=='223000058':
        bus_73.append(i)

for i,name in enumerate(route_id):
    if name=='233000130':
        bus_73_1.append(i)

#노선별 최종 데이터정리
e="운행중인 버스가 없습니다"
try:
    bus_701_data={'남은정류장':loNo1[bus_701[1]],'도착예정시간':predic_time[bus_701[1]],'버스번호':'701','차량번호':plate_no[bus_701[1]]}
except IndexError :
    bus_701_data={'남은정류장':9999,'도착예정시간':9999,'버스번호':'?'}
try:
    bus_73_data={'남은정류장':loNo1[bus_73[0]],'도착예정시간':predic_time[bus_73[0]],'버스번호':'73','차량번호':plate_no[bus_73[0]]}
except IndexError :
    bus_73_data={'남은정류장':9999,'도착예정시간':9999,'버스번호':'?'}
try:
    bus_73_1_data={'남은정류장':loNo1[bus_73_1[0]],'도착예정시간':predic_time[bus_73_1[0]],'버스번호':'73-1','차량번호':plate_no[bus_73_1[0]]}
except IndexError :
    bus_73_1_data={'남은정류장':9999,'도착예정시간':9999,'버스번호':'?'}
