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


