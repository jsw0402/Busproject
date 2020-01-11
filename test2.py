import time
x=time.localtime(time.time())
nowtime=(x.tm_hour,x.tm_min+60)
if nowtime[1]>=60:
    nowtime=(x.tm_hour+1,x.tm_min)

