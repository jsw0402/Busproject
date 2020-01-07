#url 불러오기
import requests
import api
import xml.etree.ElementTree as ET
def get_url(station):
    url=station

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
#701 상행하행구분:카카오버스로 실제 버스와비교결과 뒤에있는 701번이 병점역행
#필요한 노선별 index값 찾기
def yesol_data(route_id,loNo1,loNo2,predic_time,plate_no):
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
    return bus_701_data,bus_73_data,bus_73_1_data

def yesol_output(bus_701_data,bus_73_data,bus_73_1_data):
    bustime=[int(bus_701_data['도착예정시간']),int(bus_73_data['도착예정시간']),int(bus_73_1_data['도착예정시간'])]
    fastbus_time=min(bustime)
    print(fastbus_time)
    print(bustime)
    print(bustime[0]==fastbus_time)

    if fastbus_time==9999:
        fastbus_time='운행중인 버스가 없습니다'
        print(fastbus_time)
    elif bustime[0]==fastbus_time:
        fastbus_data=bus_701_data
        print("도착예정버스:{}번".format(fastbus_data['버스번호']))
        print("도착예정시간:{}분".format(fastbus_data['도착예정시간']))
        print("남은정류장:{}개".format(fastbus_data['남은정류장']))
    elif bustime[1]==fastbus_time:
        fastbus_data=bus_73_data
        print("도착예정버스:{}번".format(fastbus_data['버스번호']))
        print("도착예정시간:{}분".format(fastbus_data['도착예정시간']))
        print("남은정류장:{}개".format(fastbus_data['남은정류장']))
    elif bustime[2]==fastbus_time:
        fastbus_data=bus_73_1_data
        print("도착예정버스:{}번".format(fastbus_data['버스번호']))
        print("도착예정시간:{}분".format(fastbus_data['도착예정시간']))
        print("남은정류장:{}개".format(fastbus_data['남은정류장']))