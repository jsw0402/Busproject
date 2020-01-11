#예솔초에서 탈 버스 정보
from yesol import *
from _byeongjeom import *

root=get_url(yesol_api)
loNo1,loNo2,predic_time,route_id,plate_no,predic_time2,plate_no2=get_information(root)
a=bus_data(route_id,loNo1,loNo2,predic_time,plate_no,predic_time2,plate_no2)
bus_701_data,bus_701_2data=a.data_701_ys()
bus_73_data,bus_73_2data=a.data_73()
bus_73_1_data,bus_73_1_2data=a.data_73_1()
x=yesol_output(bus_701_data,bus_73_data,bus_73_1_data)
#중간정류장

middle_time,bus_number=middle_time(x)
if bus_number=='701':
    api=honbo_time

elif bus_number=='73' or bus_number=='73-1':
    api=hanlim

responseJson=get_Json_data(api)

result=bjtime(responseJson)


if api==honbo_time:
    x=result.dong_bj()
elif api==hanlim:
    x=result.hanlim_bj()

yesol_bj_time=int(middle_time)+int(x)
print(yesol_bj_time)




