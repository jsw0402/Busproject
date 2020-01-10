#예솔초에서 탈 버스 정보
from yesol import *
import api
root=get_url(api.yesol_api)
loNo1,loNo2,predic_time,route_id,plate_no,predic_time2,plate_no2=get_information(root)
a=bus_data(route_id,loNo1,loNo2,predic_time,plate_no,predic_time2,plate_no2)
bus_701_data,bus_701_2data=a.data_701_ys()
bus_73_data,bus_73_2data=a.data_73()
bus_73_1_data,bus_73_1_2data=a.data_73_1()
x=yesol_output(bus_701_data,bus_73_data,bus_73_1_data)
#중간정류장

if x['버스번호']=='701':
    root=get_url(api.hongbo)
    loNo1,loNo2,predic_time,route_id,plate_no,predic_time2,plate_no2=get_information(root)
    a=bus_data(route_id,loNo1,loNo2,predic_time,plate_no,predic_time2,plate_no2)
    bus_701_data,bus_701_2data=a.data_701()
    if bus_701_data['차량번호']==x['차량번호']:
        predic_time_hongbo=bus_701_data['도착예정시간']
        print(predic_time_hongbo)
    elif bus_701_2data['차량번호']==x['차량번호']:
        predic_time_hongbo=bus_701_2data['도착예정시간']
        print(predic_time_hongbo)
    else :
        pass



elif x['버스번호']=='73':
    root=get_url(api.central)
    loNo1,loNo2,predic_time,route_id,plate_no,predic_time2,plate_no2=get_information(root)
    a=bus_data(route_id,loNo1,loNo2,predic_time,plate_no,predic_time2,plate_no2)
    bus_73_data,bus_73_2data=a.data_73()
    if bus_73_data['차량번호']==x['차량번호']:
        predic_time_centralpark=bus_73_data['도착예정시간']
        print(predic_time_centralpark)
    elif bus_73_2data['차량번호']==x['차량번호']:
        predic_time_centralpark=bus_73_2data['도착예정시간']
        print(predic_time_centralpark)
    else :
        pass

elif x['버스번호']=='73-1':
    root=get_url(api.central)
    loNo1,loNo2,predic_time,route_id,plate_no,predic_time2,plate_no2=get_information(root)
    a=bus_data(route_id,loNo1,loNo2,predic_time,plate_no,predic_time2,plate_no2)
    bus_73_1_data,bus_73_1_2data=a.data_73_1()
    if bus_73_1_data['차량번호']==x['차량번호']:
        predic_time_centralpark2=bus_73_1_data['도착예정시간']
        print(predic_time_centralpark2)
    elif bus_73_1_2data['차량번호']==x['차량번호']:
        predic_time_centralpark2=bus_73_1_2data['도착예정시간']
        print(predic_time_centralpark2)
    else :
        pass
