from yesol import *
root=get_url()
loNo1,loNo2,predic_time,route_id,plate_no=get_information(root)
bus_701_data,bus_73_data,bus_73_1_data=yesol_data(route_id,loNo1,loNo2,predic_time,plate_no)
yesol_output=yesol_output(bus_701_data,bus_73_data,bus_73_1_data)