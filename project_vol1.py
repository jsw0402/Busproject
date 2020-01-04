import api1_ys
import api1_bJ

bustime=[int(api1_ys.bus_701_data['도착예정시간']),int(api1_ys.bus_73_data['도착예정시간']),int(api1_ys.bus_73_1_data['도착예정시간'])]
fastbus_time=min(bustime)

for i in range(0,3):
    if fastbus_time==9999:
        fastbus_time='운행중인 버스가 없습니다'
    elif bustime[i]==fastbus_time:
        fastbus_data=api1_ys.bus_701_data
    elif bustime[i]==fastbus_time:
        fastbus_data=api1_ys.bus_73_data
    elif bustime[i]==fastbus_time:
        fastbus_data=api1_ys.bus_73_1_data
print("도착예정버스:{}번".format(fastbus_data['버스번호']))
print("도착예정시간:{}분".format(fastbus_data['도착예정시간']))
print("남은정류장:{}개".format(fastbus_data['남은정류장']))
    