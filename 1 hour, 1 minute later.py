"""
1시간, 1분 뒤 출력
자정은 00:00
시간(h) : 0시부터 23시까지
분(m) : 00분부터 59분까지
23:59에서 1분 뒤 0:00
"""
time=input()
time=time.split(':')
h=int(time[0])+1
m=int(time[1])+1
if m==60:
    h+=1
    if h>=24:
        h=h-24
    print(f'{h}:00')
if h>=24:
    h=h-24
if m>=0 and m<=9:
    print(f'{h}:0{m}')
else: 
    if not m==60:
        print(f'{h}:{m}')
