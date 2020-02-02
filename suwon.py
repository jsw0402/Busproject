from api import *
from yesol import *
# 수원대에 가장빨리온는 버스정보

def suwon_output(bus_34data,bus_34_1data,bus_46data):
    bustime=[int(bus_34data['도착예정시간']),int(bus_34_1data['도착예정시간']),int(bus_46data['도착예정시간'])]
    fastbus_time=min(bustime)

    if fastbus_time==9999:
        fastbus_time='운행중인 버스가 없습니다'
        print(fastbus_time)
        return fastbus_time
    elif bustime[0]==fastbus_time:
        fastbus_data=bus_34data
        print("도착예정버스:{}번".format(fastbus_data['버스번호']))
        print("도착예정시간:{}분".format(fastbus_data['도착예정시간']))
        print("남은정류장:{}개".format(fastbus_data['남은정류장']))
        return bus_34data
    elif bustime[1]==fastbus_time:
        fastbus_data=bus_34_1data
        print("도착예정버스:{}번".format(fastbus_data['버스번호']))
        print("도착예정시간:{}분".format(fastbus_data['도착예정시간']))
        print("남은정류장:{}개".format(fastbus_data['남은정류장']))
        return bus_34_1data
    elif bustime[2]==fastbus_time:
        fastbus_data=bus_46data
        print("도착예정버스:{}번".format(fastbus_data['버스번호']))
        print("도착예정시간:{}분".format(fastbus_data['도착예정시간']))
        print("남은정류장:{}개".format(fastbus_data['남은정류장']))
        return bus_46data
    #내가탄버스가 병점역에 도착하는 시간
def arrive_time(x):
    if x['버스번호']=='34':
        root=get_url(suwon_bj)
        loNo1,loNo2,predic_time,route_id,plate_no,predic_time2,plate_no2=get_information(root)
        a=bus_data(route_id,loNo1,loNo2,predic_time,plate_no,predic_time2,plate_no2)
        bus_34data,bus_34_2data=a.data_34()
        if bus_34data['차량번호']==x['차량번호']:
            return bus_34data['도착예정시간'],'34'
            
        elif bus_34_2data['차량번호']==x['차량번호']:
            return bus_34_2data['도착예정시간'],'34'
    
        else :
            pass
    
    elif x['버스번호']=='34-1':
        root=get_url(suwon_bj)
        loNo1,loNo2,predic_time,route_id,plate_no,predic_time2,plate_no2=get_information(root)
        a=bus_data(route_id,loNo1,loNo2,predic_time,plate_no,predic_time2,plate_no2)
        bus_34_1data,bus_34_1_2data=a.data_34_1()
        if bus_34_1data['차량번호']==x['차량번호']:
            return bus_34_1data['도착예정시간'],'34-1'
            
        elif bus_34_1_2data['차량번호']==x['차량번호']:
            return bus_34_1_2data['도착예정시간'],'34-1'
    
        else :
            pass

    elif x['버스번호']=='46':
        root=get_url(suwon_bj)
        loNo1,loNo2,predic_time,route_id,plate_no,predic_time2,plate_no2=get_information(root)
        a=bus_data(route_id,loNo1,loNo2,predic_time,plate_no,predic_time2,plate_no2)
        bus_46data,bus_46_2data=a.data_46()
        if bus_46data['차량번호']==x['차량번호']:
            return bus_46data['도착예정시간'],'46'
            
        elif bus_46_2data['차량번호']==x['차량번호']:
            return bus_46_2data['도착예정시간'],'46'
    
        else :
            pass

def arrive_time_bj_suwon(x):
    if x['버스번호']=='34':
        root=get_url(bj_suwon)
        loNo1,loNo2,predic_time,route_id,plate_no,predic_time2,plate_no2=get_information(root)
        a=bus_data(route_id,loNo1,loNo2,predic_time,plate_no,predic_time2,plate_no2)
        bus_34data,bus_34_2data=a.data_34()
        if bus_34data['차량번호']==x['차량번호']:
            return bus_34data['도착예정시간'],'34'
            
        elif bus_34_2data['차량번호']==x['차량번호']:
            return bus_34_2data['도착예정시간'],'34'
    
        else :
            pass
    
    elif x['버스번호']=='34-1':
        root=get_url(bj_suwon)
        loNo1,loNo2,predic_time,route_id,plate_no,predic_time2,plate_no2=get_information(root)
        a=bus_data(route_id,loNo1,loNo2,predic_time,plate_no,predic_time2,plate_no2)
        bus_34_1data,bus_34_1_2data=a.data_34_1()
        if bus_34_1data['차량번호']==x['차량번호']:
            return bus_34_1data['도착예정시간'],'34-1'
            
        elif bus_34_1_2data['차량번호']==x['차량번호']:
            return bus_34_1_2data['도착예정시간'],'34-1'
    
        else :
            pass

    elif x['버스번호']=='46':
        root=get_url(bj_suwon)
        loNo1,loNo2,predic_time,route_id,plate_no,predic_time2,plate_no2=get_information(root)
        a=bus_data(route_id,loNo1,loNo2,predic_time,plate_no,predic_time2,plate_no2)
        bus_46data,bus_46_2data=a.data_46()
        if bus_46data['차량번호']==x['차량번호']:
            return bus_46data['도착예정시간'],'46'
            
        elif bus_46_2data['차량번호']==x['차량번호']:
            return bus_46_2data['도착예정시간'],'46'
    
        else :
            pass


    