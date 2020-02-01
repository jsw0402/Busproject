#url 불러오기
import requests
import xml.etree.ElementTree as ET
from api import *
def get_url(station):
    url=station

    response=requests.get(url)

    data=response.text

    root=ET.fromstring(data)

    return root
#정보추출해서 카테코리별로 정리
#병점역에서필요한자료 추가
def get_information(root):
    loNo1=[]
    loNo2=[]
    predic_time=[]
    predic_time2=[]
    route_id=[]
    plate_no=[]
    plate_no2=[]
    for locationNo1 in root.iter("locationNo1") :
        loNo1.append(locationNo1.text)

    for locationNo2 in root.iter("locationNo2") :
        loNo2.append(locationNo2.text)

    for predictTime1 in root.iter("predictTime1") :
        predic_time.append(predictTime1.text)
    
    for predictTime2 in root.iter("predictTime2") :
        predic_time2.append(predictTime2.text)

    for routeId in root.iter("routeId") :
        route_id.append(routeId.text)

    for plateNo1 in root.iter("plateNo1") :
        plate_no.append(plateNo1.text)
    
    for plateNo2 in root.iter("plateNo2") :
        plate_no2.append(plateNo2.text)
    
    return loNo1,loNo2,predic_time,route_id,plate_no,predic_time2,plate_no2
#701 상행하행구분:카카오버스로 실제 버스와비교결과 뒤에있는 701번이 병점역행
#필요한 노선별 index값 찾기
#class화
class bus_data():
    def __init__(self,route_id,loNo1,loNo2,predic_time,plate_no,predic_time2,plate_no2):
        self.route_id=route_id
        self.loNo1=loNo1
        self.loNo2=loNo2
        self.predic_time=predic_time
        self.predic_time2=predic_time2
        self.plate_no=plate_no
        self.plate_no2=plate_no2
    def setdata(self,route_id,loNo1,loNo2,predic_time,plate_no,predic_time2,plate_no2):
        self.route_id=route_id
        self.loNo1=loNo1
        self.loNo2=loNo2
        self.predic_time=predic_time
        self.predic_time2=predic_time2
        self.plate_no=plate_no
        self.plate_no2=plate_no2
    def data_701_ys(self):
        bus_701=[]
        for i,name in enumerate(self.route_id):
            if name=='223000032':
                bus_701.append(i)
        
        try:
            bus_701_data={'남은정류장':self.loNo1[bus_701[1]],'도착예정시간':self.predic_time[bus_701[1]],'버스번호':'701','차량번호':self.plate_no[bus_701[1]]}
        except IndexError :
            bus_701_data={'남은정류장':9999,'도착예정시간':9999,'버스번호':'701'}
        try:
            bus_701_2data={'남은정류장':self.loNo2[bus_701[1]],'도착예정시간':self.predic_time2[bus_701[1]],'버스번호':'701','차량번호':self.plate_no2[bus_701[1]]}
        except IndexError :
            bus_701_2data={'남은정류장':9999,'도착예정시간':9999,'버스번호':'701'}
        return bus_701_data,bus_701_2data
    
    def data_701(self):
        bus_701=[]
        for i,name in enumerate(self.route_id):
            if name=='223000032':
                bus_701.append(i)
        
        try:
            bus_701_data={'남은정류장':self.loNo1[bus_701[0]],'도착예정시간':self.predic_time[bus_701[0]],'버스번호':'701','차량번호':self.plate_no[bus_701[0]]}
        except IndexError :
            bus_701_data={'남은정류장':9999,'도착예정시간':9999,'버스번호':'701'}
        try:
            bus_701_2data={'남은정류장':self.loNo2[bus_701[0]],'도착예정시간':self.predic_time2[bus_701[0]],'버스번호':'701','차량번호':self.plate_no2[bus_701[0]]}
        except IndexError :
            bus_701_2data={'남은정류장':9999,'도착예정시간':9999,'버스번호':'701'}
        return bus_701_data,bus_701_2data
        
    def data_73(self):
        bus_73=[]
        for i,name in enumerate(self.route_id):
            if name=='223000058':
                bus_73.append(i)
        
        try:
            bus_73_data={'남은정류장':self.loNo1[bus_73[0]],'도착예정시간':self.predic_time[bus_73[0]],'버스번호':'73','차량번호':self.plate_no[bus_73[0]]}
        except IndexError :
            bus_73_data={'남은정류장':9999,'도착예정시간':9999,'버스번호':'73'}
        try:
            bus_73_2data={'남은정류장':self.loNo2[bus_73[0]],'도착예정시간':self.predic_time2[bus_73[0]],'버스번호':'73','차량번호':self.plate_no2[bus_73[0]]}
        except IndexError :
            bus_73_2data={'남은정류장':9999,'도착예정시간':9999,'버스번호':'73'}
        return bus_73_data,bus_73_2data
    
    def data_73_1(self):
        bus_73_1=[]
        for i,name in enumerate(self.route_id):
            if name=='233000130':
                bus_73_1.append(i)
        
        try:
            bus_73_1data={'남은정류장':self.loNo1[bus_73_1[0]],'도착예정시간':self.predic_time[bus_73_1[0]],'버스번호':'73-1','차량번호':self.plate_no[bus_73_1[0]]}
        except IndexError :
            bus_73_1data={'남은정류장':9999,'도착예정시간':9999,'버스번호':'73-1'}
        try:
            bus_73_1_2data={'남은정류장':self.loNo2[bus_73_1[0]],'도착예정시간':self.predic_time2[bus_73_1[0]],'버스번호':'73-1','차량번호':self.plate_no2[bus_73_1[0]]}
        except IndexError :
            bus_73_1_2data={'남은정류장':9999,'도착예정시간':9999,'버스번호':'73-1'}
        return bus_73_1data,bus_73_1_2data
    def data_34(self):
        bus_34=[]
        for i,name in enumerate(self.route_id):
            if name=='233000011':
                bus_34.append(i)
        
        try:
            bus_34data={'남은정류장':self.loNo1[bus_34[0]],'도착예정시간':self.predic_time[bus_34[0]],'버스번호':'34','차량번호':self.plate_no[bus_34[0]]}
        except IndexError :
            bus_34data={'남은정류장':9999,'도착예정시간':9999,'버스번호':'34'}
        try:
            bus_34_2data={'남은정류장':self.loNo2[bus_34[0]],'도착예정시간':self.predic_time2[bus_34[0]],'버스번호':'34','차량번호':self.plate_no2[bus_34[0]]}
        except IndexError :
            bus_34_2data={'남은정류장':9999,'도착예정시간':9999,'버스번호':'34'}
        return bus_34data,bus_34_2data
    
    def data_34_1(self):
        bus_34_1=[]
        for i,name in enumerate(self.route_id):
            if name=='233000012':
                bus_34_1.append(i)
        
        try:
            bus_34_1data={'남은정류장':self.loNo1[bus_34_1[0]],'도착예정시간':self.predic_time[bus_34_1[0]],'버스번호':'34-1','차량번호':self.plate_no[bus_34_1[0]]}
        except IndexError :
            bus_34_1data={'남은정류장':9999,'도착예정시간':9999,'버스번호':'34-1'}
        try:
            bus_34_1_2data={'남은정류장':self.loNo2[bus_34_1[0]],'도착예정시간':self.predic_time2[bus_34_1[0]],'버스번호':'34-1','차량번호':self.plate_no2[bus_34_1[0]]}
        except IndexError :
            bus_34_1_2data={'남은정류장':9999,'도착예정시간':9999,'버스번호':'34-1'}
        return bus_34_1data,bus_34_1_2data
    
    def data_46(self):
        bus_46=[]
        for i,name in enumerate(self.route_id):
            if name=='200000106':
                bus_46.append(i)
        
        try:
            bus_46data={'남은정류장':self.loNo1[bus_46[0]],'도착예정시간':self.predic_time[bus_46[0]],'버스번호':'46','차량번호':self.plate_no[bus_46[0]]}
        except IndexError :
            bus_46data={'남은정류장':9999,'도착예정시간':9999,'버스번호':'46'}
        try:
            bus_46_2data={'남은정류장':self.loNo2[bus_46[0]],'도착예정시간':self.predic_time2[bus_46[0]],'버스번호':'46','차량번호':self.plate_no2[bus_46[0]]}
        except IndexError :
            bus_46_2data={'남은정류장':9999,'도착예정시간':9999,'버스번호':'46'}
        return bus_46data,bus_46_2data
#예솔초정류장에서의 결과물
def yesol_output(bus_701_data,bus_73_data,bus_73_1_data):
    bustime=[int(bus_701_data['도착예정시간']),int(bus_73_data['도착예정시간']),int(bus_73_1_data['도착예정시간'])]
    fastbus_time=min(bustime)

    if fastbus_time==9999:
        fastbus_time='운행중인 버스가 없습니다'
        print(fastbus_time)
        return fastbus_time
    elif bustime[0]==fastbus_time:
        fastbus_data=bus_701_data
        print("도착예정버스:{}번".format(fastbus_data['버스번호']))
        print("도착예정시간:{}분".format(fastbus_data['도착예정시간']))
        print("남은정류장:{}개".format(fastbus_data['남은정류장']))
        return bus_701_data
    elif bustime[1]==fastbus_time:
        fastbus_data=bus_73_data
        print("도착예정버스:{}번".format(fastbus_data['버스번호']))
        print("도착예정시간:{}분".format(fastbus_data['도착예정시간']))
        print("남은정류장:{}개".format(fastbus_data['남은정류장']))
        return bus_73_data
    elif bustime[2]==fastbus_time:
        fastbus_data=bus_73_1_data
        print("도착예정버스:{}번".format(fastbus_data['버스번호']))
        print("도착예정시간:{}분".format(fastbus_data['도착예정시간']))
        print("남은정류장:{}개".format(fastbus_data['남은정류장']))
        return bus_73_1_data

#예솔초에서부터 중간정류장까지의 시간
def middle_time(x):
    if x['버스번호']=='701':
        root=get_url(hongbo)
        loNo1,loNo2,predic_time,route_id,plate_no,predic_time2,plate_no2=get_information(root)
        a=bus_data(route_id,loNo1,loNo2,predic_time,plate_no,predic_time2,plate_no2)
        bus_701_data,bus_701_2data=a.data_701()
        if bus_701_data['차량번호']==x['차량번호']:
            return bus_701_data['도착예정시간'],'701'
            
        elif bus_701_2data['차량번호']==x['차량번호']:
            return bus_701_2data['도착예정시간'],'701'
    
        else :
            pass



    elif x['버스번호']=='73':
        root=get_url(ys_yedang)
        loNo1,loNo2,predic_time,route_id,plate_no,predic_time2,plate_no2=get_information(root)
        a=bus_data(route_id,loNo1,loNo2,predic_time,plate_no,predic_time2,plate_no2)
        bus_73_data,bus_73_2data=a.data_73()
        if bus_73_data['차량번호']==x['차량번호']:
            return bus_73_data['도착예정시간'],'73'
        
        elif bus_73_2data['차량번호']==x['차량번호']:
            return bus_73_2data['도착예정시간'],'73'
            
        else :
            pass

    elif x['버스번호']=='73-1':
        root=get_url(ys_yedang)
        loNo1,loNo2,predic_time,route_id,plate_no,predic_time2,plate_no2=get_information(root)
        a=bus_data(route_id,loNo1,loNo2,predic_time,plate_no,predic_time2,plate_no2)
        bus_73_1_data,bus_73_1_2data=a.data_73_1()
        if bus_73_1_data['차량번호']==x['차량번호']:
            return bus_73_1_data['도착예정시간'],'73-1'
            
        elif bus_73_1_2data['차량번호']==x['차량번호']:
            return bus_73_1_2data['도착예정시간'],'73-1'
            
        else :
            pass    

def middle_time_home(x):
    if x['버스번호']=='701':
        root=get_url(bj_homeplus)
        loNo1,loNo2,predic_time,route_id,plate_no,predic_time2,plate_no2=get_information(root)
        a=bus_data(route_id,loNo1,loNo2,predic_time,plate_no,predic_time2,plate_no2)
        bus_701_data,bus_701_2data=a.data_701()
        if bus_701_data['차량번호']==x['차량번호']:
            return bus_701_data['도착예정시간'],'701'
            
        elif bus_701_2data['차량번호']==x['차량번호']:
            return bus_701_2data['도착예정시간'],'701'
    
        else :
            pass



    elif x['버스번호']=='73':
        root=get_url(bj_moa)
        loNo1,loNo2,predic_time,route_id,plate_no,predic_time2,plate_no2=get_information(root)
        a=bus_data(route_id,loNo1,loNo2,predic_time,plate_no,predic_time2,plate_no2)
        bus_73_data,bus_73_2data=a.data_73()
        if bus_73_data['차량번호']==x['차량번호']:
            return bus_73_data['도착예정시간'],'73'
        
        elif bus_73_2data['차량번호']==x['차량번호']:
            return bus_73_2data['도착예정시간'],'73'
            
        else :
            pass

    elif x['버스번호']=='73-1':
        root=get_url(bj_moa)
        loNo1,loNo2,predic_time,route_id,plate_no,predic_time2,plate_no2=get_information(root)
        a=bus_data(route_id,loNo1,loNo2,predic_time,plate_no,predic_time2,plate_no2)
        bus_73_1_data,bus_73_1_2data=a.data_73_1()
        if bus_73_1_data['차량번호']==x['차량번호']:
            return bus_73_1_data['도착예정시간'],'73-1'
            
        elif bus_73_1_2data['차량번호']==x['차량번호']:
            return bus_73_1_2data['도착예정시간'],'73-1'
            
        else :
            pass    