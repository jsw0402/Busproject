#url 불러오기
import requests

def get_url():
    url=api.yesol_api

    response=requests.get(url)

    data=response.text

    root=ET.fromstring(data)

    return root


#정보추출해서 카테코리별로 정리
def get_information(root):
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
    
    return loNo1,loNo2,predic_time,route_id,plate_no
#내가탄 버스의 병점역 도착예정시간
bus_701=[]
bus_73=[]
bus_73_1=[]
for i,name in enumerate(plate_no):
    if name==api1_ys.bus_701_data['차량번호']:
        bus_701.append(i)
    
for i,name in enumerate(plate_no):
    if name==api1_ys.bus_701_data['차량번호']:
        bus_73.append(i)

for i,name in enumerate(plate_no):
    if name==api1_ys.bus_701_data['차량번호']:
        bus_73_1.append(i)

try:
    bus_701_data={'차량번호':plate_no[bus_701[1]]}
except IndexError :
    bus_701_data={'차량번호':"?"}
try:
    bus_73_data={'차량번호':plate_no[bus_73[0]]}
except IndexError :
    bus_73_data={'차량번호':"?"}
try:
    bus_73_1_data={'차량번호':plate_no[bus_73_1[0]]}
except IndexError :
    bus_73_1_data={'차량번호':"?"}


