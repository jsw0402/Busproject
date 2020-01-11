#예솔초에서 탈 버스 정보
from yesol import *
from _byeongjeom import *
import time

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
    api=yedang

responseJson=get_Json_data(api)

result=bjtime(responseJson)


if api==honbo_time:
    x=result.dong_bj()
elif api==hanlim:
    x=result.yedang_bj()

yesol_bj_time=int(middle_time)+int(x)


x=time.localtime(time.time())
arr_time=(x.tm_hour,x.tm_min+yesol_bj_time)

if arr_time[1]>=60:
    arr_time=(x.tm_hour+1,x.tm_min+yesol_bj_time-60)
print(("병점역 도착예정시간은 {}시{}분입니다.").format(arr_time[0],arr_time[1]))




