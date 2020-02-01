#예솔초에서 탈 버스 정보
from yesol import *
from _byeongjeom import *
import time
from suwon import *
print("현재위치를 입력해 주세요.")
x=int(input("1.예솔초 2.병점역사거리 3.수원대 4.병점역 후문\n"))

if x==1:
    #예솔초정류장 api가공
    root=get_url(yesol_api)
    loNo1,loNo2,predic_time,route_id,plate_no,predic_time2,plate_no2=get_information(root)
    a=bus_data(route_id,loNo1,loNo2,predic_time,plate_no,predic_time2,plate_no2)
    #701번,73번,73-1번 버스 정보 가공
    bus_701_data,bus_701_2data=a.data_701_ys()
    bus_73_data,bus_73_2data=a.data_73()
    bus_73_1_data,bus_73_1_2data=a.data_73_1()
    #예솔초정류장에 가장빨리오는 버스정보
    x=yesol_output(bus_701_data,bus_73_data,bus_73_1_data)
    #중간정류장
    middle_time,bus_number=middle_time(x)
    #중간정류장으로부터 병점역까지의 시간구하기
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

    #총걸리는시간
    yesol_bj_time=int(middle_time)+int(x)

    #도착예정시간
    x=time.localtime(time.time())
    arr_time=(x.tm_hour,x.tm_min+yesol_bj_time)

    if arr_time[1]>=60:
        arr_time=(x.tm_hour+1,x.tm_min+yesol_bj_time-60)
    print(("병점역 도착예정시간은 {}시{}분입니다.").format(arr_time[0],arr_time[1]))


#병점역에서 수원대까지
elif x==2:
    #병점역사거리정류장 api가공
    root=get_url(byeongjeom)
    loNo1,loNo2,predic_time,route_id,plate_no,predic_time2,plate_no2=get_information(root)
    a=bus_data(route_id,loNo1,loNo2,predic_time,plate_no,predic_time2,plate_no2)
    #34번,34-1번,46번 버스 정보 가공
    bus_34data,bus_34_2data=a.data_34()
    bus_34_1data,bus_34_1_2data=a.data_34_1()
    bus_46data,bus_46_2data=a.data_46()
    #병점역사거리정류장에 가장빨리오는 버스정보
    x=suwon_output(bus_34data,bus_34_1data,bus_46data)
    #병점역사거리에서부터 수원대까지 걸리는시간
    arrive_time,bus_number=arrive_time(x)
    suwon_bj_time=int(arrive_time)
    #수원대 도착예정시간
    x=time.localtime(time.time())
    arr_time=(x.tm_hour,x.tm_min+suwon_bj_time)
    if arr_time[1]>=60:
        arr_time=(x.tm_hour+1,x.tm_min+suwon_bj_time-60)
    print(("수원대 도착예정시간은 {}시{}분입니다.").format(arr_time[0],arr_time[1]))

#수원대출발
elif x==3:
    #수원대 정류장api가공
    root=get_url(suwon)
    loNo1,loNo2,predic_time,route_id,plate_no,predic_time2,plate_no2=get_information(root)
    a=bus_data(route_id,loNo1,loNo2,predic_time,plate_no,predic_time2,plate_no2)
    #34번,34-1번,46번 버스 정보 가공
    bus_34data,bus_34_2data=a.data_34()
    bus_34_1data,bus_34_1_2data=a.data_34_1()
    bus_46data,bus_46_2data=a.data_46()
    #수원대 정류장에 가장빨리오는 버스정보
    x=suwon_output(bus_34data,bus_34_1data,bus_46data)
    #병점역후문에서 수원대까지 걸리는 시간
    arrive_time,bus_number=arrive_time(x)
    suwon_bj_time=int(arrive_time)
    #병점역 후문 도착예정시간
    x=time.localtime(time.time())
    arr_time=(x.tm_hour,x.tm_min+suwon_bj_time)
    if arr_time[1]>=60:
        arr_time=(x.tm_hour+1,x.tm_min+suwon_bj_time-60)
    print(("병점역 도착예정시간은 {}시{}분입니다.").format(arr_time[0],arr_time[1]))

#병점역 후문에서 집까지
elif x==4:
    #병점역 사거리api가공
    root=get_url(byeongjeom)
    loNo1,loNo2,predic_time,route_id,plate_no,predic_time2,plate_no2=get_information(root)
    a=bus_data(route_id,loNo1,loNo2,predic_time,plate_no,predic_time2,plate_no2)
    #701,73,73-1번 버스 정보 가공
    bus_701_data,bus_701_2data=a.data_701()
    bus_73_data,bus_73_2data=a.data_73()
    bus_73_1_data,bus_73_1_2data=a.data_73_1()
    #수원대 정류장에 가장빨리오는 버스정보
    x=yesol_output(bus_701_data,bus_73_data,bus_73_1_data)
    #중간정류장
    middle_time,bus_number=middle_time_home(x)
    #중간정류장으로부터 집까지 시간 구하기
    if bus_number=='701':
        api=bj_homeplus_time

    elif bus_number=='73' or bus_number=='73-1':
        api=bj_moa_time

    responseJson=get_Json_data(api)

    result=bjtime(responseJson)


    if api==bj_homeplus_time:
        x=result.dong_bj()
    elif api==bj_moa_time:
        x=result.yedang_bj()
    #집까지 걸리는 총시간
    yesol_bj_time=int(middle_time)+int(x)

    #도착예정시간
    x=time.localtime(time.time())
    arr_time=(x.tm_hour,x.tm_min+yesol_bj_time)

    if arr_time[1]>=60:
        arr_time=(x.tm_hour+1,x.tm_min+yesol_bj_time-60)
    print(("잡 도착예정시간은 {}시{}분입니다.").format(arr_time[0],arr_time[1]))