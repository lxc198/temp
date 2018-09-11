import time
#最后一个ID的时间
st = '2018-09-11 13:14:50'
t = time.strptime(st,'%Y-%m-%d %H:%M:%S')
r = time.mktime(t)
r = int(r)*1000
'28800000'
#下一个起始id
next_id = r + 28800000