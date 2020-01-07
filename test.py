#예솔초에서 탈 버스 정보
from yesol import *
import api
root=get_url(api.yesol_api)
loNo1,loNo2,predic_time,route_id,plate_no,predic_time2,plate_no2=get_information(root)
bus_701_data,bus_73_data,bus_73_1_data,bus_701_2data,bus_73_2data,bus_73_1_2data=bus_data(route_id,loNo1,loNo2,predic_time,plate_no,predic_time2,plate_no2)
ys_bus_data=yesol_output(bus_701_data,bus_73_data,bus_73_1_data)
print(bus_701_data,bus_73_data,bus_73_1_data,bus_701_2data,bus_73_2data,bus_73_1_2data)
root=get_url(api.byeongjeom)
loNo1,loNo2,predic_time,route_id,plate_no,predic_time2,plate_no2=get_information(root)
bus_701_data,bus_73_data,bus_73_1_data,bus_701_2data,bus_73_2data,bus_73_1_2data=bus_data_bj(route_id,loNo1,loNo2,predic_time,plate_no,predic_time2,plate_no2)
print(bus_701_data,bus_73_data,bus_73_1_data,bus_701_2data,bus_73_2data,bus_73_1_2data)